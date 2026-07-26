"""Build text providers from parsed command-line arguments."""

from __future__ import annotations

import argparse
import os

from ..provider import (
    DirectoryFixtureProvider,
    FixtureProvider,
    OpenAIResponsesProvider,
    TaskRoutingProvider,
    TextProvider,
)
from ..storage import StorageError, read_json, resolve_run_dir


def provider_from_args(args: argparse.Namespace) -> TextProvider:
    response_file = getattr(args, "response_file", None)
    if response_file is not None:
        return FixtureProvider(response_file)
    fixture_dir = getattr(args, "fixture_dir", None)
    if fixture_dir is not None:
        return DirectoryFixtureProvider(fixture_dir)
    if getattr(args, "openai", False):
        run_dir = resolve_run_dir(args.root, args.run_id)
        run = read_json(run_dir / "run.json")
        config = run.get("provider")
        if not isinstance(config, dict):
            raise StorageError("run.json 缺少 provider 配置")
        api_key_env = str(config.get("api_key_env", "MESHYCODE_API_KEY"))
        if not os.environ.get(api_key_env):
            raise StorageError(f"缺少 API Key 环境变量：{api_key_env}")
        base_url_env = config.get("base_url_env")
        base_url = ""
        if isinstance(base_url_env, str) and base_url_env.strip():
            base_url = os.environ.get(base_url_env, "").strip()
        if not base_url:
            base_url = str(config.get("base_url", "")).strip()
        if not base_url:
            source = base_url_env if isinstance(base_url_env, str) else "provider.base_url"
            raise StorageError(f"缺少 API Base URL：{source}")
        user_agent_env = config.get("user_agent_env")
        user_agent = "Mozilla/5.0 (compatible; NovelWorkflowRunner/0.2)"
        if isinstance(user_agent_env, str) and user_agent_env.strip():
            user_agent = os.environ.get(user_agent_env, user_agent).strip() or user_agent
        pricing = config.get("pricing")
        if not isinstance(pricing, dict):
            raise StorageError("run.json 的 provider.pricing 配置无效")
        shared = {
            "api_key_env": api_key_env,
            "base_url": base_url,
            "input_cost_per_million": pricing.get("input_per_million"),
            "output_cost_per_million": pricing.get("output_per_million"),
            "user_agent": user_agent,
        }

        routes = config.get("routes")
        if isinstance(routes, dict):
            routed: dict[str, tuple[TextProvider, ...]] = {}
            for role in ("planner", "drafter", "rewriter", "reviewer", "state"):
                route = routes.get(role)
                if not isinstance(route, dict):
                    raise StorageError(f"run.json 缺少 provider.routes.{role}")
                primary_env = route.get("model_env")
                if not isinstance(primary_env, str) or not primary_env.strip():
                    raise StorageError(f"provider.routes.{role}.model_env 无效")
                env_names = [primary_env]
                fallbacks = route.get("fallback_model_envs", [])
                if not isinstance(fallbacks, list):
                    raise StorageError(
                        f"provider.routes.{role}.fallback_model_envs 无效"
                    )
                env_names.extend(
                    item for item in fallbacks if isinstance(item, str) and item.strip()
                )
                models: list[str] = []
                for env_name in env_names:
                    model = os.environ.get(env_name, "").strip()
                    if not model:
                        if env_name == primary_env:
                            raise StorageError(
                                f"缺少 {role} 模型环境变量：{env_name}"
                            )
                        continue
                    if model not in models:
                        models.append(model)
                route_max = route.get(
                    "max_output_tokens", config.get("max_output_tokens")
                )
                route_timeout = int(
                    route.get("timeout_seconds", config.get("timeout_seconds", 120))
                )
                route_deadline_value = route.get(
                    "deadline_seconds", config.get("deadline_seconds")
                )
                route_deadline = (
                    int(route_deadline_value)
                    if route_deadline_value is not None
                    else None
                )
                reasoning_effort = route.get("reasoning_effort")
                routed[role] = tuple(
                    OpenAIResponsesProvider(
                        model=model,
                        max_output_tokens=route_max,
                        timeout_seconds=route_timeout,
                        deadline_seconds=route_deadline,
                        reasoning_effort=(
                            str(reasoning_effort) if reasoning_effort is not None else None
                        ),
                        **shared,
                    )
                    for model in models
                )
            return TaskRoutingProvider(routes=routed)

        model = str(config.get("model", ""))
        if not model.strip():
            raise StorageError(
                "run.json 未配置 provider.routes，且 provider.model 为空"
            )
        return OpenAIResponsesProvider(
            model=model,
            max_output_tokens=config.get("max_output_tokens"),
            timeout_seconds=int(config.get("timeout_seconds", 120)),
            deadline_seconds=(
                int(config["deadline_seconds"])
                if config.get("deadline_seconds") is not None
                else None
            ),
            **shared,
        )
    raise StorageError("未选择模型提供方")
