"""Structured project-profile data used to select workflow rule packs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .storage import StorageError, read_json


def default_project_profile() -> dict[str, str]:
    return {
        "platform": "",
        "channel": "",
        "genre": "xianxia",
        "style": "comedy",
    }


def load_project_profile(run_dir: Path) -> dict[str, str]:
    """Read explicit selectors; prose project material never selects rules."""

    data = read_json(run_dir / "config/project-profile.json")
    if not isinstance(data, dict):
        raise StorageError("项目档案必须是 JSON 对象")
    profile = {
        "platform": data.get("platform"),
        "channel": data.get("channel"),
        # Existing runs can keep their two-field profile. New runs persist
        # these selectors so genre and style are no longer implicit.
        "genre": data.get("genre", "xianxia"),
        "style": data.get("style", "comedy"),
    }
    if not all(isinstance(value, str) for value in profile.values()):
        raise StorageError("项目档案 platform、channel、genre 和 style 必须是字符串")
    return profile


def validate_project_profile(data: Any) -> list[str]:
    if not isinstance(data, dict):
        return ["必须是 JSON 对象"]
    issues: list[str] = []
    for key in ("platform", "channel"):
        if not isinstance(data.get(key), str):
            issues.append(f"{key} 必须是字符串")
    for key in ("genre", "style"):
        if key in data and not isinstance(data.get(key), str):
            issues.append(f"{key} 必须是字符串")
    return issues
