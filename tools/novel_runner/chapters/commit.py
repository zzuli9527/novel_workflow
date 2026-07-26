"""Atomically commit a validated chapter state event."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..file_storage import events_path, prepare_event, read_current_snapshot, transaction_path, write_snapshot
from ..state_machine import ensure_chapter_can_start, transition_record
from ..state_store import StateStoreError, append_event_once, build_snapshot, ensure_event_compatible
from ..storage import StorageError, atomic_write_json, read_json, resolve_run_dir, run_lock
from ..shared import utc_now
from .common import ChapterServiceError, _find_outline, _load_context, _relative_posix, _save_outlines


def _commit_journal_path(run_dir: Path, run_config: dict[str, Any]) -> Path:
    return transaction_path(run_dir, run_config)


def _apply_commit_journal(
    run_dir: Path,
    run_config: dict[str, Any],
    outlines: list[dict[str, Any]],
    journal: dict[str, Any],
) -> dict[str, Any]:
    chapter_number = journal.get("chapter")
    event = journal.get("event")
    if not isinstance(chapter_number, int) or not isinstance(event, dict):
        raise ChapterServiceError("提交事务日志损坏")

    index, outline = _find_outline(outlines, chapter_number)
    current_status = outline.get("status")
    if current_status not in {"state_ready", "committing", "committed"}:
        raise ChapterServiceError(
            f"提交恢复要求 state_ready / committing / committed，当前为 {current_status}"
        )

    last_committed = run_config.get("last_committed_chapter")
    if last_committed not in {chapter_number - 1, chapter_number}:
        raise ChapterServiceError("运行指针与提交事务不连续")

    event_log_path = events_path(run_dir)
    chapter_dir = run_dir / f"chapters/{chapter_number:04d}"
    try:
        previous_snapshot = (
            read_current_snapshot(run_dir, run_config, chapter_number - 1)
            if chapter_number > 1
            else None
        )
        initial_state = (
            read_json(run_dir / "config/initial-state.json")
            if chapter_number == 1
            else None
        )
        snapshot = build_snapshot(
            event, previous_snapshot, initial_state=initial_state
        )
        ensure_event_compatible(event_log_path, event)
    except (StateStoreError, StorageError) as exc:
        if current_status in {"state_ready", "committing"}:
            outline = transition_record(outline, "state_failed")
            outline = {
                **outline,
                "state_failure_kind": (
                    "content" if isinstance(exc, StateStoreError) else "format"
                ),
                "state_failure_reason": str(exc),
            }
            outlines[index] = outline
            _save_outlines(run_dir, outlines)
            atomic_write_json(chapter_dir / "outline.json", outline)
        try:
            _commit_journal_path(run_dir, run_config).unlink(missing_ok=True)
        except OSError:
            pass
        raise ChapterServiceError(str(exc)) from exc

    if current_status == "state_ready":
        outline = transition_record(outline, "committing")
        outlines[index] = outline
        _save_outlines(run_dir, outlines)

    try:
        append_event_once(event_log_path, event)
    except StateStoreError as exc:
        raise ChapterServiceError(str(exc)) from exc

    snapshot["source"] = (
        "state/events.jsonl"
        if run_config.get("storage_version") == "2.0"
        else _relative_posix(chapter_dir / "state-event.json", run_dir)
    )
    write_snapshot(run_dir, run_config, chapter_number, snapshot, event)

    run_config = {
        **{key: value for key, value in run_config.items() if key != "pause_reason"},
        "status": "running",
        "last_committed_chapter": chapter_number,
        "updated_at": utc_now(),
    }
    atomic_write_json(run_dir / "run.json", run_config)

    if outline.get("status") == "committing":
        outline = transition_record(outline, "committed")
    outlines[index] = outline
    _save_outlines(run_dir, outlines)
    atomic_write_json(chapter_dir / "outline.json", outline)

    journal_path = _commit_journal_path(run_dir, run_config)
    try:
        journal_path.unlink(missing_ok=True)
    except OSError as exc:
        raise ChapterServiceError(f"无法清理已完成提交事务日志：{exc}") from exc
    return {"run": run_config, "outline": outline, "snapshot": snapshot}


def commit_chapter(root: Path, run_id: str, chapter_number: int) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        run_dir, run_config, outlines = _load_context(root, run_id)
        _, outline = _find_outline(outlines, chapter_number)
        ensure_chapter_can_start(chapter_number, run_config["last_committed_chapter"])
        if outline.get("status") != "state_ready":
            raise ChapterServiceError("只有 state_ready 章节可以提交")

        chapter_dir = run_dir / f"chapters/{chapter_number:04d}"
        event = read_json(chapter_dir / "state-event.json")
        event = prepare_event(run_dir, run_config, event)
        journal = {
            "journal_version": "1.0",
            "chapter": chapter_number,
            "event": event,
            "created_at": utc_now(),
        }
        atomic_write_json(_commit_journal_path(run_dir, run_config), journal)
        return _apply_commit_journal(run_dir, run_config, outlines, journal)
