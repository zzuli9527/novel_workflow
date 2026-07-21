"""10～20 章故事单元顺序调度器。"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .api_runtime import load_api_call_records, summarize_api_calls
from .batching import BatchingError, ChapterBatch, partition_chapters as _partition_chapters
from .chapter_service import (
    ChapterServiceError,
    commit_chapter,
    draft_chapter,
    extract_state,
    repair_chapter,
    review_chapter,
    resume_run,
)
from .config import validate_run_directory
from .ledger import LedgerError, build_ledger
from .outline_validation import (
    OutlineValidationError,
    ensure_comedy_rotation,
    ensure_outline_valid,
    ensure_unit_contracts,
)
from .provider import ProviderError, TextProvider
from .planning_service import PlanningServiceError, plan_chapter_batch
from .reporting import ReportingError, generate_unit_review
from .storage import (
    StorageError,
    append_jsonl,
    atomic_write_json,
    read_json,
    resolve_run_dir,
    run_lock,
)


class UnitRunnerError(RuntimeError):
    """故事单元无法继续调度。"""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def partition_chapters(
    start: int,
    end: int,
    *,
    minimum: int = 3,
    maximum: int = 5,
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
            updated = {**unit, "status": status, "updated_at": _utc_now()}
            if reason is not None:
                updated["pause_reason"] = reason
            else:
                updated.pop("pause_reason", None)
            units[index] = updated
            break
        else:
            raise UnitRunnerError(f"故事单元 {unit_id} 不存在")
        run_update = {
            **run_config,
            "status": "paused" if status == "paused" else ("ready" if status == "completed" else "running"),
            "current_story_unit": unit_id,
            "current_batch": None
            if status == "completed"
            else run_config.get("current_batch"),
            "updated_at": _utc_now(),
        }
        if reason is not None:
            run_update["pause_reason"] = reason
        else:
            run_update.pop("pause_reason", None)
        atomic_write_json(run_dir / "planning/story-units.json", units)
        atomic_write_json(run_dir / "run.json", run_update)
        if previous_unit_status == "paused" and status == "running":
            next_chapter = run_config.get("last_committed_chapter", 0) + 1
            append_jsonl(
                run_dir / "logs/events.jsonl",
                {
                    "timestamp": _utc_now(),
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
                "updated_at": _utc_now(),
            },
        )


def _current_outline(root: Path, run_id: str, chapter: int) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    outlines = read_json(run_dir / "planning/chapter-outlines.json")
    matches = [item for item in outlines if item.get("number") == chapter]
    if len(matches) != 1:
        raise UnitRunnerError(f"第 {chapter} 章细纲不存在或重复")
    return matches[0]


def _state_failure_has_retry_budget(
    root: Path, run_id: str, outline: dict[str, Any]
) -> bool:
    if outline.get("status") != "state_failed":
        return False
    retry_kind = outline.get("state_failure_kind")
    if retry_kind not in {"format", "content"}:
        return False
    retry_counts = outline.get("retry_counts", {})
    retry_counter_key = f"state_{retry_kind}"
    current_count = (
        retry_counts.get(retry_counter_key, 0)
        if isinstance(retry_counts, dict)
        else 0
    )
    if not isinstance(current_count, int):
        current_count = 0
    run = read_json(resolve_run_dir(root, run_id) / "run.json")
    maximum = run["policies"]["retry"][retry_kind]
    return current_count < maximum


def _review_failure_has_retry_budget(
    root: Path, run_id: str, outline: dict[str, Any]
) -> bool:
    if outline.get("status") != "draft_quality_pending":
        return False
    if not outline.get("review_failure_reason"):
        return False
    retry_counts = outline.get("retry_counts", {})
    current_count = (
        retry_counts.get("review_format", 0)
        if isinstance(retry_counts, dict)
        else 0
    )
    if not isinstance(current_count, int):
        current_count = 0
    run = read_json(resolve_run_dir(root, run_id) / "run.json")
    maximum = run["policies"]["retry"]["format"]
    return current_count < maximum


def _drive_chapter(
    root: Path,
    run_id: str,
    chapter: int,
    provider: TextProvider,
) -> str:
    for _ in range(20):
        outline = _current_outline(root, run_id, chapter)
        status = outline.get("status")
        if status in {"committed", "locked"}:
            return str(status)
        if status == "outline_ready":
            draft_chapter(root, run_id, chapter, provider)
            continue
        if status in {
            "draft_failed_provider",
            "draft_failed_length",
            "draft_failed_contract",
            "draft_failed_quality",
        }:
            repair_chapter(root, run_id, chapter, provider)
            continue
        if status == "draft_quality_pending":
            try:
                review_chapter(root, run_id, chapter, provider)
            except ChapterServiceError:
                failed_outline = _current_outline(root, run_id, chapter)
                if _review_failure_has_retry_budget(root, run_id, failed_outline):
                    continue
                raise
            continue
        if status in {"draft_passed", "state_failed"}:
            try:
                extract_state(root, run_id, chapter, provider)
            except ChapterServiceError:
                failed_outline = _current_outline(root, run_id, chapter)
                if _state_failure_has_retry_budget(root, run_id, failed_outline):
                    continue
                raise
            continue
        if status == "state_ready":
            commit_chapter(root, run_id, chapter)
            continue
        if status in {"drafting", "state_extracting", "committing"}:
            resume_run(root, run_id)
            continue
        raise UnitRunnerError(f"第 {chapter} 章处于不可调度状态：{status}")
    raise UnitRunnerError(f"第 {chapter} 章超过内部调度循环上限")


def run_unit(
    root: Path,
    run_id: str,
    unit_id: str,
    provider: TextProvider,
) -> dict[str, Any]:
    run_dir, run_config, units, outlines, unit_index = _load_unit(root, run_id, unit_id)
    unit = units[unit_index]
    start, end, batches = _validate_unit(run_config, unit, outlines)
    try:
        minimum_calls = _ensure_unit_call_budget(
            run_dir, run_config, outlines, start, end, batches
        )
    except UnitRunnerError as exc:
        reason = str(exc)
        _set_unit_status(root, run_id, unit_id, "paused", reason=reason)
        preflight_report = {
            "unit_id": unit_id,
            "chapter_range": [start, end],
            "batches": [[batch.start, batch.end] for batch in batches],
            "committed_chapters": [],
            "ledgers": [],
            "status": "paused",
            "phase": "preflight",
            "error": reason,
        }
        atomic_write_json(run_dir / f"reports/unit-{unit_id}.json", preflight_report)
        raise
    _set_unit_status(root, run_id, unit_id, "running")

    report: dict[str, Any] = {
        "unit_id": unit_id,
        "chapter_range": [start, end],
        "batches": [[batch.start, batch.end] for batch in batches],
        "committed_chapters": [],
        "ledgers": [],
        "planned_batches": [],
        "minimum_expected_calls_at_start": minimum_calls,
        "status": "running",
    }
    try:
        for batch in batches:
            _set_current_batch(root, run_id, batch)
            current_outlines = read_json(
                run_dir / "planning/chapter-outlines.json"
            )
            current_numbers = {
                item.get("number")
                for item in current_outlines
                if isinstance(item, dict)
            }
            missing = [
                chapter
                for chapter in range(batch.start, batch.end + 1)
                if chapter not in current_numbers
            ]
            if missing:
                if len(missing) != batch.size:
                    raise UnitRunnerError(
                        f"第 {batch.start}～{batch.end} 章章纲不完整：{missing}"
                    )
                plan_chapter_batch(
                    root,
                    run_id,
                    unit_id,
                    batch.start,
                    batch.end,
                    provider,
                )
                report["planned_batches"].append([batch.start, batch.end])
            for chapter in range(batch.start, batch.end + 1):
                _drive_chapter(root, run_id, chapter, provider)
                report["committed_chapters"].append(chapter)
            ledger_path = run_dir / f"ledgers/batch-{batch.start:04d}-{batch.end:04d}.json"
            if not ledger_path.exists():
                ledger = build_ledger(
                    root, run_id, batch.start, batch.end, provider
                )
                report["ledgers"].append(ledger["batch_id"])
            else:
                report["ledgers"].append(read_json(ledger_path)["batch_id"])
    except (
        ChapterServiceError,
        LedgerError,
        PlanningServiceError,
        StorageError,
        UnitRunnerError,
    ) as exc:
        reason = str(exc)
        report.update({"status": "paused", "error": reason})
        _set_unit_status(root, run_id, unit_id, "paused", reason=reason)
        atomic_write_json(run_dir / f"reports/unit-{unit_id}.json", report)
        raise UnitRunnerError(reason) from exc

    report["status"] = "completed"
    _set_unit_status(root, run_id, unit_id, "completed")
    try:
        review = generate_unit_review(root, run_id, unit_id)
    except (ReportingError, ProviderError, StorageError) as exc:
        reason = f"正文已全部提交，但故事单元评审失败：{exc}"
        report.update({"status": "paused", "error": reason})
        _set_unit_status(root, run_id, unit_id, "paused", reason=reason)
        atomic_write_json(run_dir / f"reports/unit-{unit_id}.json", report)
        raise UnitRunnerError(reason) from exc
    report["review_path"] = f"reports/story-unit-review-{unit_id}.json"
    report["verdict"] = review["verdict"]
    atomic_write_json(run_dir / f"reports/unit-{unit_id}.json", report)
    return report
