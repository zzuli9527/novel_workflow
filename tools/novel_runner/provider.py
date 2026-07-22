"""模型文本生成提供方接口。"""

from __future__ import annotations

from dataclasses import dataclass, field
import json
import os
from pathlib import Path
from threading import Event, Thread
from typing import Any, Protocol
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class ProviderError(RuntimeError):
    """模型提供方调用失败，并携带是否允许切换候选模型的信息。"""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        error_code: str | None = None,
        fallback_allowed: bool = False,
        attempted_models: tuple[str, ...] = (),
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code
        self.fallback_allowed = fallback_allowed
        self.attempted_models = attempted_models


@dataclass(frozen=True, slots=True)
class GenerationRequest:
    task: str
    prompt: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class GenerationResponse:
    text: str
    provider: str
    model: str
    usage: dict[str, Any] = field(default_factory=dict)


class TextProvider(Protocol):
    def generate(self, request: GenerationRequest) -> GenerationResponse: ...


TASK_ROLES = {
    "plan_story_unit": "planner",
    "plan_chapter_batch": "planner",
    "draft_chapter": "drafter",
    "repair_chapter": "rewriter",
    "review_chapter": "reviewer",
    "extract_state": "state",
    "build_ledger": "state",
}


@dataclass(frozen=True, slots=True)
class FixtureProvider:
    """从本地文件返回固定响应，用于无费用端到端测试。"""

    response_path: Path
    model: str = "fixture-v1"

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        try:
            text = self.response_path.read_text(encoding="utf-8-sig")
        except OSError as exc:
            raise ProviderError(f"无法读取响应文件：{self.response_path}：{exc}") from exc
        return GenerationResponse(
            text=text,
            provider="fixture",
            model=self.model,
            usage={"input_characters": len(request.prompt), "output_characters": len(text)},
        )


@dataclass(frozen=True, slots=True)
class DirectoryFixtureProvider:
    """按任务和章节从目录选择响应文件，用于整段调度回归测试。"""

    directory: Path
    model: str = "fixture-directory-v1"

    def _response_path(self, request: GenerationRequest) -> Path:
        task = request.task
        metadata = request.metadata
        if task in {"draft_chapter", "repair_chapter", "review_chapter", "extract_state"}:
            chapter = metadata.get("chapter")
            if not isinstance(chapter, int):
                raise ProviderError(f"任务 {task} 缺少 chapter")
            extension = "json" if task in {"review_chapter", "extract_state"} else "md"
            return self.directory / f"{task}-{chapter:04d}.{extension}"
        if task == "build_ledger":
            start = metadata.get("start_chapter")
            end = metadata.get("end_chapter")
            if not isinstance(start, int) or not isinstance(end, int):
                raise ProviderError("build_ledger 缺少章节范围")
            return self.directory / f"build_ledger-{start:04d}-{end:04d}.json"
        if task == "plan_story_unit":
            unit_id = metadata.get("unit_id")
            if not isinstance(unit_id, str) or not unit_id:
                raise ProviderError("plan_story_unit 缺少 unit_id")
            return self.directory / f"plan_story_unit-{unit_id}.json"
        if task == "plan_chapter_batch":
            start = metadata.get("start_chapter")
            end = metadata.get("end_chapter")
            if not isinstance(start, int) or not isinstance(end, int):
                raise ProviderError("plan_chapter_batch 缺少章节范围")
            return self.directory / f"plan_chapter_batch-{start:04d}-{end:04d}.json"
        raise ProviderError(f"目录夹具不支持任务：{task}")

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        path = self._response_path(request)
        try:
            text = path.read_text(encoding="utf-8-sig")
        except OSError as exc:
            raise ProviderError(f"缺少任务响应文件：{path}") from exc
        return GenerationResponse(
            text=text,
            provider="fixture-directory",
            model=self.model,
            usage={"input_characters": len(request.prompt), "output_characters": len(text)},
        )


