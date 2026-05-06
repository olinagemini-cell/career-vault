# 02 — Business Rules & Conditional Logic

> **Audience**: 甲乙双方 (Both Client PM/BA and Vendor Team)  
> **Maintainer**: **甲方主导更新** — Business rules are owned by 甲方. When rules change (new product, new tax rate, new market), 甲方 updates this document and notifies 乙方.  
> **Update Frequency**: Per Release or when business rules change  
> **Related Docs**: 01 (Product Types), 05 (Odessa Field Mapping)

---

## 2.1 China Mainland vs Hong Kong Differences

These differences affect system configuration, field defaults, and validation rules across all three systems. **Any new market expansion will require a similar comparison table.**

| Attribute | China Mainland | Hong Kong |
|---|---|---|
| Currency | CNY | HKD |
| Legal Entity | BPCE Equipment Solutions China Co Ltd | BPCE Equipment Solutions Hong Kong |
| Odessa Country Code | China | HKG |
| Remit To (Lease Billing) | BPCE-CNY | BPCE-HKD |
| VAT on Rental | Yes (typically 13%) | No |
| Tax Code | CHINA_VAT / Tax type = VAT | N/A |
| Available Product Types | Finance Lease China, AOR CHINA | HKG Financial Lease (DL, SLB) |
| Available Campaigns | Direct Lease, SLB, AOR | Direct Lease, SLB |
| ZhongDeng Registration | Required (default status = Pending) | Required (default status = Pending) |
| Cost of Fund (reference range) | 2.95 – 3.10 | 0 (in sample data) |
| Funding Source | EIB | N/A (blank in sample data) |

**甲方 action required**: When expanding to a new market or when regulatory changes occur (e.g., VAT rate change from 13% to a different rate), update this table and notify 乙方 to adjust validations.

---

## 2.2 System Default Values

These values are auto-populated or fixed across all contract types. If any of these are wrong in Odessa, it indicates a **configuration defect** (system setup issue), not a data entry error.

| Field | Default Value | Module | Condition | Impact if Wrong |
|---|---|---|---|---|
| ZhongDeng Status | Pending | Lease & Loan | Always | Regulatory compliance risk |
| Day Count Convention | 30/360 | Lease & Loan | Always | Interest calculation error |
| Serviced | Yes | Lease & Loan | Always (Indirect Servicing) | Servicing workflow broken |
| Collected | Yes | Lease & Loan | Always (Indirect Servicing) | Collection workflow broken |
| Active | Yes | Lease & Loan | Always (Indirect Servicing) | Contract not active |
| Netoff with Payable Invoice | True | Lease | Always | Payment netting fails |
| Over Term (Maturity Mgmt) | False | Lease | Always (China) | Incorrect maturity handling |
| Customer VAT Type | Special | Customer | Always | Tax calculation error |
| Deliver via Email | Yes | Customer | Always | Invoice delivery fails |
| # of Inception Payments | 1 | Lease & Loan | When Repayment = **Advance** | First payment amount wrong |
| # of Inception Payments | 0 | Lease & Loan | When Repayment = **Arrears** | First payment amount wrong |
| Float Rate Index | LPR | Lease | When Rate Type = **Floating** | Interest reset fails |
| Float Rate Reset Unit | 12 months | Lease | When Float Rate Index = LPR | Reset frequency wrong |
| Move Across Month | Default value | Lease | Always | Interest calculation edge case |

**甲方 action required**: When system configuration changes (e.g., new default values for a new product line, or a change in default Float Rate Index), update this table before 乙方 begins regression testing.

---

## 2.3 Key Calculation Formulas

These formulas are used to validate calculated values in Odessa. If a calculated field is wrong, the defect is in the calculation logic, not the input data.

| Calculated Field | Formula | Validated At |
|---|---|---|
| Financed Amount | = Net Asset Amount − Down Payment | Origination (🔒 Non-Editable) |
| Total Down Payment | = Down Payment × (1 + VAT Rate) | Odessa Structure tab |
| Down Payment (excl. tax) | = Down Payment % × Net Asset Amount | QT / Origination |
| Inception Payment | = First Installment ÷ (1 + VAT Rate) | Odessa Structure tab |
| Maturity Date | = Commencement Date + (Payment Frequency × Term) | Odessa Structure tab |
| Interest Rate (Fixed) | = Cost of Funds + Margin | Odessa Interest Rate tab |
| Interest Rate (Floating) | = Base Rate (LPR) + Spread | Odessa Interest Rate tab |

**Usage**: When validating Odessa Structure or Interest Rate tabs, use these formulas to independently calculate the expected value, then compare against the system-displayed value.

**甲方 action required**: If business introduces new fee types or changes VAT calculation logic (e.g., VAT-inclusive vs VAT-exclusive pricing), update the formulas here and in Doc 05.

---

## 2.4 Rate Type Conditional Logic

Rate Type (Fixed vs Floating) is selected in QT and creates two completely different validation paths in Odessa. This is one of the most error-prone areas:

| Odessa Field | Rate Type = Fixed | Rate Type = Floating |
|---|---|---|
| Float Rate Lease | No (unchecked) | Yes (checked) |
| Restructure On Float Rate Change | No | Yes |
| Float Rate Index | N/A (empty/disabled) | LPR |
| Base Rate % | N/A | = Cost of Funds from QT |
| Spread % | N/A | = Margin from QT |
| Interest Rate % | = Cost of Funds + Margin | = Base Rate + Spread |
| Float Rate Reset Unit | N/A | 12 months |
| First Reset Date | N/A | 12 months from commencement |

**Testing tip**: Always run at least one Fixed and one Floating test case per contract type. The most common integration defect is Floating fields being populated when Rate Type = Fixed (or vice versa).

---

## 2.5 Repayment Type Impact

| Odessa Field | Repayment = Advance (In Advance) | Repayment = Arrears (In Arrear) |
|---|---|---|
| Advance (Structure tab) | Yes | No |
| # of Inception Payments | 1 | 0 |
| Residual Value in Last Installment | Yes (if configured in QT) | N/A |

---

## 2.6 Remit To Conditional Logic

| Entity | Remit To Value |
|---|---|
| BPCE Equipment Solutions **China** Co Ltd | BPCE-CNY |
| BPCE Equipment Solutions **Hong Kong** | BPCE-HKD |

This applies to both Lease Billing > Remit To and Loan Billing > Remit To.

---

## Change Log for This Document

| Date | Changed By | What Changed | Reason |
|------|-----------|-------------|--------|
| March 2026 | PM (IT) | Initial version | KB creation |
| | | | _Add entries here when rules change_ |
