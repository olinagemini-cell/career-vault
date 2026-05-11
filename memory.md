# 共享记忆

> 追加写入，勿覆盖。格式：`## [来源] YYYY-MM-DD` + 内容。

## [CC] 2026-05-11

### career-vault 仓库创建
- 仓库地址：`github.com/olinagemini-cell/career-vault`
- 用途：Hermes 与 CC 的共享记忆库
- 结构：`profile.md`（用户画像）+ `memory.md`（本文件）
- 写入规则：git clone → 编辑追加 → git commit → git push
- 读取规则：每次启动时 git pull

### Agent 架构确认
- Hermes 跑在 Ubuntu 服务器，微信作为手机交互入口，底层 hermes_cli + DeepSeek
- CC 跑在本地终端（Windows）
- 双 agent 分工：Hermes = 轻量/紧急/碎片，CC = 深度/批量/产出
- 共享记忆方案：GitHub career-vault 仓库，双向读写
