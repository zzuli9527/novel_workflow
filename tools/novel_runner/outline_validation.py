"""章节细纲的机械可写性与双引擎字段校验。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .state_machine import CHAPTER_STATUSES


@dataclass(frozen=True, slots=True)
class OutlineIssue:
    path: str
    message: str


class OutlineValidationError(RuntimeError):
    """章节细纲无法安全进入正文阶段。"""


def validate_outline(
    outline: dict[str, Any], run_config: dict[str, Any]
) -> tuple[OutlineIssue, ...]:
    issues: list[OutlineIssue] = []

    def require_text(key: str) -> None:
        value = outline.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(OutlineIssue(key, "必须是非空字符串"))

    for key in (
        "chapter_id",
        "title",
        "intent",
        "progression_payoff",
        "comedy_mechanism",
        "comedy_payoff",
        "cost_or_aftereffect",
    ):
        require_text(key)

    number = outline.get("number")
    if not isinstance(number, int) or isinstance(number, bool) or number <= 0:
        issues.append(OutlineIssue("number", "必须是正整数"))
    if outline.get("status") not in CHAPTER_STATUSES:
        issues.append(OutlineIssue("status", "不是允许的章节状态"))

    for key in (
        "opening_state",
        "required_outcomes",
        "forbidden_outcomes",
        "closing_state",
        "next_chapter_input",
    ):
        if not isinstance(outline.get(key), list):
            issues.append(OutlineIssue(key, "必须是数组"))
    for key in ("closing_state", "next_chapter_input"):
        value = outline.get(key)
        if isinstance(value, list) and not value:
            issues.append(OutlineIssue(key, "必须至少包含一条可承接状态"))

    target = outline.get("target_length")
    target_min = target_max = None
    if not isinstance(target, dict):
        issues.append(OutlineIssue("target_length", "必须是对象"))
    else:
        target_min = target.get("min")
        target_max = target.get("max")
        if (
            not isinstance(target_min, int)
            or isinstance(target_min, bool)
            or target_min <= 0
        ):
            issues.append(OutlineIssue("target_length.min", "必须是正整数"))
        if (
            not isinstance(target_max, int)
            or isinstance(target_max, bool)
            or target_max <= 0
        ):
            issues.append(OutlineIssue("target_length.max", "必须是正整数"))
        if isinstance(target_min, int) and isinstance(target_max, int) and target_min > target_max:
            issues.append(OutlineIssue("target_length", "min 不能大于 max"))
        policy = run_config["policies"]["length"]
        if isinstance(target_min, int) and target_min < policy["target_min"]:
            issues.append(OutlineIssue("target_length.min", "低于运行最小目标"))
        if isinstance(target_max, int) and target_max > policy["review_over"]:
            issues.append(OutlineIssue("target_length.max", "超过运行超长复查边界"))

    scenes = outline.get("scenes")
    scene_total = 0
    if not isinstance(scenes, list) or len(scenes) < 2:
        issues.append(OutlineIssue("scenes", "默认至少需要两个有效场景"))
    else:
        for index, scene in enumerate(scenes):
            prefix = f"scenes[{index}]"
            if not isinstance(scene, dict):
                issues.append(OutlineIssue(prefix, "必须是对象"))
                continue
            for key in ("scene_id", "intent"):
                value = scene.get(key)
                if not isinstance(value, str) or not value.strip():
                    issues.append(OutlineIssue(f"{prefix}.{key}", "必须是非空字符串"))
            length = scene.get("target_length")
            if not isinstance(length, int) or isinstance(length, bool) or length <= 0:
                issues.append(OutlineIssue(f"{prefix}.target_length", "必须是正整数"))
            else:
                scene_total += length
            if not isinstance(scene.get("required_outcomes"), list):
                issues.append(OutlineIssue(f"{prefix}.required_outcomes", "必须是数组"))
    if isinstance(target_min, int) and scene_total < target_min:
        issues.append(OutlineIssue("scenes", "场景预算合计低于章节最低目标"))
    if isinstance(target_max, int) and scene_total > int(target_max * 1.2):
        issues.append(OutlineIssue("scenes", "场景预算合计明显高于章节目标"))

    writability = outline.get("writability")
    if not isinstance(writability, dict):
        issues.append(OutlineIssue("writability", "必须是对象"))
    else:
        if writability.get("is_writable") is not True:
            issues.append(OutlineIssue("writability.is_writable", "必须明确为 true"))
        estimated = writability.get("estimated_length")
        if not isinstance(estimated, int) or isinstance(estimated, bool) or estimated <= 0:
            issues.append(OutlineIssue("writability.estimated_length", "必须是正整数"))
        risks = writability.get("risks")
        if not isinstance(risks, list):
            issues.append(OutlineIssue("writability.risks", "必须是数组"))
    return tuple(issues)


def ensure_outline_valid(outline: dict[str, Any], run_config: dict[str, Any]) -> None:
    issues = validate_outline(outline, run_config)
    if issues:
        details = "; ".join(f"{item.path}: {item.message}" for item in issues)
        raise OutlineValidationError(details)


def ensure_comedy_rotation(outlines: list[dict[str, Any]], start: int, end: int) -> None:
    ordered = sorted(
        (item for item in outlines if isinstance(item.get("number"), int) and start <= item["number"] <= end),
        key=lambda item: item["number"],
    )
    previous: str | None = None
    streak = 0
    for outline in ordered:
        mechanism = outline.get("comedy_mechanism")
        if not isinstance(mechanism, str) or not mechanism.strip():
            raise OutlineValidationError(
                f"第 {outline.get('number')} 章缺少 comedy_mechanism"
            )
        if mechanism == previous:
            streak += 1
        else:
            previous = mechanism
            streak = 1
        if streak >= 3:
            raise OutlineValidationError(
                f"主要喜剧机制“{mechanism}”连续使用 {streak} 章"
            )


def ensure_unit_contracts(
    unit: dict[str, Any], outlines: list[dict[str, Any]]
) -> None:
    chapter_range = unit.get("chapter_range")
    if (
        not isinstance(chapter_range, list)
        or len(chapter_range) != 2
        or not all(isinstance(item, int) for item in chapter_range)
    ):
        raise OutlineValidationError("故事单元 chapter_range 无效")
    start, end = chapter_range
    by_number = {
        item.get("number"): item
        for item in outlines
        if isinstance(item.get("number"), int) and start <= item["number"] <= end
    }
    if len(by_number) != end - start + 1:
        return
    setback = unit.get("required_setback")
    if isinstance(setback, str) and setback.strip():
        carried = any(
            setback in outline.get("required_outcomes", [])
            or outline.get("cost_or_aftereffect") == setback
            for outline in by_number.values()
        )
        if not carried:
            raise OutlineValidationError(
                f"完整章纲没有章节承担故事单元真实受挫：{setback}"
            )
    payoff = unit.get("required_payoff")
    final_outline = by_number[end]
    if isinstance(payoff, str) and payoff.strip():
        if payoff not in final_outline.get("required_outcomes", []):
            raise OutlineValidationError(
                f"末章 required_outcomes 缺少故事单元阶段兑现：{payoff}"
            )
    closing_state = unit.get("closing_state")
    if isinstance(closing_state, list) and closing_state:
        final_closing = final_outline.get("closing_state")
        if not isinstance(final_closing, list):
            raise OutlineValidationError("末章 closing_state 无效")
        missing = [item for item in closing_state if item not in final_closing]
        if missing:
            raise OutlineValidationError(
                f"末章 closing_state 未覆盖故事单元退出状态：{missing}"
            )
