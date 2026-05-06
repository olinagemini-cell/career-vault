# 03 — 角色与流程

> **目标读者**: 乙方（特别是新入职团队成员）
> **维护人**: 甲方 PM
> **更新频率**: 极少更新（仅在系统架构变更时更新）
> **相关文档**: 01（产品类型）、06（操作手册）

---

## 3.1 第三方角色

在中国/香港租赁业务中，每笔交易涉及多个第三方角色。理解这些角色至关重要——混淆 Supplier 与 Vendor 是最常见的错误之一：

| 角色 | 定义 | 示例 | 系统流程 |
|---|---|---|---|
| **Client**（客户） | 承租人/借款人，接收资产并进行还款 | DONGGUAN YUE MINGHUA PRINTING PACKAG CO., LTD. | QT: Customer Name → Origination: Third Parties > Client → Odessa: Customer |
| **Supplier**（供应商） | 出售资产的一方 | HEIDELBERG GRAPHICS (BEIJING) COMPANY LIMITED | QT: Supplier Name → Origination: Invoices > Payee → Odessa: Fundings > Vendor |
| **Vendor**（经销商） | 渠道合作伙伴/销售中介，负责引入交易 | HEIDELBERG CHINA CO., LTD. | QT: Dealer Name → Odessa: Origination Source（当 Source Type = Vendor 时） |
| **Guarantor (PG)** | 个人担保人——提供担保的自然人 | 自然人个人 | Origination: Guarantee section → Odessa: Third Parties |
| **Guarantor (CG)** | 企业担保人——提供担保的公司实体 | 公司实体 | Origination: Guarantee section → Odessa: Third Parties |
| **Payer**（付款人） | 支付分期款项的一方 | 通常 = Client | Origination: Transaction Params > Payer → Odessa: Bill To |

**关键区别 — Supplier 与 Vendor（Dealer）**：
- **Supplier** = 资产的原始所有者/出售方。在发票上显示为收款人。
- **Vendor（Dealer）** = 将交易引入 BPCE 的一方。可能与 Supplier 为同一实体，也可能不同。
- 在 **Direct**（直接）交易中：可能没有 Vendor/Dealer；客户直接对接。
- 在 **Vendor Program**（经销商项目）交易中：由 Vendor/Dealer 介绍客户和交易。

**当 Payer ≠ Client 时**：在某些合同中（如 CSI/Signify 安排），分期付款人与承租人为不同实体。此时，Odessa Loan 模块会设置 `Multi Party Contract = Yes`。

---

## 3.2 Odessa 中的 Lease 模块与 Loan 模块

Odessa 使用两个独立模块。模块的选择由 Campaign 类型决定：

| 属性 | Lease 模块 | Loan 模块 |
|---|---|---|
| **适用 Campaign** | Direct Lease、SLB | AOR |
| **Odessa Deal Type** | Finance Lease | Unsecured Loan |
| 是否有 Lease Asset 标签页 | 是 | 否——使用 Collateral Assets |
| Billing 标签页名称 | Lease Billing | Loan Billing |
| Interest Rate 标签页名称 | Lease Interest Rate | Loan Interest Rate |
| 结构细节 | Inception Payment、Float Rate 字段 | Loan Amount、Balloon Payment |
| 到期管理 | 是（中国地区 Over Term = False） | 不适用 |
| Payoff Assignment | 是（Option to Purchase、Late Fee） | 不适用 |
| Fundings 标签页名称 | Fundings | Loan Funding |

**实际影响**：在 Odessa 中搜索合同时，必须先进入正确的模块。在 Lease 模块中搜索 AOR 交易将不会返回任何结果。

---

## 3.3 端到端流程

一笔标准交易按顺序流经三个系统：

```
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│      报价工具        │     │      审批系统         │     │   ODESSA 后台        │
│       (QT)          │────▶│   (ORIGINATION)      │────▶│     办公系统          │
│                     │     │                      │     │                     │
│ • 创建报价          │     │ • 验证交易数据        │     │ • 验证合同           │
│ • 选择资产          │     │ • 配置发票            │     │ • 检查所有字段        │
│ • 设置参数          │     │ • 设置参与方          │     │ • 验证还款计划        │
│ • 计算 IRR          │     │ • 信用审批            │     │ • 启动交易           │
│ • 发送至 SGEF       │     │ • 发送至后台办公系统   │     │                     │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
       22 个操作                  14 个操作                   23 个操作
   (20 AI, 2 Hybrid)        (12 AI, 1 Hybrid,          (16 AI, 5 Hybrid)
                              1 Human)
```

### 阶段 1：报价工具（QT）

| 步骤 | 操作 | 详情 |
|---|---|---|
| 1 | 选择资产型号 | 从选择器中选择（如 CX104-7+L - HEIDELBERG） |
| 2 | 选择产品类型 | Finance Lease China / AOR CHINA / HKG Financial Lease |
| 3 | 输入资产详情 | 单价、数量 |
| 4 | 检索供应商 | 按名称搜索 |
| 5 | 设置交易参数 | Campaign、Customer、Dealer、首付比例、期限、频率、利率类型、残值、还款方式 |
| 6 | 高级参数 | 佣金费用、管理费、补贴、保证金、经销商押金（如适用） |
| 7 | 计算 | IRR 计算 → 模拟 → 选择方案 |
| 8 | 提交 | 连同客户信息发送至 SGEF |

### 阶段 2：Origination（审批系统）

| 步骤 | 操作 | 详情 |
|---|---|---|
| 1 | 搜索与验证 | 按 ID 查找报价，验证 Deal Overview 字段（均为不可编辑） |
| 2 | 验证详情 | 资产、交易结构、交易对手方 |
| 3 | 配置 | 发票、Global Sector Code、地点 |
| 4 | 审批 | Credit → CRO → Credit Committee → LOD1（按需） |
| 5 | 合规 | 完成 24 项检查清单，上传 6 类文件 |
| 6 | 发送 | 将交易发送至后台办公系统 |

### 阶段 3：Odessa 后台办公系统

| 步骤 | 操作 | 详情 |
|---|---|---|
| 1 | 查找合同 | 在正确模块（Lease 或 Loan）中按合同 ID 搜索 |
| 2 | 验证数据 | Primary Details → Origination → Servicing → Billing → Fundings → Assets → Structure → Interest Rate |
| 3 | 验证还款计划 | 与 Origination 进行完整还款计划对比 |
| 4 | 验证其他项 | 税务、Blended Items、到期管理、Payoff、Third Parties |
| 5 | 启动 | Classification Test → Compute Yield → Commence（如需要，覆盖警告） |

**如需包含全部 51 个操作的详细逐步执行指南，请参见文档 06。**
