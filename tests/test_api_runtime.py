from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.api_runtime import (
    BudgetExceededError,
    invoke_provider,
    load_api_call_records,
    mark_task_accepted,
    summarize_api_calls,
)
from tools.novel_runner.config import init_run, validate_run_directory
from tools.novel_runner.provider import (
    GenerationRequest,
    GenerationResponse,
    ProviderError,
)


class CountingProvider:
    def __init__(self, *, fail: bool = False, model: str = "counting-v1") -> None:
        self.calls = 0
        self.fail = fail
        self.model = model

    def cache_models(self, request: GenerationRequest) -> tuple[str, ...]:
        return (self.model,)

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        self.calls += 1
        if self.fail:
            raise ProviderError("模拟传输失败")
        return GenerationResponse(
            text="结果",
            provider="counting",
            model=self.model,
            usage={
                "input_tokens": 10,
                "output_tokens": 5,
                "cost_usd": 0.02,
            },
        )


class ApiRuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.run_dir = init_run(self.root, "budget-run")
        self.prompt_path = self.run_dir / "chapters/0001/draft.prompt.v1.md"
        self.prompt_path.parent.mkdir(parents=True)
        self.prompt_path.write_text("提示", encoding="utf-8")
        self.output_path = self.run_dir / "chapters/0001/draft.v1.md"
        self.request = GenerationRequest(task="draft_chapter", prompt="提示")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_successful_call_is_logged_and_summarized(self) -> None:
        provider = CountingProvider()
        first = invoke_provider(
            self.run_dir,
            provider,
            self.request,
            prompt_path=self.prompt_path,
            output_path=self.output_path,
            chapter=1,
        )

        records = load_api_call_records(self.run_dir / "logs/api-calls.jsonl")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["status"], "success")
        self.assertEqual(records[0]["chapter"], 1)
        self.assertEqual(self.output_path.read_text(encoding="utf-8"), "结果")
        summary = summarize_api_calls(records)
        self.assertEqual(summary["calls"], 1)
        self.assertEqual(summary["total_tokens"], 15)
        self.assertEqual(summary["total_cost"], 0.02)

    def test_identical_successful_task_reuses_output_without_api_call(self) -> None:
        provider = CountingProvider()
        first = invoke_provider(
            self.run_dir,
            provider,
            self.request,
            prompt_path=self.prompt_path,
            output_path=self.output_path,
        )
        mark_task_accepted(self.run_dir, self.request, first, self.output_path)
        second_output = self.run_dir / "chapters/0001/draft.v2.md"
        response = invoke_provider(
            self.run_dir,
            provider,
            self.request,
            prompt_path=self.prompt_path,
            output_path=second_output,
        )

        self.assertEqual(provider.calls, 1)
        self.assertTrue(response.usage["reused_cache"])
        self.assertEqual(second_output.read_text(encoding="utf-8"), "结果")
        api_records = load_api_call_records(self.run_dir / "logs/api-calls.jsonl")
        self.assertEqual(len(api_records), 1)
        self.assertEqual(len(api_records[0]["task_key"]), 64)
        task_records = [
            json.loads(line)
            for line in (self.run_dir / "logs/tasks.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
        ]
        self.assertEqual(
            [item["status"] for item in task_records],
            ["started", "response_saved", "accepted", "reused"],
        )

    def test_failed_call_is_still_counted(self) -> None:
        provider = CountingProvider(fail=True)
        with self.assertRaisesRegex(ProviderError, "模拟传输失败"):
            invoke_provider(
                self.run_dir,
                provider,
                self.request,
                prompt_path=self.prompt_path,
                output_path=self.output_path,
            )

        records = load_api_call_records(self.run_dir / "logs/api-calls.jsonl")
        self.assertEqual(records[0]["status"], "failed")
        self.assertEqual(summarize_api_calls(records)["failed_calls"], 1)
        self.assertFalse(self.output_path.exists())

    def test_accepted_output_is_not_reused_after_model_route_changes(self) -> None:
        first_provider = CountingProvider(model="model-a")
        first = invoke_provider(
            self.run_dir,
            first_provider,
            self.request,
            prompt_path=self.prompt_path,
            output_path=self.output_path,
        )
        mark_task_accepted(self.run_dir, self.request, first, self.output_path)

        second_provider = CountingProvider(model="model-b")
        second_output = self.run_dir / "chapters/0001/draft.v2.md"
        response = invoke_provider(
            self.run_dir,
            second_provider,
            self.request,
            prompt_path=self.prompt_path,
            output_path=second_output,
        )
        self.assertEqual(first_provider.calls, 1)
        self.assertEqual(second_provider.calls, 1)
        self.assertEqual(response.model, "model-b")
        self.assertNotIn("reused_cache", response.usage)

    def test_max_calls_blocks_before_contacting_provider(self) -> None:
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["budget"]["max_calls"] = 1
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")
        provider = CountingProvider()
        invoke_provider(
            self.run_dir,
            provider,
            self.request,
            prompt_path=self.prompt_path,
            output_path=self.output_path,
        )

        with self.assertRaisesRegex(BudgetExceededError, "调用次数预算已耗尽"):
            invoke_provider(
                self.run_dir,
                provider,
                GenerationRequest(task="draft_chapter", prompt="不同提示"),
                prompt_path=self.prompt_path,
                output_path=self.run_dir / "chapters/0001/draft.v2.md",
            )
        self.assertEqual(provider.calls, 1)
        paused = json.loads(
            (self.run_dir / "run.json").read_text(encoding="utf-8")
        )
        self.assertEqual(paused["status"], "paused")

    def test_invalid_budget_is_rejected_by_config_validation(self) -> None:
        run_path = self.run_dir / "run.json"
        run = json.loads(run_path.read_text(encoding="utf-8"))
        run["policies"]["budget"]["max_tokens"] = -1
        run_path.write_text(json.dumps(run, ensure_ascii=False), encoding="utf-8")

        report = validate_run_directory(self.root, "budget-run")
        self.assertFalse(report.valid)
        self.assertTrue(
            any(
                issue.path == "run.policies.budget.max_tokens"
                for issue in report.issues
            )
        )


if __name__ == "__main__":
    unittest.main()
