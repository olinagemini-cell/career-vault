# 10 — SIT 测试常见问题（FAQ）

> **目标读者**：甲乙双方所有项目成员
> **维护人**：甲方 PM
> **最后更新**：2026-03-29
> **更新频率**：持续更新（每当乙方提出知识库未能解答的问题时）
> **关联文档**：00（索引）、01-09（各专项文档）、11（模板集）

---

## 如何使用本文档

本 FAQ 汇集了 SIT 项目中**最高频的问题**，按主题分类。每个问题标注了详细答案的出处文档，方便进一步查阅。

**查找方式**：
- 按分类浏览（产品、规则、字段、流程、缺陷、自动化）
- 使用 Ctrl+F 搜索关键词

---

## 分类一：产品与合同类型

**Q1: 有哪些可用的产品类型？各自对应 Odessa 的哪个模块？**

A: 共 3 种产品类型：

| 产品类型 | 市场 | Odessa 模块 |
|---|---|---|
| Finance Lease China | 中国大陆 | Lease |
| AOR CHINA | 中国大陆 | Loan |
| HKG Financial Lease (DL, SLB) | 香港 | Lease |

核心要点：产品类型决定 Odessa 模块选择。选错将导致整套字段验证规则完全错误。
> 详见文档 01，第 1.1 节

---

**Q2: Campaign 和 Acquisition Channel 有什么区别？容易混淆怎么办？**

A: 这是**最常见的混淆点**，必须区分清楚：
- **Campaign**（如 "Direct Lease"）= 租赁结构类型，决定交易是直租、回租还是 AOR
- **Acquisition Channel**（如 "Direct"）= 获客渠道，决定客户是直接获取还是通过经销商引入

一笔交易可以是 Campaign = "Direct Lease" 且 Acquisition Channel = "International Manufacturer"，意思是"通过经销商渠道发起的直租业务"。
> 详见文档 01，第 1.3 节

---

**Q3: Campaign 如何映射到 Odessa 中的 Deal Type 和 Transaction Type？**

A:

| QT Campaign | Odessa Deal Type | Odessa Transaction Type | Odessa 模块 |
|---|---|---|---|
| Direct Lease | Finance Lease | Direct Lease | Lease |
| SLB | Finance Lease | SLB | Lease |
| AOR | Unsecured Loan | AOR | Loan |

> 详见文档 01，第 1.3 节

---

**Q4: 当前集成数据中定义了多少个测试用例？如何组织的？**

A: 共 32 个测试用例。分为两大类：
- **标准合同类型**（TC1-TC10）：覆盖主要的销售渠道 + 租赁结构组合
- **变体合同类型**：在标准类型基础上附加修饰项（抵押、非标还款、担保人等）

每种合同类型至少应有一个固定利率和一个浮动利率的测试用例。
> 详见文档 01，第 1.2 节

---

## 分类二：业务规则与条件逻辑

**Q5: 中国大陆和香港在系统中的主要差异有哪些？**

A: 关键差异一览：

| 属性 | 中国大陆 | 香港 |
|---|---|---|
| 币种 | CNY | HKD |
| 法律实体 | BPCE Equipment Solutions China Co Ltd | BPCE Equipment Solutions Hong Kong |
| 租金 VAT | 是（13%） | 否 |
| 收款方 | BPCE-CNY | BPCE-HKD |
| 可用产品 | Finance Lease, AOR | HKG Financial Lease |

> 详见文档 02，第 2.1 节

---

**Q6: 中登状态（ZhongDeng Status）的默认值是什么？如果值不对是什么问题？**

A: 默认值始终 = **Pending**。如果不是 Pending，说明是**配置缺陷**（系统设置问题），而非数据录入错误。中登是监管合规要求，值不对有合规风险。
> 详见文档 02，第 2.2 节

---

**Q7: Inception Payment（起始付款）如何计算？**

A: `Inception Payment = First Installment ÷ (1 + VAT Rate)`

此公式用于校验 Odessa Structure 标签页中的值。如果计算有误，缺陷在于计算逻辑，而非输入数据。
> 详见文档 02，第 2.3 节

