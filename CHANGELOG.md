# Cross-Agent Changelog

> 对方做了重要变更时在这里记录。先读这里，再翻文件。
> 格式：`[来源] 日期 | 变更内容`

## [CC] 2026-06-03
- **飞书配置对齐**：Hermes已将管线重构为4阶段（主动出击→面试进行中→Offer对比→已归档），同步更新CC端
  - `feishu_api.py` TABLE_PIPELINE → `tblJpSB54ABcljfq`（主动出击）
  - `feishu_config.md` 更新为实际6表结构+字段定义
  - `startup_check.py` 修复表ID、字段名、编码问题，可正常运行
  - `CLAUDE.md` 启动路径修正 `python ~/Desktop/Improve/startup_check.py`
- **龙虾(OpenClaw)确认运行中**：VPS 47.103.94.65:8000 健康，主动出击表21条记录，11条"值得投"待CC处理
- Hermes 3项联调反馈：1)备注写链接 ✅ 2)分析结果写回 ✅ 3)微信发文件→走飞书Drive
- **协议升级v3**：飞书群「跳槽管线-龙虾通知」取代GitHub messages作为三方实时通信渠道
  - `hermes_to_cc_protocol.md` → v3（新增群聊规范、三方角色表、消息前缀）
  - `CC接入指引.md` → 重写（飞书群+cc_msg.py，GitHub messages废弃）
  - `CLAUDE.md` → 新增群聊工具引用
  - CC已在群里发首条消息，Hermes待确认

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

## [CC] 2026-05-28
- **飞书总线架构上线**：飞书多维表格取代GitHub作为任务通信总线
  - 飞书Base `FEAZbWbPoaJGnPs7DZAcsuWvndb` — 跳槽管线表 + 碎片收集区
  - 应用凭据：`cli_a94d03c59bb85bb3`（olina自建，权限bitable:app+im:message）
  - 新协议 `hermes_to_cc_protocol.md` v2 — MECE分工+状态机+启动流程
  - `hermes_new_role.md` — Hermes的24/7秘书职责说明（待发送）
  - `feishu_config.md` — 表ID/字段ID+App凭据技术配置
  - `feishu_api.py` — CC端Python API封装，直调飞书REST API
  - `sync.py` PUSH_FILES 扩展至11个文件，支持新文件创建
  - CC启动流程更新：自动查飞书→整合JD→批量写简历→输出桌面+映射表
- 设计决策：不做龙虾（编排层）——飞书表格本身就是编排层，时序天然分离无并行冲突

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
