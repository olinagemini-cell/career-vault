# career-vault

Hermes ↔ CC 共享记忆仓库。两边 agent 的持久化大脑。

## 规则

1. **写入格式**：`## [来源] YYYY-MM-DD` + 内容。来源填 `CC` 或 `Hermes` 或 `User`
2. **每次写入追加在对应文件末尾**（或对应日期段），不要覆盖已有内容
3. **每次启动时先 `git pull`**，获取对方最新记忆
4. **每条记录写完后 `git push`**，确保对方能读到
5. **只记结论、决策、偏好**，不记聊天流水账

## 文件结构

| 文件 | 内容 |
|------|------|
| `profile.md` | 用户画像：偏好、价值观、工作风格、敏感点 |
| `memory.md` | 共享记忆：重要决策、项目状态、关键结论 |

## 接入方式

```bash
git clone git@github.com:olinagemini-cell/career-vault.git
# 或
git clone https://github.com/olinagemini-cell/career-vault.git
```
