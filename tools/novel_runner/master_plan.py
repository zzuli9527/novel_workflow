"""全书总纲的结构校验、人工审批与故事单元定位。"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from .storage import atomic_write_json, read_json, resolve_run_dir, run_lock


class MasterPlanError(RuntimeError):
    """全书总纲尚未满足后续规划或写作条件。"""


@dataclass(frozen=True, slots=True)
class MasterPlanIssue:
    path: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class MasterPlanReport:
    run_id: str
    valid: bool
    status: str
    content_sha256: str | None
    issues: tuple[MasterPlanIssue, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "run_id": self.run_id,
            "valid": self.valid,
            "status": self.status,
            "content_sha256": self.content_sha256,
            "issues": [issue.to_dict() for issue in self.issues],
        }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_master_plan() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "target_chapters": {"start": 1, "end": None},
        "protagonist_paths": [],
        "active_goal_phases": [],
        "final_conflict": {
            "antagonist": "",
            "antagonist_goal": "",
            "climax_rules": [],
            "resolution": "",
            "cost": "",
        },
        "volumes": [],
        "approval": {
            "status": "draft",
            "approved_at": None,
            "content_sha256": None,
        },
    }


def master_plan_content_hash(data: dict[str, Any]) -> str:
    content = {key: value for key, value in data.items() if key != "approval"}
    normalized = json.dumps(
        content,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _is_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _require_keys(
    issues: list[MasterPlanIssue], path: str, data: dict[str, Any], keys: Iterable[str]
) -> None:
    for key in keys:
        if key not in data:
            issues.append(MasterPlanIssue(f"{path}.{key}", "缺少必填字段"))


def _text(
    issues: list[MasterPlanIssue], path: str, value: Any, *, complete: bool
) -> bool:
    if not isinstance(value, str):
        issues.append(MasterPlanIssue(path, "应为字符串"))
        return False
    if complete and not value.strip():
        issues.append(MasterPlanIssue(path, "批准前必须填写"))
        return False
    return True


def _list(
    issues: list[MasterPlanIssue], path: str, value: Any, *, complete: bool = False
) -> bool:
    if not isinstance(value, list):
        issues.append(MasterPlanIssue(path, "应为数组"))
        return False
    if complete and not value:
        issues.append(MasterPlanIssue(path, "批准前必须填写"))
        return False
    return True


def _range(
    issues: list[MasterPlanIssue],
    path: str,
    value: Any,
    *,
    allow_open_end: bool,
) -> tuple[int, int] | None:
    if not isinstance(value, list) or len(value) != 2:
        issues.append(MasterPlanIssue(path, "应为 [起始章, 结束章]"))
        return None
    start, end = value
    if not _is_int(start) or (not _is_int(end) and not (allow_open_end and end is None)):
        issues.append(MasterPlanIssue(path, "章节范围必须使用整数"))
        return None
    if start <= 0 or (_is_int(end) and end < start):
        issues.append(MasterPlanIssue(path, "章节范围无效"))
        return None
    if end is None:
        return None
    return start, end


def _validate_protagonists(
    issues: list[MasterPlanIssue], value: Any, *, complete: bool
) -> set[str]:
    if not _list(issues, "master_plan.protagonist_paths", value, complete=complete):
        return set()
    if complete and len(value) < 2:
        issues.append(
            MasterPlanIssue(
                "master_plan.protagonist_paths", "至少需要两条独立主角成长路径"
            )
        )
    ids: set[str] = set()
    fields = (
        "protagonist_id",
        "name",
        "cultivation_path",
        "early_milestone",
        "middle_milestone",
        "late_milestone",
        "end_state",
    )
    for index, item in enumerate(value):
        path = f"master_plan.protagonist_paths[{index}]"
        if not isinstance(item, dict):
            issues.append(MasterPlanIssue(path, "应为对象"))
            continue
        _require_keys(issues, path, item, fields)
        for field in fields:
            if field in item:
                _text(issues, f"{path}.{field}", item[field], complete=complete)
        protagonist_id = item.get("protagonist_id")
        if isinstance(protagonist_id, str) and protagonist_id.strip():
            if protagonist_id in ids:
                issues.append(
                    MasterPlanIssue(f"{path}.protagonist_id", "主角稳定 ID 重复")
                )
            ids.add(protagonist_id)
    return ids


def _validate_goal_phases(
    issues: list[MasterPlanIssue],
    value: Any,
    *,
    complete: bool,
    target: tuple[int, int] | None,
    protagonist_ids: set[str],
) -> None:
    if not _list(issues, "master_plan.active_goal_phases", value, complete=complete):
        return
    if complete and len(value) < 3:
        issues.append(
            MasterPlanIssue(
                "master_plan.active_goal_phases", "至少需要前期、中期、后期三个目标阶段"
            )
        )
    phase_ids: set[str] = set()
    ranges: list[tuple[int, int, str]] = []
    for index, item in enumerate(value):
        path = f"master_plan.active_goal_phases[{index}]"
        if not isinstance(item, dict):
            issues.append(MasterPlanIssue(path, "应为对象"))
            continue
        _require_keys(
            issues, path, item, ("phase_id", "label", "chapter_range", "goals", "shared_goal")
        )
        for field in ("phase_id", "label", "shared_goal"):
            if field in item:
                _text(issues, f"{path}.{field}", item[field], complete=complete)
        phase_id = item.get("phase_id")
        if isinstance(phase_id, str) and phase_id.strip():
            if phase_id in phase_ids:
                issues.append(MasterPlanIssue(f"{path}.phase_id", "目标阶段 ID 重复"))
            phase_ids.add(phase_id)
        chapter_range = _range(
            issues,
            f"{path}.chapter_range",
            item.get("chapter_range"),
            allow_open_end=not complete,
        )
        if chapter_range is not None:
            ranges.append((*chapter_range, path))
        goals = item.get("goals")
        if not _list(issues, f"{path}.goals", goals, complete=complete):
            continue
        covered: set[str] = set()
        for goal_index, goal in enumerate(goals):
            goal_path = f"{path}.goals[{goal_index}]"
            if not isinstance(goal, dict):
                issues.append(MasterPlanIssue(goal_path, "应为对象"))
                continue
            _require_keys(issues, goal_path, goal, ("protagonist_id", "goal"))
            for field in ("protagonist_id", "goal"):
                if field in goal:
                    _text(
                        issues,
                        f"{goal_path}.{field}",
                        goal[field],
                        complete=complete,
                    )
            protagonist_id = goal.get("protagonist_id")
            if isinstance(protagonist_id, str) and protagonist_id.strip():
                if complete and protagonist_id not in protagonist_ids:
                    issues.append(
                        MasterPlanIssue(
                            f"{goal_path}.protagonist_id", "未引用主角成长路径中的稳定 ID"
                        )
                    )
                if protagonist_id in covered:
                    issues.append(
                        MasterPlanIssue(
                            f"{goal_path}.protagonist_id", "同一阶段的主角目标重复"
                        )
                    )
                covered.add(protagonist_id)
        if complete and covered != protagonist_ids:
            issues.append(
                MasterPlanIssue(f"{path}.goals", "每个目标阶段都必须覆盖全部主角")
            )
    if complete and target is not None:
        _validate_contiguous_ranges(
            issues,
            "master_plan.active_goal_phases",
            ranges,
            target,
        )


def _validate_final_conflict(
    issues: list[MasterPlanIssue], value: Any, *, complete: bool
) -> None:
    path = "master_plan.final_conflict"
    if not isinstance(value, dict):
        issues.append(MasterPlanIssue(path, "应为对象"))
        return
    fields = ("antagonist", "antagonist_goal", "climax_rules", "resolution", "cost")
    _require_keys(issues, path, value, fields)
    for field in ("antagonist", "antagonist_goal", "resolution", "cost"):
        if field in value:
            _text(issues, f"{path}.{field}", value[field], complete=complete)
    if "climax_rules" in value:
        _list(
            issues,
            f"{path}.climax_rules",
            value["climax_rules"],
            complete=complete,
        )


def _validate_contiguous_ranges(
    issues: list[MasterPlanIssue],
    path: str,
    ranges: list[tuple[int, int, str]],
    expected: tuple[int, int],
) -> None:
    ordered = sorted(ranges, key=lambda item: (item[0], item[1]))
    cursor = expected[0]
    for start, end, item_path in ordered:
        if start != cursor:
            relation = "重叠" if start < cursor else "存在空档"
            issues.append(MasterPlanIssue(item_path, f"章节范围{relation}，应从第 {cursor} 章开始"))
        cursor = max(cursor, end + 1)
    if cursor != expected[1] + 1:
        issues.append(
            MasterPlanIssue(path, f"章节范围必须完整覆盖第 {expected[0]}～{expected[1]} 章")
        )


def _validate_volumes(
    issues: list[MasterPlanIssue],
    value: Any,
    *,
    complete: bool,
    target: tuple[int, int] | None,
    unit_min: int,
    unit_max: int,
) -> None:
    if not _list(issues, "master_plan.volumes", value, complete=complete):
        return
    volume_ids: set[str] = set()
    unit_ids: set[str] = set()
    volume_ranges: list[tuple[int, int, str]] = []
    for volume_index, volume in enumerate(value):
        path = f"master_plan.volumes[{volume_index}]"
        if not isinstance(volume, dict):
            issues.append(MasterPlanIssue(path, "应为对象"))
            continue
        fields = (
            "volume_id",
            "title",
            "chapter_range",
            "goal",
            "climax",
            "resources",
            "comedy_plan",
            "relationship_changes",
            "irreversible_choices",
            "rough_units",
        )
        _require_keys(issues, path, volume, fields)
        for field in ("volume_id", "title", "goal", "climax"):
            if field in volume:
                _text(issues, f"{path}.{field}", volume[field], complete=complete)
        volume_id = volume.get("volume_id")
        if isinstance(volume_id, str) and volume_id.strip():
            if volume_id in volume_ids:
                issues.append(MasterPlanIssue(f"{path}.volume_id", "卷 ID 重复"))
            volume_ids.add(volume_id)
        volume_range = _range(
            issues,
            f"{path}.chapter_range",
            volume.get("chapter_range"),
            allow_open_end=not complete,
        )
        if volume_range is not None:
            volume_ranges.append((*volume_range, path))
        for field in (
            "resources",
            "comedy_plan",
            "relationship_changes",
            "irreversible_choices",
        ):
            if field in volume:
                _list(issues, f"{path}.{field}", volume[field], complete=complete)
        rough_units = volume.get("rough_units")
        if not _list(issues, f"{path}.rough_units", rough_units, complete=complete):
            continue
        unit_ranges: list[tuple[int, int, str]] = []
        for unit_index, unit in enumerate(rough_units):
            unit_path = f"{path}.rough_units[{unit_index}]"
            if not isinstance(unit, dict):
                issues.append(MasterPlanIssue(unit_path, "应为对象"))
                continue
            unit_fields = (
                "unit_id",
                "title",
                "chapter_range",
                "goal",
                "main_obstacle",
                "required_setback",
                "required_payoff",
                "closing_state",
                "next_interface",
                "must_not_resolve",
            )
            _require_keys(issues, unit_path, unit, unit_fields)
            for field in (
                "unit_id",
                "title",
                "goal",
                "main_obstacle",
                "required_setback",
                "required_payoff",
            ):
                if field in unit:
                    _text(
                        issues,
                        f"{unit_path}.{field}",
                        unit[field],
                        complete=complete,
                    )
            unit_id = unit.get("unit_id")
            if isinstance(unit_id, str) and unit_id.strip():
                if unit_id in unit_ids:
                    issues.append(MasterPlanIssue(f"{unit_path}.unit_id", "故事单元 ID 重复"))
                unit_ids.add(unit_id)
            unit_range = _range(
                issues,
                f"{unit_path}.chapter_range",
                unit.get("chapter_range"),
                allow_open_end=not complete,
            )
            if unit_range is not None:
                start, end = unit_range
                unit_ranges.append((start, end, unit_path))
                count = end - start + 1
                if complete and not unit_min <= count <= unit_max:
                    issues.append(
                        MasterPlanIssue(
                            f"{unit_path}.chapter_range",
                            f"故事单元必须为 {unit_min}～{unit_max} 章，当前为 {count} 章",
                        )
                    )
                if complete and volume_range is not None and not (
                    volume_range[0] <= start <= end <= volume_range[1]
                ):
                    issues.append(
                        MasterPlanIssue(
                            f"{unit_path}.chapter_range", "故事单元必须完全位于所属卷内"
                        )
                    )
            for field in ("closing_state", "next_interface", "must_not_resolve"):
                if field in unit:
                    _list(issues, f"{unit_path}.{field}", unit[field], complete=complete)
        if complete and volume_range is not None:
            _validate_contiguous_ranges(
                issues,
                f"{path}.rough_units",
                unit_ranges,
                volume_range,
            )
    if complete and target is not None:
        _validate_contiguous_ranges(issues, "master_plan.volumes", volume_ranges, target)


def _flatten_rough_units(data: dict[str, Any]) -> list[dict[str, Any]]:
    units: list[dict[str, Any]] = []
    for volume in data.get("volumes", []):
        if isinstance(volume, dict) and isinstance(volume.get("rough_units"), list):
            units.extend(item for item in volume["rough_units"] if isinstance(item, dict))
    def start_chapter(item: dict[str, Any]) -> int:
        chapter_range = item.get("chapter_range")
        if isinstance(chapter_range, list) and chapter_range and _is_int(chapter_range[0]):
            return chapter_range[0]
        return 0

    return sorted(units, key=start_chapter)


def _validate_existing_units(
    issues: list[MasterPlanIssue], data: dict[str, Any], story_units: Any
) -> None:
    if not isinstance(story_units, list):
        return
    expected = {
        unit.get("unit_id"): unit.get("chapter_range")
        for unit in _flatten_rough_units(data)
        if isinstance(unit.get("unit_id"), str)
    }
    ordered_actual: list[dict[str, Any]] = []
    for index, unit in enumerate(story_units):
        if not isinstance(unit, dict):
            issues.append(MasterPlanIssue(f"story_units[{index}]", "应为对象"))
            continue
        ordered_actual.append(unit)
        unit_id = unit.get("unit_id")
        if unit_id not in expected:
            issues.append(
                MasterPlanIssue(
                    f"story_units[{index}].unit_id", "已展开故事单元不在全书总纲中"
                )
            )
        elif unit.get("chapter_range") != expected[unit_id]:
            issues.append(
                MasterPlanIssue(
                    f"story_units[{index}].chapter_range",
                    "已展开故事单元范围与全书总纲不一致",
                )
            )
    ordered_actual.sort(
        key=lambda item: (
            item.get("chapter_range", [0])[0]
            if isinstance(item.get("chapter_range"), list)
            and item.get("chapter_range")
            and _is_int(item["chapter_range"][0])
            else 0
        )
    )
    planned_ids = [item.get("unit_id") for item in _flatten_rough_units(data)]
    actual_ids = [item.get("unit_id") for item in ordered_actual]
    if actual_ids != planned_ids[: len(actual_ids)]:
        issues.append(
            MasterPlanIssue(
                "story_units", "已展开故事单元必须按全书总纲顺序连续覆盖"
            )
        )


def validate_master_plan_data(
    data: Any,
    *,
    complete: bool,
    run_config: dict[str, Any] | None = None,
    initial_state: dict[str, Any] | None = None,
    story_units: Any = None,
    check_approval_hash: bool = True,
) -> tuple[MasterPlanIssue, ...]:
    issues: list[MasterPlanIssue] = []
    if not isinstance(data, dict):
        return (MasterPlanIssue("master_plan", "应为对象"),)
    _require_keys(
        issues,
        "master_plan",
        data,
        (
            "schema_version",
            "target_chapters",
            "protagonist_paths",
            "active_goal_phases",
            "final_conflict",
            "volumes",
            "approval",
        ),
    )
    if "schema_version" in data:
        _text(
            issues,
            "master_plan.schema_version",
            data["schema_version"],
            complete=True,
        )

    target: tuple[int, int] | None = None
    target_data = data.get("target_chapters")
    if not isinstance(target_data, dict):
        issues.append(MasterPlanIssue("master_plan.target_chapters", "应为对象"))
    else:
        _require_keys(issues, "master_plan.target_chapters", target_data, ("start", "end"))
        start = target_data.get("start")
        end = target_data.get("end")
        if not _is_int(start) or start <= 0:
            issues.append(
                MasterPlanIssue("master_plan.target_chapters.start", "必须是正整数")
            )
        elif complete and start != 1:
            issues.append(
                MasterPlanIssue(
                    "master_plan.target_chapters.start", "当前执行器要求全书从第 1 章开始"
                )
            )
        if end is not None and (
            not _is_int(end) or not _is_int(start) or end < start
        ):
            issues.append(
                MasterPlanIssue("master_plan.target_chapters.end", "必须是不小于起始章的整数")
            )
        elif complete and end is None:
            issues.append(
                MasterPlanIssue("master_plan.target_chapters.end", "批准前必须填写")
            )
        elif _is_int(start) and _is_int(end):
            target = (start, end)

    protagonist_ids = _validate_protagonists(
        issues, data.get("protagonist_paths"), complete=complete
    )
    _validate_goal_phases(
        issues,
        data.get("active_goal_phases"),
        complete=complete,
        target=target,
        protagonist_ids=protagonist_ids,
    )
    _validate_final_conflict(issues, data.get("final_conflict"), complete=complete)
    batch = (run_config or {}).get("policies", {}).get("batch", {})
    unit_min = int(batch.get("story_unit_min", 10))
    unit_max = int(batch.get("story_unit_max", 20))
    _validate_volumes(
        issues,
        data.get("volumes"),
        complete=complete,
        target=target,
        unit_min=unit_min,
        unit_max=unit_max,
    )

    if complete and protagonist_ids and isinstance(initial_state, dict):
        cultivation = initial_state.get("cultivation", [])
        initial_ids = {
            item.get("subject_id")
            for item in cultivation
            if isinstance(item, dict) and isinstance(item.get("subject_id"), str)
        }
        missing = sorted(protagonist_ids - initial_ids)
        if len(initial_ids) >= 2 and missing:
            issues.append(
                MasterPlanIssue(
                    "master_plan.protagonist_paths",
                    f"主角稳定 ID 未写入 initial-state.json：{missing}",
                )
            )

    approval = data.get("approval")
    if not isinstance(approval, dict):
        issues.append(MasterPlanIssue("master_plan.approval", "应为对象"))
    else:
        _require_keys(
            issues,
            "master_plan.approval",
            approval,
            ("status", "approved_at", "content_sha256"),
        )
        status = approval.get("status")
        if status not in {"draft", "approved"}:
            issues.append(
                MasterPlanIssue("master_plan.approval.status", "应为 draft / approved")
            )
        if status == "approved" and check_approval_hash:
            stored_hash = approval.get("content_sha256")
            current_hash = master_plan_content_hash(data)
            if not isinstance(stored_hash, str) or stored_hash != current_hash:
                issues.append(
                    MasterPlanIssue(
                        "master_plan.approval.content_sha256",
                        "批准后的总纲内容已变化，请重新执行 approve-master-plan",
                    )
                )
            if not isinstance(approval.get("approved_at"), str) or not approval[
                "approved_at"
            ].strip():
                issues.append(
                    MasterPlanIssue(
                        "master_plan.approval.approved_at", "approved 状态必须记录批准时间"
                    )
                )

    if complete:
        _validate_existing_units(issues, data, story_units)
    return tuple(issues)


def validate_master_plan(root: Path, run_id: str) -> MasterPlanReport:
    run_dir = resolve_run_dir(root, run_id)
    data = read_json(run_dir / "config/master-plan.json")
    run_config = read_json(run_dir / "run.json")
    initial_state = read_json(run_dir / "config/initial-state.json")
    story_units = read_json(run_dir / "planning/story-units.json")
    issues = validate_master_plan_data(
        data,
        complete=True,
        run_config=run_config,
        initial_state=initial_state,
        story_units=story_units,
    )
    approval = data.get("approval") if isinstance(data, dict) else None
    status = approval.get("status", "invalid") if isinstance(approval, dict) else "invalid"
    content_hash = master_plan_content_hash(data) if isinstance(data, dict) else None
    return MasterPlanReport(run_id, not issues, str(status), content_hash, issues)


def approve_master_plan(root: Path, run_id: str) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        data = read_json(run_dir / "config/master-plan.json")
        run_config = read_json(run_dir / "run.json")
        initial_state = read_json(run_dir / "config/initial-state.json")
        story_units = read_json(run_dir / "planning/story-units.json")
        issues = validate_master_plan_data(
            data,
            complete=True,
            run_config=run_config,
            initial_state=initial_state,
            story_units=story_units,
            check_approval_hash=False,
        )
        if issues:
            details = "; ".join(f"{item.path}: {item.message}" for item in issues)
            raise MasterPlanError(f"全书总纲不能批准：{details}")
        approved_at = _utc_now()
        content_hash = master_plan_content_hash(data)
        updated = {
            **data,
            "approval": {
                "status": "approved",
                "approved_at": approved_at,
                "content_sha256": content_hash,
            },
        }
        atomic_write_json(run_dir / "config/master-plan.json", updated)
        return {
            "run_id": run_id,
            "status": "approved",
            "approved_at": approved_at,
            "content_sha256": content_hash,
        }


def require_approved_master_plan(root: Path, run_id: str) -> dict[str, Any]:
    report = validate_master_plan(root, run_id)
    issues = list(report.issues)
    if report.status != "approved":
        issues.append(
            MasterPlanIssue(
                "master_plan.approval.status",
                "必须先由人工执行 approve-master-plan",
            )
        )
    if issues:
        details = "; ".join(f"{item.path}: {item.message}" for item in issues)
        raise MasterPlanError(f"全书总纲未通过审批闸门：{details}")
    run_dir = resolve_run_dir(root, run_id)
    return read_json(run_dir / "config/master-plan.json")


def ensure_story_units_match_master(
    master_plan: dict[str, Any],
    story_units: list[dict[str, Any]],
    *,
    require_prefix: bool,
) -> None:
    if not all(isinstance(item, dict) for item in story_units):
        raise MasterPlanError("planning/story-units.json 中的每一项都必须是对象")
    planned = _flatten_rough_units(master_plan)
    expected = {
        item.get("unit_id"): item.get("chapter_range") for item in planned
    }
    def start_chapter(item: dict[str, Any]) -> int:
        chapter_range = item.get("chapter_range")
        if isinstance(chapter_range, list) and chapter_range and _is_int(chapter_range[0]):
            return chapter_range[0]
        return 0

    ordered_actual = sorted(story_units, key=start_chapter)
    for item in ordered_actual:
        unit_id = item.get("unit_id")
        if unit_id not in expected:
            raise MasterPlanError(f"故事单元 {unit_id} 不在已批准全书总纲中")
        if item.get("chapter_range") != expected[unit_id]:
            raise MasterPlanError(f"故事单元 {unit_id} 的章节范围与已批准全书总纲不一致")
    if require_prefix:
        expected_ids = [item.get("unit_id") for item in planned[: len(ordered_actual)]]
        actual_ids = [item.get("unit_id") for item in ordered_actual]
        if actual_ids != expected_ids:
            raise MasterPlanError("导入的故事单元必须从全书总纲首单元开始连续覆盖")


def next_rough_unit(
    master_plan: dict[str, Any], story_units: list[dict[str, Any]]
) -> dict[str, Any]:
    ensure_story_units_match_master(master_plan, story_units, require_prefix=True)
    planned = _flatten_rough_units(master_plan)
    if len(story_units) >= len(planned):
        raise MasterPlanError("已批准全书总纲中的故事单元均已展开")
    return planned[len(story_units)]


def master_plan_slice(master_plan: dict[str, Any], unit_id: str) -> dict[str, Any]:
    ordered_units = _flatten_rough_units(master_plan)
    matches = [index for index, item in enumerate(ordered_units) if item.get("unit_id") == unit_id]
    if len(matches) != 1:
        raise MasterPlanError(f"全书总纲中的故事单元 {unit_id} 不存在或重复")
    unit_index = matches[0]
    unit = ordered_units[unit_index]
    volume = next(
        (
            item
            for item in master_plan.get("volumes", [])
            if isinstance(item, dict)
            and any(
                rough.get("unit_id") == unit_id
                for rough in item.get("rough_units", [])
                if isinstance(rough, dict)
            )
        ),
        None,
    )
    if not isinstance(volume, dict):
        raise MasterPlanError(f"故事单元 {unit_id} 缺少所属卷")
    unit_range = unit.get("chapter_range", [0, 0])
    active_phases = [
        phase
        for phase in master_plan.get("active_goal_phases", [])
        if isinstance(phase, dict)
        and isinstance(phase.get("chapter_range"), list)
        and max(unit_range[0], phase["chapter_range"][0])
        <= min(unit_range[1], phase["chapter_range"][1])
    ]
    volume_fields = (
        "volume_id",
        "title",
        "chapter_range",
        "goal",
        "climax",
        "resources",
        "comedy_plan",
        "relationship_changes",
        "irreversible_choices",
    )
    previous = ordered_units[unit_index - 1] if unit_index > 0 else None
    return {
        "story_pillars": {
            "target_chapters": master_plan.get("target_chapters"),
            "protagonist_paths": master_plan.get("protagonist_paths"),
            "active_goal_phases": active_phases,
            "final_conflict": master_plan.get("final_conflict"),
        },
        "current_volume": {field: volume.get(field) for field in volume_fields},
        "current_rough_unit": unit,
        "previous_interface": previous.get("next_interface", []) if previous else [],
        "next_interface": unit.get("next_interface", []),
        "long_term_must_not_resolve": {
            "unit_items": unit.get("must_not_resolve", []),
            "final_conflict_boundary": {
                "antagonist": master_plan.get("final_conflict", {}).get("antagonist"),
                "resolution": master_plan.get("final_conflict", {}).get("resolution"),
                "instruction": "不得在当前故事单元提前完成终局解决",
            },
        },
    }
