"""修仙搞笑长篇网文工作流执行器。"""

from .wordcount import (
    ChapterCheck,
    ChapterDraft,
    DraftCheckReport,
    DraftParseError,
    LengthPolicy,
    check_drafts,
    count_body_characters,
    parse_chapters,
)

__all__ = [
    "ChapterCheck",
    "ChapterDraft",
    "DraftCheckReport",
    "DraftParseError",
    "LengthPolicy",
    "check_drafts",
    "count_body_characters",
    "parse_chapters",
]

__version__ = "0.1.0"
