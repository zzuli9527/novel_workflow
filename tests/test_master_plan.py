from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.cli import main
from tools.novel_runner.config import init_run, validate_run_directory
from tools.novel_runner.master_plan import (
    MasterPlanError,
    approve_master_plan,
    require_approved_master_plan,
    validate_master_plan,
)
from tools.novel_runner.storage import atomic_write_json
from tests.master_plan_support import build_master_plan


class MasterPlanTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.run_dir = init_run(self.root, "master-run")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _write_plan(self, plan: dict[str, object]) -> None:
        atomic_write_json(self.run_dir / "config/master-plan.json", plan)

    def test_init_creates_structurally_valid_draft_master_plan(self) -> None:
        plan = json.loads(
            (self.run_dir / "config/master-plan.json").read_text(encoding="utf-8")
        )
        self.assertEqual(plan["approval"]["status"], "draft")
        self.assertIsNone(plan["target_chapters"]["end"])
        self.assertTrue(validate_run_directory(self.root, "master-run").valid)
        report = validate_master_plan(self.root, "master-run")
        self.assertFalse(report.valid)
        self.assertEqual(report.status, "draft")

    def test_missing_master_plan_is_invalid_run_configuration(self) -> None:
        (self.run_dir / "config/master-plan.json").unlink()

        report = validate_run_directory(self.root, "master-run")

        self.assertFalse(report.valid)
        self.assertTrue(
            any(issue.path == "config/master-plan.json" for issue in report.issues)
        )

    def test_invalid_approval_status_and_incomplete_approved_plan_are_rejected(self) -> None:
        plan = json.loads(
            (self.run_dir / "config/master-plan.json").read_text(encoding="utf-8")
        )
        plan["approval"]["status"] = "reviewing"
        self._write_plan(plan)
        report = validate_master_plan(self.root, "master-run")
        self.assertFalse(report.valid)
        self.assertTrue(
            any(issue.path == "master_plan.approval.status" for issue in report.issues)
        )

        plan["approval"] = {
            "status": "approved",
            "approved_at": "2026-01-01T00:00:00+00:00",
            "content_sha256": "stale",
        }
        self._write_plan(plan)
        report = validate_master_plan(self.root, "master-run")
        self.assertFalse(report.valid)
        self.assertTrue(
            any(issue.path == "master_plan.target_chapters.end" for issue in report.issues)
        )

    def test_approves_complete_plan_and_records_content_hash(self) -> None:
        self._write_plan(build_master_plan([("unit-0001", 1, 10)]))

        result = approve_master_plan(self.root, "master-run")

        self.assertEqual(result["status"], "approved")
        report = validate_master_plan(self.root, "master-run")
        self.assertTrue(report.valid, report.issues)
        self.assertEqual(result["content_sha256"], report.content_sha256)
        require_approved_master_plan(self.root, "master-run")

    def test_changed_approved_content_invalidates_hash_until_reapproved(self) -> None:
        plan = build_master_plan([("unit-0001", 1, 10)])
        self._write_plan(plan)
        first = approve_master_plan(self.root, "master-run")
        stored = json.loads(
            (self.run_dir / "config/master-plan.json").read_text(encoding="utf-8")
        )
        stored["final_conflict"]["antagonist_goal"] = "改写后的终局目标"
        atomic_write_json(self.run_dir / "config/master-plan.json", stored)

        with self.assertRaisesRegex(MasterPlanError, "内容已变化"):
            require_approved_master_plan(self.root, "master-run")

        second = approve_master_plan(self.root, "master-run")
        self.assertNotEqual(first["content_sha256"], second["content_sha256"])
        require_approved_master_plan(self.root, "master-run")

    def test_rejects_gapped_rough_units(self) -> None:
        plan = build_master_plan(
            [("unit-0001", 1, 10), ("unit-0002", 11, 20)]
        )
        plan["volumes"][0]["rough_units"][1]["chapter_range"] = [12, 21]
        self._write_plan(plan)

        with self.assertRaisesRegex(MasterPlanError, "空档"):
            approve_master_plan(self.root, "master-run")

    def test_rejects_overlapping_volumes(self) -> None:
        plan = build_master_plan(
            [("unit-0001", 1, 10), ("unit-0002", 11, 20)]
        )
        first_volume = plan["volumes"][0]
        first_volume["chapter_range"] = [1, 10]
        first_volume["rough_units"] = first_volume["rough_units"][:1]
        plan["volumes"].append(
            {
                **first_volume,
                "volume_id": "volume-02",
                "chapter_range": [10, 20],
                "rough_units": [
                    {
                        **plan["volumes"][0]["rough_units"][0],
                        "unit_id": "unit-0002",
                        "chapter_range": [10, 20],
                    }
                ],
            }
        )
        self._write_plan(plan)

        with self.assertRaisesRegex(MasterPlanError, "重叠"):
            approve_master_plan(self.root, "master-run")

    def test_story_unit_length_boundaries_accept_10_and_20(self) -> None:
        for run_id, end in (("ten", 10), ("twenty", 20)):
            with self.subTest(end=end):
                init_run(self.root, run_id)
                atomic_write_json(
                    self.root / "runs" / run_id / "config/master-plan.json",
                    build_master_plan([("unit-0001", 1, end)]),
                )
                approve_master_plan(self.root, run_id)

    def test_story_unit_length_boundaries_reject_9_and_21(self) -> None:
        for end in (9, 21):
            with self.subTest(end=end):
                self._write_plan(build_master_plan([("unit-0001", 1, end)]))
                with self.assertRaisesRegex(MasterPlanError, "10～20"):
                    approve_master_plan(self.root, "master-run")

    def test_existing_story_unit_cannot_diverge_during_reapproval(self) -> None:
        atomic_write_json(
            self.run_dir / "planning/story-units.json",
            [{"unit_id": "unit-0001", "chapter_range": [1, 12]}],
        )
        self._write_plan(build_master_plan([("unit-0001", 1, 10)]))

        with self.assertRaisesRegex(MasterPlanError, "范围.*不一致"):
            approve_master_plan(self.root, "master-run")

    def test_cli_validates_and_approves_master_plan(self) -> None:
        self._write_plan(build_master_plan([("unit-0001", 1, 10)]))
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            validate_exit = main(
                [
                    "validate-master-plan",
                    "--run",
                    "master-run",
                    "--root",
                    str(self.root),
                ]
            )
            approve_exit = main(
                [
                    "approve-master-plan",
                    "--run",
                    "master-run",
                    "--root",
                    str(self.root),
                    "--json",
                ]
            )

        self.assertEqual(validate_exit, 0)
        self.assertEqual(approve_exit, 0)
        self.assertIn("valid (draft)", stdout.getvalue())
        self.assertIn('"status": "approved"', stdout.getvalue())
        self.assertEqual(stderr.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
