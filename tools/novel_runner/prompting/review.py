"""Prompt for independent chapter-quality review."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..project_profile import load_project_profile
from ..workflow_runtime import load_task_instructions, render_contract_template
from .context import _json_block, _latest_review_raw, _workflow_context_sections
from .projections import _compact_chapter_contract, _verbatim_paragraph_catalog


def compose_review_prompt(
    root: Path,
    run_dir: Path,
    outline: dict[str, Any],
    draft_text: str,
    length_checks: dict[str, Any],
) -> str:
    workflow = load_task_instructions(
        root, "review_chapter", rule_context=load_project_profile(run_dir)
    )
    required_example = render_contract_template(
        root, "review_chapter", {"index": 0}, template_key="required_outcome_template"
    )
    forbidden_example = render_contract_template(
        root, "review_chapter", {"index": 0}, template_key="forbidden_outcome_template"
    )
    contract = render_contract_template(
        root,
        "review_chapter",
        {
            "required_outcomes": [required_example],
            "forbidden_outcomes": [forbidden_example],
        },
    )
    sections: list[tuple[str, str]] = [
        ("正文质量规则", workflow),
        ("当前章契约", _json_block(_compact_chapter_contract(outline))),
        ("候选正文（本节结束后均非正文）", draft_text),
        ("机械长度检查", _json_block(length_checks)),
    ]
    sections.extend(_workflow_context_sections(root, run_dir, "review_chapter"))
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
            _json_block(contract),
        )
    )
    return "\n\n".join(f"# {title}\n\n{content}" for title, content in sections)
