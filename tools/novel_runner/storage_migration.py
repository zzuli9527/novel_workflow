"""Dry-run-first migration from the legacy snapshot layout to FileStorage v2."""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
from typing import Any

from .file_storage import (
    V2_STORAGE_VERSION,
    checkpoints_path,
    current_snapshot_path,
    enrich_v2_events,
    events_path,
    ledger_current_path,
    ledger_history_path,
    runtime_events_path,
    storage_version,
)
from .state_store import load_events
from .storage import StorageError, append_jsonl, atomic_write_json, atomic_write_text, read_json, resolve_run_dir, run_lock


class StorageMigrationError(RuntimeError):
    """Migration audit or atomic switch failed."""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _backup_path(run_dir: Path) -> Path:
    return run_dir.parent / f"{run_dir.name}.v1-backup.zip"


def audit_storage_migration(
    root: Path, run_id: str, *, apply: bool = False
) -> dict[str, Any]:
    """Inspect a legacy run by default; ``apply`` creates one backup then switches.

    The switch is file-atomic: all new JSON/JSONL payloads are staged in memory
    and written with atomic replacement before ``run.json`` advertises v2.
    """

    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        run = read_json(run_dir / "run.json")
        current_version = storage_version(run)
        if current_version == V2_STORAGE_VERSION:
            return {
                "run_id": run_id,
                "source_version": V2_STORAGE_VERSION,
                "target_version": V2_STORAGE_VERSION,
                "status": "already_v2",
                "dry_run": not apply,
            }
        try:
            events = load_events(events_path(run_dir))
        except StorageError as exc:
            raise StorageMigrationError(str(exc)) from exc
        last_committed = run.get("last_committed_chapter")
        if not isinstance(last_committed, int) or last_committed < 0:
            raise StorageMigrationError("run.json.last_committed_chapter 无效")
        if len(events) != last_committed:
            raise StorageMigrationError("v1 事件数与正式提交指针不一致")
        snapshot = None
        if last_committed:
            snapshot = read_json(
                run_dir / f"state/snapshots/chapter-{last_committed:04d}.json"
            )
        ledgers: list[dict[str, Any]] = []
        for path in sorted((run_dir / "ledgers").glob("batch-*.json")):
            if ".raw." in path.name:
                continue
            ledgers.append(read_json(path))
        report = {
            "run_id": run_id,
            "source_version": current_version,
            "target_version": V2_STORAGE_VERSION,
            "dry_run": not apply,
            "event_count": len(events),
            "last_committed_chapter": last_committed,
            "ledger_count": len(ledgers),
            "would_create": [
                "state/current.json",
                "state/checkpoints.jsonl",
                "state/transaction.json (only during a transaction)",
                "ledgers/current.json",
                "ledgers/history.jsonl",
                "logs/runtime-events.jsonl",
            ],
            "backup_path": _backup_path(run_dir).name,
        }
        if not apply:
            return {**report, "status": "dry_run"}

        backup = _backup_path(run_dir)
        if backup.exists():
            raise StorageMigrationError(f"迁移备份已存在：{backup.name}")
        try:
            shutil.make_archive(str(backup.with_suffix("")), "zip", run_dir)
        except (OSError, shutil.Error) as exc:
            raise StorageMigrationError(f"无法创建迁移备份：{exc}") from exc

        enriched = enrich_v2_events(events)
        atomic_write_text(
            events_path(run_dir),
            "".join(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n" for item in enriched),
        )
        if snapshot is not None:
            event = enriched[-1]
            atomic_write_json(
                current_snapshot_path(run_dir),
                {
                    **snapshot,
                    "storage_version": V2_STORAGE_VERSION,
                    "last_event_sequence": event["sequence"],
                    "last_event_sha256": event["event_sha256"],
                },
            )
        atomic_write_text(checkpoints_path(run_dir), "")
        if snapshot is not None:
            append_jsonl(
                checkpoints_path(run_dir),
                {
                    "schema_version": V2_STORAGE_VERSION,
                    "unit_id": "migration-baseline",
                    "chapter_range": [1, last_committed],
                    "after_chapter": last_committed,
                    "last_event_sequence": enriched[-1]["sequence"],
                    "last_event_sha256": enriched[-1]["event_sha256"],
                    "structured_state": snapshot.get("structured_state"),
                },
            )
        atomic_write_text(
            ledger_history_path(run_dir),
            "".join(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n" for item in ledgers),
        )
        if ledgers:
            atomic_write_json(ledger_current_path(run_dir), ledgers[-1])
        atomic_write_text(runtime_events_path(run_dir, {"storage_version": V2_STORAGE_VERSION}), "")
        append_jsonl(
            runtime_events_path(run_dir, {"storage_version": V2_STORAGE_VERSION}),
            {"timestamp": _utc_now(), "action": "storage_migrated", "from": current_version, "to": V2_STORAGE_VERSION},
        )
        atomic_write_json(
            run_dir / "run.json",
            {**run, "storage_version": V2_STORAGE_VERSION, "updated_at": _utc_now()},
        )
        return {**report, "dry_run": False, "status": "migrated", "backup_path": str(backup)}
