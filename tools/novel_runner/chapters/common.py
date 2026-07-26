"""Shared chapter-service context, paths, and small invariants."""

from __future__ import annotations

from pathlib import Path
import re
from typing import Any

from ..config import validate_run_directory
from ..file_storage import record_runtime_event
from ..storage import atomic_write_json, read_json, resolve_run_dir
from ..shared import utc_now
from ..wordcount import LengthPolicy


class ChapterServiceError(RuntimeError):
    """章节垂直闭环执行失败。"""


def _log_runtime_event(run_dir: Path, action: str, **data: Any) -> None:
    run_config = read_json(run_dir / "run.json")
    record_runtime_event(
        run_dir,
        run_config,
        {"timestamp": utc_now(), "action": action, **data},
    )


def _relative_posix(path: Path, run_dir: Path) -> str:
    return path.relative_to(run_dir).as_posix()


def _load_context(root: Path, run_id: str) -> tuple[Path, dict[str, Any], list[dict[str, Any]]]:
    report = validate_run_directory(root, run_id)
    if not report.valid:
        details = "; ".join(f"{issue.path}: {issue.message}" for issue in report.issues)
        raise ChapterServiceError(f"运行配置无效：{details}")
    run_dir = resolve_run_dir(root, run_id)
    run_config = read_json(run_dir / "run.json")
    outlines = read_json(run_dir / "planning/chapter-outlines.json")
    return run_dir, run_config, outlines


def _find_outline(
    outlines: list[dict[str, Any]], chapter_number: int
) -> tuple[int, dict[str, Any]]:
    matches = [
        (index, outline)
        for index, outline in enumerate(outlines)
        if outline.get("number") == chapter_number
    ]
    if not matches:
        raise ChapterServiceError(f"未找到第 {chapter_number} 章细纲")
    if len(matches) > 1:
        raise ChapterServiceError(f"第 {chapter_number} 章细纲重复")
    return matches[0]


def _save_outlines(run_dir: Path, outlines: list[dict[str, Any]]) -> None:
    atomic_write_json(run_dir / "planning/chapter-outlines.json", outlines)


def _length_policy(run_config: dict[str, Any]) -> LengthPolicy:
    data = run_config["policies"]["length"]
    return LengthPolicy(
        target_min=data["target_min"],
        target_max=data["target_max"],
        expand_from=data["expand_from"],
        review_over=data["review_over"],
    )


def _next_draft_version(chapter_dir: Path) -> int:
    versions: list[int] = []
    for path in chapter_dir.glob("draft.v*.md"):
        middle = path.stem.removeprefix("draft.v")
        if middle.isdigit():
            versions.append(int(middle))
    return max(versions, default=0) + 1


def _next_state_version(chapter_dir: Path) -> int:
    versions: list[int] = []
    for path in chapter_dir.glob("state.raw.v*.json"):
        middle = path.name.removeprefix("state.raw.v").removesuffix(".json")
        if middle.isdigit():
            versions.append(int(middle))
    return max(versions, default=0) + 1


def _next_review_version(chapter_dir: Path) -> int:
    versions: list[int] = []
    for path in chapter_dir.glob("review.raw.v*.json"):
        middle = path.name.removeprefix("review.raw.v").removesuffix(".json")
        if middle.isdigit():
            versions.append(int(middle))
    return max(versions, default=0) + 1


def _pause_run(run_dir: Path, run_config: dict[str, Any], reason: str) -> None:
    atomic_write_json(
        run_dir / "run.json",
        {
            **run_config,
            "status": "paused",
            "pause_reason": reason,
            "updated_at": utc_now(),
        },
    )


def _read_current_draft(run_dir: Path, outline: dict[str, Any]) -> str:
    relative = outline.get("draft_path")
    if not isinstance(relative, str) or not relative:
        return ""
    path = (run_dir / Path(relative)).resolve()
    if run_dir.resolve() not in path.parents:
        raise ChapterServiceError("草稿路径越出运行目录")
    try:
        return path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise ChapterServiceError(f"无法读取失败草稿：{exc}") from exc


def _normalize_evidence(value: str) -> str:
    return re.sub(r"\s+", "", value)
