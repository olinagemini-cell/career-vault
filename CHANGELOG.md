# Cross-Agent Changelog

> 对方做了重要变更时在这里记录。先读这里，再翻文件。
> 格式：`[来源] 日期 | 变更内容`

## [CC] 2026-05-23
- 确认协作协议 `hermes_to_cc_protocol.md`，CC端落地完成
- sync.py 改为全量同步（Git Tree API），不再硬编码3个文件
- CLAUDE.md 更新启动流程和文件分工说明

## [Hermes] 2026-05-23
- **简历库重构**：删除`resumes/`文件夹（13个散装文件），全部合并至`简历库/`
  - 通用版 → `简历库/通用版/`
  - 定向简历→ `简历库/_Archive/2026-05/<公司名>/`（各含message）
- L'Oréal Data PM 定向简历完成（已投出）
- DXC Delivery Manager 定向简历完成（周一投）
- GM BI Manager 定向简历完成
- 埃森哲任务关闭，创建 2026-05-23 每日清单
