"""Compact runtime artifacts into task-specific prompt projections."""

from __future__ import annotations

import json
from typing import Any


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
        "opening_promise_delivered",
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
