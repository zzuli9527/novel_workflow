"""Execute automatic unit-end review and state-rebuild gates."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..reporting import generate_unit_review
from ..state_rebuild import rebuild_state_snapshots
from ..workflow_runtime import WorkflowLoadError, ensure_step_inputs, ensure_step_outputs, load_workflow_step
from .common import UnitRunnerError


def _execute_unit_completion_step(
    flow: dict[str, Any],
    step_id: str,
    root: Path,
    run_id: str,
    unit_id: str,
    available_artifacts: set[str],
) -> Any:
    """Execute one automatic unit-end gate declared by the workflow."""

    try:
        step = load_workflow_step(root, step_id, flow=flow)
        if step.scope != "unit":
            raise WorkflowLoadError(f"工作流步骤 {step_id} 不是单元步骤")
        ensure_step_inputs(step, available_artifacts)
    except WorkflowLoadError as exc:
        raise UnitRunnerError(str(exc)) from exc

    handlers = {
        "review_unit": lambda: generate_unit_review(root, run_id, unit_id),
        "rebuild_state": lambda: rebuild_state_snapshots(root, run_id),
    }
    handler = handlers.get(step_id)
    if handler is None:
        raise UnitRunnerError(f"单元收尾步骤没有工具执行器：{step_id}")
    result = handler()
    if not isinstance(result, dict):
        raise UnitRunnerError(f"单元收尾步骤 {step_id} 未返回结构化产物")
    available_artifacts.update(step.produces)
    try:
        ensure_step_outputs(step, available_artifacts)
    except WorkflowLoadError as exc:
        raise UnitRunnerError(str(exc)) from exc
    return result
