from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from tools.novel_runner.matrix_coverage import (
    MATRIX_COVERAGE,
    generate_coverage_report,
)


class MatrixCoverageTests(unittest.TestCase):
    def test_matrix_declares_every_x_case_once(self) -> None:
        identifiers = [item["id"] for item in MATRIX_COVERAGE]
        self.assertEqual(identifiers, [f"X{number:02d}" for number in range(1, 16)])

    def test_repository_evidence_references_exist(self) -> None:
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            report = generate_coverage_report(root, output_dir=output_dir)
            self.assertTrue(report["all_evidence_found"])
            self.assertEqual(report["case_count"], 15)
            self.assertTrue((output_dir / "coverage-report.md").is_file())


if __name__ == "__main__":
    unittest.main()
