"""Safe workflow file access and primitive value validation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import REGISTRY_PATH, WORKFLOW_VERSION, WorkflowLoadError


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise WorkflowLoadError(f"无法读取工作流文件：{path}：{exc}") from exc


def _read_json(path: Path) -> Any:
    try:
        return json.loads(_read_text(path))
    except json.JSONDecodeError as exc:
        raise WorkflowLoadError(
            f"工作流 JSON 不是有效 JSON：{path}，第 {exc.lineno} 行第 {exc.colno} 列"
        ) from exc


def _safe_relative(value: Any, *, field: str) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise WorkflowLoadError(f"工作流任务表 {field} 必须是非空字符串")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise WorkflowLoadError(f"工作流任务表 {field} 不能越出 workflow 目录")
    return path


def _safe_relative_list(value: Any, *, field: str) -> tuple[Path, ...]:
    if not isinstance(value, list):
        raise WorkflowLoadError(f"工作流任务表 {field} 必须是数组")
    return tuple(_safe_relative(item, field=field) for item in value)


def _string_list(value: Any, *, field: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item.strip() for item in value
    ):
        raise WorkflowLoadError(f"工作流任务表 {field} 必须是非空字符串数组")
    return tuple(value)


def _workflow_file(root: Path, relative: Path) -> Path:
    path = (root / "workflow" / relative).resolve()
    workflow_root = (root / "workflow").resolve()
    if workflow_root not in path.parents:
        raise WorkflowLoadError(f"工作流文件越出根目录：{relative}")
    if not path.is_file():
        raise WorkflowLoadError(f"缺少工作流文件：{path}")
    return path


def _matches_context(when: dict[str, str], context: dict[str, str] | None) -> bool:
    if context is None:
        return False
    return all(context.get(key) == expected for key, expected in when.items())


def _load_registry(root: Path) -> dict[str, Any]:
    path = root / REGISTRY_PATH
    data = _read_json(path)
    if not isinstance(data, dict):
        raise WorkflowLoadError("工作流任务表必须是对象")
    if data.get("workflow_version") != WORKFLOW_VERSION:
        raise WorkflowLoadError(
            f"工作流版本必须是 {WORKFLOW_VERSION}，当前为 {data.get('workflow_version')!r}"
        )
    tasks = data.get("tasks")
    if not isinstance(tasks, dict):
        raise WorkflowLoadError("工作流任务表缺少 tasks 对象")
    flow = data.get("flow")
    _safe_relative(flow, field="flow")
    return data
