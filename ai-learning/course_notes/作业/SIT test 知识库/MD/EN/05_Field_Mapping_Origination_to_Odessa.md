# 05 — Field Mapping: Origination → Odessa

> **Audience**: 乙方 Development & Testing Team  
> **Maintainer**: 甲方 PM  
> **Update Frequency**: Per Release (when system fields change)  
> **Related Docs**: 04 (QT → Origination), 02 (Business Rules for conditional logic)

---

## How to Use This Document

When validating Odessa contract data after a deal lands from Origination, look up any field below to find:
- Where the expected value comes from (Origination source path)
- The validation rule or expected value
- Whether the field is a validate (compare), auto-default (fixed), conditional (rule-based), or calculated (formula)

**Legend**:
- **Validate** = Compare Odessa value against Origination/QT source
- **Auto-default** = System should auto-populate this fixed value
- **Conditional** = Value depends on another field (see rule)
- **Calculated** = Value derived from formula (see Doc 02 Section 2.3)

---

## Lease Module (for Direct Lease & SLB campaigns)

### Primary Details

| Odessa Field | Origination Source | Validation Rule | Type |
|---|---|---|---|
| Customer | Client (Third Parties > Summary) | Must match Client name from QT | Validate |
| Sequence # | Deal ID | Must match Origination Deal ID; if created directly in Odessa, default = Customer#-1 | Validate |
| Legal Entity | Entity | BPCE Equipment Solutions China Co Ltd | Validate |
| Country | — | China (CN entity) / HKG (HK entity) | Conditional |
| Currency | Contract Currency | CNY (China) / HKD (HK). Auto-defaulted after selecting Line of Business | Auto-default |
| Deal Type | Campaign mapping | DL/SLB → Finance Lease. See Doc 01 Section 1.3 | Validate |
| Transaction Type | Campaign mapping | Direct value from Campaign | Validate |
| ZhongDeng Status | — | Always = Pending | Auto-default |

### Origination Tab

| Odessa Field | Origination Source | Validation Rule | Type |
|---|---|---|---|
| Origination Source Type | Acquisition Channel | Direct → "Direct"; IM/Lessor/Bank/etc. → "Vendor". See Doc 01 Section 1.4 | Conditional |
| Origination Source | Vendor/Dealer Name | = Dealer Name from QT (when Source Type = Vendor) | Validate |

### Indirect Servicing Details

| Odessa Field | Expected Value | Type |
|---|---|---|
| Effective Date | Fix due date rule | Auto-default |
| Serviced | Yes | Auto-default |
| Collected | Yes | Auto-default |
| Active | Yes | Auto-default |

### Lease Billing

| Odessa Field | Origination Source | Validation Rule | Type |
|---|---|---|---|
| Bill To | Payer (Instalment Schedule) | Must match Payer from Origination | Validate |
| Remit To | — | China entity → BPCE-CNY; HK entity → BPCE-HKD | Conditional |

### Fundings

| Odessa Field | Origination Source Path | Validation Rule | Type |
|---|---|---|---|
| Vendor | Asset > Invoices > Payee | Must match Dealer from QT | Validate |
| Invoice Date | Asset > Invoices > Issue Date | Must match | Validate |
| Invoice Issue Date | Asset > Invoices > Issue Date | Must match | Validate |
| Due Date | Asset > Invoices > Payment Due Date | Must match | Validate |
| Payable Remit To | Asset > Invoices > Payee | Must match Payee Remit To | Validate |
| Asset Cost Payable Code | — | Configured default for China | Auto-default |
| Netoff with Payable Invoice | — | Always = True | Auto-default |

### Asset and Other Costs

