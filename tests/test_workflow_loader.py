from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.workflow_runtime import (
    WorkflowLoadError,
    chapter_retry_available,
    ensure_step_inputs,
    load_task_context_sources,
    load_task_instructions,
    load_workflow_flow,
    load_workflow_step,
    render_contract_template,
    workflow_source_manifest,
)
from tests.workflow_support import install_minimal_workflow


class WorkflowLoaderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        install_minimal_workflow(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_loads_prompt_rules_and_contract_from_single_registry(self) -> None:
        text = load_task_instructions(self.root, "draft_chapter")

        self.assertIn("# 生成正文", text)
        self.assertIn("# 任务规则", text)
        self.assertIn("正文必须服从本章机械长度契约", text)
        self.assertIn("# 输出契约", text)
        self.assertIn("第一行必须是", text)

    def test_repair_prompt_separates_manual_advice_from_machine_repair(self) -> None:
        text = load_task_instructions(self.root, "repair_chapter")

        self.assertIn("候选片段（未写入文件）", text)
        self.assertIn("未经用户另行明确授权", text)
        self.assertIn("获得信息 → 判断处境 → 比较选择 → 采取行动 → 承担后果", text)
        self.assertIn("谁可能背责", text)

    def test_missing_new_workflow_does_not_fall_back_to_legacy_files(self) -> None:
        registry = self.root / "workflow/编排/任务表.json"
        registry.unlink()
        (self.root / "workflow/04-draft.md").write_text("旧正文规则", encoding="utf-8")

        with self.assertRaisesRegex(WorkflowLoadError, "无法读取工作流文件"):
            load_task_instructions(self.root, "draft_chapter")

    def test_manifest_hashes_each_composed_workflow_source(self) -> None:
        manifest = workflow_source_manifest(self.root, "review_chapter")

        self.assertEqual(manifest["workflow_version"], "4.0")
        self.assertEqual(manifest["task_id"], "review_chapter")
        self.assertEqual(len(manifest["sources"]), 5)
        self.assertTrue(all(item["sha256"] for item in manifest["sources"]))

    def test_flow_lists_every_registered_model_task_once(self) -> None:
        flow = load_workflow_flow(self.root)

        model_steps = {
            item["id"] for item in flow["steps"] if item["kind"] == "model"
        }
        self.assertEqual(
            model_steps,
            {
                "plan_story_unit",
                "plan_chapter_batch",
                "draft_chapter",
                "repair_chapter",
                "review_chapter",
                "extract_state",
                "build_ledger",
            },
        )

    def test_conditional_platform_rule_is_loaded_and_hashed(self) -> None:
        context = {"platform": "fanqie", "channel": "male"}

        text = load_task_instructions(
            self.root, "draft_chapter", rule_context=context
        )
        manifest = workflow_source_manifest(
            self.root, "draft_chapter", rule_context=context
        )

        self.assertIn("番茄小说男频正文要求", text)
        self.assertIn(
            "workflow/规则/平台/番茄男频.md",
            [item["path"] for item in manifest["sources"]],
        )

    def test_genre_and_style_rules_are_selected_from_profile(self) -> None:
        selected = workflow_source_manifest(
            self.root,
            "draft_chapter",
            rule_context={
                "platform": "",
                "channel": "",
                "genre": "xianxia",
                "style": "comedy",
            },
        )
        unselected = workflow_source_manifest(
            self.root,
            "draft_chapter",
            rule_context={
                "platform": "",
                "channel": "",
                "genre": "mystery",
                "style": "serious",
            },
        )
        selected_paths = [item["path"] for item in selected["sources"]]
        unselected_paths = [item["path"] for item in unselected["sources"]]

        self.assertIn("workflow/规则/题材/修仙.md", selected_paths)
        self.assertIn("workflow/规则/风格/喜剧.md", selected_paths)
        self.assertIn("workflow/规则/风格/笑点落地.md", selected_paths)
        self.assertNotIn("workflow/规则/题材/修仙.md", unselected_paths)
        self.assertNotIn("workflow/规则/风格/喜剧.md", unselected_paths)
        self.assertNotIn("workflow/规则/风格/笑点落地.md", unselected_paths)

    def test_joke_landing_rule_is_only_used_for_comedy_draft_and_repair(self) -> None:
        context = {
            "platform": "fanqie",
            "channel": "male",
            "genre": "xianxia",
            "style": "comedy",
        }
        joke_rule = "workflow/规则/风格/笑点落地.md"

        for task_id in ("draft_chapter", "repair_chapter"):
            with self.subTest(task_id=task_id):
                manifest = workflow_source_manifest(
                    self.root, task_id, rule_context=context
                )
                self.assertIn(
                    joke_rule,
                    [item["path"] for item in manifest["sources"]],
                )

        for task_id in (
            "plan_story_unit",
            "plan_chapter_batch",
            "review_chapter",
            "extract_state",
            "build_ledger",
        ):
            with self.subTest(task_id=task_id):
                manifest = workflow_source_manifest(
                    self.root, task_id, rule_context=context
                )
                self.assertNotIn(
                    joke_rule,
                    [item["path"] for item in manifest["sources"]],
                )

    def test_prompt_context_sources_are_selected_from_profile(self) -> None:
        selected = load_task_context_sources(
            self.root,
            "draft_chapter",
            rule_context={
                "platform": "",
                "channel": "",
                "genre": "xianxia",
                "style": "comedy",
            },
        )
        unselected = load_task_context_sources(
            self.root,
            "draft_chapter",
            rule_context={
                "platform": "",
                "channel": "",
                "genre": "mystery",
                "style": "serious",
            },
        )

        self.assertEqual(
            [item.artifact for item in selected],
            ["project_material", "progression", "comedy_bible"],
        )
        self.assertEqual(
            [item.artifact for item in unselected],
            ["project_material"],
        )

    def test_contract_template_owns_dynamic_outline_shape(self) -> None:
        outline = render_contract_template(
            self.root,
            "plan_chapter_batch",
            {
                "chapter_id": "chapter-0007",
                "chapter_number": 7,
                "story_unit_id": "unit-0001",
                "target_min": 2000,
                "target_max": 3000,
            },
            template_key="item_template",
        )

        self.assertEqual(outline["chapter_id"], "chapter-0007")
        self.assertEqual(outline["number"], 7)
        self.assertEqual(outline["scenes"][0]["scene_id"], "chapter-0007-scene-1")

    def test_rejects_registry_paths_outside_workflow(self) -> None:
        path = self.root / "workflow/编排/任务表.json"
        registry = json.loads(path.read_text(encoding="utf-8"))
        registry["tasks"]["draft_chapter"]["prompt"] = "../outside.md"
        path.write_text(json.dumps(registry, ensure_ascii=False), encoding="utf-8")

        with self.assertRaisesRegex(WorkflowLoadError, "不能越出"):
            load_task_instructions(self.root, "draft_chapter")

    def test_rejects_duplicate_orchestration_in_task_registry(self) -> None:
        path = self.root / "workflow/编排/任务表.json"
        registry = json.loads(path.read_text(encoding="utf-8"))
        registry["tasks"]["draft_chapter"]["requires"] = ["wrong_place"]
        path.write_text(json.dumps(registry, ensure_ascii=False), encoding="utf-8")

        with self.assertRaisesRegex(WorkflowLoadError, "不能重复定义编排字段"):
            load_workflow_flow(self.root)

    def test_step_inputs_and_retry_budget_are_taken_from_flow(self) -> None:
        flow = load_workflow_flow(self.root)
        step = load_workflow_step(self.root, "draft_chapter", flow=flow)

        self.assertEqual(step.requires, ("chapter_outline", "state_context"))
        with self.assertRaisesRegex(WorkflowLoadError, "state_context"):
            ensure_step_inputs(step, {"chapter_outline"})
        self.assertTrue(
            chapter_retry_available(
                flow,
                {"status": "draft_failed_provider", "retry_counts": {"transport": 1}},
                {"transport": 2, "format": 1, "content": 2},
            )
        )
        self.assertFalse(
            chapter_retry_available(
                flow,
                {"status": "draft_failed_provider", "retry_counts": {"transport": 2}},
                {"transport": 2, "format": 1, "content": 2},
            )
        )
