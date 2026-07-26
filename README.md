# 小说工作流

这是一个本地运行的长篇网文生产工具。当前工作流面向番茄小说男频：先把项目设定和完整故事计划固定下来，再按“细纲 → 正文 → 审核 → 状态 → 提交”的顺序逐章生成。

## 目录边界

```text
workflow/                  流程顺序、Prompt、规则与输入/输出契约
  编排/                    主流程和任务表
  提示词/                  六类模型任务的角色指令
  规则/                    可复用的创作、审核和状态规则
  契约/                    模型任务的输入/输出说明
tools/novel_runner/        CLI、模型调用、重试、校验、事务和文件读写
runs/<运行名>/             一部小说的设定、细纲、正文、状态、账本和修订记录
tests/                     自动化流程、工具、迁移和回归测试
  证据/矩阵运行/           已脱敏的真实/回归运行归档
```

不要把小说人物、宗门、境界、剧情或密钥写进 `workflow/` 和 `tools/`。它们属于某一次运行，只能放在 `runs/<运行名>/`。`.env` 和活动 `runs/` 已被 Git 忽略。

## 工作流顺序

```text
填写项目设定
  → 校验并人工批准全书总纲
  → 规划故事单元（10～20 章）
  → 每批规划 3～4 章细纲
  → 生成一章正文
  → 审核正文
  → 提取已发生的状态
  → 正文和状态原子提交
  → 生成账本
  → 单元评审、状态重建
  → 全书完成后人工归档
```

上一章未提交时，工具不会生成下一章。长度、细纲契约、质量或状态连续性失败都会停在当前章；只有可恢复的模型传输错误会在预算内自动重试。

`workflow/编排/流程.json` 定义完整步骤和失败去向，`任务表.json` 定义模型任务、规则包和契约。运行时会记录实际装配的 Prompt、规则和契约哈希，便于复现某次生成所用的工作流版本；不存在旧流程回退。

## 首次运行

```powershell
python -m pip install -e .
Copy-Item .env.example .env
novel init --run my-novel
```

在 `.env` 中填写网关、密钥和各角色模型。然后编辑 `runs/my-novel/config/`：

- `project.md`：题材、目标平台、主角、开篇承诺和长期目标；番茄项目应写明“目标平台：番茄小说”。
- `project-profile.json`：结构化规则档案；当前项目填写 `{"platform":"fanqie","channel":"male","genre":"xianxia","style":"comedy"}`。
- `progression.json`：修仙题材启用时装配的境界、资源、能力、伤势与突破边界。
- `comedy-bible.json`：喜剧风格启用时装配的角色反差、可用/禁用笑点和严肃场景限制。
- `initial-state.json`：第 0 章可继承状态。
- `master-plan.json`：全书分卷、粗故事单元、双主角成长线和终局。

校验并人工批准总纲：

```powershell
novel validate-config --run my-novel
novel validate-master-plan --run my-novel
novel approve-master-plan --run my-novel
```

批准后，执行一个已规划故事单元：

```powershell
novel run-unit --run my-novel --unit unit-0001 --openai
```

也可逐步执行：

```powershell
novel plan-unit --run my-novel --openai
novel plan-batch --run my-novel --unit unit-0001 --range 1-4 --openai
novel draft --run my-novel --chapter 1 --openai
novel review-draft --run my-novel --chapter 1 --openai
novel extract-state --run my-novel --chapter 1 --openai
novel commit --run my-novel --chapter 1
```

## 日常操作

```powershell
novel status --run my-novel --json
novel resume --run my-novel --json
novel rebuild-state --run my-novel --json
novel review --run my-novel --unit unit-0001 --json
novel invalidate-from --run my-novel --chapter 12 --reason "重写关键选择"
novel migrate-storage --run my-novel             # 默认只审计
novel migrate-storage --run my-novel --apply     # 备份后原子迁移到 v2
novel archive-run --run my-novel --unit unit-0001 --case T01
```

归档只接受通过评审且脱敏检查通过的运行，输出到 `tests/证据/矩阵运行/`。它不是活动小说目录，也不会成为下一章的上下文。

## 验证

```powershell
python -m unittest discover -s tests -t .
python -m compileall -q tools tests
git diff --check
```

正文风格、开篇冲突和番茄男频要求维护在 `workflow/规则/`；执行器不内置某个项目的人名或剧情。具体可编辑文件及其组合方式见 [workflow/README.md](workflow/README.md)。