| Odessa Field | Origination Source Path | Validation Rule | Type |
|---|---|---|---|
| Asset Cost | Asset > Amount > Net Amount | Must match | Validate |
| Tax | Asset > VAT > Amount | Tax matrix configuration | Validate |
| Tax Code | — | Configured VAT code (CHINA_VAT) | Auto-default |
| Payee Name | Asset > Invoices > Payee | Must match Supplier from QT | Validate |
| Amount | Asset > Invoices > Total Invoice Amount | Must match Invoice amount per asset | Validate |
| Remit To | Asset > Invoices > Payee | Must match Supplier Remit To | Validate |

### Lease Asset

| Odessa Field | Origination Source Path | Validation Rule | Type |
|---|---|---|---|
| Asset Cost | Transaction Structure > Asset | Must match Net Amount | Validate |
| Serial # | Asset > Invoices > Serial Number | Must match | Validate |
| Make | Asset Model Picker > SubSector | First 10 digits of asset model | Validate |
| Model | Asset Model Picker > Sector | Characters from asset model | Validate |
| Manufacturer | Asset Model Picker > SubSector | Characters from asset model | Validate |

### Structure

| Odessa Field | Origination Source Path | Validation Rule | Type |
|---|---|---|---|
| # of Payments | # of Payments/Installments | Must match Tenor from QT | Validate |
| Payment Frequency | Periodicity | Must match (Monthly) | Validate |
| Day Count Convention | — | 30/360 by default | Auto-default |
| Advance | In Advance / In Arrear | Must match Repayment Type | Validate |
| # of Inception Payments | — | Advance → 1; Arrears → 0 | Conditional |
| Commencement Date | — | Must match deal start date | Validate |
| Frequency Start Date | — | — | Auto-default |
| Maturity Date | — | = Commencement + Frequency × Term | Calculated |
| Term in Months | Term (Months) | Must match Tenor from QT | Validate |
| Customer Term in Months | Term (Months) | Must match Tenor from QT | Validate |
| Inception Payment | First Installment | = First Installment ÷ (1 + VAT Rate) | Calculated |
| Total Down Payment | Downpayment | = Downpayment × (1 + VAT Rate) | Calculated |
| Down Payment | Downpayment | Must match QT/Origination value | Validate |
| Tax Down Payment | Installments VAT Code | From Origination | Validate |
| Float Rate Lease | Rate Type | Fixed → No; Floating → Yes | Conditional |
| Restructure On Float Rate Change | Rate Type | Fixed → No; Floating → Yes | Conditional |

### Lease Interest Rate

| Odessa Field | Origination Source Path | Validation Rule | Type |
|---|---|---|---|
| Effective Date | — | Fix due date rule | Auto-default |
| Float Rate | Rate Type | Fixed → No; Floating → Yes | Conditional |
| Float Rate Index | — | LPR (when Floating) | Conditional |
| Base Rate % | Cost of Funds | From Origination Transaction Params | Validate |
| Spread % | Margin | From Origination Transaction Params | Validate |
| Interest Rate % | Interest Rate (w/o tax) | = COF + Margin (Fixed) or Base + Spread (Floating) | Validate |
| Float Rate Reset Unit | — | 12 (when LPR) | Conditional |
| First Reset Date | — | 12 months from commencement (when LPR) | Conditional |
| Move Across Month | — | Default value | Auto-default |

### Other Tabs

| Odessa Tab | Key Fields | Validation Rule | Type |
|---|---|---|---|
| Payment Schedule | Complete schedule (all rows) | Must match Origination Instalment Schedule row by row | Validate |
| Tax | Tax Code, Tax Rate | Tax configuration | Auto-default |
| Blended Items | Code, Name, Type, Amount, Dates, Payable Details, Self Billing | Complex validation — see Doc 07 for AI/Human split | Validate |
| Accounting | Transfer of Ownership | Default value | Auto-default |
| Maturity Management | Over Term | Always = False (China) | Auto-default |
| Payoff Assignment | Option to Purchase Fee, Late Fee Template, Invoice Grace Days, Grace Days at Inception | Payoff template values | Auto-default |
| Late Fee Setup | All values | Late Fee Template: SLB-specific | Auto-default |
| Third Parties | Relationship Type, Limit By, %, Amount, Third Party, Company, Guarantee | Contract party relationships | Validate |

