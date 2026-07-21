"""修仙连续性所需的结构化初始状态、事件校验与快照投影。"""

from __future__ import annotations

from copy import deepcopy
import math
from typing import Any


class StructuredStateError(RuntimeError):
    """结构化修炼、资源或知识状态不连续。"""


CULTIVATION_KINDS = {
    "progress",
    "insight",
    "ability",
    "injury",
    "recovery",
    "breakthrough",
    "restriction",
}
RESOURCE_OPERATIONS = {
    "gain": 1,
    "consume": -1,
    "transfer_in": 1,
    "transfer_out": -1,
    "damage": -1,
    "restore": 1,
}
KNOWLEDGE_STATES = {
    "knows",
    "believes_false",
    "suspects",
    "investigating",
    "conceals",
}
TRACKED_CULTIVATION_KINDS = {"ability", "injury", "recovery", "restriction"}
TRACKED_STATE_ACTIONS = {"set", "resolve"}
TRACKED_STATE_FIELDS = {
    "ability": "abilities",
    "injury": "injuries",
    "restriction": "limits",
}


def default_initial_state() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "cultivation": [],
        "resources": [],
        "knowledge": [],
    }


def _text(item: dict[str, Any], key: str, path: str) -> str:
    value = item.get(key)
    if not isinstance(value, str) or not value.strip():
        raise StructuredStateError(f"{path}.{key} 必须是非空字符串")
    return value.strip()


def _number(item: dict[str, Any], key: str, path: str, *, positive: bool) -> float:
    value = item.get(key)
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise StructuredStateError(f"{path}.{key} 必须是数字")
    numeric = float(value)
    if not math.isfinite(numeric):
        raise StructuredStateError(f"{path}.{key} 必须是有限数字")
    if positive and numeric <= 0:
        raise StructuredStateError(f"{path}.{key} 必须大于 0")
    if not positive and numeric < 0:
        raise StructuredStateError(f"{path}.{key} 不能小于 0")
    return numeric


def validate_initial_state(data: Any) -> None:
    if not isinstance(data, dict):
        raise StructuredStateError("initial_state 必须是对象")
    if not isinstance(data.get("schema_version"), str):
        raise StructuredStateError("initial_state.schema_version 必须是字符串")
    for field in ("cultivation", "resources", "knowledge"):
        if not isinstance(data.get(field), list):
            raise StructuredStateError(f"initial_state.{field} 必须是数组")

    cultivation_ids: set[str] = set()
    for index, item in enumerate(data["cultivation"]):
        path = f"initial_state.cultivation[{index}]"
        if not isinstance(item, dict):
            raise StructuredStateError(f"{path} 必须是对象")
        subject_id = _text(item, "subject_id", path)
        _text(item, "stage", path)
        if subject_id in cultivation_ids:
            raise StructuredStateError(f"初始修炼主体重复：{subject_id}")
        cultivation_ids.add(subject_id)
        for field in ("abilities", "injuries", "limits"):
            values = item.get(field, [])
            if not isinstance(values, list):
                raise StructuredStateError(f"{path}.{field} 必须是数组")
            for value_index, value in enumerate(values):
                value_path = f"{path}.{field}[{value_index}]"
                if isinstance(value, str) and value.strip():
                    continue
                if not isinstance(value, dict):
                    raise StructuredStateError(
                        f"{value_path} 必须是非空字符串或带稳定 ID 的对象"
                    )
                _text(value, "state_id", value_path)
                _text(value, "description", value_path)

    resource_keys: set[tuple[str, str, str]] = set()
    for index, item in enumerate(data["resources"]):
        path = f"initial_state.resources[{index}]"
        if not isinstance(item, dict):
            raise StructuredStateError(f"{path} 必须是对象")
        owner_id = _text(item, "owner_id", path)
        resource_id = _text(item, "resource_id", path)
        unit = _text(item, "unit", path)
        _number(item, "amount", path, positive=False)
        key = (owner_id, resource_id, unit)
        if key in resource_keys:
            raise StructuredStateError(f"初始资源重复：{key}")
        resource_keys.add(key)

    knowledge_keys: set[tuple[str, str]] = set()
    for index, item in enumerate(data["knowledge"]):
        path = f"initial_state.knowledge[{index}]"
        if not isinstance(item, dict):
            raise StructuredStateError(f"{path} 必须是对象")
        character_id = _text(item, "character_id", path)
        fact_id = _text(item, "fact_id", path)
        state = _text(item, "state", path)
        if state not in KNOWLEDGE_STATES:
            raise StructuredStateError(f"{path}.state 不是允许的知识状态")
        _text(item, "belief", path)
        key = (character_id, fact_id)
        if key in knowledge_keys:
            raise StructuredStateError(f"初始知识状态重复：{key}")
        knowledge_keys.add(key)


