"""Load executable steps, routes, retry policies, and terminal actions."""

from __future__ import annotations

from typing import Any, Mapping

from .io import _load_registry, _read_json, _safe_relative, _string_list, _workflow_file
from .models import WORKFLOW_VERSION, WorkflowLoadError, WorkflowStep


_STEP_KINDS = frozenset({"model", "tool_gate", "human_gate"})


def _parse_step(step: Any, *, field: str) -> WorkflowStep:
    if not isinstance(step, dict):
        raise WorkflowLoadError(f"工作流流程定义 {field} 必须是对象")
    step_id = step.get("id")
    if not isinstance(step_id, str) or not step_id.strip():
        raise WorkflowLoadError(f"工作流流程定义 {field}.id 必须是非空字符串")
    kind = step.get("kind")
    if kind not in _STEP_KINDS:
        raise WorkflowLoadError(f"工作流流程定义 {step_id}.kind 无效")
    scope = step.get("scope")
    if not isinstance(scope, str) or not scope.strip():
        raise WorkflowLoadError(f"工作流流程定义 {step_id}.scope 必须是非空字符串")
    execution = step.get("execution", "automatic")
    if execution not in {"automatic", "manual"}:
        raise WorkflowLoadError(
            f"工作流流程定义 {step_id}.execution 必须是 automatic 或 manual"
        )
    requires = _string_list(step.get("requires"), field=f"{step_id}.requires")
    optional_inputs = _string_list(
        step.get("optional_inputs", []), field=f"{step_id}.optional_inputs"
    )
    produces = _string_list(step.get("produces"), field=f"{step_id}.produces")
    success_statuses = _string_list(
        step.get("success_statuses", []), field=f"{step_id}.success_statuses"
    )
    overlap = set(requires) & set(optional_inputs)
    if overlap:
        raise WorkflowLoadError(
            f"工作流流程定义 {step_id} 的必需与可选输入重复：{sorted(overlap)}"
        )
    return WorkflowStep(
        step_id=step_id,
        kind=kind,
        scope=scope,
        requires=requires,
        optional_inputs=optional_inputs,
        produces=produces,
        success_statuses=success_statuses,
        execution=execution,
    )


def _validate_retry_policies(flow: dict[str, Any]) -> None:
    policies = flow.get("chapter_retry_policies")
    if not isinstance(policies, list) or not policies:
        raise WorkflowLoadError("工作流流程定义缺少 chapter_retry_policies 数组")
    policy_ids: set[str] = set()
    for index, policy in enumerate(policies):
        field = f"chapter_retry_policies[{index}]"
        if not isinstance(policy, dict):
            raise WorkflowLoadError(f"工作流流程定义 {field} 必须是对象")
        policy_id = policy.get("id")
        if not isinstance(policy_id, str) or not policy_id.strip():
            raise WorkflowLoadError(f"工作流流程定义 {field}.id 必须是非空字符串")
        if policy_id in policy_ids:
            raise WorkflowLoadError(f"工作流流程定义重复式重试策略：{policy_id}")
        policy_ids.add(policy_id)
        when = policy.get("when")
        if not isinstance(when, dict) or not isinstance(when.get("status"), str):
            raise WorkflowLoadError(f"工作流流程定义 {field}.when 必须声明 status")
        non_empty_field = when.get("non_empty_field")
        if non_empty_field is not None and (
            not isinstance(non_empty_field, str) or not non_empty_field
        ):
            raise WorkflowLoadError(
                f"工作流流程定义 {field}.when.non_empty_field 无效"
            )
        value_field = when.get("value_field")
        if value_field is not None:
            values = when.get("allowed_values")
            if not isinstance(value_field, str) or not value_field or not isinstance(
                values, list
            ) or not all(isinstance(item, str) and item for item in values):
                raise WorkflowLoadError(
                    f"工作流流程定义 {field}.when.value_field/allowed_values 无效"
                )
        has_fixed_counter = isinstance(policy.get("counter"), str) and bool(
            policy.get("counter")
        )
        has_template_counter = isinstance(
            policy.get("counter_template"), str
        ) and "{value}" in str(policy.get("counter_template"))
        has_fixed_budget = isinstance(policy.get("budget"), str) and bool(
            policy.get("budget")
        )
        has_dynamic_budget = policy.get("budget_from_value") is True
        on_exhausted = policy.get("on_exhausted")
        if not (has_fixed_counter or has_template_counter) or not (
            has_fixed_budget or has_dynamic_budget
        ):
            raise WorkflowLoadError(f"工作流流程定义 {field} 缺少重试计数或预算声明")
        if not isinstance(on_exhausted, str) or not on_exhausted:
            raise WorkflowLoadError(f"工作流流程定义 {field} 缺少 on_exhausted")


