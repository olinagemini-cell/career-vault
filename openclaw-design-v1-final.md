# OpenClaw v1 — 技术方案（Hermes审阅版）

> 写给Hermes看的设计文档，经审阅后定稿。
> CC请按此版本实现。

---

## 1. 定位

OpenClaw = 云端求职流水线引擎。负责JD分析→匹配打分→简历生成→飞书同步→通知推送。
Hermes = 微信入口 + 消息路由。负责接收微信消息，判断是否为JD，是则转发给OpenClaw处理。

**协作关系，不替代Hermes。**

---

## 2. 整体架构

```
微信消息
   │
   ▼
Hermes (云上，24/7)
   │
   ├── 不是JD ──→ Hermes照常处理（闲聊、查状态、手动指令等）
   │
   └── 是JD ──→ POST /api/jd → OpenClaw云服务
                                   │
                                   ├── 1. 分析JD（Claude API）
                                   ├── 2. 匹配打分（按简历规则）
                                   ├── 3. 判断是否值得投
                                   ├── 4. 生成定向简历.docx（如果值得投）
                                   ├── 5. 更新飞书Base状态
                                   └── 6. 写飞书Base状态字段供Hermes轮询
                                         │
                                         ▼
                                    Hermes轮询发现 → 微信通知用户
```

---

## 3. Hermes 需要做的事

### 3.1 新增能力：JD检测

收到微信消息后，判断是否为JD。规则：

- **关键词匹配**：`JD`、`岗位职责`、`任职要求`、`职位描述`、`招聘`、`薪资范围`、`本科及以上`
- **URL检测**：消息开头是URL或含招聘平台域名（zhipin / linkedin / 猎聘 / liepin / 51job）→ 判定为JD
- **长度阈值**：消息超过200字且含2个以上关键词 → 判定为JD
- **显式指令**：以 `/jd` 或 `投这个` 开头 → 强制当JD处理

### 3.2 新增能力：调用OpenClaw API

判定为JD后，先做消息清洗（去微信表情符号、去引用块、去多余空行），再POST到OpenClaw：

```
POST /api/jd
Content-Type: application/json
Authorization: Bearer <各自持有的secret>

{
  "raw_text": "<清洗后的JD原文>",
  "source": "wechat",
  "received_at": "2026-06-02T22:00:00+08:00"
}
```

### 3.3 接收OpenClaw结果 — 不走Webhook

**Hermes没有对外暴露的Webhook端点，不能被动接收请求。**

改为：**OpenClaw处理完直接将结果写入飞书Base「主动出击」表的指定状态字段**，Hermes下次与用户交互时主动读飞书Base获取结果。

### 3.4 保持不变的部分

- Hermes现有功能完全不动
- career-vault操作仍由CC负责（OpenClaw只生成简历文件，push由CC在SessionStart时处理）
- Hermes仍负责「每日日志」表的写入（决策记录、用户交互等）

---

## 4. OpenClaw 云服务设计

### 4.1 技术栈

| 层 | 选型 |
|---|---|
| Web框架 | FastAPI (Python) |
| AI调用 | Anthropic API (Claude Sonnet) |
| 文档转换 | md2docx（已有） |
| 存储 | SQLite（任务记录）+ 本地文件（简历输出） |
| 飞书集成 | 飞书开放API（复用现有飞书配置信息） |
| 部署 | Docker Compose on VPS |

### 4.2 API列表

| 端点 | 方法 | 用途 |
|---|---|---|
| `/api/jd` | POST | Hermes提交JD |
| `/api/jd/{id}` | GET | 查询处理状态 |
| `/api/health` | GET | 健康检查 |

### 4.3 处理流水线

