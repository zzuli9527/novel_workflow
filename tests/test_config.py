from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import tempfile
from unittest.mock import patch
import unittest

from tools.novel_runner.cli import main
from tools.novel_runner.config import init_run, validate_run_directory
from tools.novel_runner.state_machine import (
    StateTransitionError,
    ensure_chapter_can_start,
    ensure_transition,
    transition_record,
)
from tools.novel_runner.storage import StorageError


class RunInitializationTests(unittest.TestCase):
    def test_init_run_creates_minimum_structure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "demo-run")

            self.assertTrue((run_dir / "run.json").is_file())
            self.assertTrue((run_dir / "config/progression.json").is_file())
            self.assertTrue((run_dir / "config/comedy-bible.json").is_file())
            self.assertTrue((run_dir / "config/initial-state.json").is_file())
            self.assertTrue((run_dir / "planning/story-units.json").is_file())
            self.assertTrue((run_dir / "planning/chapter-outlines.json").is_file())
            self.assertTrue((run_dir / "logs/tasks.jsonl").is_file())
            self.assertTrue((run_dir / "state/snapshots").is_dir())

            report = validate_run_directory(root, "demo-run")
            self.assertTrue(report.valid, report.issues)

    def test_init_run_does_not_overwrite_existing_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            init_run(root, "demo-run")
            with self.assertRaisesRegex(StorageError, "已存在"):
                init_run(root, "demo-run")

    def test_rejects_unsafe_run_id(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(StorageError):
                init_run(Path(directory), "../escape")

    def test_validation_detects_invalid_length_order(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "demo-run")
            path = run_dir / "run.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["policies"]["length"]["target_min"] = 3100
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

            report = validate_run_directory(root, "demo-run")
            self.assertFalse(report.valid)
            self.assertTrue(
                any(issue.path == "run.policies.length" for issue in report.issues)
            )

    def test_validation_accepts_preferred_length_range_inside_hard_range(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "demo-run")
            path = run_dir / "run.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["policies"]["length"].update(
                {"preferred_min": 2200, "preferred_max": 2500}
            )
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

            report = validate_run_directory(root, "demo-run")
            self.assertTrue(report.valid, report.issues)

    def test_validation_rejects_preferred_length_range_outside_hard_range(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "demo-run")
            path = run_dir / "run.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["policies"]["length"].update(
                {"preferred_min": 1900, "preferred_max": 2250}
            )
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

            report = validate_run_directory(root, "demo-run")
            self.assertFalse(report.valid)
            self.assertTrue(
                any(issue.path == "run.policies.length" for issue in report.issues)
            )

    def test_validation_detects_run_id_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "demo-run")
            path = run_dir / "run.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["run_id"] = "another-run"
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

            report = validate_run_directory(root, "demo-run")
            self.assertFalse(report.valid)
            self.assertTrue(any(issue.path == "run.run_id" for issue in report.issues))


class StateMachineTests(unittest.TestCase):
    def test_allows_declared_transition(self) -> None:
        ensure_transition("outline_ready", "drafting")
        record = transition_record({"number": 1, "status": "outline_ready"}, "drafting")
        self.assertEqual(record["status"], "drafting")

    def test_blocks_skipping_directly_to_committed(self) -> None:
        with self.assertRaisesRegex(StateTransitionError, "不允许"):
            ensure_transition("outline_ready", "committed")

    def test_failed_draft_can_only_restart_drafting(self) -> None:
        ensure_transition("draft_failed_length", "drafting")
        ensure_transition("draft_failed_provider", "drafting")
        with self.assertRaises(StateTransitionError):
            ensure_transition("draft_failed_length", "state_extracting")

    def test_next_chapter_guard(self) -> None:
        ensure_chapter_can_start(1, 0)
        ensure_chapter_can_start(4, 3)
        with self.assertRaisesRegex(StateTransitionError, "只能开始第 4 章"):
            ensure_chapter_can_start(5, 3)


