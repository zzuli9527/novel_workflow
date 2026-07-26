"""Data models shared by workflow registry and flow loaders."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..storage import StorageError


WORKFLOW_VERSION = "4.0"
REGISTRY_PATH = Path("workflow/编排/任务表.json")


class WorkflowLoadError(StorageError):
    """The authoritative workflow is absent or internally inconsistent."""


@dataclass(frozen=True, slots=True)
class ConditionalRules:
    when: dict[str, str]
    rule_paths: tuple[Path, ...]


@dataclass(frozen=True, slots=True)
class WorkflowContextSource:
    artifact: str
    section: str
    path: Path
    format: str
    when: dict[str, str]


@dataclass(frozen=True, slots=True)
class WorkflowTask:
    task_id: str
    kind: str
    prompt_path: Path
    rule_paths: tuple[Path, ...]
    contract_paths: tuple[Path, ...]
    conditional_rules: tuple[ConditionalRules, ...]
    context_sources: tuple[WorkflowContextSource, ...]
    requires: tuple[str, ...]
    produces: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class WorkflowStep:
    """One executable or approval step declared by 流程.json."""

    step_id: str
    kind: str
    scope: str
    requires: tuple[str, ...]
    optional_inputs: tuple[str, ...]
    produces: tuple[str, ...]
    success_statuses: tuple[str, ...]
    execution: str
