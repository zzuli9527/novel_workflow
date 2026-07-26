"""Extract, validate, and stage chapter state events."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from ..api_runtime import invoke_provider, mark_task_accepted
from ..file_storage import events_path, read_current_snapshot
from ..project_profile import load_project_profile
from ..prompting import compose_state_prompt
from ..provider import GenerationRequest, ProviderError, TextProvider
from ..schema_validation import WorkflowSchemaError, ensure_artifact_schema
from ..state_machine import transition_record
from ..state_store import StateStoreError, build_snapshot, ensure_event_compatible
from ..storage import StorageError, atomic_write_json, atomic_write_text, read_json, resolve_run_dir, run_lock
from ..structured_state import StructuredStateError, validate_structured_event
from ..workflow_runtime import workflow_source_manifest
from .common import (
    ChapterServiceError,
    _find_outline,
    _load_context,
    _next_state_version,
    _normalize_evidence,
    _pause_run,
    _relative_posix,
    _save_outlines,
)


STATE_EVENT_LIST_FIELDS = (
    "entity_changes",
    "relationship_changes",
    "cultivation_changes",
    "resource_changes",
    "knowledge_changes",
    "thread_changes",
    "comedy_changes",
    "new_constraints",
    "resolved_constraints",
    "next_chapter_inputs",
    "deviations",
)

EVIDENCE_REQUIRED_FIELDS = (
    "entity_changes",
    "relationship_changes",
    "cultivation_changes",
    "resource_changes",
    "knowledge_changes",
    "thread_changes",
    "comedy_changes",
    "new_constraints",
    "resolved_constraints",
)


def _parse_state_event(
    text: str,
    chapter_number: int,
    source_draft: str,
    draft_text: str,
) -> dict[str, Any]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ChapterServiceError(
            f"状态输出不是有效 JSON：第 {exc.lineno} 行第 {exc.colno} 列"
        ) from exc
    if not isinstance(data, dict):
        raise ChapterServiceError("状态输出必须是 JSON 对象")
    for field in STATE_EVENT_LIST_FIELDS:
        if field not in data:
            raise ChapterServiceError(f"状态输出缺少字段：{field}")
        if not isinstance(data[field], list):
            raise ChapterServiceError(f"状态字段必须是数组：{field}")

    normalized_draft = _normalize_evidence(draft_text)
    for field in EVIDENCE_REQUIRED_FIELDS:
        for index, item in enumerate(data[field]):
            if not isinstance(item, dict):
                raise ChapterServiceError(f"{field}[{index}] 必须是 JSON 对象")
            change = item.get("change")
            if not isinstance(change, str) or not change.strip():
                raise ChapterServiceError(f"{field}[{index}] 缺少 change")
            evidence = item.get("source_evidence")
            if not isinstance(evidence, str) or not evidence.strip():
                raise ChapterServiceError(f"{field}[{index}] 缺少 source_evidence")
            if _normalize_evidence(evidence) not in normalized_draft:
                raise ChapterServiceError(
                    f"{field}[{index}] 的 source_evidence 不存在于 final 正文"
                )

    source_sha256 = hashlib.sha256(draft_text.encode("utf-8")).hexdigest()
    event = {
        "state_schema_version": "1.1",
        "event_id": f"chapter-{chapter_number:04d}",
        "chapter": chapter_number,
        "source_draft": source_draft,
        "source_sha256": source_sha256,
        **{field: data[field] for field in STATE_EVENT_LIST_FIELDS},
    }
    try:
        validate_structured_event(event)
    except StructuredStateError as exc:
        raise ChapterServiceError(str(exc)) from exc
    return event


def extract_state(
    root: Path, run_id: str, chapter_number: int, provider: TextProvider
) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        return _extract_state_unlocked(root, run_id, chapter_number, provider)


def _extract_state_unlocked(
    root: Path, run_id: str, chapter_number: int, provider: TextProvider
) -> dict[str, Any]:
    run_dir, _, outlines = _load_context(root, run_id)
    index, outline = _find_outline(outlines, chapter_number)
    status = outline.get("status")
    if status not in {"draft_passed", "state_failed"}:
        raise ChapterServiceError("只有 draft_passed 或 state_failed 章节可以提取状态")

    run_config = read_json(run_dir / "run.json")
    if status == "state_failed":
        retry_kind = outline.get("state_failure_kind", "format")
        if retry_kind not in {"transport", "format", "content"}:
            retry_kind = "format"
        retry_counter_key = f"state_{retry_kind}"
        retry_counts = outline.get("retry_counts", {})
        if not isinstance(retry_counts, dict):
            retry_counts = {}
        current_count = retry_counts.get(retry_counter_key, 0)
        if not isinstance(current_count, int):
            current_count = 0
        max_retries = run_config["policies"]["retry"][retry_kind]
        if current_count >= max_retries:
            reason = (
                f"第 {chapter_number} 章状态提取 {retry_kind} 重试已达到上限 "
                f"{max_retries}"
            )
            _pause_run(run_dir, run_config, reason)
            raise ChapterServiceError(reason)
        outline = {
            **outline,
            "retry_counts": {
                **retry_counts,
                retry_counter_key: current_count + 1,
            },
        }

    outline = transition_record(outline, "state_extracting")
    outlines[index] = outline
    _save_outlines(run_dir, outlines)

    chapter_dir = run_dir / f"chapters/{chapter_number:04d}"
    final_path = chapter_dir / "draft.final.md"
    checks_path = chapter_dir / "checks.json"
    try:
        draft_text = final_path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise ChapterServiceError(f"无法读取 final 正文：{exc}") from exc
    checks = read_json(checks_path)
    prompt = compose_state_prompt(root, run_dir, outline, draft_text, checks)
    version = _next_state_version(chapter_dir)
    prompt_path = chapter_dir / f"state.prompt.v{version}.md"
    atomic_write_text(prompt_path, prompt)
    atomic_write_text(chapter_dir / "state.prompt.md", prompt)
    atomic_write_json(
        chapter_dir / f"state.workflow.v{version}.json",
            workflow_source_manifest(
                root,
                "extract_state",
                rule_context=load_project_profile(run_dir),
            ),
    )

    raw_path = chapter_dir / f"state.raw.v{version}.json"
    request = GenerationRequest(
        task="extract_state",
        prompt=prompt,
        metadata={"run_id": run_id, "chapter": chapter_number},
    )
    try:
        response = invoke_provider(
            run_dir,
            provider,
            request,
            prompt_path=prompt_path,
            output_path=raw_path,
            chapter=chapter_number,
        )
    except ProviderError as exc:
        outline = transition_record(outline, "state_failed")
        outline = {
            **outline,
            "state_failure_kind": "transport",
            "state_failure_reason": str(exc),
        }
        outlines[index] = outline
        _save_outlines(run_dir, outlines)
        atomic_write_json(chapter_dir / "outline.json", outline)
        raise ChapterServiceError(str(exc)) from exc

    atomic_write_text(chapter_dir / "state.raw.json", response.text)

    try:
        event = _parse_state_event(
            response.text,
            chapter_number,
            _relative_posix(final_path, run_dir),
            draft_text,
        )
        ensure_artifact_schema(root, "state_event", event)
    except (ChapterServiceError, WorkflowSchemaError) as exc:
        outline = transition_record(outline, "state_failed")
        outline = {
            **outline,
            "state_failure_kind": "format",
            "state_failure_reason": str(exc),
        }
        outlines[index] = outline
        _save_outlines(run_dir, outlines)
        atomic_write_json(chapter_dir / "outline.json", outline)
        raise

    try:
        previous_snapshot = (
            read_current_snapshot(run_dir, run_config, chapter_number - 1)
            if chapter_number > 1
            else None
        )
        initial_state = (
            read_json(run_dir / "config/initial-state.json")
            if chapter_number == 1
            else None
        )
        build_snapshot(event, previous_snapshot, initial_state=initial_state)
        ensure_event_compatible(events_path(run_dir), event)
    except StateStoreError as exc:
        failure = ChapterServiceError(str(exc))
        outline = transition_record(outline, "state_failed")
        outline = {
            **outline,
            "state_failure_kind": "content",
            "state_failure_reason": str(exc),
        }
        outlines[index] = outline
        _save_outlines(run_dir, outlines)
        atomic_write_json(chapter_dir / "outline.json", outline)
        raise failure from exc
    except StorageError as exc:
        failure = ChapterServiceError(str(exc))
        outline = transition_record(outline, "state_failed")
        outline = {
            **outline,
            "state_failure_kind": "format",
            "state_failure_reason": str(exc),
        }
        outlines[index] = outline
        _save_outlines(run_dir, outlines)
        atomic_write_json(chapter_dir / "outline.json", outline)
        raise failure from exc

    atomic_write_json(chapter_dir / "state-event.json", event)
    outline = transition_record(outline, "state_ready")
    outline = {
        key: value
        for key, value in outline.items()
        if key not in {"state_failure_kind", "state_failure_reason"}
    }
    outlines[index] = outline
    _save_outlines(run_dir, outlines)
    atomic_write_json(chapter_dir / "outline.json", outline)
    mark_task_accepted(run_dir, request, response, raw_path)
    return event
