"""Load model-task registrations, rules, context sources, and contracts."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import re
from typing import Any

from .io import (
    _load_registry,
    _matches_context,
    _read_json,
    _safe_relative,
    _safe_relative_list,
    _workflow_file,
)
from .models import (
    ConditionalRules,
    WorkflowContextSource,
    WorkflowLoadError,
    WorkflowTask,
)


def _conditional_rules(value: Any, *, field: str) -> tuple[ConditionalRules, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        raise WorkflowLoadError(f"工作流任务表 {field} 必须是数组")
    rules: list[ConditionalRules] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise WorkflowLoadError(f"工作流任务表 {field}[{index}] 必须是对象")
        when = item.get("when")
        if not isinstance(when, dict) or not when or not all(
            isinstance(key, str)
            and key.strip()
            and isinstance(expected, str)
            and expected.strip()
            for key, expected in when.items()
        ):
            raise WorkflowLoadError(
                f"工作流任务表 {field}[{index}].when 必须是非空字符串对象"
            )
        rules.append(
            ConditionalRules(
                when=dict(when),
                rule_paths=_safe_relative_list(
                    item.get("rules", []), field=f"{field}[{index}].rules"
                ),
            )
        )
    return tuple(rules)


def _context_sources(value: Any, *, field: str) -> tuple[WorkflowContextSource, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        raise WorkflowLoadError(f"工作流任务表 {field} 必须是数组")
    sources: list[WorkflowContextSource] = []
    for index, item in enumerate(value):
        item_field = f"{field}[{index}]"
        if not isinstance(item, dict):
            raise WorkflowLoadError(f"工作流任务表 {item_field} 必须是对象")
        artifact = item.get("artifact")
        section = item.get("section")
        format_name = item.get("format")
        when = item.get("when", {})
        if not isinstance(artifact, str) or not artifact:
            raise WorkflowLoadError(f"工作流任务表 {item_field}.artifact 无效")
        if not isinstance(section, str) or not section:
            raise WorkflowLoadError(f"工作流任务表 {item_field}.section 无效")
        if format_name not in {"text", "json"}:
            raise WorkflowLoadError(f"工作流任务表 {item_field}.format 无效")
        if not isinstance(when, dict) or not all(
            isinstance(key, str)
            and key
            and isinstance(expected, str)
            and expected
            for key, expected in when.items()
        ):
            raise WorkflowLoadError(f"工作流任务表 {item_field}.when 无效")
        sources.append(
            WorkflowContextSource(
                artifact=artifact,
                section=section,
                path=_safe_relative(item.get("path"), field=f"{item_field}.path"),
                format=format_name,
                when=dict(when),
            )
        )
    return tuple(sources)


def load_workflow_task(root: Path, task_id: str) -> WorkflowTask:
    registry = _load_registry(root)
    tasks = registry["tasks"]
    definition = tasks.get(task_id)
    if not isinstance(definition, dict):
        raise WorkflowLoadError(f"工作流任务表未定义任务：{task_id}")
    prompt_path = _safe_relative(definition.get("prompt"), field=f"{task_id}.prompt")
    rules = _safe_relative_list(definition.get("rules", []), field=f"{task_id}.rules")
    contracts = _safe_relative_list(
        definition.get("contracts", []), field=f"{task_id}.contracts"
    )
    kind = definition.get("kind")
    if kind != "model":
        raise WorkflowLoadError(f"工作流模型任务 {task_id}.kind 必须是 model")
    from .flow import load_workflow_flow, load_workflow_step

    flow = load_workflow_flow(root)
    step = load_workflow_step(root, task_id, flow=flow)
    if step.kind != "model":
        raise WorkflowLoadError(f"流程步骤 {task_id}.kind 必须是 model")
    task = WorkflowTask(
        task_id=task_id,
        kind=kind,
        prompt_path=prompt_path,
        rule_paths=rules,
        contract_paths=contracts,
        conditional_rules=_conditional_rules(
            definition.get("conditional_rules"), field=f"{task_id}.conditional_rules"
        ),
        context_sources=_context_sources(
            definition.get("context_sources"), field=f"{task_id}.context_sources"
        ),
        requires=step.requires,
        produces=step.produces,
    )
    return task


def resolved_rule_paths(
    root: Path, task_id: str, *, rule_context: dict[str, str] | None = None
) -> tuple[Path, ...]:
    """Return the base and conditionally activated rule files for one task."""

    task = load_workflow_task(root, task_id)
    paths = list(task.rule_paths)
    for conditional in task.conditional_rules:
        if _matches_context(conditional.when, rule_context):
            paths.extend(conditional.rule_paths)
    return tuple(paths)


def load_task_context_sources(
    root: Path, task_id: str, *, rule_context: dict[str, str] | None = None
) -> tuple[WorkflowContextSource, ...]:
    """Return run-relative context files selected by the task registry."""

    task = load_workflow_task(root, task_id)
    return tuple(
        source
        for source in task.context_sources
        if not source.when or _matches_context(source.when, rule_context)
    )


def load_task_contracts(root: Path, task_id: str) -> tuple[dict[str, Any], ...]:
    """Load the structured contracts selected by a registered model task."""

    task = load_workflow_task(root, task_id)
    contracts: list[dict[str, Any]] = []
    for relative in task.contract_paths:
        path = _workflow_file(root, relative)
        contract = _read_json(path)
        if not isinstance(contract, dict):
            raise WorkflowLoadError(f"工作流契约必须是对象：{path}")
        supported = contract.get("task_id")
        supported_many = contract.get("task_ids")
        accepted = supported == task_id or (
            isinstance(supported_many, list) and task_id in supported_many
        )
        if not accepted:
            raise WorkflowLoadError(
                f"工作流契约 {path} 不适用于任务 {task_id}"
            )
        output = contract.get("output")
        if not isinstance(output, dict) or not isinstance(
            output.get("model_instruction"), str
        ):
            raise WorkflowLoadError(f"工作流契约缺少 output.model_instruction：{path}")
        contracts.append(contract)
    return tuple(contracts)


def load_task_contract(root: Path, task_id: str) -> dict[str, Any]:
    """Load the one output contract for a model task."""

    contracts = load_task_contracts(root, task_id)
    if len(contracts) != 1:
        raise WorkflowLoadError(f"任务 {task_id} 必须恰好关联一个输出契约")
    return contracts[0]


_PLACEHOLDER = re.compile(r"^\{\{([A-Za-z_][A-Za-z0-9_]*)\}\}$")
_INLINE_PLACEHOLDER = re.compile(r"\{\{([A-Za-z_][A-Za-z0-9_]*)\}\}")


def render_contract_template(
    root: Path,
    task_id: str,
    values: dict[str, Any],
    *,
    template_key: str = "output_template",
) -> Any:
    """Resolve a task-contract template without embedding model fields in code."""

    contract = load_task_contract(root, task_id)
    if template_key not in contract:
        raise WorkflowLoadError(f"任务 {task_id} 的契约缺少 {template_key}")

    def render(value: Any) -> Any:
        if isinstance(value, str):
            whole = _PLACEHOLDER.match(value)
            if whole:
                name = whole.group(1)
                if name not in values:
                    raise WorkflowLoadError(
                        f"任务 {task_id} 的契约模板缺少变量：{name}"
                    )
                return deepcopy(values[name])

            def replace(match: re.Match[str]) -> str:
                name = match.group(1)
                if name not in values:
                    raise WorkflowLoadError(
                        f"任务 {task_id} 的契约模板缺少变量：{name}"
                    )
                return str(values[name])

            return _INLINE_PLACEHOLDER.sub(replace, value)
        if isinstance(value, list):
            return [render(item) for item in value]
        if isinstance(value, dict):
            return {key: render(item) for key, item in value.items()}
        return value

    return render(contract[template_key])
