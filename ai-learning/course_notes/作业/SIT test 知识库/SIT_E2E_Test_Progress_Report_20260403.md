# China E2E SIT Test Progress Report
**Report Date**: 2026-04-03
**Prepared by**: Olina (SIT Lead, Client Side)
**Report Period**: 2025-10 ~ 2026-04

---

## 1. Executive Summary

China/HKG End-to-End SIT testing is currently in **mid-stage execution** with significant blockers. Out of 42 tracked deals in the latest test cycle, only **3 deals (7.1%) have successfully landed in Odessa**, while **13 deals (31%) failed at Odessa landing**, and **8 deals (19%) are still pending "Send to BO"**. The primary root causes are **recurring TP (Third Party) data quality issues** and **system integration gaps** between Origination and Odessa.

### Key Metrics at a Glance

| Metric | Value |
|--------|-------|
| Total Test Scenarios Designed (TC1-TC19) | 19 scenario types, 33 data rows |
| Total Deals Tracked (New Version) | 42 |
| Automation Completed | 16 |
| Successfully Landed in Odessa | 3 (18.8% of completed) |
| Failed at Odessa Landing | 13 (81.3% of completed) |
| Odessa Validation Passed | 0 |
| Pending "Send to BO" | 8 |
| Old Data (prior cycle) | 14 |
| Waiting for Clarification | 1 |

---

## 2. Old Version vs New Version: Key Changes

### 2.1 Structural Changes

