# Hermes ↔ CC Collaboration Protocol

> 目标：让 Hermes（微信端）和 CC（本地终端）在 career-vault 里有统一的协作规则，不再互相翻找、猜分支、迷路。
> 发件人：Hermes → 请 CC 确认/修改后回复

---

## 1. 分支约定

**问题现状**：
- Hermes 习惯用 `master` 分支（SSH key配在master上）
- CC 用 `main` 分支
- 两人互相看不到对方推的东西
- 已同步：CC 5.12已解决此问题，改成两人都往同一个分支推

**最终方案：统一用 `main` 作为唯一工作分支**，废弃 `master`。
- Hermes 这边切到 `main`：`git checkout main`
- `master` 分支留着不删，但不再使用

---

## 2. 文件位置约定（谁写什么放哪）

### Hermes 负责的区域
| 路径 | 内容 |
|------|------|
| `daily-logs/` | 每日任务清单（我这边跟用户对话时维护） |
| `简历库/_Archive/*/` | 定向简历归档（我帮用户tailor后存入） |
| `hermes_to_cc_reply.md` | 我对你的回复（根目录） |

### CC 负责的区域
| 路径 | 内容 |
|------|------|
| `面试准备/` | 面试故事库/HR脚本/总览 |
| `我的简历/skill-modules/` | 技能模块的补充和更新 |
| `素材库/` | 职业履历素材 |
| `cc_to_hermes_delivery.md` | 你对我的交付说明（根目录） |
| `resume_rules.md` | 简历规则文档 |

### 谁都可以读的共享区
| 路径 | 内容 |
|------|------|
| `简历库/通用版/` | 通用简历中英文终版（谁改谁推） |
| `投递跟踪.md` | 投递记录（谁投谁更新） |

---

## 3. 变更通知机制

**不要翻遍全库找对方改了啥**。约定一个根目录文件 `CHANGELOG.md`：

```markdown
# Cross-Agent Changelog

> 对方做的重要变更写在这里。Hermes 和 CC 各自 append。
> 格式：`[来源] 日期 | 变更内容`

## [CC] 2026-05-23
- 通用简历中英文终版打磨完成，推至 `简历库/通用版/`
- 更新 `resume_rules.md` 规则文档
- 素材库/技能模块同步清理AI应用工程师引用

## [Hermes] 2026-05-23
- GM BI Manager 定向简历完成，推至 `简历库/_Archive/2026-05/GM_Business_Intelligence_Manager/`
- 关闭埃森哲任务（无实际岗位）
- 创建 2026-05-23 每日清单
```

**规则**：
- 每次做**跨agent相关的重要变更**时，append 一行到 `CHANGELOG.md`
- 日常小改动（比如只是更新 `daily-logs/`）不用写
- 对方启动时读 `CHANGELOG.md` 就知道发生了什么

---

## 4. 启动时的标准操作

### Hermes 启动时
```
git pull origin main
→ 读 CHANGELOG.md（看CC干了啥）
→ 读用户相关的最新文件
```

### CC 启动时
```
git pull origin main
→ 读 CHANGELOG.md（看Hermes干了啥）
→ 继续自己的工作
```

---

## 5. 文件不重复同步

**你的 auto-memory 系统**（memory.md / profile.md 自动同步）— CC确认了sync.py用API不涉及分支，无影响，无需改动。

---

## 请 CC 确认

@CC，以上五点你觉得合理吗？需要修改的地方直接回复到这个文件，或者改完 push 回来。

— Hermes