```
JD文本接收
  │
  ▼
去重检查（飞书Base已有JD？）
  │
  ├── 已存在 → 跳过，写飞书状态=已存在，不通知
  │
  └── 新JD
       │
       ▼
    关键词提取（公司、职位、薪资、地点、要求）
       │
       ▼
    Claude分析（Phase 1: 意图分析 + 匹配打分）
       │
       ├── 分数<60 → 跳过，飞书记录"不值得投"
       │
       └── 分数≥60
            │
            ▼
         分组归类（通用版/药械定向/金融定向/其他定向）
            │
            ▼
         生成定向简历（Claude生成MD → md2docx转Word）
            │
            ▼
         文件存本地 + 生成下载链接（HTTP 24h有效）
            │
            ▼
         更新飞书Base（状态=简历已生成，填备注含下载链接）
            │
            ▼
         Hermes下次轮询发现，微信通知用户
```

### 4.4 飞书操作 — 并发约定

为避免写冲突，做以下分工：

| 操作者 | 操作的飞书表 | 说明 |
|--------|-------------|------|
| **OpenClaw** | 「主动出击」(tblJpSB54ABcljfq) | JD去重、新建记录、打分、状态更新，全权管理 |
| **Hermes** | 「每日日志」(tblmJ2wjOGa4H1q3) | 决策记录、用户交互记录、日常日志 |
| **暂不动** | 面试阶段、Offer对比、归档、数据表等 | 两者都不自动写入 |

### 4.5 简历交付

简历文件生成在OpenClaw的VPS上，两种方式交付：

1. **OpenClaw存本地 + 提供HTTP下载链接**（24h有效），写入飞书备注
2. **CC在SessionStart时**从OpenClaw拉取新简历到桌面 `~/Desktop/跳槽投递_YYYY-MM-DD/`

Hermes通过飞书状态发现新简历后，尝试直接从OpenClaw下载链接获取文件并微信发送给用户（微信≤20MB可传，docx通常<500KB，完全可行）。

---

## 5. 安全

| 项目 | 方案 |
|---|---|
| API认证 | `Authorization: Bearer <shared-secret>`，Hermes和OpenClaw各自持有 |
| 传输加密 | HTTPS（Let's Encrypt免费证书） |
| API Key | Anthropic API Key存在VPS环境变量，不硬编码 |
| 飞书Token | 复用现有飞书App凭证（app_id + app_secret） |
| shared-secret | **不共存放**。Hermes存`~/.hermes/config/`，OpenClaw存环境变量 |

---

## 6. 部署目标

- **类型**：轻量应用服务器（国内云厂商）
- **最低配置**：1C2G，20GB SSD
- **系统**：Ubuntu 22.04
- **预算**：约¥50-70/月
- **域名**：暂不需要，IP+端口即可

---

## 7. Hermes审阅结论 ✅ 批准

### 通过项
- 整体架构方案 **批准**
- Hermes=入口+路由，OpenClaw=流水线 — 同意解耦
- Hermes现有功能不动，只增三个模块（JD检测、API调用、飞书轮询）

### 有条件通过项

| # | 问题 | 结论 | 说明 |
|---|------|------|------|
| 1 | JD检测规则 | ✅ 接受 | 补充了URL检测规则 |
| 2 | 回调机制 | ⚠️ 改方案 | Hermes无webhook，改为OpenClaw写飞书状态 → Hermes轮询 |
| 3 | 飞书并发冲突 | ✅ 约定 | OpenClaw专用「主动出击」，Hermes专用「每日日志」 |
| 4 | 简历交付 | ✅ 微信可行 | docx<500KB，微信文件发送无问题 |
| 5 | shared-secret存储 | ⚠️ 各自持有 | 不共存放 |
| 6 | 消息清洗 | ✅ 做 | Hermes转发前做基础清洗 |

---

## 8. 下一步

1. CC阅读此文档
2. 开始写OpenClaw代码（FastAPI + 飞书集成 + Claude API + md2docx）
3. 部署到VPS（Docker Compose）
4. Hermes与OpenClaw联调（JD转发→飞书轮询→微信通知）
