# 00 — SIT Knowledge Base: Index & Navigation

> **Audience**: All project members (甲方 PM, BA, QA / 乙方 Development & Testing)  
> **Maintainer**: 甲方 PM  
> **Update Frequency**: When documents are added or restructured

---

## What Is This Knowledge Base

This is a structured knowledge base for the **China / Hong Kong Leasing Platform SIT (System Integration Testing)** project. It covers the end-to-end data flow across three systems:

```
Quotation Tool (QT)  →  Origination  →  Odessa Back Office
```

The knowledge base serves two purposes:
1. **Immediate**: Accelerate the current SIT phase by eliminating information asymmetry between 甲方 and 乙方
2. **Long-term**: Provide a reusable framework for future multi-system integration projects

---

## Document Map

The knowledge base is split into **10 documents**, organized by audience and usage scenario:

### For Everyone

| Doc | Title | What It Contains | When to Read |
|-----|-------|-----------------|--------------|
| **00** | Index & Navigation (this file) | Document map, reading paths, version history | First time, then as needed |

### For 乙方 (Vendor Team)

| Doc | Title | What It Contains | When to Read |
|-----|-------|-----------------|--------------|
| **01** | Product & Contract Types | 3 product types, 18+ contract types, campaign mapping rules | Onboarding, then as reference |
| **03** | Roles & Process Flow | Third party roles (Client/Supplier/Vendor/Guarantor), Lease vs Loan module, E2E process stages | Onboarding |
| **04** | Field Mapping: QT → Origination | 72 fields with editable/locked status | Daily reference during development & testing |
| **05** | Field Mapping: Origination → Odessa | 148+ fields across Lease, Loan, Customer modules | Daily reference during development & testing |
| **06** | Action Playbook & Execution Guide | 51 discrete actions, step-by-step execution for each E2E stage | Test execution |

### For 甲乙双方 (Both Parties)

| Doc | Title | What It Contains | When to Read |
|-----|-------|-----------------|--------------|
| **02** | Business Rules & Conditional Logic | China vs HK differences, system defaults, calculation formulas, rate type logic | Onboarding + whenever rules change. **甲方 owns updates, 乙方 executes against it** |

### For 甲方 (Client PM / QA)

| Doc | Title | What It Contains | When to Read |
|-----|-------|-----------------|--------------|
| **07** | Automation & AI Strategy | Automation classification (AI/Hybrid/Human), human intervention points, 3-tier tool roadmap | Sprint planning, tool selection |
| **08** | Project Management & Defect Framework | Defect classification tree, regression scenario status, KB maintenance protocol, test execution status | Weekly status, defect triage |
| **09** | Reuse Template & Appendix | Adaptation guide for new projects, glossary, version history, document inventory | Future project kickoff |

---

## Recommended Reading Paths

### Path A: New 乙方 team member joining the project
```
00 (this file)  →  01 (products)  →  03 (roles & flow)  →  02 (rules)  →  04 + 05 (field mapping)  →  06 (playbook)
```

### Path B: 乙方 tester executing a test case
```
06 (action playbook)  →  04 or 05 (look up specific field)  →  02 (check a business rule)
```

### Path C: 甲方 PM reviewing progress & planning
```
08 (project management)  →  07 (automation strategy)  →  02 (review rules needing update)
```

### Path D: Launching a new country / new system integration project
```
09 (reuse template)  →  00 (adapt document structure)  →  rebuild 01-06 with new content
```

---

## Cross-Reference Guide

When you encounter a question during testing, use this lookup:

| Question | Go To |
|----------|-------|
| "What product types are available?" | Doc 01, Section 1.1 |
| "How does Campaign map to Deal Type in Odessa?" | Doc 01, Section 1.2 |
| "What's the difference between China and HK?" | Doc 02, Section 2.1 |
| "What's the default value for ZhongDeng Status?" | Doc 02, Section 2.2 |
| "How is Inception Payment calculated?" | Doc 02, Section 2.3 |
| "What happens when Rate Type = Floating?" | Doc 02, Section 2.4 |
| "Who is the Supplier vs the Vendor vs the Dealer?" | Doc 03, Section 3.1 |
| "Should this go to Lease module or Loan module?" | Doc 03, Section 3.2 |
| "What QT field maps to Origination's Net Amount?" | Doc 04 |
| "What should Odessa's Remit To field show?" | Doc 05 |
| "What are all the steps for QT data entry?" | Doc 06, Stage 1 |
| "Which actions can be automated?" | Doc 07, Section 7.1 |
| "A field validation failed — whose bug is it?" | Doc 08, Section 8.1 |
| "What does AOR stand for?" | Doc 09, Glossary |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | March 2026 | PM (IT) | Initial split into 10 documents from master KB |

---

## Companion Files

| File | Format | Description |
|------|--------|-------------|
| KB_Dim1_Business_Rules.docx | Word | Formatted business rules with professional tables |
| KB_Dim2_Field_Mapping.docx | Word | Complete 148-field mapping dictionary (landscape layout) |
| KB_Action_Analysis.xlsx | Excel | 51-action inventory with automation classification, tool recommendations, human intervention analysis |
| China_end_to_end_test.xlsx | Excel | Original test data source (E2E scenarios, Integration Data, Field Validations, Regression, Deals) |
