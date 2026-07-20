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
        self.assertIn('"hard_range": [', prompt)

        reviewed = self._pass_quality_review()
        self.assertEqual(reviewed["outline"]["status"], "draft_passed")
        self.assertTrue((self.run_dir / "chapters/0001/draft.final.md").is_file())

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
        outlines[0]["required_outcomes"] = ["角色取得令牌"]
        outline_path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("review-retry-draft.md", "# 第 1 章：测试章\n角色取得令牌。\n"),
        )
        invalid = {
            **VALID_REVIEW,
            "required_outcomes": [
                {"index": 0, "passed": True, "source_evidence": "角色拿到了令牌"}
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
                {"index": 0, "passed": True, "source_evidence": "角色取得令牌"}
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
        self.assertIn("角色拿到了令牌", prompt)

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

    def test_quality_review_blocks_indistinguishable_character_voices(self) -> None:
        draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("draft.md", "# 第 1 章：测试章\n甲乙丙丁戊\n"),
        )
        review = {**VALID_REVIEW, "character_voices_distinct": False}
        result = review_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("voices-review.json", json.dumps(review, ensure_ascii=False)),
        )
        self.assertEqual(result["outline"]["status"], "draft_failed_quality")
        self.assertIn("character_voices_distinct", result["review"]["quality_failures"])

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

    def test_targeted_repair_creates_new_version_and_passes(self) -> None:
        first = draft_chapter(
            self.root,
            "demo-run",
            1,
            self._fixture("short.md", "# 第 1 章：测试章\n甲乙丙丁\n"),
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
        self.assertIn("targeted_expansion", repair_prompt)
        reviewed = self._pass_quality_review("repair-review.json")
        self.assertEqual(reviewed["outline"]["status"], "draft_passed")

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
        retry_prompt = (
            self.run_dir / "chapters/0001/state.prompt.v2.md"
        ).read_text(encoding="utf-8")
        self.assertIn("上次状态提取失败修复信息", retry_prompt)
        self.assertIn("不是有效 JSON", retry_prompt)
        self.assertIn('"previous_invalid_output": "bad"', retry_prompt)
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["retry_counts"]["format"], 1)

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
