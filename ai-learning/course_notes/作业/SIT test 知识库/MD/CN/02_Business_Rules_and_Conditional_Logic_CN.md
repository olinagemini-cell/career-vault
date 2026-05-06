# 02 — 业务规则与条件逻辑

> **目标读者**: 甲乙双方 (Both Client PM/BA and Vendor Team)
> **维护方**: **甲方主导更新** — 业务规则由甲方拥有。当规则变更时（新产品、新税率、新市场），甲方更新本文档并通知乙方。
> **更新频率**: 每次发版或业务规则变更时
> **相关文档**: 01（产品类型）、05（Odessa 字段映射）

---

## 2.1 中国大陆与香港的差异

这些差异影响三个系统的系统配置、字段默认值和校验规则。**任何新市场扩展都需要建立类似的对比表。**

| 属性 | 中国大陆 | 香港 |
|---|---|---|
| 币种 | CNY | HKD |
| 法律实体 | BPCE Equipment Solutions China Co Ltd | BPCE Equipment Solutions Hong Kong |
| Odessa 国家代码 | China | HKG |
| 收款方（租赁账单） | BPCE-CNY | BPCE-HKD |
| 租金 VAT | 是（通常 13%） | 否 |
| 税码 | CHINA_VAT / Tax type = VAT | 不适用 |
| 可用产品类型 | Finance Lease China, AOR CHINA | HKG Financial Lease (DL, SLB) |
| 可用活动 | Direct Lease, SLB, AOR | Direct Lease, SLB |
| 中登登记 | 必须（默认状态 = Pending） | 必须（默认状态 = Pending） |
| 资金成本（参考范围） | 2.95 – 3.10 | 0（样本数据中） |
| 资金来源 | EIB | 不适用（样本数据中为空） |

**甲方需执行的操作**: 当扩展至新市场或发生监管变更时（例如 VAT 税率从 13% 变更为其他税率），请更新此表并通知乙方调整校验逻辑。

---

## 2.2 系统默认值

以下值在所有合同类型中均为自动填充或固定值。如果 Odessa 中这些值有误，则表明是**配置缺陷**（系统设置问题），而非数据录入错误。

| 字段 | 默认值 | 模块 | 条件 | 若有误的影响 |
|---|---|---|---|---|
| ZhongDeng Status | Pending | 租赁 & 贷款 | 始终 | 监管合规风险 |
| Day Count Convention | 30/360 | 租赁 & 贷款 | 始终 | 利息计算错误 |
| Serviced | Yes | 租赁 & 贷款 | 始终（间接服务） | 服务工作流中断 |
| Collected | Yes | 租赁 & 贷款 | 始终（间接服务） | 催收工作流中断 |
| Active | Yes | 租赁 & 贷款 | 始终（间接服务） | 合同未激活 |
| Netoff with Payable Invoice | True | 租赁 | 始终 | 付款净额结算失败 |
| Over Term (Maturity Mgmt) | False | 租赁 | 始终（中国） | 到期处理不正确 |
| Customer VAT Type | Special | 客户 | 始终 | 税务计算错误 |
| Deliver via Email | Yes | 客户 | 始终 | 发票投递失败 |
| # of Inception Payments | 1 | 租赁 & 贷款 | 当还款方式 = **Advance** 时 | 首期付款金额错误 |
| # of Inception Payments | 0 | 租赁 & 贷款 | 当还款方式 = **Arrears** 时 | 首期付款金额错误 |
| Float Rate Index | LPR | 租赁 | 当利率类型 = **浮动** 时 | 利率重置失败 |
| Float Rate Reset Unit | 12 months | 租赁 | 当 Float Rate Index = LPR 时 | 重置频率错误 |
| Move Across Month | 默认值 | 租赁 | 始终 | 利息计算边界情况 |

**甲方需执行的操作**: 当系统配置变更时（例如新产品线的新默认值，或默认 Float Rate Index 变更），请在乙方开始回归测试前更新此表。

---

## 2.3 关键计算公式

以下公式用于校验 Odessa 中的计算值。如果某个计算字段有误，缺陷在于计算逻辑，而非输入数据。

| 计算字段 | 公式 | 校验位置 |
|---|---|---|
| Financed Amount（融资金额） | = Net Asset Amount − Down Payment | Origination（不可编辑） |
| Total Down Payment（首付总额） | = Down Payment × (1 + VAT Rate) | Odessa Structure 标签页 |
| Down Payment（不含税首付） | = Down Payment % × Net Asset Amount | QT / Origination |
| Inception Payment（起始付款） | = First Installment ÷ (1 + VAT Rate) | Odessa Structure 标签页 |
| Maturity Date（到期日） | = Commencement Date + (Payment Frequency × Term) | Odessa Structure 标签页 |
| Interest Rate（固定利率） | = Cost of Funds + Margin | Odessa Interest Rate 标签页 |
| Interest Rate（浮动利率） | = Base Rate (LPR) + Spread | Odessa Interest Rate 标签页 |

**使用方法**: 在校验 Odessa 的 Structure 或 Interest Rate 标签页时，使用这些公式独立计算预期值，然后与系统显示值进行比对。

**甲方需执行的操作**: 如果业务引入新的费用类型或变更 VAT 计算逻辑（例如含税定价 vs 不含税定价），请在此处及文档 05 中更新公式。

---

## 2.4 利率类型条件逻辑

利率类型（固定 vs 浮动）在 QT 中选择，会在 Odessa 中产生两条完全不同的校验路径。这是最容易出错的领域之一：

| Odessa 字段 | Rate Type = Fixed（固定） | Rate Type = Floating（浮动） |
|---|---|---|
| Float Rate Lease | No（未勾选） | Yes（已勾选） |
| Restructure On Float Rate Change | No | Yes |
| Float Rate Index | 不适用（空/禁用） | LPR |
| Base Rate % | 不适用 | = QT 中的 Cost of Funds |
| Spread % | 不适用 | = QT 中的 Margin |
| Interest Rate % | = Cost of Funds + Margin | = Base Rate + Spread |
| Float Rate Reset Unit | 不适用 | 12 months |
| First Reset Date | 不适用 | 起始日起 12 个月 |

**测试提示**: 每种合同类型至少各运行一个固定利率和一个浮动利率的测试用例。最常见的集成缺陷是：当 Rate Type = Fixed 时浮动相关字段被填充（或反之亦然）。

---

## 2.5 还款方式影响

| Odessa 字段 | Repayment = Advance（先付） | Repayment = Arrears（后付） |
|---|---|---|
| Advance (Structure 标签页) | Yes | No |
| # of Inception Payments | 1 | 0 |
| Residual Value in Last Installment | Yes（如在 QT 中配置） | 不适用 |

---

## 2.6 收款方条件逻辑

| 实体 | Remit To 值 |
|---|---|
| BPCE Equipment Solutions **China** Co Ltd | BPCE-CNY |
| BPCE Equipment Solutions **Hong Kong** | BPCE-HKD |

此规则适用于 Lease Billing > Remit To 和 Loan Billing > Remit To。

---

## 本文档变更日志

| 日期 | 变更人 | 变更内容 | 变更原因 |
|------|-----------|-------------|--------|
| 2026年3月 | PM (IT) | 初始版本 | 知识库创建 |
| | | | _规则变更时在此添加记录_ |
