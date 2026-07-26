"""Validate runtime artifacts against schemas owned by ``workflow/``."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError

from .storage import StorageError


class WorkflowSchemaError(StorageError):
    """A workflow schema or runtime artifact is invalid."""


_SCHEMA_DIR = Path("workflow/契约/模式")
_MAPPING_FILE = _SCHEMA_DIR / "映射.json"


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except OSError as exc:
        raise WorkflowSchemaError(f"无法读取 Schema 文件：{path}：{exc}") from exc
    except json.JSONDecodeError as exc:
        raise WorkflowSchemaError(
            f"Schema JSON 无效：{path}，第 {exc.lineno} 行第 {exc.colno} 列"
        ) from exc


def _schema_name(root: Path, artifact: str) -> str:
    mapping = _read_json(root / _MAPPING_FILE)
    if not isinstance(mapping, dict) or mapping.get("schema_mapping_version") != "1.0":
        raise WorkflowSchemaError("Schema 映射缺失或版本无效")
    artifacts = mapping.get("artifacts")
    schema_name = artifacts.get(artifact) if isinstance(artifacts, dict) else None
    if not isinstance(schema_name, str) or not schema_name:
        raise WorkflowSchemaError(f"Schema 映射未声明产物：{artifact}")
    path = Path(schema_name)
    if path.is_absolute() or ".." in path.parts or len(path.parts) != 1:
        raise WorkflowSchemaError(f"Schema 映射路径无效：{schema_name}")
    return schema_name


def artifact_schema_issues(root: Path, artifact: str, data: Any) -> list[str]:
    """Return deterministic Draft 2020-12 validation issues."""

    schema_name = _schema_name(root, artifact)
    schema = _read_json(root / _SCHEMA_DIR / schema_name)
    if not isinstance(schema, dict):
        raise WorkflowSchemaError(f"Schema 必须是对象：{schema_name}")
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise WorkflowSchemaError(f"Schema 自身无效：{schema_name}：{exc.message}") from exc
    validator = Draft202012Validator(schema)
    issues: list[str] = []
    for error in sorted(
        validator.iter_errors(data),
        key=lambda item: tuple(str(part) for part in item.absolute_path),
    ):
        path = ".".join(str(part) for part in error.absolute_path) or "$"
        issues.append(f"{path}: {error.message}")
    return issues


def ensure_artifact_schema(root: Path, artifact: str, data: Any) -> None:
    issues = artifact_schema_issues(root, artifact, data)
    if issues:
        raise WorkflowSchemaError(
            f"产物 {artifact} 未通过 Schema：" + "; ".join(issues)
        )
