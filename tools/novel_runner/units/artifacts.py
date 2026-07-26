"""Translate persisted run files into workflow artifact names."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..batching import ChapterBatch
from ..storage import read_json


def _chapter_artifacts(
    run_dir: Path,
    run_config: dict[str, Any],
    chapter: int,
    outline: dict[str, Any],
) -> set[str]:
    """Translate persisted chapter facts into workflow artifact names."""

    artifacts = {"chapter_outline"}
    last_committed = run_config.get("last_committed_chapter", 0)
    if chapter == 1 or (
        isinstance(last_committed, int) and last_committed >= chapter - 1
    ):
        artifacts.add("state_context")
    status = outline.get("status")
    if status in {
        "draft_failed_provider",
        "draft_failed_length",
        "draft_failed_contract",
        "draft_failed_quality",
    }:
        artifacts.add("failed_attempt")
    chapter_dir = run_dir / f"chapters/{chapter:04d}"
    if (chapter_dir / "draft.candidate.md").is_file():
        artifacts.add("draft_candidate")
    if (chapter_dir / "draft.final.md").is_file():
        artifacts.add("approved_draft")
    if (chapter_dir / "review.raw.json").is_file():
        artifacts.add("review")
    if (chapter_dir / "state-event.json").is_file():
        artifacts.add("state_event")
    if status in {"committed", "locked"}:
        artifacts.add("committed_chapter")
    return artifacts


def _batch_artifacts(
    run_dir: Path, unit_id: str, batch: ChapterBatch
) -> set[str]:
    artifacts: set[str] = set()
    units = read_json(run_dir / "planning/story-units.json")
    if any(
        isinstance(item, dict) and item.get("unit_id") == unit_id for item in units
    ):
        artifacts.add("story_unit")
    run = read_json(run_dir / "run.json")
    last_committed = run.get("last_committed_chapter", 0)
    if batch.start == 1 or (
        isinstance(last_committed, int) and last_committed >= batch.start - 1
    ):
        artifacts.add("state_context")
    outlines = read_json(run_dir / "planning/chapter-outlines.json")
    by_number = {
        item.get("number"): item for item in outlines if isinstance(item, dict)
    }
    expected = set(range(batch.start, batch.end + 1))
    if expected <= set(by_number):
        artifacts.add("chapter_outlines")
    if expected and all(
        isinstance(by_number.get(number), dict)
        and by_number[number].get("status") in {"committed", "locked"}
        for number in expected
    ):
        artifacts.update({"committed_batch", "batch_end_state"})
    if (run_dir / f"ledgers/batch-{batch.start:04d}-{batch.end:04d}.json").is_file():
        artifacts.add("ledger")
    return artifacts


def _unit_artifacts(
    run_dir: Path,
    unit_id: str,
    start: int,
    end: int,
    batches: tuple[ChapterBatch, ...],
) -> set[str]:
    artifacts: set[str] = set()
    units = read_json(run_dir / "planning/story-units.json")
    if any(
        isinstance(item, dict) and item.get("unit_id") == unit_id for item in units
    ):
        artifacts.add("story_unit")
    outlines = read_json(run_dir / "planning/chapter-outlines.json")
    by_number = {
        item.get("number"): item for item in outlines if isinstance(item, dict)
    }
    expected = set(range(start, end + 1))
    if expected and all(
        isinstance(by_number.get(number), dict)
        and by_number[number].get("status") in {"committed", "locked"}
        for number in expected
    ):
        artifacts.add("committed_unit")
    if all(
        (run_dir / f"ledgers/batch-{batch.start:04d}-{batch.end:04d}.json").is_file()
        for batch in batches
    ):
        artifacts.add("ledger")
    if (run_dir / f"reports/story-unit-review-{unit_id}.json").is_file():
        artifacts.add("unit_review")
    return artifacts
