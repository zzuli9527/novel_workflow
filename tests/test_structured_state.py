from __future__ import annotations

import unittest

from tools.novel_runner.structured_state import (
    StructuredStateError,
    default_initial_state,
    project_structured_state,
    validate_structured_event,
)


def empty_event() -> dict[str, object]:
    return {
        "cultivation_changes": [],
        "resource_changes": [],
        "knowledge_changes": [],
    }


class StructuredStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.initial = default_initial_state()
        self.initial["cultivation"] = [
            {
                "subject_id": "protagonist",
                "stage": "炼气一层",
                "abilities": [],
                "injuries": [],
                "limits": ["经脉承载有限"],
            }
        ]
        self.initial["resources"] = [
            {
                "owner_id": "protagonist",
                "resource_id": "spirit_stone_low",
                "amount": 3,
                "unit": "枚",
            }
        ]
        self.initial["knowledge"] = []

    def test_breakthrough_requires_costs_and_updates_stage(self) -> None:
        event = empty_event()
        event["cultivation_changes"] = [
            {
                "subject_id": "protagonist",
                "kind": "breakthrough",
                "from_stage": "炼气一层",
                "to_stage": "炼气二层",
                "prerequisites": ["周天稳定"],
                "costs": ["消耗两枚灵石"],
                "new_limits": ["三日内不能再次冲关"],
                "change": "主角完成突破",
                "source_evidence": "主角完成突破",
            }
        ]

        projected = project_structured_state(event, None, self.initial)
        protagonist = projected["cultivation"][0]
        self.assertEqual(protagonist["stage"], "炼气二层")
        self.assertIn("三日内不能再次冲关", protagonist["limits"])

    def test_breakthrough_without_cost_is_rejected(self) -> None:
        event = empty_event()
        event["cultivation_changes"] = [
            {
                "subject_id": "protagonist",
                "kind": "breakthrough",
                "from_stage": "炼气一层",
                "to_stage": "炼气二层",
                "prerequisites": ["周天稳定"],
                "costs": [],
                "new_limits": ["短期虚弱"],
                "change": "主角完成突破",
                "source_evidence": "主角完成突破",
            }
        ]
        with self.assertRaisesRegex(StructuredStateError, "costs"):
            validate_structured_event(event)

    def test_breakthrough_limit_with_state_id_can_be_updated_without_duplicate(self) -> None:
        event = empty_event()
        event["state_schema_version"] = "1.1"
        event["cultivation_changes"] = [
            {
                "subject_id": "protagonist",
                "kind": "breakthrough",
                "from_stage": "炼气一层",
                "to_stage": "炼气二层",
                "prerequisites": ["周天稳定"],
                "costs": ["消耗两枚灵石"],
                "new_limits": [
                    {
                        "state_id": "post-breakthrough-rest",
                        "description": "三日内不能再次冲关",
                    }
                ],
                "change": "主角完成突破",
                "source_evidence": "主角完成突破",
            }
        ]
        after_breakthrough = project_structured_state(event, None, self.initial)
        update = empty_event()
        update["state_schema_version"] = "1.1"
        update["cultivation_changes"] = [
            {
                "subject_id": "protagonist",
                "kind": "restriction",
                "state_id": "post-breakthrough-rest",
                "state_action": "set",
                "stage_after": "炼气二层",
                "change": "剩余两日不能再次冲关",
                "source_evidence": "剩余两日不能再次冲关",
            }
        ]

        projected = project_structured_state(update, after_breakthrough)
        protagonist = projected["cultivation"][0]

        self.assertNotIn("三日内不能再次冲关", protagonist["limits"])
        self.assertEqual(
            protagonist["limits"].count("剩余两日不能再次冲关"), 1
        )

    def test_stage_cannot_change_without_breakthrough(self) -> None:
        event = empty_event()
        event["cultivation_changes"] = [
            {
                "subject_id": "protagonist",
                "kind": "progress",
                "stage_after": "炼气二层",
                "change": "修炼进度增加",
                "source_evidence": "修炼进度增加",
            }
        ]
        with self.assertRaisesRegex(StructuredStateError, "不是 breakthrough"):
            project_structured_state(event, None, self.initial)

    def test_resource_balance_is_mechanically_projected(self) -> None:
        event = empty_event()
        event["resource_changes"] = [
            {
                "owner_id": "protagonist",
                "resource_id": "spirit_stone_low",
                "operation": "consume",
                "amount": 2,
                "unit": "枚",
                "resulting_balance": 1,
                "source_or_destination": "修炼消耗",
                "change": "主角消耗两枚灵石",
                "source_evidence": "主角消耗两枚灵石",
            }
        ]

        projected = project_structured_state(event, None, self.initial)
        self.assertEqual(projected["resources"][0]["amount"], 1.0)

    def test_multiple_resource_transactions_are_applied_in_order(self) -> None:
        event = empty_event()
        event["resource_changes"] = [
            {
                "owner_id": "protagonist",
                "resource_id": "spirit_stone_low",
                "operation": "gain",
                "amount": 2,
                "unit": "枚",
                "resulting_balance": 5,
                "source_or_destination": "任务奖励",
                "change": "主角获得两枚灵石",
                "source_evidence": "主角获得两枚灵石",
            },
            {
                "owner_id": "protagonist",
                "resource_id": "spirit_stone_low",
                "operation": "consume",
                "amount": 1,
                "unit": "枚",
                "resulting_balance": 4,
                "source_or_destination": "修炼消耗",
                "change": "主角随后消耗一枚灵石",
                "source_evidence": "主角随后消耗一枚灵石",
            },
        ]
        projected = project_structured_state(event, None, self.initial)
        self.assertEqual(projected["resources"][0]["amount"], 4.0)

    def test_resource_cannot_be_spent_below_zero(self) -> None:
        event = empty_event()
        event["resource_changes"] = [
            {
                "owner_id": "protagonist",
                "resource_id": "spirit_stone_low",
                "operation": "consume",
                "amount": 4,
                "unit": "枚",
                "resulting_balance": 0,
                "source_or_destination": "修炼消耗",
                "change": "主角消耗四枚灵石",
                "source_evidence": "主角消耗四枚灵石",
            }
        ]
        with self.assertRaisesRegex(StructuredStateError, "余额不能为负"):
            project_structured_state(event, None, self.initial)

    def test_declared_resource_balance_must_match_mechanical_result(self) -> None:
        event = empty_event()
        event["resource_changes"] = [
            {
                "owner_id": "protagonist",
                "resource_id": "spirit_stone_low",
                "operation": "consume",
                "amount": 1,
                "unit": "枚",
                "resulting_balance": 1,
                "source_or_destination": "修炼消耗",
                "change": "主角消耗一枚灵石",
                "source_evidence": "主角消耗一枚灵石",
            }
        ]
        with self.assertRaisesRegex(StructuredStateError, "余额不连续"):
            project_structured_state(event, None, self.initial)

    def test_same_character_fact_cannot_have_two_states_in_one_event(self) -> None:
        event = empty_event()
        event["knowledge_changes"] = [
            {
                "character_id": "companion",
                "fact_id": "protagonist_injury",
                "state": "suspects",
                "belief": "主角可能受伤",
                "change": "同伴开始怀疑",
                "source_evidence": "同伴开始怀疑",
            },
            {
                "character_id": "companion",
                "fact_id": "protagonist_injury",
                "state": "knows",
                "belief": "主角已经受伤",
                "change": "同伴确认伤势",
                "source_evidence": "同伴确认伤势",
            },
        ]
        with self.assertRaisesRegex(StructuredStateError, "冲突知识状态"):
            validate_structured_event(event)

    def test_knowledge_state_is_projected_per_character_across_chapters(self) -> None:
        first = empty_event()
        first["knowledge_changes"] = [
            {
                "character_id": "companion",
                "fact_id": "protagonist_injury",
                "state": "suspects",
                "belief": "主角可能受伤",
                "change": "同伴开始怀疑",
                "source_evidence": "同伴开始怀疑",
            }
        ]
        after_first = project_structured_state(first, None, self.initial)
        second = empty_event()
        second["knowledge_changes"] = [
            {
                "character_id": "companion",
                "fact_id": "protagonist_injury",
                "state": "knows",
                "belief": "主角已经受伤",
                "change": "同伴确认伤势",
                "source_evidence": "同伴确认伤势",
            }
        ]

        after_second = project_structured_state(second, after_first)
        self.assertEqual(after_second["knowledge"][0]["state"], "knows")
        self.assertEqual(after_second["knowledge"][0]["character_id"], "companion")

    def test_version_11_updates_and_resolves_one_tracked_injury(self) -> None:
        injured = empty_event()
        injured["state_schema_version"] = "1.1"
        injured["cultivation_changes"] = [
            {
                "subject_id": "protagonist",
                "kind": "injury",
                "state_id": "hearing-damage",
                "state_action": "set",
                "stage_after": "炼气一层",
                "change": "耳鸣加重并短暂失聪",
                "source_evidence": "耳鸣加重并短暂失聪",
            }
        ]
        after_injury = project_structured_state(injured, None, self.initial)
        self.assertEqual(
            after_injury["cultivation"][0]["injuries"],
            ["耳鸣加重并短暂失聪"],
        )

        improving = empty_event()
        improving["state_schema_version"] = "1.1"
        improving["cultivation_changes"] = [
            {
                "subject_id": "protagonist",
                "kind": "recovery",
                "state_id": "hearing-damage",
                "state_action": "set",
                "stage_after": "炼气一层",
                "change": "耳鸣降低但远处声音仍听不清",
                "source_evidence": "耳鸣降低但远处声音仍听不清",
            }
        ]
        after_improvement = project_structured_state(improving, after_injury)
        self.assertEqual(
            after_improvement["cultivation"][0]["injuries"],
            ["耳鸣降低但远处声音仍听不清"],
        )

        recovered = empty_event()
        recovered["state_schema_version"] = "1.1"
        recovered["cultivation_changes"] = [
            {
                "subject_id": "protagonist",
                "kind": "recovery",
                "state_id": "hearing-damage",
                "state_action": "resolve",
                "stage_after": "炼气一层",
                "change": "听力完全恢复",
                "source_evidence": "听力完全恢复",
            }
        ]
        after_recovery = project_structured_state(recovered, after_improvement)
        self.assertEqual(after_recovery["cultivation"][0]["injuries"], [])
        self.assertEqual(after_recovery["cultivation"][0]["tracked_states"], [])

    def test_version_11_recovery_requires_existing_injury_id(self) -> None:
        event = empty_event()
        event["state_schema_version"] = "1.1"
        event["cultivation_changes"] = [
            {
                "subject_id": "protagonist",
                "kind": "recovery",
                "state_id": "unknown-injury",
                "state_action": "resolve",
                "stage_after": "炼气一层",
                "change": "伤势恢复",
                "source_evidence": "伤势恢复",
            }
        ]
        with self.assertRaisesRegex(StructuredStateError, "活动伤势不存在"):
            project_structured_state(event, None, self.initial)

    def test_version_11_knowledge_can_supersede_obsolete_fact(self) -> None:
        initial = default_initial_state()
        initial["knowledge"] = [
            {
                "character_id": "companion",
                "fact_id": "old-suspicion",
                "state": "suspects",
                "belief": "主角可能偷了灵石",
            }
        ]
        event = empty_event()
        event["state_schema_version"] = "1.1"
        event["knowledge_changes"] = [
            {
                "character_id": "companion",
                "fact_id": "theft-ruling",
                "state": "knows",
                "belief": "主角没有偷灵石",
                "supersedes_fact_ids": ["old-suspicion"],
                "change": "同伴确认最终裁定",
                "source_evidence": "同伴确认最终裁定",
            }
        ]

        projected = project_structured_state(event, None, initial)

        self.assertEqual(len(projected["knowledge"]), 1)
        self.assertEqual(projected["knowledge"][0]["fact_id"], "theft-ruling")

    def test_version_11_ignores_redundant_self_supersede(self) -> None:
        initial = default_initial_state()
        initial["knowledge"] = [
            {
                "character_id": "companion",
                "fact_id": "current-belief",
                "state": "suspects",
                "belief": "仍在怀疑",
            }
        ]
        event = empty_event()
        event["state_schema_version"] = "1.1"
        event["knowledge_changes"] = [
            {
                "character_id": "companion",
                "fact_id": "current-belief",
                "state": "knows",
                "belief": "已经确认",
                "supersedes_fact_ids": ["current-belief"],
                "change": "同伴确认事实",
                "source_evidence": "同伴确认事实",
            }
        ]

        projected = project_structured_state(event, None, initial)

        self.assertEqual(len(projected["knowledge"]), 1)
        self.assertEqual(projected["knowledge"][0]["state"], "knows")


if __name__ == "__main__":
    unittest.main()
