"""CLI handlers for planning, ledgers, and story-unit execution."""

from __future__ import annotations

import argparse
import sys

from ...ledger import LedgerError, build_ledger
from ...planning_service import PlanningServiceError, plan_chapter_batch, plan_story_unit
from ...provider import ProviderError
from ...storage import StorageError
from ...units import UnitRunnerError, run_unit
from ..providers import provider_from_args
from .common import EXIT_FAILED, EXIT_PASSED, _parse_range, _render_or_json


def _run_plan_unit(args: argparse.Namespace) -> int:
    try:
        result = plan_story_unit(
            args.root,
            args.run_id,
            args.chapters,
            provider_from_args(args),
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
            provider_from_args(args),
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


def _run_build_ledger(args: argparse.Namespace) -> int:
    try:
        start, end = _parse_range(args.chapter_range)
        result = build_ledger(
            args.root,
            args.run_id,
            start,
            end,
            provider_from_args(args),
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
            provider_from_args(args),
        )
    except (UnitRunnerError, ProviderError, StorageError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_FAILED
    _render_or_json(result, args.json)
    return EXIT_PASSED
