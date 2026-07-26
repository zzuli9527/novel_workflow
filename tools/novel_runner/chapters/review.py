"""Parse and execute independent chapter-quality review."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..api_runtime import invoke_provider, mark_task_accepted
from ..project_profile import load_project_profile
from ..prompting import compose_review_prompt
from ..provider import GenerationRequest, ProviderError, TextProvider
from ..state_machine import transition_record
from ..storage import atomic_write_json, atomic_write_text, read_json, resolve_run_dir, run_lock
from ..workflow_runtime import load_task_contract, workflow_source_manifest
from .common import (
    ChapterServiceError,
    _find_outline,
    _load_context,
    _next_review_version,
    _normalize_evidence,
    _pause_run,
    _read_current_draft,
    _save_outlines,
)


def _parse_quality_review(
    root: Path,
    text: str,
    outline: dict[str, Any],
    draft_text: str,
) -> dict[str, Any]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ChapterServiceError(
            f"质量评审不是有效 JSON：第 {exc.lineno} 行第 {exc.colno} 列"
        ) from exc
    if not isinstance(data, dict):
        raise ChapterServiceError("质量评审必须是 JSON 对象")
    required_results = data.get("required_outcomes")
    forbidden_results = data.get("forbidden_outcomes")
    warnings = data.get("warnings")
    if not isinstance(required_results, list) or not isinstance(forbidden_results, list):
        raise ChapterServiceError("质量评审缺少结果数组")
    if not isinstance(warnings, list):
        raise ChapterServiceError("质量评审 warnings 必须是数组")

    required_outcomes = outline.get("required_outcomes", [])
    forbidden_outcomes = outline.get("forbidden_outcomes", [])
    if not isinstance(required_outcomes, list) or not isinstance(forbidden_outcomes, list):
        raise ChapterServiceError("章纲契约字段必须是数组")
    if len(required_results) != len(required_outcomes):
        raise ChapterServiceError("required_outcomes 评审数量与章纲不一致")
    if len(forbidden_results) != len(forbidden_outcomes):
        raise ChapterServiceError("forbidden_outcomes 评审数量与章纲不一致")

    normalized_draft = _normalize_evidence(draft_text)
    contract_failures: list[str] = []
    for index, result in enumerate(required_results):
        if not isinstance(result, dict) or result.get("index") != index:
            raise ChapterServiceError(f"required_outcomes[{index}] 格式或 index 错误")
        if result.get("passed") is not True:
            contract_failures.append(f"必做结果 {index} 未完成")
            continue
        evidence = result.get("source_evidence")
        if not isinstance(evidence, str) or not evidence.strip():
            raise ChapterServiceError(f"required_outcomes[{index}] 缺少证据")
        if _normalize_evidence(evidence) not in normalized_draft:
            raise ChapterServiceError(f"required_outcomes[{index}] 证据不在正文中")

    for index, result in enumerate(forbidden_results):
        if not isinstance(result, dict) or result.get("index") != index:
            raise ChapterServiceError(f"forbidden_outcomes[{index}] 格式或 index 错误")
        appeared = result.get("appeared")
        if not isinstance(appeared, bool):
            raise ChapterServiceError(f"forbidden_outcomes[{index}] appeared 必须是布尔值")
        if appeared:
            evidence = result.get("source_evidence")
            if not isinstance(evidence, str) or not evidence.strip():
                raise ChapterServiceError(f"forbidden_outcomes[{index}] 缺少证据")
            if _normalize_evidence(evidence) not in normalized_draft:
                raise ChapterServiceError(f"forbidden_outcomes[{index}] 证据不在正文中")
            contract_failures.append(f"禁止结果 {index} 已出现")

    policy = load_task_contract(root, "review_chapter").get("quality_policy")
    if not isinstance(policy, dict):
        raise ChapterServiceError("正文审核契约缺少 quality_policy")
    failure_when_true = policy.get("failure_when_true")
    failure_when_false = policy.get("failure_when_false")
    soft_failure_when_false = policy.get("soft_failure_when_false")
    opening_field = policy.get("opening_failure_when_false")
    opening_chapter_max = policy.get("opening_chapter_max")
    field_groups = (failure_when_true, failure_when_false, soft_failure_when_false)
    if (
        not all(
            isinstance(group, list)
            and all(isinstance(field, str) and field for field in group)
            for group in field_groups
        )
        or not isinstance(opening_field, str)
        or not isinstance(opening_chapter_max, int)
    ):
        raise ChapterServiceError("正文审核契约 quality_policy 格式无效")
    quality_flags = set(
        [*failure_when_true, *failure_when_false, *soft_failure_when_false, opening_field]
    )
    for field in quality_flags:
        if not isinstance(data.get(field), bool):
            raise ChapterServiceError(f"质量评审 {field} 必须是布尔值")
    quality_failures: list[str] = []
    for field in failure_when_true:
        if data[field]:
            quality_failures.append(field)
    for field in failure_when_false:
        if not data[field]:
            quality_failures.append(field)
    chapter_number = outline.get("number")
    if (
        isinstance(chapter_number, int)
        and chapter_number <= opening_chapter_max
        and not data[opening_field]
    ):
        quality_failures.append(opening_field)
    soft_quality_warnings = [
        field
        for field in soft_failure_when_false
        if not data[field]
    ]
    return {
        **data,
        "contract_failures": contract_failures,
        "quality_failures": quality_failures,
        "soft_quality_warnings": soft_quality_warnings,
    }


def review_chapter(
    root: Path, run_id: str, chapter_number: int, provider: TextProvider
) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        run_dir, run_config, outlines = _load_context(root, run_id)
        index, outline = _find_outline(outlines, chapter_number)
        if outline.get("status") != "draft_quality_pending":
            raise ChapterServiceError("只有 draft_quality_pending 章节可以质量评审")
        if outline.get("review_failure_reason"):
            retry_counts = outline.get("retry_counts", {})
            if not isinstance(retry_counts, dict):
                retry_counts = {}
            current_count = retry_counts.get("review_format", 0)
            if not isinstance(current_count, int):
                current_count = 0
            max_retries = run_config["policies"]["retry"]["format"]
            if current_count >= max_retries:
                reason = (
                    f"第 {chapter_number} 章质量评审格式重试已达到上限 "
                    f"{max_retries}"
                )
                _pause_run(run_dir, run_config, reason)
                raise ChapterServiceError(reason)
            outline = {
                **outline,
                "retry_counts": {
                    **retry_counts,
                    "review_format": current_count + 1,
                },
            }
            outlines[index] = outline
            _save_outlines(run_dir, outlines)
        chapter_dir = run_dir / f"chapters/{chapter_number:04d}"
        draft_text = _read_current_draft(run_dir, outline)
        checks = read_json(chapter_dir / "checks.json")
        prompt = compose_review_prompt(root, run_dir, outline, draft_text, checks)
        version = _next_review_version(chapter_dir)
        prompt_path = chapter_dir / f"review.prompt.v{version}.md"
        raw_path = chapter_dir / f"review.raw.v{version}.json"
        atomic_write_text(prompt_path, prompt)
        atomic_write_text(chapter_dir / "review.prompt.md", prompt)
        atomic_write_json(
            chapter_dir / f"review.workflow.v{version}.json",
            workflow_source_manifest(
                root,
                "review_chapter",
                rule_context=load_project_profile(run_dir),
            ),
        )
        request = GenerationRequest(
            task="review_chapter",
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
            raise ChapterServiceError(str(exc)) from exc
        atomic_write_text(chapter_dir / "review.raw.json", response.text)
        try:
            review = _parse_quality_review(root, response.text, outline, draft_text)
        except ChapterServiceError as exc:
            outline = {**outline, "review_failure_reason": str(exc)}
            outlines[index] = outline
            _save_outlines(run_dir, outlines)
            atomic_write_json(chapter_dir / "outline.json", outline)
            raise
        mark_task_accepted(run_dir, request, response, raw_path)
        if review["contract_failures"]:
            outline = transition_record(outline, "draft_failed_contract")
        elif review["quality_failures"]:
            outline = transition_record(outline, "draft_failed_quality")
        else:
            outline = transition_record(outline, "draft_passed")
            atomic_write_text(chapter_dir / "draft.final.md", draft_text)
        outline = {
            key: value
            for key, value in outline.items()
            if key != "review_failure_reason"
        }
        checks = {**checks, "quality": review, "quality_status": outline["status"]}
        outline["final_check"] = {
            "actual_length": checks.get("actual_length"),
            "status": checks.get("status"),
            "hard_pass": checks.get("hard_pass"),
            "quality_status": checks.get("quality_status"),
        }
        outline["quality_summary"] = {
            key: review.get(key)
            for key in (
                "required_outcomes",
                "forbidden_outcomes",
                "summary_like",
                "cultivation_consistent",
                "comedy_causal",
                "serious_consequences_preserved",
                "chapter_hook_concrete",
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
        }
        atomic_write_json(chapter_dir / "checks.json", checks)
        outlines[index] = outline
        _save_outlines(run_dir, outlines)
        atomic_write_json(chapter_dir / "outline.json", outline)
        return {"outline": outline, "review": review}
