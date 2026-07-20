"""从正式产物和调用日志生成确定性的故事单元评审报告。"""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
from statistics import fmean
from typing import Any

from .api_runtime import load_api_call_records, summarize_api_calls
from .state_store import load_events
from .storage import atomic_write_json, atomic_write_text, read_json, resolve_run_dir
from .wordcount import DraftParseError, LengthPolicy, check_drafts


class ReportingError(RuntimeError):
    """故事单元报告缺少必要输入。"""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _find_unit(units: list[dict[str, Any]], unit_id: str) -> dict[str, Any]:
    matches = [item for item in units if item.get("unit_id") == unit_id]
    if len(matches) != 1:
        raise ReportingError(f"故事单元 {unit_id} 不存在或重复")
    return matches[0]


def _range(unit: dict[str, Any]) -> tuple[int, int]:
    value = unit.get("chapter_range")
    if (
        not isinstance(value, list)
        or len(value) != 2
        or not all(
            isinstance(item, int) and not isinstance(item, bool) for item in value
        )
    ):
        raise ReportingError("故事单元 chapter_range 无效")
    start, end = value
    if start <= 0 or end < start:
        raise ReportingError("故事单元章节范围无效")
    return start, end


def _unit_api_records(
    records: list[dict[str, Any]], start: int, end: int
) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    for record in records:
        chapter = record.get("chapter")
        if isinstance(chapter, int) and start <= chapter <= end:
            selected.append(record)
            continue
        metadata = record.get("metadata")
        if not isinstance(metadata, dict):
            continue
        range_start = metadata.get("start_chapter")
        range_end = metadata.get("end_chapter")
        if (
            isinstance(range_start, int)
            and isinstance(range_end, int)
            and start <= range_start <= range_end <= end
        ):
            selected.append(record)
    return selected


def _comedy_rotation(outlines: list[dict[str, Any]]) -> dict[str, int]:
    adjacent_repeats = 0
    longest_streak = 0
    current_streak = 0
    previous: str | None = None
    for outline in outlines:
        mechanism = outline.get("comedy_mechanism")
        if not isinstance(mechanism, str) or not mechanism.strip():
            previous = None
            current_streak = 0
            continue
        if mechanism == previous:
            adjacent_repeats += 1
            current_streak += 1
        else:
            current_streak = 1
        longest_streak = max(longest_streak, current_streak)
        previous = mechanism
    return {
        "adjacent_repeat_count": adjacent_repeats,
        "longest_same_mechanism_streak": longest_streak,
    }