---

## Loan Module (for AOR campaign)

The Loan module mirrors Lease module structure with these key differences:

### Loan Details (replaces Primary Details)

| Odessa Field | Origination Source | Validation Rule | Type |
|---|---|---|---|
| Legal Entity | Entity | BPCE Equipment Solutions China Co Ltd | Validate |
| Country | — | China | Validate |
| Customer | Client | Must match | Validate |
| Sequence # | Deal ID | Must match | Validate |
| Multi Party Contract | — | Yes when Payer = CSI/Signify; No otherwise | Conditional |
| Currency | Contract Currency | CNY | Validate |
| Deal Type | Campaign | Unsecured Loan (for AOR) | Validate |
| Transaction Type | Campaign | AOR | Validate |
| ZhongDeng Status | — | Always = Pending | Auto-default |

### Loan-Specific Tabs

| Odessa Tab | Key Difference from Lease | Validation Rule |
|---|---|---|
| Loan Origination | Same logic as Lease Origination tab | Source Type: Direct/Vendor |
| Loan Billing | Same logic as Lease Billing | Bill To, Remit To |
| Loan Funding | Replaces Fundings; adds Collateral Assets, Other Cost, Payable Code | Validate amounts, payee details |
| Loan Structure | Uses Loan Amount (not Asset Cost), has Balloon Payment (not RV) | Validate all structure fields |
| Loan Interest Rate | Simpler — Base Rate, Spread, Interest Rate only | May not have Float Rate fields |
| Collateral Assets | Replaces Lease Asset — Manufacturer, Make, Model, Asset Type | Validate asset details |

### Loan Structure Fields

| Odessa Field | Source | Type |
|---|---|---|
| Loan Amount | Financed Amount | Validate |
| Down Payment | Downpayment | Validate |
| Tax Down Payment | — | Validate |
| Commencement Date | Deal start date | Validate |
| Payment Frequency | Periodicity | Validate |
| Number of Payments | Tenor | Validate |
| Maturity Date | Calculated | Calculated |
| Advance | Repayment Type | Validate |
| # of Inception Payments | — (1 or 0) | Conditional |
| Balloon Payment | Residual Value | Validate |
| Day Count Convention | — (30/360) | Auto-default |

---

## Customer Module

Customer master data in Odessa is populated from Origination Third Party (TP) reference data:

| Odessa Field | Origination Source Path | Type |
|---|---|---|
| Party # | — (SGEFTP ID) | Auto-default |
| Status | — | Validate (Active/Inactive) |
| Company Legal Name | TP Ref > Name Details > Local Long Name | Validate |
| Registration ID | TP Ref > Registrations > Type 00715 > Code | Validate |
| Customer VAT Type | — | Auto-default (Special) |
| Doing Business As Name | TP Ref > English Name | Validate |
| Address Line 1 (Office) | TP Ref > Legal Address > Local > Address Line | Validate |
| City (Office) | TP Ref > Legal Address > Local > City | Validate |
| State/Province (Office) | TP Ref > Legal Address > Local > Province | Validate |
| Address Line 1 (Home) | TP Ref > Additional Address > Address Line | Validate |
| City (Home) | TP Ref > Additional Address > City | Validate |
| State/Province (Home) | TP Ref > Additional Address > Province | Validate |
| Deliver via Email | — | Auto-default (Yes) |
| Email To | Client > Basic Information > Email | Validate |

---

## Field Count Summary

| Module | Total Fields | Validate | Auto-default | Conditional | Calculated |
|---|---|---|---|---|---|
| Lease | ~95 | ~55 | ~25 | ~12 | ~3 |
| Loan | ~45 | ~25 | ~12 | ~5 | ~1 |
| Customer | 14 | 9 | 3 | 0 | 0 |
| **Total** | **~154** | **~89** | **~40** | **~17** | **~4** |
