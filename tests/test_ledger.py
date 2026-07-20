from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.config import init_run
from tools.novel_runner.ledger import LedgerError, build_ledger
from tools.novel_runner.provider import FixtureProvider
from tools.novel_runner.state_store import append_event_once, build_snapshot


VALID_LEDGER = {
    "must_read_next": ["当前限制", "下一步行动"],
    "active_progression": ["修炼进度"],
    "active_resources": ["关键资源"],
    "active_relationships": [],
    "active_knowledge_gaps": ["角色仍有误会"],
    "active_threads": ["未完成任务"],
    "comedy_callbacks": ["可升级回调"],
    "avoid_repeating": ["暂停重复误会"],
    "archived": [],
    "next_batch_adjustments": ["切换喜剧机制"],
}


def make_event(chapter: int) -> dict[str, object]:
    return {
        "event_id": f"chapter-{chapter:04d}",
        "chapter": chapter,
        "source_draft": f"chapters/{chapter:04d}/draft.final.md",
        "source_sha256": f"hash-{chapter}",
        "entity_changes": [],
        "relationship_changes": [],
        "cultivation_changes": [],
        "resource_changes": [],
        "knowledge_changes": [],
        "thread_changes": [],
        "comedy_changes": [],
        "new_constraints": [],
        "resolved_constraints": [],
        "next_chapter_inputs": [],
        "deviations": [],
    }


class LedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        workflow = self.root / "workflow"
        workflow.mkdir()
        (workflow / "05-update-state.md").write_text("# 账本规则\n", encoding="utf-8")
        self.run_dir = init_run(self.root, "demo-run")

        outlines = [
            {
                "chapter_id": f"chapter-{number:04d}",
                "number": number,
                "status": "committed",
            }
            for number in range(1, 4)
        ]
        (self.run_dir / "planning/chapter-outlines.json").write_text(
            json.dumps(outlines, ensure_ascii=False), encoding="utf-8"
        )
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["last_committed_chapter"] = 3
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")

        previous = None
        events_path = self.run_dir / "state/events.jsonl"
        for chapter in range(1, 4):
            current = make_event(chapter)
            append_event_once(events_path, current)
            previous = build_snapshot(current, previous)
            (self.run_dir / f"state/snapshots/chapter-{chapter:04d}.json").write_text(
                json.dumps(previous, ensure_ascii=False), encoding="utf-8"
            )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _provider(self, name: str, payload: dict[str, object]) -> FixtureProvider:
        path = self.root / name
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        return FixtureProvider(path)

    def _add_structured_snapshot_state(self) -> None:
        path = self.run_dir / "state/snapshots/chapter-0003.json"
        snapshot = json.loads(path.read_text(encoding="utf-8"))
        snapshot["structured_state"] = {
            "cultivation": [
                {
                    "subject_id": "protagonist",
                    "stage": "炼气一层",
                    "abilities": [],
                    "injuries": [],
                    "limits": ["经脉承载有限"],
                }
            ],
            "resources": [
                {
                    "owner_id": "protagonist",
                    "resource_id": "spirit_stone_low",
                    "amount": 2.0,
                    "unit": "枚",
                }
            ],
            "knowledge": [
                {
                    "character_id": "companion",
                    "fact_id": "protagonist_injury",
                    "state": "suspects",
                    "belief": "主角可能受伤",
                }
            ],
        }
        path.write_text(json.dumps(snapshot, ensure_ascii=False), encoding="utf-8")

    def test_builds_json_and_markdown_ledger(self) -> None:
        ledger = build_ledger(
            self.root,
            "demo-run",
            1,
            3,
            self._provider("ledger.json", VALID_LEDGER),
        )
        self.assertEqual(ledger["batch_id"], "batch-0001-0003")
        self.assertEqual(ledger["source_event_ids"], [
            "chapter-0001",
            "chapter-0002",
            "chapter-0003",
        ])
        self.assertTrue((self.run_dir / "ledgers/batch-0001-0003.json").exists())
        markdown = (self.run_dir / "ledgers/batch-0001-0003.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("下一批必读", markdown)
        self.assertIn("暂停重复误会", markdown)

    def test_rejects_must_read_over_limit(self) -> None:
        invalid = {**VALID_LEDGER, "must_read_next": [str(i) for i in range(9)]}
        with self.assertRaisesRegex(LedgerError, "超过上限"):
            build_ledger(
                self.root,
                "demo-run",
                1,
                3,
                self._provider("too-heavy.json", invalid),
            )
        self.assertFalse((self.run_dir / "ledgers/batch-0001-0003.json").exists())

    def test_rejects_range_outside_configured_size(self) -> None:
        with self.assertRaisesRegex(LedgerError, "必须覆盖"):
            build_ledger(
                self.root,
                "demo-run",
                1,
                2,
                self._provider("ledger.json", VALID_LEDGER),
            )

    def test_rejects_uncommitted_chapter(self) -> None:
        path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(path.read_text(encoding="utf-8"))
        outlines[1]["status"] = "draft_passed"
        path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")
        with self.assertRaisesRegex(LedgerError, "尚未提交"):
            build_ledger(
                self.root,
                "demo-run",
                1,
                3,
                self._provider("ledger.json", VALID_LEDGER),
            )

    def test_fills_structured_active_state_when_model_omits_it(self) -> None:
        self._add_structured_snapshot_state()
        invalid = {
            **VALID_LEDGER,
            "active_progression": [],
            "active_resources": [],
            "active_knowledge_gaps": [],
        }
        ledger = build_ledger(
            self.root,
            "demo-run",
            1,
            3,
            self._provider("missing-structured.json", invalid),
        )
        self.assertEqual(ledger["active_progression"][0]["stage"], "炼气一层")
        self.assertEqual(ledger["active_resources"][0]["amount"], 2.0)
        self.assertEqual(
            ledger["active_knowledge_gaps"][0]["state"], "suspects"
        )

    def test_accepts_ledger_covering_structured_active_state(self) -> None:
        self._add_structured_snapshot_state()
        valid = {
            **VALID_LEDGER,
            "active_progression": [
                {
                    "subject_id": "protagonist",
                    "stage": "炼气一层",
                    "limits": ["经脉承载有限"],
                }
            ],
            "active_resources": [
                {
                    "owner_id": "protagonist",
                    "resource_id": "spirit_stone_low",
                    "amount": 2.0,
                    "unit": "枚",
                }
            ],
            "active_knowledge_gaps": [
                {
                    "character_id": "companion",
                    "fact_id": "protagonist_injury",
                    "state": "suspects",
                    "belief": "主角可能受伤",
                }
            ],
        }
        ledger = build_ledger(
            self.root,
            "demo-run",
            1,
            3,
            self._provider("structured-ledger.json", valid),
        )
        self.assertEqual(ledger["active_resources"][0]["amount"], 2.0)


if __name__ == "__main__":
    unittest.main()
