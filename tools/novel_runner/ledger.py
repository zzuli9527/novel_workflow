"""3～5 章批次账本生成、校验和渲染。"""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

from .api_runtime import invoke_provider, mark_task_accepted
from .config import validate_run_directory
from .prompt_composer import compose_ledger_prompt
from .provider import GenerationRequest, ProviderError, TextProvider
from .state_store import load_events
from .file_storage import (
    events_path,
    is_v2,
    read_current_snapshot,
    write_current_ledger,
)
from .storage import (
    StorageError,
    atomic_write_json,
    atomic_write_text,
    read_json,
    resolve_run_dir,
    run_lock,
)


LEDGER_LIST_FIELDS = (
    "must_read_next",
    "active_progression",
    "active_resources",
    "active_relationships",
    "active_knowledge_gaps",
    "active_threads",
    "comedy_callbacks",
    "avoid_repeating",
    "archived",
    "next_batch_adjustments",
)


class LedgerError(RuntimeError):
    """批次账本输入或模型输出不合格。"""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_context(
    root: Path, run_id: str
) -> tuple[Path, dict[str, Any], list[dict[str, Any]]]:
    report = validate_run_directory(root, run_id)
    if not report.valid:
        details = "; ".join(f"{item.path}: {item.message}" for item in report.issues)
        raise LedgerError(f"运行配置无效：{details}")
    run_dir = resolve_run_dir(root, run_id)
    return (
        run_dir,
        read_json(run_dir / "run.json"),
        read_json(run_dir / "planning/chapter-outlines.json"),
    )


def _validate_range(
    run_config: dict[str, Any],
    outlines: list[dict[str, Any]],
    start_chapter: int,
    end_chapter: int,
) -> None:
    if start_chapter <= 0 or end_chapter < start_chapter:
        raise LedgerError("批次章节范围无效")
    size = end_chapter - start_chapter + 1
    batch = run_config["policies"]["batch"]
    if not batch["ledger_batch_min"] <= size <= batch["ledger_batch_max"]:
        raise LedgerError(
            f"批次账本必须覆盖 {batch['ledger_batch_min']}～"
            f"{batch['ledger_batch_max']} 章，当前为 {size} 章"
        )
    by_number = {item.get("number"): item for item in outlines}
    for chapter in range(start_chapter, end_chapter + 1):
        outline = by_number.get(chapter)
        if outline is None:
            raise LedgerError(f"缺少第 {chapter} 章细纲记录")
        if outline.get("status") not in {"committed", "locked"}:
            raise LedgerError(f"第 {chapter} 章尚未提交，不能进入账本")
    if run_config.get("last_committed_chapter", 0) < end_chapter:
        raise LedgerError("运行指针尚未到达批次结束章节")


def _parse_ledger(
    text: str,
    *,
    batch_id: str,
    start_chapter: int,
    end_chapter: int,
    item_limit: int,
    snapshot_path: str,
    event_ids: list[str],
    snapshot: dict[str, Any],
) -> dict[str, Any]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise LedgerError(
            f"账本输出不是有效 JSON：第 {exc.lineno} 行第 {exc.colno} 列"
        ) from exc
    if not isinstance(data, dict):
        raise LedgerError("账本输出必须是 JSON 对象")
    for field in LEDGER_LIST_FIELDS:
        if field not in data:
            raise LedgerError(f"账本缺少字段：{field}")
        if not isinstance(data[field], list):
            raise LedgerError(f"账本字段必须是数组：{field}")
    if len(data["must_read_next"]) > item_limit:
        raise LedgerError(
            f"must_read_next 超过上限 {item_limit}："
            f"当前 {len(data['must_read_next'])} 条"
        )
    structured = snapshot.get("structured_state")
    if not isinstance(structured, dict):
        raise LedgerError("批次结束快照缺少 structured_state")
    active_progression: list[dict[str, Any]] = []
    for item in structured.get("cultivation", []):
        if not isinstance(item, dict):
            continue
        subject_id = item.get("subject_id")
        stage = item.get("stage")
        if not isinstance(subject_id, str) or not isinstance(stage, str):
            raise LedgerError("structured_state.cultivation 存在无效主体或境界")
        limits = [
            value for value in item.get("limits", []) if isinstance(value, str)
        ]
        limits.extend(
            f"伤势：{value}"
            for value in item.get("injuries", [])
            if isinstance(value, str)
        )
        if not item.get("tracked_states") and item.get("last_kind") in {"injury", "recovery", "restriction"} and isinstance(
            item.get("last_change"), str
        ):
            limits.append(item["last_change"])
        active_progression.append(
            {
                "subject_id": subject_id,
                "stage": stage,
                "limits": list(dict.fromkeys(limits)),
            }
        )

    active_resources: list[dict[str, Any]] = []
    for item in structured.get("resources", []):
        if not isinstance(item, dict) or not isinstance(item.get("amount"), (int, float)):
            continue
        if float(item["amount"]) <= 0:
            continue
        active_resources.append(
            {
                "owner_id": item.get("owner_id"),
                "resource_id": item.get("resource_id"),
                "amount": item.get("amount"),
                "unit": item.get("unit"),
            }
        )

    active_knowledge_gaps: list[dict[str, Any]] = []
    for item in structured.get("knowledge", []):
        if not isinstance(item, dict) or item.get("state") == "knows":
            continue
        active_knowledge_gaps.append(
            {
                "character_id": item.get("character_id"),
                "fact_id": item.get("fact_id"),
                "state": item.get("state"),
                "belief": item.get("belief"),
            }
        )
    data["active_progression"] = active_progression
    data["active_resources"] = active_resources
    data["active_knowledge_gaps"] = active_knowledge_gaps
    return {
        "batch_id": batch_id,
        "chapter_range": [start_chapter, end_chapter],
        **{field: data[field] for field in LEDGER_LIST_FIELDS},
        "source_snapshot": snapshot_path,
        "source_event_ids": event_ids,
        "created_at": _utc_now(),
    }


