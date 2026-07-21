# 测试目录说明

`test/` 用于验证修仙搞笑长篇工作流、后续执行器和长链路生产稳定性。

## 文件职责

- `test-matrix.md`：当前专项测试矩阵。
- `test-run-template.md`：每轮测试统一记录模板。
- `coverage-report.md`：X01～X15 与自动化测试的证据映射。
- `coverage-report.json`：同一覆盖报告的机器版本。
- `completion-audit.md` / `.json`：第一版要求逐项完成度审计。
- `matrix-runs/<case-id>/`：具体测试运行数据和产物。

## 测试原则

- 具体小说设定只放在独立测试运行目录。
- 每轮测试必须记录输入、章纲、正文、状态、评审和决定。
- 长正文测试必须使用真实正文，不使用摘要替代。
- 任一章节未通过硬闸门时，不得继续提交正式后续状态。
- 历史测试运行可以保留作为失败证据，但不自动代表当前修仙搞笑版本已经通过。

## 固定产物

```text
test/matrix-runs/<case-id>/
  input.md
  outline.md
  drafts.md
  states.md
  review.md
  decision.md
  data/
```

自动化实现后，`data/` 至少保存运行配置、逐章检查、状态事件和批次账本。

更新覆盖报告：

```text
novel coverage --root <项目根目录>
```