---

**Q8: Financed Amount（融资金额）如何计算？**

A: `Financed Amount = Net Asset Amount − Down Payment`

在 Origination 中为不可编辑字段，由系统自动计算。如果值有误，属于**系统缺陷**。
> 详见文档 02，第 2.3 节

---

**Q9: 利率类型（Rate Type）= Fixed 和 Floating 时，Odessa 中的字段有什么区别？**

A: 这是最容易出错的领域之一。关键区别：

| Odessa 字段 | Fixed（固定） | Floating（浮动） |
|---|---|---|
| Float Rate Lease | No | Yes |
| Float Rate Index | 空/禁用 | LPR |
| Base Rate % | 不适用 | = QT Cost of Funds |
| Spread % | 不适用 | = QT Margin |
| Interest Rate % | = COF + Margin | = Base Rate + Spread |
| Float Rate Reset Unit | 不适用 | 12 months |

最常见的集成缺陷：Rate Type = Fixed 时浮动相关字段被意外填充（或反之）。
> 详见文档 02，第 2.4 节

---

**Q10: 还款方式 Advance（先付）和 Arrears（后付）对 Odessa 有什么影响？**

A:

| Odessa 字段 | Advance（先付） | Arrears（后付） |
|---|---|---|
| Advance (Structure) | Yes | No |
| # of Inception Payments | 1 | 0 |
| Residual Value in Last Installment | Yes（如配置） | 不适用 |

> 详见文档 02，第 2.5 节

---

## 分类三：角色与系统流程

**Q11: Supplier（供应商）和 Vendor（经销商/Dealer）有什么区别？**

A: 这是**最常见的混淆之一**：
- **Supplier** = 资产的原始所有者/出售方。在发票上显示为收款人（Payee）
- **Vendor / Dealer** = 将交易引入 BPCE 的渠道合作伙伴。可能与 Supplier 为同一实体，也可能不同
- **Direct 交易**中可能没有 Vendor/Dealer
- **Vendor Program 交易**中 Vendor/Dealer 负责介绍客户

> 详见文档 03，第 3.1 节

---

**Q12: 应该在 Odessa 的 Lease 模块还是 Loan 模块中搜索合同？**

A: 取决于 Campaign 类型：
- **Direct Lease / SLB** → Lease 模块
- **AOR** → Loan 模块

在 Lease 模块中搜索 AOR 交易**不会返回任何结果**。搜不到合同时，先确认是否进入了正确的模块。
> 详见文档 03，第 3.2 节

---

**Q13: 一笔交易从头到尾要经过哪些系统？每个系统做什么？**

A:
```
QT（报价工具）→ Origination（审批系统）→ Odessa（后台系统）
```
- **QT**：创建报价、选择资产、设置参数、计算 IRR — 共 22 个操作
- **Origination**：验证交易数据、配置发票、信用审批 — 共 14 个操作
- **Odessa**：验证合同所有字段、验证还款计划、启动交易 — 共 23 个操作

总计 59 个操作（原文档为 51 个独立操作，后续细化为 59 个执行步骤）。
> 详见文档 03，第 3.3 节；文档 06 完整操作列表

---

## 分类四：字段映射与验证

**Q14: QT 的哪个字段映射到 Origination 的 Net Amount？**

A: QT 的 **Net Purchase Price** → Origination 的 **Net Amount**（🔒不可编辑）。计算方式：Unit Price × Quantity。如果值有误，属于系统缺陷。
> 详见文档 04，交易结构部分

---

**Q15: Origination 中哪些字段是不可编辑（锁定）的？**

A: 共 11 个不可编辑字段：
- 交易概览：5 个（Deal Phase, Financial Product, Campaign, Entity, Deal ID）
- 资产详情：1 个（AMT References）
- 交易结构：5 个（Net Amount, Financed Amount, # of Payments, Seasonal Payment Type, IRR）

这 11 个字段由系统控制或自动计算——值有误属于**系统缺陷**。
> 详见文档 04，快速汇总部分

---

