# 05 — 字段映射：Origination → Odessa

> **目标读者**：乙方 Development & Testing Team
> **维护人**：甲方 PM
> **更新频率**：每次发布时更新（当系统字段发生变更时）
> **相关文档**：04（QT → Origination）、02（条件逻辑的业务规则）

---

## 如何使用本文档

当交易从 Origination 落入 Odessa 后验证合同数据时，可查阅以下任意字段以了解：
- 期望值的来源（Origination 源路径）
- 验证规则或期望值
- 该字段属于验证（Validate，比对）、自动默认（Auto-default，固定值）、条件（Conditional，基于规则）还是计算（Calculated，公式推导）

**图例**：
- **验证（Validate）** = 将 Odessa 值与 Origination/QT 源进行比对
- **自动默认（Auto-default）** = 系统应自动填充此固定值
- **条件（Conditional）** = 值取决于另一字段（参见规则）
- **计算（Calculated）** = 值由公式推导得出（参见文档 02 第 2.3 节）

---

## Lease 模块（适用于 Direct Lease 及 SLB 活动）

### Primary Details

| Odessa Field | Origination Source | 验证规则 | 类型 |
|---|---|---|---|
| Customer | Client (Third Parties > Summary) | 必须与 QT 中的 Client 名称一致 | 验证（Validate） |
| Sequence # | Deal ID | 必须与 Origination Deal ID 一致；若直接在 Odessa 中创建，默认值 = Customer#-1 | 验证（Validate） |
| Legal Entity | Entity | BPCE Equipment Solutions China Co Ltd | 验证（Validate） |
| Country | — | China（CN 实体）/ HKG（HK 实体） | 条件（Conditional） |
| Currency | Contract Currency | CNY（China）/ HKD（HK）。选择 Line of Business 后自动默认 | 自动默认（Auto-default） |
| Deal Type | Campaign mapping | DL/SLB → Finance Lease。参见文档 01 第 1.3 节 | 验证（Validate） |
| Transaction Type | Campaign mapping | 直接取自 Campaign 的值 | 验证（Validate） |
| ZhongDeng Status | — | 始终 = Pending | 自动默认（Auto-default） |

### Origination Tab

| Odessa Field | Origination Source | 验证规则 | 类型 |
|---|---|---|---|
| Origination Source Type | Acquisition Channel | Direct → "Direct"；IM/Lessor/Bank/等 → "Vendor"。参见文档 01 第 1.4 节 | 条件（Conditional） |
| Origination Source | Vendor/Dealer Name | = QT 中的 Dealer Name（当 Source Type = Vendor 时） | 验证（Validate） |

### Indirect Servicing Details

| Odessa Field | 期望值 | 类型 |
|---|---|---|
| Effective Date | 固定到期日规则 | 自动默认（Auto-default） |
| Serviced | Yes | 自动默认（Auto-default） |
| Collected | Yes | 自动默认（Auto-default） |
| Active | Yes | 自动默认（Auto-default） |

### Lease Billing

| Odessa Field | Origination Source | 验证规则 | 类型 |
|---|---|---|---|
| Bill To | Payer (Instalment Schedule) | 必须与 Origination 中的 Payer 一致 | 验证（Validate） |
| Remit To | — | China 实体 → BPCE-CNY；HK 实体 → BPCE-HKD | 条件（Conditional） |

### Fundings

| Odessa Field | Origination Source Path | 验证规则 | 类型 |
|---|---|---|---|
| Vendor | Asset > Invoices > Payee | 必须与 QT 中的 Dealer 一致 | 验证（Validate） |
| Invoice Date | Asset > Invoices > Issue Date | 必须一致 | 验证（Validate） |
| Invoice Issue Date | Asset > Invoices > Issue Date | 必须一致 | 验证（Validate） |
| Due Date | Asset > Invoices > Payment Due Date | 必须一致 | 验证（Validate） |
| Payable Remit To | Asset > Invoices > Payee | 必须与 Payee Remit To 一致 | 验证（Validate） |
| Asset Cost Payable Code | — | China 配置的默认值 | 自动默认（Auto-default） |
| Netoff with Payable Invoice | — | 始终 = True | 自动默认（Auto-default） |

### Asset and Other Costs

| Odessa Field | Origination Source Path | 验证规则 | 类型 |
|---|---|---|---|
| Asset Cost | Asset > Amount > Net Amount | 必须一致 | 验证（Validate） |
| Tax | Asset > VAT > Amount | 税务矩阵配置 | 验证（Validate） |
| Tax Code | — | 配置的增值税代码（CHINA_VAT） | 自动默认（Auto-default） |
| Payee Name | Asset > Invoices > Payee | 必须与 QT 中的 Supplier 一致 | 验证（Validate） |
| Amount | Asset > Invoices > Total Invoice Amount | 必须与每项资产的发票金额一致 | 验证（Validate） |
| Remit To | Asset > Invoices > Payee | 必须与 Supplier Remit To 一致 | 验证（Validate） |

