"""Top-level story-unit orchestration."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..chapters import ChapterServiceError
from ..file_storage import append_checkpoint, archive_completed_unit_debug, record_runtime_event
from ..ledger import LedgerError
from ..planning_service import PlanningServiceError
from ..provider import ProviderError, TextProvider
from ..reporting import ReportingError
from ..state_rebuild import StateRebuildError
from ..storage import StorageError, atomic_write_json, read_json
from ..workflow_runtime import WorkflowLoadError, load_workflow_flow, workflow_terminal_action
from ..shared import utc_now
from .artifacts import _unit_artifacts
from .batch import _execute_batch_step
from .chapter import _drive_chapter
from .common import UnitRunnerError, UnitRunnerTerminal, _ensure_unit_call_budget, _load_unit, _set_current_batch, _set_unit_status, _validate_unit
from .completion import _execute_unit_completion_step


def run_unit(
    root: Path,
    run_id: str,
    unit_id: str,
    provider: TextProvider,
) -> dict[str, Any]:
    try:
        flow = load_workflow_flow(root)
    except WorkflowLoadError as exc:
        raise UnitRunnerError(str(exc)) from exc
    lifecycle = flow["unit_lifecycle"]
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
                _execute_batch_step(
                    flow,
                    lifecycle["missing_batch_outlines"],
                    root,
                    run_id,
                    unit_id,
                    batch,
                    provider,
                )
                report["planned_batches"].append([batch.start, batch.end])
            for chapter in range(batch.start, batch.end + 1):
                _drive_chapter(root, run_id, chapter, provider)
                report["committed_chapters"].append(chapter)
            ledger_path = run_dir / f"ledgers/batch-{batch.start:04d}-{batch.end:04d}.json"
            if not ledger_path.exists():
                ledger = _execute_batch_step(
                    flow,
                    lifecycle["completed_batch"],
                    root,
                    run_id,
                    unit_id,
                    batch,
                    provider,
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
        action = exc.action if isinstance(exc, UnitRunnerTerminal) else "pause"
        unit_status = "failed" if action == "fail" else "paused"
        report.update({"status": unit_status, "error": reason})
        _set_unit_status(root, run_id, unit_id, unit_status, reason=reason)
        atomic_write_json(run_dir / f"reports/unit-{unit_id}.json", report)
        raise UnitRunnerError(reason) from exc

    report["status"] = "completed"
    _set_unit_status(root, run_id, unit_id, "completed")
    try:
        review: dict[str, Any] | None = None
        completion_artifacts = _unit_artifacts(
            run_dir, unit_id, start, end, batches
        )
        for step_id in lifecycle["after_unit"]:
            result = _execute_unit_completion_step(
                flow,
                step_id,
                root,
                run_id,
                unit_id,
                completion_artifacts,
            )
            if step_id == "review_unit":
                if not isinstance(result, dict):
                    raise UnitRunnerError("单元评审未返回报告")
                review = result
            elif step_id == "rebuild_state":
                report["state_rebuild"] = result
        if review is None:
            raise UnitRunnerError("工作流单元收尾未执行 review_unit")
    except (ReportingError, ProviderError, StorageError, StateRebuildError, UnitRunnerError) as exc:
        reason = f"正文已全部提交，但故事单元评审失败：{exc}"
        try:
            terminal_action = workflow_terminal_action(flow, "unit_review_failed")
        except WorkflowLoadError as workflow_exc:
            raise UnitRunnerError(str(workflow_exc)) from workflow_exc
        unit_status = "failed" if terminal_action == "fail" else "paused"
        report.update({"status": unit_status, "error": reason})
        _set_unit_status(root, run_id, unit_id, unit_status, reason=reason)
        atomic_write_json(run_dir / f"reports/unit-{unit_id}.json", report)
        raise UnitRunnerError(reason) from exc
    report["review_path"] = f"reports/story-unit-review-{unit_id}.json"
    report["verdict"] = review["verdict"]
    atomic_write_json(run_dir / f"reports/unit-{unit_id}.json", report)
    completed_config = read_json(run_dir / "run.json")
    append_checkpoint(
        run_dir,
        completed_config,
        unit_id=unit_id,
        chapter_range=[start, end],
    )
    artifact = archive_completed_unit_debug(
        run_dir,
        completed_config,
        unit_id=unit_id,
        chapter_range=[start, end],
    )
    if artifact is not None:
        record_runtime_event(
            run_dir,
            completed_config,
            {
                "timestamp": utc_now(),
                "action": "unit_debug_archived",
                "unit_id": unit_id,
                "artifact": artifact.relative_to(run_dir).as_posix(),
            },
        )
    return report
