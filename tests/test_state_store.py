from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.state_store import (
    StateStoreError,
    append_event_once,
    build_snapshot,
    load_events,
)


def event(chapter: int, evidence: str) -> dict[str, object]:
    return {
        "event_id": f"chapter-{chapter:04d}",
        "chapter": chapter,
        "source_draft": f"chapters/{chapter:04d}/draft.final.md",
        "source_sha256": f"hash-{chapter}",
        "entity_changes": [{"change": evidence, "source_evidence": evidence}],
        "relationship_changes": [],
        "cultivation_changes": [],
        "resource_changes": [],
        "knowledge_changes": [],
        "thread_changes": [],
        "comedy_changes": [],
        "new_constraints": [],
        "resolved_constraints": [],
        "next_chapter_inputs": [{"input": evidence}],
        "deviations": [],
    }


class StateStoreTests(unittest.TestCase):
    def test_snapshot_accumulates_events_and_changes(self) -> None:
        first = build_snapshot(event(1, "第一章变化"))
        second = build_snapshot(event(2, "第二章变化"), first)

        self.assertEqual(second["after_chapter"], 2)
        self.assertEqual(second["event_ids"], ["chapter-0001", "chapter-0002"])
        self.assertEqual(len(second["changes"]["entity_changes"]), 2)
        self.assertEqual(second["next_chapter_inputs"], [{"input": "第二章变化"}])

    def test_non_first_snapshot_requires_previous(self) -> None:
        with self.assertRaisesRegex(StateStoreError, "缺少上一章"):
            build_snapshot(event(2, "变化"))

    def test_append_event_is_idempotent_for_same_hash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            self.assertTrue(append_event_once(path, event(1, "变化")))
            self.assertFalse(append_event_once(path, event(1, "变化")))
            self.assertEqual(len(load_events(path)), 1)

    def test_append_event_rejects_same_id_with_different_hash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            first = event(1, "变化")
            second = {**first, "source_sha256": "different"}
            append_event_once(path, first)
            with self.assertRaisesRegex(StateStoreError, "哈希不同"):
                append_event_once(path, second)

    def test_load_events_reports_corrupt_line(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            path.write_text("{not-json}\n", encoding="utf-8")
            with self.assertRaisesRegex(StateStoreError, "第 1 行"):
                load_events(path)


if __name__ == "__main__":
    unittest.main()
