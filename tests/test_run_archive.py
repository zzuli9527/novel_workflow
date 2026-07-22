from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.novel_runner.config import init_run
from tools.novel_runner.run_archive import RunArchiveError, archive_run
from tools.novel_runner.state_store import build_snapshot


class RunArchiveTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.run_dir = init_run(self.root, "archive-run")
        draft = "# 第 1 章：测试\n正文内容"
        chapter_dir = self.run_dir / "chapters/0001"
        chapter_dir.mkdir(parents=True)
        (chapter_dir / "draft.final.md").write_text(draft, encoding="utf-8")
        checks = {"actual_length": 4, "status": "passed"}
        (chapter_dir / "checks.json").write_text(
            json.dumps(checks, ensure_ascii=False), encoding="utf-8"
        )
        event = {
            "event_id": "chapter-0001",
            "chapter": 1,
            "source_draft": "chapters/0001/draft.final.md",
            "source_sha256": hashlib.sha256(draft.encode("utf-8")).hexdigest(),
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
        (self.run_dir / "state/events.jsonl").write_text(
            json.dumps(event, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        snapshot = build_snapshot(
            event,
            initial_state=json.loads(
                (self.run_dir / "config/initial-state.json").read_text(
                    encoding="utf-8"
                )
            ),
        )
        snapshot["source"] = "chapters/0001/state-event.json"
        snapshot_path = self.run_dir / "state/snapshots/chapter-0001.json"
        snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        snapshot_path.write_text(
            json.dumps(snapshot, ensure_ascii=False), encoding="utf-8"
        )
        unit = {
            "unit_id": "unit-0001",
            "chapter_range": [1, 1],
            "goal": "测试归档",
            "status": "completed",
        }
        outline = {
            "number": 1,
            "title": "测试",
            "status": "committed",
            "actual_length": 4,
            "scenes": [{"target_length": 4}],
        }
        (self.run_dir / "planning/story-units.json").write_text(
            json.dumps([unit], ensure_ascii=False), encoding="utf-8"
        )
        (self.run_dir / "planning/chapter-outlines.json").write_text(
            json.dumps([outline], ensure_ascii=False), encoding="utf-8"
        )
        reports = self.run_dir / "reports"
        review = {"verdict": "通过", "metrics": {}}
        (reports / "story-unit-review-unit-0001.json").write_text(
            json.dumps(review, ensure_ascii=False), encoding="utf-8"
        )
        (reports / "story-unit-review-unit-0001.md").write_text(
            "# 评审\n\n通过\n", encoding="utf-8"
        )
        (self.run_dir / "logs/api-calls.jsonl").write_text("", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_archives_six_fixed_artifacts_and_machine_data(self) -> None:
        result = archive_run(
            self.root, "archive-run", "unit-0001", "T-archive"
        )

        destination = self.root / result["destination"]
        for filename in result["fixed_artifacts"]:
            self.assertTrue((destination / filename).is_file())
        self.assertTrue((destination / "data/state/events.jsonl").is_file())
        self.assertIn("正文内容", (destination / "drafts.md").read_text(encoding="utf-8"))

    def test_blocks_secret_value_in_archive_content(self) -> None:
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["provider"]["api_key_env"] = "TEST_ARCHIVE_KEY"
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")
        (self.run_dir / "config/project.md").write_text(
            "项目误含 secret-value", encoding="utf-8"
        )

        with patch.dict(os.environ, {"TEST_ARCHIVE_KEY": "secret-value"}):
            with self.assertRaisesRegex(RunArchiveError, "API Key"):
                archive_run(
                    self.root, "archive-run", "unit-0001", "T-secret"
                )

    def test_archives_conditional_pass_when_hard_failures_are_zero(self) -> None:
        report_path = self.run_dir / "reports/story-unit-review-unit-0001.json"
        report_path.write_text(
            json.dumps(
                {
                    "verdict": "有条件通过",
                    "archivable": True,
                    "usability": "可用，待润色",
                    "metrics": {"hard_failure_count": 0},
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        result = archive_run(
            self.root, "archive-run", "unit-0001", "T-conditional"
        )

        self.assertEqual(result["verdict"], "有条件通过")

    def test_blocks_conditional_pass_without_archivable_marker(self) -> None:
        report_path = self.run_dir / "reports/story-unit-review-unit-0001.json"
        report_path.write_text(
            json.dumps(
                {"verdict": "有条件通过", "metrics": {}},
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(RunArchiveError, "评审未通过"):
            archive_run(
                self.root, "archive-run", "unit-0001", "T-not-archivable"
            )

    def test_blocks_conditional_pass_with_declared_hard_failure(self) -> None:
        report_path = self.run_dir / "reports/story-unit-review-unit-0001.json"
        report_path.write_text(
            json.dumps(
                {
                    "verdict": "有条件通过",
                    "archivable": True,
                    "metrics": {"hard_failure_count": 1},
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(RunArchiveError, "评审未通过"):
            archive_run(
                self.root, "archive-run", "unit-0001", "T-hard-failure"
            )


if __name__ == "__main__":
    unittest.main()
