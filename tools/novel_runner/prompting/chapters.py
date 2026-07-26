"""Prompts for chapter drafting, repair, and state extraction."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..project_profile import load_project_profile
from ..storage import StorageError, read_json
from ..workflow_runtime import load_task_instructions, render_contract_template
from .context import (
    _json_block,
    _latest_ledger,
    _latest_state_raw,
    _previous_snapshot,
    _read_optional_json,
    _workflow_context_sections,
)
from .projections import (
    _active_state_ids,
    _compact_state_checks,
    _compact_state_chapter_contract,
    _compact_snapshot,
    _compact_story_unit,
    _preferred_length_range,
    _state_retry_output_projection,
    _verbatim_paragraph_catalog,
)


def compose_draft_prompt(
    root: Path,
    run_dir: Path,
    run_config: dict[str, Any],
    outline: dict[str, Any],
    *,
    task_id: str = "draft_chapter",
) -> str:
    profile = load_project_profile(run_dir)
    workflow = load_task_instructions(root, task_id, rule_context=profile)
    chapter = int(outline["number"])
    previous_snapshot = _previous_snapshot(run_dir, chapter - 1)
    story_units = _read_optional_json(run_dir / "planning/story-units.json", [])
    current_unit_id = outline.get("story_unit_id") or run_config.get("current_story_unit")
    current_unit = next(
        (item for item in story_units if item.get("unit_id") == current_unit_id), None
    )
    length = run_config.get("policies", {}).get("length", {})
    target_min = int(length.get("target_min", 2000))
    target_max = int(length.get("target_max", 3000))
    preferred_min, preferred_max = _preferred_length_range(length)
    scene_budget = sum(
        scene.get("target_length", 0)
        for scene in outline.get("scenes", [])
        if isinstance(scene, dict)
        and isinstance(scene.get("target_length"), int)
    )

    sections: list[tuple[str, str]] = [
        ("通用正文工作流", workflow),
        (
            "本章机械长度契约",
            _json_block(
                {
                    "counting_unit": length.get(
                        "unit", "non_whitespace_character"
                    ),
                    "hard_range": [target_min, target_max],
                    "preferred_range": [preferred_min, preferred_max],
                    "scene_budget_total": scene_budget,
                    "instruction": (
                        "优先落在 preferred_range；绝对不得超过 hard_range 上限。"
                        "按场景预算分配篇幅，完成章末钩子后立即结束，不添加总结、"
                        "重复反应或额外收尾。"
                    ),
                }
            ),
        ),
    ]
    sections.extend(_workflow_context_sections(root, run_dir, task_id))
    if previous_snapshot is None:
        sections.append(
            (
                "初始结构化状态",
                _json_block(read_json(run_dir / "config/initial-state.json")),
            )
        )
    sections.extend(
        [
        ("当前故事单元", _json_block(_compact_story_unit(current_unit))),
        ("当前章细纲", _json_block(outline)),
        ("上一章状态快照", _json_block(_compact_snapshot(previous_snapshot))),
        ("最近批次账本", _json_block(_latest_ledger(run_dir))),
        ("运行策略", _json_block(run_config.get("policies", {}))),
        ]
    )
    return "\n\n".join(f"# {title}\n\n{content}" for title, content in sections)


def compose_state_prompt(
    root: Path,
    run_dir: Path,
    outline: dict[str, Any],
    draft_text: str,
    checks: dict[str, Any],
) -> str:
    workflow = load_task_instructions(
        root, "extract_state", rule_context=load_project_profile(run_dir)
    )
    chapter = int(outline["number"])
    previous_snapshot = _previous_snapshot(run_dir, chapter - 1)
    output_contract = render_contract_template(root, "extract_state", {})
    sections: list[tuple[str, str]] = [
        ("状态回填工作流", workflow),
        ("当前章契约", _json_block(_compact_state_chapter_contract(outline))),
        ("本章 final 正文", draft_text),
        ("本章检查结果", _json_block(_compact_state_checks(checks))),
        ("上一章状态快照", _json_block(_compact_snapshot(previous_snapshot))),
    ]
    sections.extend(_workflow_context_sections(root, run_dir, "extract_state"))
    state_reference = previous_snapshot
    if state_reference is None:
        state_reference = read_json(run_dir / "config/initial-state.json")
    sections.append(
        (
            "允许引用的活动状态 ID",
            _json_block(_active_state_ids(state_reference)),
        )
    )
    failure_reason = outline.get("state_failure_reason")
    retry_counts = outline.get("retry_counts")
    has_failure_reason = isinstance(failure_reason, str) and bool(
        failure_reason.strip()
    )
    has_retry_count = isinstance(retry_counts, dict) and any(
        isinstance(value, int) and value > 0 for value in retry_counts.values()
    )
    is_retry = has_failure_reason or has_retry_count
    if is_retry:
        previous_invalid_output = _latest_state_raw(
            run_dir / f"chapters/{chapter:04d}"
        )
        previous_output_projection = _state_retry_output_projection(
            previous_invalid_output
        )
        failure_kind = outline.get("state_failure_kind")
        if previous_output_projection is not None or failure_kind in {
            "format",
            "content",
        }:
            repair_context = {
                "state_failure_reason": failure_reason or "上一版未通过校验",
                "repair_instruction": (
                    "只修复失败原因所指向的字段；不得复制上一版中的错误资源 ID、"
                    "错误余额或无正文证据的变化。supersedes_fact_ids 只能引用"
                    "‘允许引用的活动状态 ID’区段中的活动知识 fact_id；没有合法"
                    "淘汰项时必须输出空数组，禁止根据正文措辞臆造 ID。上一版输出"
                    "中的 recovery 必须引用该区段列出的活动 injury ID，并符合"
                    "allowed_changes；已解除或未列出的伤势 ID 不得再次恢复。"
                    "已移除全部 source_evidence；请从逐字正文段落目录中重新复制"
                    "一个或多个连续段落的原文，不得删字、补字或改写。重新核对"
                    "上一状态后输出完整契约。"
                ),
                "verbatim_paragraph_catalog": _verbatim_paragraph_catalog(
                    draft_text
                ),
            }
            if previous_output_projection is not None:
                repair_context["previous_output_without_source_evidence"] = (
                    previous_output_projection
                )
            sections.append(
                (
                    "上次状态提取失败修复信息",
                    _json_block(repair_context),
                )
            )
    if previous_snapshot is None:
        sections.append(
            (
                "初始结构化状态",
                _json_block(read_json(run_dir / "config/initial-state.json")),
            )
        )
    sections.append(
        (
            "机器输出契约",
            _json_block(output_contract),
        )
    )
    return "\n\n".join(f"# {title}\n\n{content}" for title, content in sections)


def compose_repair_prompt(
    root: Path,
    run_dir: Path,
    run_config: dict[str, Any],
    outline: dict[str, Any],
    current_draft: str,
    checks: dict[str, Any],
    mode: str,
) -> str:
    base_prompt = compose_draft_prompt(
        root, run_dir, run_config, outline, task_id="repair_chapter"
    )
    length = run_config["policies"]["length"]
    actual = checks.get("actual_length", 0)
    gap = max(0, length["target_min"] - actual) if isinstance(actual, int) else 0
    directives = {
        "targeted_expansion": (
            "只扩写低于预算的现有场景，补充动作、回应、修炼过程、关系反应或后果落地；"
            "不得推进下一章、改变章末状态、新增能力或重复笑点。"
        ),
        "targeted_compression": (
            "只压缩造成超长的局部段落，优先删除重复描写、同义解释、无新增信息的对话和"
            "过长反应；不得截断有效场景、必做结果、因果链或章末钩子。"
        ),
        "rewrite_short": (
            "当前正文严重不足。严格依据原章纲重写完整章节，不保留摘要式结构；"
            "不得通过解释设定或段子堆砌凑长度。"
        ),
        "rewrite_contract": (
            "只修改 latest_checks 中 contract_failures 指向的段落，补齐缺失的必做结果或"
            "移除禁止结果；输出完整当前章节，但不要重写无关段落。"
        ),
        "rewrite_quality": (
            "只修改 latest_checks.quality.quality_failures 指向的段落，保留全部必做结果、"
            "因果和章末状态。仅当 summary_like 明确指向全章摘要化时，才允许重构必要场景；"
            "不得把局部问题扩大为整章重写。"
        ),
        "provider_retry": "沿用原章纲重新生成当前章节，不改变任何计划内容。",
    }
    if mode not in directives:
        raise StorageError(f"未知修复模式：{mode}")
    preferred_min, preferred_max = _preferred_length_range(length)
    repair_section = {
        "mode": mode,
        "actual_length": actual,
        "target_min": length["target_min"],
        "target_max": length["target_max"],
        "missing_length": gap,
        "excess_length": (
            max(0, actual - length["target_max"])
            if isinstance(actual, int)
            else 0
        ),
        "preferred_rewrite_range": [preferred_min, preferred_max],
        "hard_output_range": [length["target_min"], length["target_max"]],
        "instruction": directives[mode],
        "repair_boundaries": [
            "只处理失败字段对应的段落，保持其他段落原文不变",
            "不改人物名、既有事实、章节结构、场景顺序和章末状态",
            "不新增无关人物、能力、资源、支线或下一章事件",
            "扩写或压缩只针对局部缺口，不以同义改写波及全文",
            "状态提取错误不属于正文修复；只重试状态提取 JSON",
        ],
        "latest_checks": checks,
    }
    return (
        base_prompt
        + "\n\n# 本次修复指令\n\n"
        + _json_block(repair_section)
        + "\n\n# 当前失败草稿\n\n"
        + (current_draft or "无可用草稿，请重新生成。")
    )
