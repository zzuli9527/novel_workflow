"""把已完成运行归档为可提交、可审计的测试矩阵产物。"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from .state_store import load_events
from .file_storage import current_snapshot_path, events_path, is_v2
from .storage import (
    StorageError,
    atomic_write_json,
    atomic_write_text,
    read_json,
    resolve_run_dir,
)


class RunArchiveError(RuntimeError):
    """运行尚未完成或归档产物包含无效/敏感数据。"""


def _json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def _secret_value(run: dict[str, Any]) -> str:
    provider = run.get("provider")
    if not isinstance(provider, dict):
        return ""
    name = provider.get("api_key_env")
    if not isinstance(name, str) or not name:
        return ""
    return os.environ.get(name, "")


def _safe_write_text(path: Path, text: str, secret: str) -> None:
    if secret and secret in text:
        raise RunArchiveError(f"归档内容包含 API Key，已阻止写入：{path.name}")
    atomic_write_text(path, text)


def _copy_text(source: Path, destination: Path, secret: str) -> None:
    try:
        text = source.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise RunArchiveError(f"无法读取归档来源 {source}：{exc}") from exc
    _safe_write_text(destination, text, secret)


def _unit(units: list[Any], unit_id: str) -> dict[str, Any]:
    matches = [
        item
        for item in units
        if isinstance(item, dict) and item.get("unit_id") == unit_id
    ]
    if len(matches) != 1:
        raise RunArchiveError(f"故事单元 {unit_id} 不存在或重复")
    return matches[0]


def _render_input(
    case_id: str,
    run: dict[str, Any],
    project: str,
    unit: dict[str, Any],
    initial_state: dict[str, Any],
    progression: dict[str, Any],
    comedy: dict[str, Any],
) -> str:
    return "\n\n".join(
        (
            f"# {case_id} 固定测试输入",
            (
                f"- 运行 ID：`{run.get('run_id')}`\n"
                "- 题材边界：修仙成长 + 情境/角色喜剧\n"
                "- 通用边界：测试数据只描述当前小说，执行器不绑定本书\n"
                f"- 章节范围：`{unit.get('chapter_range')}`\n"
                f"- 故事单元状态：`{unit.get('status')}`"
            ),
            "## 项目资料\n\n" + project.strip(),
            "## 故事单元\n\n```json\n" + _json(unit) + "\n```",
            "## 初始结构化状态\n\n```json\n"
            + _json(initial_state)
            + "\n```",
            "## 修炼体系\n\n```json\n" + _json(progression) + "\n```",
            "## 喜剧圣经\n\n```json\n" + _json(comedy) + "\n```",
        )
    ) + "\n"


def _render_outline(unit: dict[str, Any], outlines: list[dict[str, Any]]) -> str:
    sections = [
        "# 故事单元与章节细纲",
        "",
        "## 单元级目标",
        "",
        "```json",
        _json(unit),
        "```",
    ]
    for outline in outlines:
        scenes = outline.get("scenes", [])
        scene_budget = sum(
            scene.get("target_length", 0)
            for scene in scenes
            if isinstance(scene, dict)
            and isinstance(scene.get("target_length"), int)
        )
        sections.extend(
            (
                "",
                f"## 第 {outline.get('number')} 章：{outline.get('title', '')}",
                "",
                f"- 状态：`{outline.get('status')}`",
                f"- 实际正文字符：`{outline.get('actual_length', 0)}`",
                f"- 场景预算：`{scene_budget}`",
                "",
                "```json",
                _json(outline),
                "```",
            )
        )
    return "\n".join(sections) + "\n"


def _render_drafts(run_dir: Path, start: int, end: int) -> str:
    sections = ["# 全部 final 正文"]
    for chapter in range(start, end + 1):
        path = run_dir / f"chapters/{chapter:04d}/draft.final.md"
        try:
            draft = path.read_text(encoding="utf-8-sig").strip()
        except OSError as exc:
            raise RunArchiveError(f"缺少第 {chapter} 章 final 正文：{exc}") from exc
        sections.extend(("", draft, "", "---"))
    return "\n".join(sections).rstrip("-\n") + "\n"


def _render_states(
    events: list[dict[str, Any]], final_snapshot: dict[str, Any]
) -> str:
    sections = ["# 逐章正式状态事件"]
    for event in events:
        sections.extend(
            (
                "",
                f"## 第 {event.get('chapter')} 章",
                "",
                "```json",
                _json(event),
                "```",
            )
        )
    sections.extend(
        (
            "",
            "## 最终结构化快照",
            "",
            "```json",
            _json(final_snapshot),
            "```",
        )
    )
    return "\n".join(sections) + "\n"


def archive_run(
    root: Path,
    run_id: str,
    unit_id: str,
    case_id: str,
) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    try:
        run = read_json(run_dir / "run.json")
        units = read_json(run_dir / "planning/story-units.json")
        outlines = read_json(run_dir / "planning/chapter-outlines.json")
        initial_state = read_json(run_dir / "config/initial-state.json")
        progression = read_json(run_dir / "config/progression.json")
        comedy = read_json(run_dir / "config/comedy-bible.json")
        project = (run_dir / "config/project.md").read_text(encoding="utf-8-sig")
    except (OSError, StorageError) as exc:
        raise RunArchiveError(str(exc)) from exc
    if not isinstance(units, list) or not isinstance(outlines, list):
        raise RunArchiveError("故事单元或章纲文件不是数组")
    unit = _unit(units, unit_id)
    if unit.get("status") != "completed":
        raise RunArchiveError(f"故事单元尚未完成：{unit.get('status')}")
    chapter_range = unit.get("chapter_range")
    if (
        not isinstance(chapter_range, list)
        or len(chapter_range) != 2
        or not all(isinstance(value, int) for value in chapter_range)
    ):
        raise RunArchiveError("故事单元 chapter_range 无效")
    start, end = chapter_range
    selected = [
        item
        for item in outlines
        if isinstance(item, dict)
        and isinstance(item.get("number"), int)
        and start <= item["number"] <= end
    ]
    selected.sort(key=lambda item: item["number"])
    if [item["number"] for item in selected] != list(range(start, end + 1)):
        raise RunArchiveError("归档章节细纲不连续")
    if any(item.get("status") not in {"committed", "locked"} for item in selected):
        raise RunArchiveError("存在尚未提交的归档章节")

    events = [
        item
        for item in load_events(events_path(run_dir))
        if isinstance(item.get("chapter"), int) and start <= item["chapter"] <= end
    ]
    if [item.get("chapter") for item in events] != list(range(start, end + 1)):
        raise RunArchiveError("归档正式状态事件不连续")
    final_snapshot_path = (
        current_snapshot_path(run_dir)
        if is_v2(run)
        else run_dir / f"state/snapshots/chapter-{end:04d}.json"
    )
    final_snapshot = read_json(final_snapshot_path)
    review_json = run_dir / f"reports/story-unit-review-{unit_id}.json"
    review_md = run_dir / f"reports/story-unit-review-{unit_id}.md"
    review = read_json(review_json)
    verdict = review.get("verdict")
    metrics = review.get("metrics")
    hard_failure_count = (
        metrics.get("hard_failure_count") if isinstance(metrics, dict) else None
    )
    declared_hard_failure = (
        isinstance(hard_failure_count, int)
        and not isinstance(hard_failure_count, bool)
        and hard_failure_count > 0
    )
    conditional_pass = (
        verdict == "有条件通过"
        and review.get("archivable") is True
        and hard_failure_count == 0
    )
    if declared_hard_failure or (verdict != "通过" and not conditional_pass):
        raise RunArchiveError(f"故事单元评审未通过：{review.get('verdict')}")

    destination = root / "test/matrix-runs" / case_id
    data = destination / "data"
    secret = _secret_value(run)
    _safe_write_text(
        destination / "input.md",
        _render_input(
            case_id, run, project, unit, initial_state, progression, comedy
        ),
        secret,
    )
    _safe_write_text(
        destination / "outline.md", _render_outline(unit, selected), secret
    )
    _safe_write_text(
        destination / "drafts.md", _render_drafts(run_dir, start, end), secret
    )
    _safe_write_text(
        destination / "states.md", _render_states(events, final_snapshot), secret
    )
    _copy_text(review_md, destination / "review.md", secret)
    decision_path = destination / "decision.md"
    if not decision_path.exists():
        _safe_write_text(
            decision_path,
            "# 决策\n\n待根据本次真实运行评审结果填写。\n",
            secret,
        )

    for source, relative in (
        (run_dir / "run.json", "run.json"),
        (run_dir / "config/project.md", "config/project.md"),
        (run_dir / "config/initial-state.json", "config/initial-state.json"),
        (run_dir / "config/progression.json", "config/progression.json"),
        (run_dir / "config/comedy-bible.json", "config/comedy-bible.json"),
        (run_dir / "planning/story-units.json", "planning/story-units.json"),
        (
            run_dir / "planning/chapter-outlines.json",
            "planning/chapter-outlines.json",
        ),
        (events_path(run_dir), "state/events.jsonl"),
        (
            final_snapshot_path,
            "state/current.json"
            if is_v2(run)
            else f"state/snapshots/chapter-{end:04d}.json",
        ),
        (review_json, f"reports/{review_json.name}"),
        (run_dir / "logs/api-calls.jsonl", "logs/api-calls.jsonl"),
    ):
        _copy_text(source, data / relative, secret)
    for ledger in sorted((run_dir / "ledgers").glob("batch-*.json")):
        _copy_text(ledger, data / "ledgers" / ledger.name, secret)
    by_number = {item.get("number"): item for item in selected}
    checks = []
    for chapter in range(start, end + 1):
        path = run_dir / f"chapters/{chapter:04d}/checks.json"
        if path.exists():
            checks.append(read_json(path))
            continue
        outline = by_number[chapter]
        checks.append(
            {
                **(
                    outline.get("final_check")
                    if isinstance(outline.get("final_check"), dict)
                    else {}
                ),
                "chapter": chapter,
                "quality": outline.get("quality_summary", {}),
            }
        )
    atomic_write_json(data / "chapter-checks.json", checks)

    return {
        "case_id": case_id,
        "run_id": run_id,
        "unit_id": unit_id,
        "chapter_range": [start, end],
        "verdict": review["verdict"],
        "destination": destination.relative_to(root).as_posix(),
        "fixed_artifacts": [
            "input.md",
            "outline.md",
            "drafts.md",
            "states.md",
            "review.md",
            "decision.md",
        ],
    }
