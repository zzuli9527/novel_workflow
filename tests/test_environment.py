from __future__ import annotations

import os
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import unittest

from tools.novel_runner.environment import EnvironmentError, load_dotenv


class EnvironmentTests(unittest.TestCase):
    def test_loads_values_and_keeps_existing_environment(self) -> None:
        with TemporaryDirectory() as temporary, patch.dict(
            os.environ, {"EXISTING": "process"}, clear=False
        ):
            path = Path(temporary) / ".env"
            path.write_text(
                "# local settings\nNEW_VALUE='hello world'\nEXISTING=file\n",
                encoding="utf-8",
            )
            loaded = load_dotenv(path)
            self.assertEqual(os.environ["NEW_VALUE"], "hello world")
            self.assertEqual(os.environ["EXISTING"], "process")
            self.assertEqual(loaded, {"NEW_VALUE": "hello world"})
            os.environ.pop("NEW_VALUE", None)

    def test_override_replaces_existing_environment(self) -> None:
        with TemporaryDirectory() as temporary, patch.dict(
            os.environ, {"VALUE": "process"}, clear=False
        ):
            path = Path(temporary) / ".env"
            path.write_text("VALUE=file\n", encoding="utf-8")
            self.assertEqual(load_dotenv(path, override=True), {"VALUE": "file"})
            self.assertEqual(os.environ["VALUE"], "file")

    def test_rejects_malformed_line(self) -> None:
        with TemporaryDirectory() as temporary:
            path = Path(temporary) / ".env"
            path.write_text("NOT_A_PAIR\n", encoding="utf-8")
            with self.assertRaisesRegex(EnvironmentError, "缺少"):
                load_dotenv(path)


if __name__ == "__main__":
    unittest.main()
