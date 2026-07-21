from __future__ import annotations

import unittest

from tools.novel_runner.config import default_run_config
from tools.novel_runner.outline_validation import (
    OutlineValidationError,
    ensure_comedy_rotation,
    validate_outline,
)


def valid_outline(number: int = 1, mechanism: str = "性格反差") -> dict[str, object]:
    return {
        "chapter_id": f"chapter-{number:04d}",
        "number": number,
        "title": f"测试{number}",
        "status": "outline_ready",
        "intent": "推进当前任务",
        "opening_state": [],
        "required_outcomes": ["完成行动"],
        "forbidden_outcomes": [],
        "progression_payoff": "获得修炼信息",
        "comedy_mechanism": mechanism,
        "comedy_payoff": "反差影响行动",
        "cost_or_aftereffect": "消耗时间",
        "closing_state": ["本章行动已经产生结果"],
        "next_chapter_input": ["继续处理本章后果"],
        "target_length": {"min": 2000, "max": 3000},
        "scenes": [
            {
                "scene_id": f"chapter-{number:04d}-scene-1",
                "intent": "建立问题",
                "target_length": 1000,
                "required_outcomes": [],
            },
            {
                "scene_id": f"chapter-{number:04d}-scene-2",
                "intent": "完成行动",
                "target_length": 1100,
                "required_outcomes": ["完成行动"],
            },
        ],
        "writability": {"is_writable": True, "estimated_length": 2100, "risks": []},
    }


class OutlineValidationTests(unittest.TestCase):
    def test_accepts_complete_writable_outline(self) -> None:
        self.assertEqual(validate_outline(valid_outline(), default_run_config("run")), ())

    def test_rejects_missing_dual_engine_fields(self) -> None:
        outline = valid_outline()
        outline["progression_payoff"] = ""
        outline["comedy_mechanism"] = ""
        issues = validate_outline(outline, default_run_config("run"))
        paths = {issue.path for issue in issues}
        self.assertIn("progression_payoff", paths)
        self.assertIn("comedy_mechanism", paths)

    def test_rejects_scene_budget_below_target(self) -> None:
        outline = valid_outline()
        outline["scenes"][0]["target_length"] = 100
        outline["scenes"][1]["target_length"] = 100
        issues = validate_outline(outline, default_run_config("run"))
        self.assertTrue(any(issue.path == "scenes" for issue in issues))

    def test_rejects_outline_without_handoff_state(self) -> None:
        outline = valid_outline()
        outline["closing_state"] = []
        outline["next_chapter_input"] = []
        issues = validate_outline(outline, default_run_config("run"))
        paths = {issue.path for issue in issues}
        self.assertIn("closing_state", paths)
        self.assertIn("next_chapter_input", paths)

    def test_rejects_three_identical_comedy_mechanisms(self) -> None:
        outlines = [valid_outline(number, "信息差") for number in range(1, 4)]
        with self.assertRaisesRegex(OutlineValidationError, "连续使用 3 章"):
            ensure_comedy_rotation(outlines, 1, 3)

    def test_allows_two_identical_then_switch(self) -> None:
        outlines = [
            valid_outline(1, "信息差"),
            valid_outline(2, "信息差"),
            valid_outline(3, "规则错位"),
        ]
        ensure_comedy_rotation(outlines, 1, 3)


if __name__ == "__main__":
    unittest.main()
