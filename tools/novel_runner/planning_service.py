"""故事单元与 3～5 章细纲批次的模型规划闭环。"""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

from .api_runtime import invoke_provider, mark_task_accepted
from .batching import BatchingError, partition_chapters
from .config import validate_run_directory
from .master_plan import (
    MasterPlanError,
    master_plan_slice,
    next_rough_unit,
    require_approved_master_plan,
)
from .outline_validation import (
    OutlineValidationError,
    ensure_comedy_rotation,
    ensure_unit_contracts,
)
from .plan_import import (
    PlanImportError,
    validate_chapter_outlines,
    validate_story_units,
)
from .prompt_composer import (
    compose_batch_outline_plan_prompt,
    compose_story_unit_plan_prompt,
)
from .provider import GenerationRequest, ProviderError, TextProvider
from .storage import (
    StorageError,
    atomic_write_json,
    atomic_write_text,
    read_json,
    resolve_run_dir,
    run_lock,
)


class PlanningServiceError(RuntimeError):
    """故事单元或章纲批次不能进入正式运行数据。"""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_context(
    root: Path, run_id: str
) -> tuple[Path, dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    report = validate_run_directory(root, run_id)
    if not report.valid:
        details = "; ".join(f"{item.path}: {item.message}" for item in report.issues)
        raise PlanningServiceError(f"运行配置无效：{details}")
    run_dir = resolve_run_dir(root, run_id)
    return (
        run_dir,
        read_json(run_dir / "run.json"),
        read_json(run_dir / "planning/story-units.json"),
        read_json(run_dir / "planning/chapter-outlines.json"),
    )


def _next_version(directory: Path, prefix: str, suffix: str) -> int:
    versions: list[int] = []
    for path in directory.glob(f"{prefix}.v*.{suffix}"):
        middle = path.name.removeprefix(f"{prefix}.v").removesuffix(f".{suffix}")
        if middle.isdigit():
            versions.append(int(middle))
    return max(versions, default=0) + 1


def _parse_json_object(text: str, label: str) -> dict[str, Any]:
    stripped = text.lstrip("\ufeff \t\r\n")
    try:
        data, end = json.JSONDecoder().raw_decode(stripped)
    except json.JSONDecodeError as exc:
        raise PlanningServiceError(
            f"{label}不是有效 JSON：第 {exc.lineno} 行第 {exc.colno} 列"
        ) from exc
    remainder = stripped[end:].strip()
    if remainder and any(character not in "}] \t\r\n" for character in remainder):
        raise PlanningServiceError(f"{label}在 JSON 对象后包含额外文本")
    if not isinstance(data, dict):
        raise PlanningServiceError(f"{label}必须是 JSON 对象")
    return data


def plan_story_unit(
    root: Path,
    run_id: str,
    chapter_count: int | None,
    provider: TextProvider,
) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        run_dir, run, units, _ = _load_context(root, run_id)
        try:
            master_plan = require_approved_master_plan(root, run_id)
        except MasterPlanError as exc:
            raise PlanningServiceError(str(exc)) from exc
        if chapter_count is not None and (
            not isinstance(chapter_count, int) or isinstance(chapter_count, bool)
        ):
            raise PlanningServiceError("chapter_count 必须是整数")
        active = [
            unit
            for unit in units
            if unit.get("status") in {"planned", "running", "paused"}
        ]
        if active:
            raise PlanningServiceError(
                f"已有未完成故事单元：{active[0].get('unit_id')}"
            )
        try:
            rough_unit = next_rough_unit(master_plan, units)
            context_slice = master_plan_slice(master_plan, rough_unit["unit_id"])
        except MasterPlanError as exc:
            raise PlanningServiceError(str(exc)) from exc
        unit_id = rough_unit["unit_id"]
        start, end = rough_unit["chapter_range"]
        expected_start = int(run.get("last_committed_chapter", 0)) + 1
        if start != expected_start:
            raise PlanningServiceError(
                f"全书总纲下一单元从第 {start} 章开始，但运行指针要求第 {expected_start} 章"
            )
        planned_count = end - start + 1
        if chapter_count is not None and chapter_count != planned_count:
            raise PlanningServiceError(
                f"--chapters 必须与全书总纲中的 {unit_id} 一致：应为 {planned_count} 章"
            )
        prompt = compose_story_unit_plan_prompt(
            root,
            run_dir,
            unit_id,
            start,
            end,
            context_slice,
        )
        planning_dir = run_dir / "planning/generated"
        prefix = f"story-unit-{unit_id}"
        version = _next_version(planning_dir, prefix, "json")
        prompt_path = planning_dir / f"{prefix}.prompt.v{version}.md"
        raw_path = planning_dir / f"{prefix}.v{version}.json"
        atomic_write_text(prompt_path, prompt)
        request = GenerationRequest(
            task="plan_story_unit",
            prompt=prompt,
            metadata={
                "run_id": run_id,
                "unit_id": unit_id,
                "start_chapter": start,
                "end_chapter": end,
            },
        )
        try:
            response = invoke_provider(
                run_dir,
                provider,
                request,
                prompt_path=prompt_path,
                output_path=raw_path,
            )
        except ProviderError as exc:
            raise PlanningServiceError(str(exc)) from exc
        candidate = _parse_json_object(response.text, "故事单元输出")
        if candidate.get("unit_id") != unit_id:
            raise PlanningServiceError("故事单元输出 unit_id 与请求不一致")
        if candidate.get("chapter_range") != [start, end]:
            raise PlanningServiceError("故事单元输出 chapter_range 与请求不一致")
        try:
            normalized, _ = validate_story_units([candidate], run)
        except PlanImportError as exc:
            raise PlanningServiceError(str(exc)) from exc
        unit = normalized[0]
        for existing in units:
            chapter_range = existing.get("chapter_range")
            if not isinstance(chapter_range, list) or len(chapter_range) != 2:
                continue
            if max(start, chapter_range[0]) <= min(end, chapter_range[1]):
                raise PlanningServiceError("新故事单元与已有章节范围重叠")
        mark_task_accepted(run_dir, request, response, raw_path)
        units.append(unit)
        atomic_write_json(run_dir / "planning/story-units.json", units)
        atomic_write_json(planning_dir / f"{prefix}.final.json", unit)
        atomic_write_json(
            run_dir / "run.json",
            {
                **run,
                "status": "planning",
                "current_story_unit": unit_id,
                "updated_at": _utc_now(),
            },
        )
        return unit


def _find_unit(units: list[dict[str, Any]], unit_id: str) -> dict[str, Any]:
    matches = [item for item in units if item.get("unit_id") == unit_id]
    if len(matches) != 1:
        raise PlanningServiceError(f"故事单元 {unit_id} 不存在或重复")
    return matches[0]


def _request_chunks(start: int, end: int, size: int) -> tuple[tuple[int, int], ...]:
    if size <= 0:
        raise PlanningServiceError("outline_request_chunk_size 必须大于 0")
    chunks: list[tuple[int, int]] = []
    cursor = start
    while cursor <= end:
        chunk_end = min(end, cursor + size - 1)
        chunks.append((cursor, chunk_end))
        cursor = chunk_end + 1
    return tuple(chunks)


def plan_chapter_batch(
    root: Path,
    run_id: str,
    unit_id: str,
    start_chapter: int,
    end_chapter: int,
    provider: TextProvider,
) -> list[dict[str, Any]]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        run_dir, run, units, outlines = _load_context(root, run_id)
        try:
            require_approved_master_plan(root, run_id)
        except MasterPlanError as exc:
            raise PlanningServiceError(str(exc)) from exc
        unit = _find_unit(units, unit_id)
        unit_range = unit.get("chapter_range")
        if not isinstance(unit_range, list) or len(unit_range) != 2:
            raise PlanningServiceError("故事单元 chapter_range 无效")
        policy = run["policies"]["batch"]
        try:
            canonical = partition_chapters(
                unit_range[0],
                unit_range[1],
                minimum=policy["ledger_batch_min"],
                maximum=policy["ledger_batch_max"],
                preferred=policy["outline_batch_size"],
            )
        except BatchingError as exc:
            raise PlanningServiceError(str(exc)) from exc
        if (start_chapter, end_chapter) not in {
            (batch.start, batch.end) for batch in canonical
        }:
            raise PlanningServiceError("请求范围不是当前故事单元的标准章纲批次")
        existing = [
            item
            for item in outlines
            if isinstance(item.get("number"), int)
            and start_chapter <= item["number"] <= end_chapter
        ]
        if existing:
            if len(existing) == end_chapter - start_chapter + 1:
                return sorted(existing, key=lambda item: item["number"])
            raise PlanningServiceError("目标批次已有部分章纲，禁止覆盖或混合生成")

        planning_dir = run_dir / "planning/generated"
        prefix = f"outline-{start_chapter:04d}-{end_chapter:04d}"
        version = _next_version(planning_dir, prefix, "json")
        logical_prompt = compose_batch_outline_plan_prompt(
            root, run_dir, unit, start_chapter, end_chapter, outlines
        )
        atomic_write_text(
            planning_dir / f"{prefix}.prompt.v{version}.md", logical_prompt
        )
        chunk_size = int(policy.get("outline_request_chunk_size", end_chapter - start_chapter + 1))
        batch_outlines: list[dict[str, Any]] = []
        accepted_parts: list[
            tuple[GenerationRequest, Any, Path]
        ] = []
        raw_parts: list[dict[str, Any]] = []
        chunks = list(_request_chunks(start_chapter, end_chapter, chunk_size))
        chunk_index = 0
        while chunk_index < len(chunks):
            chunk_start, chunk_end = chunks[chunk_index]
            prompt = compose_batch_outline_plan_prompt(
                root, run_dir, unit, chunk_start, chunk_end, [*outlines, *batch_outlines]
            )
            part_prefix = (
                f"{prefix}.part-{chunk_start:04d}-{chunk_end:04d}"
            )
            prompt_path = planning_dir / f"{part_prefix}.prompt.v{version}.md"
            raw_path = planning_dir / f"{part_prefix}.v{version}.json"
            atomic_write_text(prompt_path, prompt)
            request = GenerationRequest(
                task="plan_chapter_batch",
                prompt=prompt,
                metadata={
                    "run_id": run_id,
                    "unit_id": unit_id,
                    "start_chapter": chunk_start,
                    "end_chapter": chunk_end,
                    "batch_start_chapter": start_chapter,
                    "batch_end_chapter": end_chapter,
                },
            )
            try:
                response = invoke_provider(
                    run_dir,
                    provider,
                    request,
                    prompt_path=prompt_path,
                    output_path=raw_path,
                )
            except ProviderError as exc:
                if (
                    chunk_start < chunk_end
                    and (
                        exc.status_code == 524
                        or exc.error_code == "transport_error"
                    )
                ):
                    midpoint = (chunk_start + chunk_end) // 2
                    chunks[chunk_index : chunk_index + 1] = [
                        (chunk_start, midpoint),
                        (midpoint + 1, chunk_end),
                    ]
                    continue
                raise PlanningServiceError(str(exc)) from exc
            data = _parse_json_object(
                response.text,
                f"章纲批次第 {chunk_start}～{chunk_end} 章输出",
            )
            chunk_outlines = data.get("chapter_outlines")
            expected_numbers = list(range(chunk_start, chunk_end + 1))
            if not isinstance(chunk_outlines, list):
                raise PlanningServiceError("章纲批次输出缺少 chapter_outlines 数组")
            actual_numbers = [
                item.get("number") if isinstance(item, dict) else None
                for item in chunk_outlines
            ]
            if sorted(actual_numbers) != expected_numbers:
                raise PlanningServiceError(
                    f"章纲分片必须恰好覆盖 {expected_numbers}，当前为 {actual_numbers}"
                )
            batch_outlines.extend(chunk_outlines)
            accepted_parts.append((request, response, raw_path))
            raw_parts.append(
                {
                    "chapter_range": [chunk_start, chunk_end],
                    "output": data,
                }
            )
            chunk_index += 1
        expected_batch_numbers = list(range(start_chapter, end_chapter + 1))
        if sorted(item.get("number") for item in batch_outlines) != expected_batch_numbers:
            raise PlanningServiceError(
                f"章纲批次必须恰好覆盖 {expected_batch_numbers}"
            )
        atomic_write_json(
            planning_dir / f"{prefix}.v{version}.json",
            {"parts": raw_parts},
        )
        ranges = {unit_id: (unit_range[0], unit_range[1])}
        try:
            normalized = validate_chapter_outlines(
                batch_outlines, ranges, run, require_complete=False
            )
            combined = sorted([*outlines, *normalized], key=lambda item: item["number"])
            ensure_comedy_rotation(combined, unit_range[0], unit_range[1])
            ensure_unit_contracts(unit, combined)
        except (PlanImportError, OutlineValidationError) as exc:
            raise PlanningServiceError(str(exc)) from exc
        for request, response, raw_path in accepted_parts:
            mark_task_accepted(run_dir, request, response, raw_path)
        atomic_write_json(run_dir / "planning/chapter-outlines.json", combined)
        atomic_write_json(
            planning_dir / f"{prefix}.final.json",
            {
                "unit_id": unit_id,
                "chapter_range": [start_chapter, end_chapter],
                "chapter_outlines": normalized,
                "created_at": _utc_now(),
            },
        )
        return normalized