class ConfigCliTests(unittest.TestCase):
    def test_cli_init_and_validate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            stdout = io.StringIO()
            stderr = io.StringIO()
            with redirect_stdout(stdout), redirect_stderr(stderr):
                init_exit = main(["init", "demo-run", "--root", directory])
                validate_exit = main(
                    ["validate-config", "--run", "demo-run", "--root", directory]
                )

            self.assertEqual(init_exit, 0)
            self.assertEqual(validate_exit, 0)
            self.assertIn("valid", stdout.getvalue())
            self.assertEqual(stderr.getvalue(), "")

    def test_openai_command_preflights_routed_model_before_chapter_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "demo-run")
            stderr = io.StringIO()
            with patch.dict(
                "os.environ",
                {
                    "MESHYCODE_API_KEY": "secret",
                    "MESHYCODE_BASE_URL": "https://api.example.test/v1",
                },
                clear=True,
            ), redirect_stderr(stderr):
                exit_code = main(
                    [
                        "draft",
                        "--run",
                        "demo-run",
                        "--chapter",
                        "1",
                        "--openai",
                        "--root",
                        directory,
                    ]
                )

            self.assertEqual(exit_code, 1)
            self.assertIn("NOVEL_MODEL_PLANNER", stderr.getvalue())
            self.assertFalse((run_dir / "chapters/0001").exists())

    def test_default_config_keeps_gateway_and_models_in_environment(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "demo-run")
            data = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
            provider = data["provider"]
            self.assertEqual(provider["base_url"], "")
            self.assertEqual(provider["base_url_env"], "MESHYCODE_BASE_URL")
            self.assertEqual(provider["api_key_env"], "MESHYCODE_API_KEY")
            self.assertEqual(
                provider["routes"]["drafter"]["model_env"],
                "NOVEL_MODEL_REWRITER",
            )
            self.assertEqual(
                provider["routes"]["drafter"]["fallback_model_envs"],
                ["NOVEL_MODEL_REVIEWER"],
            )
            self.assertEqual(
                provider["routes"]["rewriter"]["fallback_model_envs"],
                ["NOVEL_MODEL_DRAFTER"],
            )
            self.assertEqual(
                data["policies"]["batch"]["outline_request_chunk_size"], 2
            )
            self.assertEqual(provider["deadline_seconds"], 300)
            self.assertEqual(provider["routes"]["planner"]["deadline_seconds"], 300)
            self.assertEqual(provider["routes"]["reviewer"]["deadline_seconds"], 240)
            self.assertNotIn("efficiency", data["policies"])
            self.assertEqual(
                data["policies"]["budget"],
                {"max_calls": None, "max_tokens": None, "max_cost": None},
            )

    def test_validation_accepts_positive_or_null_deadlines(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "demo-run")
            path = run_dir / "run.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["provider"]["deadline_seconds"] = 45
            data["provider"]["routes"]["state"]["deadline_seconds"] = None
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            report = validate_run_directory(root, "demo-run")
            self.assertTrue(report.valid, report.issues)

    def test_validation_rejects_invalid_deadlines(self) -> None:
        for value in (0, -1, True, "300"):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                run_dir = init_run(root, "demo-run")
                path = run_dir / "run.json"
                data = json.loads(path.read_text(encoding="utf-8"))
                data["provider"]["deadline_seconds"] = value
                data["provider"]["routes"]["state"]["deadline_seconds"] = value
                path.write_text(
                    json.dumps(data, ensure_ascii=False), encoding="utf-8"
                )
                report = validate_run_directory(root, "demo-run")
                paths = {issue.path for issue in report.issues}
                self.assertIn("run.provider.deadline_seconds", paths)
                self.assertIn(
                    "run.provider.routes.state.deadline_seconds", paths
                )

    def test_validation_ignores_legacy_efficiency_thresholds(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "demo-run")
            path = run_dir / "run.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["policies"]["efficiency"] = {
                "warning_calls": 61,
                "hard_calls": 60,
            }
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            report = validate_run_directory(root, "demo-run")
            self.assertTrue(report.valid, report.issues)

    def test_cli_validate_outline_returns_structured_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "demo-run")
            (run_dir / "planning/chapter-outlines.json").write_text(
                json.dumps(
                    [
                        {
                            "chapter_id": "chapter-0001",
                            "number": 1,
                            "status": "outline_ready",
                        }
                    ],
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exit_code = main(
                    [
                        "validate-outline",
                        "--run",
                        "demo-run",
                        "--chapter",
                        "1",
                        "--root",
                        directory,
                        "--json",
                    ]
                )

            self.assertEqual(exit_code, 1)
            result = json.loads(stdout.getvalue())
            self.assertFalse(result["valid"])
            self.assertTrue(any(item["path"] == "intent" for item in result["issues"]))


if __name__ == "__main__":
    unittest.main()
