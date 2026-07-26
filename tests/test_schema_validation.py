from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tests.workflow_support import install_minimal_workflow
from tools.novel_runner.config import init_run, validate_run_directory
from tools.novel_runner.schema_validation import (
    WorkflowSchemaError,
    ensure_artifact_schema,
)


class WorkflowSchemaTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        install_minimal_workflow(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_default_run_artifacts_pass_workflow_schemas(self) -> None:
        init_run(self.root, "demo-run")

        report = validate_run_directory(self.root, "demo-run")

        self.assertTrue(report.valid, report.issues)

    def test_config_validation_reports_schema_failure(self) -> None:
        run_dir = init_run(self.root, "demo-run")
        path = run_dir / "run.json"
        run = json.loads(path.read_text(encoding="utf-8"))
        run["last_committed_chapter"] = "one"
        path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")

        report = validate_run_directory(self.root, "demo-run")

        self.assertFalse(report.valid)
        self.assertTrue(
            any(item.path == "run.json.schema" for item in report.issues)
        )

    def test_state_event_schema_is_enforced_at_runtime_boundary(self) -> None:
        with self.assertRaisesRegex(WorkflowSchemaError, "event_id"):
            ensure_artifact_schema(
                self.root,
                "state_event",
                {
                    "chapter": 1,
                    "source_draft": "chapters/0001/draft.final.md",
                    "source_sha256": "abc",
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
                },
            )
