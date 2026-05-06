# 06 — Action Playbook & Execution Guide

> **Audience**: 乙方 Testing Execution Team  
> **Maintainer**: 甲方 PM  
> **Update Frequency**: Per Sprint (as actions are automated or changed)  
> **Related Docs**: 04-05 (Field Mapping for lookups), 02 (Business Rules), 07 (Automation Strategy)

---

## How to Use This Playbook

This document lists every discrete action required to execute one complete E2E test case, from QT data entry through Odessa validation. For each action:
- **Input Source** tells you where to get the test data
- **Expected Result** tells you what to check
- **Classification** tells you if it's automated (✅), hybrid (🔶), or manual (🔴)

**Before starting**: Open the Integration Data sheet in `China_end_to_end_test.xlsx` and locate the row for your test case (TC1, TC2, etc.).

---

## Stage 1: Quotation Tool (QT) — 22 Actions

### Data Entry (A01–A18)

| ID | Action | Input Source (Integration Data Column) | Expected Result |
|---|---|---|---|
| A01 | Select Asset Model from picker | Asset Model | Asset model is selected and displayed |
| A02 | Select Product Type | Product Type | Product type is selected (Finance Lease China / AOR / HKG FL) |
| A03 | Start quote simulation | — (button click) | Quote simulation screen is displayed |
| A04 | Enter Asset Unit Price | Asset Unit Price | Price value is entered |
| A05 | Enter Asset Quantity | Asset Quantity | Quantity is entered |
| A06 | Retrieve Supplier by name search | Supplier Name | Supplier details are retrieved and displayed |
| A07 | Select Campaign | Campaign | Campaign is selected (Direct Lease / SLB / AOR) |
| A08 | Retrieve Client by name search | Customer Name | Client details are retrieved |
| A09 | Enter Dealer Name | Dealer Name | Dealer name is entered |
| A10 | Enter Down Payment Percentage | Downpayment percentage | Percentage is entered |
| A11 | Enter Tenor | Tenor | Tenor in months is entered |
| A12 | Select Installment Frequency | Installment frequency | Frequency is selected (Monthly) |
| A13 | Select Rate Type | Rate type | Fixed or Floating is selected |
| A14 | Enter Residual Value | Residual value | Value is entered (may be 0) |
| A15 | Select Repayment Type | Repayment type | Advance or Arrears is selected |
| A16 | Toggle Residual Value in Last Installment | RV in last installment | Yes or No is selected |
| A17 | Select Seasonal Payment (if applicable) | Seasonal payment type | Standard or seasonal payment selected |
| A18 | Enter Advanced Parameters (6 fields) | Commission Fee, Management Fee, Subsidy, Vendor Deposit, Security Deposit, Refund Month | All 6 values entered |

**Classification**: All A01–A18 are ✅ AI Automatable — direct data entry from test data matrix.

### Calculation & Submission (A19–A22)

| ID | Action | Detail | Classification |
|---|---|---|---|
| A19 | Click Calculate IRR | Button click, wait for calculation | ✅ AI |
| A20 | Click Calculate Simulations | Button click, verify options displayed | ✅ AI |
| A21 | **Verify simulation results** | Check: first option selected, Financed Amount and Installment calculated. Values should be commercially reasonable | 🔶 Hybrid — AI calculates expected values, human confirms reasonableness |
| A22 | Send to SGEF | Click Send to SGEF → fill customer info dialog → confirm | ✅ AI |

**Stage 1 result**: Quotation is created and sent to SGEF. Note the Quote ID (e.g., QT-CHN-LE-2026-XXXX) for Stage 2.

---

## Stage 2: Origination — 14 Actions

### Search & Verification (B01–B09)

| ID | Action | What to Check | Expected Result | Classification |
|---|---|---|---|---|
| B01 | Navigate to Origination, search by Quote ID | — | Deal is found and displayed | ✅ AI |
| B02 | Verify Deal ID | Odessa Deal ID = QT Opportunity ID | Exact match | ✅ AI |
| B03 | Verify Deal Phase | — | Expected phase value | ✅ AI |
| B04 | Verify Financial Product, Campaign, Entity | 3 fields, all 🔒 Non-Editable | All match QT values | ✅ AI |
| B05 | Verify Asset Model | — | Matches QT Asset Model | ✅ AI |
| B06 | Verify Asset Quantity | — | Matches QT Quantity | ✅ AI |
| B07 | Verify Financed Amount | — | Matches QT calculated Financed Amount (tolerance ±0.01) | ✅ AI |
| B08 | Verify Term and Periodicity | — | Term = QT Tenor, Periodicity = QT Frequency | ✅ AI |
| B09 | Verify Client, Dealer, Supplier names | CounterParty section | All 3 names match QT inputs | ✅ AI |

### Data Entry & Workflow (B10–B14)

| ID | Action | Detail | Classification |
|---|---|---|---|
| B10 | Verify Exposure / New Request Amount | — | 🔶 Hybrid — AI validates arithmetic, human confirms business context |
| B11 | Enter Global Sector Code | Value from test data | ✅ AI |
| B12 | Progress deal to Analysis phase | Button click | ✅ AI |
| B13 | **Credit approval workflow** | Multi-stage: Credit → CRO → Committee → LOD1 | 🔴 Human Required — needs authorized signatory |
| B14 | Send deal to Back Office | Button click after approval | ✅ AI |

