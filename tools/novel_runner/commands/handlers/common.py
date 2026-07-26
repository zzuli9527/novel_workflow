"""Shared CLI rendering, range parsing, and exit codes."""

from __future__ import annotations

import json


EXIT_PASSED = 0
EXIT_FAILED = 1
EXIT_REVIEW_REQUIRED = 2
EXIT_INPUT_ERROR = 3


def _render_or_json(data: object, as_json: bool) -> None:
    if as_json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(data)


def _parse_range(value: str) -> tuple[int, int]:
    normalized = value.replace("～", "-").replace("~", "-")
    parts = normalized.split("-", maxsplit=1)
    if len(parts) != 2 or not all(part.strip().isdigit() for part in parts):
        raise ValueError("章节范围格式应为 start-end")
    return int(parts[0]), int(parts[1])
