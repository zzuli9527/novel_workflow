# tools 代码结构

`tools/novel_runner/` 只负责执行工作流，不保存小说设定，也不定义正文规则。业务顺序、Prompt、规则和契约仍以项目根目录的 `workflow/` 为唯一来源。

## 目录

```text
novel_runner/
  cli.py                    稳定的命令行入口
  commands/                 参数、Provider 构建和命令处理
    handlers/               按校验、规划、章节、维护拆分的命令处理器
  workflow_runtime/         读取任务表、流程路由、契约和来源清单
  prompting/                上下文读取、数据压缩和各任务 Prompt 装配
  chapters/                 正文、审核、状态、提交和恢复
  units/                    故事单元预算、章节/批次调度和单元收尾
  shared/                   唯一的跨模块基础能力，目前仅包含 UTC 时钟

  config.py                 运行初始化与完整配置校验
  master_plan.py            全书总纲领域校验与审批
  planning_service.py       故事单元和章节批次规划服务
  ledger.py                 批次账本服务
  provider.py               模型提供方实现
  api_runtime.py            调用预算、日志和幂等复用
  storage.py                原子文件操作和运行锁
  file_storage.py           FileStorage v1/v2 路径与生命周期
  state_store.py            状态事件与快照投影
```

旧的 `chapter_service.py`、`prompt_composer.py`、`unit_runner.py` 和 `workflow_loader.py` 转发入口已经删除。代码与测试直接导入对应子包，不保留第二条入口路径。

## 依赖方向

```text
cli / commands
      ↓
units / chapters / planning_service / ledger
      ↓
prompting / workflow_runtime / 领域校验
      ↓
provider / storage / state_store
```

约束：

- 不得重新创建四个旧转发入口，应直接导入对应子包。
- `workflow_runtime/` 不依赖章节或单元执行器。
- `prompting/` 只读取并压缩上下文，不调用模型、不提交状态。
- `chapters/` 处理单章生命周期；`units/` 只负责编排，不复制单章逻辑。
- 禁止新增含混的 `utils.py`；共享能力应放进职责明确的模块。
- 完全相同的多语句函数体不得重复；UTC 时间只能由 `shared/clock.py` 提供。
- 子包中的单个实现文件原则上不超过 400 行。

这些边界由 `tests/test_tools_architecture.py` 自动检查。
