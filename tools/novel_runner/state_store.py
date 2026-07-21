"""追加式状态事件和可重建章节快照。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .storage import StorageError, append_jsonl
from .structured_state import StructuredStateError, project_structured_state


ACCUMULATED_FIELDS = (
    "entity_changes",
    "relationship_changes",
    "cultivation_changes",
    "resource_changes",
    "knowledge_changes",
    "thread_changes",
    "comedy_changes",
    "new_constraints",
    "resolved_constraints",
)


class StateStoreError(RuntimeError):
    """状态事件重复、损坏或无法构建快照。"""


def load_events(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    events: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except OSError as exc:
        raise StorageError(f"无法读取状态事件：{path}：{exc}") from exc
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise StateStoreError(f"状态事件第 {line_number} 行损坏") from exc
        if not isinstance(event, dict):
            raise StateStoreError(f"状态事件第 {line_number} 行不是对象")
        events.append(event)
    return events


def ensure_event_compatible(path: Path, event: dict[str, Any]) -> bool:
    event_id = event.get("event_id")
    if not isinstance(event_id, str) or not event_id:
        raise StateStoreError("状态事件缺少 event_id")
    for existing in load_events(path):
        if existing.get("event_id") != event_id:
            continue
        if existing.get("source_sha256") != event.get("source_sha256"):
            raise StateStoreError(f"事件 {event_id} 已存在但正文哈希不同")
        return False
    return True


def append_event_once(path: Path, event: dict[str, Any]) -> bool:
    if not ensure_event_compatible(path, event):
        return False
    append_jsonl(path, event)
    return True


def build_snapshot(
    event: dict[str, Any],
    previous: dict[str, Any] | None = None,
    *,
    initial_state: dict[str, Any] | None = None,
) -> dict[str, Any]:
    chapter = event.get("chapter")
    if not isinstance(chapter, int) or chapter <= 0:
        raise StateStoreError("状态事件 chapter 必须是正整数")

    if previous is None:
        if chapter != 1:
            raise StateStoreError("非首章快照缺少上一章快照")
        previous_changes = {field: [] for field in ACCUMULATED_FIELDS}
        previous_structured = None
        event_ids: list[str] = []
    else:
        if previous.get("after_chapter") != chapter - 1:
            raise StateStoreError("上一章快照与当前章节不连续")
        previous_changes = previous.get("changes")
        if not isinstance(previous_changes, dict):
            raise StateStoreError("上一章快照缺少 changes")
        event_ids_value = previous.get("event_ids")
        if not isinstance(event_ids_value, list):
            raise StateStoreError("上一章快照缺少 event_ids")
        event_ids = list(event_ids_value)
        previous_structured = previous.get("structured_state")
        if not isinstance(previous_structured, dict):
            raise StateStoreError("上一章快照缺少 structured_state")

    changes: dict[str, list[Any]] = {}
    for field in ACCUMULATED_FIELDS:
        old_items = previous_changes.get(field, [])
        new_items = event.get(field, [])
        if not isinstance(old_items, list) or not isinstance(new_items, list):
            raise StateStoreError(f"状态字段不是数组：{field}")
        changes[field] = [*old_items, *new_items]

    event_id = event.get("event_id")
    if not isinstance(event_id, str) or not event_id:
        raise StateStoreError("状态事件缺少 event_id")
    event_ids.append(event_id)
    try:
        structured_state = project_structured_state(
            event, previous_structured, initial_state
        )
    except StructuredStateError as exc:
        raise StateStoreError(str(exc)) from exc
    return {
        "after_chapter": chapter,
        "event_ids": event_ids,
        "changes": changes,
        "structured_state": structured_state,
        "next_chapter_inputs": event.get("next_chapter_inputs", []),
        "deviations": event.get("deviations", []),
        "last_source_draft": event.get("source_draft"),
        "last_source_sha256": event.get("source_sha256"),
    }
