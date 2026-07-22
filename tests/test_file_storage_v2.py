from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.config import init_run
from tools.novel_runner.file_storage import enrich_v2_events, transaction_path
from tools.novel_runner.state_rebuild import rebuild_state_snapshots
from tools.novel_runner.storage import atomic_write_json, atomic_write_text, read_json


STATE_FIELDS = (
    "entity_changes",
    "relationship_changes",
    "cultivation_changes",
    "resource_changes",
    "knowledge_changes",
    "thread_changes",
    "comedy_changes",
    "new_constraints",
    "resolved_constraints",
)


class FileStorageV2StressTests(unittest.TestCase):
    def test_200_chapter_replay_100k_event_file_and_transaction_cycles(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_dir = init_run(root, "stress-run", storage_version="2.0")
            run_path = run_dir / "run.json"
            run = read_json(run_path)
            run["last_committed_chapter"] = 200
            atomic_write_json(run_path, run)

            events: list[dict[str, object]] = []
            for chapter in range(1, 201):
                draft = f"# 第 {chapter} 章：压力测试\n正文{chapter}\n"
                draft_path = run_dir / f"chapters/{chapter:04d}/draft.final.md"
                atomic_write_text(draft_path, draft)
                events.append(
                    {
                        "state_schema_version": "1.1",
                        "event_id": f"chapter-{chapter:04d}",
                        "chapter": chapter,
                        "source_draft": draft_path.relative_to(run_dir).as_posix(),
                        "source_sha256": hashlib.sha256(draft.encode("utf-8")).hexdigest(),
                        **{field: [] for field in STATE_FIELDS},
                        "next_chapter_inputs": [],
                        "deviations": [],
                    }
                )
            enriched = enrich_v2_events(events)
            atomic_write_text(
                run_dir / "state/events.jsonl",
                "".join(json.dumps(event, ensure_ascii=False) + "\n" for event in enriched),
            )

            first = rebuild_state_snapshots(root, "stress-run")
            second = rebuild_state_snapshots(root, "stress-run")
            self.assertEqual(first["changed_chapters"], list(range(1, 201)))
            self.assertEqual(second["changed_chapters"], [])
            self.assertEqual(second["unchanged_chapters"], list(range(1, 201)))

            journal = transaction_path(run_dir, read_json(run_path))
            for index in range(100):
                atomic_write_json(journal, {"phase": index, "chapter": 200})
                self.assertEqual(read_json(journal)["phase"], index)
                journal.unlink()
            self.assertFalse(journal.exists())

            load_rows = [
                json.dumps({"event_kind": "pressure", "sequence": index})
                for index in range(1, 100001)
            ]
            atomic_write_text(run_dir / "state/events.jsonl", "\n".join(load_rows) + "\n")
            self.assertEqual(
                len((run_dir / "state/events.jsonl").read_text(encoding="utf-8").splitlines()),
                100000,
            )
            for unit in range(1, 21):
                atomic_write_text(run_dir / f"artifacts/unit-{unit:04d}.zip", "debug")

            structured = [
                path
                for path in (run_dir / "state").iterdir()
                if path.is_file()
            ] + [
                path
                for path in (run_dir / "ledgers").iterdir()
                if path.is_file()
            ]
            self.assertLessEqual(len(structured), 15)
            all_files = [path for path in run_dir.rglob("*") if path.is_file()]
            self.assertLessEqual(len(all_files), 300)
            for folder in (run_dir, run_dir / "state", run_dir / "artifacts"):
                self.assertLessEqual(len(list(folder.iterdir())), 1000)


if __name__ == "__main__":
    unittest.main()
