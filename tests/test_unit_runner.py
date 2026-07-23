from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.config import init_run
from tools.novel_runner.chapter_service import get_run_status, resume_run
from tools.novel_runner.provider import (
    GenerationRequest,
    GenerationResponse,
    ProviderError,
    TextProvider,
)
from tools.novel_runner.run_archive import archive_run
from tools.novel_runner.unit_runner import (
    UnitRunnerError,
    partition_chapters,
    run_unit,
)
from tests.master_plan_support import install_approved_master_plan
from tools.novel_runner.master_plan import default_master_plan
from tools.novel_runner.storage import atomic_write_json


EMPTY_STATE = {
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

LEDGER = {
    "must_read_next": ["继续当前行动"],
    "active_progression": [],
    "active_resources": [],
    "active_relationships": [],
    "active_knowledge_gaps": [],
    "active_threads": [],
    "comedy_callbacks": [],
    "avoid_repeating": [],
    "archived": [],
    "next_batch_adjustments": [],
}

REVIEW = {
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


def make_outline(number: int) -> dict[str, object]:
    mechanisms = ["性格反差", "性格反差", "规则错位", "规则错位"]
    return {
        "chapter_id": f"chapter-{number:04d}",
        "number": number,
        "title": f"测试{number}",
        "story_unit_id": "unit-0001",
        "status": "outline_ready",
        "target_length": {"min": 5, "max": 7},
        "intent": "推进当前行动",
        "opening_state": [],
        "required_outcomes": [],
        "forbidden_outcomes": [],
        "progression_payoff": "获得修炼信息",
        "comedy_mechanism": mechanisms[(number - 1) % len(mechanisms)],
        "comedy_payoff": "喜剧影响行动",
        "cost_or_aftereffect": "消耗时间",
        "closing_state": [f"第{number}章行动完成"],
        "next_chapter_input": ["继续当前行动"],
        "scenes": [
            {
                "scene_id": f"chapter-{number:04d}-scene-1",
                "intent": "建立问题",
                "target_length": 2,
                "required_outcomes": [],
            },
            {
                "scene_id": f"chapter-{number:04d}-scene-2",
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


class ScriptedProvider:
    def __init__(
        self,
        fail_chapter: int | None = None,
        fail_plan_start: int | None = None,
    ) -> None:
        self.fail_chapter = fail_chapter
        self.fail_plan_start = fail_plan_start
        self.calls: list[tuple[str, int | None]] = []

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        chapter = request.metadata.get("chapter")
        self.calls.append((request.task, chapter if isinstance(chapter, int) else None))
        if request.task in {"draft_chapter", "repair_chapter"}:
            assert isinstance(chapter, int)
            body = "甲乙" if chapter == self.fail_chapter else "甲乙丙丁戊"
            text = f"# 第 {chapter} 章：测试{chapter}\n{body}\n"
        elif request.task == "extract_state":
            text = json.dumps(EMPTY_STATE, ensure_ascii=False)
        elif request.task == "review_chapter":
            text = json.dumps(REVIEW, ensure_ascii=False)
        elif request.task == "build_ledger":
            text = json.dumps(LEDGER, ensure_ascii=False)
        elif request.task == "plan_chapter_batch":
            start = request.metadata["start_chapter"]
            end = request.metadata["end_chapter"]
            if start == self.fail_plan_start:
                text = "不是 JSON"
            else:
                text = json.dumps(
                    {
                        "chapter_outlines": [
                            make_outline(number) for number in range(start, end + 1)
                        ]
                    },
                    ensure_ascii=False,
                )
        else:
            raise AssertionError(request.task)
        return GenerationResponse(
            text=text,
            provider="scripted",
            model="scripted-v1",
            usage={},
        )


class PartitionTests(unittest.TestCase):
    def test_all_supported_unit_sizes_partition_into_three_to_five(self) -> None:
        for total in range(10, 21):
            batches = partition_chapters(1, total)
            self.assertEqual(sum(batch.size for batch in batches), total)
            self.assertTrue(all(3 <= batch.size <= 5 for batch in batches))
            self.assertEqual(batches[0].start, 1)
            self.assertEqual(batches[-1].end, total)

    def test_rejects_unpartitionable_short_range(self) -> None:
        with self.assertRaises(UnitRunnerError):
            partition_chapters(1, 2)


class UnitRunnerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        workflow = self.root / "workflow"
        workflow.mkdir()
        (workflow / "03-chapters.md").write_text("# 章纲规则\n", encoding="utf-8")
        (workflow / "04-draft.md").write_text("# 正文规则\n", encoding="utf-8")
        (workflow / "05-update-state.md").write_text("# 状态规则\n", encoding="utf-8")
        self.run_dir = init_run(self.root, "demo-run")

        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["length"].update(
            {"expand_from": 3, "target_min": 5, "target_max": 7, "review_over": 9}
        )
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")

        units = [
            {
                "unit_id": "unit-0001",
                "chapter_range": [1, 10],
                "status": "planned",
            }
        ]
        outlines = [make_outline(number) for number in range(1, 11)]
        (self.run_dir / "planning/story-units.json").write_text(
            json.dumps(units, ensure_ascii=False), encoding="utf-8"
        )
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

    def test_runs_ten_chapter_unit_to_completion(self) -> None:
        provider = ScriptedProvider()
        report = run_unit(self.root, "demo-run", "unit-0001", provider)

        self.assertEqual(report["status"], "completed")
        self.assertEqual(report["committed_chapters"], list(range(1, 11)))
        self.assertTrue(all(3 <= end - start + 1 <= 5 for start, end in report["batches"]))
        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(run["last_committed_chapter"], 10)
        self.assertIsNone(run["current_batch"])
        units = json.loads(
            (self.run_dir / "planning/story-units.json").read_text(encoding="utf-8")
        )
        self.assertEqual(units[0]["status"], "completed")
        self.assertEqual(len(report["ledgers"]), len(report["batches"]))
        self.assertEqual(report["verdict"], "通过")
        review = json.loads(
            (self.run_dir / report["review_path"]).read_text(encoding="utf-8")
        )
        self.assertTrue(review["archivable"])
        self.assertEqual(review["usability"], "可用")
        self.assertTrue(
            (self.run_dir / "reports/story-unit-review-unit-0001.md").is_file()
        )

    def test_draft_master_plan_blocks_unit_before_provider_call(self) -> None:
        atomic_write_json(
            self.run_dir / "config/master-plan.json",
            default_master_plan(),
        )
        provider = ScriptedProvider()

        with self.assertRaisesRegex(UnitRunnerError, "审批闸门"):
            run_unit(self.root, "demo-run", "unit-0001", provider)

        self.assertEqual(provider.calls, [])

    def test_v2_run_uses_fixed_state_and_ledger_files(self) -> None:
        v2_dir = init_run(self.root, "v2-run", storage_version="2.0")
        run_path = v2_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["length"].update(
            {"expand_from": 3, "target_min": 5, "target_max": 7, "review_over": 9}
        )
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")
        (v2_dir / "planning/story-units.json").write_text(
            json.dumps(
                [
                    {
                        "unit_id": "unit-0001",
                        "chapter_range": [1, 10],
                        "status": "planned",
                    }
                ],
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        (v2_dir / "planning/chapter-outlines.json").write_text(
            json.dumps([make_outline(number) for number in range(1, 11)], ensure_ascii=False),
            encoding="utf-8",
        )
        install_approved_master_plan(
            self.root,
            "v2-run",
            [("unit-0001", 1, 10)],
        )

        report = run_unit(self.root, "v2-run", "unit-0001", ScriptedProvider())

        self.assertEqual(report["status"], "completed")
        self.assertTrue((v2_dir / "state/events.jsonl").is_file())
        self.assertTrue((v2_dir / "state/current.json").is_file())
        self.assertTrue((v2_dir / "state/checkpoints.jsonl").is_file())
        self.assertFalse((v2_dir / "state/snapshots").exists())
        events = [
            json.loads(line)
            for line in (v2_dir / "state/events.jsonl").read_text(
                encoding="utf-8"
            ).splitlines()
            if line.strip()
        ]
        self.assertEqual([event["sequence"] for event in events], list(range(1, 11)))
        self.assertTrue(all(event.get("event_sha256") for event in events))
        current = json.loads((v2_dir / "state/current.json").read_text(encoding="utf-8"))
        self.assertEqual(current["after_chapter"], 10)
        self.assertEqual(current["last_event_sequence"], 10)
        checkpoints = (v2_dir / "state/checkpoints.jsonl").read_text(
            encoding="utf-8"
        ).splitlines()
        self.assertEqual(len([line for line in checkpoints if line.strip()]), 1)
        self.assertTrue((v2_dir / "ledgers/current.json").is_file())
        history = (v2_dir / "ledgers/history.jsonl").read_text(encoding="utf-8")
        self.assertEqual(len([line for line in history.splitlines() if line.strip()]), 3)
        self.assertTrue((v2_dir / "artifacts/unit-0001.zip").is_file())
        self.assertEqual(
            [path.name for path in (v2_dir / "chapters/0001").iterdir()],
            ["draft.final.md"],
        )
        self.assertFalse(any((v2_dir / "ledgers").glob("batch-*")))
        archived = archive_run(
            self.root, "v2-run", "unit-0001", "Xv2-storage-layout"
        )
        self.assertEqual(archived["verdict"], "通过")
        self.assertTrue(
            (
                self.root
                / "test/matrix-runs/Xv2-storage-layout/data/state/current.json"
            ).is_file()
        )
        self.assertFalse(get_run_status(self.root, "v2-run")["commit_recovery_pending"])
        self.assertEqual(
            resume_run(self.root, "v2-run"),
            {"action": "none", "last_committed_chapter": 10},
        )

    def test_retries_initial_draft_transport_failure_inside_unit(self) -> None:
        class TransientDraftProvider(ScriptedProvider):
            def __init__(self) -> None:
                super().__init__()
                self.chapter_one_attempts = 0

            def generate(self, request: GenerationRequest) -> GenerationResponse:
                chapter = request.metadata.get("chapter")
                if (
                    request.task in {"draft_chapter", "repair_chapter"}
                    and chapter == 1
                ):
                    self.calls.append((request.task, 1))
                    self.chapter_one_attempts += 1
                    if self.chapter_one_attempts == 1:
                        raise ProviderError("模拟瞬时传输失败", fallback_allowed=True)
                    return GenerationResponse(
                        text="# 第 1 章：测试1\n甲乙丙丁戊\n",
                        provider="scripted",
                        model="scripted-v1",
                        usage={},
                    )
                return super().generate(request)

        provider = TransientDraftProvider()
        report = run_unit(self.root, "demo-run", "unit-0001", provider)

        self.assertEqual(report["status"], "completed")
        self.assertEqual(
            [call for call in provider.calls if call[1] == 1][:2],
            [("draft_chapter", 1), ("repair_chapter", 1)],
        )
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["retry_counts"]["transport"], 1)
        self.assertEqual(outlines[0]["status"], "committed")

    def test_pauses_after_draft_transport_retry_budget_is_exhausted(self) -> None:
        class FailingDraftProvider(ScriptedProvider):
            def generate(self, request: GenerationRequest) -> GenerationResponse:
                chapter = request.metadata.get("chapter")
                if (
                    request.task in {"draft_chapter", "repair_chapter"}
                    and chapter == 1
                ):
                    self.calls.append((request.task, 1))
                    raise ProviderError("模拟持续传输失败", fallback_allowed=True)
                return super().generate(request)

        provider = FailingDraftProvider()
        with self.assertRaisesRegex(UnitRunnerError, "模拟持续传输失败"):
            run_unit(self.root, "demo-run", "unit-0001", provider)

        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["status"], "draft_failed_provider")
        self.assertEqual(outlines[0]["retry_counts"]["transport"], 2)
        self.assertEqual(outlines[1]["status"], "outline_ready")
        self.assertEqual(
            [call for call in provider.calls if call[1] == 1],
            [
                ("draft_chapter", 1),
                ("repair_chapter", 1),
                ("repair_chapter", 1),
            ],
        )
        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(run["status"], "paused")

    def test_soft_quality_warning_does_not_trigger_repair(self) -> None:
        class SoftWarningProvider(ScriptedProvider):
            def generate(self, request: GenerationRequest) -> GenerationResponse:
                chapter = request.metadata.get("chapter")
                if request.task == "review_chapter" and chapter == 1:
                    self.calls.append(("review_chapter", 1))
                    return GenerationResponse(
                        text=json.dumps(
                            {**REVIEW, "character_voices_distinct": False},
                            ensure_ascii=False,
                        ),
                        provider="scripted",
                        model="scripted-v1",
                        usage={},
                    )
                return super().generate(request)

        provider = SoftWarningProvider()
        report = run_unit(self.root, "demo-run", "unit-0001", provider)
        self.assertEqual(report["status"], "completed")
        self.assertEqual(report["verdict"], "有条件通过")
        review = json.loads(
            (self.run_dir / report["review_path"]).read_text(encoding="utf-8")
        )
        self.assertTrue(review["archivable"])
        self.assertEqual(review["usability"], "可用，待润色")
        self.assertNotIn("repair_chapter", [task for task, _ in provider.calls])

    def test_soft_length_warning_does_not_trigger_repair(self) -> None:
        class SoftLengthProvider(ScriptedProvider):
            def generate(self, request: GenerationRequest) -> GenerationResponse:
                chapter = request.metadata.get("chapter")
                if request.task == "draft_chapter" and chapter == 1:
                    self.calls.append(("draft_chapter", 1))
                    return GenerationResponse(
                        text="# 第 1 章：测试1\n甲乙丙丁\n",
                        provider="scripted",
                        model="scripted-v1",
                        usage={},
                    )
                return super().generate(request)

        provider = SoftLengthProvider()
        report = run_unit(self.root, "demo-run", "unit-0001", provider)
        self.assertEqual(report["status"], "completed")
        self.assertEqual(report["verdict"], "有条件通过")
        self.assertNotIn("repair_chapter", [task for task, _ in provider.calls])

    def test_hard_quality_failure_still_triggers_repair(self) -> None:
        class HardFailureProvider(ScriptedProvider):
            def __init__(self) -> None:
                super().__init__()
                self.chapter_one_reviews = 0

            def generate(self, request: GenerationRequest) -> GenerationResponse:
                chapter = request.metadata.get("chapter")
                if request.task == "review_chapter" and chapter == 1:
                    self.calls.append(("review_chapter", 1))
                    self.chapter_one_reviews += 1
                    return GenerationResponse(
                        text=json.dumps(
                            {
                                **REVIEW,
                                "cultivation_consistent": (
                                    self.chapter_one_reviews > 1
                                ),
                            },
                            ensure_ascii=False,
                        ),
                        provider="scripted",
                        model="scripted-v1",
                        usage={},
                    )
                return super().generate(request)

        provider = HardFailureProvider()
        report = run_unit(self.root, "demo-run", "unit-0001", provider)
        self.assertEqual(report["status"], "completed")
        self.assertEqual(
            [call for call in provider.calls if call == ("repair_chapter", 1)],
            [("repair_chapter", 1)],
        )

    def test_retries_state_content_failure_inside_unit(self) -> None:
        class StateRetryProvider(ScriptedProvider):
            def __init__(self) -> None:
                super().__init__()
                self.state_attempts = 0

            def generate(self, request: GenerationRequest) -> GenerationResponse:
                chapter = request.metadata.get("chapter")
                if request.task == "extract_state" and chapter == 1:
                    self.calls.append(("extract_state", 1))
                    self.state_attempts += 1
                    if self.state_attempts == 1:
                        invalid = {
                            **EMPTY_STATE,
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
                        return GenerationResponse(
                            text=json.dumps(invalid, ensure_ascii=False),
                            provider="scripted",
                            model="scripted-v1",
                            usage={},
                        )
                return super().generate(request)

        provider = StateRetryProvider()
        report = run_unit(self.root, "demo-run", "unit-0001", provider)

        self.assertEqual(report["status"], "completed")
        self.assertEqual(provider.state_attempts, 2)
        self.assertTrue((self.run_dir / "chapters/0001/state.raw.v2.json").exists())
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["retry_counts"]["state_content"], 1)
        self.assertEqual(outlines[0]["status"], "committed")
        retry_prompt = (
            self.run_dir / "chapters/0001/state.prompt.v2.md"
        ).read_text(encoding="utf-8")
        repair_context = retry_prompt.split(
            "# 上次状态提取失败修复信息\n\n", 1
        )[1].split("\n\n# ", 1)[0]
        self.assertIn('"previous_output_without_source_evidence"', repair_context)
        self.assertIn('"fact_id": "new-fact"', repair_context)
        self.assertNotIn('"source_evidence"', repair_context)
        self.assertEqual(retry_prompt.count('"knowledge_fact_ids_by_character"'), 1)

    def test_retries_state_transport_failure_inside_unit(self) -> None:
        class StateTransportRetryProvider(ScriptedProvider):
            def __init__(self) -> None:
                super().__init__()
                self.state_attempts = 0

            def generate(self, request: GenerationRequest) -> GenerationResponse:
                chapter = request.metadata.get("chapter")
                if request.task == "extract_state" and chapter == 1:
                    self.calls.append(("extract_state", 1))
                    self.state_attempts += 1
                    if self.state_attempts == 1:
                        raise ProviderError(
                            "模拟瞬时状态传输失败", fallback_allowed=True
                        )
                    return GenerationResponse(
                        text=json.dumps(EMPTY_STATE, ensure_ascii=False),
                        provider="scripted",
                        model="scripted-v1",
                        usage={},
                    )
                return super().generate(request)

        provider = StateTransportRetryProvider()
        report = run_unit(self.root, "demo-run", "unit-0001", provider)

        self.assertEqual(report["status"], "completed")
        self.assertEqual(provider.state_attempts, 2)
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["retry_counts"]["state_transport"], 1)
        self.assertEqual(outlines[0]["status"], "committed")

    def test_repeated_state_content_failure_pauses_unit(self) -> None:
        class RepeatedInvalidStateProvider(ScriptedProvider):
            def __init__(self) -> None:
                super().__init__()
                self.state_attempts = 0

            def generate(self, request: GenerationRequest) -> GenerationResponse:
                chapter = request.metadata.get("chapter")
                if request.task == "extract_state" and chapter == 1:
                    self.calls.append(("extract_state", 1))
                    self.state_attempts += 1
                    invalid = {
                        **EMPTY_STATE,
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
                    return GenerationResponse(
                        text=json.dumps(invalid, ensure_ascii=False),
                        provider="scripted",
                        model="scripted-v1",
                        usage={},
                    )
                return super().generate(request)

        provider = RepeatedInvalidStateProvider()
        with self.assertRaisesRegex(UnitRunnerError, "知识状态不存在"):
            run_unit(self.root, "demo-run", "unit-0001", provider)

        self.assertEqual(provider.state_attempts, 3)
        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(run["status"], "paused")
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["status"], "state_failed")
        self.assertEqual(outlines[0]["retry_counts"]["state_content"], 2)
        self.assertEqual(outlines[1]["status"], "outline_ready")

    def test_retries_review_evidence_failure_inside_unit(self) -> None:
        outline_path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(outline_path.read_text(encoding="utf-8"))
        outlines[0]["required_outcomes"] = ["甲乙丙丁戊"]
        outline_path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")

        class ReviewRetryProvider(ScriptedProvider):
            def __init__(self) -> None:
                super().__init__()
                self.review_attempts = 0

            def generate(self, request: GenerationRequest) -> GenerationResponse:
                chapter = request.metadata.get("chapter")
                if request.task == "review_chapter" and chapter == 1:
                    self.calls.append(("review_chapter", 1))
                    self.review_attempts += 1
                    if self.review_attempts == 1:
                        return GenerationResponse(
                            text=json.dumps(
                                {
                                    **REVIEW,
                                    "required_outcomes": [
                                        {
                                            "index": 0,
                                            "passed": True,
                                            "source_evidence": "甲乙丁戊",
                                        }
                                    ],
                                },
                                ensure_ascii=False,
                            ),
                            provider="scripted",
                            model="scripted-v1",
                            usage={},
                        )
                    return GenerationResponse(
                        text=json.dumps(
                            {
                                **REVIEW,
                                "required_outcomes": [
                                    {
                                        "index": 0,
                                        "passed": True,
                                        "source_evidence": "甲乙丙丁戊",
                                    }
                                ],
                            },
                            ensure_ascii=False,
                        ),
                        provider="scripted",
                        model="scripted-v1",
                        usage={},
                    )
                return super().generate(request)

        provider = ReviewRetryProvider()
        report = run_unit(self.root, "demo-run", "unit-0001", provider)

        self.assertEqual(report["status"], "completed")
        self.assertEqual(provider.review_attempts, 2)
        self.assertTrue((self.run_dir / "chapters/0001/review.raw.v2.json").exists())
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[0]["retry_counts"]["review_format"], 1)
        self.assertEqual(outlines[0]["status"], "committed")
        retry_prompt = (
            self.run_dir / "chapters/0001/review.prompt.v2.md"
        ).read_text(encoding="utf-8")
        self.assertIn('"verbatim_paragraph_catalog"', retry_prompt)
        self.assertIn("甲乙丙丁戊", retry_prompt)

    def test_repeated_review_evidence_failure_pauses_unit(self) -> None:
        outline_path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(outline_path.read_text(encoding="utf-8"))
        outlines[0]["required_outcomes"] = ["甲乙丙丁戊"]
        outline_path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")

        class RepeatedInvalidReviewProvider(ScriptedProvider):
            def __init__(self) -> None:
                super().__init__()
                self.review_attempts = 0

            def generate(self, request: GenerationRequest) -> GenerationResponse:
                chapter = request.metadata.get("chapter")
                if request.task == "review_chapter" and chapter == 1:
                    self.calls.append(("review_chapter", 1))
                    self.review_attempts += 1
                    return GenerationResponse(
                        text=json.dumps(
                            {
                                **REVIEW,
                                "required_outcomes": [
                                    {
                                        "index": 0,
                                        "passed": True,
                                        "source_evidence": "甲乙丁戊",
                                    }
                                ],
                            },
                            ensure_ascii=False,
                        ),
                        provider="scripted",
                        model="scripted-v1",
                        usage={},
                    )
                return super().generate(request)

        provider = RepeatedInvalidReviewProvider()
        with self.assertRaisesRegex(UnitRunnerError, "证据不在正文"):
            run_unit(self.root, "demo-run", "unit-0001", provider)

        self.assertEqual(provider.review_attempts, 2)
        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(run["status"], "paused")
        outlines = json.loads(outline_path.read_text(encoding="utf-8"))
        self.assertEqual(outlines[0]["status"], "draft_quality_pending")
        self.assertEqual(outlines[0]["retry_counts"]["review_format"], 1)
        self.assertEqual(outlines[1]["status"], "outline_ready")

    def test_failure_pauses_unit_and_does_not_advance_later_chapters(self) -> None:
        provider = ScriptedProvider(fail_chapter=5)
        with self.assertRaises(UnitRunnerError):
            run_unit(self.root, "demo-run", "unit-0001", provider)

        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(run["status"], "paused")
        self.assertEqual(run["last_committed_chapter"], 4)
        self.assertEqual(run["current_batch"], "batch-0005-0007")
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines[4]["status"], "draft_failed_length")
        self.assertEqual(outlines[5]["status"], "outline_ready")
        report = json.loads(
            (self.run_dir / "reports/unit-unit-0001.json").read_text(encoding="utf-8")
        )
        self.assertEqual(report["status"], "paused")

    def test_insufficient_call_budget_blocks_before_provider_use(self) -> None:
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["budget"]["max_calls"] = 31
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")
        provider = ScriptedProvider()

        with self.assertRaisesRegex(UnitRunnerError, "调用预算不足"):
            run_unit(self.root, "demo-run", "unit-0001", provider)

        self.assertEqual(provider.calls, [])
        paused = json.loads(run_path.read_text(encoding="utf-8"))
        self.assertEqual(paused["status"], "paused")
        self.assertEqual(paused["last_committed_chapter"], 0)

    def test_pending_revision_outline_blocks_unit_start(self) -> None:
        path = self.run_dir / "planning/chapter-outlines.json"
        outlines = json.loads(path.read_text(encoding="utf-8"))
        outlines[4]["revalidation_status"] = "pending"
        path.write_text(json.dumps(outlines, ensure_ascii=False), encoding="utf-8")

        with self.assertRaisesRegex(UnitRunnerError, "尚未重验"):
            run_unit(self.root, "demo-run", "unit-0001", ScriptedProvider())

    def test_run_unit_plans_each_missing_batch_after_previous_ledger(self) -> None:
        (self.run_dir / "planning/chapter-outlines.json").write_text(
            "[]", encoding="utf-8"
        )
        provider = ScriptedProvider()

        report = run_unit(self.root, "demo-run", "unit-0001", provider)

        self.assertEqual(report["status"], "completed")
        self.assertEqual(report["planned_batches"], [[1, 4], [5, 7], [8, 10]])
        plan_calls = [task for task, _ in provider.calls if task == "plan_chapter_batch"]
        self.assertEqual(len(plan_calls), 6)
        chapter_five_prompt = (
            self.run_dir / "chapters/0005/draft.prompt.v1.md"
        ).read_text(encoding="utf-8")
        self.assertIn("继续当前行动", chapter_five_prompt)
        batch_two_plan_prompt = (
            self.run_dir
            / "planning/generated/outline-0005-0007.prompt.v1.md"
        ).read_text(encoding="utf-8")
        self.assertIn("继续当前行动", batch_two_plan_prompt)
        self.assertNotIn('"event_ids"', batch_two_plan_prompt)

    def test_failed_next_batch_plan_pauses_and_can_resume(self) -> None:
        (self.run_dir / "planning/chapter-outlines.json").write_text(
            "[]", encoding="utf-8"
        )
        with self.assertRaisesRegex(UnitRunnerError, "章纲批次.*输出不是有效 JSON"):
            run_unit(
                self.root,
                "demo-run",
                "unit-0001",
                ScriptedProvider(fail_plan_start=5),
            )

        paused = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(paused["last_committed_chapter"], 4)
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(len(outlines), 4)
        self.assertTrue(all(item["status"] == "committed" for item in outlines))
        self.assertFalse((self.run_dir / "chapters/0005").exists())

        resumed = run_unit(
            self.root, "demo-run", "unit-0001", ScriptedProvider()
        )
        self.assertEqual(resumed["status"], "completed")
        self.assertEqual(resumed["planned_batches"], [[5, 7], [8, 10]])
        review = json.loads(
            (
                self.run_dir / "reports/story-unit-review-unit-0001.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(review["metrics"]["breakpoint_recovery_count"], 1)
        runtime_events = [
            json.loads(line)
            for line in (self.run_dir / "logs/events.jsonl").read_text(
                encoding="utf-8"
            ).splitlines()
            if line.strip()
        ]
        self.assertEqual(runtime_events[-1]["action"], "unit_resumed")


if __name__ == "__main__":
    unittest.main()
