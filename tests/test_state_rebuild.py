from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.config import init_run
from tools.novel_runner.state_rebuild import StateRebuildError, rebuild_state_snapshots


def _event(chapter: int, draft_text: str) -> dict[str, object]:
    return {
        "event_id": f"chapter-{chapter:04d}",
        "chapter": chapter,
        "source_draft": f"chapters/{chapter:04d}/draft.final.md",
        "source_sha256": hashlib.sha256(draft_text.encode("utf-8")).hexdigest(),
        "entity_changes": [],
        "relationship_changes": [],
        "cultivation_changes": [],
        "resource_changes": [],
        "knowledge_changes": [],
        "thread_changes": [],
        "comedy_changes": [],
        "new_constraints": [],
        "resolved_constraints": [],
        "next_chapter_inputs": [f"第{chapter}章结束"],
        "deviations": [],
    }


class StateRebuildTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.run_dir = init_run(self.root, "rebuild-run")
        events = []
        for chapter in (1, 2):
            draft = f"# 第 {chapter} 章：测试\n第{chapter}章正文"
            chapter_dir = self.run_dir / f"chapters/{chapter:04d}"
            chapter_dir.mkdir(parents=True)
            (chapter_dir / "draft.final.md").write_text(draft, encoding="utf-8")
            events.append(_event(chapter, draft))
        (self.run_dir / "state/events.jsonl").write_text(
            "\n".join(json.dumps(item, ensure_ascii=False) for item in events) + "\n",
            encoding="utf-8",
        )
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["last_committed_chapter"] = 2
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_rebuilds_all_snapshots_and_is_idempotent(self) -> None:
        first = rebuild_state_snapshots(self.root, "rebuild-run")
        second = rebuild_state_snapshots(self.root, "rebuild-run")

        self.assertEqual(first["changed_chapters"], [1, 2])
        self.assertEqual(second["unchanged_chapters"], [1, 2])
        final = json.loads(
            (self.run_dir / "state/snapshots/chapter-0002.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(final["event_ids"], ["chapter-0001", "chapter-0002"])

    def test_rejects_draft_hash_drift_before_writing(self) -> None:
        (self.run_dir / "chapters/0002/draft.final.md").write_text(
            "正文被改写", encoding="utf-8"
        )

        with self.assertRaisesRegex(StateRebuildError, "正文哈希"):
            rebuild_state_snapshots(self.root, "rebuild-run")

        self.assertFalse(
            (self.run_dir / "state/snapshots/chapter-0001.json").exists()
        )


if __name__ == "__main__":
    unittest.main()