def validate_structured_event(event: dict[str, Any]) -> None:
    state_schema_version = event.get("state_schema_version", "1.0")
    if state_schema_version not in {"1.0", "1.1"}:
        raise StructuredStateError("state_schema_version 只支持 1.0 或 1.1")
    strict_tracked_state = state_schema_version == "1.1"
    cultivation = event.get("cultivation_changes", [])
    resources = event.get("resource_changes", [])
    knowledge = event.get("knowledge_changes", [])

    for index, item in enumerate(cultivation):
        path = f"cultivation_changes[{index}]"
        subject_id = _text(item, "subject_id", path)
        kind = _text(item, "kind", path)
        if kind not in CULTIVATION_KINDS:
            raise StructuredStateError(f"{path}.kind 不是允许的修炼变化类型")
        if kind == "breakthrough":
            from_stage = _text(item, "from_stage", path)
            to_stage = _text(item, "to_stage", path)
            if from_stage == to_stage:
                raise StructuredStateError(f"{path} 突破前后境界不能相同")
            for field in ("prerequisites", "costs", "new_limits"):
                value = item.get(field)
                if not isinstance(value, list) or not value:
                    raise StructuredStateError(f"{path}.{field} 必须是非空数组")
            for limit_index, limit in enumerate(item["new_limits"]):
                limit_path = f"{path}.new_limits[{limit_index}]"
                if isinstance(limit, str) and limit.strip():
                    continue
                if not isinstance(limit, dict):
                    raise StructuredStateError(
                        f"{limit_path} 必须是非空字符串或带稳定 ID 的对象"
                    )
                _text(limit, "state_id", limit_path)
                _text(limit, "description", limit_path)
        elif "stage_after" in item:
            _text(item, "stage_after", path)
        if strict_tracked_state and kind in TRACKED_CULTIVATION_KINDS:
            state_id = _text(item, "state_id", path)
            state_action = _text(item, "state_action", path)
            if state_action not in TRACKED_STATE_ACTIONS:
                raise StructuredStateError(
                    f"{path}.state_action 只允许 set 或 resolve"
                )
            if kind == "injury" and state_action != "set":
                raise StructuredStateError(
                    f"{path} injury 只能使用 state_action=set；解除伤势请使用 recovery"
                )
            if not state_id:
                raise StructuredStateError(f"{path}.state_id 无效")
        if not subject_id:
            raise StructuredStateError(f"{path}.subject_id 无效")

    for index, item in enumerate(resources):
        path = f"resource_changes[{index}]"
        owner_id = _text(item, "owner_id", path)
        resource_id = _text(item, "resource_id", path)
        unit = _text(item, "unit", path)
        operation = _text(item, "operation", path)
        if operation not in RESOURCE_OPERATIONS:
            raise StructuredStateError(f"{path}.operation 不是允许的资源操作")
        _number(item, "amount", path, positive=True)
        _number(item, "resulting_balance", path, positive=False)
        _text(item, "source_or_destination", path)
        if not owner_id or not resource_id or not unit:
            raise StructuredStateError(f"{path} 资源标识无效")

    knowledge_keys: set[tuple[str, str]] = set()
    for index, item in enumerate(knowledge):
        path = f"knowledge_changes[{index}]"
        character_id = _text(item, "character_id", path)
        fact_id = _text(item, "fact_id", path)
        state = _text(item, "state", path)
        if state not in KNOWLEDGE_STATES:
            raise StructuredStateError(f"{path}.state 不是允许的知识状态")
        _text(item, "belief", path)
        if strict_tracked_state:
            supersedes = item.get("supersedes_fact_ids")
            if not isinstance(supersedes, list) or not all(
                isinstance(value, str) and value.strip() for value in supersedes
            ):
                raise StructuredStateError(
                    f"{path}.supersedes_fact_ids 必须是字符串数组"
                )
        key = (character_id, fact_id)
        if key in knowledge_keys:
            raise StructuredStateError(
                f"同一章角色对同一事实出现冲突知识状态：{character_id}/{fact_id}"
            )
        knowledge_keys.add(key)


