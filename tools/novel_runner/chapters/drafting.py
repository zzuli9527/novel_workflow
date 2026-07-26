"""Generate and repair chapter drafts."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..api_runtime import invoke_provider, mark_task_accepted
from ..master_plan import MasterPlanError, require_approved_master_plan
from ..outline_validation import OutlineValidationError, ensure_outline_valid
from ..project_profile import load_project_profile
from ..prompting import compose_draft_prompt, compose_repair_prompt
from ..provider import GenerationRequest, ProviderError, TextProvider
from ..state_machine import StateTransitionError, ensure_chapter_can_start, transition_record
from ..storage import atomic_write_json, atomic_write_text, read_json, resolve_run_dir, run_lock
from ..wordcount import DraftParseError, check_drafts
from ..workflow_runtime import workflow_source_manifest
from .common import (
    ChapterServiceError,
    _find_outline,
    _length_policy,
    _load_context,
    _next_draft_version,
    _pause_run,
    _read_current_draft,
    _relative_posix,
    _save_outlines,
)


def draft_chapter(
    root: Path, run_id: str, chapter_number: int, provider: TextProvider
) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        return _draft_chapter_unlocked(root, run_id, chapter_number, provider)


def _draft_chapter_unlocked(
    root: Path,
    run_id: str,
    chapter_number: int,
    provider: TextProvider,
    *,
    prompt_override: str | None = None,
    task: str = "draft_chapter",
    retry_kind: str | None = None,
) -> dict[str, Any]:
    try:
        require_approved_master_plan(root, run_id)
    except MasterPlanError as exc:
        raise ChapterServiceError(str(exc)) from exc
    run_dir, run_config, outlines = _load_context(root, run_id)
    index, outline = _find_outline(outlines, chapter_number)
    try:
        ensure_outline_valid(outline, run_config)
    except OutlineValidationError as exc:
        raise ChapterServiceError(f"第 {chapter_number} 章章纲无效：{exc}") from exc
    ensure_chapter_can_start(chapter_number, run_config["last_committed_chapter"])

    current_status = outline.get("status")
    if current_status not in {
        "outline_ready",
        "draft_failed_provider",
        "draft_failed_length",
        "draft_failed_contract",
        "draft_failed_quality",
    }:
        raise ChapterServiceError(
            f"第 {chapter_number} 章当前状态 {current_status} 不能生成正文"
        )

    try:
        outline = transition_record(outline, "drafting")
    except StateTransitionError as exc:
        raise ChapterServiceError(str(exc)) from exc
    if retry_kind is not None:
        retry_counts = outline.get("retry_counts", {})
        if not isinstance(retry_counts, dict):
            retry_counts = {}
        outline = {
            **outline,
            "retry_counts": {
                **retry_counts,
                retry_kind: int(retry_counts.get(retry_kind, 0)) + 1,
            },
        }
    outlines[index] = outline
    _save_outlines(run_dir, outlines)

    chapter_dir = run_dir / f"chapters/{chapter_number:04d}"
    chapter_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_json(chapter_dir / "outline.json", outline)
    version = _next_draft_version(chapter_dir)
    prompt = prompt_override or compose_draft_prompt(
        root, run_dir, run_config, outline, task_id=task
    )
    prompt_path = chapter_dir / f"draft.prompt.v{version}.md"
    atomic_write_text(prompt_path, prompt)
    atomic_write_text(chapter_dir / "draft.prompt.md", prompt)
    atomic_write_json(
        chapter_dir / f"draft.workflow.v{version}.json",
        workflow_source_manifest(
            root, task, rule_context=load_project_profile(run_dir)
        ),
    )

    draft_path = chapter_dir / f"draft.v{version}.md"
    request = GenerationRequest(
        task=task,
        prompt=prompt,
        metadata={"run_id": run_id, "chapter": chapter_number},
    )
    try:
        response = invoke_provider(
            run_dir,
            provider,
            request,
            prompt_path=prompt_path,
            output_path=draft_path,
            chapter=chapter_number,
        )
    except ProviderError as exc:
        outline = transition_record(outline, "draft_failed_provider")
        outlines[index] = outline
        _save_outlines(run_dir, outlines)
        atomic_write_json(chapter_dir / "outline.json", outline)
        raise ChapterServiceError(str(exc)) from exc
    outline = transition_record(outline, "draft_generated")
    try:
        report = check_drafts(response.text, _length_policy(run_config))
        if len(report.chapters) != 1 or report.chapters[0].number != chapter_number:
            raise DraftParseError("响应必须只包含当前章节")
    except DraftParseError as exc:
        outline = transition_record(outline, "draft_failed_contract")
        check_data = {
            "chapter": chapter_number,
            "status": "draft_failed_contract",
            "can_update_state": False,
            "error": str(exc),
        }
    else:
        check = report.chapters[0]
        if not check.hard_pass:
            outline = transition_record(outline, "draft_failed_length")
        elif check.requires_review:
            outline = transition_record(outline, "draft_failed_quality")
        else:
            outline = transition_record(outline, "draft_quality_pending")
            atomic_write_text(chapter_dir / "draft.candidate.md", response.text)
            mark_task_accepted(run_dir, request, response, draft_path)
        check_data = {
            **check.to_dict(),
            "chapter": chapter_number,
            "draft_version": version,
            "draft_path": _relative_posix(draft_path, run_dir),
        }

    atomic_write_json(chapter_dir / "checks.json", check_data)
    outline = {
        **outline,
        "actual_length": check_data.get("actual_length", 0),
        "draft_path": _relative_posix(draft_path, run_dir),
        "checks": {"length": check_data.get("status")},
    }
    if version == 1:
        outline["initial_draft"] = {
            "actual_length": check_data.get("actual_length"),
            "status": check_data.get("status"),
            "passed": check_data.get("status") == "passed",
        }
    outlines[index] = outline
    _save_outlines(run_dir, outlines)
    atomic_write_json(chapter_dir / "outline.json", outline)
    return {"outline": outline, "check": check_data}


def repair_chapter(
    root: Path, run_id: str, chapter_number: int, provider: TextProvider
) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        run_dir, run_config, outlines = _load_context(root, run_id)
        _, outline = _find_outline(outlines, chapter_number)
        status = outline.get("status")
        modes = {
            "draft_failed_provider": ("provider_retry", "transport"),
            "draft_failed_contract": ("rewrite_contract", "content"),
            "draft_failed_quality": ("rewrite_quality", "content"),
        }
        checks_path = run_dir / f"chapters/{chapter_number:04d}/checks.json"
        checks = read_json(checks_path) if checks_path.exists() else {}
        if status == "draft_failed_length":
            actual = checks.get("actual_length", 0)
            expand_from = run_config["policies"]["length"]["expand_from"]
            review_over = run_config["policies"]["length"]["review_over"]
            if isinstance(actual, int) and actual > review_over:
                mode = "targeted_compression"
            elif isinstance(actual, int) and actual >= expand_from:
                mode = "targeted_expansion"
            else:
                mode = "rewrite_short"
            retry_kind = "content"
        elif status in modes:
            mode, retry_kind = modes[status]
        else:
            raise ChapterServiceError(
                f"第 {chapter_number} 章当前状态 {status} 不能执行修复"
            )

        retry_counts = outline.get("retry_counts", {})
        if not isinstance(retry_counts, dict):
            retry_counts = {}
        current_count = retry_counts.get(retry_kind, 0)
        if not isinstance(current_count, int):
            current_count = 0
        max_retries = run_config["policies"]["retry"][retry_kind]
        if current_count >= max_retries:
            reason = (
                f"第 {chapter_number} 章 {retry_kind} 重试已达到上限 {max_retries}"
            )
            _pause_run(run_dir, run_config, reason)
            raise ChapterServiceError(reason)

        current_draft = _read_current_draft(run_dir, outline)
        prompt = compose_repair_prompt(
            root,
            run_dir,
            run_config,
            outline,
            current_draft,
            checks,
            mode,
        )
        return _draft_chapter_unlocked(
            root,
            run_id,
            chapter_number,
            provider,
            prompt_override=prompt,
            task="repair_chapter",
            retry_kind=retry_kind,
        )
