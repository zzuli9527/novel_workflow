"""Unit validation, budgets, status transitions, and shared lookups."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..api_runtime import load_api_call_records, summarize_api_calls
from ..batching import BatchingError, ChapterBatch, partition_chapters as _partition_chapters
from ..config import validate_run_directory
from ..file_storage import record_runtime_event
from ..master_plan import MasterPlanError, require_approved_master_plan
from ..outline_validation import OutlineValidationError, ensure_comedy_rotation, ensure_outline_valid, ensure_unit_contracts
from ..storage import StorageError, atomic_write_json, read_json, resolve_run_dir, run_lock
from ..shared import utc_now


class UnitRunnerError(RuntimeError):
    """故事单元无法继续调度。"""


class UnitRunnerTerminal(UnitRunnerError):
    """A workflow-declared terminal action stopped the current unit."""

    def __init__(self, action: str, message: str) -> None:
        super().__init__(message)
        self.action = action


def partition_chapters(
    start: int,
    end: int,
    *,
    minimum: int = 3,
    maximum: int = 4,
    preferred: int = 4,
) -> tuple[ChapterBatch, ...]:
    try:
        return _partition_chapters(
            start,
            end,
            minimum=minimum,
            maximum=maximum,
            preferred=preferred,
        )
    except BatchingError as exc:
        raise UnitRunnerError(str(exc)) from exc


def _load_unit(
    root: Path, run_id: str, unit_id: str
) -> tuple[Path, dict[str, Any], list[dict[str, Any]], list[dict[str, Any]], int]:
    try:
        require_approved_master_plan(root, run_id)
    except MasterPlanError as exc:
        raise UnitRunnerError(str(exc)) from exc
    report = validate_run_directory(root, run_id)
    if not report.valid:
        details = "; ".join(f"{item.path}: {item.message}" for item in report.issues)
        raise UnitRunnerError(f"运行配置无效：{details}")
    run_dir = resolve_run_dir(root, run_id)
    run_config = read_json(run_dir / "run.json")
    units = read_json(run_dir / "planning/story-units.json")
    outlines = read_json(run_dir / "planning/chapter-outlines.json")
    matches = [index for index, item in enumerate(units) if item.get("unit_id") == unit_id]
    if len(matches) != 1:
        raise UnitRunnerError(f"故事单元 {unit_id} 不存在或重复")
    return run_dir, run_config, units, outlines, matches[0]


def _validate_unit(
    run_config: dict[str, Any],
    unit: dict[str, Any],
    outlines: list[dict[str, Any]],
) -> tuple[int, int, tuple[ChapterBatch, ...]]:
    chapter_range = unit.get("chapter_range")
    if (
        not isinstance(chapter_range, list)
        or len(chapter_range) != 2
        or not all(
            isinstance(item, int) and not isinstance(item, bool)
            for item in chapter_range
        )
    ):
        raise UnitRunnerError("故事单元 chapter_range 必须是两个整数")
    start, end = chapter_range
    count = end - start + 1
    batch_policy = run_config["policies"]["batch"]
    if not batch_policy["story_unit_min"] <= count <= batch_policy["story_unit_max"]:
        raise UnitRunnerError(
            f"故事单元必须为 {batch_policy['story_unit_min']}～"
            f"{batch_policy['story_unit_max']} 章，当前为 {count} 章"
        )
    relevant = [
        item
        for item in outlines
        if isinstance(item.get("number"), int) and start <= item["number"] <= end
    ]
    numbers = [item["number"] for item in relevant]
    if len(numbers) != len(set(numbers)):
        raise UnitRunnerError("故事单元存在重复章节细纲")
    pending_revalidation = [
        item["number"]
        for item in relevant
        if item.get("revalidation_status") == "pending"
    ]
    if pending_revalidation:
        raise UnitRunnerError(
            f"修订后章纲尚未重验：{pending_revalidation}；"
            "请先执行 validate-outline --accept-revision"
        )
    try:
        for outline in relevant:
            ensure_outline_valid(outline, run_config)
        ensure_comedy_rotation(relevant, start, end)
        ensure_unit_contracts(unit, relevant)
    except OutlineValidationError as exc:
        raise UnitRunnerError(f"故事单元章纲校验失败：{exc}") from exc
    batches = partition_chapters(
        start,
        end,
        minimum=batch_policy["ledger_batch_min"],
        maximum=batch_policy["ledger_batch_max"],
        preferred=batch_policy["ledger_batch_size"],
    )
    number_set = set(numbers)
    for batch in batches:
        present = [
            number
            for number in range(batch.start, batch.end + 1)
            if number in number_set
        ]
        if present and len(present) != batch.size:
            raise UnitRunnerError(
                f"章纲批次第 {batch.start}～{batch.end} 章只存在部分章纲：{present}"
            )
    return start, end, batches


def _minimum_remaining_calls(
    run_dir: Path,
    run_config: dict[str, Any],
    outlines: list[dict[str, Any]],
    start: int,
    end: int,
    batches: tuple[ChapterBatch, ...],
) -> int:
    by_number = {item.get("number"): item for item in outlines}
    calls_by_status = {
        "planned": 3,
        "outline_ready": 3,
        "drafting": 3,
        "draft_generated": 2,
        "draft_failed_provider": 3,
        "draft_failed_length": 3,
        "draft_failed_contract": 3,
        "draft_failed_quality": 3,
        "draft_quality_pending": 2,
        "draft_passed": 1,
        "state_extracting": 1,
        "state_failed": 1,
        "state_ready": 0,
        "committing": 0,
        "committed": 0,
        "locked": 0,
    }
    total = 0
    for chapter in range(start, end + 1):
        outline = by_number.get(chapter)
        status = outline.get("status") if isinstance(outline, dict) else "planned"
        total += calls_by_status.get(str(status), 3)
    for batch in batches:
        if any(
            chapter not in by_number
            for chapter in range(batch.start, batch.end + 1)
        ):
            chunk_size = int(
                run_config["policies"]["batch"].get(
                    "outline_request_chunk_size", batch.size
                )
            )
            total += (batch.size + chunk_size - 1) // chunk_size
        path = run_dir / f"ledgers/batch-{batch.start:04d}-{batch.end:04d}.json"
        if not path.exists():
            total += 1
    return total


def _ensure_unit_call_budget(
    run_dir: Path,
    run_config: dict[str, Any],
    outlines: list[dict[str, Any]],
    start: int,
    end: int,
    batches: tuple[ChapterBatch, ...],
) -> int:
    minimum = _minimum_remaining_calls(
        run_dir, run_config, outlines, start, end, batches
    )
    max_calls = run_config["policies"]["budget"].get("max_calls")
    if max_calls is None:
        return minimum
    summary = summarize_api_calls(
        load_api_call_records(run_dir / "logs/api-calls.jsonl")
    )
    remaining = max_calls - summary["calls"]
    if remaining < minimum:
        raise UnitRunnerError(
            f"调用预算不足以完成当前故事单元：至少还需 {minimum} 次，"
            f"预算仅剩 {remaining} 次"
        )
    return minimum


def _set_unit_status(
    root: Path,
    run_id: str,
    unit_id: str,
    status: str,
    *,
    reason: str | None = None,
) -> None:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        run_config = read_json(run_dir / "run.json")
        units = read_json(run_dir / "planning/story-units.json")
        previous_unit_status: str | None = None
        previous_pause_reason: str | None = None
        for index, unit in enumerate(units):
            if unit.get("unit_id") != unit_id:
                continue
            previous_unit_status = (
                unit.get("status") if isinstance(unit.get("status"), str) else None
            )
            previous_pause_reason = (
                unit.get("pause_reason")
                if isinstance(unit.get("pause_reason"), str)
                else None
            )
            updated = {**unit, "status": status, "updated_at": utc_now()}
            if reason is not None:
                updated["pause_reason"] = reason
            else:
                updated.pop("pause_reason", None)
            units[index] = updated
            break
        else:
            raise UnitRunnerError(f"故事单元 {unit_id} 不存在")
        run_status = {
            "paused": "paused",
            "failed": "failed",
            "completed": "ready",
        }.get(status, "running")
        run_update = {
            **run_config,
            "status": run_status,
            "current_story_unit": unit_id,
            "current_batch": None
            if status == "completed"
            else run_config.get("current_batch"),
            "updated_at": utc_now(),
        }
        if reason is not None:
            run_update["pause_reason"] = reason
        else:
            run_update.pop("pause_reason", None)
        atomic_write_json(run_dir / "planning/story-units.json", units)
        atomic_write_json(run_dir / "run.json", run_update)
        if previous_unit_status == "paused" and status == "running":
            next_chapter = run_config.get("last_committed_chapter", 0) + 1
            record_runtime_event(
                run_dir,
                run_config,
                {
                    "timestamp": utc_now(),
                    "action": "unit_resumed",
                    "unit_id": unit_id,
                    "chapter": next_chapter,
                    "previous_pause_reason": previous_pause_reason,
                },
            )


def _set_current_batch(root: Path, run_id: str, batch: ChapterBatch) -> None:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        run = read_json(run_dir / "run.json")
        atomic_write_json(
            run_dir / "run.json",
            {
                **run,
                "status": "running",
                "current_batch": f"batch-{batch.start:04d}-{batch.end:04d}",
                "updated_at": utc_now(),
            },
        )


def _current_outline(root: Path, run_id: str, chapter: int) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    outlines = read_json(run_dir / "planning/chapter-outlines.json")
    matches = [item for item in outlines if item.get("number") == chapter]
    if len(matches) != 1:
        raise UnitRunnerError(f"第 {chapter} 章细纲不存在或重复")
    return matches[0]
