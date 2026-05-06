# 01 — 产品与合同类型

> **目标读者**: 乙方 (Vendor Development & Testing Team)
> **维护人**: 甲方 PM
> **更新频率**: 每次发版更新
> **关联文档**: 02 (业务规则), 03 (角色与流程)

---

## 1.1 产品类型

产品类型在报价工具 (QT) 阶段选定。它决定了下游系统模块和验证规则的适用范围。

| 产品类型 | 市场 | Odessa 模块 | 描述 |
|---|---|---|---|
| Finance Lease China | 中国大陆 | Lease | 所有大陆租赁合同：Direct Lease (DL)、Sale-and-Leaseback (SLB)、Optional Residual Value (ORV) |
| AOR CHINA | 中国大陆 | Loan | Asset Operating Rental（资产经营性租赁）。在 Odessa Back Office 中映射为 "Unsecured Loan" |
| HKG Financial Lease (DL, SLB) | 香港 | Lease | 所有香港租赁合同，包括 Direct Lease、SLB 和 Hire Purchase (HP) |

**核心要点**: 产品类型驱动 Odessa 中的模块选择。Finance Lease → Lease 模块。AOR → Loan 模块。如果选错，将导致整套字段的验证规则完全错误。

---

## 1.2 合同类型（测试场景矩阵）

集成数据表中定义了 32 个测试用例。每个测试用例将**销售渠道**与**租赁结构**及可选的**修饰项**进行组合：

### 标准合同类型

| 测试用例编号 | 合同类型 | 市场 | 描述 |
|---|---|---|---|
| TC1 | Vendor Program - Domestic DL | 中国 | 经销商渠道的境内 Direct Lease。资产来自境内经销商（如 TRUMPF China、HEIDELBERG China） |
| TC2 | Vendor Program - Domestic SLB | 中国 | 经销商渠道的 Sale-and-Leaseback。客户将现有资产出售给出租人，再回租 |
| TC3 | Vendor Program - Domestic HP | 香港 | 香港经销商渠道的 Hire Purchase |
| TC4 | Vendor Program - Domestic HP (variant) | 香港 | HP 变体，条款不同 |
| TC5 | Vendor Program - Domestic ORV | 中国 | 带 Optional Residual Value（可选余值）的 Direct Lease，在租赁期末行使 |
| TC6 | Vendor Program - Import DL | 中国 | 资产来自海外供应商的 Direct Lease（进口） |
| TC7 | Vendor Program - Import SLB | 中国 | 资产来自海外的 Sale-and-Leaseback（进口） |
| TC8 | Vendor Program - AOR | 中国 | 经销商渠道的 Asset Operating Rental |
| TC9 | Direct - Domestic DL | 中国 | 直销渠道（无经销商中介）的境内 Direct Lease |
| TC10 | Direct - Domestic SLB | 中国 | 直销渠道的 Sale-and-Leaseback |

### 变体合同类型（在标准类型基础上附加修饰项）

| 合同类型 | 市场 | 关键修饰项 |
|---|---|---|
| DL with Mortgage | 中国 | 附带抵押担保 |
| SLB with Mortgage | 中国 | 附带抵押担保，等额还款结构 |
| DL with Irregular Payment | 中国 | 非标准（季节性）还款计划 |
| SLB with Irregular Payment | 中国 | 非标准还款计划 |
| AOR with Interest | 中国 | AOR 附加利息计算 |
| AOR with Irregular Payment | 中国 | AOR 的非标准还款计划 |
| SLB with PG, CG, Vendor First Loss | 中国 | 个人担保人 + 公司担保人 + 经销商首损担保 |
| DL with Multi-Different Assets | 中国 | 单一合同包含多种不同资产类型 |
| Full-featured DL | 中国 | 全选项：个人担保人、公司担保人、联系信息、多资产、资产所在地、首付款、保证金、经销商佣金、管理费、购买选择权 |

---

## 1.3 Campaign 映射规则

Campaign 在 QT 中设定，在 Origination 中**不可编辑**。它驱动 Odessa 中的两个关键字段：

| QT Campaign | Odessa Deal Type | Odessa Transaction Type | Odessa 模块 |
|---|---|---|---|
| Direct Lease | Finance Lease | Direct Lease | Lease |
| SLB | Finance Lease | SLB | Lease |
| AOR | Unsecured Loan | AOR | Loan |

**常见错误**: 混淆 "Direct Lease"（Campaign / 租赁结构）与 "Direct"（Acquisition Channel / 获客渠道）。它们是不同的概念：
- Campaign "Direct Lease" = 租赁结构为直租（购买资产并出租）
- Acquisition Channel "Direct" = 客户为直接获取（无经销商中介）

一笔交易可以是 Campaign = "Direct Lease" 且 Acquisition Channel = "International Manufacturer" —— 这表示通过经销商渠道发起的直租业务。

---

## 1.4 Acquisition Channel → Origination Source Type 映射

此条件映射是最常见的混淆来源之一：

| QT Acquisition Channel | Odessa Origination Source Type | Origination Source Value |
|---|---|---|
| Direct | **Direct** | 不适用 |
| International Manufacturer (IM) | **Vendor** | = QT 中的 Dealer Name |
| International Lessor | **Vendor** | = QT 中的 Dealer Name |
| National Lessor | **Vendor** | = QT 中的 Dealer Name |
| Local Relationship | **Vendor** | = QT 中的 Dealer Name |
| Bank | **Vendor** | = QT 中的 Dealer Name |
| Syndication | **Vendor** | = QT 中的 Dealer Name |

**简单规则**: 只有 "Direct" → Source Type 为 "Direct"。其余所有渠道 → Source Type 为 "Vendor"，并以 Dealer Name 作为 Source 值。
