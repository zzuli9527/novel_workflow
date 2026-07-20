"""章节状态机和顺序生成守卫。"""

from __future__ import annotations


CHAPTER_STATUSES = {
    "planned",
    "outline_ready",
    "drafting",
    "draft_generated",
    "draft_failed_provider",
    "draft_failed_length",
    "draft_failed_contract",
    "draft_failed_quality",
    "draft_quality_pending",
    "draft_passed",
    "state_extracting",
    "state_failed",
    "state_ready",
    "committing",
    "committed",
    "locked",
}

ALLOWED_TRANSITIONS: dict[str, frozenset[str]] = {
    "planned": frozenset({"outline_ready"}),
    "outline_ready": frozenset({"drafting"}),
    "drafting": frozenset({"draft_generated", "draft_failed_provider"}),
    "draft_failed_provider": frozenset({"drafting"}),
    "draft_generated": frozenset(
        {
            "draft_failed_length",
            "draft_failed_contract",
            "draft_failed_quality",
            "draft_quality_pending",
        }
    ),
    "draft_failed_length": frozenset({"drafting"}),
    "draft_failed_contract": frozenset({"drafting"}),
    "draft_failed_quality": frozenset({"drafting"}),
    "draft_quality_pending": frozenset(
        {"draft_failed_contract", "draft_failed_quality", "draft_passed"}
    ),
    "draft_passed": frozenset({"state_extracting"}),
    "state_extracting": frozenset({"state_failed", "state_ready"}),
    "state_failed": frozenset({"state_extracting"}),
    "state_ready": frozenset({"committing", "state_failed"}),
    "committing": frozenset({"committed", "state_failed"}),
    "committed": frozenset({"locked"}),
    "locked": frozenset(),
}


class StateTransitionError(RuntimeError):
    """非法章节状态转换。"""


def validate_status(status: str) -> str:
    if status not in CHAPTER_STATUSES:
        raise StateTransitionError(f"未知章节状态：{status}")
    return status


def ensure_transition(current: str, target: str) -> None:
    validate_status(current)
    validate_status(target)
    if target not in ALLOWED_TRANSITIONS[current]:
        raise StateTransitionError(f"不允许从 {current} 转换到 {target}")


def transition_record(record: dict[str, object], target: str) -> dict[str, object]:
    current = record.get("status")
    if not isinstance(current, str):
        raise StateTransitionError("章节记录缺少字符串 status")
    ensure_transition(current, target)
    return {**record, "status": target}


def ensure_chapter_can_start(chapter_number: int, last_committed_chapter: int) -> None:
    if chapter_number <= 0:
        raise StateTransitionError("章节编号必须大于 0")
    expected = last_committed_chapter + 1
    if chapter_number != expected:
        raise StateTransitionError(
            f"只能开始第 {expected} 章；当前请求为第 {chapter_number} 章"
        )
