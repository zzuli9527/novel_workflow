from __future__ import annotations

import ast
from pathlib import Path
import unittest


PACKAGE_ROOT = Path(__file__).resolve().parents[1] / "tools/novel_runner"
REMOVED_LEGACY_ENTRY_POINTS = {
    "chapter_service.py",
    "prompt_composer.py",
    "unit_runner.py",
    "workflow_loader.py",
}
IMPLEMENTATION_PACKAGES = {
    "chapters",
    "commands",
    "prompting",
    "shared",
    "units",
    "workflow_runtime",
}


def _module_name(path: Path) -> str:
    parts = list(path.relative_to(PACKAGE_ROOT).with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(("novel_runner", *parts))


def _dependency_graph() -> dict[str, set[str]]:
    paths = list(PACKAGE_ROOT.rglob("*.py"))
    modules = {_module_name(path): path for path in paths}
    graph = {module: set() for module in modules}
    for module, path in modules.items():
        tree = ast.parse(path.read_text(encoding="utf-8-sig"))
        package = module if path.name == "__init__.py" else module.rsplit(".", 1)[0]
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.level:
                    base = package.split(".")
                    base = base[: len(base) - (node.level - 1)]
                    suffix = (node.module or "").split(".") if node.module else []
                    target = ".".join((*base, *suffix))
                else:
                    target = node.module or ""
                if target in modules:
                    graph[module].add(target)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name in modules:
                        graph[module].add(alias.name)
    return graph


class ToolsArchitectureTests(unittest.TestCase):
    def test_expected_implementation_packages_exist(self) -> None:
        for name in IMPLEMENTATION_PACKAGES:
            self.assertTrue((PACKAGE_ROOT / name / "__init__.py").is_file(), name)

    def test_legacy_entry_points_stay_removed(self) -> None:
        for name in REMOVED_LEGACY_ENTRY_POINTS:
            self.assertFalse((PACKAGE_ROOT / name).exists(), name)
        self.assertLessEqual(
            len((PACKAGE_ROOT / "cli.py").read_text(encoding="utf-8-sig").splitlines()),
            60,
        )

    def test_implementation_does_not_import_public_facades(self) -> None:
        forbidden = {Path(name).stem for name in REMOVED_LEGACY_ENTRY_POINTS}
        for package in IMPLEMENTATION_PACKAGES:
            for path in (PACKAGE_ROOT / package).rglob("*.py"):
                tree = ast.parse(path.read_text(encoding="utf-8-sig"))
                imported = {
                    node.module.split(".")[-1]
                    for node in ast.walk(tree)
                    if isinstance(node, ast.ImportFrom) and node.module
                }
                self.assertFalse(forbidden & imported, path.as_posix())

    def test_implementation_modules_stay_focused(self) -> None:
        for package in IMPLEMENTATION_PACKAGES:
            for path in (PACKAGE_ROOT / package).rglob("*.py"):
                lines = len(path.read_text(encoding="utf-8-sig").splitlines())
                self.assertLessEqual(lines, 400, path.as_posix())

    def test_no_exact_duplicate_multistatement_functions(self) -> None:
        bodies: dict[str, list[str]] = {}
        for path in PACKAGE_ROOT.rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8-sig"))
            for node in ast.walk(tree):
                if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if len(node.body) < 2:
                    continue
                body = ast.dump(
                    ast.Module(body=node.body, type_ignores=[]),
                    include_attributes=False,
                )
                bodies.setdefault(body, []).append(
                    f"{path.relative_to(PACKAGE_ROOT).as_posix()}:{node.lineno}:{node.name}"
                )
        duplicates = [locations for locations in bodies.values() if len(locations) > 1]
        self.assertEqual(duplicates, [])

    def test_utc_clock_has_one_definition(self) -> None:
        definitions: list[str] = []
        for path in PACKAGE_ROOT.rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8-sig"))
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name in {"utc_now", "_utc_now"}:
                    definitions.append(
                        f"{path.relative_to(PACKAGE_ROOT).as_posix()}:{node.lineno}:{node.name}"
                    )
        self.assertEqual(definitions, ["shared/clock.py:8:utc_now"])

    def test_internal_import_graph_has_no_cycles(self) -> None:
        graph = _dependency_graph()
        visited: set[str] = set()
        active: list[str] = []

        def visit(module: str) -> None:
            if module in active:
                cycle = " -> ".join((*active[active.index(module) :], module))
                self.fail(f"检测到代码依赖环：{cycle}")
            if module in visited:
                return
            active.append(module)
            for dependency in sorted(graph[module]):
                visit(dependency)
            active.pop()
            visited.add(module)

        for module in sorted(graph):
            visit(module)


if __name__ == "__main__":
    unittest.main()
