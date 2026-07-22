from __future__ import annotations

import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest

from tools.novel_runner.storage import RunLockedError, _process_alive, run_lock


class RunLockTests(unittest.TestCase):
    def test_nested_lock_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            with run_lock(run_dir):
                with self.assertRaises(RunLockedError):
                    with run_lock(run_dir):
                        pass
            self.assertFalse((run_dir / ".run.lock").exists())

    def test_stale_same_host_lock_is_recovered(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            lock_path = run_dir / ".run.lock"
            lock_path.write_text(
                json.dumps(
                    {
                        "pid": 2147483647,
                        "hostname": socket.gethostname(),
                        "created_at": "2000-01-01T00:00:00+00:00",
                    }
                ),
                encoding="utf-8",
            )
            with run_lock(run_dir):
                self.assertTrue(lock_path.exists())
            self.assertFalse(lock_path.exists())

    def test_unknown_lock_is_not_silently_removed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            (run_dir / ".run.lock").write_text("not-json", encoding="utf-8")
            with self.assertRaises(RunLockedError):
                with run_lock(run_dir):
                    pass

    def test_exited_process_is_not_treated_as_alive(self) -> None:
        child = subprocess.Popen([sys.executable, "-c", "pass"])
        child.wait(timeout=10)
        self.assertFalse(_process_alive(child.pid))


if __name__ == "__main__":
    unittest.main()
