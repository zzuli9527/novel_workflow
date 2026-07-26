"""Prompts for story-unit and chapter-batch planning."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..project_profile import load_project_profile
from ..storage import read_json
from ..workflow_runtime import load_task_instructions, render_contract_template
from .context import (
    _json_block,
    _latest_ledger,
    _planning_snapshot,
    _previous_snapshot,
    _workflow_context_sections,
)
from .projections import _compact_snapshot, _compact_story_unit


def compose_story_unit_plan_prompt(
    root: Path,
    run_dir: Path,
    unit_id: str,
    start_chapter: int,
    end_chapter: int,
    master_context: dict[str, Any],
) -> str:
    profile = load_project_profile(run_dir)
    runtime_prompt = load_task_instructions(
        root, "plan_story_unit", rule_context=profile
    )
    contract = render_contract_template(
        root,
        "plan_story_unit",
        {
            "unit_id": unit_id,
            "chapter_range": [start_chapter, end_chapter],
        },
    )
    sections: list[tuple[str, str]] = [("任务规则", runtime_prompt)]
    sections.extend(_workflow_context_sections(root, run_dir, "plan_story_unit"))
    sections.extend((
        ("已批准全书总纲切片", _json_block(master_context)),
        (
            "当前结构化状态",
            _json_block(
                _compact_snapshot(
                    _previous_snapshot(
                        run_dir,
                        int(read_json(run_dir / "run.json").get("last_committed_chapter", 0)),
                    )
                )
                or read_json(run_dir / "config/initial-state.json")
            ),
        ),
        ("最近批次账本", _json_block(_latest_ledger(run_dir))),
        ("固定章节范围", f"unit_id={unit_id}，第 {start_chapter}～{end_chapter} 章"),
        (
            "机器输出契约",
            _json_block(contract),
        ),
    ))
    return "\n\n".join(f"# {title}\n\n{content}" for title, content in sections)


def compose_batch_outline_plan_prompt(
    root: Path,
    run_dir: Path,
    unit: dict[str, Any],
    start_chapter: int,
    end_chapter: int,
    existing_outlines: list[dict[str, Any]],
) -> str:
    profile = load_project_profile(run_dir)
    runtime_prompt = load_task_instructions(
        root, "plan_chapter_batch", rule_context=profile
    )
    length_policy = read_json(run_dir / "run.json").get("policies", {}).get("length", {})
    target_min = int(length_policy.get("target_min", 2000))
    target_max = int(length_policy.get("target_max", 3000))
    previous_snapshot = _planning_snapshot(run_dir, start_chapter - 1)
    example_chapter_id = f"chapter-{start_chapter:04d}"
    outline_example = render_contract_template(
        root,
        "plan_chapter_batch",
        {
            "chapter_id": example_chapter_id,
            "chapter_number": start_chapter,
            "story_unit_id": unit.get("unit_id"),
            "target_min": target_min,
            "target_max": target_max,
        },
        template_key="item_template",
    )
    contract = render_contract_template(
        root,
        "plan_chapter_batch",
        {"chapter_outlines": [outline_example]},
    )
    prior_full = sorted(
        (item for item in existing_outlines if item.get("number", 0) < start_chapter),
        key=lambda item: item["number"],
    )[-2:]
    prior = [
        {
            "number": item.get("number"),
            "title": item.get("title"),
            "comedy_mechanism": item.get("comedy_mechanism"),
            "closing_state": item.get("closing_state", []),
            "next_chapter_input": item.get("next_chapter_input", []),
        }
        for item in prior_full
    ]
    sections: list[tuple[str, str]] = [("任务规则", runtime_prompt)]
    sections.extend(_workflow_context_sections(root, run_dir, "plan_chapter_batch"))
    sections.extend((
        ("当前故事单元", _json_block(_compact_story_unit(unit))),
        ("上一批结束快照", _json_block(_compact_snapshot(previous_snapshot))),
        ("最近批次账本", _json_block(_latest_ledger(run_dir))),
        ("前两章喜剧机制参考", _json_block(prior)),
        ("固定批次范围", f"第 {start_chapter}～{end_chapter} 章，共 {end_chapter - start_chapter + 1} 章"),
        (
            "单元契约映射",
            "完整单元中必须至少有一章把 required_setback 原句放入 required_outcomes；"
            "末章必须把 required_payoff 原句作为 required_outcomes 数组中的一个独立元素逐字符复制，"
            "禁止在前后添加 required_payoff、冒号、说明或任何改写；"
            "末章 closing_state 也必须把故事单元 closing_state 的每一项逐字符作为独立元素复制，"
            "可以额外补充状态，但不得用释义替换原句。",
        ),
        (
            "机器输出契约",
            _json_block(contract),
        ),
    ))
    return "\n\n".join(f"# {title}\n\n{content}" for title, content in sections)
