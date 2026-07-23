"""本地命令行入口。"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
from typing import Sequence

from .chapter_service import (
    ChapterServiceError,
    commit_chapter,
    draft_chapter,
    extract_state,
    get_run_status,
    repair_chapter,
    review_chapter,
    resume_run,
)
from .config import init_run, validate_run_directory
from .environment import EnvironmentError, load_project_environment
from .ledger import LedgerError, build_ledger
from .matrix_coverage import generate_coverage_report
from .master_plan import (
    MasterPlanError,
    approve_master_plan,
    validate_master_plan,
)
from .outline_validation import (
    OutlineValidationError,
    ensure_comedy_rotation,
    validate_outline,
)
from .plan_import import PlanImportError, import_plan
from .planning_service import (
    PlanningServiceError,
    plan_chapter_batch,
    plan_story_unit,
)
from .provider import (
    DirectoryFixtureProvider,
    FixtureProvider,
    OpenAIResponsesProvider,
    ProviderError,
    TaskRoutingProvider,
    TextProvider,
)
from .reporting import ReportingError, generate_unit_review
from .revision import RevisionError, invalidate_from
from .run_archive import RunArchiveError, archive_run
from .state_rebuild import StateRebuildError, rebuild_state_snapshots
from .storage_migration import StorageMigrationError, audit_storage_migration
from .storage import (
    StorageError,
    atomic_write_json,
    read_json,
    resolve_run_dir,
    run_lock,
)
from .unit_runner import UnitRunnerError, run_unit
from .wordcount import (
    DraftParseError,
    LengthPolicy,
    check_drafts,
    render_text_report,
)


EXIT_PASSED = 0
EXIT_FAILED = 1
EXIT_REVIEW_REQUIRED = 2
EXIT_INPUT_ERROR = 3


def _configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8")


def _add_single_provider_args(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--response-file", type=Path, help="本地固定响应文件")
    group.add_argument(
        "--openai",
        action="store_true",
        help="读取 run.json 的 provider 配置并调用 OpenAI Responses API",
    )


def _provider_from_args(args: argparse.Namespace) -> TextProvider:
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


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="novel")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser(
        "check-drafts", help="拆分 Markdown 章节并执行机械长度闸门"
    )
    check_parser.add_argument("path", type=Path, help="包含一章或多章的 Markdown 文件")
    check_parser.add_argument("--min", dest="target_min", type=int, default=2000)
    check_parser.add_argument("--max", dest="target_max", type=int, default=3000)
    check_parser.add_argument("--expand-from", type=int, default=1800)
    check_parser.add_argument("--review-over", type=int, default=3500)
    check_parser.add_argument(
        "--json", action="store_true", help="以 JSON 输出逐章检查结果"
    )

    init_parser = subparsers.add_parser("init", help="创建新的小说运行目录")
    init_parser.add_argument("run_id", help="运行标识")
    init_parser.add_argument(
        "--root", type=Path, default=Path.cwd(), help="项目根目录，默认为当前目录"
    )

    validate_parser = subparsers.add_parser(
        "validate-config", help="校验运行目录中的最小 JSON 配置"
    )
    validate_parser.add_argument("--run", dest="run_id", required=True)
    validate_parser.add_argument(
        "--root", type=Path, default=Path.cwd(), help="项目根目录，默认为当前目录"
    )
    validate_parser.add_argument("--json", action="store_true")

    validate_master_parser = subparsers.add_parser(
        "validate-master-plan", help="校验全书总纲是否达到人工审批条件"
    )
    validate_master_parser.add_argument("--run", dest="run_id", required=True)
    validate_master_parser.add_argument(
        "--root", type=Path, default=Path.cwd(), help="项目根目录，默认为当前目录"
    )
    validate_master_parser.add_argument("--json", action="store_true")

    approve_master_parser = subparsers.add_parser(
        "approve-master-plan", help="人工确认并批准当前全书总纲内容哈希"
    )
    approve_master_parser.add_argument("--run", dest="run_id", required=True)
    approve_master_parser.add_argument(
        "--root", type=Path, default=Path.cwd(), help="项目根目录，默认为当前目录"
    )
    approve_master_parser.add_argument("--json", action="store_true")

    validate_outline_parser = subparsers.add_parser(
        "validate-outline", help="校验单章细纲及其所在范围的喜剧机制轮换"
    )
    validate_outline_parser.add_argument("--run", dest="run_id", required=True)
    validate_outline_parser.add_argument("--chapter", type=int, required=True)
    validate_outline_parser.add_argument("--root", type=Path, default=Path.cwd())
    validate_outline_parser.add_argument("--json", action="store_true")
    validate_outline_parser.add_argument(
        "--accept-revision",
        action="store_true",
        help="机械校验通过后接受该章修订依赖重验",
    )

    import_parser = subparsers.add_parser(
        "import-plan", help="校验并导入工作流产出的故事单元与章节细纲"
    )
    import_parser.add_argument("--run", dest="run_id", required=True)
    import_parser.add_argument("--file", type=Path, required=True)
    import_parser.add_argument("--root", type=Path, default=Path.cwd())
    import_parser.add_argument("--json", action="store_true")

    plan_unit_parser = subparsers.add_parser(
        "plan-unit", help="依据项目资料生成一个 10～20 章故事单元"
    )
    plan_unit_parser.add_argument("--run", dest="run_id", required=True)
    plan_unit_parser.add_argument(
        "--chapters",
        type=int,
        help="兼容参数；如提供，必须与已批准总纲中的下一单元章数一致",
    )
    _add_single_provider_args(plan_unit_parser)
    plan_unit_parser.add_argument("--root", type=Path, default=Path.cwd())
    plan_unit_parser.add_argument("--json", action="store_true")

    plan_batch_parser = subparsers.add_parser(
        "plan-batch", help="为故事单元生成一个标准 3～5 章细纲批次"
    )
    plan_batch_parser.add_argument("--run", dest="run_id", required=True)
    plan_batch_parser.add_argument("--unit", dest="unit_id", required=True)
    plan_batch_parser.add_argument("--range", dest="chapter_range", required=True)
    _add_single_provider_args(plan_batch_parser)
    plan_batch_parser.add_argument("--root", type=Path, default=Path.cwd())
    plan_batch_parser.add_argument("--json", action="store_true")

    draft_parser = subparsers.add_parser(
        "draft", help="使用提供方响应生成并检查单章草稿"
    )
    draft_parser.add_argument("--run", dest="run_id", required=True)
    draft_parser.add_argument("--chapter", type=int, required=True)
    _add_single_provider_args(draft_parser)
    draft_parser.add_argument("--root", type=Path, default=Path.cwd())
    draft_parser.add_argument("--json", action="store_true")

    state_parser = subparsers.add_parser(
        "extract-state", help="使用提供方响应提取章节状态增量"
    )
    state_parser.add_argument("--run", dest="run_id", required=True)
    state_parser.add_argument("--chapter", type=int, required=True)
    _add_single_provider_args(state_parser)
    state_parser.add_argument("--root", type=Path, default=Path.cwd())
    state_parser.add_argument("--json", action="store_true")

    commit_parser = subparsers.add_parser("commit", help="提交已通过的章节与状态")
    commit_parser.add_argument("--run", dest="run_id", required=True)
    commit_parser.add_argument("--chapter", type=int, required=True)
    commit_parser.add_argument("--root", type=Path, default=Path.cwd())
    commit_parser.add_argument("--json", action="store_true")

    repair_parser = subparsers.add_parser(
        "repair", help="根据失败类型定向扩写、重写或重试当前章节"
    )
    repair_parser.add_argument("--run", dest="run_id", required=True)
    repair_parser.add_argument("--chapter", type=int, required=True)
    _add_single_provider_args(repair_parser)
    repair_parser.add_argument("--root", type=Path, default=Path.cwd())
    repair_parser.add_argument("--json", action="store_true")

    review_parser = subparsers.add_parser(
        "review-draft", help="对长度通过的候选正文执行剧情与质量契约评审"
    )
    review_parser.add_argument("--run", dest="run_id", required=True)
    review_parser.add_argument("--chapter", type=int, required=True)
    _add_single_provider_args(review_parser)
    review_parser.add_argument("--root", type=Path, default=Path.cwd())
    review_parser.add_argument("--json", action="store_true")

    status_parser = subparsers.add_parser("status", help="查看运行指针和章节状态")
    status_parser.add_argument("--run", dest="run_id", required=True)
    status_parser.add_argument("--root", type=Path, default=Path.cwd())
    status_parser.add_argument("--json", action="store_true")

    resume_parser = subparsers.add_parser("resume", help="恢复未完成的安全提交")
    resume_parser.add_argument("--run", dest="run_id", required=True)
    resume_parser.add_argument("--root", type=Path, default=Path.cwd())
    resume_parser.add_argument("--json", action="store_true")

    invalidate_parser = subparsers.add_parser(
        "invalidate-from",
        help="修订已提交章节前归档并失效该章及其后续依赖",
    )
    invalidate_parser.add_argument("--run", dest="run_id", required=True)
    invalidate_parser.add_argument("--chapter", type=int, required=True)
    invalidate_parser.add_argument("--reason", required=True)
    invalidate_parser.add_argument("--root", type=Path, default=Path.cwd())
    invalidate_parser.add_argument("--json", action="store_true")

    ledger_parser = subparsers.add_parser(
        "build-ledger", help="为连续已提交章节生成压缩账本"
    )
    ledger_parser.add_argument("--run", dest="run_id", required=True)
    ledger_parser.add_argument("--range", dest="chapter_range", required=True)
    _add_single_provider_args(ledger_parser)
    ledger_parser.add_argument("--root", type=Path, default=Path.cwd())
    ledger_parser.add_argument("--json", action="store_true")

    unit_parser = subparsers.add_parser(
        "run-unit", help="顺序执行一个已经规划好的 10～20 章故事单元"
    )
    unit_parser.add_argument("--run", dest="run_id", required=True)
    unit_parser.add_argument("--unit", dest="unit_id", required=True)
    unit_provider_group = unit_parser.add_mutually_exclusive_group(required=True)
    unit_provider_group.add_argument(
        "--fixture-dir",
        type=Path,
        help="当前阶段使用的目录夹具提供方",
    )
    unit_provider_group.add_argument(
        "--openai",
        action="store_true",
        help="读取 run.json 的 provider 配置并调用 OpenAI Responses API",
    )
    unit_parser.add_argument("--root", type=Path, default=Path.cwd())
    unit_parser.add_argument("--json", action="store_true")

    report_parser = subparsers.add_parser(
        "review", help="从正式产物生成故事单元指标与评审报告"
    )
    report_parser.add_argument("--run", dest="run_id", required=True)
    report_parser.add_argument("--unit", dest="unit_id", required=True)
    report_parser.add_argument("--root", type=Path, default=Path.cwd())
    report_parser.add_argument("--json", action="store_true")

    rebuild_parser = subparsers.add_parser(
        "rebuild-state", help="从初始状态与正式事件原子重建全部章节快照"
    )
    rebuild_parser.add_argument("--run", dest="run_id", required=True)
    rebuild_parser.add_argument("--root", type=Path, default=Path.cwd())
    rebuild_parser.add_argument("--json", action="store_true")

    migrate_parser = subparsers.add_parser(
        "migrate-storage", help="审计或迁移 v1 运行到 FileStorage v2"
    )
    migrate_parser.add_argument("--run", dest="run_id", required=True)
    migrate_parser.add_argument(
        "--apply", action="store_true", help="创建备份后执行原子切换；默认只 dry-run"
    )
    migrate_parser.add_argument("--root", type=Path, default=Path.cwd())
    migrate_parser.add_argument("--json", action="store_true")

    archive_parser = subparsers.add_parser(
        "archive-run", help="把已完成故事单元归档到 test/matrix-runs"
    )
    archive_parser.add_argument("--run", dest="run_id", required=True)
    archive_parser.add_argument("--unit", dest="unit_id", required=True)
    archive_parser.add_argument("--case", dest="case_id", required=True)
    archive_parser.add_argument("--root", type=Path, default=Path.cwd())
    archive_parser.add_argument("--json", action="store_true")

    coverage_parser = subparsers.add_parser(
        "coverage", help="生成 X01～X15 自动化测试证据映射"
    )
    coverage_parser.add_argument("--root", type=Path, default=Path.cwd())
    coverage_parser.add_argument("--json", action="store_true")
    return parser


def _run_check_drafts(args: argparse.Namespace) -> int:
    try:
        policy = LengthPolicy(
            target_min=args.target_min,
            target_max=args.target_max,
            expand_from=args.expand_from,
            review_over=args.review_over,
        )
        markdown = args.path.read_text(encoding="utf-8-sig")
        report = check_drafts(markdown, policy)
    except (OSError, UnicodeError, DraftParseError, ValueError) as exc:
        if args.json:
            print(
                json.dumps(
                    {"result": "input_error", "exit_code": EXIT_INPUT_ERROR, "error": str(exc)},
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            print(f"Error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR

    if args.json:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(render_text_report(report))
    return report.exit_code


def _run_init(args: argparse.Namespace) -> int:
    try:
        run_dir = init_run(args.root, args.run_id, storage_version="2.0")
    except StorageError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    print(f"Created run: {run_dir}")
    return EXIT_PASSED


def _run_validate_config(args: argparse.Namespace) -> int:
    try:
        report = validate_run_directory(args.root, args.run_id)
    except StorageError as exc:
        if args.json:
            print(
                json.dumps(
                    {"run_id": args.run_id, "valid": False, "issues": [{"path": "run", "message": str(exc)}]},
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            print(f"Error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR

    if args.json:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    elif report.valid:
        print(f"Run {report.run_id}: valid")
    else:
        print(f"Run {report.run_id}: invalid")
        for issue in report.issues:
            print(f"- {issue.path}: {issue.message}")
    return EXIT_PASSED if report.valid else EXIT_FAILED


def _run_validate_master_plan(args: argparse.Namespace) -> int:
    try:
        report = validate_master_plan(args.root, args.run_id)
    except StorageError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    if args.json:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    elif report.valid:
        print(f"Master plan {report.run_id}: valid ({report.status})")
    else:
        print(f"Master plan {report.run_id}: invalid ({report.status})")
        for issue in report.issues:
            print(f"- {issue.path}: {issue.message}")
    return EXIT_PASSED if report.valid else EXIT_FAILED


def _run_approve_master_plan(args: argparse.Namespace) -> int:
    try:
        result = approve_master_plan(args.root, args.run_id)
    except (MasterPlanError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_validate_outline(args: argparse.Namespace) -> int:
    try:
        run_dir = resolve_run_dir(args.root, args.run_id)
        with run_lock(run_dir):
            run = read_json(run_dir / "run.json")
            outlines = read_json(run_dir / "planning/chapter-outlines.json")
            matches = [
                (index, item)
                for index, item in enumerate(outlines)
                if item.get("number") == args.chapter
            ]
            if len(matches) != 1:
                raise StorageError(f"第 {args.chapter} 章细纲不存在或重复")
            outline_index, outline = matches[0]
            issues = [
                {"path": item.path, "message": item.message}
                for item in validate_outline(outline, run)
            ]
            if not issues:
                unit_id = outline.get("story_unit_id")
                units = read_json(run_dir / "planning/story-units.json")
                unit = next(
                    (item for item in units if item.get("unit_id") == unit_id), None
                )
                chapter_range = (
                    unit.get("chapter_range") if isinstance(unit, dict) else None
                )
                if isinstance(chapter_range, list) and len(chapter_range) == 2:
                    try:
                        ensure_comedy_rotation(
                            outlines, chapter_range[0], chapter_range[1]
                        )
                    except OutlineValidationError as exc:
                        issues.append(
                            {"path": "comedy_mechanism", "message": str(exc)}
                        )
            accepted_revision = False
            if args.accept_revision and not issues:
                if outline.get("revalidation_status") != "pending":
                    raise StorageError("该章没有待接受的修订重验")
                outlines[outline_index] = {
                    **outline,
                    "revalidation_status": "accepted",
                    "revalidated_at": datetime.now(timezone.utc).isoformat(),
                }
                atomic_write_json(
                    run_dir / "planning/chapter-outlines.json", outlines
                )
                chapter_dir = run_dir / f"chapters/{args.chapter:04d}"
                if chapter_dir.exists():
                    atomic_write_json(
                        chapter_dir / "outline.json", outlines[outline_index]
                    )
                accepted_revision = True
    except (StorageError, TypeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    result = {
        "run_id": args.run_id,
        "chapter": args.chapter,
        "valid": not issues,
        "issues": issues,
        "accepted_revision": accepted_revision,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif result["valid"]:
        print(f"Chapter {args.chapter}: valid")
    else:
        print(f"Chapter {args.chapter}: invalid")
        for issue in issues:
            print(f"- {issue['path']}: {issue['message']}")
    return EXIT_PASSED if result["valid"] else EXIT_FAILED


def _run_import_plan(args: argparse.Namespace) -> int:
    try:
        result = import_plan(args.root, args.run_id, args.file)
    except (PlanImportError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_plan_unit(args: argparse.Namespace) -> int:
    try:
        result = plan_story_unit(
            args.root,
            args.run_id,
            args.chapters,
            _provider_from_args(args),
        )
    except (PlanningServiceError, ProviderError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_plan_batch(args: argparse.Namespace) -> int:
    try:
        start, end = _parse_range(args.chapter_range)
        result = plan_chapter_batch(
            args.root,
            args.run_id,
            args.unit_id,
            start,
            end,
            _provider_from_args(args),
        )
    except (
        ValueError,
        PlanningServiceError,
        ProviderError,
        StorageError,
    ) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _render_or_json(data: object, as_json: bool) -> None:
    if as_json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(data)


def _run_draft(args: argparse.Namespace) -> int:
    try:
        result = draft_chapter(
            args.root,
            args.run_id,
            args.chapter,
            _provider_from_args(args),
        )
    except (ChapterServiceError, ProviderError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    status = result["outline"]["status"]
    if status == "draft_quality_pending":
        return EXIT_REVIEW_REQUIRED
    return EXIT_PASSED if status == "draft_passed" else EXIT_FAILED


def _run_extract_state(args: argparse.Namespace) -> int:
    try:
        event = extract_state(
            args.root,
            args.run_id,
            args.chapter,
            _provider_from_args(args),
        )
    except (ChapterServiceError, ProviderError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(event, args.json)
    return EXIT_PASSED


def _run_commit(args: argparse.Namespace) -> int:
    try:
        result = commit_chapter(args.root, args.run_id, args.chapter)
    except (ChapterServiceError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_repair(args: argparse.Namespace) -> int:
    try:
        result = repair_chapter(
            args.root,
            args.run_id,
            args.chapter,
            _provider_from_args(args),
        )
    except (ChapterServiceError, ProviderError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return (
        EXIT_REVIEW_REQUIRED
        if result["outline"]["status"] == "draft_quality_pending"
        else EXIT_FAILED
    )


def _run_review_draft(args: argparse.Namespace) -> int:
    try:
        result = review_chapter(
            args.root,
            args.run_id,
            args.chapter,
            _provider_from_args(args),
        )
    except (ChapterServiceError, ProviderError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED if result["outline"]["status"] == "draft_passed" else EXIT_FAILED


def _run_status(args: argparse.Namespace) -> int:
    try:
        result = get_run_status(args.root, args.run_id)
    except (ChapterServiceError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_resume(args: argparse.Namespace) -> int:
    try:
        result = resume_run(args.root, args.run_id)
    except (ChapterServiceError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_invalidate(args: argparse.Namespace) -> int:
    try:
        result = invalidate_from(
            args.root,
            args.run_id,
            args.chapter,
            reason=args.reason,
        )
    except (RevisionError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _parse_range(value: str) -> tuple[int, int]:
    normalized = value.replace("～", "-").replace("~", "-")
    parts = normalized.split("-", maxsplit=1)
    if len(parts) != 2 or not all(part.strip().isdigit() for part in parts):
        raise ValueError("章节范围格式应为 start-end")
    return int(parts[0]), int(parts[1])


def _run_build_ledger(args: argparse.Namespace) -> int:
    try:
        start, end = _parse_range(args.chapter_range)
        result = build_ledger(
            args.root,
            args.run_id,
            start,
            end,
            _provider_from_args(args),
        )
    except (ValueError, LedgerError, ProviderError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_unit(args: argparse.Namespace) -> int:
    try:
        result = run_unit(
            args.root,
            args.run_id,
            args.unit_id,
            _provider_from_args(args),
        )
    except (UnitRunnerError, ProviderError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_review(args: argparse.Namespace) -> int:
    try:
        result = generate_unit_review(args.root, args.run_id, args.unit_id)
    except (ReportingError, ProviderError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED if result["verdict"] == "通过" else EXIT_REVIEW_REQUIRED


def _run_rebuild_state(args: argparse.Namespace) -> int:
    try:
        result = rebuild_state_snapshots(args.root, args.run_id)
    except (StateRebuildError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_migrate_storage(args: argparse.Namespace) -> int:
    try:
        result = audit_storage_migration(args.root, args.run_id, apply=args.apply)
    except (StorageMigrationError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_archive(args: argparse.Namespace) -> int:
    try:
        result = archive_run(
            args.root, args.run_id, args.unit_id, args.case_id
        )
    except (RunArchiveError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED


def _run_coverage(args: argparse.Namespace) -> int:
    result = generate_coverage_report(args.root)
    _render_or_json(result, args.json)
    return EXIT_PASSED if result["all_evidence_found"] else EXIT_FAILED


def main(argv: Sequence[str] | None = None) -> int:
    _configure_stdio()
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        load_project_environment(getattr(args, "root", Path.cwd()))
    except EnvironmentError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    if args.command == "check-drafts":
        return _run_check_drafts(args)
    if args.command == "init":
        return _run_init(args)
    if args.command == "validate-config":
        return _run_validate_config(args)
    if args.command == "validate-master-plan":
        return _run_validate_master_plan(args)
    if args.command == "approve-master-plan":
        return _run_approve_master_plan(args)
    if args.command == "validate-outline":
        return _run_validate_outline(args)
    if args.command == "import-plan":
        return _run_import_plan(args)
    if args.command == "plan-unit":
        return _run_plan_unit(args)
    if args.command == "plan-batch":
        return _run_plan_batch(args)
    if args.command == "draft":
        return _run_draft(args)
    if args.command == "extract-state":
        return _run_extract_state(args)
    if args.command == "commit":
        return _run_commit(args)
    if args.command == "repair":
        return _run_repair(args)
    if args.command == "review-draft":
        return _run_review_draft(args)
    if args.command == "status":
        return _run_status(args)
    if args.command == "resume":
        return _run_resume(args)
    if args.command == "invalidate-from":
        return _run_invalidate(args)
    if args.command == "build-ledger":
        return _run_build_ledger(args)
    if args.command == "run-unit":
        return _run_unit(args)
    if args.command == "review":
        return _run_review(args)
    if args.command == "rebuild-state":
        return _run_rebuild_state(args)
    if args.command == "migrate-storage":
        return _run_migrate_storage(args)
    if args.command == "archive-run":
        return _run_archive(args)
    if args.command == "coverage":
        return _run_coverage(args)
    parser.error(f"未知命令：{args.command}")
    return EXIT_INPUT_ERROR


if __name__ == "__main__":
    raise SystemExit(main())
