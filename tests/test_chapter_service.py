from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.chapter_service import (
    ChapterServiceError,
    commit_chapter,
    draft_chapter,
    extract_state,
    get_run_status,
    repair_chapter,
    review_chapter,
    resume_run,
)
from tools.novel_runner.config import init_run
from tools.novel_runner.provider import FixtureProvider
from tools.novel_runner.provider import GenerationRequest, ProviderError
from tools.novel_runner.master_plan import default_master_plan
from tools.novel_runner.storage import atomic_write_json
from tests.master_plan_support import install_approved_master_plan


VALID_STATE_EVENT = {
    "entity_changes": [],
    "relationship_changes": [],
    "cultivation_changes": [],
    "resource_changes": [],
    "knowledge_changes": [],
    "thread_changes": [],
    "comedy_changes": [],
    "new_constraints": [],
    "resolved_constraints": [],
    "next_chapter_inputs": [],
    "deviations": [],
}

VALID_REVIEW = {
    "required_outcomes": [],
    "forbidden_outcomes": [],
    "summary_like": False,
    "cultivation_consistent": True,
    "comedy_causal": True,
    "serious_consequences_preserved": True,
    "chapter_hook_concrete": True,
    "resource_continuity_consistent": True,
    "knowledge_states_consistent": True,
    "character_voices_distinct": True,
    "multi_line_causality_preserved": True,
    "warnings": [],
}


class ChapterServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        workflow = self.root / "workflow"
        workflow.mkdir()
        (workflow / "04-draft.md").write_text("# 正文规则\n", encoding="utf-8")
        (workflow / "05-update-state.md").write_text("# 状态规则\n", encoding="utf-8")
        self.run_dir = init_run(self.root, "demo-run")

        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["length"].update(
            {"expand_from": 3, "target_min": 5, "target_max": 7, "review_over": 9}
        )
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")

        outlines = [
            {
                "chapter_id": "chapter-0001",
                "number": 1,
                "title": "测试章",
                "story_unit_id": None,
                "status": "outline_ready",
                "target_length": {"min": 5, "max": 7},
                "intent": "测试完整闭环",
                "opening_state": [],
                "required_outcomes": [],
                "forbidden_outcomes": [],
                "progression_payoff": "推进修炼信息",
                "comedy_mechanism": "性格反差",
                "comedy_payoff": "反差改变行动",
                "cost_or_aftereffect": "消耗时间",
                "closing_state": ["本章测试行动完成"],
                "next_chapter_input": ["继续测试后续行动"],
                "scenes": [
                    {
                        "scene_id": "chapter-0001-scene-1",
                        "intent": "建立问题",
                        "target_length": 2,
                        "required_outcomes": [],
                    },
                    {
                        "scene_id": "chapter-0001-scene-2",
                        "intent": "完成行动",
                        "target_length": 3,
                        "required_outcomes": [],
                    },
                ],
                "writability": {
                    "is_writable": True,
                    "estimated_length": 5,
                    "risks": [],
                },
            }
        ]
        (self.run_dir / "planning/chapter-outlines.json").write_text(
            json.dumps(outlines, ensure_ascii=False), encoding="utf-8"
        )
        install_approved_master_plan(
            self.root,
            "demo-run",
            [("unit-0001", 1, 10)],
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _fixture(self, name: str, content: str) -> FixtureProvider:
        path = self.root / name
        path.write_text(content, encoding="utf-8")
        return FixtureProvider(path)

    def _pass_quality_review(self, name: str = "review.json") -> dict[str, object]:
        return review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture(name, json.dumps(VALID_REVIEW, ensure_ascii=False)),
        )

    def _draft_and_review(self, body: str = "甲乙丙丁戊") -> None:
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("draft.md", f"# 第 1 章：测试章\n{body}\n"),
        )
        self._pass_quality_review()

    def test_draft_master_plan_blocks_direct_chapter_drafting(self) -> None:
        atomic_write_json(
            self.run_dir / "config/master-plan.json",
            default_master_plan(),
        )

        with self.assertRaisesRegex(ChapterServiceError, "审批闸门"):
            draft_chapter(
                self.root,
                "demo-run",
                1,
                self._fixture("blocked-draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
            )

        self.assertFalse((self.run_dir / "chapters/0001").exists())

    def test_draft_requires_quality_review_before_creating_final(self) -> None:
        result = draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )

        self.assertEqual(result["outline"]["status"], "draft_quality_pending")
        self.assertFalse((self.run_dir / "chapters/0001/draft.final.md").is_file())
        self.assertTrue((self.run_dir / "chapters/0001/draft.prompt.md").is_file())
        self.assertEqual(result["check"]["actual_length"], 5)
        prompt = (self.run_dir / "chapters/0001/draft.prompt.v1.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("本章机械长度契约", prompt)
        self.assertIn('"preferred_range": [', prompt)
        self.assertIn('"preferred_range": [\n    5,\n    6\n  ]', prompt)
        self.assertIn('"hard_range": [', prompt)

        reviewed = self._pass_quality_review()
        self.assertEqual(reviewed["outline"]["status"], "draft_passed")
        self.assertTrue((self.run_dir / "chapters/0001/draft.final.md").is_file())

    def test_review_and_state_prompts_use_compact_chapter_contract(self) -> None:
        self._draft_and_review()
        review_prompt = (
            self.run_dir / "chapters/0001/review.prompt.v1.md"
        ).read_text(encoding="utf-8")
        self.assertIn("当前章契约", review_prompt)
        self.assertIn('"required_outcomes"', review_prompt)
        self.assertNotIn('"scene_id"', review_prompt)

        extract_state(
            self.root,
            "demo-run",
            1,
            self._fixture("compact-state.json", json.dumps(VALID_STATE_EVENT)),
        )
        state_prompt = (
            self.run_dir / "chapters/0001/state.prompt.v1.md"
        ).read_text(encoding="utf-8")
        self.assertIn("当前章契约", state_prompt)
        self.assertIn('"closing_state"', state_prompt)
        self.assertNotIn('"scene_id"', state_prompt)
        state_contract = state_prompt.split("# 当前章契约\n\n", 1)[1].split(
            "\n\n# ", 1
        )[0]
        self.assertNotIn('"intent"', state_contract)
        self.assertNotIn('"opening_state"', state_contract)
        state_checks = state_prompt.split("# 本章检查结果\n\n", 1)[1].split(
            "\n\n# ", 1
        )[0]
        self.assertIn('"quality_failures"', state_checks)
        self.assertNotIn('"required_outcomes"', state_checks)
        self.assertNotIn('"source_evidence"', state_checks)

    def test_short_draft_is_blocked(self) -> None:
        result = draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("short.md", "# 第 1 章：测试章\n甲乙\n"),
        )
        self.assertEqual(result["outline"]["status"], "draft_failed_length")
        self.assertFalse((self.run_dir / "chapters/0001/draft.final.md").exists())
        with self.assertRaisesRegex(ChapterServiceError, "draft_passed"):
            extract_state(
                self.root,
                "demo-run",
                1,
                self._fixture("state.json", json.dumps(VALID_STATE_EVENT)),
            )

    def test_slightly_short_draft_continues_to_quality_review(self) -> None:
        result = draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("slightly-short.md", "# 第 1 章：测试章\n甲乙丙丁\n"),
        )
        self.assertEqual(result["outline"]["status"], "draft_quality_pending")
        self.assertEqual(result["check"]["status"], "needs_expansion")
        self.assertTrue(result["check"]["hard_pass"])
        reviewed = self._pass_quality_review("slightly-short-review.json")
        self.assertEqual(reviewed["outline"]["status"], "draft_passed")

    def test_slightly_long_draft_continues_to_quality_review(self) -> None:
        result = draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "slightly-long.md",
                "# 第 1 章：测试章\n甲乙丙丁戊己庚辛\n",
            ),
        )
        self.assertEqual(result["outline"]["status"], "draft_quality_pending")
        self.assertEqual(result["check"]["status"], "needs_redundancy_review")
        self.assertTrue(result["check"]["hard_pass"])

    def test_rejects_response_with_wrong_chapter_number(self) -> None:
        result = draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("wrong.md", "# 第 2 章：错误\n甲乙丙丁戊\n"),
        )
        self.assertEqual(result["outline"]["status"], "draft_failed_contract")

    def test_quality_review_enforces_required_and_forbidden_contracts(self) -> None:
        outline_path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(outline_path.read_text(encoding="utf-8"))
        outlines[0]["required_outcomes"] = ["角色取得令牌"]
        outlines[0]["forbidden_outcomes"] = ["角色直接突破"]
        outline_path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("contract-draft.md", "# 第 1 章：测试章\n角色取得令牌。\n"),
        )
        review = {
            **VALID_REVIEW,
            "required_outcomes": [
                {"index": 0, "passed": True, "source_evidence": "角色取得令牌"}
            ],
            "forbidden_outcomes": [
                {"index": 0, "appeared": False, "source_evidence": ""}
            ],
        }
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("contract-review.json", json.dumps(review, ensure_ascii=False)),
        )
        self.assertEqual(result["outline"]["status"], "draft_passed")

    def test_quality_review_blocks_missing_required_outcome(self) -> None:
        outline_path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(outline_path.read_text(encoding="utf-8"))
        outlines[0]["required_outcomes"] = ["角色取得令牌"]
        outline_path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        review = {
            **VALID_REVIEW,
            "required_outcomes": [
                {"index": 0, "passed": False, "source_evidence": ""}
            ],
        }
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("missing-review.json", json.dumps(review, ensure_ascii=False)),
        )
        self.assertEqual(result["outline"]["status"], "draft_failed_contract")
        self.assertFalse((self.run_dir / "chapters/0001/draft.final.md").exists())

    def test_quality_review_evidence_failure_retries_without_rewriting_draft(self) -> None:
        outline_path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(outline_path.read_text(encoding="utf-8"))
        outlines[0]["required_outcomes"] = ["角色记下令牌"]
        outline_path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("review-retry-draft.md", "# 第 1 章：测试章\n角色记下令牌。\n"),
        )
        invalid = {
            **VALID_REVIEW,
            "required_outcomes": [
                {"index": 0, "passed": True, "source_evidence": "角色令牌"}
            ],
        }
        with self.assertRaisesRegex(ChapterServiceError, "证据不在正文"):
            review_chapter(
                self.root,
                "demo-run",
                1,
                self._fixture(
                    "invalid-review-evidence.json",
                    json.dumps(invalid, ensure_ascii=False),
                ),
            )
        failed = json.loads(outline_path.read_text(encoding="utf-8"))[0]
        self.assertEqual(failed["status"], "draft_quality_pending")
        self.assertIn("证据不在正文", failed["review_failure_reason"])

        valid = {
            **VALID_REVIEW,
            "required_outcomes": [
                {"index": 0, "passed": True, "source_evidence": "角色记下令牌"}
            ],
        }
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "valid-review-evidence.json",
                json.dumps(valid, ensure_ascii=False),
            ),
        )

        self.assertEqual(result["outline"]["status"], "draft_passed")
        self.assertNotIn("review_failure_reason", result["outline"])
        self.assertEqual(result["outline"]["retry_counts"]["review_format"], 1)
        prompt = (self.run_dir / "chapters/0001/review.prompt.v2.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("上次质量评审失败修复信息", prompt)
        self.assertIn('"verbatim_paragraph_catalog"', prompt)
        self.assertIn("角色记下令牌。", prompt)
        self.assertIn("角色令牌", prompt)

    def test_quality_review_evidence_ignores_whitespace(self) -> None:
        outline_path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(outline_path.read_text(encoding="utf-8"))
        outlines[0]["required_outcomes"] = ["角色取得令牌"]
        outline_path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "review-whitespace-draft.md",
                "# 第 1 章：测试章\n角色 取得\n令牌。\n",
            ),
        )
        review = {
            **VALID_REVIEW,
            "required_outcomes": [
                {"index": 0, "passed": True, "source_evidence": "角色取得令牌"}
            ],
        }
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "review-whitespace.json",
                json.dumps(review, ensure_ascii=False),
            ),
        )
        self.assertEqual(result["outline"]["status"], "draft_passed")

    def test_quality_review_blocks_summary_like_draft(self) -> None:
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        review = {**VALID_REVIEW, "summary_like": True}
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("summary-review.json", json.dumps(review, ensure_ascii=False)),
        )
        self.assertEqual(result["outline"]["status"], "draft_failed_quality")

    def test_quality_review_blocks_cultivation_inconsistency(self) -> None:
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        review = {**VALID_REVIEW, "cultivation_consistent": False}
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "cultivation-review.json", json.dumps(review, ensure_ascii=False)
            ),
        )
        self.assertEqual(result["outline"]["status"], "draft_failed_quality")
        self.assertIn("cultivation_consistent", result["review"]["quality_failures"])

    def test_quality_review_blocks_comedy_that_erases_consequence(self) -> None:
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        review = {**VALID_REVIEW, "serious_consequences_preserved": False}
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "consequence-review.json", json.dumps(review, ensure_ascii=False)
            ),
        )
        self.assertEqual(result["outline"]["status"], "draft_failed_quality")
        self.assertIn(
            "serious_consequences_preserved",
            result["review"]["quality_failures"],
        )

    def test_quality_review_allows_soft_quality_warnings(self) -> None:
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        review = {
            **VALID_REVIEW,
            "comedy_causal": False,
            "chapter_hook_concrete": False,
            "character_voices_distinct": False,
        }
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("voices-review.json", json.dumps(review, ensure_ascii=False)),
        )
        self.assertEqual(result["outline"]["status"], "draft_passed")
        self.assertEqual(result["review"]["quality_failures"], [])
        self.assertEqual(
            result["review"]["soft_quality_warnings"],
            [
                "comedy_causal",
                "chapter_hook_concrete",
                "character_voices_distinct",
            ],
        )
        self.assertTrue((self.run_dir / "chapters/0001/draft.final.md").is_file())

    def test_hard_quality_failure_still_blocks_with_soft_warning(self) -> None:
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        review = {
            **VALID_REVIEW,
            "serious_consequences_preserved": False,
            "character_voices_distinct": False,
        }
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("mixed-review.json", json.dumps(review, ensure_ascii=False)),
        )
        self.assertEqual(result["outline"]["status"], "draft_failed_quality")
        self.assertIn(
            "serious_consequences_preserved", result["review"]["quality_failures"]
        )
        self.assertEqual(
            result["review"]["soft_quality_warnings"],
            ["character_voices_distinct"],
        )

    def test_quality_review_blocks_disconnected_multi_line_plot(self) -> None:
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        review = {**VALID_REVIEW, "multi_line_causality_preserved": False}
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "multi-line-review.json", json.dumps(review, ensure_ascii=False)
            ),
        )
        self.assertEqual(result["outline"]["status"], "draft_failed_quality")
        self.assertIn(
            "multi_line_causality_preserved", result["review"]["quality_failures"]
        )

    def test_extract_and_commit_complete_vertical_slice(self) -> None:
        self._draft_and_review()
        event = extract_state(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "state.json", json.dumps(VALID_STATE_EVENT, ensure_ascii=False)
            ),
        )
        self.assertEqual(event["chapter"], 1)
        self.assertEqual(event["source_draft"], "chapters/0001/draft.final.md")

        result = commit_chapter(self.root, "demo-run", 1)
        self.assertEqual(result["outline"]["status"], "committed")
        self.assertEqual(result["run"]["last_committed_chapter"], 1)
        self.assertTrue((self.run_dir / "state/events.jsonl").is_file())
        self.assertTrue(
            (self.run_dir / "state/snapshots/chapter-0001.json").is_file()
        )

    def test_successful_commit_clears_stale_pause_reason(self) -> None:
        self._draft_and_review()
        extract_state(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "state-clear-pause.json",
                json.dumps(VALID_STATE_EVENT, ensure_ascii=False),
            ),
        )
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run.update({"status": "paused", "pause_reason": "旧失败原因"})
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")

        result = commit_chapter(self.root, "demo-run", 1)

        self.assertEqual(result["run"]["status"], "running")
        self.assertNotIn("pause_reason", result["run"])

    def test_continuity_failure_does_not_append_state_event(self) -> None:
        self._draft_and_review()
        state = {
            **VALID_STATE_EVENT,
            "resource_changes": [
                {
                    "owner_id": "protagonist",
                    "resource_id": "spirit_stone_low",
                    "operation": "consume",
                    "amount": 1,
                    "unit": "枚",
                    "resulting_balance": 0,
                    "source_or_destination": "修炼消耗",
                    "change": "消耗一枚灵石",
                    "source_evidence": "甲乙丙丁戊",
                }
            ],
        }
        with self.assertRaisesRegex(ChapterServiceError, "余额不能为负"):
            extract_state(
                self.root,
                "demo-run",
                1,
                self._fixture(
                    "negative-resource.json", json.dumps(state, ensure_ascii=False)
                ),
            )

        events_path = self.run_dir / "state/events.jsonl"
        self.assertFalse(events_path.exists())
        self.assertFalse((self.run_dir / "chapters/0001/state-event.json").exists())
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["status"], "state_failed")
        self.assertIn("余额不能为负", outlines[0]["state_failure_reason"])
        self.assertFalse((self.run_dir / "logs/commit-journal.json").exists())

        task_records = [
            json.loads(line)
            for line in (self.run_dir / "logs/tasks.jsonl").read_text(
                encoding="utf-8"
            ).splitlines()
            if line.strip()
        ]
        state_records = [
            item for item in task_records if item.get("task") == "extract_state"
        ]
        self.assertNotIn("accepted", [item.get("status") for item in state_records])

    def test_state_prompt_lists_legal_changes_for_active_tracked_states(self) -> None:
        initial_path = self.run_dir / "config/initial-state.json"
        initial = json.loads(initial_path.read_text(encoding="utf-8"))
        initial["cultivation"] = [
            {
                "subject_id": "protagonist",
                "stage": "炼气一层",
                "abilities": [
                    {"state_id": "wind-sense", "description": "可感知风向"}
                ],
                "injuries": [
                    {"state_id": "old-wound", "description": "旧伤仍在"}
                ],
                "limits": [
                    {"state_id": "night-limit", "description": "夜间不能御舟"}
                ],
            }
        ]
        initial_path.write_text(
            json.dumps(initial, ensure_ascii=False), encoding="utf-8"
        )
        self._draft_and_review()
        extract_state(
            self.root,
            "demo-run",
            1,
            self._fixture("state.json", json.dumps(VALID_STATE_EVENT)),
        )
        prompt = (
            self.run_dir / "chapters/0001/state.prompt.v1.md"
        ).read_text(encoding="utf-8")
        section = prompt.split("# 允许引用的活动状态 ID\n\n", 1)[1].split(
            "\n\n# ", 1
        )[0]
        allowed = json.loads(section)
        details = {
            item["state_id"]: item
            for item in allowed["active_tracked_states_by_subject"]["protagonist"]
        }
        self.assertEqual(
            details["old-wound"]["allowed_changes"],
            ["injury:set", "recovery:set", "recovery:resolve"],
        )
        self.assertEqual(
            details["wind-sense"]["allowed_changes"],
            ["ability:set", "ability:resolve"],
        )
        self.assertEqual(
            details["night-limit"]["allowed_changes"],
            ["restriction:set", "restriction:resolve"],
        )
        self.assertNotIn("resolved-old-wound", section)

    def test_unknown_superseded_fact_is_content_retry_with_allowed_ids(self) -> None:
        initial_path = self.run_dir / "config/initial-state.json"
        initial = json.loads(initial_path.read_text(encoding="utf-8"))
        initial["knowledge"] = [
            {
                "character_id": "protagonist",
                "fact_id": "known-fact",
                "state": "suspects",
                "belief": "旧怀疑",
            }
        ]
        initial_path.write_text(
            json.dumps(initial, ensure_ascii=False), encoding="utf-8"
        )
        self._draft_and_review()
        outlines_path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(outlines_path.read_text(encoding="utf-8"))
        outlines[0]["retry_counts"] = {"content": 2}
        outlines_path.write_text(
            json.dumps(outlines, ensure_ascii=False), encoding="utf-8"
        )
        (self.run_dir / "chapters/0001/outline.json").write_text(
            json.dumps(outlines[0], ensure_ascii=False), encoding="utf-8"
        )
        invalid = {
            **VALID_STATE_EVENT,
            "knowledge_changes": [
                {
                    "character_id": "protagonist",
                    "fact_id": "new-fact",
                    "state": "knows",
                    "belief": "新事实",
                    "supersedes_fact_ids": ["missing-fact"],
                    "change": "确认新事实",
                    "source_evidence": "甲乙丙丁戊",
                }
            ],
        }
        with self.assertRaisesRegex(ChapterServiceError, "知识状态不存在"):
            extract_state(
                self.root,
                "demo-run",
                1,
                self._fixture(
                    "unknown-superseded-fact.json",
                    json.dumps(invalid, ensure_ascii=False),
                ),
            )

        first_prompt = (
            self.run_dir / "chapters/0001/state.prompt.v1.md"
        ).read_text(encoding="utf-8")
        self.assertIn("允许引用的活动状态 ID", first_prompt)
        self.assertIn('"known-fact"', first_prompt)

        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["status"], "state_failed")
        self.assertEqual(outlines[0]["state_failure_kind"], "content")
        self.assertFalse((self.run_dir / "state/events.jsonl").exists())
        self.assertFalse((self.run_dir / "chapters/0001/state-event.json").exists())

        valid = {
            **invalid,
            "knowledge_changes": [
                {
                    **invalid["knowledge_changes"][0],
                    "supersedes_fact_ids": ["known-fact"],
                }
            ],
        }
        event = extract_state(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "valid-superseded-fact.json", json.dumps(valid, ensure_ascii=False)
            ),
        )
        self.assertEqual(event["knowledge_changes"][0]["fact_id"], "new-fact")
        retry_prompt = (
            self.run_dir / "chapters/0001/state.prompt.v2.md"
        ).read_text(encoding="utf-8")
        self.assertIn("要淘汰的知识状态不存在", retry_prompt)
        self.assertIn('"knowledge_fact_ids_by_character"', retry_prompt)
        self.assertIn('"known-fact"', retry_prompt)
        self.assertIn("只能引用‘允许引用的活动状态 ID’区段", retry_prompt)
        repair_context = retry_prompt.split(
            "# 上次状态提取失败修复信息\n\n", 1
        )[1].split("\n\n# ", 1)[0]
        self.assertIn('"previous_output_without_source_evidence"', repair_context)
        self.assertIn('"fact_id": "new-fact"', repair_context)
        self.assertNotIn('"source_evidence"', repair_context)
        self.assertEqual(retry_prompt.count('"knowledge_fact_ids_by_character"'), 1)
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["retry_counts"]["state_content"], 1)
        self.assertEqual(outlines[0]["retry_counts"]["content"], 2)

    def test_invalid_state_json_moves_to_state_failed(self) -> None:
        self._draft_and_review()
        with self.assertRaisesRegex(ChapterServiceError, "有效 JSON"):
            extract_state(
                self.root,
                "demo-run",
                1,
                self._fixture("invalid-state.txt", "不是 JSON"),
            )
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["status"], "state_failed")

    def test_state_change_requires_exact_draft_evidence(self) -> None:
        self._draft_and_review()
        state = {**VALID_STATE_EVENT, "cultivation_changes": [{"change": "提升"}]}
        with self.assertRaisesRegex(ChapterServiceError, "source_evidence"):
            extract_state(
                self.root,
                "demo-run",
                1,
                self._fixture("missing-evidence.json", json.dumps(state, ensure_ascii=False)),
            )

    def test_state_change_requires_nonempty_change_description(self) -> None:
        self._draft_and_review()
        state = {
            **VALID_STATE_EVENT,
            "cultivation_changes": [
                {"change": "", "source_evidence": "甲乙丙丁戊"}
            ],
        }
        with self.assertRaisesRegex(ChapterServiceError, "缺少 change"):
            extract_state(
                self.root,
                "demo-run",
                1,
                self._fixture(
                    "empty-change.json", json.dumps(state, ensure_ascii=False)
                ),
            )

    def test_state_evidence_must_exist_in_final_draft(self) -> None:
        self._draft_and_review()
        state = {
            **VALID_STATE_EVENT,
            "resource_changes": [
                {"change": "获得资源", "source_evidence": "正文里不存在的句子"}
            ],
        }
        with self.assertRaisesRegex(ChapterServiceError, "不存在于 final 正文"):
            extract_state(
                self.root,
                "demo-run",
                1,
                self._fixture("wrong-evidence.json", json.dumps(state, ensure_ascii=False)),
            )

    def test_state_evidence_accepts_exact_quote_ignoring_whitespace(self) -> None:
        self._draft_and_review("甲乙 丙丁戊")
        state = {
            **VALID_STATE_EVENT,
            "entity_changes": [
                {"change": "状态变化", "source_evidence": "甲乙丙丁戊"}
            ],
        }
        event = extract_state(
            self.root,
            "demo-run",
            1,
            self._fixture("valid-evidence.json", json.dumps(state, ensure_ascii=False)),
        )
        self.assertEqual(event["event_id"], "chapter-0001")
        self.assertEqual(len(event["source_sha256"]), 64)

    def test_status_reports_pending_outline(self) -> None:
        status = get_run_status(self.root, "demo-run")
        self.assertEqual(status["last_committed_chapter"], 0)
        self.assertEqual(status["chapter_status_counts"], {"outline_ready": 1})
        self.assertFalse(status["commit_recovery_pending"])

    def test_resume_completes_prepared_commit_journal(self) -> None:
        self._draft_and_review()
        event = extract_state(
            self.root,
            "demo-run",
            1,
            self._fixture("state.json", json.dumps(VALID_STATE_EVENT)),
        )
        journal = {
            "journal_version": "1.0",
            "chapter": 1,
            "event": event,
            "created_at": "2026-07-19T00:00:00+00:00",
        }
        (self.run_dir / "logs/commit-journal.json").write_text(
            json.dumps(journal, ensure_ascii=False), encoding="utf-8"
        )

        result = resume_run(self.root, "demo-run")
        self.assertEqual(result["action"], "commit_recovered")
        self.assertEqual(result["run"]["last_committed_chapter"], 1)
        self.assertFalse((self.run_dir / "logs/commit-journal.json").exists())

    def test_resume_is_noop_without_journal(self) -> None:
        result = resume_run(self.root, "demo-run")
        self.assertEqual(result, {"action": "none", "last_committed_chapter": 0})

    def test_provider_failure_moves_draft_to_retryable_state(self) -> None:
        class FailingProvider:
            def generate(self, request: GenerationRequest):
                raise ProviderError("模拟提供方失败")

        with self.assertRaisesRegex(ChapterServiceError, "模拟提供方失败"):
            draft_chapter(self.root, "demo-run", 1, FailingProvider())
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["status"], "draft_failed_provider")

    def test_resume_recovers_stranded_drafting_state(self) -> None:
        path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(path.read_text(encoding="utf-8"))
        outlines[0]["status"] = "drafting"
        path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")

        result = resume_run(self.root, "demo-run")
        self.assertEqual(result["action"], "incomplete_tasks_recovered")
        self.assertEqual(result["draft_chapters"], [1])

    def test_overlong_repair_uses_targeted_compression(self) -> None:
        first = draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "overlong.md",
                "# 第 1 章：测试章\n甲乙丙丁戊己庚辛壬癸\n",
            ),
        )
        self.assertEqual(first["outline"]["status"], "draft_failed_length")

        result = repair_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("repaired.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        self.assertEqual(result["outline"]["status"], "draft_quality_pending")
        self.assertEqual(result["outline"]["retry_counts"]["content"], 1)
        self.assertTrue((self.run_dir / "chapters/0001/draft.v2.md").is_file())
        repair_prompt = (
            self.run_dir / "chapters/0001/draft.prompt.v2.md"
        ).read_text(encoding="utf-8")
        self.assertIn("targeted_compression", repair_prompt)
        self.assertIn("只处理失败字段对应的段落", repair_prompt)
        self.assertIn("不改人物名、既有事实、章节结构", repair_prompt)
        reviewed = self._pass_quality_review("repair-review.json")
        self.assertEqual(reviewed["outline"]["status"], "draft_passed")

    def test_quality_repair_prompt_is_limited_to_failed_fields(self) -> None:
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("quality-draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture(
                "quality-failure.json",
                json.dumps(
                    {**VALID_REVIEW, "cultivation_consistent": False},
                    ensure_ascii=False,
                ),
            ),
        )
        repair_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("quality-repaired.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        prompt = (self.run_dir / "chapters/0001/draft.prompt.v2.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("rewrite_quality", prompt)
        self.assertIn("latest_checks.quality.quality_failures", prompt)
        self.assertIn("cultivation_consistent", prompt)
        self.assertIn("保持其他段落原文不变", prompt)

    def test_severely_short_draft_uses_rewrite_mode(self) -> None:
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("short.md", "# 第 1 章：测试章\n甲乙\n"),
        )
        repair_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("rewritten.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        prompt = (self.run_dir / "chapters/0001/draft.prompt.v2.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("rewrite_short", prompt)

    def test_content_retry_limit_pauses_run(self) -> None:
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["retry"]["content"] = 1
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")

        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("short.md", "# 第 1 章：测试章\n甲乙\n"),
        )
        repair_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("still-short.md", "# 第 1 章：测试章\n甲乙\n"),
        )
        with self.assertRaisesRegex(ChapterServiceError, "达到上限"):
            repair_chapter(
                self.root,
                "demo-run",
                1,
                self._fixture("unused.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
            )
        paused = json.loads(run_path.read_text(encoding="utf-8"))
        self.assertEqual(paused["status"], "paused")
        self.assertIn("达到上限", paused["pause_reason"])

    def test_invalid_state_can_be_retried_with_new_version(self) -> None:
        self._draft_and_review()
        final_path = self.run_dir / "chapters/0001/draft.final.md"
        final_before = final_path.read_text(encoding="utf-8")
        with self.assertRaises(ChapterServiceError):
            extract_state(
                self.root,
                "demo-run",
                1,
                self._fixture("bad-state.txt", "bad"),
            )
        event = extract_state(
            self.root,
            "demo-run",
            1,
            self._fixture("good-state.json", json.dumps(VALID_STATE_EVENT)),
        )
        self.assertEqual(event["chapter"], 1)
        self.assertTrue((self.run_dir / "chapters/0001/state.raw.v2.json").exists())
        self.assertEqual(final_path.read_text(encoding="utf-8"), final_before)
        self.assertFalse((self.run_dir / "chapters/0001/draft.v2.md").exists())
        retry_prompt = (
            self.run_dir / "chapters/0001/state.prompt.v2.md"
        ).read_text(encoding="utf-8")
        self.assertIn("上次状态提取失败修复信息", retry_prompt)
        self.assertIn("不是有效 JSON", retry_prompt)
        self.assertIn('"invalid_json_excerpt": "bad"', retry_prompt)
        self.assertIn('"verbatim_paragraph_catalog"', retry_prompt)
        self.assertIn("甲乙丙丁戊", retry_prompt)
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["retry_counts"]["state_format"], 1)

    def test_long_invalid_state_json_uses_bounded_retry_excerpt(self) -> None:
        self._draft_and_review()
        invalid = "HEAD" + "x" * 5000 + "TAIL"
        with self.assertRaisesRegex(ChapterServiceError, "有效 JSON"):
            extract_state(
                self.root,
                "demo-run",
                1,
                self._fixture("long-invalid-state.txt", invalid),
            )
        extract_state(
            self.root,
            "demo-run",
            1,
            self._fixture("valid-state.json", json.dumps(VALID_STATE_EVENT)),
        )
        retry_prompt = (
            self.run_dir / "chapters/0001/state.prompt.v2.md"
        ).read_text(encoding="utf-8")
        repair_context = retry_prompt.split(
            "# 上次状态提取失败修复信息\n\n", 1
        )[1].split("\n\n# ", 1)[0]
        self.assertIn("HEAD", repair_context)
        self.assertIn("TAIL", repair_context)
        self.assertIn("...<truncated>...", repair_context)
        self.assertIn('"original_character_count": 5008', repair_context)
        self.assertNotIn("x" * 2001, repair_context)

    def test_state_provider_failure_is_retryable(self) -> None:
        class FailingProvider:
            def generate(self, request: GenerationRequest):
                raise ProviderError("状态提供方失败")

        self._draft_and_review()
        with self.assertRaisesRegex(ChapterServiceError, "状态提供方失败"):
            extract_state(self.root, "demo-run", 1, FailingProvider())
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["status"], "state_failed")
        self.assertEqual(outlines[0]["state_failure_kind"], "transport")

        extract_state(
            self.root,
            "demo-run",
            1,
            self._fixture("valid-after-transport.json", json.dumps(VALID_STATE_EVENT)),
        )
        retry_prompt = (
            self.run_dir / "chapters/0001/state.prompt.v1.md"
        ).read_text(encoding="utf-8")
        self.assertNotIn("上次状态提取失败修复信息", retry_prompt)
        self.assertNotIn('"verbatim_paragraph_catalog"', retry_prompt)
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["retry_counts"]["state_transport"], 1)

    def test_resume_recovers_stranded_state_extraction(self) -> None:
        path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(path.read_text(encoding="utf-8"))
        outlines[0]["status"] = "state_extracting"
        path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")

        result = resume_run(self.root, "demo-run")
        self.assertEqual(result["action"], "incomplete_tasks_recovered")
        self.assertEqual(result["state_chapters"], [1])


if __name__ == "__main__":
    unittest.main()
