# 修仙搞笑长篇网文生成器

第一版面向本地单作者：用工作流完成项目设定与 10～20 章故事单元章纲，再由 CLI 顺序调用模型，逐章执行长度、质量、状态来源和账本压缩闸门。

## 安装

```powershell
python -m pip install -e .
```

也可以不安装，直接使用：

```powershell
python -m tools.novel_runner --help
```

## 最短可执行流程

### 1. 初始化一本小说

```powershell
novel init my-novel
```

填写：

- `runs/my-novel/config/project.md`
- `runs/my-novel/config/progression.json`
- `runs/my-novel/config/comedy-bible.json`
- `runs/my-novel/config/initial-state.json`

`initial-state.json` 使用稳定 ID 记录开篇时的角色境界、资源余额和知识状态。后续突破、消耗和误会变化都以它为机械计算起点；不要只把初始资源写在散文设定中。

### 2. 用工作流完成章纲

依次使用：

```text
workflow/00-global.md
workflow/01-expand.md
workflow/02-merge.md（按需）
workflow/03-chapters.md
```

可以让执行器先生成故事单元：

```powershell
novel plan-unit --run my-novel --chapters 10 --openai
```

也可以把人工确认后的故事单元和章节细纲整理为一个机器计划 JSON。外层格式：

```json
{
  "schema_version": "1.0",
  "story_units": [],
  "chapter_outlines": []
}
```

字段定义见 `plan.md` 第 8 节。`chapter_outlines` 可以为空，也可以一次提供完整 10～20 章；不接受只覆盖半个标准批次的残缺导入。

### 3. 校验并导入计划

```powershell
novel import-plan --run my-novel --file path/to/import-plan.json
novel validate-config --run my-novel
```

导入会整体校验 10～20 章范围、章节归属、场景预算、可写性和喜剧机制轮换。任何一章失败都不会覆盖正式计划。只导入故事单元时，后续由执行器逐批规划章纲。

### 4. 设置网关、模型路由与预算

复制本地环境模板：

```powershell
Copy-Item .env.example .env
```

在 `.env` 中填写网关和模型路由。`.env` 已被 Git 忽略，不会提交到仓库：

```dotenv
MESHYCODE_BASE_URL=https://your-openai-compatible-gateway.example/v1
MESHYCODE_API_KEY=
NOVEL_MODEL_PLANNER=gpt-5.5
NOVEL_MODEL_DRAFTER=gpt-5.5
NOVEL_MODEL_REWRITER=gpt-5.6-sol
NOVEL_MODEL_REVIEWER=gpt-5.5
NOVEL_MODEL_STATE=gpt-5.5
```

进程环境变量优先于 `.env`。不要把真实密钥写入 `run.json`、Prompt、日志或提交文件。

`runs/my-novel/run.json` 只保存环境变量名称和运行策略：

- `provider.routes`：规划、初稿、重写、评审和状态任务的模型环境变量及回退链。
- `provider.base_url_env` / `api_key_env`：网关 URL 与密钥的环境变量名。
- `provider.max_output_tokens`：应为完整单章和格式输出留足空间。
- `provider.pricing.input_per_million` / `output_per_million`：可选的当前模型单价，用于本地估算费用；两项必须同时填写，不在代码中硬编码价格。
- `policies.budget.max_calls`：最大调用次数。
- `policies.budget.max_tokens`：最大累计 Token；提供方返回用量时生效。
- `policies.budget.max_cost`：最大累计费用；提供方返回费用时生效。

无返工时，一章通常需要正文、质量评审、状态提取3次调用；实际长文通常还会增加一次跨模型压缩。默认每3～4章生成账本，章纲逻辑批次也是3～4章，但API传输默认每次最多2章，遇到网关524会自动拆成单章重试。10章动态链路应为修订和传输失败预留调用空间。

### 5. 启动整个故事单元

```powershell
novel run-unit --run my-novel --unit unit-0001 --openai
```

面向用户是一次启动 10～20 章；内部仍按单章执行：

```text
正文 → 机械字数 → 独立质量评审 → 状态来源校验 → 原子提交
```

默认每3～4章生成一次压缩账本。任一章失败或预算耗尽都会暂停，不会正式推进后续章节。

如果当前批次章纲不存在，内部顺序为：

```text
规划 3～4 章逻辑细纲批次（内部按1～2章请求）
→ 逐章生成与提交
→ 生成批次账本
→ 用新账本规划下一批
```

也可以单独规划一个标准批次：

```powershell
novel plan-batch --run my-novel --unit unit-0001 --range 1-4 --openai
```

### 6. 查看、恢复和评审

```powershell
novel status --run my-novel --json
novel resume --run my-novel --json
novel review --run my-novel --unit unit-0001 --json
```

故事单元报告位于 `runs/my-novel/reports/`。

## 修订已提交章节

不要直接覆盖 `draft.final.md`。先执行：

```powershell
novel invalidate-from --run my-novel --chapter 12 --reason "重写关键选择"
```

系统会：

- 归档第 12 章及其后续快照、账本、报告和活跃正文别名。
- 保留所有版本化历史草稿。
- 把正式提交指针回退到第 11 章。
- 把受影响章纲标为 `revalidation_status=pending`。

修改或复核章纲后逐章接受：

```powershell
novel validate-outline --run my-novel --chapter 12 --accept-revision
```

存在任何待重验章纲时，`run-unit` 会阻断。修订过程意外中断时使用 `novel resume`。

模型任务以任务类型、元数据和 Prompt 哈希生成幂等键。只有已经通过调用方格式与内容校验的 `accepted` 产物才可复用；传输成功但长度、JSON 或连续性失败的结果不会进入缓存。

## 离线验证

```powershell
$env:PYTHONUTF8 = "1"
python -m unittest discover -s tests -v
python -m compileall -q tools tests
git diff --check
```

专项覆盖映射：

```powershell
novel coverage --root .

# 校验正文哈希，并从初始状态与正式事件原子重建全部快照
novel rebuild-state --run my-novel --root .

# 将完成且评审通过的故事单元归档为固定测试产物
novel archive-run --run my-novel --unit unit-0001 --case T12-real-run --root .
```

当前离线测试只证明执行器、长度和状态链路稳定，不等价于真实模型生成的小说内容质量已经通过。
