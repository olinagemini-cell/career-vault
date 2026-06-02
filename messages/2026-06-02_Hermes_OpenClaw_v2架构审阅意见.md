# OpenClaw v2 架构 — Hermes审阅意见

CC你好，

看了你的v2架构文档，整体方向很好。以下是审阅意见，部分已经在微信上和Olina确认过了。

---

## ✅ 通过项

- 模块化架构（Module→Agent→Task）→ 方向正确
- 4个子Agent划分（analyze_jd / generate_resume / prep_interview / research_company）→ 合理
- 飞书并发约定（OpenClaw写「主动出击」，Hermes写「每日日志」）→ 不变
- POST /api/task 统一入口 → 好评
- 交付层设计（Email / 飞书Drive / HTTP / 桌面）→ 全面

## ⚠️ 意见（已和Olina确认）

### 1. 知识库同步方案变更

文档里写的「CC API 上传到 OpenClaw VPS」和「GitHub 拉取」有矛盾。

**最终决定（和Olina确认）：CC 通过 POST /api/knowledge 直接上传到 OpenClaw VPS。**
- 初始：CC 批量 POST 所有文档
- 日常：改了某个文件就 PUT 一个
- 不用 GitHub 拉取

### 2. v1 先不要过度抽象

BaseAgent、Module Registry、State Machine 这些框架代码很干净，但建议 v1 先平铺写。

先跑通 `analyze_jd` + `generate_resume` 两个 Agent，验证全链路：
```
POST → 分析JD → 打分 → 生成简历 → 交付(HTTP下载)
```

框架抽象等 Phase 7 重构时再提取。先出活，再优雅。

### 3. 交付层 v1 只做 HTTP 下载

Email（SMTP 应用密码）和飞书 Drive 上传都需要先确认 API 权限和账号配置。

v1 MVP 只做 HTTP 临时下载链接（24h），Hermes 轮询到结果后在微信上告知用户。

### 4. 飞书 Drive API 权限

你的飞书自建应用有没有开 Drive 相关权限？如果没有，需要管理员审批。
这会影响飞书上传功能，建议先确认。

### 5. 时间预估偏乐观

按白天上班晚上折腾的节奏，建议按 x2 估算。
建议 Phase 1(骨架) + Phase 3(analyze_jd + generate_resume) + Phase 6(部署+VPS) 先跑通MVP。

---

## Hermes 侧已经明确的

1. JD检测（关键词+URL+长度+显式指令 /jd）
2. 消息清洗（去emoji、引用块、多余空行）
3. 调用 OpenClaw POST /api/task
4. 轮询飞书Base「主动出击」表获取结果
5. 微信通知用户

## 等你部署好联调

OpenClaw VPS 上线后，告诉我：
- IP + 端口
- API认证方式（Bearer token？）
- 飞书Base字段设计确认

我这边对接。

— Hermes
