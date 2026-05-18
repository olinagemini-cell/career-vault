# 跳槽工作目录 — Claude Code 指引

> **用途**：每次 Claude Code 在本目录工作时，先读这份。它定义了用户是谁、文件夹结构、JD 分析方法论、定向简历生成工作流。
> **最后更新**：2026-05-07

---

## 0. 用户基本信息（一句话）

刘小妍，14年项目群PM，最后一站BPCE（法巴 / 法国邮政集团 IT条线），目标方向：MNC IT BRM / 数字化转型PM / Senior Program Manager / Commercial IT PM-BA混合岗。

详细职业素材以下面这份文档为**唯一源（SSOT）**：
- `素材库/简历构建逻辑与职业履历素材库.md`

任何简历 bullet 落笔前，必须反向锁定到这份素材库里有据可查的经历。**JD 行话不等于素材**——这是定向简历最常见的越位错误。

---

## 1. 文件夹结构

```
跳槽/
├── CLAUDE.md                          ← 你现在读的这份
├── start_obsidian.bat                 ← 用户启动 Obsidian 的快捷方式（与 Claude 无关）
│
├── 素材库/                            ← 职业履历素材（SSOT）
│   ├── 简历构建逻辑与职业履历素材库.md   ★主源
│   ├── JD分析模板.md                   ← Claude Code JD分析输出模板
│   ├── 跳槽简历重构_进展与思路存档.md
│   └── Obsidian使用指南_跳槽文件夹.md
│
├── 我的简历/                          ← 简历生产资料（模块、模板、证件）
│   ├── skill-modules/CN/              ← 13个可复用技能模块.md  ★模块库唯一位置
│   │   ├── 00_模块索引.md              ★必读：模块清单 + 场景组合 + 压缩规则
│   │   └── (各模块文件)
│   ├── resume-templates/AI产品经理模板.md
│   └── 证件照.png / 身份证-*.png
│
├── 简历库/                            ← 投递成品归档
│   ├── 通用版/                        ← 通用简历（含稀缺性版）
│   └── _Archive/<月份>/<公司名>/       （定向版按公司归档）
│
└── JD库/_已分析/投递中/<公司_职位>/    ← 已投递 JD 原文（仅保留已投递的，作为反馈对照样本）
```

**结构规则**：
- 技能模块**只**放在 `我的简历/skill-modules/CN/`，不要再创建别的模块文件夹。
- JD 分析过程**不另建档案**，直接按 §3 在对话里跑 Phase 1 / 0.5 / 0；JD 原文存入 `JD库/_已分析/投递中/<公司名_职位名>/`，**只在确定要投递时才存档**。
- 定向简历输出到 `简历库/_Archive/<月份>/<公司名>/`。
- 通用版简历（含稀缺性版）**只放 `简历库/通用版/`**。

---

## 2. 用户偏好与硬性规则

### 2.1 简历内容
- **AI 工具名默认不写**（Claude / Perplexity / 飞书 / GPT 等）。AI 能力以"思维框架 + 部门知识资产沉淀"叙述。
  - **例外**：AI / 创新 / 数字化原生岗位，且 JD 或面试官明确鼓励工具熟练度时，可单独决策放开。这属于个案判断，不是默认行为。
- **诚实校准**：不 over-claim。对没真做过的 JD 术语（retain/retire/refactor、TIME/6R、Zero Trust 等），使用**两层关键词策略**：
  - ATS/HR 层：Summary 用中性上位词（rationalization、portfolio governance、data sovereignty）过筛
  - 面试层：诚实讲"upstream 经验 + 框架准备"
  - 禁区：具体术语不入正文 bullet