**Q16: Odessa 的 Remit To 字段应该显示什么？**

A: 取决于法律实体：
- **China 实体** → BPCE-CNY
- **Hong Kong 实体** → BPCE-HKD

适用于 Lease Billing > Remit To 和 Loan Billing > Remit To。
> 详见文档 02，第 2.6 节；文档 05，Lease Billing 部分

---

**Q17: Odessa 字段验证有哪几种类型？各自代表什么？**

A: 共 4 种验证类型：
- **Validate（验证）**：将 Odessa 值与 Origination/QT 源进行比对
- **Auto-default（自动默认）**：系统应自动填充的固定值
- **Conditional（条件）**：值取决于另一字段（需查规则）
- **Calculated（计算）**：值由公式推导（参见文档 02 第 2.3 节的公式）

Origination → Odessa 共约 154 个字段（Lease ~95、Loan ~45、Customer 14）。
> 详见文档 05

---

## 分类五：测试执行与操作

**Q18: 执行一个完整端到端测试用例前需要准备什么？**

A: 开始前必须：
1. 打开 `China_end_to_end_test.xlsx` 中的 Integration Data 工作表
2. 找到你的测试用例所在行（TC1、TC2 等）
3. 确认已在正确的系统环境中登录
4. 准备好记录工具（用于记录报价编号、交易编号）

> 详见文档 06，"开始之前"部分

---

**Q19: 测试中哪些操作必须由人工完成，无法自动化？**

A: 仅 **1 个操作完全依赖人工**：
- **B13 — 信贷审批工作流**：需要具有审批权限的授权签字人，涉及 Credit → CRO → Committee → LOD1 多阶段

另有 **8 个混合操作**（AI 完成 70-80%，人工审核异常），包括：
- A21：验证模拟结果（人工确认商业合理性）
- C17：验证还款计划（人工审核差异行）
- C19：验证混合项目（人工验证入账逻辑）
- C22：验证第三方关系（人工审核低置信度匹配）
- C23：带警告启动交易（人工决定是否覆盖警告）

> 详见文档 06 + 文档 07，第 7.2 节

---

**Q20: 完成测试后需要做哪些收尾工作？**

A: 执行后检查清单：
- [ ] 在 Deals Automated 工作表中记录结果
- [ ] 如有验证失败：使用文档 08 第 8.1 节的决策树分类缺陷
- [ ] 如出现知识库未涵盖的新问题：记录并提交给 PM
- [ ] 如测试用例已完全自动化：更新文档 07 的自动化状态

> 详见文档 06，执行后检查清单

---

## 分类六：缺陷分类与管理

**Q21: 字段验证失败了——这是谁的缺陷？怎么判断？**

A: 使用缺陷分类决策树：

| 现象 | 缺陷类型 | 责任方 |
|------|---------|--------|
| Origination 值正确，Odessa 值错误 | 集成缺陷 | 乙方 |
| QT 值正确，Origination 值错误 | Origination 缺陷 | 乙方 |
| QT 本身的值就错误 | 测试数据问题 | 甲方 |
| 默认值不正确（如中登 ≠ Pending） | 配置缺陷 | 乙方 |
| 计算值不正确（如到期日偏差） | 计算缺陷 | 乙方 |

> 详见文档 08，第 8.1 节

---

**Q22: 缺陷优先级如何定义？**

A:

| 优先级 | 定义 | 示例 |
|---|---|---|
| P1 严重 | 阻塞所有测试或导致数据损坏 | 合同完全无法落地 Odessa |
| P2 高 | 特定合同类型或字段类别异常 | 所有浮动利率字段显示为固定值 |
| P3 中 | 单个字段不正确但有变通 | Tax Code 显示错误值 |
| P4 低 | 外观或非功能性问题 | 字段标签不匹配 |

> 详见文档 08，第 8.1 节

---

**Q23: 如何用 AI 快速生成标准化的 Bug 报告？**

A: 将你发现的问题用口语描述，配合以下信息提供给 AI：
- 功能模块、测试环境、浏览器/设备、账号角色