def render_ledger_markdown(ledger: dict[str, Any]) -> str:
    titles = (
        ("must_read_next", "下一批必读"),
        ("active_progression", "修炼状态与限制"),
        ("active_resources", "关键资源"),
        ("active_relationships", "关系与义务"),
        ("active_knowledge_gaps", "知识差与误会"),
        ("active_threads", "活跃线程"),
        ("comedy_callbacks", "喜剧回调"),
        ("avoid_repeating", "暂停使用 / 避免重复"),
        ("archived", "可归档"),
        ("next_batch_adjustments", "下一批调整"),
    )
    start, end = ledger["chapter_range"]
    lines = [f"# 批次账本：第 {start}～{end} 章", ""]
    for key, title in titles:
        lines.extend((f"## {title}", ""))
        items = ledger.get(key, [])
        if not items:
            lines.extend(("- 无", ""))
            continue
        for item in items:
            if isinstance(item, str):
                rendered = item
            else:
                rendered = json.dumps(item, ensure_ascii=False, separators=(",", ":"))
            lines.append(f"- {rendered}")
        lines.append("")
    return "\n".join(lines)


def _next_raw_version(ledger_dir: Path, batch_id: str) -> int:
    versions: list[int] = []
    for path in ledger_dir.glob(f"{batch_id}.raw.v*.json"):
        middle = path.name.removeprefix(f"{batch_id}.raw.v").removesuffix(".json")
        if middle.isdigit():
            versions.append(int(middle))
    return max(versions, default=0) + 1


def build_ledger(
    root: Path,
    run_id: str,
    start_chapter: int,
    end_chapter: int,
    provider: TextProvider,
) -> dict[str, Any]:
    run_dir = resolve_run_dir(root, run_id)
    with run_lock(run_dir):
        run_dir, run_config, outlines = _load_context(root, run_id)
        _validate_range(run_config, outlines, start_chapter, end_chapter)

        if is_v2(run_config):
            snapshot = read_current_snapshot(run_dir, run_config, end_chapter)
            if snapshot is None:
                raise LedgerError("v2 当前快照不存在")
            snapshot_path = run_dir / "state/current.json"
        else:
            snapshot_path = run_dir / f"state/snapshots/chapter-{end_chapter:04d}.json"
            snapshot = read_json(snapshot_path)
        event_ids = snapshot.get("event_ids")
        if not isinstance(event_ids, list):
            raise LedgerError("批次结束快照缺少 event_ids")
        wanted = {f"chapter-{chapter:04d}" for chapter in range(start_chapter, end_chapter + 1)}
        events = [
            item
            for item in load_events(events_path(run_dir))
            if item.get("event_id") in wanted
        ]
        if len(events) != end_chapter - start_chapter + 1:
            raise LedgerError("批次状态事件不完整")

        item_limit = run_config["policies"]["batch"]["ledger_item_limit"]
        prompt = compose_ledger_prompt(
            root,
            run_dir,
            start_chapter,
            end_chapter,
            snapshot,
            events,
            item_limit,
        )
        batch_id = f"batch-{start_chapter:04d}-{end_chapter:04d}"
        ledger_dir = run_dir / "ledgers"
        version = _next_raw_version(ledger_dir, batch_id)
        prompt_path = ledger_dir / f"{batch_id}.prompt.v{version}.md"
        atomic_write_text(prompt_path, prompt)
        atomic_write_text(ledger_dir / f"{batch_id}.prompt.md", prompt)

        raw_path = ledger_dir / f"{batch_id}.raw.v{version}.json"
        request = GenerationRequest(
            task="build_ledger",
            prompt=prompt,
            metadata={
                "run_id": run_id,
                "start_chapter": start_chapter,
                "end_chapter": end_chapter,
            },
        )
        try:
            response = invoke_provider(
                run_dir,
                provider,
                request,
                prompt_path=prompt_path,
                output_path=raw_path,
            )
        except ProviderError as exc:
            raise LedgerError(str(exc)) from exc

        ledger = _parse_ledger(
            response.text,
            batch_id=batch_id,
            start_chapter=start_chapter,
            end_chapter=end_chapter,
            item_limit=item_limit,
            snapshot_path=snapshot_path.relative_to(run_dir).as_posix(),
            event_ids=[item["event_id"] for item in events],
            snapshot=snapshot,
        )
        mark_task_accepted(run_dir, request, response, raw_path)
        final_json = ledger_dir / f"{batch_id}.json"
        final_md = ledger_dir / f"{batch_id}.md"
        atomic_write_json(final_json, ledger)
        atomic_write_text(final_md, render_ledger_markdown(ledger))
        write_current_ledger(run_dir, run_config, ledger)
        return ledger
