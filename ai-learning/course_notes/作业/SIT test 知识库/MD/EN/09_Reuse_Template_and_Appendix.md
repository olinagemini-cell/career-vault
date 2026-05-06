# 09 — Reuse Template & Appendix

> **Audience**: Future project teams adapting this KB for new countries or new system integrations  
> **Maintainer**: 甲方 PM  
> **Update Frequency**: Rarely (framework-level updates only)  
> **Related Docs**: 00 (Index — for current project navigation)

---

## 9.1 Reusability Guide — Adapting for Future Projects

This knowledge base is designed for reuse. The 10-document structure, action classification methodology, and project management framework are universal. Only the content within each document changes per project.

### What to Replace (country/project-specific content)

| Document | What Changes | Example |
|---|---|---|
| 01 - Product & Contract Types | Product types, contract types, campaign values | "Finance Lease China" → "Finance Lease Vietnam" |
| 02 - Business Rules | Tax rates, currency, legal entity, regulatory rules, default values, formulas | VAT 13% → GST 10%; CNY → VND; ZhongDeng → local registration |
| 03 - Roles & Process Flow | Third party role definitions (if different), approval workflow stages | May have different approval chain or additional parties |
| 04 - QT → Origination Mapping | Field names, editable/locked status (if system version differs) | New fields may be added, some may be removed |
| 05 - Origination → Odessa Mapping | Field names, validation rules, default values, conditional logic | All validation rules are country-specific |
| 06 - Action Playbook | Action steps (if UI differs), input sources | UI navigation may differ per system version |
| 08 - Project Management | Test execution status, defect counts, regression scenario list | Completely new data per project |

### What to Keep As-Is (universal framework)

| Document | What Stays | Reason |
|---|---|---|
| 00 - Index & Navigation | 10-doc structure, reading paths, cross-reference guide | Framework is system-agnostic |
| 07 - Automation & AI Strategy | Classification methodology (AI/Hybrid/Human), tier structure, ROI model | Approach applies to any multi-system integration |
| 08 - Project Management | Defect classification tree structure, maintenance protocol, weekly report template | Universal PM practices |
| 09 - Reuse Template | This guide, glossary structure, version history format | Meta-framework |

### Adaptation Checklist for New Project

- [ ] **Step 1**: Copy all 10 documents to new project folder
- [ ] **Step 2**: Update Doc 00 with new project name, systems, team contacts
- [ ] **Step 3**: Replace all values in Doc 01 tables with new country/product data
- [ ] **Step 4**: Rebuild Doc 02 from new business requirements and regulatory rules
- [ ] **Step 5**: Update Doc 03 if party roles or process stages differ
- [ ] **Step 6**: Rebuild Docs 04-05 from new system field specification documents
- [ ] **Step 7**: Re-run action decomposition on new E2E test cases → update Doc 06
- [ ] **Step 8**: Reassess automation tool selection in Doc 07 based on new system's technology stack
- [ ] **Step 9**: Reset Doc 08 status tracking for new project
- [ ] **Step 10**: Update Doc 09 glossary with new terms

**Estimated effort to adapt**: 3-5 days for a similar-scope project (same system platforms, new country). 1-2 weeks if system platforms also change.

---

## 9.2 Glossary

### Business Terms

| Term | Full Name | Definition |
|---|---|---|
| DL | Direct Lease | Lessor purchases asset from supplier and leases to customer |
| SLB | Sale-and-Leaseback | Customer sells existing asset to lessor and leases it back |
| AOR | Asset Operating Rental | Operating rental / unsecured loan structure |
| HP | Hire Purchase | Customer acquires ownership after final payment (Hong Kong) |
| ORV | Optional Residual Value | Lease with customer option to purchase at residual value at end of term |
| PG | Personal Guarantor | Individual providing personal guarantee for a lease |
| CG | Corporate Guarantor | Company providing corporate guarantee for a lease |
| COF | Cost of Funds | Base interest rate representing the lessor's funding cost |
| LPR | Loan Prime Rate | China's benchmark floating rate index, published by PBOC |
| IRR | Internal Rate of Return | Profitability measure calculated in Quotation Tool |
| IM | International Manufacturer | Acquisition channel: asset sourced through international manufacturer's local entity |

