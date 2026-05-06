# 06 — 操作手册与执行指南

> **目标读者**: 乙方 Testing Execution Team
> **维护人**: 甲方 PM
> **更新频率**: 每个 Sprint 更新（当操作被自动化或变更时）
> **相关文档**: 04-05（字段映射查询）、02（业务规则）、07（自动化策略）

---

## 如何使用本手册

本文档列出了执行一个完整端到端测试用例所需的每一个离散操作，涵盖从 QT 数据录入到 Odessa 验证的全过程。对于每个操作：
- **输入来源** 告诉你从哪里获取测试数据
- **预期结果** 告诉你需要检查什么
- **分类** 告诉你该操作是自动化的（✅）、混合的（🔶）还是手动的（🔴）

**开始之前**：打开 `China_end_to_end_test.xlsx` 中的 Integration Data 工作表，找到你的测试用例所在行（TC1、TC2 等）。

---

## 阶段 1：Quotation Tool (QT) — 22 个操作

### 数据录入 (A01–A18)

| ID | 操作 | 输入来源（Integration Data 列） | 预期结果 |
|---|---|---|---|
| A01 | 从选择器中选择资产型号 | Asset Model | 资产型号已选择并显示 |
| A02 | 选择产品类型 | Product Type | 产品类型已选择（Finance Lease China / AOR / HKG FL） |
| A03 | 启动报价模拟 | —（按钮点击） | 显示报价模拟界面 |
| A04 | 输入资产单价 | Asset Unit Price | 价格值已输入 |
| A05 | 输入资产数量 | Asset Quantity | 数量已输入 |
| A06 | 按名称搜索供应商 | Supplier Name | 供应商信息已检索并显示 |
| A07 | 选择营销活动 | Campaign | 营销活动已选择（Direct Lease / SLB / AOR） |
| A08 | 按名称搜索客户 | Customer Name | 客户信息已检索 |
| A09 | 输入经销商名称 | Dealer Name | 经销商名称已输入 |
| A10 | 输入首付款百分比 | Downpayment percentage | 百分比已输入 |
| A11 | 输入租期 | Tenor | 租期月数已输入 |
| A12 | 选择分期付款频率 | Installment frequency | 频率已选择（Monthly） |
| A13 | 选择利率类型 | Rate type | 已选择固定或浮动利率 |
| A14 | 输入残值 | Residual value | 值已输入（可能为 0） |
| A15 | 选择还款方式 | Repayment type | 已选择先付或后付 |
| A16 | 切换残值是否包含在最后一期 | RV in last installment | 已选择是或否 |
| A17 | 选择季节性付款（如适用） | Seasonal payment type | 已选择标准或季节性付款 |
| A18 | 输入高级参数（6 个字段） | Commission Fee, Management Fee, Subsidy, Vendor Deposit, Security Deposit, Refund Month | 全部 6 个值已输入 |

**分类**: A01–A18 全部为 ✅ AI 可自动化 — 从测试数据矩阵直接录入数据。

### 计算与提交 (A19–A22)

| ID | 操作 | 详情 | 分类 |
|---|---|---|---|
| A19 | 点击计算 IRR | 按钮点击，等待计算完成 | ✅ AI |
| A20 | 点击计算模拟方案 | 按钮点击，验证选项已显示 | ✅ AI |
| A21 | **验证模拟结果** | 检查：第一个选项已选中，融资金额和分期付款金额已计算。数值应在商业合理范围内 | 🔶 Hybrid — AI 计算预期值，人工确认合理性 |
| A22 | 发送至 SGEF | 点击发送至 SGEF → 填写客户信息对话框 → 确认 | ✅ AI |

**阶段 1 结果**：报价已创建并发送至 SGEF。记录报价编号（例如 QT-CHN-LE-2026-XXXX）供阶段 2 使用。

---

## 阶段 2：Origination — 14 个操作

### 搜索与验证 (B01–B09)

| ID | 操作 | 检查内容 | 预期结果 | 分类 |
|---|---|---|---|---|
| B01 | 导航至 Origination，按报价编号搜索 | — | 交易已找到并显示 | ✅ AI |
| B02 | 验证交易编号 | Odessa Deal ID = QT Opportunity ID | 完全匹配 | ✅ AI |
| B03 | 验证交易阶段 | — | 预期阶段值 | ✅ AI |
| B04 | 验证金融产品、营销活动、实体 | 3 个字段，均为 🔒 不可编辑 | 全部与 QT 值匹配 | ✅ AI |
| B05 | 验证资产型号 | — | 与 QT 资产型号匹配 | ✅ AI |
| B06 | 验证资产数量 | — | 与 QT 数量匹配 | ✅ AI |
| B07 | 验证融资金额 | — | 与 QT 计算的融资金额匹配（容差 ±0.01） | ✅ AI |
| B08 | 验证期限和付款周期 | — | Term = QT Tenor，Periodicity = QT Frequency | ✅ AI |
| B09 | 验证客户、经销商、供应商名称 | CounterParty 部分 | 全部 3 个名称与 QT 输入匹配 | ✅ AI |

### 数据录入与工作流 (B10–B14)

