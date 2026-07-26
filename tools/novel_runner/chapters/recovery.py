"""Recover interrupted chapter work and report run status."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..revision import RevisionError, resume_revision
from ..state_machine import transition_record
from ..storage import atomic_write_json, read_json, resolve_run_dir, run_lock
from .commit import _apply_commit_journal, _commit_journal_path
from .common import ChapterServiceError, _load_context, _log_runtime_event, _save_outlines


def resume_run(root: Path, run_id: str) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        revision_journal = run_dir / "logs/revision-journal.json"
        if revision_journal.exists():
            try:
                manifest = resume_revision(run_dir)
            except RevisionError as exc:
                raise ChapterServiceError(str(exc)) from exc
            _log_runtime_event(
                run_dir,
                "revision_recovered",
                chapter=manifest.get("invalidated_from_chapter"),
                revision_id=manifest.get("revision_id"),
            )
            return {"action": "revision_recovered", "revision": manifest}
        run_dir, run_config, outlines = _load_context(root, run_id)
        journal_path = _commit_journal_path(run_dir, run_config)
        if not journal_path.exists():
            recovered: list[int] = []
            recovered_states: list[int] = []
            for index, outline in enumerate(outlines):
                status = outline.get("status")
                if status == "drafting":
                    outlines[index] = transition_record(outline, "draft_failed_provider")
                    chapter = outline.get("number")
                    if isinstance(chapter, int):
                        recovered.append(chapter)
                elif status == "state_extracting":
                    recovered_outline = transition_record(outline, "state_failed")
                    outlines[index] = {
                        **recovered_outline,
                        "state_failure_kind": "transport",
                    }
                    chapter = outline.get("number")
                    if isinstance(chapter, int):
                        recovered_states.append(chapter)
                else:
                    continue
                if isinstance(chapter, int):
                    chapter_dir = run_dir / f"chapters/{chapter:04d}"
                    if chapter_dir.exists():
                        atomic_write_json(chapter_dir / "outline.json", outlines[index])
            if recovered or recovered_states:
                _save_outlines(run_dir, outlines)
                _log_runtime_event(
                    run_dir,
                    "incomplete_tasks_recovered",
                    chapters=sorted([*recovered, *recovered_states]),
                )
                return {
                    "action": "incomplete_tasks_recovered",
                    "draft_chapters": recovered,
                    "state_chapters": recovered_states,
                    "last_committed_chapter": run_config.get("last_committed_chapter"),
                }
            return {
                "action": "none",
                "last_committed_chapter": run_config.get("last_committed_chapter"),
            }
        journal = read_json(journal_path)
        result = _apply_commit_journal(run_dir, run_config, outlines, journal)
        _log_runtime_event(
            run_dir,
            "commit_recovered",
            chapter=journal.get("chapter"),
        )
        return {"action": "commit_recovered", **result}


def get_run_status(root: Path, run_id: str) -> dict[str, Any]:
    run_dir, run_config, outlines = _load_context(root, run_id)
    status_counts: dict[str, int] = {}
    for outline in outlines:
        status = str(outline.get("status", "missing"))
        status_counts[status] = status_counts.get(status, 0) + 1
    return {
        "run_id": run_id,
        "status": run_config.get("status"),
        "last_committed_chapter": run_config.get("last_committed_chapter"),
        "current_story_unit": run_config.get("current_story_unit"),
        "current_batch": run_config.get("current_batch"),
        "chapter_status_counts": status_counts,
        "commit_recovery_pending": _commit_journal_path(run_dir, run_config).exists(),
        "revision_recovery_pending": (
            run_dir / "logs/revision-journal.json"
        ).exists(),
    }
