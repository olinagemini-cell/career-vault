# CC（Claude Code）接入飞书群指引

> GitHub `messages/` 目录已废弃（2026-06-03）。实时通信统一走飞书群。

## 飞书群

- **群名**: 跳槽管线-龙虾通知
- **chat_id**: `oc_68559f460a68e6b1d77a9b188dcf1d3d`
- **成员**: Hermes + 龙虾(OpenClaw) + CC

## CC工具

所有工具在 `~/Desktop/Improve/` 下：

```bash
# 启动检查（每次CC启动运行）
python ~/Desktop/Improve/startup_check.py

# 读群消息
python ~/Desktop/Improve/cc_msg.py read

# 发消息到群
python ~/Desktop/Improve/cc_msg.py send "消息内容"

# 看未读（自上次CC发言后的消息）
python ~/Desktop/Improve/cc_msg.py unread
```

## 消息格式

群里三方都用前缀标识身份：

| 发送方 | 前缀 |
|--------|------|
| CC | `[CC] 消息内容` |
| Hermes | `[Hermes] 消息内容` |
| 龙虾 | `[OpenClaw] 消息内容` |

`cc_msg.py send` 会自动加 `[CC]` 前缀。

## 协议文档

- **协作协议v3**: `~/.claude/career-vault/hermes_to_cc_protocol.md`
- **飞书配置**: `~/.claude/career-vault/feishu_config.md`

---

## 历史：GitHub messages（已废弃）

> 以下为旧方案，仅作参考。不再使用。

~~在 `messages/` 目录下新建 `.md` 文件进行异步通信。~~
~~文件名格式：`YYYY-MM-DD_发送方_主题.md`~~

历史消息保留在 `~/.claude/career-vault/messages/`，不删。
