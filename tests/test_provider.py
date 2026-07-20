from __future__ import annotations

import io
import json
import os
from unittest.mock import patch
import unittest

from tools.novel_runner.provider import (
    GenerationResponse,
    GenerationRequest,
    OpenAIResponsesProvider,
    ProviderError,
    TaskRoutingProvider,
)


class FakeResponse:
    def __init__(self, data: dict[str, object]) -> None:
        self.payload = json.dumps(data, ensure_ascii=False).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self) -> bytes:
        return self.payload


class OpenAIResponsesProviderTests(unittest.TestCase):
    def test_requires_api_key_environment_variable(self) -> None:
        provider = OpenAIResponsesProvider(model="test-model", api_key_env="MISSING_TEST_KEY")
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("MISSING_TEST_KEY", None)
            with self.assertRaisesRegex(ProviderError, "MISSING_TEST_KEY"):
                provider.generate(GenerationRequest(task="draft", prompt="hello"))

    def test_sends_responses_request_and_reads_direct_output_text(self) -> None:
        provider = OpenAIResponsesProvider(
            model="test-model",
            base_url="https://api.example.test/v1",
            max_output_tokens=1234,
        )
        fake = FakeResponse(
            {"output_text": "生成结果", "usage": {"input_tokens": 10, "output_tokens": 20}}
        )
        with patch.dict(os.environ, {"OPENAI_API_KEY": "secret"}), patch(
            "tools.novel_runner.provider.urlopen", return_value=fake
        ) as mocked:
            response = provider.generate(
                GenerationRequest(task="draft_chapter", prompt="写一章")
            )

        request = mocked.call_args.args[0]
        sent = json.loads(request.data.decode("utf-8"))
        self.assertEqual(request.full_url, "https://api.example.test/v1/responses")
        self.assertEqual(sent["model"], "test-model")
        self.assertEqual(sent["input"], "写一章")
        self.assertEqual(sent["max_output_tokens"], 1234)
        self.assertEqual(response.text, "生成结果")
        self.assertEqual(response.usage["output_tokens"], 20)
        self.assertNotIn("secret", repr(response))

    def test_extracts_nested_output_text(self) -> None:
        provider = OpenAIResponsesProvider(model="test-model")
        fake = FakeResponse(
            {
                "output": [
                    {
                        "type": "message",
                        "content": [
                            {"type": "output_text", "text": "第一段"},
                            {"type": "output_text", "text": "第二段"},
                        ],
                    }
                ]
            }
        )
        with patch.dict(os.environ, {"OPENAI_API_KEY": "secret"}), patch(
            "tools.novel_runner.provider.urlopen", return_value=fake
        ):
            response = provider.generate(GenerationRequest(task="state", prompt="prompt"))
        self.assertEqual(response.text, "第一段第二段")

    def test_rejects_response_without_text(self) -> None:
        provider = OpenAIResponsesProvider(model="test-model")
        fake = FakeResponse({"output": []})
        with patch.dict(os.environ, {"OPENAI_API_KEY": "secret"}), patch(
            "tools.novel_runner.provider.urlopen", return_value=fake
        ):
            with self.assertRaisesRegex(ProviderError, "output_text"):
                provider.generate(GenerationRequest(task="draft", prompt="prompt"))

    def test_rejects_incomplete_response_even_with_partial_text(self) -> None:
        provider = OpenAIResponsesProvider(model="test-model")
        fake = FakeResponse(
            {
                "status": "incomplete",
                "incomplete_details": {"reason": "max_output_tokens"},
                "output_text": "已经生成但被截断的正文",
                "usage": {"output_tokens": 100},
            }
        )
        with patch.dict(os.environ, {"OPENAI_API_KEY": "secret"}), patch(
            "tools.novel_runner.provider.urlopen", return_value=fake
        ):
            with self.assertRaisesRegex(ProviderError, "max_output_tokens"):
                provider.generate(GenerationRequest(task="draft", prompt="prompt"))

    def test_uses_run_supplied_pricing_to_estimate_cost(self) -> None:
        provider = OpenAIResponsesProvider(
            model="test-model",
            input_cost_per_million=2.0,
            output_cost_per_million=8.0,
        )
        fake = FakeResponse(
            {
                "status": "completed",
                "output_text": "结果",
                "usage": {"input_tokens": 1000, "output_tokens": 500},
            }
        )
        with patch.dict(os.environ, {"OPENAI_API_KEY": "secret"}), patch(
            "tools.novel_runner.provider.urlopen", return_value=fake
        ):
            response = provider.generate(
                GenerationRequest(task="draft", prompt="prompt")
            )
        self.assertEqual(response.usage["cost_usd"], 0.006)
        self.assertEqual(response.usage["cost_source"], "run_config_pricing")

    def test_sends_configured_user_agent(self) -> None:
        provider = OpenAIResponsesProvider(
            model="test-model",
            user_agent="custom-agent/1.0",
        )
        fake = FakeResponse({"output_text": "ok"})
        with patch.dict(os.environ, {"OPENAI_API_KEY": "secret"}), patch(
            "tools.novel_runner.provider.urlopen", return_value=fake
        ) as mocked:
            provider.generate(GenerationRequest(task="draft", prompt="prompt"))
        self.assertEqual(mocked.call_args.args[0].headers["User-agent"], "custom-agent/1.0")

    def test_sends_low_reasoning_effort_when_configured(self) -> None:
        provider = OpenAIResponsesProvider(
            model="test-model",
            reasoning_effort="low",
        )
        fake = FakeResponse({"output_text": "ok"})
        with patch.dict(os.environ, {"OPENAI_API_KEY": "secret"}), patch(
            "tools.novel_runner.provider.urlopen", return_value=fake
        ) as mocked:
            provider.generate(GenerationRequest(task="draft", prompt="prompt"))
        sent = json.loads(mocked.call_args.args[0].data.decode("utf-8"))
        self.assertEqual(sent["reasoning"], {"effort": "low"})


