# 测试归档

本目录用于归档本轮针对 `workflow/03-chapters.md` 与 `workflow/04-draft.md` 的迭代测试结果。

## 本轮测试目标

验证更新后的细纲与正文 Prompt，是否能明显改善以下问题：

- 节奏慢
- 首章慢启动
- 整章只铺不兑
- 专业感只靠讲解
- 章末钩子过虚
- 多目标章节容易写平

## 已测场景

1. 首章开局迭代：`ch01-v1` ~ `ch01-v4`
2. 首章后承接章：`ch02-verify`
3. 施压章：`pressure-chapter`
4. 诗词破圈章：`poem-breakout`
5. 多目标推进章：`multi-goal-chapter`
6. 轻情绪/关系推进章：`emotion-relationship`
7. 连续 3 章组测：`batch-3chapters`
8. 失败/受挫章：`failure-setback`
9. 多线正式交汇章：`multi-line-merge`
10. 朝堂/权谋试探章：`court-politics`
11. 长信息揭示章：`long-info-reveal`
12. 状态回填联动测试：`state-feedback-loop`
13. 同一卖点疲劳测试：`motif-fatigue`

## 文件说明

- `test-plan.md`：测试范围、观察指标、结果概览
- `reviews.md`：每轮测试评价与结论
- `final-evaluation.md`：本轮 Prompt 迭代的最终判断
- `test-matrix.md`：后续跨章型测试矩阵与评分标准
- `test-run-template.md`：单轮测试记录模板
- `drafts/`：测试正文产物