- **纯英文简历**：当前阶段只出英文简历，专注外企投递。英文简历按英文简历写法独立写作（不是中文翻译）。
- **领导力叙事**：核心竞争力是跨矩阵无授权影响力（cross-matrix influence without formal authority）——从Hertz的全球协作到NCR的跨职能协调到BPCE的HQ资源争取，这是贯穿始终的领导力签名。不写"管理X人团队"，也不主动暴露Hertz的7人团队数字（面试被问到时诚实回答即可）。
- **诚信边界已标注**：BPCE 不涉及供应商管理、SOX、DR 独立领导经验、Eaton 专有词汇（CAR / OC / Book of Business）—— 详见 `00_模块索引.md`。

### 2.2 简历格式
- **交付简历开头只有姓名 H1**，不要"目标岗位 / 核心定位 / 生成日期"等元数据头。
- **一页纸硬限制**（定向简历）。通用版 ≤1.5 页。
- **Captain narrative**，不是 checklist——突出 ownership 叙事。
- **不放匹配度对照表**进简历。
- 篇幅硬标：BPCE ≤180 字 / NCR ≤80 字 / WuXi & Hertz 各 1 行。10.5pt + 1.27cm 边距。

### 2.3 工作流
- 简历 .md 转 Word **用 `md2docx/md2docx.py` 自动完成**，输出 Times New Roman 10.5pt / 1.27cm 边距，格式开箱即用。
- JD 分析 + 简历生成都在 Claude Code 里完成（前情：曾试图用 Streamlit/Python 独立搭建，与 Claude Code 能力重复，已弃）。

---

## 3. JD 分析方法论

> 每次拿到新 JD，按这个流程跑一遍。**Claude 只负责到匹配度评估 + 缺口分类，"投不投"由用户决定。**

### 3.1 总体流程

> **输出模板**: 使用 `素材库/JD分析模板.md` 作为输出结构，确保每次分析格式一致。

```
JD 输入
  ↓
【Phase 1】意图分析       ← 回答"他们到底要什么样的人"
  ↓
【Phase 0.5】匹配度评分   ← 输出 % + 关键词命中清单
  ↓
【Phase 0】缺口分析       ← A/B/C 三类缺口分类
  ↓
【Post-Gap】缺口驱动能力刷新 ← 用缺口作为回忆线索，检查是否有新素材可补充
  ↓
（用户决定是否投递）
  ↓
【Phase 1-6】定向简历生成 ← 用 captain narrative 工作流
  ↓
输出：单页英文 .docx
```

### 3.2 Phase 1：意图分析

回答：**"他们真正想要什么样的人？"**

| 维度 | 问题 | 输出例子 |
|------|------|---------|
| 公司类型 | 服务商/交付型 vs 甲方/产品型 vs 咨询型？ | "医疗 IT 服务商 → 全能 captain" |
| 关键动词 | JD 中反复出现什么动词（≥2次）？ | "主导"/"端到端"/"关键沟通桥梁" |
| 真实诉求 | 这些动词背后的人物画像？ | "端到端交付官，不是功能执行者" |
| 角色定位 | 我是 internal partner 还是 vendor partner？ | BRM=internal；交付PM=vendor |

**输出**：一句话的人物画像。然后跟用户确认：✅继续 / ❌调整。

### 3.3 Phase 0.5：匹配度评分

**步骤**：
1. 从 JD 提取 10-20 个核心需求关键词
2. 每个关键词查 §4 的"模块→关键词映射表"，看能否落到我的某个技能模块
3. 计算覆盖率：`匹配度 = 命中关键词数 / JD 总关键词数 × 100%`
4. **输出格式**：
   - 总匹配度 X%
   - 命中关键词清单（落到哪个模块）
   - 未命中关键词清单（流向 Phase 0 缺口分析）
   - **不再给"投不投"的决策建议**——这是用户的事

### 3.4 Phase 0：缺口分析

对所有"未覆盖的 JD 需求"分类：

| 类型 | 含义 | 处理方案 |
|------|------|---------|
| **A类** | 我有这个模块，完整覆盖 | ✅ 直接用 |
| **B类** | 我有这个经历，但模块库没写 | 🔄 补充模块 → 更新索引 → 重新评分 |
| **C类** | 我真的没这个能力 | ⚠️ 用户决策：(1)放弃 (2)两层关键词策略+诚实面试 |

