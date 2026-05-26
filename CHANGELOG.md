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

## [CC] 2026-05-26
- **目录结构大重组**：扁平文件按职能分入子目录
  - 工作流文档/（CLAUDE.md, cc_to_hermes_delivery.md, resume_rules.md）
  - 策略与复盘/（市场分析、投递策略、进展诊断等8个文件）
  - 投递管理/（outreach追踪、猎头渠道、消息模板 + 投递跟踪表）
  - 我的简历/（skill-modules 17个CN模块 + 猎聘项目经历 中英版）
- 简历库扩充：新增欧莱雅、勃林格、施耐德、西门子医疗、强生等方向
- 面试准备：新增 docx 版本（总览/电话脚本/案例库）
- 合并 Hermes 的 main 分支变更（resumes→简历库合并等）
- master 分支内容推送至 main，sync.py 全量同步 192 文件
