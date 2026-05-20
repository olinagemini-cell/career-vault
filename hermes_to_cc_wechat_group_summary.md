# Hermes → CC：微信群消息增量汇总脚本

## 背景

用户有一个日活几百条的微信群，想知道「从我上次汇总到现在，群里新增了什么话题」。用户接受**手动触发**（想看的时候双击跑一次），不需要常驻服务。

你已经打通了解密管道（find_all_keys.py → decrypt_db.py），以下是基于你已验证成果的完整方案。

---

## 整体流程

用户双击 `summarize_wechat_group.bat` →
输入小时数（如 "18" 表示过去18小时） →
你的脚本工作：
1. 密钥提取（用你已验证的 find_all_keys.py 或 WeChatMsg CLI）
2. 解密DB
3. 查询消息：WHERE timestamp > (now - N小时) AND local_type=1 AND WCDB_CT=0
4. 按 sender 分块，按关键词聚类话题
5. 输出 `微信群_摘要_{日期}.txt`

---

## 第一步：确定目标群的表名

用户会告诉你群名（中文）。你需要做一次性的映射：

```
session.db → SessionTable → 查群名 → 拿到群ID（一串数字）
群ID → MD5 → 得到 message_0.db 里的表名 Msg_{MD5hash}
```

这个映射**只需要做一次**，记下来硬编码到脚本里（比如放到一个群配置JSON）：
```json
{
  "groups": {
    "XXX群": {
      "db": "message_0.db",
      "table": "Msg_{MD5hash}"
    }
  }
}
```

后续用户不管问多少次，直接查这个表就行，不需要重新映射。

---

## 第二步：增量查询

用户输入的 N 小时，转换为 Unix 秒时间戳（你已验证过 WeChat 时间戳是 Unix 秒）：

```sql
SELECT CreateTime, strSender, strContent
FROM Msg_{MD5hash}
WHERE CreateTime > (unix_timestamp() - N*3600)
  AND local_type = 1
  AND WCDB_CT = 0
ORDER BY CreateTime ASC
```

⚠️ 注意：用 `strSender` 而不是 StrTalker（调试确认字段名）。

---

## 第三步：消息聚类输出

不要一股脑堆原始消息。按这个格式输出摘要：

```
=== 微信群消息摘要 ===
查询范围：过去18小时（2026-05-21 08:00 ~ 2026-05-22 02:00）
共计 X 条消息

--- 话题1：关于XX讨论 ---
发言人A：XXX
发言人B：XXX
（2条消息，核心观点：XXX）

--- 话题2：关于YY讨论 ---
发言人C：XXX
（1条消息）

--- 未归类的零散消息（X条）---
（人少、话题不集中，仅列出发言人+摘要）
```

聚类逻辑推荐按「提及关键词」或「连续时间段内同一sender连续话题」做简单分组——不需要NLP，找高频关键词 + 时间窗口聚合即可。

---

## 第四步：输出文件

输出到桌面上，例如：
```
C:\Users\{用户名}\Desktop\微信群_摘要_2026-05-22.txt
```

用户看一眼就行。如果祂想让我（Hermes）做进一步深度分析，把文件内容复制/发给我即可。这一步**不是必须的**。

---

## 汇总：你最终交付什么

| 交付物 | 说明 |
|--------|------|
| `summarize_wechat_group.py` | 主脚本：解密 → 查询 → 聚类 → 输出 |
| `group_config.json` | 群名→表名映射（你手动填一次） |
| `run.bat` | 双击启动，提示输入小时数 |
| `requirements.txt` | 依赖（若需要） |

---

## 已知踩坑（你的经验，已验证）

- `x'<hex>'` = 96hex（64key + 32salt），不是64hex
- `message_0.db` 和 `biz_message_0.db` 是不同DB，key要匹配精确
- 消息 content 已是 str，decode 会报错
- WeChat 时间戳是 Unix 秒，不是毫秒
- 需要管理员权限 + 微信登录状态

## 新增注意（来自Hermes）

- 增量查询的 `WHERE CreateTime > X` 必须加上 `ORDER BY CreateTime ASC`，方便用户按时间线阅读
- 如果群太活跃（几百条），建议追加 `LIMIT 200` 防止脚本跑太久或输出文件太大
- 输出文件编码用 UTF-8（避免中文乱码）
- 如果用户没输入小时数，默认过去24小时
- `local_type` 和 `WCDB_CT` 这些过滤条件最好在脚本里加注释说明每条是干什么的，方便以后微信升级字段变化时排查

---

## 交付验收标准

1. ✅ 双击 `run.bat`，提示"请输入要回溯的小时数（默认24h）："
2. ✅ 输入后脚本执行，不报错
3. ✅ 桌面生成 `微信群_摘要_YYYY-MM-DD.txt`
4. ✅ 文件内容按话题分组，可读性强
5. ✅ 第二次运行时，输出与第一次不冲突（不同文件名）