**B 类典型**："Salesforce CRM 管理我在 NCR 做过 5 年，为什么显示缺？" → 检查发现 ERPCRM 模块只有骨架没写 NCR 案例 → 补充模块内容 → 更新 `00_模块索引.md` → 重新评分。

### 3.5 Post-Gap 能力刷新（缺口驱动回忆）

**为什么放在 Phase 0 之后而不是之前？** 冷问"最近有没有新东西"很难回忆。把缺口（红灯/黄灯）作为回忆线索，比凭空提问高效得多。

**提问**（在 Phase 0 输出后问用户）：

1. **"看一下这些 B/C 类缺口，有没有哪个你最近刚好有相关经历可以补上？"** — 缺口是最有效的记忆触发器。用户可能意识到某个 C 类缺口其实是 B 类（有经历，模块没写）。
2. **"这家公司/行业你之前有没有相关接触，可以弥补行业陌生感？"** — 捕捉可能降低 C 类严重度的领域熟悉度。
3. **"看到这些缺口分布，有没有什么新的角度或故事是分析没覆盖到的？"** — 捕捉关键词匹配可能漏掉的新叙事素材。

**后续行动**（如果用户补充了新素材）：
- **C → B**：用户有真实经验 → 补充/新建模块 → 更新索引 → 重新评分
- **C 严重度降低**：领域熟悉度或相邻经验降低风险
- **发现新 A 类**：关键词匹配漏掉了用户实际有的能力

---

## 4. 模块 → JD 关键词映射表

JD 分析时用来对照"这个 JD 关键词命中了哪个模块"。模块文件都在 `我的简历/skill-modules/CN/`。

| 模块 | 状态 | 命中关键词 | 适配公司类型 | 适配岗位 |
|------|------|-----------|-------------|---------|
| **跨境数字化转型** | 🟢完整 | 全球-本地、全球化、系统集成、端到端交付、跨地域、多市场、海外运营、本地化、cross-border、global rollout、glocal | MNC、跨国、出海、外资 | 转型PM、Digital PM、Global PM |
| **投资组合管理** | 🟢完整 | 组合治理、portfolio、资源优化、PMO、项目群、多项目、并行项目、战略对齐、program governance | MNC、大型企业、IT部门 | PMO、Program Manager、Senior PM、Portfolio Manager |
| **业务分析BA** | 🟢完整 | 需求分析、需求管理、用户故事、backlog、流程梳理、UAT、用户验收、变更管理、commercial IT、BA | 服务商、IT咨询、甲方IT | PM/BA混合、BA、商业IT PM、Functional Analyst |
| **变革管理** | 🟢完整 | 变革管理、组织变革、用户采纳、adoption、利益相关方、stakeholder、培训、change enablement、resistance management | MNC、大型企业、咨询 | 变革PM、转型PM、Change Manager、Delivery PM |
| **业务关系管理BRM** | 🟢完整 | BRM、trusted advisor、business partner、primary interface、shape IT demand、demand management、business value、ROI、business case、QBR、escalation | MNC、大型企业、金融 | IT BRM、IT Director、Principal PM、Senior PM |
| **商业论证与预算治理** | 🟢完整 | business case、business justification、预算、budget、P&L、cost、ROI、financial governance、funding、profit plan、cash-out、CapEx、OpEx | MNC、大型企业、金融 | IT Director、Portfolio Manager、PM、IT Finance |
| **供应商与合同管理** | 🟡部分（NCR重仓、BPCE不涉及） | vendor management、合同、SLA、RFP、vendor scorecard、negotiation、procurement、vendor selection | MNC、IT部门、采购型PMO、金融 | IT Director、PMO、Vendor Manager、Procurement Manager |
| **ERP/CRM系统** | 🟡部分 | ERP、SAP、Oracle、CRM、Salesforce、SFE、workflow、流程自动化、integration、MDM、user adoption、系统上线 | 服务商、商业IT、咨询、甲方IT | 商业IT PM、ERP PM、CRM PM、系统实施 |
| **AI赋能项目管理** | 🟢完整 | AI、Gen-AI、大模型、AI应用、automation、流程优化、效率提升、知识管理、AI赋能 | 创新企业、科技公司 | AI PM、创新PM、数字化PM |
| **云迁移云架构** | 🔴待补充 | 云迁移、cloud migration、云架构、hybrid cloud、multi-cloud、IaaS、PaaS、disaster recovery | MNC、云服务商 | Cloud PM、Infrastructure PM |
| **中国数据合规PIPL** | 🟡部分（BPCE真实经验） | PIPL、个人信息保护法、data residency、数据本地化、跨境数据、等保、MLPS、GDPR、compliance、data governance | MNC、外资金融、数据驱动 | 数字化转型PM、合规PM、数据治理 |
| **身份与访问管理IAM** | ⚫缺失 | IAM、AD、Active Directory、零信任、zero trust、segmentation、access control、SSO | MNC、大型IT、金融 | Security PM、Infrastructure PM |
| **应用组合治理APM** | ⚫缺失 | application portfolio、rationalization、应用盘点、retain/retire/replace/refactor、TIME model、6R、sunset planning | MNC、大型企业、金融 | IT Director、Transformation PM |
| **AI治理AI Governance** | ⚫缺失 | AI governance、Gen AI合规、AI风险评估、企业级AI策略、responsible AI | MNC、金融、科技 | AI治理PM、合规PM |
| **数据驱动治理与低代码平台** | 🟢完整 | 数据驱动、数据可视化、dashboard、Power BI、低代码、low-code、飞书多维表格、数据建模、报表开发、BI、数据中枢、ROI论证、数据驱动决策 | MNC、商业IT、数字化PM | IT PM（含BI职责）、数字化转型PM、Commercial IT PM |
| **基础信息** | 🟢必选 | — | 所有 | 所有 |
| **教育认证** | 🟢必选 | — | 所有 | 所有 |

