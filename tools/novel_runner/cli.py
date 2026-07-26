"""Public command-line entry point."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Sequence

from .commands import EXIT_INPUT_ERROR, build_parser, run_command
from .environment import EnvironmentError, load_project_environment


def _configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    _configure_stdio()
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        load_project_environment(getattr(args, "root", Path.cwd()))
        return run_command(args)
    except EnvironmentError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    except ValueError as exc:
        parser.error(str(exc))
        return EXIT_INPUT_ERROR


if __name__ == "__main__":
    raise SystemExit(main())