AI 会输出标准格式：Bug 标题、严重程度、重现步骤、预期结果、实际结果、影响范围、附件建议。

> 详见文档 11 模板集中的"缺陷报告模板"；场景文档第 6.3 节

---

## 分类七：自动化与 AI 策略

**Q24: 哪些操作可以自动化？当前自动化覆盖率是多少？**

A:

| 分类 | 数量 | 占比 |
|---|---|---|
| AI 可自动化 | 37 | 73% |
| Hybrid（AI+人工） | 12 | 23% |
| 必须人工 | 2 | 4% |

使用 AI 自动化后，每个测试用例从约 3-4 小时降至约 30-45 分钟，节省 75-85%。
> 详见文档 07，第 7.1 节

---

**Q25: 自动化实施的优先级是什么？先做什么？**

A: 三层路线图：
- **Tier 1（第 1-2 周）**：RPA 自动化 QT 数据录入 + Python 断言框架覆盖 60+ 字段验证 → 立即见效
- **Tier 2（第 2-4 周）**：LLM 截图验证 + 还款计划比对器 + 测试数据生成器 → 中期价值
- **Tier 3（第 2 月+）**：端到端编排器 + 知识库自动更新 → 战略级

> 详见文档 07，第 7.3 节

---

## 分类八：项目管理与进度

**Q26: 当前 SIT 测试执行进度如何？主要风险是什么？**

A: 截至最新统计：
- 已完成且成功落地 Odessa：7 个（18%）
- 已完成但落地失败：6 个（16%）— 需根因分析
- 工作流未完成：9 个（24%）— 被审批流程阻塞
- 尚未开始：16 个（42%）— 最大进度风险

主要风险：42% 测试用例未启动 + 仅 7 个完全成功（不足以完成 SIT 签收）。
> 详见文档 08，第 8.2 节

---

**Q27: AOR 代表什么？其他常用缩写呢？**

A: 常用缩写速查：

| 缩写 | 全称 | 含义 |
|---|---|---|
| AOR | Asset Operating Rental | 资产经营性租赁 |
| DL | Direct Lease | 直接租赁 |
| SLB | Sale-and-Leaseback | 售后回租 |
| HP | Hire Purchase | 分期付款购买（香港） |
| ORV | Optional Residual Value | 可选残值 |
| COF | Cost of Funds | 资金成本 |
| LPR | Loan Prime Rate | 贷款市场报价利率 |
| IRR | Internal Rate of Return | 内部收益率 |
| QT | Quotation Tool | 报价工具 |
| SIT | System Integration Testing | 系统集成测试 |

> 完整术语表详见文档 09，第 9.2 节

---

## 分类九：AI 辅助测试工作流

**Q28: 如何用 AI 从需求文档生成测试用例？**

A: 三步走：
1. **输入**：将需求文档/PRD/用户故事提供给 AI
2. **AI 处理**：按正常流程、边界条件、异常场景三个维度自动拆解
3. **输出**：结构化测试用例表（编号、模块、类型、描述、前置条件、步骤、预期结果、优先级）

注意：AI 生成的用例**必须人工审核**，特别是涉及本地化、特定业务规则、历史遗留逻辑的场景。
> 提示词模板详见文档 11 模板集

---

**Q29: 如何逐步沉淀提升 AI 辅助的效果？**

A: 按阶段推进：
- **短期（1-2 周）**：拿一个功能试跑，对比 AI 生成 vs 自己编写的用例，记录 AI 遗漏的点
- **中期（1-2 月）**：将优化后的提示词 + 补充规则沉淀为 SIT SOP 文档
- **长期（3-6 月）**：用缺陷数据生成质量分析报告，推动乙方建立自检流程

> 详见场景文档第 8 节

---

## 更新记录

| 日期 | 变更人 | 变更内容 | 变更原因 |
|------|--------|---------|---------|
| 2026-03-29 | PM (IT) | 初始版本：从知识库 01-09 及场景文档提取高频问题 | 补充知识库 FAQ 类文档 |
| | | | _新问题在此添加记录_ |