def _validate_unit_lifecycle(flow: dict[str, Any], step_ids: set[str]) -> None:
    lifecycle = flow.get("unit_lifecycle")
    if not isinstance(lifecycle, dict):
        raise WorkflowLoadError("工作流流程定义缺少 unit_lifecycle 对象")
    for key in ("missing_batch_outlines", "completed_batch"):
        step_id = lifecycle.get(key)
        if not isinstance(step_id, str) or step_id not in step_ids:
            raise WorkflowLoadError(f"工作流单元流程 {key} 未引用已声明步骤")
    for key in ("after_unit", "release"):
        values = lifecycle.get(key)
        if not isinstance(values, list) or not values or not all(
            isinstance(item, str) and item in step_ids for item in values
        ):
            raise WorkflowLoadError(f"工作流单元流程 {key} 必须引用已声明步骤数组")


def load_workflow_flow(root: Path) -> dict[str, Any]:
    """Load and validate the machine-readable, executable production flow."""

    registry = _load_registry(root)
    flow_path = _workflow_file(root, _safe_relative(registry["flow"], field="flow"))
    flow = _read_json(flow_path)
    if not isinstance(flow, dict) or flow.get("workflow_version") != WORKFLOW_VERSION:
        raise WorkflowLoadError("工作流流程定义缺失或版本不一致")
    steps = flow.get("steps")
    if not isinstance(steps, list) or not steps:
        raise WorkflowLoadError("工作流流程定义缺少 steps 数组")
    parsed_steps = [_parse_step(step, field=f"steps[{index}]") for index, step in enumerate(steps)]
    step_ids = [step.step_id for step in parsed_steps]
    if len(step_ids) != len(set(step_ids)):
        raise WorkflowLoadError("工作流流程定义包含重复步骤 ID")
    task_ids = set(registry["tasks"])
    model_step_ids = {step.step_id for step in parsed_steps if step.kind == "model"}
    if model_step_ids != task_ids:
        raise WorkflowLoadError("流程模型步骤与任务表不一致")
    for task_id, definition in registry["tasks"].items():
        if not isinstance(definition, dict):
            raise WorkflowLoadError(f"工作流任务表 {task_id} 必须是对象")
        duplicate_control_fields = {"requires", "optional_inputs", "produces", "on_failure"} & set(definition)
        if duplicate_control_fields:
            raise WorkflowLoadError(
                f"工作流任务表 {task_id} 不能重复定义编排字段：{sorted(duplicate_control_fields)}"
            )
    terminal_statuses = flow.get("chapter_terminal_statuses")
    if not isinstance(terminal_statuses, list) or not terminal_statuses or not all(
        isinstance(status, str) and status for status in terminal_statuses
    ):
        raise WorkflowLoadError("工作流流程定义缺少 chapter_terminal_statuses")
    max_steps = flow.get("chapter_max_steps")
    if not isinstance(max_steps, int) or isinstance(max_steps, bool) or max_steps <= 0:
        raise WorkflowLoadError("工作流流程定义 chapter_max_steps 必须是正整数")
    routes = flow.get("chapter_routes")
    if not isinstance(routes, dict) or not routes or not all(
        isinstance(status, str)
        and status
        and isinstance(route, str)
        and route in step_ids
        for status, route in routes.items()
    ):
        raise WorkflowLoadError("流程章节路由缺失或引用了未知步骤")
    terminal_routes = flow.get("terminal_routes")
    if not isinstance(terminal_routes, dict) or not terminal_routes or not all(
        isinstance(event, str)
        and event
        and action in {"pause", "fail"}
        for event, action in terminal_routes.items()
    ):
        raise WorkflowLoadError("工作流终止路由必须映射到 pause 或 fail")
    _validate_retry_policies(flow)
    for policy in flow["chapter_retry_policies"]:
        if policy["on_exhausted"] not in terminal_routes:
            raise WorkflowLoadError(
                f"重试策略 {policy['id']} 的终止事件未在 terminal_routes 中声明"
            )
    _validate_unit_lifecycle(flow, set(step_ids))
    return flow


def load_workflow_step(
    root: Path, step_id: str, *, flow: dict[str, Any] | None = None
) -> WorkflowStep:
    """Return one validated step from the authoritative flow definition."""

    selected_flow = flow if flow is not None else load_workflow_flow(root)
    steps = selected_flow.get("steps", [])
    for index, step in enumerate(steps):
        parsed = _parse_step(step, field=f"steps[{index}]")
        if parsed.step_id == step_id:
            return parsed
    raise WorkflowLoadError(f"工作流流程定义未声明步骤：{step_id}")