### Lease Asset

| Odessa Field | Origination Source Path | 验证规则 | 类型 |
|---|---|---|---|
| Asset Cost | Transaction Structure > Asset | 必须与 Net Amount 一致 | 验证（Validate） |
| Serial # | Asset > Invoices > Serial Number | 必须一致 | 验证（Validate） |
| Make | Asset Model Picker > SubSector | 资产型号的前 10 位 | 验证（Validate） |
| Model | Asset Model Picker > Sector | 取自资产型号的字符 | 验证（Validate） |
| Manufacturer | Asset Model Picker > SubSector | 取自资产型号的字符 | 验证（Validate） |

### Structure

| Odessa Field | Origination Source Path | 验证规则 | 类型 |
|---|---|---|---|
| # of Payments | # of Payments/Installments | 必须与 QT 中的 Tenor 一致 | 验证（Validate） |
| Payment Frequency | Periodicity | 必须一致（Monthly） | 验证（Validate） |
| Day Count Convention | — | 默认 30/360 | 自动默认（Auto-default） |
| Advance | In Advance / In Arrear | 必须与 Repayment Type 一致 | 验证（Validate） |
| # of Inception Payments | — | Advance → 1；Arrears → 0 | 条件（Conditional） |
| Commencement Date | — | 必须与交易起始日期一致 | 验证（Validate） |
| Frequency Start Date | — | — | 自动默认（Auto-default） |
| Maturity Date | — | = Commencement + Frequency × Term | 计算（Calculated） |
| Term in Months | Term (Months) | 必须与 QT 中的 Tenor 一致 | 验证（Validate） |
| Customer Term in Months | Term (Months) | 必须与 QT 中的 Tenor 一致 | 验证（Validate） |
| Inception Payment | First Installment | = First Installment ÷ (1 + VAT Rate) | 计算（Calculated） |
| Total Down Payment | Downpayment | = Downpayment × (1 + VAT Rate) | 计算（Calculated） |
| Down Payment | Downpayment | 必须与 QT/Origination 的值一致 | 验证（Validate） |
| Tax Down Payment | Installments VAT Code | 取自 Origination | 验证（Validate） |
| Float Rate Lease | Rate Type | Fixed → No；Floating → Yes | 条件（Conditional） |
| Restructure On Float Rate Change | Rate Type | Fixed → No；Floating → Yes | 条件（Conditional） |

### Lease Interest Rate

| Odessa Field | Origination Source Path | 验证规则 | 类型 |
|---|---|---|---|
| Effective Date | — | 固定到期日规则 | 自动默认（Auto-default） |
| Float Rate | Rate Type | Fixed → No；Floating → Yes | 条件（Conditional） |
| Float Rate Index | — | LPR（当为 Floating 时） | 条件（Conditional） |
| Base Rate % | Cost of Funds | 取自 Origination Transaction Params | 验证（Validate） |
| Spread % | Margin | 取自 Origination Transaction Params | 验证（Validate） |
| Interest Rate % | Interest Rate (w/o tax) | = COF + Margin（Fixed）或 Base + Spread（Floating） | 验证（Validate） |
| Float Rate Reset Unit | — | 12（当为 LPR 时） | 条件（Conditional） |
| First Reset Date | — | 自起始日起 12 个月（当为 LPR 时） | 条件（Conditional） |
| Move Across Month | — | 默认值 | 自动默认（Auto-default） |

### Other Tabs

| Odessa Tab | 关键字段 | 验证规则 | 类型 |
|---|---|---|---|
| Payment Schedule | 完整还款计划（所有行） | 必须与 Origination Instalment Schedule 逐行一致 | 验证（Validate） |
| Tax | Tax Code, Tax Rate | 税务配置 | 自动默认（Auto-default） |
| Blended Items | Code, Name, Type, Amount, Dates, Payable Details, Self Billing | 复杂验证 — 参见文档 07 了解 AI/人工分工 | 验证（Validate） |
| Accounting | Transfer of Ownership | 默认值 | 自动默认（Auto-default） |
| Maturity Management | Over Term | 始终 = False（China） | 自动默认（Auto-default） |
| Payoff Assignment | Option to Purchase Fee, Late Fee Template, Invoice Grace Days, Grace Days at Inception | Payoff 模板值 | 自动默认（Auto-default） |
| Late Fee Setup | 所有值 | Late Fee Template：SLB 专用 | 自动默认（Auto-default） |
| Third Parties | Relationship Type, Limit By, %, Amount, Third Party, Company, Guarantee | 合同相关方关系 | 验证（Validate） |

