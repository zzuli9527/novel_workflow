"""Prompt for compressed batch-ledger generation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..project_profile import load_project_profile
from ..workflow_runtime import load_task_instructions, render_contract_template
from .context import _json_block, _latest_ledger, _workflow_context_sections


def compose_ledger_prompt(
    root: Path,
    run_dir: Path,
    start_chapter: int,
    end_chapter: int,
    snapshot: dict[str, Any],
    events: list[dict[str, Any]],
    item_limit: int,
) -> str:
    workflow = load_task_instructions(
        root, "build_ledger", rule_context=load_project_profile(run_dir)
    )
    previous_ledger = _latest_ledger(run_dir)
    snapshot_context = {
        "after_chapter": snapshot.get("after_chapter"),
        "next_chapter_inputs": snapshot.get("next_chapter_inputs", []),
        "deviations": snapshot.get("deviations", []),
    }
    contract = render_contract_template(root, "build_ledger", {})
    sections: list[tuple[str, str]] = [
        ("批次账本工作流", workflow),
        ("批次范围", f"第 {start_chapter}～{end_chapter} 章"),
        ("上一批账本", _json_block(previous_ledger)),
        ("批次结束交接状态", _json_block(snapshot_context)),
        ("本批状态事件", _json_block(events)),
    ]
    sections.extend(_workflow_context_sections(root, run_dir, "build_ledger"))
    sections.extend([
        ("本次账本上限", f"must_read_next 最多 {item_limit} 条。"),
        (
            "机器输出契约",
            _json_block(contract),
        ),
    ])
    return "\n\n".join(f"# {title}\n\n{content}" for title, content in sections)