@dataclass(frozen=True, slots=True)
class OpenAIResponsesProvider:
    """使用 OpenAI Responses API 的真实网络提供方。

    模型名称必须由运行配置提供，不在代码中固定。API Key 只从环境变量读取。
    """

    model: str
    api_key_env: str = "OPENAI_API_KEY"
    base_url: str = "https://api.openai.com/v1"
    timeout_seconds: int = 120
    deadline_seconds: int | None = None
    max_output_tokens: int | None = None
    input_cost_per_million: float | None = None
    output_cost_per_million: float | None = None
    user_agent: str = "Mozilla/5.0 (compatible; NovelWorkflowRunner/0.2)"
    reasoning_effort: str | None = None

    def cache_models(self, request: GenerationRequest) -> tuple[str, ...]:
        return (self.model,)

    def _endpoint(self) -> str:
        base = self.base_url.rstrip("/")
        return base if base.endswith("/responses") else f"{base}/responses"

    @staticmethod
    def _extract_text(data: dict[str, Any]) -> str:
        direct = data.get("output_text")
        if isinstance(direct, str) and direct:
            return direct
        pieces: list[str] = []
        output = data.get("output")
        if isinstance(output, list):
            for item in output:
                if not isinstance(item, dict):
                    continue
                content = item.get("content")
                if not isinstance(content, list):
                    continue
                for part in content:
                    if not isinstance(part, dict):
                        continue
                    if part.get("type") == "output_text" and isinstance(part.get("text"), str):
                        pieces.append(part["text"])
        text = "".join(pieces)
        if not text:
            raise ProviderError("Responses API 返回中没有可用 output_text")
        return text

    @staticmethod
    def _read_with_absolute_deadline(
        http_request: Request,
        *,
        request_timeout: int,
        deadline_seconds: int,
    ) -> bytes:
        """Read an HTTP response without allowing a stalled connection to block a run.

        ``urllib`` applies its timeout to individual socket operations.  In
        particular, a proxy can leave the connection waiting for response
        headers indefinitely even when the configured socket timeout has
        elapsed.  Run the blocking operation in a daemon worker so the caller
        can enforce the configured absolute deadline during both connection
        setup and response reading.
        """

        deadline_reached = Event()
        completed = Event()
        response_holder: list[Any | None] = [None]
        result: list[bytes | None] = [None]
        failure: list[BaseException | None] = [None]

        def read_response() -> None:
            try:
                with urlopen(http_request, timeout=request_timeout) as response:
                    response_holder[0] = response
                    if deadline_reached.is_set():
                        raise TimeoutError("请求在响应读取前已超过绝对截止时间")
                    raw = response.read()
                    if deadline_reached.is_set():
                        raise TimeoutError("请求读取超过绝对截止时间")
                    result[0] = raw
            except BaseException as exc:  # 由调用方统一转换为 ProviderError。
                failure[0] = exc
            finally:
                response_holder[0] = None
                completed.set()

        worker = Thread(target=read_response, name="novel-openai-request", daemon=True)
        worker.start()
        if not completed.wait(deadline_seconds):
            deadline_reached.set()
            response = response_holder[0]
            close = getattr(response, "close", None)
            if callable(close):
                try:
                    close()
                except OSError:
                    pass
            raise TimeoutError("请求超过绝对截止时间")
        if failure[0] is not None:
            raise failure[0]
        if result[0] is None:
            raise OSError("OpenAI API 请求未返回响应正文")
        return result[0]

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        if not self.model.strip():
            raise ProviderError("OpenAI provider 未配置 model")
        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise ProviderError(f"缺少 API Key 环境变量：{self.api_key_env}")

        payload: dict[str, Any] = {"model": self.model, "input": request.prompt}
        if self.reasoning_effort is not None:
            if self.reasoning_effort not in {"none", "minimal", "low", "medium", "high"}:
                raise ProviderError(
                    "reasoning_effort 必须是 none/minimal/low/medium/high"
                )
            payload["reasoning"] = {"effort": self.reasoning_effort}
        if self.max_output_tokens is not None:
            if self.max_output_tokens <= 0:
                raise ProviderError("max_output_tokens 必须大于 0")
            payload["max_output_tokens"] = self.max_output_tokens
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        http_request = Request(
            self._endpoint(),
            data=body,
            method="POST",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": self.user_agent,
            },
        )
        if self.deadline_seconds is not None and (
            not isinstance(self.deadline_seconds, int)
            or isinstance(self.deadline_seconds, bool)
            or self.deadline_seconds <= 0
        ):
            raise ProviderError("deadline_seconds 必须是正整数或 null")
        request_timeout = self.timeout_seconds
        if self.deadline_seconds is not None:
            request_timeout = min(request_timeout, self.deadline_seconds)
        try:
            if self.deadline_seconds is None:
                with urlopen(http_request, timeout=request_timeout) as response:
                    raw = response.read()
            else:
                raw = self._read_with_absolute_deadline(
                    http_request,
                    request_timeout=request_timeout,
                    deadline_seconds=self.deadline_seconds,
                )
        except HTTPError as exc:
            try:
                detail = exc.read().decode("utf-8", errors="replace")[:2000]
            except OSError:
                detail = ""
            error_code: str | None = None
            try:
                error_data = json.loads(detail)
            except json.JSONDecodeError:
                error_data = None
            if isinstance(error_data, dict):
                error = error_data.get("error")
                if isinstance(error, dict) and isinstance(error.get("code"), str):
                    error_code = error["code"]
            suffix = f"：{detail}" if detail else ""
            fallback_allowed = exc.code in {
                404,
                408,
                409,
                429,
                500,
                502,
                503,
                504,
                520,
                521,
                522,
                523,
                524,
                525,
                526,
                527,
            }
            if error_code in {"model_not_found", "model_unavailable", "rate_limit_exceeded"}:
                fallback_allowed = True
            raise ProviderError(
                f"OpenAI API HTTP {exc.code}{suffix}",
                status_code=exc.code,
                error_code=error_code,
                fallback_allowed=fallback_allowed,
                attempted_models=(self.model,),
            ) from exc
        except (URLError, TimeoutError, OSError) as exc:
            if isinstance(exc, TimeoutError) and self.deadline_seconds is not None:
                raise ProviderError(
                    f"OpenAI API 请求超过绝对截止时间：{self.deadline_seconds} 秒",
                    error_code="deadline_exceeded",
                    fallback_allowed=True,
                    attempted_models=(self.model,),
                ) from exc
            raise ProviderError(
                f"OpenAI API 请求失败：{exc}",
                error_code="transport_error",
                fallback_allowed=True,
                attempted_models=(self.model,),
            ) from exc
        try:
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ProviderError("OpenAI API 返回了无法解析的 JSON") from exc
        if not isinstance(data, dict):
            raise ProviderError("OpenAI API 返回必须是 JSON 对象")
        status = data.get("status")
        if status in {"incomplete", "failed", "cancelled", "queued", "in_progress"}:
            details = data.get("incomplete_details") or data.get("error")
            if isinstance(details, dict):
                reason = details.get("reason") or details.get("message")
            else:
                reason = details
            suffix = f"：{reason}" if isinstance(reason, str) and reason else ""
            raise ProviderError(f"OpenAI API 响应未完成（{status}）{suffix}")
        usage = data.get("usage") if isinstance(data.get("usage"), dict) else {}
        usage = dict(usage)
        if (
            self.input_cost_per_million is not None
            and self.output_cost_per_million is not None
        ):
            input_tokens = usage.get("input_tokens", 0)
            output_tokens = usage.get("output_tokens", 0)
            if (
                isinstance(input_tokens, (int, float))
                and not isinstance(input_tokens, bool)
                and isinstance(output_tokens, (int, float))
                and not isinstance(output_tokens, bool)
            ):
                usage["cost_usd"] = round(
                    (float(input_tokens) * self.input_cost_per_million / 1_000_000)
                    + (
                        float(output_tokens)
                        * self.output_cost_per_million
                        / 1_000_000
                    ),
                    10,
                )
                usage["cost_source"] = "run_config_pricing"
        return GenerationResponse(
            text=self._extract_text(data),
            provider="openai-responses",
            model=self.model,
            usage=usage,
        )


