"""Markdown 章节拆分和正文长度闸门。"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import re
from typing import Iterable


CHAPTER_HEADING_RE = re.compile(
    r"^\s{0,3}#{1,6}\s*第\s*"
    r"(?P<number>\d+|[零〇一二两三四五六七八九十百千]+)"
    r"\s*章(?:\s*[：:、.．\-—]\s*)?(?P<title>.*?)\s*$"
)

METADATA_HEADING_RE = re.compile(
    r"^\s{0,3}#{1,6}\s*(?:"
    r"本章自检|本章检查|成稿自检|"
    r"状态回填|状态增量|本章状态(?:回填|增量)?|"
    r"第\s*(?:\d+|[零〇一二两三四五六七八九十百千]+)\s*章.*状态(?:回填|增量)|"
    r"作者说明|作者的话|本章说|写作说明|元数据"
    r")\s*$"
)

INLINE_AUTHOR_NOTE_RE = re.compile(
    r"^\s*(?:作者说明|作者的话|本章说|写作说明)\s*[：:]"
)

HORIZONTAL_RULE_RE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
WHITESPACE_RE = re.compile(r"\s+")


class DraftParseError(ValueError):
    """输入 Markdown 无法被安全拆分为章节。"""


@dataclass(frozen=True, slots=True)
class LengthPolicy:
    """单章正文长度策略。"""

    target_min: int = 2000
    target_max: int = 3000
    expand_from: int = 1800
    review_over: int = 3500

    def __post_init__(self) -> None:
        values = (
            self.expand_from,
            self.target_min,
            self.target_max,
            self.review_over,
        )
        if any(value < 0 for value in values):
            raise ValueError("长度策略不能包含负数")
        if not (
            self.expand_from
            <= self.target_min
            <= self.target_max
            <= self.review_over
        ):
            raise ValueError(
                "长度策略必须满足 expand_from <= target_min <= "
                "target_max <= review_over"
            )


@dataclass(frozen=True, slots=True)
class ChapterDraft:
    """从 Markdown 中提取出的单章正文。"""

    number: int
    title: str
    body: str
    start_line: int
    end_line: int


@dataclass(frozen=True, slots=True)
class ChapterCheck:
    """单章机械长度检查结果。"""

    number: int
    title: str
    actual_length: int
    status: str
    hard_pass: bool
    requires_review: bool
    can_update_state: bool
    message: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class DraftCheckReport:
    """一个 Markdown 文件的逐章检查报告。"""

    chapters: tuple[ChapterCheck, ...]
    result: str
    exit_code: int

    def to_dict(self) -> dict[str, object]:
        return {
            "result": self.result,
            "exit_code": self.exit_code,
            "chapters": [chapter.to_dict() for chapter in self.chapters],
        }


def _chinese_number_to_int(value: str) -> int:
    digits = {
        "零": 0,
        "〇": 0,
        "一": 1,
        "二": 2,
        "两": 2,
        "三": 3,
        "四": 4,
        "五": 5,
        "六": 6,
        "七": 7,
        "八": 8,
        "九": 9,
    }
    units = {"十": 10, "百": 100, "千": 1000}

    if all(char in digits for char in value):
        return int("".join(str(digits[char]) for char in value))

    total = 0
    current = 0
    for char in value:
        if char in digits:
            current = digits[char]
            continue
        if char not in units:
            raise DraftParseError(f"无法识别章节数字：{value}")
        unit = units[char]
        total += (current or 1) * unit
        current = 0
    return total + current


def parse_chapter_number(value: str) -> int:
    if value.isdigit():
        number = int(value)
    else:
        number = _chinese_number_to_int(value)
    if number <= 0:
        raise DraftParseError(f"章节编号必须大于 0：{value}")
    return number


def _extract_body(lines: list[str]) -> str:
    body_lines: list[str] = []
    for line in lines:
        if METADATA_HEADING_RE.match(line) or INLINE_AUTHOR_NOTE_RE.match(line):
            break
        if HORIZONTAL_RULE_RE.match(line):
            continue
        body_lines.append(line)

    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)
    while body_lines and not body_lines[-1].strip():
        body_lines.pop()
    return "\n".join(body_lines)


def parse_chapters(markdown: str) -> tuple[ChapterDraft, ...]:
    """按 Markdown 章节标题拆分正文。

    章节标题必须使用 ``# 第 N 章`` 至 ``###### 第 N 章`` 的形式。
    标题之前的文档说明会被忽略；自检、状态和作者说明区块不计入正文。
    """

    lines = markdown.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    headings: list[tuple[int, int, str]] = []

    in_fence = False
    fence_marker: str | None = None
    for index, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            continue
        if in_fence:
            continue

        if METADATA_HEADING_RE.match(line):
            continue
        match = CHAPTER_HEADING_RE.match(line)
        if not match:
            continue
        number = parse_chapter_number(match.group("number"))
        title = match.group("title").strip()
        headings.append((index, number, title))

    if not headings:
        raise DraftParseError(
            "未找到章节标题；请使用 Markdown 标题，例如：# 第 1 章：标题"
        )

    numbers = [number for _, number, _ in headings]
    if len(set(numbers)) != len(numbers):
        raise DraftParseError("检测到重复章节编号")
    if numbers != sorted(numbers):
        raise DraftParseError("章节编号必须按升序排列")

    chapters: list[ChapterDraft] = []
    for position, (heading_index, number, title) in enumerate(headings):
        next_index = (
            headings[position + 1][0]
            if position + 1 < len(headings)
            else len(lines)
        )
        body = _extract_body(lines[heading_index + 1 : next_index])
        chapters.append(
            ChapterDraft(
                number=number,
                title=title,
                body=body,
                start_line=heading_index + 1,
                end_line=next_index,
            )
        )

    return tuple(chapters)


def count_body_characters(body: str) -> int:
    """统计去除所有空白后的 Unicode 字符数，标点计入。"""

    return len(WHITESPACE_RE.sub("", body))


def check_chapter(chapter: ChapterDraft, policy: LengthPolicy) -> ChapterCheck:
    actual = count_body_characters(chapter.body)

    if actual < policy.expand_from:
        return ChapterCheck(
            number=chapter.number,
            title=chapter.title,
            actual_length=actual,
            status="failed_too_short",
            hard_pass=False,
            requires_review=False,
            can_update_state=False,
            message="正文严重不足；应重写或回查章纲",
        )
    if actual < policy.target_min:
        return ChapterCheck(
            number=chapter.number,
            title=chapter.title,
            actual_length=actual,
            status="needs_expansion",
            hard_pass=False,
            requires_review=False,
            can_update_state=False,
            message="正文轻微不足；应按场景缺口定向扩写",
        )
    if actual <= policy.target_max:
        return ChapterCheck(
            number=chapter.number,
            title=chapter.title,
            actual_length=actual,
            status="passed",
            hard_pass=True,
            requires_review=False,
            can_update_state=True,
            message="长度闸门通过",
        )
    if actual <= policy.review_over:
        return ChapterCheck(
            number=chapter.number,
            title=chapter.title,
            actual_length=actual,
            status="needs_redundancy_review",
            hard_pass=True,
            requires_review=True,
            can_update_state=False,
            message="超过目标上限；完成冗余复查后才能放行",
        )
    return ChapterCheck(
        number=chapter.number,
        title=chapter.title,
        actual_length=actual,
        status="needs_compression_review",
        hard_pass=True,
        requires_review=True,
        can_update_state=False,
        message="正文明显超长；压缩复查后才能放行",
    )


def check_drafts(
    markdown: str, policy: LengthPolicy | None = None
) -> DraftCheckReport:
    active_policy = policy or LengthPolicy()
    checks = tuple(
        check_chapter(chapter, active_policy)
        for chapter in parse_chapters(markdown)
    )

    if any(not check.hard_pass for check in checks):
        return DraftCheckReport(checks, "failed", 1)
    if any(check.requires_review for check in checks):
        return DraftCheckReport(checks, "review_required", 2)
    return DraftCheckReport(checks, "passed", 0)


def render_text_report(report: DraftCheckReport) -> str:
    lines: list[str] = []
    for chapter in report.chapters:
        title = f"《{chapter.title}》" if chapter.title else ""
        lines.append(
            f"Chapter {chapter.number}{title}: "
            f"{chapter.actual_length} chars, {chapter.status}, "
            f"can_update_state={'yes' if chapter.can_update_state else 'no'}"
        )
    lines.append(f"Result: {report.result}")
    return "\n".join(lines)


def iter_failed(report: DraftCheckReport) -> Iterable[ChapterCheck]:
    return (chapter for chapter in report.chapters if not chapter.hard_pass)
