"""Drive one chapter through workflow-declared routes."""

from __future__ import annotations

from pathlib import Path

from ..chapters import ChapterServiceError, commit_chapter, draft_chapter, extract_state, repair_chapter, review_chapter, resume_run
from ..provider import TextProvider
from ..storage import read_json, resolve_run_dir
from ..workflow_runtime import WorkflowLoadError, chapter_retry_available, chapter_retry_terminal_action, ensure_step_inputs, ensure_step_outputs, load_workflow_flow, load_workflow_step
from .artifacts import _chapter_artifacts
from .common import UnitRunnerError, UnitRunnerTerminal, _current_outline


def _execute_chapter_step(
    step_id: str,
    root: Path,
    run_id: str,
    chapter: int,
    provider: TextProvider,
) -> None:
    """Run a registered tool capability; the workflow chooses ``step_id``."""

    handlers = {
        "draft_chapter": lambda: draft_chapter(root, run_id, chapter, provider),
        "repair_chapter": lambda: repair_chapter(root, run_id, chapter, provider),
        "review_chapter": lambda: review_chapter(root, run_id, chapter, provider),
        "extract_state": lambda: extract_state(root, run_id, chapter, provider),
        "commit_chapter": lambda: commit_chapter(root, run_id, chapter),
        "resume_chapter": lambda: resume_run(root, run_id),
    }
    handler = handlers.get(step_id)
    if handler is None:
        raise UnitRunnerError(f"章节流程步骤没有工具执行器：{step_id}")
    handler()


def _drive_chapter(
    root: Path,
    run_id: str,
    chapter: int,
    provider: TextProvider,
) -> str:
    try:
        flow = load_workflow_flow(root)
    except WorkflowLoadError as exc:
        raise UnitRunnerError(str(exc)) from exc
    for _ in range(flow["chapter_max_steps"]):
        outline = _current_outline(root, run_id, chapter)
        status = outline.get("status")
        if status in flow["chapter_terminal_statuses"]:
            return str(status)
        try:
            route = flow["chapter_routes"].get(status)
            if not isinstance(route, str):
                raise WorkflowLoadError(f"章节状态未定义工作流路由：{status}")
            step = load_workflow_step(root, route, flow=flow)
            run_dir = resolve_run_dir(root, run_id)
            run_config = read_json(run_dir / "run.json")
            ensure_step_inputs(
                step, _chapter_artifacts(run_dir, run_config, chapter, outline)
            )
        except WorkflowLoadError as exc:
            raise UnitRunnerError(str(exc)) from exc
        try:
            _execute_chapter_step(route, root, run_id, chapter, provider)
        except ChapterServiceError as exc:
            failed_outline = _current_outline(root, run_id, chapter)
            retry_config = read_json(resolve_run_dir(root, run_id) / "run.json").get(
                "policies", {}
            ).get("retry", {})
            try:
                if chapter_retry_available(flow, failed_outline, retry_config):
                    continue
                terminal_action = chapter_retry_terminal_action(flow, failed_outline)
            except WorkflowLoadError as workflow_exc:
                raise UnitRunnerError(str(workflow_exc)) from workflow_exc
            if terminal_action is not None:
                raise UnitRunnerTerminal(terminal_action, str(exc)) from exc
            raise
        updated_outline = _current_outline(root, run_id, chapter)
        if updated_outline.get("status") in step.success_statuses:
            try:
                updated_run = read_json(resolve_run_dir(root, run_id) / "run.json")
                ensure_step_outputs(
                    step,
                    _chapter_artifacts(
                        resolve_run_dir(root, run_id),
                        updated_run,
                        chapter,
                        updated_outline,
                    ),
                )
            except WorkflowLoadError as exc:
                raise UnitRunnerError(str(exc)) from exc
    raise UnitRunnerError(
        f"第 {chapter} 章超过工作流声明的调度循环上限 {flow['chapter_max_steps']}"
    )
