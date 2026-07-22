from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import io
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.cli import main
from tools.novel_runner.wordcount import (
    DraftParseError,
    LengthPolicy,
    check_drafts,
    count_body_characters,
    parse_chapters,
)


class ParseChaptersTests(unittest.TestCase):
    def test_excludes_title_self_check_separator_and_whitespace(self) -> None:
        markdown = """# 第 1 章：开局

甲 乙。\n丙！

---

## 本章自检
- 这里不计入正文
"""
        chapters = parse_chapters(markdown)

        self.assertEqual(len(chapters), 1)
        self.assertEqual(chapters[0].number, 1)
        self.assertEqual(chapters[0].title, "开局")
        self.assertEqual(count_body_characters(chapters[0].body), 5)

    def test_splits_multiple_chapters_and_stops_at_each_metadata_block(self) -> None:
        markdown = """# 草稿汇总

## 第 1 章：第一章
甲乙丙

### 本章自检
不计入

## 第 2 章：第二章
丁戊己庚

### 第 2 章状态增量
不计入
"""
        chapters = parse_chapters(markdown)

        self.assertEqual([chapter.number for chapter in chapters], [1, 2])
        self.assertEqual([count_body_characters(chapter.body) for chapter in chapters], [3, 4])

    def test_supports_chinese_chapter_numbers(self) -> None:
        markdown = """# 第十二章：测试
正文

# 第一百零二章：继续
又一章
"""
        chapters = parse_chapters(markdown)
        self.assertEqual([chapter.number for chapter in chapters], [12, 102])

    def test_rejects_duplicate_numbers(self) -> None:
        markdown = """# 第 1 章
甲
# 第 1 章
乙
"""
        with self.assertRaisesRegex(DraftParseError, "重复"):
            parse_chapters(markdown)

    def test_rejects_missing_chapter_heading(self) -> None:
        with self.assertRaisesRegex(DraftParseError, "未找到章节标题"):
            parse_chapters("只有正文，没有标题")

    def test_ignores_chapter_like_text_inside_code_fence(self) -> None:
        markdown = """```text
# 第 99 章：示例
```

# 第 1 章：正文
甲乙
"""
        chapters = parse_chapters(markdown)
        self.assertEqual([chapter.number for chapter in chapters], [1])


class LengthGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = LengthPolicy(
            expand_from=3,
            target_min=5,
            target_max=7,
            review_over=9,
        )

    def _check(self, body: str):
        return check_drafts(f"# 第 1 章\n{body}\n", self.policy).chapters[0]

    def test_classifies_severe_shortage(self) -> None:
        check = self._check("甲乙")
        self.assertEqual(check.status, "failed_too_short")
        self.assertFalse(check.can_update_state)

    def test_classifies_targeted_expansion(self) -> None:
        check = self._check("甲乙丙丁")
        self.assertEqual(check.status, "needs_expansion")
        self.assertTrue(check.hard_pass)
        self.assertFalse(check.requires_review)
        self.assertTrue(check.can_update_state)

    def test_passes_target_range(self) -> None:
        check = self._check("甲乙丙丁戊")
        self.assertEqual(check.status, "passed")
        self.assertTrue(check.can_update_state)

    def test_requires_redundancy_review_above_target(self) -> None:
        check = self._check("甲乙丙丁戊己庚辛")
        self.assertEqual(check.status, "needs_redundancy_review")
        self.assertTrue(check.hard_pass)
        self.assertFalse(check.requires_review)
        self.assertTrue(check.can_update_state)

    def test_requires_compression_review_when_overlong(self) -> None:
        check = self._check("甲乙丙丁戊己庚辛壬癸")
        self.assertEqual(check.status, "needs_compression_review")
        self.assertFalse(check.hard_pass)
        self.assertFalse(check.can_update_state)

    def test_report_passes_with_soft_length_warnings(self) -> None:
        markdown = """# 第 1 章
甲乙丙丁
# 第 2 章
甲乙丙丁戊己庚辛
"""
        report = check_drafts(markdown, self.policy)
        self.assertEqual(report.result, "passed")
        self.assertEqual(report.exit_code, 0)

    def test_report_fails_when_any_chapter_is_short(self) -> None:
        markdown = """# 第 1 章
甲乙丙丁戊
# 第 2 章
甲乙
"""
        report = check_drafts(markdown, self.policy)
        self.assertEqual(report.result, "failed")
        self.assertEqual(report.exit_code, 1)

    def test_default_policy_boundaries(self) -> None:
        policy = LengthPolicy()
        cases = (
            (1799, "failed_too_short", False),
            (1800, "needs_expansion", True),
            (1999, "needs_expansion", True),
            (2000, "passed", True),
            (3000, "passed", True),
            (3001, "needs_redundancy_review", True),
            (3500, "needs_redundancy_review", True),
            (3501, "needs_compression_review", False),
        )
        for length, status, hard_pass in cases:
            with self.subTest(length=length):
                check = check_drafts(
                    f"# 第 1 章\n{'甲' * length}\n", policy
                ).chapters[0]
                self.assertEqual(check.status, status)
                self.assertEqual(check.hard_pass, hard_pass)

    def test_policy_rejects_invalid_threshold_order(self) -> None:
        with self.assertRaises(ValueError):
            LengthPolicy(expand_from=10, target_min=5, target_max=7, review_over=9)


class CliTests(unittest.TestCase):
    def _run_cli(self, markdown: str, *extra: str) -> tuple[int, str, str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "drafts.md"
            path.write_text(markdown, encoding="utf-8")
            stdout = io.StringIO()
            stderr = io.StringIO()
            with redirect_stdout(stdout), redirect_stderr(stderr):
                exit_code = main(
                    [
                        "check-drafts",
                        str(path),
                        "--expand-from",
                        "3",
                        "--min",
                        "5",
                        "--max",
                        "7",
                        "--review-over",
                        "9",
                        *extra,
                    ]
                )
            return exit_code, stdout.getvalue(), stderr.getvalue()

    def test_cli_returns_nonzero_for_short_chapter(self) -> None:
        exit_code, stdout, _ = self._run_cli("# 第 1 章\n甲乙\n")
        self.assertEqual(exit_code, 1)
        self.assertIn("failed_too_short", stdout)

    def test_cli_returns_zero_for_soft_length_warning(self) -> None:
        exit_code, stdout, _ = self._run_cli("# 第 1 章\n甲乙丙丁戊己庚辛\n")
        self.assertEqual(exit_code, 0)
        self.assertIn("needs_redundancy_review", stdout)

    def test_cli_returns_failure_for_hard_overlength(self) -> None:
        exit_code, stdout, _ = self._run_cli("# 第 1 章\n甲乙丙丁戊己庚辛壬癸\n")
        self.assertEqual(exit_code, 1)
        self.assertIn("needs_compression_review", stdout)

    def test_cli_json_output(self) -> None:
        exit_code, stdout, _ = self._run_cli("# 第 1 章\n甲乙丙丁戊\n", "--json")
        self.assertEqual(exit_code, 0)
        self.assertIn('"result": "passed"', stdout)

    def test_cli_returns_input_error_for_missing_heading(self) -> None:
        exit_code, _, stderr = self._run_cli("没有章节标题")
        self.assertEqual(exit_code, 3)
        self.assertIn("未找到章节标题", stderr)


if __name__ == "__main__":
    unittest.main()
