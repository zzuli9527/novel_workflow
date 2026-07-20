"""模型调用的统一预算、日志和用量汇总入口。"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
from time import monotonic
from typing import Any

from .provider import GenerationRequest, GenerationResponse, ProviderError, TextProvider
from .storage import append_jsonl, atomic_write_json, atomic_write_text, read_json


class BudgetExceededError(ProviderError):
    """运行预算已经耗尽，禁止发起新的模型调用。"""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _number(value: Any) -> float:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        numeric = float(value)
        return numeric if math.isfinite(numeric) else 0.0
    return 0.0


def _usage_tokens(usage: dict[str, Any]) -> int:
    total = _number(usage.get("total_tokens"))
    if total:
        return int(total)
    input_tokens = max(
        _number(usage.get("input_tokens")),
        _number(usage.get("prompt_tokens")),
    )
    output_tokens = max(
        _number(usage.get("output_tokens")),
        _number(usage.get("completion_tokens")),
    )
    return int(input_tokens + output_tokens)


def _usage_cost(usage: dict[str, Any]) -> float:
    for key in ("total_cost", "cost_usd", "cost"):
        value = _number(usage.get(key))
        if value:
            return value
    return 0.0


def load_api_call_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except OSError as exc:
        raise ProviderError(f"无法读取 API 调用日志：{exc}") from exc
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ProviderError(
                f"API 调用日志第 {line_number} 行不是有效 JSON"
            ) from exc
        if not isinstance(item, dict):
            raise ProviderError(f"API 调用日志第 {line_number} 行必须是对象")
        records.append(item)
    return records


def summarize_api_calls(records: list[dict[str, Any]]) -> dict[str, Any]:
    total_tokens = 0
    total_cost = 0.0
    total_duration = 0.0
    input_characters = 0
    output_characters = 0
    failed_calls = 0
    for record in records:
        usage = record.get("usage")
        if not isinstance(usage, dict):
            usage = {}
        total_tokens += _usage_tokens(usage)
        total_cost += _usage_cost(usage)
        input_characters += int(_number(usage.get("input_characters")))
        output_characters += int(_number(usage.get("output_characters")))
        total_duration += _number(record.get("duration_seconds"))
        if record.get("status", "success") != "success":
            failed_calls += 1
    return {
        "calls": len(records),
        "successful_calls": len(records) - failed_calls,
        "failed_calls": failed_calls,
        "total_tokens": total_tokens,
        "total_cost": round(total_cost, 8),
        "input_characters": input_characters,
        "output_characters": output_characters,
        "total_duration_seconds": round(total_duration, 6),
    }


def _budget_reasons(summary: dict[str, Any], budget: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    limits = (
        ("max_calls", "calls", "调用次数"),
        ("max_tokens", "total_tokens", "Token"),
        ("max_cost", "total_cost", "费用"),
    )
    for limit_key, used_key, label in limits:
        limit = budget.get(limit_key)
        if limit is None:
            continue
        if _number(summary.get(used_key)) >= _number(limit):
            reasons.append(f"{label}预算已耗尽：{summary.get(used_key)} / {limit}")
    return reasons


def ensure_budget_available(run_dir: Path) -> dict[str, Any]:
    run = read_json(run_dir / "run.json")
    budget = run.get("policies", {}).get("budget", {})
    if not isinstance(budget, dict):
        raise BudgetExceededError("run.json 的预算配置无效")
    records = load_api_call_records(run_dir / "logs/api-calls.jsonl")
    summary = summarize_api_calls(records)
    reasons = _budget_reasons(summary, budget)
    if reasons:
        reason = "；".join(reasons)
        atomic_write_json(
            run_dir / "run.json",
            {
                **run,
                "status": "paused",
                "pause_reason": reason,
                "updated_at": _utc_now(),
            },
        )
        raise BudgetExceededError(reason)
    return summary


def _task_key(request: GenerationRequest) -> str:
    payload = {
        "task": request.task,
        "metadata": request.metadata,
        "prompt_sha256": hashlib.sha256(request.prompt.encode("utf-8")).hexdigest(),
    }
    canonical = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _provider_cache_models(
    provider: TextProvider, request: GenerationRequest
) -> tuple[str, ...] | None:
    method = getattr(provider, "cache_models", None)
    if callable(method):
        models = method(request)
        if isinstance(models, tuple) and all(isinstance(item, str) for item in models):
            return tuple(item for item in models if item)
    model = getattr(provider, "model", None)
    if isinstance(model, str) and model:
        return (model,)
    return None


def _log_task(
    run_dir: Path,
    *,
    task_key: str,
    request: GenerationRequest,
    status: str,
    **extra: Any,
) -> None:
    append_jsonl(
        run_dir / "logs/tasks.jsonl",
        {
            "timestamp": _utc_now(),
            "task_key": task_key,
            "task": request.task,
            "metadata": request.metadata,
            "status": status,
            **extra,
        },
    )


def load_task_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except OSError as exc:
        raise ProviderError(f"无法读取任务日志：{exc}") from exc
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ProviderError(f"任务日志第 {line_number} 行不是有效 JSON") from exc
        if not isinstance(item, dict):
            raise ProviderError(f"任务日志第 {line_number} 行必须是对象")
        records.append(item)
    return records


def mark_task_accepted(
    run_dir: Path,
    request: GenerationRequest,
    response: GenerationResponse,
    output_path: Path,
) -> None:
    _log_task(
        run_dir,
        task_key=_task_key(request),
        request=request,
        status="accepted",
        output_path=output_path.relative_to(run_dir).as_posix(),
        provider=response.provider,
        model=response.model,
        usage=response.usage,
    )


def invoke_provider(
    run_dir: Path,
    provider: TextProvider,
    request: GenerationRequest,
    *,
    prompt_path: Path,
    output_path: Path,
    chapter: int | None = None,
) -> GenerationResponse:
    """在一次模型调用前检查预算，并无遗漏地记录成功或失败。"""

    task_key = _task_key(request)
    cache_models = _provider_cache_models(provider, request)
    task_records = load_task_records(run_dir / "logs/tasks.jsonl")
    for record in reversed(task_records):
        if record.get("task_key") != task_key or record.get("status") != "accepted":
            continue
        if cache_models is not None and record.get("model") not in cache_models:
            continue
        prior_relative = record.get("output_path")
        if not isinstance(prior_relative, str):
            continue
        prior_path = (run_dir / prior_relative).resolve()
        if run_dir.resolve() not in prior_path.parents or not prior_path.is_file():
            continue
        try:
            cached_text = prior_path.read_text(encoding="utf-8-sig")
        except OSError:
            continue
        atomic_write_text(output_path, cached_text)
        _log_task(
            run_dir,
            task_key=task_key,
            request=request,
            status="reused",
            source_output_path=prior_relative,
            output_path=output_path.relative_to(run_dir).as_posix(),
        )
        usage = record.get("usage") if isinstance(record.get("usage"), dict) else {}
        return GenerationResponse(
            text=cached_text,
            provider=str(record.get("provider", "cached")),
            model=str(record.get("model", "cached")),
            usage={**usage, "reused_cache": True},
        )

    ensure_budget_available(run_dir)
    _log_task(
        run_dir,
        task_key=task_key,
        request=request,
        status="started",
        prompt_path=prompt_path.relative_to(run_dir).as_posix(),
    )
    started = monotonic()
    base_record: dict[str, Any] = {
        "timestamp": _utc_now(),
        "task": request.task,
        "provider": "unknown",
        "model": "unknown",
        "prompt_path": prompt_path.relative_to(run_dir).as_posix(),
        "output_path": output_path.relative_to(run_dir).as_posix(),
        "metadata": request.metadata,
        "task_key": task_key,
    }
    if chapter is not None:
        base_record["chapter"] = chapter
    try:
        response = provider.generate(request)
    except ProviderError as exc:
        attempted_models = getattr(exc, "attempted_models", ())
        append_jsonl(
            run_dir / "logs/api-calls.jsonl",
            {
                **base_record,
                "provider": "openai-responses" if attempted_models else base_record["provider"],
                "model": ",".join(attempted_models) if attempted_models else base_record["model"],
                "status": "failed",
                "duration_seconds": round(monotonic() - started, 6),
                "usage": {},
                "error": str(exc),
            },
        )
        _log_task(
            run_dir,
            task_key=task_key,
            request=request,
            status="failed",
            error=str(exc),
        )
        raise

    atomic_write_text(output_path, response.text)
    append_jsonl(
        run_dir / "logs/api-calls.jsonl",
        {
            **base_record,
            "status": "success",
            "provider": response.provider,
            "model": response.model,
            "duration_seconds": round(monotonic() - started, 6),
            "usage": response.usage,
        },
    )
    _log_task(
        run_dir,
        task_key=task_key,
        request=request,
        status="response_saved",
        output_path=output_path.relative_to(run_dir).as_posix(),
    )
    return response
