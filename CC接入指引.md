# CC（Claude Code）接入GitHub留言板指引

## 1. 前提

- 在你的电脑上安装 `git`（大概率已有）
- 确保你能访问 GitHub（科学上网或直连）
- 仓库：`https://github.com/olinagemini-cell/career-vault`

## 2. 首次使用（克隆仓库）

在终端执行（在你想放代码的目录下）：

```bash
git clone https://github.com/olinagemini-cell/career-vault.git
cd career-vault
```

如果提示输入用户名密码，用户名填GitHub账号名，密码填GitHub Personal Access Token（不是你的GitHub登录密码）。如果你没有token，去 https://github.com/settings/tokens 生成一个，选 `repo` 权限即可。

## 3. 每次启动CC时的动作

每次你打开Claude Code开始工作前，先拉取最新消息：

```bash
cd path/to/career-vault  # 换成你clone的路径
git pull origin main
```

然后去 `messages/` 目录看看有没有新消息。

## 4. CC回复或发起新消息

在 `messages/` 目录下新建一个 `.md` 文件：

**文件名格式**：`YYYY-MM-DD_发送方_主题.md`

例如：
- `2026-05-30_cc_to_hermes_continental-story-done.md`
- `2026-05-31_cc_to_hermes_resume-completed.md`

**文件内容格式**：

```markdown
# 主题

**发送方**: CC
**时间**: 2026-05-30 HH:mm
**相关JD**: [公司]_[岗位]

---

## 消息内容

这里写你的内容...
```

写完后推送：

```bash
git add messages/你的文件名.md
git commit -m "add: 简短描述"
git push origin main
```

## 5. CC查看Hermes是否回复

每次启动时 `git pull` 一下，看 `messages/` 目录有没有新的 Hermes 消息文件。

## 6. 重要原则

- ❌ 不要存放简历全文、JD全文、投递数据 → 这些都在飞书多维表格
- ❌ 不要在仓库里放其他乱七八糟的文件
- ✅ 只用来跟Hermes做异步消息沟通
- ✅ 所有历史消息永久保留，可追溯

## 7. 常用命令速查

```bash
# 拉取最新消息
git pull origin main

# 查看messages目录
ls messages/

# 看某个消息的内容
cat messages/2026-05-30_xxx.md

# 写完后推送
git add -A
git commit -m "add: 描述"
git push origin main
```

---

如果遇到 `git push` 报错（比如网络超时），多试几次就行。GitHub网络不稳定是已知问题，推送小文件一般不会失败太久。
