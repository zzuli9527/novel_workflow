from __future__ import annotations

from pathlib import Path
from typing import Iterable

from tools.novel_runner.master_plan import approve_master_plan
from tools.novel_runner.storage import atomic_write_json


def build_master_plan(
    units: Iterable[tuple[str, int, int]],
    *,
    protagonist_ids: tuple[str, str] = ("lead-a", "lead-b"),
) -> dict[str, object]:
    unit_specs = list(units)
    if not unit_specs:
        raise ValueError("tests require at least one rough unit")
    target_start = unit_specs[0][1]
    target_end = unit_specs[-1][2]
    total = target_end - target_start + 1
    first_end = target_start + total // 3 - 1
    second_end = target_start + (total * 2) // 3 - 1
    phases = [
        ("early", target_start, first_end),
        ("middle", first_end + 1, second_end),
        ("late", second_end + 1, target_end),
    ]
    paths = [
        {
            "protagonist_id": protagonist_id,
            "name": protagonist_id,
            "cultivation_path": f"{protagonist_id} 独立修炼路线",
            "early_milestone": "建立能力边界",
            "middle_milestone": "承担路线代价",
            "late_milestone": "完成路线选择",
            "end_state": "以自身路线进入终局",
        }
        for protagonist_id in protagonist_ids
    ]
    rough_units = [
        {
            "unit_id": unit_id,
            "title": f"测试单元 {unit_id}",
            "chapter_range": [start, end],
            "goal": "完成阶段目标",
            "main_obstacle": "资源和规则同时受限",
            "required_setback": "中段失去一次机会",
            "required_payoff": "阶段目标得到可见兑现",
            "closing_state": ["阶段结果已经形成"],
            "next_interface": ["承接阶段后果"],
            "must_not_resolve": ["终局冲突"],
        }
        for unit_id, start, end in unit_specs
    ]
    return {
        "schema_version": "1.0",
        "target_chapters": {"start": target_start, "end": target_end},
        "protagonist_paths": paths,
        "active_goal_phases": [
            {
                "phase_id": phase_id,
                "label": phase_id,
                "chapter_range": [start, end],
                "goals": [
                    {
                        "protagonist_id": protagonist_id,
                        "goal": f"{protagonist_id} 的 {phase_id} 目标",
                    }
                    for protagonist_id in protagonist_ids
                ],
                "shared_goal": f"共同完成 {phase_id} 阶段任务",
            }
            for phase_id, start, end in phases
        ],
        "final_conflict": {
            "antagonist": "终局对手",
            "antagonist_goal": "夺取世界规则控制权",
            "climax_rules": ["必须由两条成长路线共同完成"],
            "resolution": "主角以不可逆选择结束冲突",
            "cost": "失去一项无法恢复的优势",
        },
        "volumes": [
            {
                "volume_id": "volume-01",
                "title": "测试卷",
                "chapter_range": [target_start, target_end],
                "goal": "完成本卷阶段问题",
                "climax": "本卷矛盾形成可见结果",
                "resources": ["资源发生获得或消耗"],
                "comedy_plan": ["轮换性格反差与规则错位"],
                "relationship_changes": ["双主角合作关系发生变化"],
                "irreversible_choices": ["做出不能无损撤销的选择"],
                "rough_units": rough_units,
            }
        ],
        "approval": {
            "status": "draft",
            "approved_at": None,
            "content_sha256": None,
        },
    }


def install_approved_master_plan(
    root: Path,
    run_id: str,
    units: Iterable[tuple[str, int, int]],
    *,
    protagonist_ids: tuple[str, str] = ("lead-a", "lead-b"),
) -> dict[str, object]:
    run_dir = root / "runs" / run_id
    plan = build_master_plan(units, protagonist_ids=protagonist_ids)
    atomic_write_json(run_dir / "config/master-plan.json", plan)
    approve_master_plan(root, run_id)
    return plan
