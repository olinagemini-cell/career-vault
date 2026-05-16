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


## [Hermes] 2026-05-11

### 妈妈（田园的风铃）空调方案
- 济南，已退休，普陀区圣天地小区
- 20㎡卧室 → **格力云锦三代 1.5匹挂机**（国补后≈¥2,375）
- 30多㎡客厅 → **格力云锦三代 2匹柜机**（国补后≈¥4,800）
- 两台均已下单，总价≈¥7,175
- 选择云锦三代而非天仪的原因：冷酷外机（济南夏天实用）+APP远程操控（用户可以帮妈妈提前开空调）+左右扫风
- 忌讳：聊天时不用"身体不好"之类假设性表述，会被认为不吉利
- 妈妈微信名：田园的风铃

### 普陀区政府信息公开申请
- 申请事项：圣天地小区物业招投标手续公开
- 受理机关：普陀区住房保障和房屋管理局
- 线上入口：https://xxgk.sh.gov.cn/zwgk_interface/pages/zwgkfront/publicApplyOU.html?ouguid=U2102
- 申请人已自行填写提交，等待20个工作日内答复

## [CC] 2026-05-11 (session #2)

### career-vault 部署完成
- GitHub repo 已上线，CC 端接入完毕
- 同步方式：gh API（git HTTPS 被墙），sync.py pull/push
- CLAUDE.md 已更新，CC 每次启动会自动 pull 共享记忆
- Hermes 写入正常，CC 已验证可读取

## [Hermes] 2026-05-12

### 今日关键信息：CC推到了main分支
- CC的同步用的是main分支，但Hermes本地之前看着master分支
- 解决方案：本地切换到main分支，跟CC对齐
- 以后双agent统一用main分支共享记忆

### 今日日程
- 12:00 健身
- 15:30 出庭（热水费诉讼，文档在trial/目录）
- 健身教练不续了（一年花了5-6万效果一般）

### sync脚本更新
- 本地已从main分支拉取最新 memory.md 和 profile.md
- 双向同步已恢复，以后 git pull/push 都走main

## [CC] 2026-05-12

> 诉讼相关内容已迁移至独立仓库 [lawsuit-memory](https://github.com/olinagemini-cell/lawsuit-memory)，Hermes 请从该仓库拉取诉讼上下文。
