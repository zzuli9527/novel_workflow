from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.config import init_run
from tools.novel_runner.provider import GenerationRequest, GenerationResponse
from tools.novel_runner.state_store import load_events
from tools.novel_runner.unit_runner import run_unit
from tools.novel_runner.wordcount import count_body_characters


class LongWorkloadProvider:
    def __init__(self) -> None:
        self.expected_lengths: dict[int, int] = {}

    @staticmethod
    def _markers(chapter: int) -> tuple[str, str, str, str]:
        return (
            f"第{chapter}章修炼推进完成",
            f"第{chapter}章喜剧因果生效",
            f"第{chapter}章代价仍然存在",
            f"第{chapter}章末角色决定继续行动",
        )

    def _draft(self, chapter: int) -> str:
        progression, comedy, consequence, hook = self._markers(chapter)
        target = 2050 + (chapter % 5) * 75
        opening = f"{progression}。{comedy}。{consequence}。"
        closing = f"{hook}。"
        filler: list[str] = []
        index = 1
        while count_body_characters(opening + "".join(filler) + closing) < target:
            filler.append(
                f"角色完成第{chapter}章第{index}次灵气运转，石台第{index}道刻痕亮起，"
                f"同伴根据第{index}个现场变化调整阵位，行动留下可追踪结果。"
            )
            index += 1
        filler_text = "".join(filler)
        body = opening + filler_text + closing
        while count_body_characters(body) > target:
            filler_text = filler_text[:-1]
            body = opening + filler_text + closing
        self.expected_lengths[chapter] = count_body_characters(body)
        return f"# 第 {chapter} 章：长压测{chapter}\n\n{opening}\n{filler_text}\n{closing}\n"

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        chapter = request.metadata.get("chapter")
        if request.task in {
            "draft_chapter",
            "repair_chapter",
            "review_chapter",
            "extract_state",
        } and not isinstance(chapter, int):
            raise AssertionError("chapter metadata missing")

        if request.task in {"draft_chapter", "repair_chapter"}:
            text = self._draft(chapter)
        elif request.task == "review_chapter":
            progression, _, _, _ = self._markers(chapter)
            text = json.dumps(
                {
                    "required_outcomes": [
                        {
                            "index": 0,
                            "passed": True,
                            "source_evidence": progression,
                        }
                    ],
                    "forbidden_outcomes": [
                        {"index": 0, "appeared": False, "source_evidence": ""}
                    ],
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
                },
                ensure_ascii=False,
            )
        elif request.task == "extract_state":
            progression, comedy, consequence, hook = self._markers(chapter)
            text = json.dumps(
                {
                    "entity_changes": [],
                    "relationship_changes": [],
                    "cultivation_changes": [
                        {
                            "subject_id": "protagonist",
                            "kind": "progress",
                            "stage_after": "炼气初阶",
                            "change": progression,
                            "source_evidence": progression,
                        }
                    ],
                    "resource_changes": [],
                    "knowledge_changes": [],
                    "thread_changes": [
                        {"change": hook, "source_evidence": hook}
                    ],
                    "comedy_changes": [
                        {"change": comedy, "source_evidence": comedy}
                    ],
                    "new_constraints": [
                        {"change": consequence, "source_evidence": consequence}
                    ],
                    "resolved_constraints": [],
                    "next_chapter_inputs": [{"input": hook}],
                    "deviations": [],
                },
                ensure_ascii=False,
            )
        elif request.task == "build_ledger":
            end = request.metadata["end_chapter"]
            text = json.dumps(
                {
                    "must_read_next": [
                        f"承接第{end}章结束状态",
                        "继续保持修炼限制",
                        "下一批切换喜剧机制",
                    ],
                    "active_progression": [
                        {
                            "subject_id": "protagonist",
                            "stage": "炼气初阶",
                            "limits": [],
                        }
                    ],
                    "active_resources": [],
                    "active_relationships": [],
                    "active_knowledge_gaps": [],
                    "active_threads": ["继续当前行动"],
                    "comedy_callbacks": ["允许升级前批回调"],
                    "avoid_repeating": ["暂停上一批主要笑点"],
                    "archived": [],
                    "next_batch_adjustments": ["切换场景和喜剧机制"],
                },
                ensure_ascii=False,
            )
        else:
            raise AssertionError(request.task)
        return GenerationResponse(
            text=text,
            provider="long-workload",
            model="fixture-long-v1",
            usage={"output_characters": len(text)},
        )