def _read_jsonl_objects(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except OSError as exc:
        raise ReportingError(f"无法读取运行事件日志：{exc}") from exc
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ReportingError(f"运行事件日志第 {line_number} 行损坏") from exc
        if isinstance(item, dict):
            records.append(item)
    return records


def _render_markdown(report: dict[str, Any]) -> str:
    metrics = report["metrics"]
    api = metrics["api"]
    ledger = metrics["ledger_compression"]
    lines = [
        f"# 故事单元评审：{report['unit_id']}",
        "",
        f"- 章节范围：第 {report['chapter_range'][0]}～{report['chapter_range'][1]} 章",
        f"- 单元状态：{report['unit_status']}",
        f"- 自动结论：{report['verdict']}",
        f"- 正式提交：{metrics['committed_chapters']} / {metrics['planned_chapters']} 章",
        f"- 目标字数合格率：{metrics['length_target_pass_rate']:.2%}",
        f"- 首稿长度合格率：{metrics['initial_draft_length_pass_rate']:.2%}",
        f"- 正文总字符：{metrics['total_body_characters']}",
        f"- 返工章节：{metrics['reworked_chapters']}",
        f"- 有任意重试的章节：{metrics['chapters_with_any_retry']}",
        f"- 平均重试次数：{metrics['average_retries_per_chapter']:.2f}",
        "",
        "## 连续性与质量",
        "",
        f"- 摘要化章节：{metrics['summary_like_chapters']}",
        f"- 修炼一致性失败：{metrics['cultivation_inconsistencies']}",
        f"- 严肃后果被取消：{metrics['serious_consequence_failures']}",
        f"- 资源连续性失败：{metrics['resource_continuity_failures']}",
        f"- 知识状态失败：{metrics['knowledge_state_failures']}",
        f"- 角色语言区分失败：{metrics['character_voice_failures']}",
        f"- 多线因果失败：{metrics['multi_line_causality_failures']}",
        f"- 当前状态失败章节：{metrics['current_state_failures']}",
        f"- 状态事件：{metrics['state_event_count']}",
        f"- 喜剧机制相邻重复：{metrics['comedy_rotation']['adjacent_repeat_count']}",
        f"- 同机制最长连续：{metrics['comedy_rotation']['longest_same_mechanism_streak']}",
        "",
        "## 账本压缩",
        "",
        f"- 账本数量：{ledger['ledger_count']}",
        f"- 下一批必读最大条目：{ledger['max_must_read_items']}",
        f"- 是否全部不超过限制：{'是' if ledger['within_limit'] else '否'}",
        "",
        "## 模型调用",
        "",
        f"- 调用次数：{api['calls']}（失败 {api['failed_calls']}）",
        f"- Token：{api['total_tokens']}",
        f"- 已记录费用：{api['total_cost']}",
        f"- 总耗时：{api['total_duration_seconds']} 秒",
        f"- 平均输入字符：{metrics['average_context_characters']:.2f}",
        f"- 人工修订次数：{metrics['manual_intervention_count']}",
        f"- 断点恢复次数：{metrics['breakpoint_recovery_count']}",
        "",
        "## 尚不能完全自动证明",
        "",
    ]
    for item in report["automated_gaps"]:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def generate_unit_review(root: Path, run_id: str, unit_id: str) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    units = read_json(run_dir / "planning/story-units.json")
    outlines = read_json(run_dir / "planning/chapter-outlines.json")
    if not isinstance(units, list) or not isinstance(outlines, list):
        raise ReportingError("故事单元或章纲文件不是数组")
    unit = _find_unit(units, unit_id)
    run_config = read_json(run_dir / "run.json")
    start, end = _range(unit)
    by_number = {
        item.get("number"): item
        for item in outlines
        if isinstance(item, dict) and isinstance(item.get("number"), int)
    }
    selected_outlines = [
        by_number[number] for number in range(start, end + 1) if number in by_number
    ]
    if len(selected_outlines) != end - start + 1:
        raise ReportingError("故事单元章纲不完整，无法生成评审")

    target_passes = 0
    total_characters = 0
    deviations: list[dict[str, Any]] = []
    quality_reviews: list[dict[str, Any]] = []
    current_state_failures = 0
    retry_totals: list[int] = []
    reworked_chapters = 0
    chapters_with_any_retry = 0
    initial_draft_results: list[dict[str, Any]] = []
    length_config = run_config["policies"]["length"]
    length_policy = LengthPolicy(
        target_min=length_config["target_min"],
        target_max=length_config["target_max"],
        expand_from=length_config["expand_from"],
        review_over=length_config["review_over"],
    )
    committed = 0
    for outline in selected_outlines:
        chapter = outline["number"]
        if outline.get("status") in {"committed", "locked"}:
            committed += 1
        if outline.get("status") == "state_failed":
            current_state_failures += 1
        retries = outline.get("retry_counts")
        retry_total = (
            sum(value for value in retries.values() if isinstance(value, int))
            if isinstance(retries, dict)
            else 0
        )
        retry_totals.append(retry_total)
        if retry_total:
            chapters_with_any_retry += 1
        if isinstance(retries, dict) and isinstance(retries.get("content"), int):
            if retries["content"] > 0:
                reworked_chapters += 1
        initial_path = run_dir / f"chapters/{chapter:04d}/draft.v1.md"
        if initial_path.exists():
            try:
                initial_report = check_drafts(
                    initial_path.read_text(encoding="utf-8-sig"), length_policy
                )
            except (OSError, DraftParseError):
                initial_draft_results.append(
                    {"chapter": chapter, "actual_length": None, "passed": False}
                )
            else:
                initial = initial_report.chapters[0]
                initial_draft_results.append(
                    {
                        "chapter": chapter,
                        "actual_length": initial.actual_length,
                        "status": initial.status,
                        "passed": initial.status == "passed",
                    }
                )
        checks_path = run_dir / f"chapters/{chapter:04d}/checks.json"
        if not checks_path.exists():
            continue
        checks = read_json(checks_path)
        actual = checks.get("actual_length")
        target = outline.get("target_length")
        if isinstance(actual, int):
            total_characters += actual
            if (
                isinstance(target, dict)
                and isinstance(target.get("min"), int)
                and isinstance(target.get("max"), int)
                and target["min"] <= actual <= target["max"]
            ):
                target_passes += 1
            scenes = outline.get("scenes")
            if isinstance(scenes, list):
                budget = sum(
                    scene.get("target_length", 0)
                    for scene in scenes
                    if isinstance(scene, dict)
                    and isinstance(scene.get("target_length"), int)
                )
                if budget > 0:
                    deviations.append(
                        {
                            "chapter": chapter,
                            "actual": actual,
                            "scene_budget": budget,
                            "difference": actual - budget,
                            "absolute_ratio": round(abs(actual - budget) / budget, 6),
                        }
                    )
        quality = checks.get("quality")
        if isinstance(quality, dict):
            quality_reviews.append(quality)

    events = [
        event
        for event in load_events(run_dir / "state/events.jsonl")
        if isinstance(event.get("chapter"), int) and start <= event["chapter"] <= end
    ]
    ledger_files = sorted(run_dir.glob("ledgers/batch-*.json"))
    ledger_sizes: list[int] = []
    ledger_limit = run_config["policies"]["batch"][
        "ledger_item_limit"
    ]
    for path in ledger_files:
        ledger = read_json(path)
        chapter_range = ledger.get("chapter_range")
        if (
            isinstance(chapter_range, list)
            and len(chapter_range) == 2
            and start <= chapter_range[0] <= chapter_range[1] <= end
        ):
            items = ledger.get("must_read_next")
            ledger_sizes.append(len(items) if isinstance(items, list) else ledger_limit + 1)

    records = load_api_call_records(run_dir / "logs/api-calls.jsonl")
    api_records = _unit_api_records(records, start, end)
    api_summary = summarize_api_calls(api_records)
    input_sizes: list[int] = []
    for record in api_records:
        usage = record.get("usage")
        if isinstance(usage, dict) and isinstance(usage.get("input_characters"), int):
            input_sizes.append(usage["input_characters"])
            continue
        prompt_relative = record.get("prompt_path")
        if not isinstance(prompt_relative, str):
            continue
        prompt_path = (run_dir / prompt_relative).resolve()
        if run_dir.resolve() not in prompt_path.parents or not prompt_path.is_file():
            continue
        try:
            input_sizes.append(len(prompt_path.read_text(encoding="utf-8-sig")))
        except OSError:
            continue
    manual_interventions = 0
    revisions_dir = run_dir / "revisions"
    for path in (
        revisions_dir.glob("revision-*/manifest.json")
        if revisions_dir.exists()
        else []
    ):
        manifest = read_json(path)
        invalidated_from = manifest.get("invalidated_from_chapter")
        if isinstance(invalidated_from, int) and start <= invalidated_from <= end:
            manual_interventions += 1
    recovery_count = 0
    for runtime_event in _read_jsonl_objects(run_dir / "logs/events.jsonl"):
        if runtime_event.get("action") not in {
            "revision_recovered",
            "incomplete_tasks_recovered",
            "commit_recovered",
        }:
            continue
        chapter_value = runtime_event.get("chapter")
        chapters_value = runtime_event.get("chapters")
        if isinstance(chapter_value, int) and start <= chapter_value <= end:
            recovery_count += 1
        elif isinstance(chapters_value, list) and any(
            isinstance(item, int) and start <= item <= end
            for item in chapters_value
        ):
            recovery_count += 1
    planned = end - start + 1
    quality_failures = {
        "summary_like_chapters": sum(
            review.get("summary_like") is True for review in quality_reviews
        ),
        "cultivation_inconsistencies": sum(
            review.get("cultivation_consistent") is False for review in quality_reviews
        ),
        "serious_consequence_failures": sum(
            review.get("serious_consequences_preserved") is False
            for review in quality_reviews
        ),
        "resource_continuity_failures": sum(
            review.get("resource_continuity_consistent") is False
            for review in quality_reviews
        ),
        "knowledge_state_failures": sum(
            review.get("knowledge_states_consistent") is False
            for review in quality_reviews
        ),
        "character_voice_failures": sum(
            review.get("character_voices_distinct") is False
            for review in quality_reviews
        ),
        "multi_line_causality_failures": sum(
            review.get("multi_line_causality_preserved") is False
            for review in quality_reviews
        ),
    }
    critical_failure_count = (
        planned - committed
        + sum(quality_failures.values())
        + current_state_failures
        + sum(size > ledger_limit for size in ledger_sizes)
    )
    verdict = "通过" if critical_failure_count == 0 and target_passes == planned else "有条件通过"
    if unit.get("status") == "paused" or critical_failure_count > 0:
        verdict = "失败"

    metrics = {
        "planned_chapters": planned,
        "committed_chapters": committed,
        "length_target_pass_count": target_passes,
        "length_target_pass_rate": target_passes / planned,
        "initial_draft_length_pass_count": sum(
            item["passed"] is True for item in initial_draft_results
        ),
        "initial_draft_length_pass_rate": (
            sum(item["passed"] is True for item in initial_draft_results)
            / planned
        ),
        "initial_drafts": initial_draft_results,
        "total_body_characters": total_characters,
        "scene_budget": {
            "evaluated_chapters": len(deviations),
            "mean_absolute_deviation_characters": round(
                fmean(abs(item["difference"]) for item in deviations), 2
            )
            if deviations
            else 0.0,
            "mean_absolute_deviation_ratio": round(
                fmean(item["absolute_ratio"] for item in deviations), 6
            )
            if deviations
            else 0.0,
            "chapters": deviations,
        },
        **quality_failures,
        "current_state_failures": current_state_failures,
        "state_event_count": len(events),
        "reworked_chapters": reworked_chapters,
        "chapters_with_any_retry": chapters_with_any_retry,
        "average_retries_per_chapter": round(fmean(retry_totals), 4),
        "comedy_rotation": _comedy_rotation(selected_outlines),
        "ledger_compression": {
            "ledger_count": len(ledger_sizes),
            "must_read_item_counts": ledger_sizes,
            "max_must_read_items": max(ledger_sizes, default=0),
            "within_limit": all(size <= ledger_limit for size in ledger_sizes),
            "item_limit": ledger_limit,
        },
        "api": api_summary,
        "average_context_characters": round(fmean(input_sizes), 2)
        if input_sizes
        else 0.0,
        "manual_intervention_count": manual_interventions,
        "breakpoint_recovery_count": recovery_count,
    }
    report = {
        "schema_version": "1.0",
        "run_id": run_id,
        "unit_id": unit_id,
        "chapter_range": [start, end],
        "unit_status": unit.get("status"),
        "verdict": verdict,
        "metrics": metrics,
        "automated_gaps": [
            "结构化字段可以核对余额、境界和知识状态，但正文是否正确提取这些事实仍需独立评审。",
            "角色语言区分与笑点实际效果仍需要人工或独立模型评审。",
            "API 用量只证明调用规模；未配置模型单价时，total_cost 不能作为真实费用结论。",
        ],
        "generated_at": _utc_now(),
    }
    report_dir = run_dir / "reports"
    json_path = report_dir / f"story-unit-review-{unit_id}.json"
    md_path = report_dir / f"story-unit-review-{unit_id}.md"
    atomic_write_json(json_path, report)
    atomic_write_text(md_path, _render_markdown(report))
    atomic_write_json(report_dir / "story-unit-review.json", report)
    atomic_write_text(report_dir / "story-unit-review.md", _render_markdown(report))
    return report
