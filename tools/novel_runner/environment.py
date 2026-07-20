"""Load local environment settings without adding a runtime dependency.

The repository-level ``.env`` file is for developer-local secrets and is ignored
by Git. Existing process environment variables always take precedence so CI and
production callers can inject secrets without using a file.
"""

from __future__ import annotations

import os
from pathlib import Path


class EnvironmentError(ValueError):
    """Raised when a local environment file cannot be parsed safely."""


def _parse_value(raw: str, line_number: int) -> str:
    value = raw.strip()
    if not value:
        return ""
    if value[0] in {"'", '"'}:
        quote = value[0]
        if len(value) < 2 or value[-1] != quote:
            raise EnvironmentError(f".env 第 {line_number} 行的引号未闭合")
        return value[1:-1]
    return value


def load_dotenv(path: Path, *, override: bool = False) -> dict[str, str]:
    """Load KEY=VALUE pairs from *path* and return values actually applied."""

    if not path.is_file():
        return {}
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except OSError as exc:
        raise EnvironmentError(f"无法读取环境文件 {path}：{exc}") from exc

    loaded: dict[str, str] = {}
    for line_number, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            raise EnvironmentError(f".env 第 {line_number} 行缺少 '='")
        key, raw_value = line.split("=", maxsplit=1)
        key = key.strip()
        if not key or not key.replace("_", "a").isalnum() or key[0].isdigit():
            raise EnvironmentError(f".env 第 {line_number} 行的变量名无效")
        value = _parse_value(raw_value, line_number)
        if override or key not in os.environ:
            os.environ[key] = value
            loaded[key] = value
    return loaded


def load_project_environment(root: Path | None = None) -> dict[str, str]:
    """Load ``.env`` from the explicit project root or current directory."""

    project_root = (root or Path.cwd()).resolve()
    return load_dotenv(project_root / ".env")
