from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.config import init_run
from tools.novel_runner.storage_migration import audit_storage_migration


class StorageMigrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.run_dir = init_run(self.root, "legacy-run")
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["last_committed_chapter"] = 1
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")
        event = {
            "state_schema_version": "1.1",
            "event_id": "chapter-0001",
            "chapter": 1,
            "source_draft": "chapters/0001/draft.final.md",
            "source_sha256": "hash",
        }
        (self.run_dir / "state/events.jsonl").write_text(
            json.dumps(event, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        (self.run_dir / "state/snapshots/chapter-0001.json").write_text(
            json.dumps(
                {
                    "after_chapter": 1,
                    "event_ids": ["chapter-0001"],
                    "changes": {},
                    "structured_state": {},
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        (self.run_dir / "ledgers/batch-0001-0003.json").write_text(
            json.dumps({"batch_id": "batch-0001-0003", "must_read_next": []}),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_dry_run_reports_without_changing_legacy_run(self) -> None:
        result = audit_storage_migration(self.root, "legacy-run")

        self.assertEqual(result["status"], "dry_run")
        self.assertTrue(result["dry_run"])
        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertNotIn("storage_version", run)
        self.assertFalse((self.run_dir / "state/current.json").exists())

    def test_apply_backs_up_and_switches_atomically_to_v2_files(self) -> None:
        result = audit_storage_migration(self.root, "legacy-run", apply=True)

        self.assertEqual(result["status"], "migrated")
        self.assertTrue(Path(result["backup_path"]).is_file())
        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(run["storage_version"], "2.0")
        event = json.loads(
            (self.run_dir / "state/events.jsonl").read_text(encoding="utf-8")
        )
        self.assertEqual(event["sequence"], 1)
        self.assertTrue(event["event_sha256"])
        current = json.loads(
            (self.run_dir / "state/current.json").read_text(encoding="utf-8")
        )
        self.assertEqual(current["last_event_sequence"], 1)
        self.assertTrue((self.run_dir / "ledgers/current.json").is_file())
        self.assertTrue((self.run_dir / "logs/runtime-events.jsonl").is_file())
        repeat = audit_storage_migration(self.root, "legacy-run")
        self.assertEqual(repeat["status"], "already_v2")


if __name__ == "__main__":
    unittest.main()
