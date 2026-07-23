"""把工作流模板与当前运行数据拼装为单职责 Prompt。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .storage import StorageError, read_json
from .file_storage import is_v2, ledger_current_path, read_current_snapshot


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
    return _latest_json(run_dir / "ledgers", "batch-*.json")


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


def _verbatim_paragraph_catalog(text: str) -> list[dict[str, str]]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    paragraphs = [
        paragraph.strip()
        for paragraph in normalized.split("\n\n")
        if paragraph.strip()
    ]
    return [
        {"paragraph_id": f"P{index:03d}", "text": paragraph}
        for index, paragraph in enumerate(paragraphs, start=1)
    ]


def _compact_state_checks(checks: Any) -> Any:
    """Keep state-relevant review results without repeating review evidence."""

    if not isinstance(checks, dict):
        return checks
    quality = checks.get("quality")
    if not isinstance(quality, dict):
        quality = {}
    quality_fields = (
        "summary_like",
        "cultivation_consistent",
        "serious_consequences_preserved",
        "resource_continuity_consistent",
        "knowledge_states_consistent",
        "character_voices_distinct",
        "multi_line_causality_preserved",
        "warnings",
        "contract_failures",
        "quality_failures",
        "soft_quality_warnings",
    )
    return {
        "actual_length": checks.get("actual_length"),
        "hard_pass": checks.get("hard_pass"),
        "quality_status": checks.get("quality_status"),
        "quality": {field: quality.get(field) for field in quality_fields},
    }


def _strip_source_evidence(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _strip_source_evidence(item)
            for key, item in value.items()
            if key != "source_evidence"
        }
    if isinstance(value, list):
        return [_strip_source_evidence(item) for item in value]
    return value


def _state_retry_output_projection(text: str, *, excerpt_limit: int = 2000) -> Any:
    stripped = text.strip()
    if not stripped:
        return None
    try:
        parsed = json.loads(stripped)
    except json.JSONDecodeError:
        if len(stripped) <= excerpt_limit:
            return {"invalid_json_excerpt": stripped}
        head_length = excerpt_limit // 2
        tail_length = excerpt_limit - head_length
        return {
            "invalid_json_excerpt": (
                stripped[:head_length]
                + "\n...<truncated>...\n"
                + stripped[-tail_length:]
            ),
            "original_character_count": len(stripped),
        }
    return _strip_source_evidence(parsed)


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
            "active_tracked_states_by_subject": {},
            "resource_ids_by_owner": {},
            "knowledge_fact_ids_by_character": {},
        }
    structured = snapshot_or_initial.get("structured_state")
    if not isinstance(structured, dict):
        structured = snapshot_or_initial

    tracked_by_subject: dict[str, list[str]] = {}
    tracked_details_by_subject: dict[str, list[dict[str, Any]]] = {}
    cultivation = structured.get("cultivation", [])
    if not isinstance(cultivation, list):
        cultivation = []
    for item in cultivation:
        if not isinstance(item, dict) or not isinstance(item.get("subject_id"), str):
            continue
        active_states: list[dict[str, Any]] = []
        tracked_states = item.get("tracked_states", [])
        if isinstance(tracked_states, list):
            active_states.extend(
                state for state in tracked_states if isinstance(state, dict)
            )
        for kind, field in (
            ("ability", "abilities"),
            ("injury", "injuries"),
            ("restriction", "limits"),
        ):
            values = item.get(field, [])
            if not isinstance(values, list):
                continue
            active_states.extend(
                {**state, "kind": kind}
                for state in values
                if isinstance(state, dict)
            )

        details_by_id: dict[str, dict[str, Any]] = {}
        for state in active_states:
            state_id = state.get("state_id")
            kind = state.get("kind")
            if (
                not isinstance(state_id, str)
                or not state_id.strip()
                or kind not in {"ability", "injury", "restriction"}
            ):
                continue
            allowed_changes = {
                "ability": ["ability:set", "ability:resolve"],
                "injury": ["injury:set", "recovery:set", "recovery:resolve"],
                "restriction": ["restriction:set", "restriction:resolve"],
            }[kind]
            details_by_id[state_id] = {
                "state_id": state_id,
                "kind": kind,
                "allowed_changes": allowed_changes,
            }
        if details_by_id:
            subject_id = item["subject_id"]
            details = sorted(details_by_id.values(), key=lambda value: value["state_id"])
            tracked_by_subject[subject_id] = [value["state_id"] for value in details]
            tracked_details_by_subject[subject_id] = details

    resources_by_owner: dict[str, list[str]] = {}
    resources = structured.get("resources", [])
    if not isinstance(resources, list):
        resources = []
    for item in resources:
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
    knowledge = structured.get("knowledge", [])
    if not isinstance(knowledge, list):
        knowledge = []
    for item in knowledge:
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
        "active_tracked_states_by_subject": tracked_details_by_subject,
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


def _compact_state_chapter_contract(outline: Any) -> Any:
    """Project an outline down to facts needed by state extraction."""

    if not isinstance(outline, dict):
        return outline
    fields = (
        "chapter_id",
        "number",
        "title",
        "required_outcomes",
        "forbidden_outcomes",
        "cost_or_aftereffect",
        "closing_state",
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
    master_context: dict[str, Any],
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
    previous_snapshot = _planning_snapshot(run_dir, start_chapter - 1)
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
            "只输出一个 JSON 对象，不要代码围栏。每一章的 writability 必须是对象，"
            "并且 writability.is_writable 必须逐字输出为 JSON 布尔值 true；不得省略、"
            "写成字符串或留给读者推断。chapter_outlines 必须恰好覆盖固定批次范围：\n"
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
    workflow = _runtime_prompt(root, "extract-state.md")
    chapter = int(outline["number"])
    previous_snapshot = _previous_snapshot(run_dir, chapter - 1)
    output_contract = {
        "entity_changes": [{"change": "", "source_evidence": "正文中的连续原句"}],
        "relationship_changes": [{"change": "", "source_evidence": "正文中的连续原句"}],
        "cultivation_changes": [
            {
                "subject_id": "角色稳定 ID",
                "kind": "progress / insight / ability / injury / recovery / breakthrough / restriction",
                "change": "",
                "state_id": "ability/injury/recovery/restriction 必填的稳定状态 ID",
                "state_action": (
                    "上述四类必填：set / resolve；必须符合活动状态 ID 中的 allowed_changes，"
                    "recovery 只能引用当前活动 injury ID"
                ),
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
        ("当前章契约", _json_block(_compact_state_chapter_contract(outline))),
        ("本章 final 正文", draft_text),
        ("本章检查结果", _json_block(_compact_state_checks(checks))),
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
    previous_ledger = _latest_ledger(run_dir)
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
                            "逐字正文段落目录中的一个或多个连续段落，不得补主语、删字、"
                            "改动引语或拼接改写。不要复用上一版已经失败的证据文本。"
                        ),
                        "verbatim_paragraph_catalog": _verbatim_paragraph_catalog(
                            draft_text
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
