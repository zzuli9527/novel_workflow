# 当前状态

更新日期：2026-07-26

- 工作流已切换为 v4：唯一来源是 `workflow/编排/流程.json` 与 `任务表.json` 及其引用的 Prompt、规则、契约文件。
- 旧 `workflow/runtime/` 与按阶段复制规则的旧 Markdown 已删除；工具不会回退到它们。
- `tools/novel_runner/` 负责模型调用、重试、校验、状态机、事务、迁移和归档。
- 活动小说仅保存在本地 `runs/`，并已从 Git 跟踪中移除。
- 脱敏测试归档位于 `tests/证据/矩阵运行/`；自动化测试和归档证据都归入 `tests/`。
- 当前正文规则仅在结构化项目档案声明 `platform=fanqie`、`channel=male` 时注入番茄男频规则，并对前 3 章强制校验开篇承诺是否兑现。

下一步由具体小说运行决定：填写/校验/批准 `master-plan.json` 后，先运行一个完整的故事单元，再根据 `status`、`review` 和 `rebuild-state` 的结果继续或修订。