def _normalize_cultivation_entry(item: dict[str, Any]) -> dict[str, Any]:
    normalized = deepcopy(item)
    tracked: list[dict[str, str]] = []
    for kind, field in TRACKED_STATE_FIELDS.items():
        descriptions: list[str] = []
        for value in normalized.get(field, []):
            if isinstance(value, str):
                descriptions.append(value)
                continue
            state_id = value["state_id"].strip()
            description = value["description"].strip()
            descriptions.append(description)
            tracked.append(
                {
                    "state_id": state_id,
                    "kind": kind,
                    "description": description,
                }
            )
        normalized[field] = descriptions
    existing = normalized.get("tracked_states", [])
    if isinstance(existing, list):
        tracked.extend(
            deepcopy(value)
            for value in existing
            if isinstance(value, dict)
            and isinstance(value.get("state_id"), str)
            and isinstance(value.get("kind"), str)
            and isinstance(value.get("description"), str)
        )
    normalized["tracked_states"] = sorted(
        {value["state_id"]: value for value in tracked}.values(),
        key=lambda value: value["state_id"],
    )
    return normalized


def _initial_projection(initial_state: dict[str, Any] | None) -> dict[str, Any]:
    source = deepcopy(initial_state or default_initial_state())
    validate_initial_state(source)
    return {
        "cultivation": [
            _normalize_cultivation_entry(item) for item in source["cultivation"]
        ],
        "resources": deepcopy(source["resources"]),
        "knowledge": deepcopy(source["knowledge"]),
    }


def _apply_tracked_cultivation_change(
    current: dict[str, Any], change: dict[str, Any]
) -> None:
    state_id = change["state_id"]
    state_action = change["state_action"]
    event_kind = change["kind"]
    tracked = {
        item["state_id"]: deepcopy(item)
        for item in current.get("tracked_states", [])
        if isinstance(item, dict)
        and isinstance(item.get("state_id"), str)
        and item.get("kind") in TRACKED_STATE_FIELDS
        and isinstance(item.get("description"), str)
    }
    existing = tracked.get(state_id)

    if event_kind == "recovery":
        target_kind = "injury"
        if existing is None or existing.get("kind") != "injury":
            raise StructuredStateError(
                f"recovery 引用的活动伤势不存在：{state_id}"
            )
    else:
        target_kind = event_kind

    if existing is not None and existing.get("kind") != target_kind:
        raise StructuredStateError(
            f"状态 ID {state_id} 类型不连续：{existing.get('kind')} -> {target_kind}"
        )

    if existing is not None:
        old_field = TRACKED_STATE_FIELDS[existing["kind"]]
        current[old_field] = [
            value
            for value in current.get(old_field, [])
            if value != existing["description"]
        ]

    if state_action == "resolve":
        if existing is None:
            raise StructuredStateError(f"要解除的活动状态不存在：{state_id}")
        tracked.pop(state_id, None)
    else:
        description = change["change"]
        field = TRACKED_STATE_FIELDS[target_kind]
        values = [
            value for value in current.get(field, []) if isinstance(value, str)
        ]
        if description not in values:
            values.append(description)
        current[field] = values
        tracked[state_id] = {
            "state_id": state_id,
            "kind": target_kind,
            "description": description,
        }

    current["tracked_states"] = sorted(
        tracked.values(), key=lambda value: value["state_id"]
    )


