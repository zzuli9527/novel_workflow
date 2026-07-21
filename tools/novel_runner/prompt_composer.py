"""把工作流模板与当前运行数据拼装为单职责 Prompt。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .storage import StorageError, read_json


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


def _runtime_prompt(root: Path, name: str) -> str:
    path = root / "workflow/runtime" / name
    if path.is_file():
        return path.read_text(encoding="utf-8-sig")
    legacy = {
        "plan-story-unit.md": "01-expand.md",
        "plan-chapter-batch.md": "03-chapters.md",
        "draft-chapter.md": "04-draft.md",
        "review-chapter.md": "04-draft.md",
        "extract-state.md": "05-update-state.md",
        "build-ledger.md": "05-update-state.md",
    }.get(name)
    legacy_path = root / "workflow" / legacy if legacy else None
    if legacy_path is not None and legacy_path.is_file():
        return legacy_path.read_text(encoding="utf-8-sig")
    raise StorageError(f"缺少运行时 Prompt：{path}")


def _compact_snapshot(snapshot: Any) -> Any:
    if not isinstance(snapshot, dict):
        return snapshot
    structured = snapshot.get("structured_state")
    if isinstance(structured, dict):
        structured = {
            "cultivation": structured.get("cultivation", []),
            "resources": structured.get("resources", []),
            "knowledge": [
                item
                for item in structured.get("knowledge", [])
                if isinstance(item, dict) and item.get("state") != "knows"
            ],
        }
    return {
        "after_chapter": snapshot.get("after_chapter"),
        "structured_state": structured,
        "next_chapter_inputs": snapshot.get("next_chapter_inputs", []),
        "deviations": snapshot.get("deviations", []),
        "last_source_draft": snapshot.get("last_source_draft"),
        "last_source_sha256": snapshot.get("last_source_sha256"),
    }


def _active_state_ids(snapshot_or_initial: Any) -> dict[str, Any]:
    """Return the stable IDs a state-repair response may legally reference."""

    if not isinstance(snapshot_or_initial, dict):
        return {
            "tracked_state_ids_by_subject": {},
            "resource_ids_by_owner": {},
            "knowledge_fact_ids_by_character": {},
        }
    structured = snapshot_or_initial.get("structured_state")
    if not isinstance(structured, dict):
        structured = snapshot_or_initial

    tracked_by_subject: dict[str, list[str]] = {}
    for item in structured.get("cultivation", []):
        if not isinstance(item, dict) or not isinstance(item.get("subject_id"), str):
            continue
        state_ids = sorted(
            {
                state["state_id"]
                for state in item.get("tracked_states", [])
                if isinstance(state, dict)
                and isinstance(state.get("state_id"), str)
                and state["state_id"].strip()
            }
        )
        if state_ids:
            tracked_by_subject[item["subject_id"]] = state_ids

    resources_by_owner: dict[str, list[str]] = {}
    for item in structured.get("resources", []):
        if not isinstance(item, dict):
            continue
        owner_id = item.get("owner_id")
        resource_id = item.get("resource_id")
        if not isinstance(owner_id, str) or not isinstance(resource_id, str):
            continue
        resources_by_owner.setdefault(owner_id, []).append(resource_id)
    resources_by_owner = {
        owner_id: sorted(set(resource_ids))
        for owner_id, resource_ids in resources_by_owner.items()
    }

    knowledge_by_character: dict[str, list[str]] = {}
    for item in structured.get("knowledge", []):
        if not isinstance(item, dict):
            continue
        character_id = item.get("character_id")
        fact_id = item.get("fact_id")
        if not isinstance(character_id, str) or not isinstance(fact_id, str):
            continue
        knowledge_by_character.setdefault(character_id, []).append(fact_id)
    knowledge_by_character = {
        character_id: sorted(set(fact_ids))
        for character_id, fact_ids in knowledge_by_character.items()
    }

    return {
        "tracked_state_ids_by_subject": tracked_by_subject,
        "resource_ids_by_owner": resources_by_owner,
        "knowledge_fact_ids_by_character": knowledge_by_character,
    }


def _compact_story_unit(unit: Any) -> Any:
    if not isinstance(unit, dict):
        return unit
    fields = (
        "unit_id",
        "chapter_range",
        "goal",
        "main_obstacle",
        "closing_state",
        "required_setback",
        "required_payoff",
        "must_not_resolve",
    )
    return {field: unit.get(field) for field in fields}


def _compact_chapter_contract(outline: Any) -> Any:
    """Project a chapter outline down to the fields used by review/state tasks."""

    if not isinstance(outline, dict):
        return outline
    fields = (
        "chapter_id",
        "number",
        "title",
        "story_unit_id",
        "intent",
        "opening_state",
        "required_outcomes",
        "forbidden_outcomes",
        "progression_payoff",
        "comedy_mechanism",
        "comedy_payoff",
        "cost_or_aftereffect",
        "closing_state",
        "next_chapter_input",
    )
    return {field: outline.get(field) for field in fields}


def _preferred_length_range(length: dict[str, Any]) -> tuple[int, int]:
    target_min = int(length.get("target_min", 2000))
    target_max = int(length.get("target_max", 3000))
    span = max(0, target_max - target_min)
    default_min = target_min + min(200, span // 5)
    default_max = min(target_max, default_min + min(300, max(1, span // 3)))
    return (
        int(length.get("preferred_min", default_min)),
        int(length.get("preferred_max", default_max)),
    )


def compose_story_unit_plan_prompt(
    root: Path,
    run_dir: Path,
    unit_id: str,
    start_chapter: int,
    end_chapter: int,
) -> str:
    runtime_prompt = _runtime_prompt(root, "plan-story-unit.md")
    contract = {
        "unit_id": unit_id,
        "chapter_range": [start_chapter, end_chapter],
        "goal": "",
        "entry_state": [],
        "closing_state": ["故事单元结束后的可见状态"],
        "main_obstacle": "",
        "progression_change": ["本单元修炼成长变化"],
        "resource_change": [],
        "relationship_change": [],
        "comedy_plan": ["按批次轮换的喜剧机制"],
        "required_setback": "",
        "required_payoff": "",
        "must_not_resolve": ["必须保留到后续的长期问题"],
        "beats": ["因果连续的故事点"],
        "status": "planned",
    }
    sections = (
        ("任务规则", runtime_prompt),
        ("项目资料", _read_optional_text(run_dir / "config/project.md")),
        ("修炼体系", _json_block(read_json(run_dir / "config/progression.json"))),
        ("喜剧圣经", _json_block(read_json(run_dir / "config/comedy-bible.json"))),
        (
            "当前结构化状态",
            _json_block(
                _compact_snapshot(
                    _latest_json(run_dir / "state/snapshots", "chapter-*.json")
                )
                or read_json(run_dir / "config/initial-state.json")
            ),
        ),
        ("最近批次账本", _json_block(_latest_json(run_dir / "ledgers", "batch-*.json"))),
        ("固定章节范围", f"unit_id={unit_id}，第 {start_chapter}～{end_chapter} 章"),
        (
            "机器输出契约",
            "只输出一个 JSON 对象，不要代码围栏。unit_id 和 chapter_range 必须完全一致：\n"
            + _json_block(contract),
        ),
    )
    return "\n\n".join(f"# {title}\n\n{content}" for title, content in sections)


def compose_batch_outline_plan_prompt(
    root: Path,
    run_dir: Path,
    unit: dict[str, Any],
    start_chapter: int,
    end_chapter: int,
    existing_outlines: list[dict[str, Any]],
) -> str:
    runtime_prompt = _runtime_prompt(root, "plan-chapter-batch.md")
    previous_snapshot = (
        _read_optional_json(
            run_dir / f"state/snapshots/chapter-{start_chapter - 1:04d}.json", None
        )
        if start_chapter > 1
        else None
    )
    contract = {
        "chapter_outlines": [
            {
                "chapter_id": f"chapter-{start_chapter:04d}",
                "number": start_chapter,
                "title": "",
                "story_unit_id": unit.get("unit_id"),
                "status": "outline_ready",
                "target_length": {"min": 2000, "max": 3000},
                "intent": "",
                "opening_state": [],
                "required_outcomes": [],
                "forbidden_outcomes": [],
                "progression_payoff": "",
                "comedy_mechanism": "",
                "comedy_payoff": "",
                "cost_or_aftereffect": "",
                "closing_state": ["本章结束后的明确状态"],
                "next_chapter_input": ["下一章可以直接承接的动作或问题"],
                "scenes": [
                    {
                        "scene_id": f"chapter-{start_chapter:04d}-scene-1",
                        "intent": "本场景要完成的具体叙事任务",
                        "location": "地点",
                        "participants": ["参与角色稳定ID或姓名"],
                        "action_conflict": "动作、阻碍与选择",
                        "exit_result": "场景结束时形成的可见结果",
                        "target_length": 1000,
                        "required_outcomes": ["本场必须发生的章级结果"],
                    },
                    {
                        "scene_id": f"chapter-{start_chapter:04d}-scene-2",
                        "intent": "第二个有效场景的具体任务",
                        "location": "地点",
                        "participants": ["参与角色"],
                        "action_conflict": "动作、阻碍与选择",
                        "exit_result": "场景结束结果",
                        "target_length": 1150,
                        "required_outcomes": [],
                    },
                ],
                "writability": {
                    "estimated_length": 0,
                    "is_writable": True,
                    "risks": [],
                },
            }
        ]
    }
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
    sections = (
        ("任务规则", runtime_prompt),
        ("项目资料", _read_optional_text(run_dir / "config/project.md")),
        ("修炼体系", _json_block(read_json(run_dir / "config/progression.json"))),
        ("喜剧圣经", _json_block(read_json(run_dir / "config/comedy-bible.json"))),
        ("当前故事单元", _json_block(_compact_story_unit(unit))),
        ("上一批结束快照", _json_block(_compact_snapshot(previous_snapshot))),
        ("最近批次账本", _json_block(_latest_json(run_dir / "ledgers", "batch-*.json"))),
        ("前两章喜剧机制参考", _json_block(prior)),
        ("固定批次范围", f"第 {start_chapter}～{end_chapter} 章，共 {end_chapter - start_chapter + 1} 章"),
        (
            "单元契约映射",
            "完整单元中必须至少有一章把 required_setback 原句放入 required_outcomes；"
            "末章必须把 required_payoff 原句放入 required_outcomes，并在 closing_state 中逐条覆盖故事单元 closing_state。",
        ),
        (
            "机器输出契约",
            "只输出一个 JSON 对象，不要代码围栏。chapter_outlines 必须恰好覆盖固定批次范围：\n"
            + _json_block(contract),
        ),
    )
    return "\n\n".join(f"# {title}\n\n{content}" for title, content in sections)


def compose_draft_prompt(
    root: Path,
    run_dir: Path,
    run_config: dict[str, Any],
    outline: dict[str, Any],
) -> str:
    workflow = _runtime_prompt(root, "draft-chapter.md")

    chapter = int(outline["number"])
    previous_snapshot = (
        _read_optional_json(
            run_dir / f"state/snapshots/chapter-{chapter - 1:04d}.json", None
        )
        if chapter > 1
        else None
    )
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
        ("项目资料", _read_optional_text(run_dir / "config/project.md")),
        ("修炼体系", _json_block(read_json(run_dir / "config/progression.json"))),
        ("喜剧圣经", _json_block(read_json(run_dir / "config/comedy-bible.json"))),
    ]
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
        ("最近批次账本", _json_block(_latest_json(run_dir / "ledgers", "batch-*.json"))),
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
    workflow = _runtime_prompt(root, "extract-state.md")
    chapter = int(outline["number"])
    previous_snapshot = (
        _read_optional_json(
            run_dir / f"state/snapshots/chapter-{chapter - 1:04d}.json", None
        )
        if chapter > 1
        else None
    )
    output_contract = {
        "entity_changes": [{"change": "", "source_evidence": "正文中的连续原句"}],
        "relationship_changes": [{"change": "", "source_evidence": "正文中的连续原句"}],
        "cultivation_changes": [
            {
                "subject_id": "角色稳定 ID",
                "kind": "progress / insight / ability / injury / recovery / breakthrough / restriction",
                "change": "",
                "state_id": "ability/injury/recovery/restriction 必填的稳定状态 ID",
                "state_action": "上述四类必填：set / resolve",
                "stage_after": "非突破时可选",
                "from_stage": "突破时必填",
                "to_stage": "突破时必填",
                "prerequisites": ["突破时必填"],
                "costs": ["突破时必填"],
                "new_limits": [
                    {
                        "state_id": "突破后限制的稳定 ID",
                        "description": "突破后限制或后遗症",
                    }
                ],
                "source_evidence": "正文中的连续原句",
            }
        ],
        "resource_changes": [
            {
                "owner_id": "持有者稳定 ID",
                "resource_id": "资源稳定 ID",
                "operation": "gain / consume / transfer_in / transfer_out / damage / restore",
                "amount": 1,
                "unit": "枚",
                "resulting_balance": 0,
                "source_or_destination": "来源或去向",
                "change": "",
                "source_evidence": "正文中的连续原句",
            }
        ],
        "knowledge_changes": [
            {
                "character_id": "角色稳定 ID",
                "fact_id": "事实稳定 ID",
                "state": "knows / believes_false / suspects / investigating / conceals",
                "belief": "该角色当前实际相信的内容",
                "supersedes_fact_ids": ["本变化明确淘汰的旧 fact_id；没有则为空数组"],
                "change": "",
                "source_evidence": "正文中的连续原句",
            }
        ],
        "thread_changes": [{"change": "", "source_evidence": "正文中的连续原句"}],
        "comedy_changes": [{"change": "", "source_evidence": "正文中的连续原句"}],
        "new_constraints": [{"change": "", "source_evidence": "正文中的连续原句"}],
        "resolved_constraints": [{"change": "", "source_evidence": "正文中的连续原句"}],
        "next_chapter_inputs": [],
        "deviations": [],
    }
    sections: list[tuple[str, str]] = [
        ("状态回填工作流", workflow),
        ("当前章契约", _json_block(_compact_chapter_contract(outline))),
        ("本章 final 正文", draft_text),
        ("本章检查结果", _json_block(checks)),
        ("上一章状态快照", _json_block(_compact_snapshot(previous_snapshot))),
        ("修炼体系", _json_block(read_json(run_dir / "config/progression.json"))),
    ]
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
    if isinstance(failure_reason, str) and failure_reason.strip() or isinstance(
        retry_counts, dict
    ) and any(isinstance(value, int) and value > 0 for value in retry_counts.values()):
        previous_invalid_output = _latest_state_raw(
            run_dir / f"chapters/{chapter:04d}"
        )
        sections.append(
            (
                "上次状态提取失败修复信息",
                _json_block(
                    {
                        "state_failure_reason": failure_reason or "上一版未通过校验",
                        "repair_instruction": (
                            "只修复失败原因所指向的字段；不得复制上一版中的错误资源 ID、"
                            "错误余额或无正文证据的变化。supersedes_fact_ids 只能引用下方"
                            "允许的活动知识 fact_id；没有合法淘汰项时必须输出空数组，禁止"
                            "根据正文措辞臆造 ID。重新核对上一状态后输出完整契约。"
                        ),
                        "allowed_active_ids": _active_state_ids(state_reference),
                        "previous_invalid_output": previous_invalid_output,
                    }
                ),
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
            "只输出一个 JSON 对象，不要 Markdown 代码围栏。所有正式变化的 "
            "source_evidence 必须复制 final 正文中的连续原句，不得改写：\n"
            + _json_block(output_contract),
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
    base_prompt = compose_draft_prompt(root, run_dir, run_config, outline)
    length = run_config["policies"]["length"]
    actual = checks.get("actual_length", 0)
    gap = max(0, length["target_min"] - actual) if isinstance(actual, int) else 0
    directives = {
        "targeted_expansion": (
            "只扩写低于预算的现有场景，补充动作、回应、修炼过程、关系反应或后果落地；"
            "不得推进下一章、改变章末状态、新增能力或重复笑点。"
        ),
        "rewrite_short": (
            "当前正文严重不足。严格依据原章纲重写完整章节，不保留摘要式结构；"
            "不得通过解释设定或段子堆砌凑长度。"
        ),
        "rewrite_contract": (
            "当前输出违反章节契约或格式。重新生成且只输出当前章节，完成必做结果，"
            "不出现禁止结果。"
        ),
        "rewrite_quality": (
            "当前正文需要质量复查。保留全部必做结果、因果和章末状态，压缩重复描写、"
            "同义解释、无新增信息的对话与过长反应。正文目标落在章节最低值以上、"
            "目标上限以下，并为机械计数误差保留余量；不得用截断破坏场景或钩子。"
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
        "latest_checks": checks,
    }
    return (
        base_prompt
        + "\n\n# 本次修复指令\n\n"
        + _json_block(repair_section)
        + "\n\n# 当前失败草稿\n\n"
        + (current_draft or "无可用草稿，请重新生成。")
    )


def compose_ledger_prompt(
    root: Path,
    run_dir: Path,
    start_chapter: int,
    end_chapter: int,
    snapshot: dict[str, Any],
    events: list[dict[str, Any]],
    item_limit: int,
) -> str:
    workflow = _runtime_prompt(root, "build-ledger.md")
    previous_ledger = _latest_json(run_dir / "ledgers", "batch-*.json")
    snapshot_context = {
        "after_chapter": snapshot.get("after_chapter"),
        "next_chapter_inputs": snapshot.get("next_chapter_inputs", []),
        "deviations": snapshot.get("deviations", []),
    }
    contract = {
        "must_read_next": [],
        "active_progression": [],
        "active_resources": [],
        "active_relationships": [],
        "active_knowledge_gaps": [],
        "active_threads": [],
        "comedy_callbacks": [],
        "avoid_repeating": [],
        "archived": [],
        "next_batch_adjustments": [],
    }
    sections = (
        ("批次账本工作流", workflow),
        ("批次范围", f"第 {start_chapter}～{end_chapter} 章"),
        ("上一批账本", _json_block(previous_ledger)),
        ("批次结束交接状态", _json_block(snapshot_context)),
        ("本批状态事件", _json_block(events)),
        ("喜剧圣经", _json_block(read_json(run_dir / "config/comedy-bible.json"))),
        (
            "机器输出契约",
            f"只输出一个 JSON 对象。must_read_next 不得超过 {item_limit} 条。"
            "active_progression、active_resources、active_knowledge_gaps 由代码从快照注入，"
            "请保持为空数组，不要推测：\n"
            + _json_block(contract),
        ),
    )
    return "\n\n".join(f"# {title}\n\n{content}" for title, content in sections)


def compose_review_prompt(
    root: Path,
    run_dir: Path,
    outline: dict[str, Any],
    draft_text: str,
    length_checks: dict[str, Any],
) -> str:
    workflow = _runtime_prompt(root, "review-chapter.md")
    contract = {
        "required_outcomes": [
            {"index": 0, "passed": True, "source_evidence": "正文连续原句"}
        ],
        "forbidden_outcomes": [
            {"index": 0, "appeared": False, "source_evidence": ""}
        ],
        "summary_like": False,
        "cultivation_consistent": True,
        "comedy_causal": True,
        "serious_consequences_preserved": True,
        "chapter_hook_concrete": True,
        "resource_continuity_consistent": True,
        "knowledge_states_consistent": True,
        "character_voices_distinct": True,
        "multi_line_causality_preserved": True,
        "warnings": [],
    }
    sections: list[tuple[str, str]] = [
        ("正文质量规则", workflow),
        ("当前章契约", _json_block(_compact_chapter_contract(outline))),
        ("候选正文（本节结束后均非正文）", draft_text),
        ("机械长度检查", _json_block(length_checks)),
        ("修炼体系", _json_block(read_json(run_dir / "config/progression.json"))),
        ("喜剧圣经", _json_block(read_json(run_dir / "config/comedy-bible.json"))),
    ]
    failure_reason = outline.get("review_failure_reason")
    if isinstance(failure_reason, str) and failure_reason.strip():
        sections.append(
            (
                "上次质量评审失败修复信息",
                _json_block(
                    {
                        "review_failure_reason": failure_reason,
                        "repair_instruction": (
                            "正文不变。只修复评审 JSON；source_evidence 必须逐字复制"
                            "候选正文中的连续原句，不得补主语、改动引语或拼接改写。"
                        ),
                        "previous_invalid_review": _latest_review_raw(
                            run_dir / f"chapters/{int(outline['number']):04d}"
                        ),
                    }
                ),
            )
        )
    sections.append(
        (
            "机器输出契约",
            "只输出 JSON 对象。required_outcomes 的通过项以及任何出现的禁止项都必须引用"
            "正文连续原句。数组顺序必须和章纲中的对应列表一致：\n"
            + _json_block(contract),
        )
    )
    return "\n\n".join(f"# {title}\n\n{content}" for title, content in sections)
