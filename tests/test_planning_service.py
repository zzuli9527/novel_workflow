from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.config import init_run
from tools.novel_runner.planning_service import (
    PlanningServiceError,
    plan_chapter_batch,
    plan_story_unit,
)
from tools.novel_runner.prompt_composer import compose_batch_outline_plan_prompt
from tools.novel_runner.provider import (
    FixtureProvider,
    GenerationRequest,
    GenerationResponse,
    ProviderError,
)
from tools.novel_runner.storage import atomic_write_json


def unit_payload() -> dict[str, object]:
    return {
        "unit_id": "unit-0001",
        "chapter_range": [1, 10],
        "goal": "完成一次有代价的修炼任务",
        "entry_state": [],
        "closing_state": ["取得阶段结果"],
        "main_obstacle": "资源与规则同时受限",
        "progression_change": ["确认当前能力边界"],
        "resource_change": ["消耗任务资源"],
        "relationship_change": ["形成合作义务"],
        "comedy_plan": ["性格反差", "规则错位"],
        "required_setback": "中段失去一次机会",
        "required_payoff": "阶段目标有可见结果",
        "must_not_resolve": ["长期修炼限制"],
        "beats": ["接取任务", "遭遇受挫", "完成阶段目标"],
        "status": "planned",
    }


def outline(number: int) -> dict[str, object]:
    mechanisms = ["性格反差", "信息差", "规则错位", "行动连锁"]
    return {
        "chapter_id": f"chapter-{number:04d}",
        "number": number,
        "title": f"计划章{number}",
        "story_unit_id": "unit-0001",
        "status": "outline_ready",
        "target_length": {"min": 2000, "max": 3000},
        "intent": "推进当前修炼任务",
        "opening_state": [],
        "required_outcomes": [f"完成第{number}章行动"],
        "forbidden_outcomes": ["无代价突破"],
        "progression_payoff": "修炼认知发生变化",
        "comedy_mechanism": mechanisms[(number - 1) % len(mechanisms)],
        "comedy_payoff": "笑点迫使角色调整行动",
        "cost_or_aftereffect": "消耗时间并保留限制",
        "closing_state": [f"第{number}章行动完成"],
        "next_chapter_input": ["继续处理后果"],
        "scenes": [
            {
                "scene_id": f"chapter-{number:04d}-scene-1",
                "intent": "建立问题并采取行动",
                "target_length": 1000,
                "required_outcomes": [],
            },
            {
                "scene_id": f"chapter-{number:04d}-scene-2",
                "intent": "形成结果和后果",
                "target_length": 1150,
                "required_outcomes": [f"完成第{number}章行动"],
            },
        ],
        "writability": {
            "is_writable": True,
            "estimated_length": 2150,
            "risks": [],
        },
    }


class PlanningServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        workflow = self.root / "workflow"
        workflow.mkdir()
        (workflow / "01-expand.md").write_text("# 单元规划\n", encoding="utf-8")
        (workflow / "03-chapters.md").write_text("# 章纲规划\n", encoding="utf-8")
        (workflow / "modules.md").write_text("# 模块库\n", encoding="utf-8")
        self.run_dir = init_run(self.root, "planning-run")
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["batch"]["outline_request_chunk_size"] = 4
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _fixture(self, name: str, data: object) -> FixtureProvider:
        path = self.root / name
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        return FixtureProvider(path)

    def test_plans_story_unit_with_fixed_id_and_range(self) -> None:
        unit = unit_payload()
        result = plan_story_unit(
            self.root,
            "planning-run",
            10,
            self._fixture("unit.json", unit),
        )

        self.assertEqual(result["unit_id"], "unit-0001")
        self.assertEqual(result["chapter_range"], [1, 10])
        stored = json.loads(
            (self.run_dir / "planning/story-units.json").read_text(encoding="utf-8")
        )
        self.assertEqual(stored, [result])
        prompt = next((self.run_dir / "planning/generated").glob("story-unit-*.prompt.v1.md"))
        self.assertIn("第 1～10 章", prompt.read_text(encoding="utf-8"))

    def test_rejects_story_unit_that_changes_requested_range(self) -> None:
        unit = {**unit_payload(), "chapter_range": [1, 12]}
        with self.assertRaisesRegex(PlanningServiceError, "chapter_range"):
            plan_story_unit(
                self.root,
                "planning-run",
                10,
                self._fixture("wrong-unit.json", unit),
            )

    def test_plans_canonical_outline_batch(self) -> None:
        (self.run_dir / "planning/story-units.json").write_text(
            json.dumps([unit_payload()], ensure_ascii=False), encoding="utf-8"
        )
        response = {"chapter_outlines": [outline(number) for number in range(1, 5)]}
        result = plan_chapter_batch(
            self.root,
            "planning-run",
            "unit-0001",
            1,
            4,
            self._fixture("batch.json", response),
        )

        self.assertEqual([item["number"] for item in result], list(range(1, 5)))
        stored = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(len(stored), 4)
        prompt = next(
            (self.run_dir / "planning/generated").glob(
                "outline-0001-0004.part-0001-0004.prompt.v1.md"
            )
        )
        prompt_text = prompt.read_text(encoding="utf-8")
        self.assertIn('"target_length": 1000', prompt_text)
        self.assertIn('"required_outcomes"', prompt_text)

    def test_final_chapter_prompt_requires_literal_unit_contract_copy(self) -> None:
        prompt = compose_batch_outline_plan_prompt(
            self.root,
            self.run_dir,
            unit_payload(),
            10,
            10,
            [],
        )

        self.assertIn("逐字符复制", prompt)
        self.assertIn("禁止在前后添加 required_payoff、冒号", prompt)
        self.assertIn("不得用释义替换原句", prompt)
        self.assertIn("阶段目标有可见结果", prompt)
        self.assertIn("取得阶段结果", prompt)

    def test_accepts_only_redundant_closing_delimiters_after_json_object(self) -> None:
        (self.run_dir / "planning/story-units.json").write_text(
            json.dumps([unit_payload()], ensure_ascii=False), encoding="utf-8"
        )
        response = {"chapter_outlines": [outline(number) for number in range(1, 5)]}
        path = self.root / "extra-closing.json"
        path.write_text(
            json.dumps(response, ensure_ascii=False) + " } ] ", encoding="utf-8"
        )

        result = plan_chapter_batch(
            self.root,
            "planning-run",
            "unit-0001",
            1,
            4,
            FixtureProvider(path),
        )

        self.assertEqual([item["number"] for item in result], [1, 2, 3, 4])

    def test_rejects_second_json_object_after_valid_plan(self) -> None:
        (self.run_dir / "planning/story-units.json").write_text(
            json.dumps([unit_payload()], ensure_ascii=False), encoding="utf-8"
        )
        response = {"chapter_outlines": [outline(number) for number in range(1, 5)]}
        path = self.root / "second-object.json"
        path.write_text(
            json.dumps(response, ensure_ascii=False) + '{"extra":true}',
            encoding="utf-8",
        )

        with self.assertRaisesRegex(PlanningServiceError, "额外文本"):
            plan_chapter_batch(
                self.root,
                "planning-run",
                "unit-0001",
                1,
                4,
                FixtureProvider(path),
            )

    def test_rejects_noncanonical_batch_range(self) -> None:
        (self.run_dir / "planning/story-units.json").write_text(
            json.dumps([unit_payload()], ensure_ascii=False), encoding="utf-8"
        )
        with self.assertRaisesRegex(PlanningServiceError, "标准章纲批次"):
            plan_chapter_batch(
                self.root,
                "planning-run",
                "unit-0001",
                1,
                5,
                self._fixture("unused.json", {}),
            )

    def test_splits_outline_transport_chunk_after_gateway_524(self) -> None:
        class AdaptiveProvider:
            def __init__(self) -> None:
                self.ranges: list[tuple[int, int]] = []

            def generate(self, request: GenerationRequest) -> GenerationResponse:
                start = int(request.metadata["start_chapter"])
                end = int(request.metadata["end_chapter"])
                self.ranges.append((start, end))
                if end > start:
                    raise ProviderError(
                        "gateway timeout",
                        status_code=524,
                        fallback_allowed=True,
                    )
                return GenerationResponse(
                    text=json.dumps(
                        {"chapter_outlines": [outline(start)]},
                        ensure_ascii=False,
                    ),
                    provider="adaptive",
                    model="adaptive-v1",
                )

        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["batch"]["outline_request_chunk_size"] = 2
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")
        (self.run_dir / "planning/story-units.json").write_text(
            json.dumps([unit_payload()], ensure_ascii=False), encoding="utf-8"
        )
        provider = AdaptiveProvider()
        result = plan_chapter_batch(
            self.root,
            "planning-run",
            "unit-0001",
            1,
            4,
            provider,
        )
        self.assertEqual([item["number"] for item in result], [1, 2, 3, 4])
        self.assertEqual(
            provider.ranges,
            [(1, 2), (1, 1), (2, 2), (3, 4), (3, 3), (4, 4)],
        )

    def test_splits_outline_chunk_after_connection_transport_error(self) -> None:
        class TransportProvider:
            def __init__(self) -> None:
                self.ranges: list[tuple[int, int]] = []

            def generate(self, request: GenerationRequest) -> GenerationResponse:
                start = int(request.metadata["start_chapter"])
                end = int(request.metadata["end_chapter"])
                self.ranges.append((start, end))
                if end > start:
                    raise ProviderError(
                        "connection closed",
                        error_code="transport_error",
                        fallback_allowed=True,
                    )
                return GenerationResponse(
                    text=json.dumps(
                        {"chapter_outlines": [outline(start)]},
                        ensure_ascii=False,
                    ),
                    provider="transport",
                    model="transport-v1",
                )

        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["batch"]["outline_request_chunk_size"] = 2
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")
        (self.run_dir / "planning/story-units.json").write_text(
            json.dumps([unit_payload()], ensure_ascii=False), encoding="utf-8"
        )

        result = plan_chapter_batch(
            self.root,
            "planning-run",
            "unit-0001",
            1,
            4,
            TransportProvider(),
        )

        self.assertEqual([item["number"] for item in result], [1, 2, 3, 4])

    def test_v2_future_planning_uses_last_committed_snapshot(self) -> None:
        v2_dir = init_run(self.root, "planning-v2", storage_version="2.0")
        run_path = v2_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["last_committed_chapter"] = 4
        atomic_write_json(run_path, run)
        atomic_write_json(
            v2_dir / "state/current.json",
            {
                "after_chapter": 4,
                "event_ids": ["chapter-0004"],
                "changes": {},
                "structured_state": {},
                "next_chapter_inputs": ["continue from chapter 4"],
            },
        )

        prompt = compose_batch_outline_plan_prompt(
            self.root,
            v2_dir,
            unit_payload(),
            7,
            7,
            [outline(number) for number in range(1, 7)],
        )

        self.assertIn('"after_chapter": 4', prompt)

    def test_v2_split_batch_plans_beyond_current_snapshot(self) -> None:
        class RangeProvider:
            def __init__(self) -> None:
                self.ranges: list[tuple[int, int]] = []

            def generate(self, request: GenerationRequest) -> GenerationResponse:
                start = int(request.metadata["start_chapter"])
                end = int(request.metadata["end_chapter"])
                self.ranges.append((start, end))
                return GenerationResponse(
                    text=json.dumps(
                        {"chapter_outlines": [outline(number) for number in range(start, end + 1)]},
                        ensure_ascii=False,
                    ),
                    provider="range",
                    model="range-v1",
                )

        v2_dir = init_run(self.root, "planning-v2-split", storage_version="2.0")
        run_path = v2_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["last_committed_chapter"] = 4
        run["policies"]["batch"]["outline_request_chunk_size"] = 2
        atomic_write_json(run_path, run)
        atomic_write_json(
            v2_dir / "state/current.json",
            {
                "after_chapter": 4,
                "event_ids": ["chapter-0001", "chapter-0002", "chapter-0003", "chapter-0004"],
                "changes": {},
                "structured_state": {},
                "next_chapter_inputs": [],
            },
        )
        atomic_write_json(v2_dir / "planning/story-units.json", [unit_payload()])
        atomic_write_json(
            v2_dir / "planning/chapter-outlines.json",
            [outline(number) for number in range(1, 5)],
        )

        provider = RangeProvider()
        result = plan_chapter_batch(
            self.root,
            "planning-v2-split",
            "unit-0001",
            5,
            7,
            provider,
        )

        self.assertEqual([item["number"] for item in result], [5, 6, 7])
        self.assertEqual(provider.ranges, [(5, 6), (7, 7)])


if __name__ == "__main__":
    unittest.main()