def resolve_chapter_step(root: Path, status: str) -> WorkflowStep | None:
    """Resolve the next chapter step solely from the workflow declaration."""

    flow = load_workflow_flow(root)
    if status in flow["chapter_terminal_statuses"]:
        return None
    route = flow["chapter_routes"].get(status)
    if not isinstance(route, str):
        raise WorkflowLoadError(f"章节状态未定义工作流路由：{status}")
    return load_workflow_step(root, route, flow=flow)


def ensure_step_inputs(step: WorkflowStep, available_artifacts: set[str]) -> None:
    """Reject scheduling a step before its declared required artifacts exist."""

    missing = sorted(set(step.requires) - available_artifacts)
    if missing:
        raise WorkflowLoadError(
            f"工作流步骤 {step.step_id} 缺少必需产物：{', '.join(missing)}"
        )


def ensure_step_outputs(step: WorkflowStep, available_artifacts: set[str]) -> None:
    """Reject a successful step that did not materialize its declared outputs."""

    missing = sorted(set(step.produces) - available_artifacts)
    if missing:
        raise WorkflowLoadError(
            f"工作流步骤 {step.step_id} 未产生声明产物：{', '.join(missing)}"
        )


def chapter_retry_available(
    flow: Mapping[str, Any],
    outline: Mapping[str, Any],
    retry_limits: Mapping[str, Any],
) -> bool:
    """Evaluate the workflow-declared retry policy for one failed chapter state."""

    status = outline.get("status")
    retry_counts = outline.get("retry_counts")
    counts = retry_counts if isinstance(retry_counts, Mapping) else {}
    for policy in flow.get("chapter_retry_policies", []):
        if not isinstance(policy, Mapping):
            continue
        when = policy.get("when")
        if not isinstance(when, Mapping) or when.get("status") != status:
            continue
        non_empty_field = when.get("non_empty_field")
        if isinstance(non_empty_field, str) and not outline.get(non_empty_field):
            continue
        value: str | None = None
        value_field = when.get("value_field")
        if isinstance(value_field, str):
            raw_value = outline.get(value_field)
            allowed_values = when.get("allowed_values")
            if not isinstance(raw_value, str) or not isinstance(allowed_values, list):
                continue
            if raw_value not in allowed_values:
                continue
            value = raw_value
        counter = policy.get("counter")
        if not isinstance(counter, str) or not counter:
            template = policy.get("counter_template")
            if not isinstance(template, str) or value is None:
                continue
            counter = template.format(value=value)
        budget = policy.get("budget")
        if policy.get("budget_from_value") is True:
            budget = value
        if not isinstance(budget, str) or not budget:
            continue
        current = counts.get(counter, 0)
        maximum = retry_limits.get(budget)
        if not isinstance(current, int) or isinstance(current, bool):
            current = 0
        if not isinstance(maximum, int) or isinstance(maximum, bool):
            raise WorkflowLoadError(f"运行重试预算缺少 {budget}")
        return current < maximum
    return False


def chapter_retry_terminal_action(
    flow: Mapping[str, Any], outline: Mapping[str, Any]
) -> str | None:
    """Resolve the terminal action for the retry policy matching this state."""

    status = outline.get("status")
    for policy in flow.get("chapter_retry_policies", []):
        if not isinstance(policy, Mapping):
            continue
        when = policy.get("when")
        if not isinstance(when, Mapping) or when.get("status") != status:
            continue
        non_empty_field = when.get("non_empty_field")
        if isinstance(non_empty_field, str) and not outline.get(non_empty_field):
            continue
        value_field = when.get("value_field")
        if isinstance(value_field, str):
            raw_value = outline.get(value_field)
            allowed_values = when.get("allowed_values")
            if not isinstance(allowed_values, list) or raw_value not in allowed_values:
                continue
        event = policy.get("on_exhausted")
        terminal_routes = flow.get("terminal_routes")
        if not isinstance(event, str) or not isinstance(terminal_routes, Mapping):
            return None
        action = terminal_routes.get(event)
        return action if action in {"pause", "fail"} else None
    return None


def workflow_terminal_action(flow: Mapping[str, Any], event: str) -> str:
    """Resolve a named non-retry terminal event from the workflow."""

    routes = flow.get("terminal_routes")
    action = routes.get(event) if isinstance(routes, Mapping) else None
    if action not in {"pause", "fail"}:
        raise WorkflowLoadError(f"工作流终止事件未定义：{event}")
    return action
