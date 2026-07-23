from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.config import init_run
from tools.novel_runner.plan_import import PlanImportError, import_plan
from tests.master_plan_support import install_approved_master_plan


def story_unit() -> dict[str, object]:
    return {
        "unit_id": "unit-0001",
        "chapter_range": [1, 10],
        "goal": "完成一次有代价的修炼任务",
        "entry_state": [],
        "closing_state": ["取得阶段结果"],
        "main_obstacle": "资源和规则同时受限",
        "progression_change": ["确认当前能力边界"],
        "resource_change": ["消耗任务资源"],
        "relationship_change": ["形成新的合作义务"],
        "comedy_plan": ["性格反差", "信息差", "规则错位"],
        "required_setback": "中段失去一次机会",
        "required_payoff": "阶段目标有可见结果",
        "must_not_resolve": ["长期修炼限制"],
        "beats": ["接取任务", "遭遇受挫", "完成阶段目标"],
        "status": "planned",
    }


def chapter_outline(number: int) -> dict[str, object]:
    mechanisms = ["性格反差", "信息差", "规则错位", "行动连锁"]
    required_outcomes = [f"完成第{number}章行动"]
    closing_state = [f"第{number}章形成可承接结果"]
    if number == 5:
        required_outcomes.append("中段失去一次机会")
    if number == 10:
        required_outcomes.append("阶段目标有可见结果")
        closing_state.append("取得阶段结果")
    return {
        "chapter_id": f"chapter-{number:04d}",
        "number": number,
        "title": f"计划章{number}",
        "story_unit_id": "unit-0001",
        "status": "outline_ready",
        "target_length": {"min": 2000, "max": 3000},
        "intent": "推进当前修炼任务",
        "opening_state": [],
        "required_outcomes": required_outcomes,
        "forbidden_outcomes": ["无代价突破"],
        "progression_payoff": "修炼认知发生变化",
        "comedy_mechanism": mechanisms[(number - 1) % len(mechanisms)],
        "comedy_payoff": "笑点迫使角色调整行动",
        "cost_or_aftereffect": "消耗时间并保留限制",
        "closing_state": closing_state,
        "next_chapter_input": ["继续处理行动后果"],
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


class PlanImportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.run_dir = init_run(self.root, "import-run")
        self.payload = {
            "schema_version": "1.0",
            "story_units": [story_unit()],
            "chapter_outlines": [chapter_outline(number) for number in range(1, 11)],
        }
        install_approved_master_plan(
            self.root,
            "import-run",
            [("unit-0001", 1, 10)],
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _source(self, content: str, suffix: str = ".json") -> Path:
        path = self.root / f"plan{suffix}"
        path.write_text(content, encoding="utf-8")
        return path

    def test_imports_valid_json_without_losing_source(self) -> None:
        source = self._source(json.dumps(self.payload, ensure_ascii=False))
        result = import_plan(self.root, "import-run", source)

        self.assertEqual(result["story_unit_count"], 1)
        self.assertEqual(result["chapter_count"], 10)
        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(run["status"], "ready")
        self.assertEqual(run["current_story_unit"], "unit-0001")
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(len(outlines), 10)
        self.assertTrue((self.run_dir / "planning/import-source.md").is_file())

    def test_accepts_one_machine_json_block_inside_markdown(self) -> None:
        content = (
            "# 人工章纲\n\n```json\n"
            + json.dumps(self.payload, ensure_ascii=False)
            + "\n```\n"
        )
        result = import_plan(self.root, "import-run", self._source(content, ".md"))
        self.assertEqual(result["chapter_count"], 10)

    def test_rejects_incomplete_outline_without_partial_write(self) -> None:
        self.payload["chapter_outlines"] = self.payload["chapter_outlines"][:-1]
        source = self._source(json.dumps(self.payload, ensure_ascii=False))
        with self.assertRaisesRegex(PlanImportError, "章纲范围不完整"):
            import_plan(self.root, "import-run", source)

        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(outlines, [])

    def test_allows_story_unit_only_for_later_batch_planning(self) -> None:
        self.payload["chapter_outlines"] = []
        source = self._source(json.dumps(self.payload, ensure_ascii=False))

        result = import_plan(self.root, "import-run", source)

        self.assertEqual(result["chapter_count"], 0)
        run = json.loads((self.run_dir / "run.json").read_text(encoding="utf-8"))
        self.assertEqual(run["status"], "planning")
        self.assertEqual(run["current_story_unit"], "unit-0001")

    def test_rejects_story_unit_range_not_in_approved_master_plan(self) -> None:
        self.payload["story_units"][0]["chapter_range"] = [1, 12]
        source = self._source(json.dumps(self.payload, ensure_ascii=False))

        with self.assertRaisesRegex(PlanImportError, "范围.*不一致"):
            import_plan(self.root, "import-run", source)

    def test_rejects_story_unit_id_not_in_approved_master_plan(self) -> None:
        self.payload["story_units"][0]["unit_id"] = "unit-9999"
        for outline in self.payload["chapter_outlines"]:
            outline["story_unit_id"] = "unit-9999"
        source = self._source(json.dumps(self.payload, ensure_ascii=False))

        with self.assertRaisesRegex(PlanImportError, "不在已批准全书总纲"):
            import_plan(self.root, "import-run", source)

    def test_draft_master_plan_blocks_import_without_writing(self) -> None:
        plan_path = self.run_dir / "config/master-plan.json"
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        plan["approval"] = {
            "status": "draft",
            "approved_at": None,
            "content_sha256": None,
        }
        plan_path.write_text(json.dumps(plan, ensure_ascii=False), encoding="utf-8")
        source = self._source(json.dumps(self.payload, ensure_ascii=False))

        with self.assertRaisesRegex(PlanImportError, "人工执行 approve-master-plan"):
            import_plan(self.root, "import-run", source)

        self.assertEqual(
            json.loads(
                (self.run_dir / "planning/story-units.json").read_text(
                    encoding="utf-8"
                )
            ),
            [],
        )

    def test_allows_complete_first_batch_for_dynamic_later_planning(self) -> None:
        self.payload["chapter_outlines"] = self.payload["chapter_outlines"][:4]
        source = self._source(json.dumps(self.payload, ensure_ascii=False))

        result = import_plan(self.root, "import-run", source)

        self.assertEqual(result["chapter_count"], 4)
        outlines = json.loads(
            (self.run_dir / "planning/chapter-outlines.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual([item["number"] for item in outlines], list(range(1, 5)))

    def test_rejects_three_identical_comedy_mechanisms(self) -> None:
        for outline in self.payload["chapter_outlines"][:3]:
            outline["comedy_mechanism"] = "同一种误会"
        source = self._source(json.dumps(self.payload, ensure_ascii=False))
        with self.assertRaisesRegex(PlanImportError, "喜剧轮换无效"):
            import_plan(self.root, "import-run", source)

    def test_rejects_complete_unit_without_final_payoff_mapping(self) -> None:
        self.payload["chapter_outlines"][-1]["required_outcomes"] = ["其他结果"]
        source = self._source(json.dumps(self.payload, ensure_ascii=False))
        with self.assertRaisesRegex(PlanImportError, "阶段兑现"):
            import_plan(self.root, "import-run", source)

    def test_rejects_complete_unit_without_setback_mapping(self) -> None:
        self.payload["chapter_outlines"][4]["required_outcomes"] = ["其他结果"]
        source = self._source(json.dumps(self.payload, ensure_ascii=False))
        with self.assertRaisesRegex(PlanImportError, "真实受挫"):
            import_plan(self.root, "import-run", source)

    def test_refuses_reimport_after_chapter_work_has_started(self) -> None:
        outlines = [chapter_outline(number) for number in range(1, 11)]
        outlines[0]["status"] = "drafting"
        (self.run_dir / "planning/chapter-outlines.json").write_text(
            json.dumps(outlines, ensure_ascii=False), encoding="utf-8"
        )
        source = self._source(json.dumps(self.payload, ensure_ascii=False))
        with self.assertRaisesRegex(PlanImportError, "已开始生成"):
            import_plan(self.root, "import-run", source)


if __name__ == "__main__":
    unittest.main()
