"""运行初始化和最小配置校验。"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from .storage import (
    StorageError,
    atomic_write_json,
    atomic_write_text,
    read_json,
    resolve_run_dir,
    validate_run_id,
)
from .structured_state import (
    StructuredStateError,
    default_initial_state,
    validate_initial_state,
)
from .master_plan import default_master_plan, validate_master_plan_data
from .wordcount import LengthPolicy


RUN_STATUSES = {"planning", "ready", "running", "paused", "completed", "failed"}


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    path: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class ValidationReport:
    run_id: str
    valid: bool
    issues: tuple[ValidationIssue, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "run_id": self.run_id,
            "valid": self.valid,
            "issues": [issue.to_dict() for issue in self.issues],
        }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_run_config(run_id: str, *, storage_version: str | None = None) -> dict[str, Any]:
    timestamp = _utc_now()
    config = {
        "schema_version": "1.0",
        "run_id": run_id,
        "status": "planning",
        "current_story_unit": None,
        "current_batch": None,
        "last_committed_chapter": 0,
        "provider": {
            "kind": "openai_responses",
            "model": "",
            "api_key_env": "MESHYCODE_API_KEY",
            "base_url": "",
            "base_url_env": "MESHYCODE_BASE_URL",
            "user_agent_env": "MESHYCODE_USER_AGENT",
            "timeout_seconds": 120,
            "deadline_seconds": 300,
            "max_output_tokens": 6000,
            "routes": {
                "planner": {
                    "model_env": "NOVEL_MODEL_PLANNER",
                    "fallback_model_envs": ["NOVEL_MODEL_REWRITER"],
                    "max_output_tokens": 6000,
                    "timeout_seconds": 600,
                    "deadline_seconds": 300,
                    "reasoning_effort": "low",
                },
                "drafter": {
                    "model_env": "NOVEL_MODEL_REWRITER",
                    "fallback_model_envs": ["NOVEL_MODEL_REVIEWER"],
                    "max_output_tokens": 4500,
                    "timeout_seconds": 600,
                    "deadline_seconds": 300,
                    "reasoning_effort": "low",
                },
                "rewriter": {
                    "model_env": "NOVEL_MODEL_REWRITER",
                    "fallback_model_envs": ["NOVEL_MODEL_DRAFTER"],
                    "max_output_tokens": 4500,
                    "timeout_seconds": 600,
                    "deadline_seconds": 300,
                    "reasoning_effort": "low",
                },
                "reviewer": {
                    "model_env": "NOVEL_MODEL_REVIEWER",
                    "fallback_model_envs": ["NOVEL_MODEL_REWRITER"],
                    "max_output_tokens": 4000,
                    "timeout_seconds": 300,
                    "deadline_seconds": 240,
                    "reasoning_effort": "low",
                },
                "state": {
                    "model_env": "NOVEL_MODEL_STATE",
                    "fallback_model_envs": [],
                    "max_output_tokens": 5000,
                    "timeout_seconds": 300,
                    "deadline_seconds": 240,
                    "reasoning_effort": "low",
                },
            },
            "pricing": {
                "input_per_million": None,
                "output_per_million": None,
            },
        },
        "policies": {
            "length": {
                "unit": "non_whitespace_character",
                "target_min": 2000,
                "target_max": 3000,
                "expand_from": 1800,
                "review_over": 3500,
            },
            "batch": {
                "story_unit_min": 10,
                "story_unit_max": 20,
                "outline_batch_size": 4,
                "outline_request_chunk_size": 2,
                "ledger_batch_size": 4,
                "ledger_batch_min": 3,
                "ledger_batch_max": 4,
                "ledger_item_limit": 8,
            },
            "retry": {"transport": 2, "format": 1, "content": 2},
            "budget": {"max_calls": None, "max_tokens": None, "max_cost": None},
        },
        "created_at": timestamp,
        "updated_at": timestamp,
    }
    if storage_version is not None:
        config["storage_version"] = storage_version
    return config


def default_progression_config() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "realms": [],
        "resources": [],
        "techniques": [],
        "artifacts": [],
        "injury_rules": [],
        "breakthrough_rules": [],
        "power_boundaries": [],
        "exceptions": [],
    }


def default_comedy_bible() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "density": "medium",
        "protagonist_role": "",
        "character_contrasts": [],
        "allowed_mechanisms": [],
        "forbidden_humor": [],
        "language_boundaries": [],
        "callbacks": [],
        "fatigued_mechanisms": [],
        "serious_scene_limits": [],
    }


def init_run(
    root: Path, run_id: str, *, storage_version: str | None = None
) -> Path:
    validate_run_id(run_id)
    run_dir = resolve_run_dir(root, run_id)
    if run_dir.exists():
        raise StorageError(f"运行目录已存在：{run_dir}")

    v2 = storage_version == "2.0"
    directories = [
        "config/prompt-patches",
        "planning",
        "chapters",
        "ledgers",
        "logs",
        "reports",
    ]
    directories.extend(("state", "work", "artifacts") if v2 else ("state/snapshots",))
    for relative in directories:
        (run_dir / relative).mkdir(parents=True, exist_ok=False)

    atomic_write_json(
        run_dir / "run.json", default_run_config(run_id, storage_version=storage_version)
    )
    atomic_write_json(run_dir / "config/progression.json", default_progression_config())
    atomic_write_json(run_dir / "config/comedy-bible.json", default_comedy_bible())
    atomic_write_json(run_dir / "config/initial-state.json", default_initial_state())
    atomic_write_json(run_dir / "config/master-plan.json", default_master_plan())
    atomic_write_json(run_dir / "planning/story-units.json", [])
    atomic_write_json(run_dir / "planning/chapter-outlines.json", [])
    atomic_write_json(
        run_dir / "planning/import-plan.template.json",
        {"schema_version": "1.0", "story_units": [], "chapter_outlines": []},
    )
    atomic_write_json(run_dir / "checks.json", [])
    atomic_write_text(
        run_dir / "config/project.md",
        "# 项目资料\n\n请填写项目定位、核心角色、开局状态和长期目标。\n",
    )
    atomic_write_text(run_dir / "logs/tasks.jsonl", "")
    atomic_write_text(run_dir / "logs/api-calls.jsonl", "")
    if v2:
        atomic_write_text(run_dir / "state/events.jsonl", "")
        atomic_write_text(run_dir / "state/checkpoints.jsonl", "")
        atomic_write_text(run_dir / "ledgers/history.jsonl", "")
        atomic_write_text(run_dir / "logs/runtime-events.jsonl", "")
    else:
        atomic_write_text(run_dir / "logs/events.jsonl", "")
    return run_dir


def _expect_type(
    issues: list[ValidationIssue], path: str, value: Any, expected: type | tuple[type, ...]
) -> bool:
    if not isinstance(value, expected):
        if isinstance(expected, tuple):
            name = " / ".join(item.__name__ for item in expected)
        else:
            name = expected.__name__
        issues.append(ValidationIssue(path, f"应为 {name}"))
        return False
    return True


def _require_keys(
    issues: list[ValidationIssue], path: str, data: dict[str, Any], keys: Iterable[str]
) -> None:
    for key in keys:
        if key not in data:
            issues.append(ValidationIssue(f"{path}.{key}", "缺少必填字段"))


def _validate_run_json(data: Any, expected_run_id: str) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if not _expect_type(issues, "run", data, dict):
        return issues

    _require_keys(
        issues,
        "run",
        data,
        (
            "schema_version",
            "run_id",
            "status",
            "last_committed_chapter",
            "policies",
            "provider",
        ),
    )
    if data.get("run_id") != expected_run_id:
        issues.append(ValidationIssue("run.run_id", "与运行目录名称不一致"))
    if data.get("status") not in RUN_STATUSES:
        issues.append(ValidationIssue("run.status", "不是允许的运行状态"))
    storage_version = data.get("storage_version")
    if storage_version is not None and storage_version not in {"1.0", "2.0"}:
        issues.append(
            ValidationIssue("run.storage_version", "仅支持 1.0、2.0 或省略（v1）")
        )

    provider = data.get("provider")
    if _expect_type(issues, "run.provider", provider, dict):
        if provider.get("kind") != "openai_responses":
            issues.append(
                ValidationIssue("run.provider.kind", "第一版只支持 openai_responses")
            )
        for key in ("model", "api_key_env", "base_url"):
            if not isinstance(provider.get(key), str):
                issues.append(ValidationIssue(f"run.provider.{key}", "应为字符串"))
        for key in ("base_url_env", "user_agent_env"):
            value = provider.get(key)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                issues.append(
                    ValidationIssue(f"run.provider.{key}", "应为非空字符串或省略")
                )
        if not provider.get("base_url") and not provider.get("base_url_env"):
            issues.append(
                ValidationIssue(
                    "run.provider.base_url",
                    "base_url 与 base_url_env 至少配置一个",
                )
            )
        timeout = provider.get("timeout_seconds")
        if not isinstance(timeout, int) or isinstance(timeout, bool) or timeout <= 0:
            issues.append(
                ValidationIssue("run.provider.timeout_seconds", "应为正整数")
            )
        deadline = provider.get("deadline_seconds")
        if deadline is not None and (
            not isinstance(deadline, int)
            or isinstance(deadline, bool)
            or deadline <= 0
        ):
            issues.append(
                ValidationIssue(
                    "run.provider.deadline_seconds", "应为正整数或 null"
                )
            )
        max_output = provider.get("max_output_tokens")
        if max_output is not None and (
            not isinstance(max_output, int) or isinstance(max_output, bool) or max_output <= 0
        ):
            issues.append(
                ValidationIssue(
                    "run.provider.max_output_tokens", "应为正整数或 null"
                )
            )
        routes = provider.get("routes")
        if routes is not None:
            if not isinstance(routes, dict):
                issues.append(ValidationIssue("run.provider.routes", "应为对象"))
            else:
                required_roles = (
                    "planner",
                    "drafter",
                    "rewriter",
                    "reviewer",
                    "state",
                )
                for role in required_roles:
                    route = routes.get(role)
                    path = f"run.provider.routes.{role}"
                    if not isinstance(route, dict):
                        issues.append(ValidationIssue(path, "应为对象"))
                        continue
                    model_env = route.get("model_env")
                    if not isinstance(model_env, str) or not model_env.strip():
                        issues.append(
                            ValidationIssue(f"{path}.model_env", "应为非空字符串")
                        )
                    fallback_envs = route.get("fallback_model_envs", [])
                    if not isinstance(fallback_envs, list) or not all(
                        isinstance(item, str) and item.strip()
                        for item in fallback_envs
                    ):
                        issues.append(
                            ValidationIssue(
                                f"{path}.fallback_model_envs",
                                "应为非空字符串数组",
                            )
                        )
                    route_max = route.get("max_output_tokens")
                    if route_max is not None and (
                        not isinstance(route_max, int)
                        or isinstance(route_max, bool)
                        or route_max <= 0
                    ):
                        issues.append(
                            ValidationIssue(
                                f"{path}.max_output_tokens",
                                "应为正整数或 null",
                            )
                        )
                    route_timeout = route.get("timeout_seconds")
                    if route_timeout is not None and (
                        not isinstance(route_timeout, int)
                        or isinstance(route_timeout, bool)
                        or route_timeout <= 0
                    ):
                        issues.append(
                            ValidationIssue(
                                f"{path}.timeout_seconds",
                                "应为正整数或 null",
                            )
                        )
                    route_deadline = route.get("deadline_seconds")
                    if route_deadline is not None and (
                        not isinstance(route_deadline, int)
                        or isinstance(route_deadline, bool)
                        or route_deadline <= 0
                    ):
                        issues.append(
                            ValidationIssue(
                                f"{path}.deadline_seconds",
                                "应为正整数或 null",
                            )
                        )
                    reasoning_effort = route.get("reasoning_effort")
                    if reasoning_effort is not None and reasoning_effort not in {
                        "none",
                        "minimal",
                        "low",
                        "medium",
                        "high",
                    }:
                        issues.append(
                            ValidationIssue(
                                f"{path}.reasoning_effort",
                                "应为 none/minimal/low/medium/high 或省略",
                            )
                        )
        pricing = provider.get("pricing")
        if not isinstance(pricing, dict):
            issues.append(ValidationIssue("run.provider.pricing", "应为对象"))
        else:
            price_values = (
                pricing.get("input_per_million"),
                pricing.get("output_per_million"),
            )
            for key, value in zip(
                ("input_per_million", "output_per_million"), price_values
            ):
                if value is not None and (
                    not isinstance(value, (int, float))
                    or isinstance(value, bool)
                    or value < 0
                ):
                    issues.append(
                        ValidationIssue(
                            f"run.provider.pricing.{key}", "应为非负数或 null"
                        )
                    )
            if (price_values[0] is None) != (price_values[1] is None):
                issues.append(
                    ValidationIssue(
                        "run.provider.pricing",
                        "输入和输出单价必须同时配置或同时为 null",
                    )
                )

    last_committed = data.get("last_committed_chapter")
    if not isinstance(last_committed, int) or isinstance(last_committed, bool) or last_committed < 0:
        issues.append(ValidationIssue("run.last_committed_chapter", "应为非负整数"))

    policies = data.get("policies")
    if not _expect_type(issues, "run.policies", policies, dict):
        return issues

    length = policies.get("length")
    if _expect_type(issues, "run.policies.length", length, dict):
        try:
            LengthPolicy(
                target_min=length["target_min"],
                target_max=length["target_max"],
                expand_from=length["expand_from"],
                review_over=length["review_over"],
            )
        except KeyError as exc:
            issues.append(
                ValidationIssue(
                    f"run.policies.length.{exc.args[0]}", "缺少必填字段"
                )
            )
        except (TypeError, ValueError) as exc:
            issues.append(ValidationIssue("run.policies.length", str(exc)))
        if length.get("unit") != "non_whitespace_character":
            issues.append(
                ValidationIssue(
                    "run.policies.length.unit",
                    "第一版只支持 non_whitespace_character",
                )
            )
        preferred_min = length.get("preferred_min")
        preferred_max = length.get("preferred_max")
        if (preferred_min is None) != (preferred_max is None):
            issues.append(
                ValidationIssue(
                    "run.policies.length",
                    "preferred_min 和 preferred_max 必须同时配置或同时省略",
                )
            )
        elif preferred_min is not None and preferred_max is not None:
            target_min = length.get("target_min")
            target_max = length.get("target_max")
            if not all(
                isinstance(value, int) and not isinstance(value, bool)
                for value in (preferred_min, preferred_max)
            ):
                issues.append(
                    ValidationIssue(
                        "run.policies.length",
                        "preferred_min 和 preferred_max 必须是整数",
                    )
                )
            elif (
                isinstance(target_min, int)
                and not isinstance(target_min, bool)
                and isinstance(target_max, int)
                and not isinstance(target_max, bool)
                and not (
                    target_min <= preferred_min <= preferred_max <= target_max
                )
            ):
                issues.append(
                    ValidationIssue(
                        "run.policies.length",
                        "首选长度区间必须位于正文硬范围内",
                    )
                )

    batch = policies.get("batch")
    if _expect_type(issues, "run.policies.batch", batch, dict):
        for key in (
            "story_unit_min",
            "story_unit_max",
            "outline_batch_size",
            "outline_request_chunk_size",
            "ledger_batch_size",
            "ledger_batch_min",
            "ledger_batch_max",
            "ledger_item_limit",
        ):
            value = batch.get(key)
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                issues.append(
                    ValidationIssue(f"run.policies.batch.{key}", "应为正整数")
                )
        if (
            isinstance(batch.get("story_unit_min"), int)
            and isinstance(batch.get("story_unit_max"), int)
            and batch["story_unit_min"] > batch["story_unit_max"]
        ):
            issues.append(
                ValidationIssue(
                    "run.policies.batch", "story_unit_min 不能大于 story_unit_max"
                )
            )
        if (
            isinstance(batch.get("ledger_batch_min"), int)
            and isinstance(batch.get("ledger_batch_max"), int)
            and batch["ledger_batch_min"] > batch["ledger_batch_max"]
        ):
            issues.append(
                ValidationIssue(
                    "run.policies.batch", "ledger_batch_min 不能大于 ledger_batch_max"
                )
            )
        if all(
            isinstance(batch.get(key), int)
            for key in (
                "outline_batch_size",
                "outline_request_chunk_size",
                "ledger_batch_size",
                "ledger_batch_min",
                "ledger_batch_max",
            )
        ):
            if not (
                batch["ledger_batch_min"]
                <= batch["outline_batch_size"]
                <= batch["ledger_batch_max"]
            ):
                issues.append(
                    ValidationIssue(
                        "run.policies.batch.outline_batch_size",
                        "必须落在 ledger_batch_min～ledger_batch_max 内",
                    )
                )
            if not (
                batch["ledger_batch_min"]
                <= batch["ledger_batch_size"]
                <= batch["ledger_batch_max"]
            ):
                issues.append(
                    ValidationIssue(
                        "run.policies.batch.ledger_batch_size",
                        "必须落在 ledger_batch_min～ledger_batch_max 内",
                    )
                )
            if batch["outline_batch_size"] != batch["ledger_batch_size"]:
                issues.append(
                    ValidationIssue(
                        "run.policies.batch",
                        "第一版要求 outline_batch_size 与 ledger_batch_size 相同",
                    )
                )
            if batch["outline_request_chunk_size"] > batch["outline_batch_size"]:
                issues.append(
                    ValidationIssue(
                        "run.policies.batch.outline_request_chunk_size",
                        "不能大于 outline_batch_size",
                    )
                )

    retry = policies.get("retry")
    if _expect_type(issues, "run.policies.retry", retry, dict):
        for key in ("transport", "format", "content"):
            value = retry.get(key)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                issues.append(
                    ValidationIssue(f"run.policies.retry.{key}", "应为非负整数")
                )
    budget = policies.get("budget")
    if _expect_type(issues, "run.policies.budget", budget, dict):
        max_calls = budget.get("max_calls")
        max_tokens = budget.get("max_tokens")
        max_cost = budget.get("max_cost")
        for key, value in (("max_calls", max_calls), ("max_tokens", max_tokens)):
            if value is not None and (
                not isinstance(value, int) or isinstance(value, bool) or value < 0
            ):
                issues.append(
                    ValidationIssue(
                        f"run.policies.budget.{key}", "应为非负整数或 null"
                    )
                )
        if max_cost is not None and (
            not isinstance(max_cost, (int, float))
            or isinstance(max_cost, bool)
            or max_cost < 0
        ):
            issues.append(
                ValidationIssue(
                    "run.policies.budget.max_cost", "应为非负数或 null"
                )
            )
    return issues


def _validate_progression(data: Any) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if not _expect_type(issues, "progression", data, dict):
        return issues
    _require_keys(
        issues,
        "progression",
        data,
        (
            "schema_version",
            "realms",
            "resources",
            "techniques",
            "artifacts",
            "injury_rules",
            "breakthrough_rules",
            "power_boundaries",
            "exceptions",
        ),
    )
    for key in (
        "realms",
        "resources",
        "techniques",
        "artifacts",
        "injury_rules",
        "breakthrough_rules",
        "power_boundaries",
        "exceptions",
    ):
        if key in data:
            _expect_type(issues, f"progression.{key}", data[key], list)
    return issues


def _validate_comedy(data: Any) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if not _expect_type(issues, "comedy_bible", data, dict):
        return issues
    _require_keys(
        issues,
        "comedy_bible",
        data,
        (
            "schema_version",
            "density",
            "protagonist_role",
            "character_contrasts",
            "allowed_mechanisms",
            "forbidden_humor",
            "language_boundaries",
            "callbacks",
            "fatigued_mechanisms",
            "serious_scene_limits",
        ),
    )
    if data.get("density") not in {"low", "medium", "high"}:
        issues.append(
            ValidationIssue("comedy_bible.density", "应为 low / medium / high")
        )
    if "protagonist_role" in data:
        _expect_type(
            issues, "comedy_bible.protagonist_role", data["protagonist_role"], str
        )
    for key in (
        "character_contrasts",
        "allowed_mechanisms",
        "forbidden_humor",
        "language_boundaries",
        "callbacks",
        "fatigued_mechanisms",
        "serious_scene_limits",
    ):
        if key in data:
            _expect_type(issues, f"comedy_bible.{key}", data[key], list)
    return issues


def _validate_initial_state(data: Any) -> list[ValidationIssue]:
    try:
        validate_initial_state(data)
    except StructuredStateError as exc:
        return [ValidationIssue("initial_state", str(exc))]
    return []


def _validate_list_file(data: Any, name: str) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    _expect_type(issues, name, data, list)
    return issues


def validate_run_directory(root: Path, run_id: str) -> ValidationReport:
    run_dir = resolve_run_dir(root, run_id)
    files: tuple[tuple[str, Any], ...] = (
        ("run.json", lambda data: _validate_run_json(data, run_id)),
        ("config/progression.json", _validate_progression),
        ("config/comedy-bible.json", _validate_comedy),
        ("config/initial-state.json", _validate_initial_state),
        (
            "config/master-plan.json",
            lambda data: [
                ValidationIssue(item.path, item.message)
                for item in validate_master_plan_data(data, complete=False)
            ],
        ),
        ("planning/story-units.json", lambda data: _validate_list_file(data, "story_units")),
        (
            "planning/chapter-outlines.json",
            lambda data: _validate_list_file(data, "chapter_outlines"),
        ),
        ("checks.json", lambda data: _validate_list_file(data, "checks")),
    )

    issues: list[ValidationIssue] = []
    for relative, validator in files:
        path = run_dir / relative
        try:
            data = read_json(path)
        except StorageError as exc:
            issues.append(ValidationIssue(relative, str(exc)))
            continue
        issues.extend(validator(data))
    return ValidationReport(run_id, not issues, tuple(issues))