**Stage 2 result**: Deal is approved and sent to Odessa Back Office. Note the Deal ID for Stage 3.

---

## Stage 3: Odessa Validation — 23 Actions

### Navigation (C01)

| ID | Action | Detail | Classification |
|---|---|---|---|
| C01 | Navigate to Odessa, search in correct module | Lease module (for DL/SLB) or Loan module (for AOR). Search by contract ID | ✅ AI |

### Primary Details & Configuration (C02–C08)

| ID | Action | Fields to Check | Classification |
|---|---|---|---|
| C02 | Validate Primary Details | Customer, Sequence#, Legal Entity, Country, Currency (5 fields) | ✅ AI |
| C03 | Validate Deal Type mapping | Campaign → Deal Type (DL/SLB → Finance Lease, AOR → Unsecured Loan) | ✅ AI |
| C04 | Validate Transaction Type | Direct from Campaign value | ✅ AI |
| C05 | Validate ZhongDeng Status | Must = Pending | ✅ AI |
| C06 | Validate Origination Source Type | Conditional: Direct channel → Direct, others → Vendor | ✅ AI |
| C07 | Validate Indirect Servicing defaults | Serviced=Yes, Collected=Yes, Active=Yes (3 fields) | ✅ AI |
| C08 | Validate Billing | Bill To = Customer, Remit To = BPCE-CNY or BPCE-HKD (conditional on entity) | ✅ AI |

### Financial Data (C09–C16)

| ID | Action | Fields to Check | Classification |
|---|---|---|---|
| C09 | Validate Fundings | Vendor, Invoice Date, Issue Date, Due Date, Payable Remit To, Payable Code, Netoff (7 fields) | ✅ AI |
| C10 | Validate Asset & Costs | Asset Cost, Tax, Tax Code, Payee, Amount, Remit To (6 fields) | ✅ AI |
| C11 | Validate Lease Asset | Asset Cost, Serial#, Make, Model, Manufacturer (5 fields) | ✅ AI |
| C12 | Validate Structure | #Payments, Frequency, Day Count, Advance, Inception Payments, Dates, Terms, Down Payments, Float Rate flags (15+ fields) | ✅ AI |
| C13 | Validate Maturity Date | = Commencement + Frequency × Term (date calculation) | ✅ AI |
| C14 | Validate Total Down Payment | = Downpayment × (1 + VAT Rate) | ✅ AI |
| C15 | Validate Inception Payment | = First Installment ÷ (1 + VAT Rate) | ✅ AI |
| C16 | Validate Interest Rate fields | 9 fields, conditional on Rate Type (Fixed vs Floating). See Doc 02 Section 2.4 | ✅ AI |

### Complex Validations (C17–C22)

| ID | Action | Detail | Classification |
|---|---|---|---|
| C17 | **Validate Payment Schedule** | Row-by-row comparison of full schedule: Due Dates, Rental Amounts, Totals | 🔶 Hybrid — AI does row-by-row diff with ±0.01 tolerance, flags mismatches for human review |
| C18 | Validate Tax Code & Rate | Tax configuration values | ✅ AI |
| C19 | **Validate Blended Items** | Code, Name, Type, Amount, Booking Mode, Dates, Payable Details, Self Billing | 🔶 Hybrid — AI validates structure, human validates booking logic |
| C20 | Validate Over Term | Must = False (China) | ✅ AI |
| C21 | Validate Payoff Assignment | Option to Purchase, Late Fee Template, Grace Days (4 fields) | ✅ AI |
| C22 | **Validate Third Party Relationships** | Relationship Type, Limit, %, Amount, Party Name, Company, Guarantee | 🔶 Hybrid — AI does fuzzy name matching, human reviews low-confidence matches |

### Deal Activation (C23)

| ID | Action | Detail | Classification |
|---|---|---|---|
| C23 | **Commence deal** | Click Accounting → Perform Classification Test → Compute Yield → Commence. If warnings appear, decide whether to Override | 🔶 Hybrid — AI clicks through standard steps, human decides on warning overrides |

**Stage 3 result**: Deal is activated. Confirmation message received. Test case complete.

---

## Post-Execution Checklist

After completing all 3 stages for a test case:

- [ ] Record result in Deals Automated sheet (Status, Landed in Odessa, Validated)
- [ ] If any validation failed: classify defect using Doc 08 Section 8.1 decision tree
- [ ] If new question arose not covered in KB: log for PM to add to FAQ
- [ ] If test case is fully automated: update Doc 07 automation status

---

## Quick Reference: Action Counts per Stage

| Stage | Total Actions | ✅ AI | 🔶 Hybrid | 🔴 Human |
|---|---|---|---|---|
| QT | 22 | 20 | 2 | 0 |
| Origination | 14 | 12 | 1 | 1 |
| Odessa | 23 | 16 | 5 | 0 |
| **Total** | **59** | **48** | **8** | **1** |
