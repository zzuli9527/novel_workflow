"""CLI handlers for initialization and structural validation."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import sys

from ...config import init_run, validate_run_directory
from ...master_plan import MasterPlanError, approve_master_plan, validate_master_plan
from ...outline_validation import OutlineValidationError, ensure_comedy_rotation, validate_outline
from ...plan_import import PlanImportError, import_plan
from ...storage import StorageError, atomic_write_json, read_json, resolve_run_dir, run_lock
from ...wordcount import DraftParseError, LengthPolicy, check_drafts, render_text_report
from .common import EXIT_FAILED, EXIT_INPUT_ERROR, EXIT_PASSED, _render_or_json


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
