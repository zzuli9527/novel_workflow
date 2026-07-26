"""Install the authoritative workflow into isolated runner test roots."""

from __future__ import annotations

from pathlib import Path
import shutil


def install_minimal_workflow(root: Path) -> None:
    """Copy the real workflow so tests cannot drift onto an old fixture."""

    source = Path(__file__).resolve().parents[1] / "workflow"
    shutil.copytree(source, root / "workflow")
