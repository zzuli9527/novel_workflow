"""Execute workflow-declared planning and ledger batch steps."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..batching import ChapterBatch
from ..ledger import build_ledger
from ..planning_service import plan_chapter_batch
from ..provider import TextProvider
from ..storage import resolve_run_dir
from ..workflow_runtime import WorkflowLoadError, ensure_step_inputs, ensure_step_outputs, load_workflow_step
from .artifacts import _batch_artifacts
from .common import UnitRunnerError


def _execute_batch_step(
    flow: dict[str, Any],
    step_id: str,
    root: Path,
    run_id: str,
    unit_id: str,
    batch: ChapterBatch,
    provider: TextProvider,
) -> Any:
    """Execute a batch capability selected by ``unit_lifecycle``."""

    try:
        step = load_workflow_step(root, step_id, flow=flow)
        if step.scope != "batch":
            raise WorkflowLoadError(f"工作流步骤 {step_id} 不是批次步骤")
        ensure_step_inputs(
            step, _batch_artifacts(resolve_run_dir(root, run_id), unit_id, batch)
        )
    except WorkflowLoadError as exc:
        raise UnitRunnerError(str(exc)) from exc

    handlers = {
        "plan_chapter_batch": lambda: plan_chapter_batch(
            root, run_id, unit_id, batch.start, batch.end, provider
        ),
        "build_ledger": lambda: build_ledger(
            root, run_id, batch.start, batch.end, provider
        ),
    }
    handler = handlers.get(step_id)
    if handler is None:
        raise UnitRunnerError(f"批次流程步骤没有工具执行器：{step_id}")
    result = handler()
    try:
        ensure_step_outputs(
            step, _batch_artifacts(resolve_run_dir(root, run_id), unit_id, batch)
        )
    except WorkflowLoadError as exc:
        raise UnitRunnerError(str(exc)) from exc
    return result
