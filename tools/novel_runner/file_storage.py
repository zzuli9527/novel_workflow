"""Storage-layout helpers for the compact FileStorage v2 format.

V1 runs deliberately keep their original paths. V2 is selected explicitly by
``run.json.storage_version`` so historical runs remain read-compatible.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any
import zipfile

from .storage import append_jsonl, atomic_write_json, read_json


V1_STORAGE_VERSION = "1.0"
V2_STORAGE_VERSION = "2.0"


def storage_version(run_config: dict[str, Any]) -> str:
    value = run_config.get("storage_version")
    if value is None:
        return V1_STORAGE_VERSION
    if value in {V1_STORAGE_VERSION, V2_STORAGE_VERSION}:
        return str(value)
    raise ValueError(f"不支持的 storage_version：{value!r}")


def is_v2(run_config: dict[str, Any]) -> bool:
    return storage_version(run_config) == V2_STORAGE_VERSION


def events_path(run_dir: Path) -> Path:
    return run_dir / "state/events.jsonl"


def current_snapshot_path(run_dir: Path) -> Path:
    return run_dir / "state/current.json"


def checkpoints_path(run_dir: Path) -> Path:
    return run_dir / "state/checkpoints.jsonl"


def transaction_path(run_dir: Path, run_config: dict[str, Any]) -> Path:
    if is_v2(run_config):
        return run_dir / "state/transaction.json"
    return run_dir / "logs/commit-journal.json"


def runtime_events_path(run_dir: Path, run_config: dict[str, Any]) -> Path:
    if is_v2(run_config):
        return run_dir / "logs/runtime-events.jsonl"
    return run_dir / "logs/events.jsonl"


def ledger_current_path(run_dir: Path) -> Path:
    return run_dir / "ledgers/current.json"


def ledger_history_path(run_dir: Path) -> Path:
    return run_dir / "ledgers/history.jsonl"


def _event_digest(event: dict[str, Any]) -> str:
    canonical = {
        key: value
        for key, value in event.items()
        if key not in {"event_sha256", "sequence"}
    }
    payload = json.dumps(
        canonical, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _read_event_rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        value = json.loads(line)
        if isinstance(value, dict):
            rows.append(value)
    return rows


def prepare_event(
    run_dir: Path, run_config: dict[str, Any], event: dict[str, Any]
) -> dict[str, Any]:
    """Add the v2 sequence and content hash before appending an event."""

    if not is_v2(run_config):
        return event
    prepared = {
        **event,
        "schema_version": V2_STORAGE_VERSION,
        "sequence": len(_read_event_rows(events_path(run_dir))) + 1,
    }
    return {**prepared, "event_sha256": _event_digest(prepared)}


def enrich_v2_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return an ordered v2 representation of existing v1 events."""

    result: list[dict[str, Any]] = []
    for sequence, event in enumerate(events, start=1):
        prepared = {
            **event,
            "schema_version": V2_STORAGE_VERSION,
            "sequence": sequence,
        }
        result.append({**prepared, "event_sha256": _event_digest(prepared)})
    return result


def read_current_snapshot(
    run_dir: Path, run_config: dict[str, Any], chapter: int
) -> dict[str, Any] | None:
    """Read the prior committed snapshot from either supported layout."""

    if chapter <= 0:
        return None
    if not is_v2(run_config):
        return read_json(run_dir / f"state/snapshots/chapter-{chapter:04d}.json")
    path = current_snapshot_path(run_dir)
    if not path.exists():
        return None
    snapshot = read_json(path)
    if snapshot.get("after_chapter") != chapter:
        raise ValueError(
            f"v2 当前快照章节不连续：期望 {chapter}，实际 {snapshot.get('after_chapter')}"
        )
    return snapshot


def write_snapshot(
    run_dir: Path,
    run_config: dict[str, Any],
    chapter: int,
    snapshot: dict[str, Any],
    event: dict[str, Any],
) -> Path:
    if not is_v2(run_config):
        path = run_dir / f"state/snapshots/chapter-{chapter:04d}.json"
        atomic_write_json(path, snapshot)
        return path
    path = current_snapshot_path(run_dir)
    atomic_write_json(
        path,
        {
            **snapshot,
            "storage_version": V2_STORAGE_VERSION,
            "last_event_sequence": event.get("sequence"),
            "last_event_sha256": event.get("event_sha256"),
        },
    )
    return path


def append_checkpoint(
    run_dir: Path,
    run_config: dict[str, Any],
    *,
    unit_id: str,
    chapter_range: list[int],
) -> None:
    if not is_v2(run_config):
        return
    snapshot = read_json(current_snapshot_path(run_dir))
    append_jsonl(
        checkpoints_path(run_dir),
        {
            "schema_version": V2_STORAGE_VERSION,
            "unit_id": unit_id,
            "chapter_range": chapter_range,
            "after_chapter": snapshot.get("after_chapter"),
            "last_event_sequence": snapshot.get("last_event_sequence"),
            "last_event_sha256": snapshot.get("last_event_sha256"),
            "structured_state": snapshot.get("structured_state"),
            "next_chapter_inputs": snapshot.get("next_chapter_inputs", []),
        },
    )


def record_runtime_event(
    run_dir: Path,
    run_config: dict[str, Any],
    event: dict[str, Any],
) -> None:
    append_jsonl(runtime_events_path(run_dir, run_config), event)


def write_current_ledger(
    run_dir: Path, run_config: dict[str, Any], ledger: dict[str, Any]
) -> None:
    if not is_v2(run_config):
        return
    atomic_write_json(ledger_current_path(run_dir), ledger)
    append_jsonl(ledger_history_path(run_dir), ledger)


def archive_completed_unit_debug(
    run_dir: Path,
    run_config: dict[str, Any],
    *,
    unit_id: str,
    chapter_range: list[int],
) -> Path | None:
    """Bundle completed-unit debug files and leave only final readable state.

    The archive is local diagnostic material. It intentionally remains outside
    the public matrix archive, where raw prompts and provider payloads are not
    publishable.
    """

    if not is_v2(run_config):
        return None
    if len(chapter_range) != 2:
        raise ValueError("chapter_range 必须包含起止章节")
    start, end = chapter_range
    artifact = run_dir / "artifacts" / f"{unit_id}.zip"
    if artifact.exists():
        return artifact
    artifact.parent.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for chapter in range(start, end + 1):
        chapter_dir = run_dir / f"chapters/{chapter:04d}"
        if chapter_dir.exists():
            paths.extend(path for path in chapter_dir.rglob("*") if path.is_file())
    generated = run_dir / "planning/generated"
    if generated.exists():
        paths.extend(path for path in generated.rglob("*") if path.is_file())
    ledger_dir = run_dir / "ledgers"
    if ledger_dir.exists():
        paths.extend(
            path
            for path in ledger_dir.glob("batch-*")
            if path.is_file()
        )
    with zipfile.ZipFile(artifact, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(set(paths)):
            archive.write(path, path.relative_to(run_dir).as_posix())

    for chapter in range(start, end + 1):
        chapter_dir = run_dir / f"chapters/{chapter:04d}"
        if not chapter_dir.exists():
            continue
        for path in chapter_dir.rglob("*"):
            if path.is_file() and path.name != "draft.final.md":
                path.unlink()
        for path in sorted(chapter_dir.rglob("*"), reverse=True):
            if path.is_dir() and not any(path.iterdir()):
                path.rmdir()
    for path in paths:
        if path.is_file() and path.parent == generated or (
            path.is_file() and path.parent == ledger_dir and path.name.startswith("batch-")
        ):
            path.unlink(missing_ok=True)
    return artifact
