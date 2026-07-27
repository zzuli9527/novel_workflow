"""Command-line argument definitions."""

from __future__ import annotations

import argparse
from pathlib import Path


def _add_single_provider_args(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--response-file", type=Path, help="本地固定响应文件")
    group.add_argument(
        "--openai",
        action="store_true",
        help="读取 run.json 的 provider 配置并调用 OpenAI Responses API",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="novel")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser(
        "check-drafts", help="拆分 Markdown 章节并执行机械长度闸门"
    )
    check_parser.add_argument("path", type=Path, help="包含一章或多章的 Markdown 文件")
    check_parser.add_argument("--min", dest="target_min", type=int, default=1800)
    check_parser.add_argument("--max", dest="target_max", type=int, default=3200)
    check_parser.add_argument("--expand-from", type=int, default=1600)
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
        "plan-batch", help="为故事单元生成一个标准 3～4 章细纲批次"
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
        "archive-run", help="把已完成故事单元归档到 tests/证据/矩阵运行"
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
