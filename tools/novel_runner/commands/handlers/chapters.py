"""CLI handlers for chapter drafting, review, state, commit, and recovery."""

from __future__ import annotations

import argparse
import sys

from ...chapters import ChapterServiceError, commit_chapter, draft_chapter, extract_state, get_run_status, repair_chapter, review_chapter, resume_run
from ...provider import ProviderError
from ...revision import RevisionError, invalidate_from
from ...storage import StorageError
from ..providers import provider_from_args
from .common import EXIT_FAILED, EXIT_PASSED, EXIT_REVIEW_REQUIRED, _render_or_json


def _run_draft(args: argparse.Namespace) -> int:
    try:
        result = draft_chapter(
            args.root,
            args.run_id,
            args.chapter,
            provider_from_args(args),
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
            provider_from_args(args),
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
            provider_from_args(args),
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
            provider_from_args(args),
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
