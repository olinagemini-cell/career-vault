# career-vault

个人职业与知识管理仓库。由 Hermes Agent 维护与使用。

## 目录结构

```
career-vault/
│
├── career/                          ← 跳槽相关 · 核心内容
│   ├── resumes/
│   │   ├── skill-modules/CN/         技能模块（15个）—— 最核心资产
│   │   ├── 简历库/                   投递过的各版本简历
│   │   │   ├── 通用版/                 通用简历模板
│   │   │   └── _Archive/              旧投递记录备查
│   │   └── 素材库/                   策略 / 模板 / 笔记
│   │
│   └── jd_collection/              收集的JD及深度分析
│       └── 强生医疗_IT项目经理/       含Phase 1-5完整分析流程
│
├── skills/                          Hermes Agent技能存放
│
├── resume_rules.md                  简历构建规则
│
└── README.md                        本文件
```

## 使用方式

- **文件格式**：Markdown 优先（.md），docx/PDF为投递存档
- **文件名规范**：`Olina_Liu_公司名_岗位名_EN/CN.md`（简历）；`JD原文.md` + `PhaseN_描述.md`（JD分析）
- **维护者**：Hermes Agent（你）—— 收到新JD或修改简历时，通过GitHub API直接操作，无需本地clone
- **协作模式**：用户在微信上发JD/改需求 → Hermes读取skill modules → 写简历 → 推回仓库

## 关于这个仓库

最初是为了让 Hermes Agent 能读取简历素材、Skill Modules 和 JD 分析，方便定向写简历和准备面试。后来演变成完整的职业管理中枢。

**当前状态**：2026-05-10 大清理后，只保留跳槽相关内容。
- ✅ 已删除：`legal/`（诉讼材料）、`ai-learning/`（学习笔记）、`_archive/`（空目录）
- ✅ 保留：全部15个Skill Modules + 简历库 + JD库 + 素材库

## Hermes Agent 维护指令

Hermes 通过 GitHub API 操作此仓库（无需 clone）：
- 读文件：`GET /repos/olinagemini-cell/career-vault/contents/{path}`
- 写文件：`PUT /repos/olinagemini-cell/career-vault/contents/{path}`
- 删文件：`DELETE /repos/olinagemini-cell/career-vault/contents/{path}`
- 查结构：`GET /repos/olinagemini-cell/career-vault/git/trees/main?recursive=1`
