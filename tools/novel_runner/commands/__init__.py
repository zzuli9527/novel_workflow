"""Command-line parsing, provider construction, and command dispatch."""

from .handlers import EXIT_FAILED, EXIT_INPUT_ERROR, EXIT_PASSED, EXIT_REVIEW_REQUIRED, run_command
from .parser import build_parser

__all__ = [
    "EXIT_FAILED",
    "EXIT_INPUT_ERROR",
    "EXIT_PASSED",
    "EXIT_REVIEW_REQUIRED",
    "build_parser",
    "run_command",
]