### System Terms

| Term | Full Name | Definition |
|---|---|---|
| QT | Quotation Tool | Front-end system for creating lease quotes and simulations |
| Origination | Origination System | Middle-office system for deal structuring, approval, and compliance |
| Odessa | Odessa Back Office | Back-office system for contract management, billing, and accounting |
| SGEF | Société Générale Equipment Finance | Parent company platform / integration endpoint |
| TP Ref | Third Party Reference | Unique identifier for a party (customer, supplier, vendor) in the system |
| AMT | Asset Management Tool | Asset reference system providing model codes |

### Technical Terms

| Term | Full Name | Definition |
|---|---|---|
| SIT | System Integration Testing | Testing phase verifying data flow across multiple connected systems |
| E2E | End-to-End | Complete flow from first system (QT) through last system (Odessa) |
| RPA | Robotic Process Automation | Software automation for repetitive UI-based tasks |
| UAT | User Acceptance Testing | Testing phase where business users validate system behavior |
| KB | Knowledge Base | Structured repository of project knowledge for team reference |

### Chinese Regulatory Terms

| Term | Definition |
|---|---|
| 中登 (ZhongDeng) | China's movable property registration system. Finance lease contracts must be registered for legal protection |
| 增值税 (VAT) | Value-Added Tax. Standard rate 13% for tangible goods leasing in China |
| 统一社会信用代码 | Unified Social Credit Code. 18-digit identifier for Chinese business entities (Registration ID type 00715) |

---

## 9.3 Document Inventory

| File | Format | Content | Primary Audience |
|---|---|---|---|
| 00_Index_and_Navigation.md | Markdown | Master index, reading paths, cross-reference | All |
| 01_Product_and_Contract_Types.md | Markdown | Product types, contract types, campaign mapping | 乙方 |
| 02_Business_Rules_and_Conditional_Logic.md | Markdown | China/HK differences, defaults, formulas, rate logic | 甲乙双方 |
| 03_Roles_and_Process_Flow.md | Markdown | Third party roles, Lease vs Loan, E2E flow | 乙方 (onboarding) |
| 04_Field_Mapping_QT_to_Origination.md | Markdown | 72 fields with editable/locked status | 乙方 Dev & Test |
| 05_Field_Mapping_Origination_to_Odessa.md | Markdown | 148+ fields, Lease/Loan/Customer modules | 乙方 Dev & Test |
| 06_Action_Playbook_and_Execution_Guide.md | Markdown | 51 actions, step-by-step execution guide | 乙方 Test Execution |
| 07_Automation_and_AI_Strategy.md | Markdown | Classification, human points, tool roadmap | 甲方 PM |
| 08_Project_Management_and_Defect_Framework.md | Markdown | Defect tree, status, regression, maintenance | 甲方 PM + QA |
| 09_Reuse_Template_and_Appendix.md | Markdown | Adaptation guide, glossary, inventory | Future projects |
| KB_Dim1_Business_Rules.docx | Word | Formatted business rules (printable) | Reference |
| KB_Dim2_Field_Mapping.docx | Word | Field mapping dictionary (landscape) | Reference |
| KB_Action_Analysis.xlsx | Excel | Action inventory with tool recommendations | Reference |
| China_end_to_end_test.xlsx | Excel | Source test data | Source |

---

## 9.4 Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | March 2026 | PM (IT) | Initial version: 10 Markdown documents split from master KB |
| | | | _Future entries below_ |
| | | | |

---

## 9.5 Feedback & Improvement

To improve this knowledge base:

1. **乙方 team**: When you encounter a question not answered by the KB, don't just ask the PM — also note which document you expected to find the answer in. This helps us place new content correctly.
2. **甲方 PM**: After each sprint, review the defect log for patterns that indicate missing KB content. A recurring question = a missing KB entry.
3. **Future projects**: After completing adaptation (Section 9.1), document what was harder than expected. Update the adaptation checklist for the next team.