| ID | 操作 | 详情 | 分类 |
|---|---|---|---|
| B10 | 验证敞口 / 新申请金额 | — | 🔶 Hybrid — AI 验证算术计算，人工确认业务上下文 |
| B11 | 输入全球行业代码 | 来自测试数据的值 | ✅ AI |
| B12 | 将交易推进到分析阶段 | 按钮点击 | ✅ AI |
| B13 | **信贷审批工作流** | 多阶段：Credit → CRO → Committee → LOD1 | 🔴 Human Required — 需要授权签字人 |
| B14 | 将交易发送至后台 | 审批通过后按钮点击 | ✅ AI |

**阶段 2 结果**：交易已审批并发送至 Odessa 后台。记录交易编号供阶段 3 使用。

---

## 阶段 3：Odessa 验证 — 23 个操作

### 导航 (C01)

| ID | 操作 | 详情 | 分类 |
|---|---|---|---|
| C01 | 导航至 Odessa，在正确模块中搜索 | Lease 模块（用于 DL/SLB）或 Loan 模块（用于 AOR）。按合同编号搜索 | ✅ AI |

### 基本信息与配置 (C02–C08)

| ID | 操作 | 需检查的字段 | 分类 |
|---|---|---|---|
| C02 | 验证基本信息 | Customer, Sequence#, Legal Entity, Country, Currency（5 个字段） | ✅ AI |
| C03 | 验证交易类型映射 | Campaign → Deal Type（DL/SLB → Finance Lease，AOR → Unsecured Loan） | ✅ AI |
| C04 | 验证交易类型 | 直接来自 Campaign 值 | ✅ AI |
| C05 | 验证中登网状态 | 必须 = Pending | ✅ AI |
| C06 | 验证发起来源类型 | 条件判断：Direct channel → Direct，其他 → Vendor | ✅ AI |
| C07 | 验证间接服务默认值 | Serviced=Yes, Collected=Yes, Active=Yes（3 个字段） | ✅ AI |
| C08 | 验证账单信息 | Bill To = Customer，Remit To = BPCE-CNY 或 BPCE-HKD（根据实体条件判断） | ✅ AI |

### 财务数据 (C09–C16)

| ID | 操作 | 需检查的字段 | 分类 |
|---|---|---|---|
| C09 | 验证资金信息 | Vendor, Invoice Date, Issue Date, Due Date, Payable Remit To, Payable Code, Netoff（7 个字段） | ✅ AI |
| C10 | 验证资产与费用 | Asset Cost, Tax, Tax Code, Payee, Amount, Remit To（6 个字段） | ✅ AI |
| C11 | 验证租赁资产 | Asset Cost, Serial#, Make, Model, Manufacturer（5 个字段） | ✅ AI |
| C12 | 验证结构 | #Payments, Frequency, Day Count, Advance, Inception Payments, Dates, Terms, Down Payments, Float Rate flags（15+ 个字段） | ✅ AI |
| C13 | 验证到期日 | = Commencement + Frequency × Term（日期计算） | ✅ AI |
| C14 | 验证首付款总额 | = Downpayment × (1 + VAT Rate) | ✅ AI |
| C15 | 验证起始付款 | = First Installment ÷ (1 + VAT Rate) | ✅ AI |
| C16 | 验证利率字段 | 9 个字段，根据利率类型（固定 vs 浮动）条件判断。参见文档 02 第 2.4 节 | ✅ AI |

### 复杂验证 (C17–C22)

| ID | 操作 | 详情 | 分类 |
|---|---|---|---|
| C17 | **验证付款计划** | 逐行比对完整计划表：到期日、租金金额、合计金额 | 🔶 Hybrid — AI 进行逐行差异比对（容差 ±0.01），标记不匹配项供人工审核 |
| C18 | 验证税码与税率 | 税务配置值 | ✅ AI |
| C19 | **验证混合项目** | Code, Name, Type, Amount, Booking Mode, Dates, Payable Details, Self Billing | 🔶 Hybrid — AI 验证结构，人工验证记账逻辑 |
| C20 | 验证超期标志 | 必须 = False（中国） | ✅ AI |
| C21 | 验证买断权分配 | Option to Purchase, Late Fee Template, Grace Days（4 个字段） | ✅ AI |
| C22 | **验证第三方关系** | Relationship Type, Limit, %, Amount, Party Name, Company, Guarantee | 🔶 Hybrid — AI 进行模糊名称匹配，人工审核低置信度匹配结果 |

### 交易激活 (C23)

| ID | 操作 | 详情 | 分类 |
|---|---|---|---|
| C23 | **启动交易** | 点击 Accounting → Perform Classification Test → Compute Yield → Commence。如出现警告，决定是否覆盖 | 🔶 Hybrid — AI 执行标准步骤，人工决定警告覆盖 |

**阶段 3 结果**：交易已激活。已收到确认消息。测试用例完成。

---

## 执行后检查清单

完成一个测试用例的全部 3 个阶段后：

- [ ] 在 Deals Automated 工作表中记录结果（Status、Landed in Odessa、Validated）
- [ ] 如有验证失败：使用文档 08 第 8.1 节的决策树对缺陷进行分类
- [ ] 如出现知识库未涵盖的新问题：记录并提交给 PM 添加至常见问题
- [ ] 如测试用例已完全自动化：更新文档 07 的自动化状态

---

## 快速参考：各阶段操作数量

| 阶段 | 操作总数 | ✅ AI | 🔶 Hybrid | 🔴 Human |
|---|---|---|---|---|
| QT | 22 | 20 | 2 | 0 |
| Origination | 14 | 12 | 1 | 1 |
| Odessa | 23 | 16 | 5 | 0 |
| **合计** | **59** | **48** | **8** | **1** |
