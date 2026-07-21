"""把工作流产出的机器计划安全导入运行目录。"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from typing import Any

from .batching import BatchingError, partition_chapters
from .config import validate_run_directory
from .outline_validation import (
    OutlineValidationError,
    ensure_comedy_rotation,
    ensure_outline_valid,
    ensure_unit_contracts,
)
from .storage import (
    atomic_write_json,
    atomic_write_text,
    read_json,
    resolve_run_dir,
    run_lock,
)


class PlanImportError(RuntimeError):
    """机器计划不完整或不符合当前运行策略。"""


JSON_FENCE_RE = re.compile(r"```json\s*(.*?)```", re.IGNORECASE | re.DOTALL)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_payload(source: Path) -> tuple[dict[str, Any], str]:
    try:
        text = source.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise PlanImportError(f"无法读取计划文件：{source}：{exc}") from exc
    candidates = [text] if source.suffix.lower() == ".json" else JSON_FENCE_RE.findall(text)
    parsed: list[dict[str, Any]] = []
    for candidate in candidates:
        try:
            value = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict) and {
            "story_units",
            "chapter_outlines",
        }.issubset(value):
            parsed.append(value)
    if len(parsed) != 1:
        raise PlanImportError(
            "计划文件必须包含且只能包含一个带 story_units 和 chapter_outlines 的 JSON 对象"
        )
    return parsed[0], text


def _require_text(item: dict[str, Any], key: str, prefix: str) -> None:
    if not isinstance(item.get(key), str) or not item[key].strip():
        raise PlanImportError(f"{prefix}.{key} 必须是非空字符串")


def validate_story_units(
    units: Any, run_config: dict[str, Any]
) -> tuple[list[dict[str, Any]], dict[str, tuple[int, int]]]:
    if not isinstance(units, list) or not units:
        raise PlanImportError("story_units 必须是非空数组")
    policy = run_config["policies"]["batch"]
    normalized: list[dict[str, Any]] = []
    ranges: dict[str, tuple[int, int]] = {}
    occupied: set[int] = set()
    list_fields = (
        "entry_state",
        "closing_state",
        "progression_change",
        "resource_change",
        "relationship_change",
        "comedy_plan",
        "must_not_resolve",
        "beats",
    )
    text_fields = (
        "unit_id",
        "goal",
        "main_obstacle",
        "required_setback",
        "required_payoff",
    )
    for index, unit in enumerate(units):
        prefix = f"story_units[{index}]"
        if not isinstance(unit, dict):
            raise PlanImportError(f"{prefix} 必须是对象")
        for key in text_fields:
            _require_text(unit, key, prefix)
        unit_id = unit["unit_id"]
        if unit_id in ranges:
            raise PlanImportError(f"故事单元 ID 重复：{unit_id}")
        chapter_range = unit.get("chapter_range")
        if (
            not isinstance(chapter_range, list)
            or len(chapter_range) != 2
            or not all(
                isinstance(value, int) and not isinstance(value, bool)
                for value in chapter_range
            )
        ):
            raise PlanImportError(f"{prefix}.chapter_range 必须是两个整数")
        start, end = chapter_range
        count = end - start + 1
        if start <= 0 or end < start:
            raise PlanImportError(f"{prefix}.chapter_range 无效")
        if not policy["story_unit_min"] <= count <= policy["story_unit_max"]:
            raise PlanImportError(
                f"{prefix} 必须覆盖 {policy['story_unit_min']}～"
                f"{policy['story_unit_max']} 章，当前为 {count} 章"
            )
        overlap = occupied.intersection(range(start, end + 1))
        if overlap:
            raise PlanImportError(f"故事单元章节范围重叠：{sorted(overlap)}")
        occupied.update(range(start, end + 1))
        for key in list_fields:
            if not isinstance(unit.get(key), list):
                raise PlanImportError(f"{prefix}.{key} 必须是数组")
        for key in ("closing_state", "progression_change", "comedy_plan", "must_not_resolve", "beats"):
            if not unit[key]:
                raise PlanImportError(f"{prefix}.{key} 必须是非空数组")
        status = unit.get("status", "planned")
        if status != "planned":
            raise PlanImportError(f"{prefix}.status 导入时必须是 planned")
        normalized.append({**unit, "status": "planned"})
        ranges[unit_id] = (start, end)
    return normalized, ranges


def validate_chapter_outlines(
    outlines: Any,
    units: dict[str, tuple[int, int]],
    run_config: dict[str, Any],
    *,
    require_complete: bool = True,
) -> list[dict[str, Any]]:
    if not isinstance(outlines, list):
        raise PlanImportError("chapter_outlines 必须是数组")
    if not outlines:
        return []
    numbers: set[int] = set()
    chapter_ids: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for index, outline in enumerate(outlines):
        prefix = f"chapter_outlines[{index}]"
        if not isinstance(outline, dict):
            raise PlanImportError(f"{prefix} 必须是对象")
        number = outline.get("number")
        if not isinstance(number, int) or isinstance(number, bool):
            raise PlanImportError(f"{prefix}.number 必须是整数")
        if number in numbers:
            raise PlanImportError(f"章节编号重复：{number}")
        numbers.add(number)
        chapter_id = outline.get("chapter_id")
        if not isinstance(chapter_id, str) or not chapter_id.strip():
            raise PlanImportError(f"{prefix}.chapter_id 必须是非空字符串")
        if chapter_id in chapter_ids:
            raise PlanImportError(f"章节 ID 重复：{chapter_id}")
        chapter_ids.add(chapter_id)
        unit_id = outline.get("story_unit_id")
        if unit_id not in units:
            raise PlanImportError(f"{prefix}.story_unit_id 未引用已导入故事单元")
        start, end = units[unit_id]
        if not start <= number <= end:
            raise PlanImportError(f"第 {number} 章不在故事单元 {unit_id} 的范围内")
        candidate = {**outline, "status": "outline_ready"}
        try:
            ensure_outline_valid(candidate, run_config)
        except OutlineValidationError as exc:
            raise PlanImportError(f"第 {number} 章章纲无效：{exc}") from exc
        normalized.append(candidate)

    if require_complete:
        expected = {
            number
            for start, end in units.values()
            for number in range(start, end + 1)
        }
        missing = sorted(expected - numbers)
        extra = sorted(numbers - expected)
        if missing or extra:
            raise PlanImportError(f"章纲范围不完整：缺少 {missing}，越界 {extra}")
    for unit_id, (start, end) in units.items():
        try:
            ensure_comedy_rotation(normalized, start, end)
        except OutlineValidationError as exc:
            raise PlanImportError(f"故事单元 {unit_id} 喜剧轮换无效：{exc}") from exc
    return sorted(normalized, key=lambda item: item["number"])


def _validate_imported_batch_coverage(
    ranges: dict[str, tuple[int, int]],
    outlines: list[dict[str, Any]],
    run_config: dict[str, Any],
) -> None:
    policy = run_config["policies"]["batch"]
    numbers = {item["number"] for item in outlines}
    for unit_id, (start, end) in ranges.items():
        try:
            batches = partition_chapters(
                start,
                end,
                minimum=policy["ledger_batch_min"],
                maximum=policy["ledger_batch_max"],
                preferred=policy["outline_batch_size"],
            )
        except BatchingError as exc:
            raise PlanImportError(str(exc)) from exc
        encountered_empty = False
        for batch in batches:
            present = [
                number
                for number in range(batch.start, batch.end + 1)
                if number in numbers
            ]
            if not present:
                encountered_empty = True
                continue
            if len(present) != batch.size:
                raise PlanImportError(
                    f"章纲范围不完整：标准批次第 {batch.start}～{batch.end} 章"
                    f"只包含 {present}"
                )
            if encountered_empty:
                raise PlanImportError(
                    f"故事单元 {unit_id} 的已导入章纲必须从首批连续覆盖"
                )


def import_plan(root: Path, run_id: str, source: Path) -> dict[str, Any]:
    payload, source_text = _load_payload(source)
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        report = validate_run_directory(root, run_id)
        if not report.valid:
            details = "; ".join(
                f"{issue.path}: {issue.message}" for issue in report.issues
            )
            raise PlanImportError(f"运行配置无效：{details}")
        run = read_json(run_dir / "run.json")
        existing_outlines = read_json(run_dir / "planning/chapter-outlines.json")
        if run.get("last_committed_chapter", 0) != 0:
            raise PlanImportError("已有正式提交章节，禁止整体重新导入计划")
        if isinstance(existing_outlines, list) and any(
            item.get("status") not in {"planned", "outline_ready"}
            for item in existing_outlines
            if isinstance(item, dict)
        ):
            raise PlanImportError("现有章节已开始生成，禁止整体重新导入计划")

        units, ranges = validate_story_units(payload.get("story_units"), run)
        outlines = validate_chapter_outlines(
            payload.get("chapter_outlines"),
            ranges,
            run,
            require_complete=False,
        )
        _validate_imported_batch_coverage(ranges, outlines, run)
        for unit in units:
            try:
                ensure_unit_contracts(unit, outlines)
            except OutlineValidationError as exc:
                raise PlanImportError(
                    f"故事单元 {unit['unit_id']} 契约无效：{exc}"
                ) from exc
        source_hash = hashlib.sha256(source_text.encode("utf-8")).hexdigest()
        import_record = {
            "schema_version": "1.0",
            "source_name": source.name,
            "source_sha256": source_hash,
            "story_unit_count": len(units),
            "chapter_count": len(outlines),
            "imported_at": _utc_now(),
        }
        atomic_write_json(run_dir / "planning/import-plan.json", payload)
        atomic_write_text(run_dir / "planning/import-source.md", source_text)
        atomic_write_json(run_dir / "planning/story-units.json", units)
        atomic_write_json(run_dir / "planning/chapter-outlines.json", outlines)
        first_unit = min(units, key=lambda item: item["chapter_range"][0])
        updated_run = {
            **run,
            "status": "ready" if outlines else "planning",
            "current_story_unit": first_unit["unit_id"],
            "updated_at": _utc_now(),
            "last_plan_import": import_record,
        }
        atomic_write_json(run_dir / "run.json", updated_run)
        atomic_write_json(run_dir / "planning/import-record.json", import_record)
        return import_record