| Aspect | Old Version (Mar 28) | New Version (Apr 3) |
|--------|---------------------|---------------------|
| Total Sheets | 7 | 11 |
| Deals Tracked | 38 (many blank) | 42 (all with data) |
| Deals Automated Columns | 6 (basic) | 8 (with contract#, comments, cloning info) |
| Odessa Validation Columns | 8 | 10 (added "Validated" + "Field/Default Value") |
| Regression Scenarios | 1 combined sheet (92 rows) | Split into UK (92 rows) + China-specific (57 rows) |
| New Sheets Added | - | China MasterTestcases, QT-CHN-TESTING-COE-26071, Test reference - Business |

### 2.2 Data & Mapping Corrections (Integration Data Sheet)

| Field | Old Version | New Version | Impact |
|-------|------------|-------------|--------|
| SLB Campaign Mapping | "SLB" | "Sale and Leaseback" | Proper Odessa naming convention |
| AOR Campaign Mapping | "AOR" | "Assignment Of Receivables" | Proper Odessa naming convention |
| AOR Deal Type in Odessa | Formula reference (=AS) | Explicit "Unsecured Loan" | Clear mapping, no formula dependency |
| ZhongDeng Status | Blank | "Pending or Confirmed" | Added expected validation value |

### 2.3 Odessa Field Validation Enhancement

New version added two critical columns:
- **"Validated" column**: Tracks which fields have been verified (Yes/Config/blank)
- **"Field / Default Value" column**: Documents the source field or expected default

**Validation coverage status** (Lease section, ~94 fields):
- **Validated = Yes**: ~52 fields (55%)
- **Validated = Config**: 4 fields (Make, Model, Manufacture, Asset Type)
- **Validated = blank/pending**: ~38 fields (40%) -- notably Interest Rate details, Tax, Blended Items, Payoff Assignment, Late Fee, some Structure fields

### 2.4 New Test Cases & Artifacts

1. **China MasterTestcases**: A new 17-step standardized Odessa validation checklist covering Profile, Fundings, Assets, Structure, Interest Rate, Payment Schedule, Tax, Investment Details, Blended Items, Accounting, Maturity Management, Contract Options, Late Fees, and Third Parties.

2. **QT-CHN-TESTING-COE-26071**: Detailed field-by-field payload mapping for deal QT-CHN-TESTING-COE-26071 (84 rows), exposing significant gaps:
   - **"Missing in Odessa scraped File"**: 15+ fields (Asset costs, Tax, Payee, Lease Asset details, Payment schedule, Contract Third Party)
   - **"Missing in Both payloads"**: 12+ fields (Interest Rate details, Tax code/rate, Blended Items, Payoff Assignment, Late Fee, Third Parties)

3. **Regression Scenarios (CH)**: 57 China-specific regression test cases (TC_01 ~ TC_53) covering Customer Creation, Asset Management, Lease/Loan operations, Restructure, Payoff, Security Deposit, Float Rate, Jobs, etc.

---

## 3. Current Deal Execution Status (Deals Automated - New Version)

### 3.1 Status Distribution

```
Completed + Success:      3 deals  ( 7.1%)  -- 1586(validation failed), 1658, 1669
Completed + Failed:      13 deals  (31.0%)  -- see breakdown below
Waiting for Clarification: 1 deal  ( 2.4%)  -- 1662 (SLB import cashflow question)
Pending Send to BO:       8 deals  (19.0%)  -- 1659,1664,1667,1668,HKG-145/146,1676,1677
Old Data (prior cycle):  14 deals  (33.3%)  -- carried forward, not re-tested
Send to BO (HKG):         2 deals  ( 4.8%)  -- HKG-159, HKG-160
No Status:                1 deal   ( 2.4%)  -- HKG-133
```

### 3.2 Failed Deals Root Cause Analysis

| Root Cause Category | Affected Deals | Count | Severity |
|---------------------|---------------|-------|----------|
| **TP Data Quality - Province/State Missing** | 1657, 1660, 1665, 1666, 1670, 1624 | 6 | Critical (Recurring) |
| **TP Data Quality - Legal Name Missing** | 1658(resolved), 1624 | 2 | Critical (Recurring) |
| **TP Data Quality - Multiple Matching Entities** | 1658, 1624 | 2 | Major |
| **Deal Not Reflecting in Odessa** (pushed but invisible) | 1665, 1666, 1670, 1672, 1673, 1674, HKG-163 | 7 | Critical (Systemic) |
| **Tax Code/Rate Missing** | 1655 | 1 | Major |
| **Cross-Entity Vendor Mismatch** | 1621 | 1 | Major (Business Rule) |
| **Odessa Landing - Unknown/To Check** | 1609, 1656 | 2 | Under Investigation |
| **Validation Failed post-Success** | 1586 | 1 | High |
| **ORIG Cannot Sync TP Update** | 1660 | 1 | Critical (System Bug) |

### 3.3 Contract Type Coverage

| Contract Type | Total Deals | Completed | Success | Failed | Pending |
|---------------|-------------|-----------|---------|--------|---------|
| Direct Lease | 17 | 7 | 0 | 5 | 4 |
| SLB | 11 | 5 | 2 | 3 | 2 |
| AOR | 5 | 3 | 0 | 3 | 1 |
| Operating Lease | 2 | 1 | 0 | 1 | 1 |
| Direct Lease Import | 1 | 1 | 0 | 1 | 0 |
| SLB Import | 1 | 0 | 0 | 0 | 0 (waiting) |
| HKG Direct Lease | 4 | 1 | 0 | 1 | 2 |
| HKG SLB | 1 | 0 | 0 | 0 | 1 |

---

## 4. Recurring Issues from Integration Test (Constraint Tracker)

From the **Integration test update** file, 26 integration constraints were identified:

### 4.1 Resolution Status

| Status | Count | Percentage |
|--------|-------|-----------|
| Solved | 17 | 65.4% |
| WIP (Work in Progress) | 4 | 15.4% |
| No Status / New | 5 | 19.2% |

### 4.2 Critical WIP Items (Blocking Progress)

| # | Issue | Owner | Impact |
|---|-------|-------|--------|
| 2 | **TP entity alignment - cross BU relationships** | GW | CHN deals with HKG TP/guarantor fail; GW to manage multiple relationships | 
| 5 | **Global Sector Code** not auto-managed | ORIG | "cost center" mandatory for EXACT in Odessa, manual workaround needed |
| 15 | **First instalment date = disbursement date** | Odessa | China/HKG use fixed instalment due day; Odessa needs to accept instalment from ORIG |
| 18 | **2-decimal vs 4-decimal precision** | Odessa | QT/ORIG run 4-decimal calculations; Odessa only accepts 2 decimals, causing rounding failures |

### 4.3 New/Unresolved Constraints (No Status)

| # | Issue | Impact |
|---|-------|--------|
| 23 | Invoice Date must be on/before disbursement date | China invoicing practice conflict |
| 24 | VAT code mandatory on Cashflow (not mandatory in ORIG) | Missing data at Odessa landing |
| 25 | Third Party mandatory on Cashflow (not mandatory in ORIG) | Missing data at Odessa landing |
| 26 | Invoice amount must equal sum of Assets Cost + Other Costs | Recurring landing failures |

### 4.4 Issues Recurring in Current Test Cycle

These "solved" or "known" issues are **still causing failures** in the new test cycle:

| Issue Pattern | Originally From | Still Occurring In |
|--------------|-----------------|-------------------|
| Province/State missing in TP | Constraint #20 (marked Solved) | Deals 1657, 1660, 1665, 1666, 1670, 1624 |
| Invoice amount mismatch | Constraint #26 (no status) | Historical deals 1482, 1484, 1494, 1496, 1497 |
| TP Legal Name missing | Related to Constraint #9 | Deals 1658, 1624 |
| Deal pushed to BO but not reflecting in Odessa | New pattern | 7 deals in current cycle |
| Data format (scientific notation) | Related to Constraint #18 | Deal 1490 |

**Key Observation**: The TP data quality issue (Province/State missing) was marked as "Solved" in the constraint tracker, but it continues to be the #1 failure cause in the current test cycle. This suggests the fix is incomplete or the fix does not cover all TP records.

---

## 5. Odessa Validation Gap Analysis

Based on the detailed mapping in **QT-CHN-TESTING-COE-26071**, the following field categories have validation gaps:

### Fields Successfully Validated
- Primary Details (Customer, Sequence#, Legal Entity, Country, Currency, Deal Type, Transaction Type, ZhongDeng Status)
- Origination (Source Type, Source)
- Lease Billing (Bill To, Remit To)
- Fundings (Vendor - partial)
- Structure (# of payments, Frequency, Advance, Commencement Date, Down Payment, Term)

### Fields with Known Issues
| Category | Missing/Issue Fields | Status |
|----------|---------------------|--------|
| **Asset & Costs** | Asset cost, Tax, Tax code, Payee, Amount, Remit to | Missing in Odessa scraped file |
| **Lease Asset** | Serial#, Make, Model, Manufacture | Missing in Odessa scraped file |
| **Interest Rate** (9 fields) | Float Rate Index, Base Rate%, Spread%, Float Rate Reset Unit, First Reset Date, Move Across Month | Missing in both payloads |
| **Payment Schedule** | Full schedule details | Missing in Odessa scraped file |
| **Tax** | Tax code, Tax Rate | Missing in both payloads |
| **Blended Items** | All items | Missing in both payloads |
| **Payoff Assignment** (4 fields) | OTP Fee, Late Fee Template, Grace Days | Missing in both payloads |
| **Late Fee Setup** | All values | Missing in both payloads |
| **Third Parties** | All values | Missing in both payloads |
| **Contract Third Party Relationship** (7 fields) | All fields | Missing in Odessa scraped file |
| **Structure - Float Rate** | Float Rate Lease shows False but should be True for floating rate deals | Data mismatch |

---

## 6. Test Coverage Assessment

### 6.1 E2E Scenario Coverage (TC1-TC19)

| Scenario | Type | China/HKG | Has Test Data | Executed | Passed E2E |
|----------|------|-----------|---------------|----------|------------|
| TC1 | Vendor-Domestic DL | China | Yes | Old cycle | No (decimal issue) |
| TC2 | Vendor-Domestic SLB | China | Yes (4 sub-deals) | Old cycle | Partial |
| TC3 | Vendor-Domestic HP | HKG | Yes | Old cycle | Unknown |
| TC4 | HKG FL | HKG | Yes | Old cycle | Unknown |
| TC5 | Vendor-Domestic ORV | China | Yes | Old cycle | No |
| TC6 | Vendor-Import DL | China | Yes | New cycle | Failed (TP) |
| TC7 | Vendor-Import SLB | China | Yes (2 sub-deals) | Partial | Waiting |
| TC8 | Vendor-AOR | China | Yes | New cycle | Failed |
| TC9 | Direct-Domestic DL | China | Yes (5 sub-deals) | Multiple attempts | Partial |
| TC10 | Direct-Domestic SLB | China | Yes (2 sub-deals) | Old cycle | Unknown |
| TC11 | SLB with Mortgage | China | Yes | New cycle | Unknown |
| TC12 | DL with Mortgage | China | Yes | New cycle | Unknown |
| TC13 | SLB Irregular Payment | China | Yes | New cycle | Unknown |
| TC14 | DL Irregular Payment | China | Yes | New cycle | Unknown |
| TC15 | AOR with Interest | China | Yes | New cycle | Unknown |
| TC16 | AOR Irregular Payment | China | Yes | Old cycle | Unknown |
| TC17 | DL Multi-Asset | China | Yes | New cycle | Unknown |
| TC18 | SLB with PG/CG/VFL Guarantee | China | Yes | New cycle | Unknown |
| TC19 | DL Full Feature (Guarantor, Multi-asset, DP, SD, Commission, MF, OTP) | China | Yes | Yes | Landed but validation failed |

**E2E Pass Rate: 0/19 scenarios fully validated end-to-end.**

### 6.2 Regression Test Readiness

- **UK Regression Scenarios**: 92 scenarios, ~18 marked applicable to China/HKG
- **China-Specific Regression**: 57 scenarios (TC_01-TC_53) designed, **0 executed** (blocked by E2E failures)

---

## 7. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| TP data quality continues to block testing | **High** | Critical | Require TP data pre-validation before deal creation; build TP data checklist |
| "Deal not reflecting in Odessa" is a systemic issue | **High** | Critical | Escalate to Odessa team for root cause analysis on the 7 affected deals |
| Interest Rate and Blended Item validation cannot proceed | **Medium** | High | Payload mapping incomplete; need GW/Odessa team to expose missing fields |
| Regression testing delayed indefinitely | **High** | High | Cannot start regression until at least 3-5 E2E scenarios pass fully |
| 4 WIP integration constraints still unresolved | **Medium** | High | Track weekly with GW/ORIG/Odessa owners |

---

## 8. Recommendations

### Immediate Actions (This Week)
1. **Escalate "Deal not reflecting in Odessa" issue** - 7 deals successfully pushed to BO but invisible in Odessa. This is a new systemic issue not in the constraint tracker.
2. **TP Data Quality Blitz** - Create a pre-flight checklist for TP data (Province, Legal Name, Address State) and validate ALL TPs before creating new test deals.
3. **Close the 4 open constraints** (#23, 24, 25, 26) - Assign owners and ETAs.

### Short-term (Next 2 Weeks)
4. **Complete payload mapping** - The QT-CHN-TESTING-COE-26071 analysis shows 27+ fields "missing in both payloads". GW team needs to expose these fields.
5. **Re-run the 3 successful deals** through full Odessa validation (including Interest Rate, Payment Schedule, Blended Items).
6. **Prioritize TC19 (full feature DL)** for complete validation as the benchmark scenario.

### Medium-term (Next Month)
7. **Start China-specific regression** (57 scenarios) once at least 5 E2E scenarios pass completely.
8. **Automate TP data validation** as a pre-step in the automation pipeline.

---

## Appendix A: Deal Status Detail (New Cycle Only)

| Deal | Contract# | Type | Status | Odessa | Issue Summary |
|------|-----------|------|--------|--------|---------------|
| 1586 | DL-AUTO-83537 | DL | Done | Success/Val Failed | Validation issues pending Anish email |
| 1609 | AOR-AUTO-557 | AOR | Done | Failed | To check with Odessa |
| 1621 | SLB-AUTO-71121 | SLB | Done | Failed | Invalid vendor (cross-entity), corrected |
| 1656 | DL-AUTO-37215 | DL | Done | Failed | To check with Odessa |
| 1657 | DL-AUTO-44211 | DL | Done | Failed | Province missing (SGEFTP-40258) |
| 1655 | SLB-AUTO-17880 | SLB | Done | Failed | No tax code/rate for combination |
| 1658 | SLB-AUTO-38396 | SLB | Done | Success | TP issues resolved after multiple rounds |
| 1624 | OL-AUTO-52447 | OL | Done | Failed | TP Province + Legal Name missing (multiple rounds) |
| 1660 | - | DL Import | Done | Failed | Address state missing; ORIG can't sync TP update |
| 1665 | DL-AUTO-9065 | DL | Done | Failed | Province missing; pushed but not in Odessa |
| 1666 | SLB-AUTO-67627 | SLB | Done | Failed | Address state missing; pushed but not in Odessa |
| 1669 | SLB-AUTO-76918 | SLB | Done | Success | Clean pass |
| 1670 | DL-AUTO-12161 | DL | Done | Failed | Address state missing; pushed but not in Odessa |
| 1672 | AOR-AUTO-568 | AOR | Done | Failed | Supplier validation + pushed but not in Odessa |
| 1673 | AOR-AUTO-40237 | AOR | Done | Failed | Same as 1672 |
| 1674 | DL-AUTO-29326 | DL | Done | Failed | Pushed but not in Odessa |
| HKG-163 | HKG-DL-AUTO-78369 | DL | Done | Failed | Pushed but not in Odessa |

---

*Report generated with assistance from AI analysis tools.*
*Data sources: China end to end test.xlsx, China end to end test -new version.xlsx, Integration test updat.xlsx, KB_Action_Analysis.xlsx*
