# 04 — 字段映射：QT → Origination

> **目标读者**：乙方 Development & Testing Team
> **维护人**：甲方 PM
> **更新频率**：每次发布时更新（当系统字段发生变更时）
> **关联文档**：05（Origination → Odessa）、01（产品类型）

---

## 如何使用本文档

在开发或测试 QT → Origination 集成时，可查阅以下字段以了解：
- 该字段对应 QT 中的哪个源字段
- 该字段在 Origination 中是否可编辑或锁定
- 任何特殊说明或条件

**图例说明**：🔒 = 不可编辑（从 QT 锁定，无法在 Origination 中修改） | ✏️ = 在 Origination 中可编辑

---

## 交易概览

| Origination 字段 | QT 源字段 | 可编辑性 | 说明 |
|---|---|---|---|
| Deal Phase | — | 🔒 | 由系统自动设置 |
| Financial Product | Financial Product | 🔒 | 从 QT 锁定 |
| Campaign | Campaign | 🔒 | Direct Lease / SLB / AOR。参见文档 01 第 1.3 节 |
| Entity | Entity | 🔒 | 法律实体。参见文档 02 第 2.1 节了解中国与香港的区别 |
| Deal ID | Opportunity ID | 🔒 | 系统生成，映射至 QT 的 Opportunity ID |

---

## 资产详情

| Origination 字段 | QT 源字段 | 可编辑性 | 说明 |
|---|---|---|---|
| Asset Model Picker | Asset Model | ✏️ | QT 提交后可修改 |
| AMT References | — | 🔒 | 系统生成，不来自 QT |
| Supplier Name | Supplier Name | ✏️ | |
| Condition | — | ✏️ | |
| Quantity | Asset Quantity | ✏️ | |
| Currency | Currency | ✏️ | 中国为 CNY，香港为 HKD |
| Unit Price | Unit Asset Price | ✏️ | |
| Attachment Price | Attachment Price | ✏️ | |
| Residual Value | Residual Value | ✏️ | |
| BPCE ES Residual Value | — | ✏️ | BPCE 内部残值 |
| VAT Amount | VAT on Rental % | ✏️ | 来自 QT 的增值税百分比 |
| Supplier VAT Code | — | ✏️ | |
| Is VAT Financed? | — | ✏️ | |
| Downpayment | Down Payment | ✏️ | |

---

## 发票

所有发票字段均为 **✏️ 可编辑**，大部分在 Origination 中手动输入（不从 QT 自动填充）：

| Origination 字段 | QT 源字段 | 说明 |
|---|---|---|
| TP Ref Picker (Supplier) | Supplier Name | 关联 QT 中的供应商 |
| Invoice Number | — | 在 Origination 中手动输入 |
| Issue Date | — | 手动输入 |
| Delivery Date | — | 手动输入 |
| Payment Due Date | — | 手动输入 |
| Payee | Supplier Name | |
| Payee Payment Method | — | |
| Payee Self Billing | — | |
| Bank Account | — | |
| Asset Card - AMT Reference | — | |

**地址信息部分**：✏️ 可编辑。资产位置信息在 Origination 中录入。

---

## 交易结构

| Origination 字段 | QT 源字段 | 可编辑性 | 说明 |
|---|---|---|---|
| Net Amount | Net Purchase Price | 🔒 | 计算得出：Unit Price × Quantity |
| Downpayment | Down Payment | ✏️ | |
| Financed Amount | Financed Amount | 🔒 | 计算得出：Net Amount − Downpayment |
| Payer | Customer Name | ✏️ | 通常 = 客户 |
| Payer Payment Method | — | ✏️ | |
| Payer Self Billing | — | ✏️ | |
| # of Payments or Installments | # of Installments | 🔒 | 来自 QT 计算结果 |
| Periodicity | Installment Frequency | ✏️ | 按月 |
| Grace Period | — | ✏️ | |
| Term | Tenor | ✏️ | 以月为单位（24、36、48） |
| First Installment Date | First Installment Date | ✏️ | |
| In Advance / In Arrear | Repayment Type | ✏️ | 先付或后付 |
| Installments VAT Code | — | ✏️ | 中国为 CHINA_VAT |
| Seasonal Payment Type | Seasonal Payment Type | 🔒 | 如在 QT 中已配置 |
| Installments with Tax | Inception Payment? | ✏️ | |
| RV / Balloon Payment | Residual Value | ✏️ | |
| RV / Balloon Payment VAT Code | — | ✏️ | |
| RV / Balloon Payment Method | — | ✏️ | |
| Banking Entity | Entity | ✏️ | |
| Rate Type | Rate Type | ✏️ | 固定或浮动 |
| Cost of Funds | Cost of Fund | ✏️ | 利率计算的基准利率 |
| Margin | Margin | ✏️ | 高于 COF 的利差 |
| IRR | IRR | 🔒 | 在 QT 中计算 |
| Interest Rate (without taxes) | External Interest Rate | ✏️ | |
| Interest Rate (with taxes) | External Interest Rate | ✏️ | |
| Interest VAT Code | — | ✏️ | |
| Disbursement Date | Disbursement Date | ✏️ | |

**附加参数**：Global Sector Code（✏️ 可编辑，不来自 QT）。
**增值税部分**：✏️ 可编辑，增值税配置。

---

## 担保

所有字段 ✏️ 可编辑，在 Origination 中配置（不来自 QT）：

| Origination 字段 | 说明 |
|---|---|
| Guarantee Type | PG / CG / Vendor First Loss |
| Guarantor Name / TP Ref Picker | 搜索并选择担保人 |
| Guarantee Amount | 担保金额 |

---

## 第三方

所有字段 ✏️ 可编辑：

| 部分 | 描述 |
|---|---|
| Client | 客户详情，来源于 QT 的 Customer Name |
| Suppliers | 供应商详情，来源于 QT 的 Supplier Name |
| Vendor | 经销商/供应商详情，来源于 QT 的 Dealer Name |
| Guarantor | 如已配置担保 |

---

## 审批与合规

所有字段 ✏️ 可编辑：

| 部分 | 字段 |
|---|---|
| Exposure | Date of Last Approval、Approved By |
| Credit Approval | Conflict of Interest、Approval/Rejection |
| CRO Approval | Conflict of Interest、Approval/Rejection |
| Credit Committee | Conflict of Interest、Approval/Rejection |
| LOD1 | Conflict of Interest、Approval/Rejection |
| Checklist | 24 项检查清单 — Validation Status |
| Documents | 6 种文件类型 — 是否上传文件 |

---

## 快速汇总

| 类别 | 字段总数 | 可编辑 | 不可编辑（锁定） |
|---|---|---|---|
| 交易概览 | 5 | 0 | 5 |
| 资产详情 | 14 | 13 | 1 |
| 发票 | 10 | 10 | 0 |
| 交易结构 | 27 | 22 | 5 |
| 担保 | 3 | 3 | 0 |
| 第三方 | 4 | 4 | 0 |
| 审批与合规 | 9 | 9 | 0 |
| **合计** | **72** | **61** | **11** |

11 个不可编辑字段由系统控制或自动计算——如果这些字段的值有误，属于**系统缺陷**，而非用户操作错误。