class LongWorkloadTests(unittest.TestCase):
    def test_twelve_chapters_keep_real_length_and_state_chain(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = root / "workflow"
            workflow.mkdir()
            (workflow / "04-draft.md").write_text("# 正文规则\n", encoding="utf-8")
            (workflow / "05-update-state.md").write_text("# 状态规则\n", encoding="utf-8")
            run_dir = init_run(root, "long-run")
            (run_dir / "config/initial-state.json").write_text(
                json.dumps(
                    {
                        "schema_version": "1.0",
                        "cultivation": [
                            {
                                "subject_id": "protagonist",
                                "stage": "炼气初阶",
                                "abilities": [],
                                "injuries": [],
                                "limits": [],
                            }
                        ],
                        "resources": [],
                        "knowledge": [],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            mechanisms = ["性格反差", "信息差", "规则错位", "行动连锁"]
            units = [
                {
                    "unit_id": "unit-long-001",
                    "chapter_range": [1, 12],
                    "goal": "完成一次修仙搞笑阶段推进",
                    "status": "planned",
                }
            ]
            outlines = []
            for chapter in range(1, 13):
                progression = f"第{chapter}章修炼推进完成"
                outlines.append(
                    {
                        "chapter_id": f"chapter-{chapter:04d}",
                        "number": chapter,
                        "title": f"长压测{chapter}",
                        "story_unit_id": "unit-long-001",
                        "status": "outline_ready",
                        "target_length": {"min": 2000, "max": 3000},
                        "intent": "推进修炼并完成喜剧因果",
                        "opening_state": [],
                        "required_outcomes": [progression],
                        "forbidden_outcomes": ["无代价突破"],
                        "progression_payoff": progression,
                        "comedy_mechanism": mechanisms[(chapter - 1) % len(mechanisms)],
                        "comedy_payoff": "喜剧改变角色行动",
                        "cost_or_aftereffect": f"第{chapter}章代价仍然存在",
                        "closing_state": [f"第{chapter}章形成可承接结果"],
                        "next_chapter_input": [f"承接第{chapter}章末行动"],
                        "scenes": [
                            {
                                "scene_id": f"chapter-{chapter:04d}-scene-1",
                                "intent": "建立修炼问题",
                                "target_length": 1000,
                                "required_outcomes": [],
                            },
                            {
                                "scene_id": f"chapter-{chapter:04d}-scene-2",
                                "intent": "完成行动并保留代价",
                                "target_length": 1150,
                                "required_outcomes": [progression],
                            },
                        ],
                        "writability": {
                            "is_writable": True,
                            "estimated_length": 2150,
                            "risks": [],
                        },
                    }
                )
            (run_dir / "planning/story-units.json").write_text(
                json.dumps(units, ensure_ascii=False), encoding="utf-8"
            )
            (run_dir / "planning/chapter-outlines.json").write_text(
                json.dumps(outlines, ensure_ascii=False), encoding="utf-8"
            )

            provider = LongWorkloadProvider()
            report = run_unit(root, "long-run", "unit-long-001", provider)

            self.assertEqual(report["status"], "completed")
            self.assertEqual(report["committed_chapters"], list(range(1, 13)))
            self.assertEqual(report["batches"], [[1, 4], [5, 8], [9, 12]])
            total_length = 0
            for chapter in range(1, 13):
                checks = json.loads(
                    (run_dir / f"chapters/{chapter:04d}/checks.json").read_text(
                        encoding="utf-8"
                    )
                )
                actual = checks["actual_length"]
                self.assertTrue(2000 <= actual <= 3000)
                self.assertEqual(checks["quality_status"], "draft_passed")
                total_length += actual
            self.assertGreaterEqual(total_length, 24000)
            self.assertEqual(len(load_events(run_dir / "state/events.jsonl")), 12)
            final_snapshot = json.loads(
                (run_dir / "state/snapshots/chapter-0012.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(len(final_snapshot["event_ids"]), 12)
            self.assertEqual(len(report["ledgers"]), 3)
            self.assertEqual(report["verdict"], "通过")
            review = json.loads(
                (run_dir / "reports/story-unit-review-unit-long-001.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(review["metrics"]["length_target_pass_count"], 12)
            self.assertEqual(review["metrics"]["state_event_count"], 12)
            self.assertEqual(review["metrics"]["ledger_compression"]["ledger_count"], 3)
            self.assertEqual(review["metrics"]["api"]["calls"], 39)
            chapter_five_prompt = (
                run_dir / "chapters/0005/draft.prompt.v1.md"
            ).read_text(encoding="utf-8")
            self.assertIn("继续保持修炼限制", chapter_five_prompt)
            self.assertNotIn('"event_ids"', chapter_five_prompt)


if __name__ == "__main__":
    unittest.main()
