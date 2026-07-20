"""已提交章节修订时的依赖失效、归档和可恢复回退。"""

from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
from typing import Any

from .state_store import load_events
from .storage import (
    atomic_write_json,
    atomic_write_text,
    read_json,
    resolve_run_dir,
    run_lock,
)


class RevisionError(RuntimeError):
    """运行不能安全回退到指定章节。"""


LEDGER_RANGE_RE = re.compile(r"batch-(\d{4})-(\d{4})")
SNAPSHOT_RE = re.compile(r"chapter-(\d{4})\.json$")
ACTIVE_CHAPTER_FILES = (
    "draft.final.md",
    "draft.candidate.md",
    "state-event.json",
    "checks.json",
    "review.raw.json",
    "state.raw.json",
    "draft.prompt.md",
    "review.prompt.md",
    "state.prompt.md",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _revision_id(run: dict[str, Any]) -> str:
    number = run.get("revision_number", 0)
    if not isinstance(number, int) or isinstance(number, bool) or number < 0:
        number = 0
    return f"revision-{number + 1:04d}"


def _journal_path(run_dir: Path) -> Path:
    return run_dir / "logs/revision-journal.json"


def _jsonl_text(items: list[dict[str, Any]]) -> str:
    return "".join(
        json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n"
        for item in items
    )


def _safe_relative(run_dir: Path, relative: str) -> Path:
    path = (run_dir / relative).resolve()
    if run_dir.resolve() not in path.parents:
        raise RevisionError(f"修订路径越出运行目录：{relative}")
    return path


def _archive_source(
    run_dir: Path,
    revision_dir: Path,
    relative: str,
) -> str:
    source = _safe_relative(run_dir, relative)
    target = revision_dir / "artifacts" / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        return target.relative_to(run_dir).as_posix()
    if not source.exists():
        raise RevisionError(f"待归档文件同时不存在于活动区和归档区：{relative}")
    try:
        os.replace(source, target)
    except OSError as exc:
        raise RevisionError(f"无法归档 {relative}：{exc}") from exc
    return target.relative_to(run_dir).as_posix()


def apply_revision_journal(run_dir: Path, journal: dict[str, Any]) -> dict[str, Any]:
    revision_id = journal.get("revision_id")
    if not isinstance(revision_id, str) or not revision_id:
        raise RevisionError("修订事务日志缺少 revision_id")
    archive_sources = journal.get("archive_sources")
    retained_events = journal.get("retained_events")
    invalidated_events = journal.get("invalidated_events")
    outlines = journal.get("outlines")
    units = journal.get("units")
    updated_run = journal.get("updated_run")
    manifest = journal.get("manifest")
    if (
        not isinstance(archive_sources, list)
        or not all(isinstance(item, str) for item in archive_sources)
        or not isinstance(retained_events, list)
        or not isinstance(invalidated_events, list)
        or not isinstance(outlines, list)
        or not isinstance(units, list)
        or not isinstance(updated_run, dict)
        or not isinstance(manifest, dict)
    ):
        raise RevisionError("修订事务日志损坏")

    revision_dir = run_dir / "revisions" / revision_id
    revision_dir.mkdir(parents=True, exist_ok=True)
    archived = [
        _archive_source(run_dir, revision_dir, relative)
        for relative in archive_sources
    ]
    final_manifest = {**manifest, "archived_paths": archived}
    atomic_write_text(
        revision_dir / "events.invalidated.jsonl",
        _jsonl_text(invalidated_events),
    )
    atomic_write_text(
        run_dir / "state/events.jsonl",
        _jsonl_text(retained_events),
    )
    atomic_write_json(run_dir / "planning/chapter-outlines.json", outlines)
    atomic_write_json(run_dir / "planning/story-units.json", units)
    for outline in outlines:
        number = outline.get("number")
        if (
            isinstance(number, int)
            and outline.get("invalidated_by_revision") == revision_id
        ):
            chapter_dir = run_dir / f"chapters/{number:04d}"
            if chapter_dir.exists():
                atomic_write_json(chapter_dir / "outline.json", outline)
    atomic_write_json(run_dir / "run.json", updated_run)
    atomic_write_json(revision_dir / "manifest.json", final_manifest)
    try:
        _journal_path(run_dir).unlink(missing_ok=True)
    except OSError as exc:
        raise RevisionError(f"无法清理修订事务日志：{exc}") from exc
    return final_manifest


def resume_revision(run_dir: Path) -> dict[str, Any]:
    path = _journal_path(run_dir)
    if not path.exists():
        raise RevisionError("没有待恢复修订事务")
    return apply_revision_journal(run_dir, read_json(path))


def invalidate_from(
    root: Path,
    run_id: str,
    chapter: int,
    *,
    reason: str,
) -> dict[str, Any]:
    if not isinstance(chapter, int) or isinstance(chapter, bool) or chapter <= 0:
        raise RevisionError("chapter 必须是正整数")
    if not isinstance(reason, str) or not reason.strip():
        raise RevisionError("必须提供非空修订原因")
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        if _journal_path(run_dir).exists():
            raise RevisionError("存在待恢复修订事务，请先执行 resume")
        if (run_dir / "logs/commit-journal.json").exists():
            raise RevisionError("存在待恢复提交事务，请先执行 resume")
        run = read_json(run_dir / "run.json")
        last_committed = run.get("last_committed_chapter")
        if not isinstance(last_committed, int) or chapter > last_committed:
            raise RevisionError(
                f"只能从已提交章节失效；当前最后提交为 {last_committed}"
            )
        outlines = read_json(run_dir / "planning/chapter-outlines.json")
        units = read_json(run_dir / "planning/story-units.json")
        if not isinstance(outlines, list) or not isinstance(units, list):
            raise RevisionError("规划文件损坏")
        target = [item for item in outlines if item.get("number") == chapter]
        if len(target) != 1 or target[0].get("status") not in {"committed", "locked"}:
            raise RevisionError(f"第 {chapter} 章不是可失效的正式章节")

        events = load_events(run_dir / "state/events.jsonl")
        committed_chapters = {
            item.get("chapter")
            for item in events
            if isinstance(item.get("chapter"), int)
        }
        missing = [
            number
            for number in range(1, last_committed + 1)
            if number not in committed_chapters
        ]
        if missing:
            raise RevisionError(f"正式状态事件不完整，缺少章节：{missing}")
        retained_events = [item for item in events if item.get("chapter", 0) < chapter]
        invalidated_events = [item for item in events if item.get("chapter", 0) >= chapter]

        revision_id = _revision_id(run)
        if (run_dir / "revisions" / revision_id).exists():
            raise RevisionError(f"修订目录已存在：{revision_id}")
        archive_sources: list[str] = []
        for path in sorted((run_dir / "state/snapshots").glob("chapter-*.json")):
            match = SNAPSHOT_RE.search(path.name)
            if match and int(match.group(1)) >= chapter:
                archive_sources.append(path.relative_to(run_dir).as_posix())
        ledgers_dir = run_dir / "ledgers"
        for path in sorted(ledgers_dir.iterdir() if ledgers_dir.exists() else []):
            if path.is_file():
                match = LEDGER_RANGE_RE.search(path.name)
                if match and int(match.group(2)) >= chapter:
                    archive_sources.append(path.relative_to(run_dir).as_posix())
        reports_dir = run_dir / "reports"
        for path in sorted(reports_dir.iterdir() if reports_dir.exists() else []):
            if path.is_file() and (
                path.name.startswith("unit-")
                or path.name.startswith("story-unit-review")
            ):
                archive_sources.append(path.relative_to(run_dir).as_posix())

        stale_outline_keys = {
            "actual_length",
            "draft_path",
            "checks",
            "retry_counts",
            "state_failure_kind",
            "state_failure_reason",
            "review_failure_reason",
            "pause_reason",
        }
        affected_chapters: list[int] = []
        invalidated_at = _utc_now()
        for index, outline in enumerate(outlines):
            number = outline.get("number")
            if not isinstance(number, int) or number < chapter:
                continue
            affected_chapters.append(number)
            reset = {
                key: value
                for key, value in outline.items()
                if key not in stale_outline_keys
            }
            reset.update(
                {
                    "status": "outline_ready",
                    "revalidation_status": "pending",
                    "invalidated_by_revision": revision_id,
                    "invalidated_at": invalidated_at,
                }
            )
            outlines[index] = reset
            chapter_dir = run_dir / f"chapters/{number:04d}"
            if chapter_dir.exists():
                for filename in ACTIVE_CHAPTER_FILES:
                    path = chapter_dir / filename
                    if path.is_file():
                        archive_sources.append(path.relative_to(run_dir).as_posix())

        affected_units: list[str] = []
        current_unit: str | None = None
        for index, unit in enumerate(units):
            chapter_range = unit.get("chapter_range")
            if (
                not isinstance(chapter_range, list)
                or len(chapter_range) != 2
                or chapter_range[1] < chapter
            ):
                continue
            unit_id = unit.get("unit_id")
            if isinstance(unit_id, str):
                affected_units.append(unit_id)
                if current_unit is None and chapter_range[0] <= chapter <= chapter_range[1]:
                    current_unit = unit_id
            units[index] = {
                **unit,
                "status": "planned",
                "revision_required_from": chapter,
                "invalidated_by_revision": revision_id,
                "updated_at": invalidated_at,
            }

        revision_number = run.get("revision_number", 0)
        if not isinstance(revision_number, int) or isinstance(revision_number, bool):
            revision_number = 0
        updated_run = {
            **run,
            "status": "ready",
            "last_committed_chapter": chapter - 1,
            "current_story_unit": current_unit or run.get("current_story_unit"),
            "revision_number": revision_number + 1,
            "active_revision": revision_id,
            "updated_at": invalidated_at,
        }
        updated_run.pop("pause_reason", None)
        manifest = {
            "schema_version": "1.0",
            "revision_id": revision_id,
            "run_id": run_id,
            "invalidated_from_chapter": chapter,
            "previous_last_committed_chapter": last_committed,
            "new_last_committed_chapter": chapter - 1,
            "reason": reason.strip(),
            "affected_chapters": sorted(affected_chapters),
            "affected_units": affected_units,
            "invalidated_event_ids": [
                item.get("event_id") for item in invalidated_events
            ],
            "archived_paths": [],
            "created_at": invalidated_at,
        }
        journal = {
            "journal_version": "1.0",
            "revision_id": revision_id,
            "archive_sources": sorted(set(archive_sources)),
            "retained_events": retained_events,
            "invalidated_events": invalidated_events,
            "outlines": outlines,
            "units": units,
            "updated_run": updated_run,
            "manifest": manifest,
            "created_at": invalidated_at,
        }
        atomic_write_json(_journal_path(run_dir), journal)
        return apply_revision_journal(run_dir, journal)
