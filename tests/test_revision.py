from __future__ import annotations

import json
from contextlib import redirect_stdout
import io
from pathlib import Path
import tempfile
from unittest.mock import patch
import unittest

from tools.novel_runner.chapter_service import resume_run
from tools.novel_runner.cli import main
from tools.novel_runner.config import init_run
from tools.novel_runner.revision import RevisionError, invalidate_from
from tools.novel_runner.state_store import append_event_once, build_snapshot, load_events


def event(chapter: int) -> dict[str, object]:
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


class RevisionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.run_dir = init_run(self.root, "revision-run")
        outlines = []
        previous = None
        events_path = self.run_dir / "state/events.jsonl"
        for chapter in range(1, 4):
            outline = {
                "chapter_id": f"chapter-{chapter:04d}",
                "number": chapter,
                "title": f"正式章{chapter}",
                "story_unit_id": "unit-0001",
                "status": "committed",
                "intent": "推进正式修炼任务",
                "opening_state": [],
                "required_outcomes": ["完成本章行动"],
                "forbidden_outcomes": ["无代价突破"],
                "progression_payoff": "修炼状态发生变化",
                "comedy_mechanism": ["性格反差", "信息差", "规则错位"][chapter - 1],
                "comedy_payoff": "笑点改变行动",
                "cost_or_aftereffect": "保留实际代价",
                "closing_state": ["本章形成可承接结果"],
                "next_chapter_input": ["继续处理本章后果"],
                "target_length": {"min": 2000, "max": 3000},
                "scenes": [
                    {
                        "scene_id": f"chapter-{chapter:04d}-scene-1",
                        "intent": "建立问题",
                        "target_length": 1000,
                        "required_outcomes": [],
                    },
                    {
                        "scene_id": f"chapter-{chapter:04d}-scene-2",
                        "intent": "完成行动",
                        "target_length": 1100,
                        "required_outcomes": ["完成本章行动"],
                    },
                ],
                "writability": {
                    "is_writable": True,
                    "estimated_length": 2100,
                    "risks": [],
                },
                "draft_path": f"chapters/{chapter:04d}/draft.v1.md",
                "actual_length": 2100,
                "retry_counts": {"content": 1},
            }
            outlines.append(outline)
            chapter_dir = self.run_dir / f"chapters/{chapter:04d}"
            chapter_dir.mkdir(parents=True)
            (chapter_dir / "outline.json").write_text(
                json.dumps(outline, ensure_ascii=False), encoding="utf-8"
            )
            (chapter_dir / "draft.v1.md").write_text(
                f"# 第 {chapter} 章\n历史版本\n", encoding="utf-8"
            )
            (chapter_dir / "draft.final.md").write_text(
                f"# 第 {chapter} 章\n正式正文\n", encoding="utf-8"
            )
            (chapter_dir / "state-event.json").write_text(
                json.dumps(event(chapter), ensure_ascii=False), encoding="utf-8"
            )
            (chapter_dir / "checks.json").write_text("{}", encoding="utf-8")
            current = event(chapter)
            append_event_once(events_path, current)
            previous = build_snapshot(current, previous)
            (self.run_dir / f"state/snapshots/chapter-{chapter:04d}.json").write_text(
                json.dumps(previous, ensure_ascii=False), encoding="utf-8"
            )
        (self.run_dir / "planning/chapter-outlines.json").write_text(
            json.dumps(outlines, ensure_ascii=False), encoding="utf-8"
        )
        (self.run_dir / "planning/story-units.json").write_text(
            json.dumps(
                [
                    {
                        "unit_id": "unit-0001",
                        "chapter_range": [1, 3],
                        "status": "completed",
                    }
                ],
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run.update(
            {
                "status": "ready",
                "last_committed_chapter": 3,
                "current_story_unit": "unit-0001",
            }
        )
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")
        (self.run_dir / "ledgers/batch-0001-0003.json").write_text(
            "{}", encoding="utf-8"
        )
        (self.run_dir / "ledgers/batch-0001-0003.md").write_text(
            "# 旧账本\n", encoding="utf-8"
        )
        (self.run_dir / "reports/unit-unit-0001.json").write_text(
            "{}", encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_invalidate_archives_downstream_and_rewinds_active_state(self) -> None:
        manifest = invalidate_from(
            self.root,
            "revision-run",
            2,
            reason="重写第二章关键选择",
        )

        self.assertEqual(manifest["new_last_committed_chapter"], 1)
        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(run["last_committed_chapter"], 1)
        self.assertEqual(run["active_revision"], "revision-0001")
        self.assertEqual(
            [item["chapter"] for item in load_events(self.run_dir / "state/events.jsonl")],
            [1],
        )
        self.assertTrue(
            (self.run_dir / "state/snapshots/chapter-0001.json").is_file()
        )
        self.assertFalse(
            (self.run_dir / "state/snapshots/chapter-0002.json").exists()
        )
        self.assertTrue(
            (
                self.run_dir
                / "revisions/revision-0001/artifacts/state/snapshots/chapter-0002.json"
            ).is_file()
        )
        self.assertFalse((self.run_dir / "ledgers/batch-0001-0003.json").exists())
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["status"], "committed")
        self.assertEqual(outlines[1]["status"], "outline_ready")
        self.assertEqual(outlines[2]["status"], "outline_ready")
        self.assertEqual(outlines[1]["revalidation_status"], "pending")
        self.assertNotIn("draft_path", outlines[1])
        self.assertFalse((self.run_dir / "chapters/0002/draft.final.md").exists())
        self.assertTrue((self.run_dir / "chapters/0002/draft.v1.md").is_file())

    def test_validate_outline_can_accept_pending_revision(self) -> None:
        invalidate_from(
            self.root,
            "revision-run",
            2,
            reason="重验第二章章纲",
        )
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exit_code = main(
                [
                    "validate-outline",
                    "--run",
                    "revision-run",
                    "--chapter",
                    "2",
                    "--accept-revision",
                    "--json",
                    "--root",
                    str(self.root),
                ]
            )

        self.assertEqual(exit_code, 0)
        self.assertTrue(json.loads(stdout.getvalue())["accepted_revision"])
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[1]["revalidation_status"], "accepted")

    def test_revision_journal_can_resume_after_interruption(self) -> None:
        with patch(
            "tools.novel_runner.revision.apply_revision_journal",
            side_effect=RuntimeError("模拟中断"),
        ):
            with self.assertRaisesRegex(RuntimeError, "模拟中断"):
                invalidate_from(
                    self.root,
                    "revision-run",
                    2,
                    reason="模拟修订中断",
                )
        self.assertTrue((self.run_dir / "logs/revision-journal.json").is_file())

        result = resume_run(self.root, "revision-run")

        self.assertEqual(result["action"], "revision_recovered")
        self.assertFalse((self.run_dir / "logs/revision-journal.json").exists())
        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(run["last_committed_chapter"], 1)
        runtime_events = [
            json.loads(line)
            for line in (self.run_dir / "logs/events.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
        ]
        self.assertEqual(runtime_events[-1]["action"], "revision_recovered")

    def test_rejects_uncommitted_invalidation_target(self) -> None:
        with self.assertRaisesRegex(RevisionError, "最后提交"):
            invalidate_from(
                self.root,
                "revision-run",
                4,
                reason="无效请求",
            )


if __name__ == "__main__":
    unittest.main()
