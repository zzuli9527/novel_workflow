"""专项测试矩阵与自动化测试证据的可审计映射。"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .storage import atomic_write_json, atomic_write_text


MATRIX_COVERAGE: tuple[dict[str, Any], ...] = (
    {
        "id": "X01",
        "status": "partial",
        "evidence": [("tests/test_outline_validation.py", "test_rejects_missing_dual_engine_fields")],
        "remaining": "需要真实首章正文验证修仙问题与喜剧气质是否同时成立。",
    },
    {
        "id": "X02",
        "status": "automated_flow_pass",
        "evidence": [("tests/test_long_workload.py", "test_twelve_chapters_keep_real_length_and_state_chain")],
        "remaining": "真实模型仍需验证不靠重复和摘要凑足长度。",
    },
    {
        "id": "X03",
        "status": "partial",
        "evidence": [
            ("tests/test_chapter_service.py", "test_quality_review_blocks_cultivation_inconsistency"),
            ("tests/test_chapter_service.py", "test_state_change_requires_exact_draft_evidence"),
        ],
        "remaining": "需要带具体境界、伤势和能力限制的多章正文样例。",
    },
    {
        "id": "X04",
        "status": "automated_flow_pass",
        "evidence": [("tests/test_structured_state.py", "test_breakthrough_without_cost_is_rejected")],
        "remaining": "结构化事件已强制前置、成本和新限制；真实突破场景仍需正文验证。",
    },
    {
        "id": "X05",
        "status": "automated_flow_pass",
        "evidence": [
            ("tests/test_structured_state.py", "test_resource_balance_is_mechanically_projected"),
            ("tests/test_chapter_service.py", "test_continuity_failure_does_not_append_state_event"),
        ],
        "remaining": "余额、来源去向和正文证据已机械核验；真实资源叙事仍需正文验证。",
    },
    {
        "id": "X06",
        "status": "automated_flow_pass",
        "evidence": [
            ("tests/test_outline_validation.py", "test_rejects_three_identical_comedy_mechanisms"),
            ("tests/test_plan_import.py", "test_rejects_three_identical_comedy_mechanisms"),
        ],
        "remaining": "真实笑点是否有效仍需正文评审。",
    },
    {
        "id": "X07",
        "status": "automated_flow_pass",
        "evidence": [("tests/test_structured_state.py", "test_knowledge_state_is_projected_per_character_across_chapters")],
        "remaining": "已按角色和事实投影知识状态；复杂误会的文学合理性仍需正文验证。",
    },
    {
        "id": "X08",
        "status": "partial",
        "evidence": [("tests/test_chapter_service.py", "test_quality_review_allows_soft_quality_warnings")],
        "remaining": "已有独立软质量告警，角色声音是否真正鲜明仍需真实正文验证。",
    },
    {
        "id": "X09",
        "status": "automated_flow_pass",
        "evidence": [("tests/test_plan_import.py", "test_rejects_complete_unit_without_setback_mapping")],
        "remaining": "章纲必须明确承载真实受挫；失败后果与追读动力仍需真实正文验证。",
    },
    {
        "id": "X10",
        "status": "partial",
        "evidence": [("tests/test_chapter_service.py", "test_quality_review_blocks_comedy_that_erases_consequence")],
        "remaining": "需要严肃损失场景的独立正文样例。",
    },
    {
        "id": "X11",
        "status": "partial",
        "evidence": [("tests/test_chapter_service.py", "test_quality_review_blocks_disconnected_multi_line_plot")],
        "remaining": "已有多线因果闸门，仍需真实多线交汇正文样例。",
    },
    {
        "id": "X12",
        "status": "automated_flow_pass",
        "evidence": [
            ("tests/test_ledger.py", "test_builds_json_and_markdown_ledger"),
            ("tests/test_ledger.py", "test_fills_structured_active_state_when_model_omits_it"),
            ("tests/test_long_workload.py", "test_twelve_chapters_keep_real_length_and_state_chain"),
            ("tests/test_unit_runner.py", "test_run_unit_plans_each_missing_batch_after_previous_ledger"),
        ],
        "remaining": "离线已证明下一批章纲和正文 Prompt 使用首批账本；真实模型需验证信息充分性。",
    },
    {
        "id": "X13",
        "status": "automated_flow_pass",
        "evidence": [
            ("tests/test_plan_import.py", "test_rejects_complete_unit_without_final_payoff_mapping"),
            ("tests/test_unit_runner.py", "test_runs_ten_chapter_unit_to_completion"),
        ],
        "remaining": "末章兑现和退出状态已绑定章纲，文学兑现仍需真实正文。",
    },
    {
        "id": "X14",
        "status": "automated_flow_pass",
        "evidence": [("tests/test_long_workload.py", "test_twelve_chapters_keep_real_length_and_state_chain")],
        "remaining": "已完成 12 章、约 2.4 万以上正文字符的离线长链路负载测试。",
    },
    {
        "id": "X15",
        "status": "automated_flow_pass",
        "evidence": [
            ("tests/test_unit_runner.py", "test_failure_pauses_unit_and_does_not_advance_later_chapters"),
            ("tests/test_chapter_service.py", "test_resume_completes_prepared_commit_journal"),
            ("tests/test_revision.py", "test_revision_journal_can_resume_after_interruption"),
        ],
        "remaining": "真实网络中断仍需在获批调用后验证。",
    },
)


def _verify_evidence(root: Path, path: str, test_name: str) -> bool:
    source = root / path
    if not source.exists():
        return False
    try:
        text = source.read_text(encoding="utf-8-sig")
    except OSError:
        return False
    return f"def {test_name}(" in text


def _render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# X01～X15 自动化覆盖报告",
        "",
        "状态含义：`automated_flow_pass` 证明执行器闸门和链路；`partial` 只证明部分规则；`real_model_required` 必须用真实正文补证。",
        "",
        "| 编号 | 状态 | 自动化证据 | 尚缺验证 |",
        "| --- | --- | --- | --- |",
    ]
    for item in report["cases"]:
        evidence = "<br>".join(
            f"`{entry['path']}::{entry['test']}`" for entry in item["evidence"]
        ) or "无"
        lines.append(
            f"| {item['id']} | {item['status']} | {evidence} | {item['remaining']} |"
        )
    lines.extend(
        (
            "",
            f"证据引用完整：{'是' if report['all_evidence_found'] else '否'}",
            "",
        )
    )
    return "\n".join(lines)


def generate_coverage_report(
    root: Path, *, output_dir: Path | None = None
) -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    all_evidence_found = True
    for item in MATRIX_COVERAGE:
        evidence = []
        for path, test_name in item["evidence"]:
            found = _verify_evidence(root, path, test_name)
            all_evidence_found = all_evidence_found and found
            evidence.append({"path": path, "test": test_name, "found": found})
        cases.append({**item, "evidence": evidence})
    report = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "case_count": len(cases),
        "all_evidence_found": all_evidence_found,
        "status_counts": {
            status: sum(item["status"] == status for item in cases)
            for status in ("automated_flow_pass", "partial", "real_model_required")
        },
        "cases": cases,
    }
    destination = output_dir or (root / "test")
    atomic_write_json(destination / "coverage-report.json", report)
    atomic_write_text(destination / "coverage-report.md", _render_markdown(report))
    return report
