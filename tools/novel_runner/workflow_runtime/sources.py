"""Compose task instructions and hash every workflow source used."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from typing import Any

from .io import _load_registry, _read_text, _safe_relative, _workflow_file
from .models import REGISTRY_PATH, WORKFLOW_VERSION, WorkflowLoadError
from .registry import (
    load_task_contracts,
    load_workflow_task,
    resolved_rule_paths,
)


def load_task_instructions(
    root: Path, task_id: str, *, rule_context: dict[str, str] | None = None
) -> str:
    """Compose one model task from its registered prompt, rules and contract."""

    task = load_workflow_task(root, task_id)
    prompt = _read_text(_workflow_file(root, task.prompt_path)).strip()
    rule_texts = [
        _read_text(_workflow_file(root, item)).strip()
        for item in resolved_rule_paths(root, task_id, rule_context=rule_context)
    ]
    contract_texts = [
        str(contract["output"]["model_instruction"]).strip()
        for contract in load_task_contracts(root, task_id)
    ]
    sections = [prompt]
    if rule_texts:
        sections.append("# 任务规则\n\n" + "\n\n".join(rule_texts))
    if contract_texts:
        sections.append("# 输出契约\n\n" + "\n\n".join(contract_texts))
    return "\n\n".join(section for section in sections if section)


def load_workflow_rule(root: Path, relative: str) -> str:
    """Read a named reusable rule from ``workflow/规则`` only."""

    path = _safe_relative(relative, field="rule")
    if not path.parts or path.parts[0] != "规则":
        raise WorkflowLoadError("可复用规则必须位于 workflow/规则/")
    return _read_text(_workflow_file(root, path)).strip()


def workflow_source_manifest(
    root: Path, task_id: str, *, rule_context: dict[str, str] | None = None
) -> dict[str, Any]:
    """Return hashes of the workflow sources that formed a task prompt."""

    task = load_workflow_task(root, task_id)
    registry = _load_registry(root)
    registry_relative = REGISTRY_PATH.relative_to("workflow")
    flow_relative = _safe_relative(registry["flow"], field="flow")
    paths = (
        registry_relative,
        flow_relative,
        task.prompt_path,
        *resolved_rule_paths(root, task_id, rule_context=rule_context),
        *task.contract_paths,
    )
    sources = []
    for relative in paths:
        text = _read_text(_workflow_file(root, relative))
        sources.append(
            {
                "path": (Path("workflow") / relative).as_posix(),
                "sha256": sha256(text.encode("utf-8")).hexdigest(),
            }
        )
    return {
        "workflow_version": WORKFLOW_VERSION,
        "task_id": task_id,
        "sources": sources,
    }
