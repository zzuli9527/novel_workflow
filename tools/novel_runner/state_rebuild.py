"""从初始状态和正式事件原子重建全部章节快照。"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from .state_store import StateStoreError, build_snapshot, load_events
from .file_storage import events_path, is_v2, current_snapshot_path, write_snapshot
from .storage import (
    StorageError,
    atomic_write_json,
    read_json,
    resolve_run_dir,
    run_lock,
)


class StateRebuildError(RuntimeError):
    """正式事件、正文或运行指针不足以重建连续快照。"""


def _source_draft(run_dir: Path, event: dict[str, Any], chapter: int) -> Path:
    relative = event.get("source_draft")
    if not isinstance(relative, str) or not relative:
        raise StateRebuildError(f"第 {chapter} 章事件缺少 source_draft")
    path = (run_dir / relative).resolve()
    if run_dir.resolve() not in path.parents:
        raise StateRebuildError(f"第 {chapter} 章 source_draft 越出运行目录")
    if not path.is_file():
        raise StateRebuildError(f"第 {chapter} 章 final 正文不存在：{relative}")
    return path


def rebuild_state_snapshots(root: Path, run_id: str) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        try:
            run = read_json(run_dir / "run.json")
            initial_state = read_json(run_dir / "config/initial-state.json")
            events = load_events(events_path(run_dir))
        except (StorageError, StateStoreError) as exc:
            raise StateRebuildError(str(exc)) from exc

        last_committed = run.get("last_committed_chapter")
        if not isinstance(last_committed, int) or last_committed < 0:
            raise StateRebuildError("run.json 的 last_committed_chapter 无效")
        if len(events) != last_committed:
            raise StateRebuildError(
                "正式事件数量与提交指针不一致："
                f"events={len(events)}，last_committed={last_committed}"
            )

        rebuilt: list[tuple[int, dict[str, Any]]] = []
        previous: dict[str, Any] | None = None
        for chapter, event in enumerate(events, start=1):
            if event.get("chapter") != chapter:
                raise StateRebuildError(
                    f"正式事件章节不连续：期望 {chapter}，实际 {event.get('chapter')}"
                )
            expected_id = f"chapter-{chapter:04d}"
            if event.get("event_id") != expected_id:
                raise StateRebuildError(
                    f"第 {chapter} 章 event_id 应为 {expected_id}"
                )
            draft_path = _source_draft(run_dir, event, chapter)
            try:
                draft_text = draft_path.read_text(encoding="utf-8-sig")
            except OSError as exc:
                raise StateRebuildError(
                    f"无法读取第 {chapter} 章 final 正文：{exc}"
                ) from exc
            actual_sha256 = hashlib.sha256(draft_text.encode("utf-8")).hexdigest()
            if event.get("source_sha256") != actual_sha256:
                raise StateRebuildError(
                    f"第 {chapter} 章正文哈希与正式事件不一致"
                )
            try:
                snapshot = build_snapshot(
                    event,
                    previous,
                    initial_state=initial_state if chapter == 1 else None,
                )
            except StateStoreError as exc:
                raise StateRebuildError(
                    f"第 {chapter} 章快照重建失败：{exc}"
                ) from exc
            snapshot["source"] = (
                "state/events.jsonl"
                if is_v2(run)
                else f"chapters/{chapter:04d}/state-event.json"
            )
            rebuilt.append((chapter, snapshot))
            previous = snapshot

        if is_v2(run):
            existing = (
                read_json(current_snapshot_path(run_dir))
                if current_snapshot_path(run_dir).exists()
                else None
            )
            final_snapshot = rebuilt[-1][1] if rebuilt else None
            comparable_existing = (
                {
                    key: value
                    for key, value in existing.items()
                    if key
                    not in {"storage_version", "last_event_sequence", "last_event_sha256"}
                }
                if isinstance(existing, dict)
                else None
            )
            changed = (
                []
                if comparable_existing == final_snapshot
                else list(range(1, last_committed + 1))
            )
            unchanged = list(range(1, last_committed + 1)) if not changed else []
            if final_snapshot is not None:
                write_snapshot(
                    run_dir,
                    run,
                    last_committed,
                    final_snapshot,
                    events[-1],
                )
            return {
                "run_id": run_id,
                "last_committed_chapter": last_committed,
                "rebuilt_snapshots": len(rebuilt),
                "changed_chapters": changed,
                "unchanged_chapters": unchanged,
                "source": "config/initial-state.json + state/events.jsonl",
            }

        snapshots_dir = run_dir / "state/snapshots"
        existing_numbers: set[int] = set()
        for path in snapshots_dir.glob("chapter-*.json"):
            token = path.stem.removeprefix("chapter-")
            if token.isdigit():
                existing_numbers.add(int(token))
        expected_numbers = set(range(1, last_committed + 1))
        extras = sorted(existing_numbers - expected_numbers)
        if extras:
            raise StateRebuildError(f"存在超出提交指针的快照：{extras}")

        changed: list[int] = []
        unchanged: list[int] = []
        for chapter, snapshot in rebuilt:
            path = snapshots_dir / f"chapter-{chapter:04d}.json"
            existing = read_json(path) if path.exists() else None
            if existing == snapshot:
                unchanged.append(chapter)
            else:
                changed.append(chapter)

        for chapter, snapshot in rebuilt:
            atomic_write_json(
                snapshots_dir / f"chapter-{chapter:04d}.json", snapshot
            )

        return {
            "run_id": run_id,
            "last_committed_chapter": last_committed,
            "rebuilt_snapshots": len(rebuilt),
            "changed_chapters": changed,
            "unchanged_chapters": unchanged,
            "source": "config/initial-state.json + state/events.jsonl",
        }
