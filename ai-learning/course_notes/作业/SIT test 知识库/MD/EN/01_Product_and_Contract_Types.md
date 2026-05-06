# 01 — Product & Contract Types

> **Audience**: 乙方 (Vendor Development & Testing Team)  
> **Maintainer**: 甲方 PM  
> **Update Frequency**: Per Release  
> **Related Docs**: 02 (Business Rules), 03 (Roles & Flow)

---

## 1.1 Product Types

Product Type is selected at the Quotation Tool (QT) stage. It determines which downstream system modules and validation rules apply.

| Product Type | Market | Odessa Module | Description |
|---|---|---|---|
| Finance Lease China | China Mainland | Lease | All mainland leasing contracts: Direct Lease (DL), Sale-and-Leaseback (SLB), Optional Residual Value (ORV) |
| AOR CHINA | China Mainland | Loan | Asset Operating Rental. Maps to "Unsecured Loan" in Odessa Back Office |
| HKG Financial Lease (DL, SLB) | Hong Kong | Lease | All Hong Kong leasing contracts including Direct Lease, SLB, and Hire Purchase (HP) |

**Key takeaway**: Product Type drives module selection in Odessa. Finance Lease → Lease module. AOR → Loan module. Getting this wrong means validating against the wrong set of fields entirely.

---

## 1.2 Contract Types (Test Scenario Matrix)

32 test cases are defined in the Integration Data sheet. Each test case combines a **sales channel** with a **lease structure** and optional **modifiers**:

### Standard Contract Types

| TC # | Contract Type | Market | Description |
|---|---|---|---|
| TC1 | Vendor Program - Domestic DL | China | Vendor-sourced domestic Direct Lease. Asset from domestic vendor (e.g., TRUMPF China, HEIDELBERG China) |
| TC2 | Vendor Program - Domestic SLB | China | Vendor-sourced Sale-and-Leaseback. Customer sells existing asset to lessor, leases it back |
| TC3 | Vendor Program - Domestic HP | Hong Kong | Hire Purchase through vendor channel in Hong Kong |
| TC4 | Vendor Program - Domestic HP (variant) | Hong Kong | HP variant with different terms |
| TC5 | Vendor Program - Domestic ORV | China | Direct Lease with Optional Residual Value at end of term |
| TC6 | Vendor Program - Import DL | China | Direct Lease with imported asset from overseas supplier |
| TC7 | Vendor Program - Import SLB | China | Sale-and-Leaseback with imported asset |
| TC8 | Vendor Program - AOR | China | Asset Operating Rental through vendor channel |
| TC9 | Direct - Domestic DL | China | Direct-sourced (no vendor intermediary) domestic Direct Lease |
| TC10 | Direct - Domestic SLB | China | Direct-sourced Sale-and-Leaseback |

### Variant Contract Types (additional modifiers on standard types)

| Contract Type | Market | Key Modifier |
|---|---|---|
| DL with Mortgage | China | Mortgage collateral attached |
| SLB with Mortgage | China | Mortgage collateral, Constant Payment structure |
| DL with Irregular Payment | China | Non-standard (seasonal) payment schedule |
| SLB with Irregular Payment | China | Non-standard payment schedule |
| AOR with Interest | China | Interest calculation applied to AOR |
| AOR with Irregular Payment | China | Non-standard payment schedule on AOR |
| SLB with PG, CG, Vendor First Loss | China | Personal Guarantor + Corporate Guarantor + Vendor First Loss Guarantee |
| DL with Multi-Different Assets | China | Multiple different asset types in one contract |
| Full-featured DL | China | All options: PG, CG, contact info, multi-assets, asset location, downpayment, security deposit, vendor commission, management fee, option to purchase |

---

## 1.3 Campaign Mapping Rules

Campaign is set in QT and is **non-editable** in Origination. It drives two critical fields in Odessa:

| QT Campaign | Odessa Deal Type | Odessa Transaction Type | Odessa Module |
|---|---|---|---|
| Direct Lease | Finance Lease | Direct Lease | Lease |
| SLB | Finance Lease | SLB | Lease |
| AOR | Unsecured Loan | AOR | Loan |

**Common mistake**: Confusing "Direct Lease" (a Campaign/lease structure) with "Direct" (an Acquisition Channel). They are different concepts:
- Campaign "Direct Lease" = the lease is a direct lease structure (asset purchased and leased)
- Acquisition Channel "Direct" = the customer was sourced directly (no dealer intermediary)

A deal can be Campaign = "Direct Lease" with Acquisition Channel = "International Manufacturer" — this is a vendor-sourced direct lease.

---

## 1.4 Acquisition Channel → Origination Source Type

This conditional mapping is one of the most common sources of confusion:

| QT Acquisition Channel | Odessa Origination Source Type | Origination Source Value |
|---|---|---|
| Direct | **Direct** | N/A |
| International Manufacturer (IM) | **Vendor** | = Dealer Name from QT |
| International Lessor | **Vendor** | = Dealer Name from QT |
| National Lessor | **Vendor** | = Dealer Name from QT |
| Local Relationship | **Vendor** | = Dealer Name from QT |
| Bank | **Vendor** | = Dealer Name from QT |
| Syndication | **Vendor** | = Dealer Name from QT |

**Simple rule**: Only "Direct" → Source Type "Direct". Everything else → Source Type "Vendor", with the Dealer Name as the Source value.
