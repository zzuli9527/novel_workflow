"""CLI handlers for reports, rebuilds, migration, archive, and coverage."""

from __future__ import annotations

import argparse
import sys

from ...matrix_coverage import generate_coverage_report
from ...provider import ProviderError
from ...reporting import ReportingError, generate_unit_review
from ...run_archive import RunArchiveError, archive_run
from ...state_rebuild import StateRebuildError, rebuild_state_snapshots
from ...storage import StorageError
from ...storage_migration import StorageMigrationError, audit_storage_migration
from .common import EXIT_FAILED, EXIT_PASSED, EXIT_REVIEW_REQUIRED, _render_or_json


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