---

## Loan 模块（适用于 AOR 活动）

Loan 模块与 Lease 模块结构相似，主要区别如下：

### Loan Details（替代 Primary Details）

| Odessa Field | Origination Source | 验证规则 | 类型 |
|---|---|---|---|
| Legal Entity | Entity | BPCE Equipment Solutions China Co Ltd | 验证（Validate） |
| Country | — | China | 验证（Validate） |
| Customer | Client | 必须一致 | 验证（Validate） |
| Sequence # | Deal ID | 必须一致 | 验证（Validate） |
| Multi Party Contract | — | 当 Payer = CSI/Signify 时为 Yes；否则为 No | 条件（Conditional） |
| Currency | Contract Currency | CNY | 验证（Validate） |
| Deal Type | Campaign | Unsecured Loan（适用于 AOR） | 验证（Validate） |
| Transaction Type | Campaign | AOR | 验证（Validate） |
| ZhongDeng Status | — | 始终 = Pending | 自动默认（Auto-default） |

### Loan 专用标签页

| Odessa Tab | 与 Lease 的主要区别 | 验证规则 |
|---|---|---|
| Loan Origination | 与 Lease Origination 标签页逻辑相同 | Source Type：Direct/Vendor |
| Loan Billing | 与 Lease Billing 逻辑相同 | Bill To、Remit To |
| Loan Funding | 替代 Fundings；增加 Collateral Assets、Other Cost、Payable Code | 验证金额、收款方详情 |
| Loan Structure | 使用 Loan Amount（非 Asset Cost），含 Balloon Payment（非 RV） | 验证所有结构字段 |
| Loan Interest Rate | 更简化 — 仅含 Base Rate、Spread、Interest Rate | 可能不含 Float Rate 字段 |
| Collateral Assets | 替代 Lease Asset — Manufacturer、Make、Model、Asset Type | 验证资产详情 |

### Loan Structure Fields

| Odessa Field | Source | 类型 |
|---|---|---|
| Loan Amount | Financed Amount | 验证（Validate） |
| Down Payment | Downpayment | 验证（Validate） |
| Tax Down Payment | — | 验证（Validate） |
| Commencement Date | Deal start date | 验证（Validate） |
| Payment Frequency | Periodicity | 验证（Validate） |
| Number of Payments | Tenor | 验证（Validate） |
| Maturity Date | Calculated | 计算（Calculated） |
| Advance | Repayment Type | 验证（Validate） |
| # of Inception Payments | —（1 或 0） | 条件（Conditional） |
| Balloon Payment | Residual Value | 验证（Validate） |
| Day Count Convention | —（30/360） | 自动默认（Auto-default） |

---

## Customer 模块

Odessa 中的客户主数据由 Origination Third Party (TP) 参考数据填充：

| Odessa Field | Origination Source Path | 类型 |
|---|---|---|
| Party # | —（SGEFTP ID） | 自动默认（Auto-default） |
| Status | — | 验证（Validate）（Active/Inactive） |
| Company Legal Name | TP Ref > Name Details > Local Long Name | 验证（Validate） |
| Registration ID | TP Ref > Registrations > Type 00715 > Code | 验证（Validate） |
| Customer VAT Type | — | 自动默认（Auto-default）（Special） |
| Doing Business As Name | TP Ref > English Name | 验证（Validate） |
| Address Line 1 (Office) | TP Ref > Legal Address > Local > Address Line | 验证（Validate） |
| City (Office) | TP Ref > Legal Address > Local > City | 验证（Validate） |
| State/Province (Office) | TP Ref > Legal Address > Local > Province | 验证（Validate） |
| Address Line 1 (Home) | TP Ref > Additional Address > Address Line | 验证（Validate） |
| City (Home) | TP Ref > Additional Address > City | 验证（Validate） |
| State/Province (Home) | TP Ref > Additional Address > Province | 验证（Validate） |
| Deliver via Email | — | 自动默认（Auto-default）（Yes） |
| Email To | Client > Basic Information > Email | 验证（Validate） |

---

## 字段数量汇总

| 模块 | 字段总数 | 验证（Validate） | 自动默认（Auto-default） | 条件（Conditional） | 计算（Calculated） |
|---|---|---|---|---|---|
| Lease | ~95 | ~55 | ~25 | ~12 | ~3 |
| Loan | ~45 | ~25 | ~12 | ~5 | ~1 |
| Customer | 14 | 9 | 3 | 0 | 0 |
| **合计** | **~154** | **~89** | **~40** | **~17** | **~4** |
