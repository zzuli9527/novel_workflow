from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.config import init_run
from tools.novel_runner.reporting import generate_unit_review


QUALITY = {
    "required_outcomes": [],
    "forbidden_outcomes": [],
    "summary_like": False,
    "cultivation_consistent": True,
    "comedy_causal": True,
    "serious_consequences_preserved": True,
    "chapter_hook_concrete": True,
    "resource_continuity_consistent": True,
    "knowledge_states_consistent": True,
    "character_voices_distinct": True,
    "multi_line_causality_preserved": True,
    "warnings": [],
}


class ReportingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.run_dir = init_run(self.root, "report-run")
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["length"].update(
            {"expand_from": 3, "target_min": 5, "target_max": 7, "review_over": 9}
        )
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")
        unit = {
            "unit_id": "unit-0001",
            "chapter_range": [1, 1],
            "status": "completed",
        }
        outline = {
            "number": 1,
            "title": "测试",
            "status": "committed",
            "target_length": {"min": 5, "max": 7},
            "comedy_mechanism": "规则错位",
            "scenes": [{"target_length": 5}],
        }
        (self.run_dir / "planning/story-units.json").write_text(
            json.dumps([unit], ensure_ascii=False), encoding="utf-8"
        )
        (self.run_dir / "planning/chapter-outlines.json").write_text(
            json.dumps([outline], ensure_ascii=False), encoding="utf-8"
        )
        self.chapter_dir = self.run_dir / "chapters/0001"
        self.chapter_dir.mkdir(parents=True)
        self._write_chapter("甲乙丙丁戊", QUALITY)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _write_chapter(self, body: str, quality: dict[str, object]) -> None:
        draft = f"# 第 1 章：测试\n{body}\n"
        (self.chapter_dir / "draft.v1.md").write_text(draft, encoding="utf-8")
        if len(body) < 5:
            status = "needs_expansion"
        elif len(body) <= 7:
            status = "passed"
        elif len(body) <= 9:
            status = "needs_redundancy_review"
        else:
            status = "needs_compression_review"
        checks = {
            "actual_length": len(body),
            "status": status,
            "quality": quality,
        }
        (self.chapter_dir / "checks.json").write_text(
            json.dumps(checks, ensure_ascii=False), encoding="utf-8"
        )

    def test_high_usage_is_recorded_without_affecting_verdict(self) -> None:
        records = [
            {
                "chapter": 1,
                "status": "success",
                "duration_seconds": 1,
                "usage": {
                    "total_tokens": 100000,
                    "input_characters": 50000,
                },
            }
            for _ in range(100)
        ]
        (self.run_dir / "logs/api-calls.jsonl").write_text(
            "".join(json.dumps(item) + "\n" for item in records),
            encoding="utf-8",
        )

        report = generate_unit_review(
            self.root, "report-run", "unit-0001"
        )

        self.assertEqual(report["verdict"], "通过")
        self.assertTrue(report["archivable"])
        self.assertEqual(report["metrics"]["api"]["calls"], 100)
        self.assertEqual(report["metrics"]["api"]["total_tokens"], 10000000)
        self.assertEqual(report["metrics"]["average_context_characters"], 50000)
        self.assertEqual(report["metrics"]["quality_rubric"]["total"], 17)
        self.assertTrue(report["metrics"]["quality_rubric"]["passed"])
        self.assertNotIn("efficiency", report["metrics"])
        markdown = (
            self.run_dir / "reports/story-unit-review-unit-0001.md"
        ).read_text(encoding="utf-8")
        self.assertIn("调用次数：100", markdown)
        self.assertIn("质量评分：17 / 18", markdown)
        self.assertNotIn("调用阈值", markdown)
        self.assertNotIn("效率分级", markdown)

    def test_soft_length_warning_is_archivable(self) -> None:
        self._write_chapter("甲乙丙丁", QUALITY)
        outline_path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(outline_path.read_text(encoding="utf-8"))
        outlines[0]["target_length"] = {"min": 4, "max": 7}
        outline_path.write_text(
            json.dumps(outlines, ensure_ascii=False), encoding="utf-8"
        )

        report = generate_unit_review(
            self.root, "report-run", "unit-0001"
        )

        self.assertEqual(report["verdict"], "有条件通过")
        self.assertEqual(report["usability"], "可用，待润色")
        self.assertTrue(report["archivable"])
        self.assertEqual(report["metrics"]["length_soft_warning_count"], 1)
        self.assertEqual(report["metrics"]["target_length_deviation_count"], 0)
        self.assertEqual(report["metrics"]["hard_failure_count"], 0)

    def test_hard_quality_failure_is_not_archivable(self) -> None:
        self._write_chapter(
            "甲乙丙丁戊",
            {**QUALITY, "cultivation_consistent": False},
        )

        report = generate_unit_review(
            self.root, "report-run", "unit-0001"
        )

        self.assertEqual(report["verdict"], "失败")
        self.assertEqual(report["usability"], "不可用")
        self.assertFalse(report["archivable"])
        self.assertEqual(report["metrics"]["hard_failure_count"], 1)


if __name__ == "__main__":
    unittest.main()
