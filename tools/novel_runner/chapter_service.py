"""单章生成、状态提取和提交的第一版垂直闭环。"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from typing import Any

from .api_runtime import invoke_provider, mark_task_accepted
from .config import validate_run_directory
from .master_plan import MasterPlanError, require_approved_master_plan
from .prompt_composer import (
    compose_draft_prompt,
    compose_repair_prompt,
    compose_review_prompt,
    compose_state_prompt,
)
from .outline_validation import OutlineValidationError, ensure_outline_valid
from .provider import GenerationRequest, ProviderError, TextProvider
from .revision import RevisionError, resume_revision
from .state_machine import (
    StateTransitionError,
    ensure_chapter_can_start,
    transition_record,
)
from .state_store import (
    StateStoreError,
    append_event_once,
    build_snapshot,
    ensure_event_compatible,
)
from .file_storage import (
    events_path,
    prepare_event,
    read_current_snapshot,
    record_runtime_event,
    transaction_path,
    write_snapshot,
)
from .storage import (
    StorageError,
    atomic_write_json,
    atomic_write_text,
    read_json,
    resolve_run_dir,
    run_lock,
)
from .wordcount import DraftParseError, LengthPolicy, check_drafts
from .structured_state import StructuredStateError, validate_structured_event


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


class ChapterServiceError(RuntimeError):
    """章节垂直闭环执行失败。"""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _log_runtime_event(run_dir: Path, action: str, **data: Any) -> None:
    run_config = read_json(run_dir / "run.json")
    record_runtime_event(
        run_dir,
        run_config,
        {"timestamp": _utc_now(), "action": action, **data},
    )


def _relative_posix(path: Path, run_dir: Path) -> str:
    return path.relative_to(run_dir).as_posix()


def _load_context(root: Path, run_id: str) -> tuple[Path, dict[str, Any], list[dict[str, Any]]]:
    report = validate_run_directory(root, run_id)
    if not report.valid:
        details = "; ".join(f"{issue.path}: {issue.message}" for issue in report.issues)
        raise ChapterServiceError(f"运行配置无效：{details}")
    run_dir = resolve_run_dir(root, run_id)
    run_config = read_json(run_dir / "run.json")
    outlines = read_json(run_dir / "planning/chapter-outlines.json")
    return run_dir, run_config, outlines


def _find_outline(
    outlines: list[dict[str, Any]], chapter_number: int
) -> tuple[int, dict[str, Any]]:
    matches = [
        (index, outline)
        for index, outline in enumerate(outlines)
        if outline.get("number") == chapter_number
    ]
    if not matches:
        raise ChapterServiceError(f"未找到第 {chapter_number} 章细纲")
    if len(matches) > 1:
        raise ChapterServiceError(f"第 {chapter_number} 章细纲重复")
    return matches[0]


def _save_outlines(run_dir: Path, outlines: list[dict[str, Any]]) -> None:
    atomic_write_json(run_dir / "planning/chapter-outlines.json", outlines)


def _length_policy(run_config: dict[str, Any]) -> LengthPolicy:
    data = run_config["policies"]["length"]
    return LengthPolicy(
        target_min=data["target_min"],
        target_max=data["target_max"],
        expand_from=data["expand_from"],
        review_over=data["review_over"],
    )


def _next_draft_version(chapter_dir: Path) -> int:
    versions: list[int] = []
    for path in chapter_dir.glob("draft.v*.md"):
        middle = path.stem.removeprefix("draft.v")
        if middle.isdigit():
            versions.append(int(middle))
    return max(versions, default=0) + 1


def _next_state_version(chapter_dir: Path) -> int:
    versions: list[int] = []
    for path in chapter_dir.glob("state.raw.v*.json"):
        middle = path.name.removeprefix("state.raw.v").removesuffix(".json")
        if middle.isdigit():
            versions.append(int(middle))
    return max(versions, default=0) + 1


def _next_review_version(chapter_dir: Path) -> int:
    versions: list[int] = []
    for path in chapter_dir.glob("review.raw.v*.json"):
        middle = path.name.removeprefix("review.raw.v").removesuffix(".json")
        if middle.isdigit():
            versions.append(int(middle))
    return max(versions, default=0) + 1


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
    prompt = prompt_override or compose_draft_prompt(root, run_dir, run_config, outline)
    prompt_path = chapter_dir / f"draft.prompt.v{version}.md"
    atomic_write_text(prompt_path, prompt)
    atomic_write_text(chapter_dir / "draft.prompt.md", prompt)

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


def _pause_run(run_dir: Path, run_config: dict[str, Any], reason: str) -> None:
    atomic_write_json(
        run_dir / "run.json",
        {
            **run_config,
            "status": "paused",
            "pause_reason": reason,
            "updated_at": _utc_now(),
        },
    )


def _read_current_draft(run_dir: Path, outline: dict[str, Any]) -> str:
    relative = outline.get("draft_path")
    if not isinstance(relative, str) or not relative:
        return ""
    path = (run_dir / Path(relative)).resolve()
    if run_dir.resolve() not in path.parents:
        raise ChapterServiceError("草稿路径越出运行目录")
    try:
        return path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise ChapterServiceError(f"无法读取失败草稿：{exc}") from exc


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


def _normalize_evidence(value: str) -> str:
    return re.sub(r"\s+", "", value)


def _parse_quality_review(
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

    quality_flags = (
        "summary_like",
        "cultivation_consistent",
        "comedy_causal",
        "serious_consequences_preserved",
        "chapter_hook_concrete",
        "resource_continuity_consistent",
        "knowledge_states_consistent",
        "character_voices_distinct",
        "multi_line_causality_preserved",
    )
    for field in quality_flags:
        if not isinstance(data.get(field), bool):
            raise ChapterServiceError(f"质量评审 {field} 必须是布尔值")
    quality_failures: list[str] = []
    if data["summary_like"]:
        quality_failures.append("正文摘要化")
    for field in (
        "cultivation_consistent",
        "serious_consequences_preserved",
        "resource_continuity_consistent",
        "knowledge_states_consistent",
        "multi_line_causality_preserved",
    ):
        if not data[field]:
            quality_failures.append(field)
    soft_quality_warnings = [
        field
        for field in (
            "comedy_causal",
            "chapter_hook_concrete",
            "character_voices_distinct",
        )
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
            review = _parse_quality_review(response.text, outline, draft_text)
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
    except ChapterServiceError as exc:
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


def _commit_journal_path(run_dir: Path, run_config: dict[str, Any]) -> Path:
    return transaction_path(run_dir, run_config)


def _apply_commit_journal(
    run_dir: Path,
    run_config: dict[str, Any],
    outlines: list[dict[str, Any]],
    journal: dict[str, Any],
) -> dict[str, Any]:
    chapter_number = journal.get("chapter")
    event = journal.get("event")
    if not isinstance(chapter_number, int) or not isinstance(event, dict):
        raise ChapterServiceError("提交事务日志损坏")

    index, outline = _find_outline(outlines, chapter_number)
    current_status = outline.get("status")
    if current_status not in {"state_ready", "committing", "committed"}:
        raise ChapterServiceError(
            f"提交恢复要求 state_ready / committing / committed，当前为 {current_status}"
        )

    last_committed = run_config.get("last_committed_chapter")
    if last_committed not in {chapter_number - 1, chapter_number}:
        raise ChapterServiceError("运行指针与提交事务不连续")

    event_log_path = events_path(run_dir)
    chapter_dir = run_dir / f"chapters/{chapter_number:04d}"
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
        snapshot = build_snapshot(
            event, previous_snapshot, initial_state=initial_state
        )
        ensure_event_compatible(event_log_path, event)
    except (StateStoreError, StorageError) as exc:
        if current_status in {"state_ready", "committing"}:
            outline = transition_record(outline, "state_failed")
            outline = {
                **outline,
                "state_failure_kind": (
                    "content" if isinstance(exc, StateStoreError) else "format"
                ),
                "state_failure_reason": str(exc),
            }
            outlines[index] = outline
            _save_outlines(run_dir, outlines)
            atomic_write_json(chapter_dir / "outline.json", outline)
        try:
            _commit_journal_path(run_dir, run_config).unlink(missing_ok=True)
        except OSError:
            pass
        raise ChapterServiceError(str(exc)) from exc

    if current_status == "state_ready":
        outline = transition_record(outline, "committing")
        outlines[index] = outline
        _save_outlines(run_dir, outlines)

    try:
        append_event_once(event_log_path, event)
    except StateStoreError as exc:
        raise ChapterServiceError(str(exc)) from exc

    snapshot["source"] = (
        "state/events.jsonl"
        if run_config.get("storage_version") == "2.0"
        else _relative_posix(chapter_dir / "state-event.json", run_dir)
    )
    write_snapshot(run_dir, run_config, chapter_number, snapshot, event)

    run_config = {
        **{key: value for key, value in run_config.items() if key != "pause_reason"},
        "status": "running",
        "last_committed_chapter": chapter_number,
        "updated_at": _utc_now(),
    }
    atomic_write_json(run_dir / "run.json", run_config)

    if outline.get("status") == "committing":
        outline = transition_record(outline, "committed")
    outlines[index] = outline
    _save_outlines(run_dir, outlines)
    atomic_write_json(chapter_dir / "outline.json", outline)

    journal_path = _commit_journal_path(run_dir, run_config)
    try:
        journal_path.unlink(missing_ok=True)
    except OSError as exc:
        raise ChapterServiceError(f"无法清理已完成提交事务日志：{exc}") from exc
    return {"run": run_config, "outline": outline, "snapshot": snapshot}


def commit_chapter(root: Path, run_id: str, chapter_number: int) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        run_dir, run_config, outlines = _load_context(root, run_id)
        _, outline = _find_outline(outlines, chapter_number)
        ensure_chapter_can_start(chapter_number, run_config["last_committed_chapter"])
        if outline.get("status") != "state_ready":
            raise ChapterServiceError("只有 state_ready 章节可以提交")

        chapter_dir = run_dir / f"chapters/{chapter_number:04d}"
        event = read_json(chapter_dir / "state-event.json")
        event = prepare_event(run_dir, run_config, event)
        journal = {
            "journal_version": "1.0",
            "chapter": chapter_number,
            "event": event,
            "created_at": _utc_now(),
        }
        atomic_write_json(_commit_journal_path(run_dir, run_config), journal)
        return _apply_commit_journal(run_dir, run_config, outlines, journal)


def resume_run(root: Path, run_id: str) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        revision_journal = run_dir / "logs/revision-journal.json"
        if revision_journal.exists():
            try:
                manifest = resume_revision(run_dir)
            except RevisionError as exc:
                raise ChapterServiceError(str(exc)) from exc
            _log_runtime_event(
                run_dir,
                "revision_recovered",
                chapter=manifest.get("invalidated_from_chapter"),
                revision_id=manifest.get("revision_id"),
            )
            return {"action": "revision_recovered", "revision": manifest}
        run_dir, run_config, outlines = _load_context(root, run_id)
        journal_path = _commit_journal_path(run_dir, run_config)
        if not journal_path.exists():
            recovered: list[int] = []
            recovered_states: list[int] = []
            for index, outline in enumerate(outlines):
                status = outline.get("status")
                if status == "drafting":
                    outlines[index] = transition_record(outline, "draft_failed_provider")
                    chapter = outline.get("number")
                    if isinstance(chapter, int):
                        recovered.append(chapter)
                elif status == "state_extracting":
                    recovered_outline = transition_record(outline, "state_failed")
                    outlines[index] = {
                        **recovered_outline,
                        "state_failure_kind": "transport",
                    }
                    chapter = outline.get("number")
                    if isinstance(chapter, int):
                        recovered_states.append(chapter)
                else:
                    continue
                if isinstance(chapter, int):
                    chapter_dir = run_dir / f"chapters/{chapter:04d}"
                    if chapter_dir.exists():
                        atomic_write_json(chapter_dir / "outline.json", outlines[index])
            if recovered or recovered_states:
                _save_outlines(run_dir, outlines)
                _log_runtime_event(
                    run_dir,
                    "incomplete_tasks_recovered",
                    chapters=sorted([*recovered, *recovered_states]),
                )
                return {
                    "action": "incomplete_tasks_recovered",
                    "draft_chapters": recovered,
                    "state_chapters": recovered_states,
                    "last_committed_chapter": run_config.get("last_committed_chapter"),
                }
            return {
                "action": "none",
                "last_committed_chapter": run_config.get("last_committed_chapter"),
            }
        journal = read_json(journal_path)
        result = _apply_commit_journal(run_dir, run_config, outlines, journal)
        _log_runtime_event(
            run_dir,
            "commit_recovered",
            chapter=journal.get("chapter"),
        )
        return {"action": "commit_recovered", **result}


def get_run_status(root: Path, run_id: str) -> dict[str, Any]:
    run_dir, run_config, outlines = _load_context(root, run_id)
    status_counts: dict[str, int] = {}
    for outline in outlines:
        status = str(outline.get("status", "missing"))
        status_counts[status] = status_counts.get(status, 0) + 1
    return {
        "run_id": run_id,
        "status": run_config.get("status"),
        "last_committed_chapter": run_config.get("last_committed_chapter"),
        "current_story_unit": run_config.get("current_story_unit"),
        "current_batch": run_config.get("current_batch"),
        "chapter_status_counts": status_counts,
        "commit_recovery_pending": _commit_journal_path(run_dir, run_config).exists(),
        "revision_recovery_pending": (
            run_dir / "logs/revision-journal.json"
        ).exists(),
    }
