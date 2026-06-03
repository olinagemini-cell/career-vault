# 飞书跳槽管线 — 技术配置

> CC、Hermes、OpenClaw(龙虾)共用。飞书Base和多维表格的ID映射。
> 最后更新: 2026-06-03 (Hermes重构为4阶段管线)

## 应用凭据（3个独立App，2026-06-03拆分）

| 角色 | App名称 | App ID | App Secret | 权限 |
|------|---------|--------|------------|------|
| CC | Improve | `cli_a94d03c59bb85bb3` | `ndgOy1DR50BStPfOlnJSsbitF6Q4es7F` | bitable:app, im:message, drive:file |
| Hermes | Hermes秘书 | `cli_aa950ddcd7b85bcd` | `4xhjJXZVtC9PpaiXDa0fHgW7cHHGiXqr` | bitable:app, im:chat, im:message |
| 龙虾 | 龙虾OpenClaw | `cli_aa95082153391be3` | `O8ljDi99fZgQvjwqHgeuwbjVUIoInWVj` | bitable:app, im:chat, drive:file |

## Base

- **名称**: 跳槽管线
- **app_token**: `FEAZbWbPoaJGnPs7DZAcsuWvndb`
- **URL**: https://rcn139sraus1.feishu.cn/base/FEAZbWbPoaJGnPs7DZAcsuWvndb

## 表1: 主动出击 (tblJpSB54ABcljfq)

> OpenClaw 主写，CC/Hermes 读写。替代旧「跳槽管线」表。

| 字段名 | field_id | 类型 | 选项 |
|--------|----------|------|------|
| 公司+职位 | — | 文本(主键) | — |
| JD链接 | — | URL | — |
| 状态 | — | 单选 | 待初筛/值得投/已归类/简历已生成/已投递/放弃/面试中/等待投递 |
| 我的核心优势 | — | 文本 | — |
| JD核心能力 | — | 文本 | OpenClaw分析填充 |
| JD核心要求 | — | 文本 | OpenClaw分析填充 |
| Hermes备注 | — | 文本 | Hermes初筛判断 |
| CC备注 | — | 文本 | CC/OpenClaw写匹配分+简历链接 |
| 投递截止 | — | 日期 | — |
| 投递日期 | — | 日期 | — |
| 面试记录 | — | 文本 | — |

**并发约定**: OpenClaw 独写此表（auto-scan + task完成时），Hermes只读，CC只在傍晚手动更新。避免写冲突。

## 表2: 面试进行中 (tbl0fIwrtlgeqChX)

> 从主动出击晋级到此表的面试阶段JD。

## 表3: Offer对比 (tbltMPWGqK2A3ytF)

> 拿到Offer后的对比分析。

## 表4: 已归档投递 (tblgSOBhxS64FEtd)

> 已投递完成的归档。

## 表5: 碎片收集区 (tblA4apFskqLsxsp)

> Hermes白天收集的碎片信息。不变。

| 字段名 | field_id | 类型 | 选项 |
|--------|----------|------|------|
| 内容摘要 | — | 文本(主键) | — |
| 详情 | — | 文本 | — |
| 类型 | — | 单选 | JD链接/猎头信息/想法碎片/行业情报/其他 |
| 关联JD | — | 文本 | — |
| 处理状态 | — | 单选 | 待处理/已处理 |

## 表6: 每日日志 (tblmJ2wjOGa4H1q3)

> Hermes/CC/olina三方写入的操作日志。

| 字段名 | field_id | 类型 | 选项 |
|--------|----------|------|------|
| 日期 | — | 日期 | — |
| 来源 | — | 单选 | Hermes/CC/olina |
| 类型 | — | 单选 | 任务/决策/备注/投递记录/面试记录/市场分析/新JD/Target追踪/离线沟通 |
| 内容 | — | 文本 | — |

## 群聊

- **跳槽管线-龙虾通知**: `oc_68559f460a68e6b1d77a9b188dcf1d3d`
  - OpenClaw 分析/生成完成后自动发消息到此群
  - CC 通过 `cc_msg.py` 在此群收发消息

## 飞书文档

- **协作协议v2**: https://rcn139sraus1.feishu.cn/docx/TOn1dPNoDocBiXxbqhUci9flnug
