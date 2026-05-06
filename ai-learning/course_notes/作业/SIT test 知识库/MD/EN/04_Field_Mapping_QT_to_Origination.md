# 04 — Field Mapping: QT → Origination

> **Audience**: 乙方 Development & Testing Team  
> **Maintainer**: 甲方 PM  
> **Update Frequency**: Per Release (when system fields change)  
> **Related Docs**: 05 (Origination → Odessa), 01 (Product Types)

---

## How to Use This Document

When developing or testing the QT → Origination integration, look up any field below to find:
- Which QT field it maps from
- Whether it's editable or locked in Origination
- Any special notes or conditions

**Legend**: 🔒 = Non-Editable (locked from QT, cannot be changed in Origination) | ✏️ = Editable in Origination

---

## Deal Overview

| Origination Field | QT Source Field | Editable | Notes |
|---|---|---|---|
| Deal Phase | — | 🔒 | Auto-set by system |
| Financial Product | Financial Product | 🔒 | Locked from QT |
| Campaign | Campaign | 🔒 | Direct Lease / SLB / AOR. See Doc 01 Section 1.3 |
| Entity | Entity | 🔒 | Legal entity. See Doc 02 Section 2.1 for China vs HK |
| Deal ID | Opportunity ID | 🔒 | System-generated, maps to QT Opportunity ID |

---

## Asset Details

| Origination Field | QT Source Field | Editable | Notes |
|---|---|---|---|
| Asset Model Picker | Asset Model | ✏️ | Can be modified after QT submission |
| AMT References | — | 🔒 | System-generated, not from QT |
| Supplier Name | Supplier Name | ✏️ | |
| Condition | — | ✏️ | |
| Quantity | Asset Quantity | ✏️ | |
| Currency | Currency | ✏️ | CNY for China, HKD for HK |
| Unit Price | Unit Asset Price | ✏️ | |
| Attachment Price | Attachment Price | ✏️ | |
| Residual Value | Residual Value | ✏️ | |
| BPCE ES Residual Value | — | ✏️ | BPCE internal residual value |
| VAT Amount | VAT on Rental % | ✏️ | VAT percentage from QT |
| Supplier VAT Code | — | ✏️ | |
| Is VAT Financed? | — | ✏️ | |
| Downpayment | Down Payment | ✏️ | |

---

## Invoices

All Invoice fields are **✏️ Editable** and mostly entered manually in Origination (not auto-populated from QT):

| Origination Field | QT Source Field | Notes |
|---|---|---|
| TP Ref Picker (Supplier) | Supplier Name | Links to supplier from QT |
| Invoice Number | — | Manual entry in Origination |
| Issue Date | — | Manual entry |
| Delivery Date | — | Manual entry |
| Payment Due Date | — | Manual entry |
| Payee | Supplier Name | |
| Payee Payment Method | — | |
| Payee Self Billing | — | |
| Bank Account | — | |
| Asset Card - AMT Reference | — | |

**Location section**: ✏️ Editable. Asset location information entered in Origination.

---

## Transaction Structure

| Origination Field | QT Source Field | Editable | Notes |
|---|---|---|---|
| Net Amount | Net Purchase Price | 🔒 | Calculated: Unit Price × Quantity |
| Downpayment | Down Payment | ✏️ | |
| Financed Amount | Financed Amount | 🔒 | Calculated: Net Amount − Downpayment |
| Payer | Customer Name | ✏️ | Usually = Client |
| Payer Payment Method | — | ✏️ | |
| Payer Self Billing | — | ✏️ | |
| # of Payments or Installments | # of Installments | 🔒 | From QT calculation |
| Periodicity | Installment Frequency | ✏️ | Monthly |
| Grace Period | — | ✏️ | |
| Term | Tenor | ✏️ | In months (24, 36, 48) |
| First Installment Date | First Installment Date | ✏️ | |
| In Advance / In Arrear | Repayment Type | ✏️ | Advance or Arrears |
| Installments VAT Code | — | ✏️ | CHINA_VAT for China |
| Seasonal Payment Type | Seasonal Payment Type | 🔒 | If configured in QT |
| Installments with Tax | Inception Payment? | ✏️ | |
| RV / Balloon Payment | Residual Value | ✏️ | |
| RV / Balloon Payment VAT Code | — | ✏️ | |
| RV / Balloon Payment Method | — | ✏️ | |
| Banking Entity | Entity | ✏️ | |
| Rate Type | Rate Type | ✏️ | Fixed or Floating |
| Cost of Funds | Cost of Fund | ✏️ | Base rate for interest calculation |
| Margin | Margin | ✏️ | Spread above COF |
| IRR | IRR | 🔒 | Calculated in QT |
| Interest Rate (without taxes) | External Interest Rate | ✏️ | |
| Interest Rate (with taxes) | External Interest Rate | ✏️ | |
| Interest VAT Code | — | ✏️ | |
| Disbursement Date | Disbursement Date | ✏️ | |

**Additional Parameters**: Global Sector Code (✏️ Editable, not from QT).  
**VAT section**: ✏️ Editable, VAT configuration.

---

## Guarantee

All fields ✏️ Editable, configured in Origination (not from QT):

| Origination Field | Notes |
|---|---|
| Guarantee Type | PG / CG / Vendor First Loss |
| Guarantor Name / TP Ref Picker | Search and select guarantor |
| Guarantee Amount | Guarantee value |

---

## Third Parties

All fields ✏️ Editable:

| Section | Description |
|---|---|
| Client | Customer details, sourced from QT Customer Name |
| Suppliers | Supplier details, sourced from QT Supplier Name |
| Vendor | Dealer/Vendor details, sourced from QT Dealer Name |
| Guarantor | If guarantee is configured |

---

## Approval & Compliance

All fields ✏️ Editable:

| Section | Fields |
|---|---|
| Exposure | Date of Last Approval, Approved By |
| Credit Approval | Conflict of Interest, Approval/Rejection |
| CRO Approval | Conflict of Interest, Approval/Rejection |
| Credit Committee | Conflict of Interest, Approval/Rejection |
| LOD1 | Conflict of Interest, Approval/Rejection |
| Checklist | 24 checklist items — Validation Status |
| Documents | 6 document types — File Upload Yes/No |

---

## Quick Summary

| Category | Total Fields | Editable | Non-Editable (Locked) |
|---|---|---|---|
| Deal Overview | 5 | 0 | 5 |
| Asset Details | 14 | 13 | 1 |
| Invoices | 10 | 10 | 0 |
| Transaction Structure | 27 | 22 | 5 |
| Guarantee | 3 | 3 | 0 |
| Third Parties | 4 | 4 | 0 |
| Approval & Compliance | 9 | 9 | 0 |
| **Total** | **72** | **61** | **11** |

11 Non-Editable fields are system-controlled or calculated — if their values are wrong, it's a **system defect**, not a user error.
