# X01～X15 自动化覆盖报告

状态含义：`automated_flow_pass` 证明执行器闸门和链路；`partial` 只证明部分规则；`real_model_required` 必须用真实正文补证。

| 编号 | 状态 | 自动化证据 | 尚缺验证 |
| --- | --- | --- | --- |
| X01 | partial | `tests/test_outline_validation.py::test_rejects_missing_dual_engine_fields` | 需要真实首章正文验证修仙问题与喜剧气质是否同时成立。 |
| X02 | automated_flow_pass | `tests/test_long_workload.py::test_twelve_chapters_keep_real_length_and_state_chain` | 真实模型仍需验证不靠重复和摘要凑足长度。 |
| X03 | partial | `tests/test_chapter_service.py::test_quality_review_blocks_cultivation_inconsistency`<br>`tests/test_chapter_service.py::test_state_change_requires_exact_draft_evidence` | 需要带具体境界、伤势和能力限制的多章正文样例。 |
| X04 | automated_flow_pass | `tests/test_structured_state.py::test_breakthrough_without_cost_is_rejected` | 结构化事件已强制前置、成本和新限制；真实突破场景仍需正文验证。 |
| X05 | automated_flow_pass | `tests/test_structured_state.py::test_resource_balance_is_mechanically_projected`<br>`tests/test_chapter_service.py::test_continuity_failure_does_not_append_state_event` | 余额、来源去向和正文证据已机械核验；真实资源叙事仍需正文验证。 |
| X06 | automated_flow_pass | `tests/test_outline_validation.py::test_rejects_three_identical_comedy_mechanisms`<br>`tests/test_plan_import.py::test_rejects_three_identical_comedy_mechanisms` | 真实笑点是否有效仍需正文评审。 |
| X07 | automated_flow_pass | `tests/test_structured_state.py::test_knowledge_state_is_projected_per_character_across_chapters` | 已按角色和事实投影知识状态；复杂误会的文学合理性仍需正文验证。 |
| X08 | partial | `tests/test_chapter_service.py::test_quality_review_allows_soft_quality_warnings` | 已有独立软质量告警，角色声音是否真正鲜明仍需真实正文验证。 |
| X09 | automated_flow_pass | `tests/test_plan_import.py::test_rejects_complete_unit_without_setback_mapping` | 章纲必须明确承载真实受挫；失败后果与追读动力仍需真实正文验证。 |
| X10 | partial | `tests/test_chapter_service.py::test_quality_review_blocks_comedy_that_erases_consequence` | 需要严肃损失场景的独立正文样例。 |
| X11 | partial | `tests/test_chapter_service.py::test_quality_review_blocks_disconnected_multi_line_plot` | 已有多线因果闸门，仍需真实多线交汇正文样例。 |
| X12 | automated_flow_pass | `tests/test_ledger.py::test_builds_json_and_markdown_ledger`<br>`tests/test_ledger.py::test_fills_structured_active_state_when_model_omits_it`<br>`tests/test_long_workload.py::test_twelve_chapters_keep_real_length_and_state_chain`<br>`tests/test_unit_runner.py::test_run_unit_plans_each_missing_batch_after_previous_ledger` | 离线已证明下一批章纲和正文 Prompt 使用首批账本；真实模型需验证信息充分性。 |
| X13 | automated_flow_pass | `tests/test_plan_import.py::test_rejects_complete_unit_without_final_payoff_mapping`<br>`tests/test_unit_runner.py::test_runs_ten_chapter_unit_to_completion` | 末章兑现和退出状态已绑定章纲，文学兑现仍需真实正文。 |
| X14 | automated_flow_pass | `tests/test_long_workload.py::test_twelve_chapters_keep_real_length_and_state_chain` | 已完成 12 章、约 2.4 万以上正文字符的离线长链路负载测试。 |
| X15 | automated_flow_pass | `tests/test_unit_runner.py::test_failure_pauses_unit_and_does_not_advance_later_chapters`<br>`tests/test_chapter_service.py::test_resume_completes_prepared_commit_journal`<br>`tests/test_revision.py::test_revision_journal_can_resume_after_interruption` | 真实网络中断仍需在获批调用后验证。 |

证据引用完整：是