**JD 高频信号词**（用于快速识别 JD 类型）：
- 高频动词：主导、负责端到端、关键沟通桥梁、独立统筹、管理集成
- 高频技能词：CRM、ERP、SAP、Salesforce、数据治理、流程优化
- 高频特征词：MNC、全球、转型、敏捷、PMO

---

## 5. 模块组合速查（按岗位类型）

详细组合见 `我的简历/skill-modules/CN/00_模块索引.md`。常用六种：

| 岗位类型 | 必选 | 核心 | 补充 | 预期匹配度 |
|---------|------|------|------|-----------|
| MNC 数字化转型 PM | 基础信息+教育认证 | 跨境数字化转型 + 投资组合管理 | 变革管理 + PIPL | 85-95% |
| PMO / Senior PM | 基础信息+教育认证 | 投资组合管理 | AI赋能 + 变革管理 | 80-90% |
| 商业 IT PM/BA | 基础信息+教育认证 | 跨境数字化转型 + 业务分析BA | ERP/CRM + 变革管理 | 75-85% |
| Implementation PM | 基础信息+教育认证 | 变革管理 | 投资组合 + BA | 70-80% |
| IT BRM / IT Director | 基础信息+教育认证 | BRM + 投资组合 + 商业论证 | 供应商管理 + 跨境 | 85-95% |
| Program Manager / PMO | 基础信息+教育认证 | 投资组合管理 | 商业论证 + 供应商 | 80-90% |
| 数据驱动PM / 商业IT PM | 基础信息+教育认证 | 业务分析BA + 数据驱动治理与低代码平台 | 跨境数字化转型 + AI赋能 | 75-85% |

---

## 6. 定向简历生成工作流（Phase 1-6）

用户决定要投后进入：

