"""Dispatch parsed commands to focused handler modules."""

from __future__ import annotations

import argparse

from .chapters import _run_commit, _run_draft, _run_extract_state, _run_invalidate, _run_repair, _run_resume, _run_review_draft, _run_status
from .common import EXIT_FAILED, EXIT_INPUT_ERROR, EXIT_PASSED, EXIT_REVIEW_REQUIRED
from .maintenance import _run_archive, _run_coverage, _run_migrate_storage, _run_rebuild_state, _run_review
from .planning import _run_build_ledger, _run_plan_batch, _run_plan_unit, _run_unit
from .validation import _run_approve_master_plan, _run_check_drafts, _run_import_plan, _run_init, _run_validate_config, _run_validate_master_plan, _run_validate_outline


_COMMAND_HANDLERS = {
    "check-drafts": _run_check_drafts,
    "init": _run_init,
    "validate-config": _run_validate_config,
    "validate-master-plan": _run_validate_master_plan,
    "approve-master-plan": _run_approve_master_plan,
    "validate-outline": _run_validate_outline,
    "import-plan": _run_import_plan,
    "plan-unit": _run_plan_unit,
    "plan-batch": _run_plan_batch,
    "draft": _run_draft,
    "extract-state": _run_extract_state,
    "commit": _run_commit,
    "repair": _run_repair,
    "review-draft": _run_review_draft,
    "status": _run_status,
    "resume": _run_resume,
    "invalidate-from": _run_invalidate,
    "build-ledger": _run_build_ledger,
    "run-unit": _run_unit,
    "review": _run_review,
    "rebuild-state": _run_rebuild_state,
    "migrate-storage": _run_migrate_storage,
    "archive-run": _run_archive,
    "coverage": _run_coverage,
}


def run_command(args: argparse.Namespace) -> int:
    """Dispatch one parsed command without coupling the entry point to services."""

    handler = _COMMAND_HANDLERS.get(args.command)
    if handler is None:
        raise ValueError(f"未知命令：{args.command}")
    return handler(args)
