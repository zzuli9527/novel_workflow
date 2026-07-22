from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from tools.novel_runner import chapter_service
from tools.novel_runner.chapter_service import commit_chapter, resume_run
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


class FileStorageV2CommitRecoveryTests(unittest.TestCase):
    """Exercise the on-disk journal at every commit phase, not just its path."""

    def _new_prepared_run(self, root: Path, index: int) -> Path:
        run_id = f"fault-{index:03d}"
        run_dir = init_run(root, run_id, storage_version="2.0")
        draft = "# 第 1 章：事务恢复\n正文证据。\n"
        draft_path = run_dir / "chapters/0001/draft.final.md"
        atomic_write_text(draft_path, draft)
        digest = hashlib.sha256(draft.encode("utf-8")).hexdigest()
        event = {
            "state_schema_version": "1.1",
            "event_id": "chapter-0001",
            "chapter": 1,
            "source_draft": "chapters/0001/draft.final.md",
            "source_sha256": digest,
            **{field: [] for field in STATE_FIELDS},
            "next_chapter_inputs": [],
            "deviations": [],
        }
        atomic_write_json(run_dir / "chapters/0001/state-event.json", event)
        atomic_write_json(
            run_dir / "planning/chapter-outlines.json",
            [
                {
                    "chapter_id": "chapter-0001",
                    "number": 1,
                    "status": "state_ready",
                }
            ],
        )
        return run_dir

    def _inject_once(self, run_dir: Path, phase: int) -> None:
        if phase == 0:
            with mock.patch.object(
                chapter_service,
                "_save_outlines",
                side_effect=OSError("injected before event append"),
            ):
                with self.assertRaises(OSError):
                    commit_chapter(run_dir.parent.parent, run_dir.name, 1)
        elif phase == 1:
            with mock.patch.object(
                chapter_service,
                "append_event_once",
                side_effect=OSError("injected event append interruption"),
            ):
                with self.assertRaises(OSError):
                    commit_chapter(run_dir.parent.parent, run_dir.name, 1)
        elif phase == 2:
            with mock.patch.object(
                chapter_service,
                "write_snapshot",
                side_effect=OSError("injected snapshot interruption"),
            ):
                with self.assertRaises(OSError):
                    commit_chapter(run_dir.parent.parent, run_dir.name, 1)
        elif phase == 3:
            original = chapter_service.atomic_write_json

            def fail_run_write(path: Path, value: object) -> None:
                if path.name == "run.json":
                    raise OSError("injected run pointer interruption")
                original(path, value)

            with mock.patch.object(chapter_service, "atomic_write_json", fail_run_write):
                with self.assertRaises(OSError):
                    commit_chapter(run_dir.parent.parent, run_dir.name, 1)
        else:
            journal = run_dir / "state/transaction.json"
            original_unlink = Path.unlink

            def fail_journal_cleanup(path: Path, *args: object, **kwargs: object) -> None:
                if path == journal:
                    raise OSError("injected journal cleanup interruption")
                original_unlink(path, *args, **kwargs)

            with mock.patch.object(Path, "unlink", fail_journal_cleanup):
                with self.assertRaisesRegex(Exception, "无法清理"):
                    commit_chapter(run_dir.parent.parent, run_dir.name, 1)

    def test_100_commit_phase_interruptions_recover_without_duplicate_event(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for index in range(100):
                run_dir = self._new_prepared_run(root, index)
                self._inject_once(run_dir, index % 5)
                self.assertTrue((run_dir / "state/transaction.json").is_file())

                result = resume_run(root, run_dir.name)
                self.assertEqual(result["action"], "commit_recovered")
                self.assertEqual(result["run"]["last_committed_chapter"], 1)
                self.assertFalse((run_dir / "state/transaction.json").exists())
                self.assertEqual(
                    len((run_dir / "state/events.jsonl").read_text(encoding="utf-8").splitlines()),
                    1,
                )
                outline = read_json(run_dir / "planning/chapter-outlines.json")[0]
                self.assertEqual(outline["status"], "committed")


if __name__ == "__main__":
    unittest.main()
