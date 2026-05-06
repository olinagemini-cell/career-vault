# 03 — Roles & Process Flow

> **Audience**: 乙方 (especially new team members onboarding)  
> **Maintainer**: 甲方 PM  
> **Update Frequency**: Rarely (only when system architecture changes)  
> **Related Docs**: 01 (Product Types), 06 (Action Playbook)

---

## 3.1 Third Party Roles

In the China/HK leasing business, multiple third-party roles are involved in each deal. Understanding these roles is critical — confusing Supplier with Vendor is one of the most common errors:

| Role | Definition | Example | System Flow |
|---|---|---|---|
| **Client** (Customer) | The lessee / borrower who receives the asset and makes payments | DONGGUAN YUE MINGHUA PRINTING PACKAG CO., LTD. | QT: Customer Name → Origination: Third Parties > Client → Odessa: Customer |
| **Supplier** | The party who sells the asset | HEIDELBERG GRAPHICS (BEIJING) COMPANY LIMITED | QT: Supplier Name → Origination: Invoices > Payee → Odessa: Fundings > Vendor |
| **Vendor** (Dealer) | The channel partner / sales intermediary who introduces the deal | HEIDELBERG CHINA CO., LTD. | QT: Dealer Name → Odessa: Origination Source (when Source Type = Vendor) |
| **Guarantor (PG)** | Personal Guarantor — individual providing guarantee | An individual person | Origination: Guarantee section → Odessa: Third Parties |
| **Guarantor (CG)** | Corporate Guarantor — company providing guarantee | A company entity | Origination: Guarantee section → Odessa: Third Parties |
| **Payer** | The party who pays installments | Usually = Client | Origination: Transaction Params > Payer → Odessa: Bill To |

**Key distinction — Supplier vs Vendor (Dealer)**:
- **Supplier** = who originally owns/sells the asset. Appears on invoices as the payee.
- **Vendor (Dealer)** = who brought the deal to BPCE. May or may not be the same entity as Supplier.
- In a **Direct** deal: there may be no Vendor/Dealer; the customer comes directly.
- In a **Vendor Program** deal: the Vendor/Dealer introduced the customer and the deal.

**When Payer ≠ Client**: In some contracts (e.g., CSI/Signify arrangements), the installment payer is a different entity from the lessee. When this happens, the Odessa Loan module sets `Multi Party Contract = Yes`.

---

## 3.2 Lease Module vs Loan Module in Odessa

Odessa uses two separate modules. The module is determined by the Campaign type:

| Attribute | Lease Module | Loan Module |
|---|---|---|
| **Used for Campaign** | Direct Lease, SLB | AOR |
| **Odessa Deal Type** | Finance Lease | Unsecured Loan |
| Has Lease Asset tab | Yes | No — uses Collateral Assets |
| Billing tab name | Lease Billing | Loan Billing |
| Interest Rate tab name | Lease Interest Rate | Loan Interest Rate |
| Structure specifics | Inception Payment, Float Rate fields | Loan Amount, Balloon Payment |
| Maturity Management | Yes (Over Term = False for China) | N/A |
| Payoff Assignment | Yes (Option to Purchase, Late Fee) | N/A |
| Fundings tab name | Fundings | Loan Funding |

**Practical impact**: When searching for a contract in Odessa, you must navigate to the correct module first. Searching for an AOR deal in the Lease module will return no results.

---

## 3.3 End-to-End Process Flow

A standard deal flows through three systems in sequence:

```
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│   QUOTATION TOOL    │     │    ORIGINATION       │     │   ODESSA BACK       │
│       (QT)          │────▶│                      │────▶│     OFFICE          │
│                     │     │                      │     │                     │
│ • Create quote      │     │ • Verify deal data   │     │ • Validate contract │
│ • Select asset      │     │ • Configure invoices  │     │ • Check all fields  │
│ • Set parameters    │     │ • Set up parties      │     │ • Validate schedule │
│ • Calculate IRR     │     │ • Credit approval     │     │ • Commence deal     │
│ • Send to SGEF      │     │ • Send to Back Office │     │                     │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
     22 actions                  14 actions                  23 actions
   (20 AI, 2 Hybrid)        (12 AI, 1 Hybrid,          (16 AI, 5 Hybrid)
                              1 Human)
```

### Stage 1: Quotation Tool (QT)

| Step | Action | Detail |
|---|---|---|
| 1 | Select Asset Model | Choose from picker (e.g., CX104-7+L - HEIDELBERG) |
| 2 | Select Product Type | Finance Lease China / AOR CHINA / HKG Financial Lease |
| 3 | Enter Asset Details | Unit Price, Quantity |
| 4 | Retrieve Supplier | Search by name |
| 5 | Set Deal Parameters | Campaign, Customer, Dealer, Down Payment %, Tenor, Frequency, Rate Type, Residual Value, Repayment Type |
| 6 | Advanced Parameters | Commission Fee, Management Fee, Subsidy, Security Deposit, Vendor Deposit (if applicable) |
| 7 | Calculate | IRR calculation → Simulation → Select option |
| 8 | Submit | Send to SGEF with customer information |

### Stage 2: Origination

| Step | Action | Detail |
|---|---|---|
| 1 | Search & Verify | Find quote by ID, verify Deal Overview fields (all Non-Editable) |
| 2 | Verify Details | Asset, Transaction Structure, Counter Parties |
| 3 | Configure | Invoices, Global Sector Code, Locations |
| 4 | Approve | Credit → CRO → Credit Committee → LOD1 (as required) |
| 5 | Compliance | Complete 24 checklist items, upload 6 document types |
| 6 | Send | Send deal to Back Office |

### Stage 3: Odessa Back Office

| Step | Action | Detail |
|---|---|---|
| 1 | Find Contract | Search in correct module (Lease or Loan) by contract ID |
| 2 | Validate Data | Primary Details → Origination → Servicing → Billing → Fundings → Assets → Structure → Interest Rate |
| 3 | Validate Schedule | Full payment schedule comparison with Origination |
| 4 | Validate Others | Tax, Blended Items, Maturity, Payoff, Third Parties |
| 5 | Commence | Classification Test → Compute Yield → Commence (override warnings if needed) |

**For the detailed step-by-step execution guide with all 51 actions, see Doc 06.**
