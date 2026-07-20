"""运行目录和 JSON 文件的安全读写。"""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import socket
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Any


RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")


class StorageError(RuntimeError):
    """运行目录或文件读写失败。"""


class RunLockedError(StorageError):
    """运行正在被另一个进程使用。"""


def validate_run_id(run_id: str) -> str:
    if not RUN_ID_RE.fullmatch(run_id):
        raise StorageError(
            "run-id 只能包含字母、数字、点、下划线和连字符，且长度为 1～64"
        )
    return run_id


def resolve_runs_root(root: Path) -> Path:
    return (root.resolve() / "runs").resolve()


def resolve_run_dir(root: Path, run_id: str) -> Path:
    validate_run_id(run_id)
    runs_root = resolve_runs_root(root)
    run_dir = (runs_root / run_id).resolve()
    if run_dir.parent != runs_root:
        raise StorageError("run-id 解析后越出 runs 目录")
    return run_dir


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError as exc:
        raise StorageError(f"文件不存在：{path}") from exc
    except json.JSONDecodeError as exc:
        raise StorageError(
            f"JSON 无法解析：{path}，第 {exc.lineno} 行第 {exc.colno} 列"
        ) from exc
    except OSError as exc:
        raise StorageError(f"无法读取文件：{path}：{exc}") from exc


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    try:
        temp_path.write_text(content, encoding="utf-8", newline="\n")
        os.replace(temp_path, path)
    except OSError as exc:
        try:
            temp_path.unlink(missing_ok=True)
        except OSError:
            pass
        raise StorageError(f"无法写入文件：{path}：{exc}") from exc


def atomic_write_json(path: Path, data: Any) -> None:
    content = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    atomic_write_text(path, content)


def append_jsonl(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n"
    try:
        with path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(line)
            handle.flush()
            os.fsync(handle.fileno())
    except OSError as exc:
        raise StorageError(f"无法追加文件：{path}：{exc}") from exc


def _process_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


def _lock_is_stale(lock_path: Path) -> bool:
    try:
        data = json.loads(lock_path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return False
    pid = data.get("pid")
    hostname = data.get("hostname")
    return (
        isinstance(pid, int)
        and hostname == socket.gethostname()
        and not _process_alive(pid)
    )


@contextmanager
def run_lock(run_dir: Path):
    """使用独占文件锁保护一次运行的写操作。

    同一主机上由已退出进程遗留的锁会自动清理；无法证明失效的锁不会被覆盖。
    """

    lock_path = run_dir / ".run.lock"
    if lock_path.exists() and _lock_is_stale(lock_path):
        try:
            lock_path.unlink()
        except OSError as exc:
            raise RunLockedError(f"无法清理失效运行锁：{lock_path}") from exc

    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
    try:
        descriptor = os.open(lock_path, flags)
    except FileExistsError as exc:
        raise RunLockedError(f"运行已被锁定：{run_dir}") from exc
    try:
        payload = {
            "pid": os.getpid(),
            "hostname": socket.gethostname(),
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        yield
    finally:
        try:
            lock_path.unlink(missing_ok=True)
        except OSError:
            pass