class RecordingProvider:
    def __init__(
        self,
        model: str,
        *,
        error: ProviderError | None = None,
    ) -> None:
        self.model = model
        self.error = error
        self.tasks: list[str] = []

    def cache_models(self, request: GenerationRequest) -> tuple[str, ...]:
        return (self.model,)

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        self.tasks.append(request.task)
        if self.error is not None:
            raise self.error
        return GenerationResponse(
            text=self.model,
            provider="recording",
            model=self.model,
        )


class TaskRoutingProviderTests(unittest.TestCase):
    def test_routes_tasks_to_independent_roles(self) -> None:
        planner = RecordingProvider("planner-model")
        drafter = RecordingProvider("draft-model")
        rewriter = RecordingProvider("rewrite-model")
        reviewer = RecordingProvider("review-model")
        state = RecordingProvider("state-model")
        provider = TaskRoutingProvider(
            routes={
                "planner": (planner,),
                "drafter": (drafter,),
                "rewriter": (rewriter,),
                "reviewer": (reviewer,),
                "state": (state,),
            }
        )

        cases = {
            "plan_story_unit": "planner-model",
            "plan_chapter_batch": "planner-model",
            "draft_chapter": "draft-model",
            "repair_chapter": "rewrite-model",
            "review_chapter": "review-model",
            "extract_state": "state-model",
            "build_ledger": "state-model",
        }
        for task, expected in cases.items():
            response = provider.generate(GenerationRequest(task=task, prompt="p"))
            self.assertEqual(response.model, expected)

    def test_falls_back_only_for_eligible_provider_error(self) -> None:
        primary = RecordingProvider(
            "unavailable",
            error=ProviderError("unavailable", fallback_allowed=True),
        )
        fallback = RecordingProvider("fallback")
        provider = TaskRoutingProvider(
            routes={"drafter": (primary, fallback)}
        )
        response = provider.generate(
            GenerationRequest(task="draft_chapter", prompt="p")
        )
        self.assertEqual(response.model, "fallback")
        self.assertEqual(primary.tasks, ["draft_chapter"])
        self.assertEqual(fallback.tasks, ["draft_chapter"])

    def test_does_not_fallback_for_content_or_local_error(self) -> None:
        primary = RecordingProvider(
            "bad",
            error=ProviderError("bad request", fallback_allowed=False),
        )
        fallback = RecordingProvider("fallback")
        provider = TaskRoutingProvider(
            routes={"drafter": (primary, fallback)}
        )
        with self.assertRaisesRegex(ProviderError, "bad request"):
            provider.generate(GenerationRequest(task="draft_chapter", prompt="p"))
        self.assertEqual(fallback.tasks, [])


if __name__ == "__main__":
    unittest.main()