def project_structured_state(
    event: dict[str, Any],
    previous: dict[str, Any] | None,
    initial_state: dict[str, Any] | None = None,
) -> dict[str, Any]:
    validate_structured_event(event)
    state = deepcopy(previous) if previous is not None else _initial_projection(initial_state)
    if not isinstance(state, dict):
        raise StructuredStateError("上一章 structured_state 必须是对象")
    for field in ("cultivation", "resources", "knowledge"):
        if not isinstance(state.get(field), list):
            raise StructuredStateError(f"structured_state.{field} 必须是数组")

    cultivation = {
        item["subject_id"]: _normalize_cultivation_entry(item)
        for item in state["cultivation"]
        if isinstance(item, dict) and isinstance(item.get("subject_id"), str)
    }
    for change in event.get("cultivation_changes", []):
        subject_id = change["subject_id"]
        current = cultivation.get(subject_id)
        if current is None:
            raise StructuredStateError(
                f"修炼主体 {subject_id} 不在初始状态或上一章快照中"
            )
        if change["kind"] == "breakthrough":
            if current.get("stage") != change["from_stage"]:
                raise StructuredStateError(
                    f"{subject_id} 突破前境界不连续：快照为 {current.get('stage')}，"
                    f"事件声明为 {change['from_stage']}"
                )
            current["stage"] = change["to_stage"]
            for limit in change["new_limits"]:
                if isinstance(limit, str):
                    current["limits"] = [*current.get("limits", []), limit]
                    continue
                _apply_tracked_cultivation_change(
                    current,
                    {
                        "kind": "restriction",
                        "state_id": limit["state_id"],
                        "state_action": "set",
                        "change": limit["description"],
                    },
                )
        elif isinstance(change.get("stage_after"), str):
            if current.get("stage") != change["stage_after"]:
                raise StructuredStateError(
                    f"{subject_id} 的境界发生变化但 kind 不是 breakthrough："
                    f"{current.get('stage')} -> {change['stage_after']}"
                )
        if (
            event.get("state_schema_version") == "1.1"
            and change["kind"] in TRACKED_CULTIVATION_KINDS
        ):
            _apply_tracked_cultivation_change(current, change)
        current["last_kind"] = change["kind"]
        current["last_change"] = change["change"]
        cultivation[subject_id] = current

    resources = {
        (item["owner_id"], item["resource_id"], item["unit"]): deepcopy(item)
        for item in state["resources"]
        if isinstance(item, dict)
        and all(isinstance(item.get(key), str) for key in ("owner_id", "resource_id", "unit"))
    }
    for change in event.get("resource_changes", []):
        key = (change["owner_id"], change["resource_id"], change["unit"])
        current = resources.get(
            key,
            {
                "owner_id": key[0],
                "resource_id": key[1],
                "unit": key[2],
                "amount": 0.0,
            },
        )
        expected = float(current["amount"]) + (
            RESOURCE_OPERATIONS[change["operation"]] * float(change["amount"])
        )
        if expected < -1e-9:
            raise StructuredStateError(
                f"资源余额不能为负：{key}，当前 {current['amount']}，变化 {change['amount']}"
            )
        resulting = float(change["resulting_balance"])
        if abs(expected - resulting) > 1e-9:
            raise StructuredStateError(
                f"资源余额不连续：{key}，机械结果 {expected}，事件声明 {resulting}"
            )
        current["amount"] = resulting
        current["last_operation"] = change["operation"]
        current["last_source_or_destination"] = change["source_or_destination"]
        resources[key] = current

    knowledge = {
        (item["character_id"], item["fact_id"]): deepcopy(item)
        for item in state["knowledge"]
        if isinstance(item, dict)
        and isinstance(item.get("character_id"), str)
        and isinstance(item.get("fact_id"), str)
    }
    for change in event.get("knowledge_changes", []):
        key = (change["character_id"], change["fact_id"])
        if event.get("state_schema_version") == "1.1":
            for old_fact_id in change["supersedes_fact_ids"]:
                if old_fact_id == change["fact_id"]:
                    continue
                old_key = (change["character_id"], old_fact_id)
                if old_key not in knowledge:
                    raise StructuredStateError(
                        "要淘汰的知识状态不存在："
                        f"{change['character_id']}/{old_fact_id}"
                    )
                knowledge.pop(old_key)
        knowledge[key] = {
            "character_id": key[0],
            "fact_id": key[1],
            "state": change["state"],
            "belief": change["belief"],
            "last_change": change["change"],
        }

    return {
        "cultivation": sorted(cultivation.values(), key=lambda item: item["subject_id"]),
        "resources": sorted(
            resources.values(),
            key=lambda item: (item["owner_id"], item["resource_id"], item["unit"]),
        ),
        "knowledge": sorted(
            knowledge.values(), key=lambda item: (item["character_id"], item["fact_id"])
        ),
    }
