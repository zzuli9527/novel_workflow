"""Read and format the runtime context selected for model prompts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..file_storage import is_v2, ledger_current_path, read_current_snapshot
from ..project_profile import load_project_profile
from ..storage import StorageError, read_json
from ..workflow_runtime import load_task_context_sources


def _read_optional_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return read_json(path)


def _read_optional_text(path: Path, default: str = "") -> str:
    if not path.exists():
        return default
    try:
        return path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise StorageError(f"无法读取文件：{path}：{exc}") from exc


def _latest_json(directory: Path, pattern: str) -> Any:
    candidates = sorted(directory.glob(pattern)) if directory.exists() else []
    return read_json(candidates[-1]) if candidates else None


def _previous_snapshot(run_dir: Path, chapter: int) -> Any:
    if chapter <= 0:
        return None
    run_config = read_json(run_dir / "run.json")
    if is_v2(run_config):
        return read_current_snapshot(run_dir, run_config, chapter)
    return _read_optional_json(
        run_dir / f"state/snapshots/chapter-{chapter:04d}.json", None
    )


def _planning_snapshot(run_dir: Path, chapter: int) -> Any:
    """Return the newest committed state available to a future-outline prompt.

    A planning request can itself be split (for example chapters 5--6 followed
    by chapter 7) before either planned chapter has a state snapshot. V2 keeps
    only the current committed snapshot, so asking it for ``chapter - 1`` in
    that situation is both impossible and incorrect. Use the run pointer as
    the upper bound while draft/state prompts retain their exact-state rule.
    """

    if chapter <= 0:
        return None
    run_config = read_json(run_dir / "run.json")
    last_committed = run_config.get("last_committed_chapter", 0)
    if not isinstance(last_committed, int) or isinstance(last_committed, bool):
        last_committed = 0
    return _previous_snapshot(run_dir, min(chapter, max(0, last_committed)))


def _latest_ledger(run_dir: Path) -> Any:
    run_config = read_json(run_dir / "run.json")
    if is_v2(run_config):
        path = ledger_current_path(run_dir)
        return _read_optional_json(path, None)
    ledger_dir = run_dir / "ledgers"
    # A batch keeps raw provider output and the workflow-source manifest next
    # to its accepted ledger.  Neither is context for the next chapter.  The
    # broad historical glob used to select the lexically last sidecar file,
    # so a workflow manifest could silently replace the actual ledger in a prompt.
    candidates = [
        path
        for path in ledger_dir.glob("batch-*.json")
        if ".raw." not in path.name and ".workflow." not in path.name
    ] if ledger_dir.exists() else []
    return read_json(sorted(candidates)[-1]) if candidates else None


def _latest_state_raw(chapter_dir: Path) -> str:
    candidates: list[tuple[int, Path]] = []
    for path in chapter_dir.glob("state.raw.v*.json"):
        version = path.name.removeprefix("state.raw.v").removesuffix(".json")
        if version.isdigit():
            candidates.append((int(version), path))
    if not candidates:
        return ""
    return _read_optional_text(max(candidates, key=lambda item: item[0])[1])


def _latest_review_raw(chapter_dir: Path) -> str:
    candidates: list[tuple[int, Path]] = []
    for path in chapter_dir.glob("review.raw.v*.json"):
        version = path.name.removeprefix("review.raw.v").removesuffix(".json")
        if version.isdigit():
            candidates.append((int(version), path))
    if not candidates:
        return ""
    return _read_optional_text(max(candidates, key=lambda item: item[0])[1])


def _json_block(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def _workflow_context_sections(
    root: Path, run_dir: Path, task_id: str
) -> list[tuple[str, str]]:
    """Load static run context exactly as declared by the task registry."""

    profile = load_project_profile(run_dir)
    sections: list[tuple[str, str]] = []
    for source in load_task_context_sources(
        root, task_id, rule_context=profile
    ):
        path = (run_dir / source.path).resolve()
        if run_dir.resolve() not in path.parents:
            raise StorageError(f"工作流上下文路径越出运行目录：{source.path}")
        content = (
            _json_block(read_json(path))
            if source.format == "json"
            else _read_optional_text(path)
        )
        sections.append((source.section, content))
    return sections