@dataclass(frozen=True, slots=True)
class TaskRoutingProvider:
    """按任务角色选择模型，并只在可安全切换的提供方错误上回退。"""

    routes: dict[str, tuple[TextProvider, ...]]
    default_role: str = "drafter"

    def _role(self, request: GenerationRequest) -> str:
        return TASK_ROLES.get(request.task, self.default_role)

    def _candidates(self, request: GenerationRequest) -> tuple[TextProvider, ...]:
        role = self._role(request)
        candidates = self.routes.get(role)
        if not candidates:
            raise ProviderError(f"任务角色 {role} 没有可用模型路由")
        return candidates

    def cache_models(self, request: GenerationRequest) -> tuple[str, ...]:
        """只复用当前首选模型已验收的结果；路由改变后重新调用。"""

        primary = self._candidates(request)[0]
        method = getattr(primary, "cache_models", None)
        if callable(method):
            models = method(request)
            if isinstance(models, tuple) and all(isinstance(item, str) for item in models):
                return models[:1]
        model = getattr(primary, "model", None)
        return (model,) if isinstance(model, str) and model else ()

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        candidates = self._candidates(request)
        failures: list[str] = []
        attempted_models: list[str] = []
        for index, provider in enumerate(candidates):
            try:
                return provider.generate(request)
            except ProviderError as exc:
                failures.append(str(exc))
                attempted_models.extend(exc.attempted_models)
                if not exc.attempted_models:
                    model = getattr(provider, "model", None)
                    if isinstance(model, str) and model:
                        attempted_models.append(model)
                if not exc.fallback_allowed or index == len(candidates) - 1:
                    if len(failures) == 1:
                        raise
                    raise ProviderError(
                        "模型路由全部失败：" + " | ".join(failures),
                        status_code=exc.status_code,
                        error_code=exc.error_code,
                        fallback_allowed=exc.fallback_allowed,
                        attempted_models=tuple(dict.fromkeys(attempted_models)),
                    ) from exc
        raise ProviderError("模型路由没有执行任何候选模型")