| Phase | 任务 | 关键约束 |
|-------|------|---------|
| 1 | 分析 JD 意图 + 公司性质 | 输出一句话人物画像 |
| 2 | 一页纸硬限制设计 | 结构框架定好 |
| 3 | 组织 captain narrative（不是 checklist） | ownership 叙事 |
| 4 | 诚实校准（防 over-claim） | 反向锁定素材库 |
| 5 | 诚信审查：每句话对标素材库 | 用户直觉 = 最后防线 |
| 6 | 压缩 pass | 见下文压缩规则 |

**输出**：
- **纯英文单文件**，输出 `.md` → 自动转换 `.docx`
- **Phase 6 结束后必须运行 `python md2docx/md2docx.py <file.md>` 转成 .docx**（HR/猎头无法读 .md）
- 路径：`简历库/_Archive/<月份>/<公司名>/`
- 命名：`刘小妍_上海_<公司名>_<职位名>.md` → `.docx`
- **投递策略**：LinkedIn / 外企官网 / 猎头均用英文单文件
- 转换工具：`md2docx/md2docx.py` — Times New Roman 10.5pt / 1.27cm边距 / 22pt-16pt-14pt 标题层级，输出开箱即用

### Phase 6 压缩规则（硬要求）

1. **培训/认证不单独成 bullet**——"参与过 X training"不算工作成绩，认证归到 cert 行
2. **项目细节不展开**——具体数字（EPM 30%、YUM 5%/20%）压到 aggregate 成绩（#1 ROI 3 年、零事故 20+ 发布），细节留面试
3. **同作用域 bullet 合并**——例如 "Primary interface" + "Financial governance" 都在描述 ownership scope，合并
4. **非 AI 岗直接切 AI bullet**——BRM/portfolio/vendor 类岗位上 AI 是稀释项不是加分项
5. **篇幅硬标**——BPCE ≤180 字 / NCR ≤80 字 / WuXi & Hertz 各 1 行；总 ≤1.5 页

---

## 7. 模块新增/更新流程（B 类缺口处理）

当发现"用户做过但模块库没写"：

```
1. 跟用户对一遍：确认这段经历在哪家公司、哪个项目、哪些可量化成果
2. 在 我的简历/skill-modules/CN/ 新建 <模块名>.md
   结构按 00_模块索引.md 末尾的"模块内容结构"模板：
     模块元信息 / 技能定义 / 现有经验映射 / 知识框架 / 技能差距 / 简历呈现 / 面试准备
3. 更新 00_模块索引.md 的清单（状态、市场频率、组合场景）
4. 更新本文件 §4 的关键词映射表（新增一行）
5. 重新跑 Phase 0.5 评分
```

---

## 8. 不要做的事

- ❌ 不要再单独搭建 Python/Streamlit 简历引擎——已弃，分析+生成全部在 Claude Code 里
- ❌ 不要在简历里写 AI 工具名（Claude / Perplexity / 飞书 等），除非 §2.1 例外条件成立且用户单独同意
- ❌ 不要在交付简历开头写"目标岗位 / 核心定位 / 生成日期"
- ❌ 不要把 JD 行话直接套进简历正文 bullet（必须反向锁素材）
- ❌ 不要把"培训"包装成"工作成绩"
- ❌ 不要主动给"投不投"的决策建议——只输出匹配度 + 缺口分析，决策权留给用户
- ❌ 不要重建 Pandoc 工具链——已有 `md2docx/` 小工具，用就完了
- ❌ 不要在 `素材库/`、`我的简历/skill-modules/CN/` 之外另建模块文件夹
- ❌ 不要把未投递的 JD 存进 `JD库/`——只在确定要投递时才存档原文

---

*历史沉淀：原 §3.5 投递决策矩阵、§8 反馈循环、Pandoc 工具链、技能频率统计表、能力-JD 关系索引、BA 经验挖掘引导方案、Centific 历史 JD 案例 —— 均已在 2026-04-25 评估后删除。如未来恢复反馈循环或决策矩阵，重新加回即可。*
