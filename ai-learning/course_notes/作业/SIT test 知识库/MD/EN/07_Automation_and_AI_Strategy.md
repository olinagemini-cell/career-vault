# 07 — Automation & AI Strategy

> **Audience**: 甲方 PM  
> **Maintainer**: 甲方 PM  
> **Update Frequency**: Per Phase (as automation tools are implemented)  
> **Related Docs**: 06 (Action Playbook), 08 (Project Management)

---

## 7.1 Automation Classification Summary

| Classification | Count | Percentage | Definition |
|---|---|---|---|
| ✅ AI Automatable | 37 | 73% | Zero human involvement. RPA or script executes fully |
| 🔶 Hybrid (AI + Human) | 12 | 23% | AI does 70-80% of work, human reviews exceptions or provides judgment |
| 🔴 Human Required | 2 | 4% | Cannot be automated — requires authorization or business judgment |
| **Total** | **51** | **100%** | |

### By Stage

| Stage | Total | ✅ AI | 🔶 Hybrid | 🔴 Human |
|---|---|---|---|---|
| QT Data Entry | 22 | 20 | 2 | 0 |
| Origination | 14 | 12 | 1 | 1 |
| Odessa Validation | 23 | 16 | 5 | 0 |
| KB Maintenance | 6 | 3 | 2 | 1 |

### Estimated Effort Impact

| Metric | Manual Execution | With AI Automation | Saving |
|---|---|---|---|
| Time per test case | ~3–4 hours | ~30–45 minutes | 75–85% |
| Human actions per TC | 51 | 10–12 (hybrid + human points) | ~80% |
| Monthly effort (30 TCs) | ~100–120 hours | ~15–25 hours | ~75–90 hours |

---

## 7.2 Human Intervention Points — Complete List

These are the **only** points where a human must be actively involved. The AI strategy is to minimize human time at each point through pre-processing:

| ID | Action | Why Human Needed | AI Assist Strategy | Human Time |
|---|---|---|---|---|
| A20-A21 | Verify QT simulation results | Business judgment: are IRR/installment commercially reasonable? | AI independently calculates expected values using formulas from Doc 02 Section 2.3. Flags only when delta > threshold or values outside historical range | 2–3 min |
| B10 | Verify Exposure Amount | External factors (group limits, existing exposure) not in test data | AI validates the arithmetic; human confirms business context is correct | 1–2 min |
| B13 | Credit approval workflow | Requires authorized signatories with approval authority | AI pre-populates approval forms, routes to correct approver, sends reminders | 10–15 min |
| C17 | Validate Payment Schedule | Rounding differences, holiday adjustments, seasonal irregularities may be acceptable or defective | AI does row-by-row comparison, flags only rows with delta > 0.01. Human reviews flagged rows only (typically <5% of total rows) | 5–10 min |
| C19 | Validate Blended Items | Complex booking rules for commission/management fee/subsidy. Amount + booking mode + date combinations need business knowledge | AI validates structure (required fields present, amounts > 0). Human validates booking logic and GL mapping | 3–5 min |
| C22 | Validate Third Party relationships | Guarantor names may have variants, guarantee amounts need cross-reference with approval | AI fuzzy name match (>90% similarity = auto-pass). Only low-confidence matches escalated to human | 2–3 min |
| C23 | Commence deal with warnings | System warnings may indicate real issues vs known acceptable conditions | AI categorizes warnings against known-safe list. Only unknown/new warning types escalated to human | 3–5 min |
| D01 | Update business rules in KB | Rule changes need stakeholder sign-off and impact analysis | AI drafts updated entries based on change request. Human reviews and publishes | 30–60 min |
| D06 | Classify regression scenarios | 92 scenarios, many for other markets. Applicability requires China-specific regulatory understanding | AI pre-classifies with ~85% accuracy. Human reviews the uncertain ~15% | 60–90 min |

**Total human time per TC (excluding D01, D06 which are ad-hoc)**: ~25–40 minutes, concentrated on approval (B13) and exception reviews.

---

## 7.3 Three-Tier Implementation Roadmap

### Tier 1: Immediate Impact — Week 1-2

| Tool | Actions Covered | What It Does | Setup Effort | ROI |
|---|---|---|---|---|
| **RPA (Selenium / Playwright)** | A01-A19, A22, B01-B12, B14, C01 | Automates all QT data entry + Origination navigation and search. One parameterized script per contract type, driven by Integration Data matrix | Low | Very High |
| **Assertion Framework (Python + pytest)** | B02-B09, C02-C16, C18, C20-C21 | Reusable assertion library: `exact_match()`, `numeric_match(tolerance)`, `conditional_rule()`. Covers 60+ Odessa field validations | Low | Very High |
| **Rule Engine (decision table)** | C03, C04, C06, C08, C12, C16 | Encodes conditional mappings from Doc 01 and Doc 02 into executable rules. Campaign→DealType, Channel→SourceType, RateType→InterestFields | Low–Med | High |

**Expected outcome**: Each TC drops from ~3-4 hours to ~30-45 minutes within 2 weeks.

### Tier 2: Medium-Term Value — Week 2-4

| Tool | Actions Covered | What It Does | Setup Effort | ROI |
|---|---|---|---|---|
| **LLM Screenshot Validation** | A20, A21 | Capture QT simulation screen, use Claude/GPT-4V to extract values and validate against expected ranges | Medium | Medium |
| **Payment Schedule Comparator** | C17 | Export both schedules as DataFrames, row-by-row diff with tolerance, auto-flag discrepancies for human review | Medium | High |
| **LLM Test Data Generator** | D03 | Given business rules + constraints from Doc 02, generate valid test data covering untested edge cases (e.g., max tenor + floating rate + seasonal payment) | Medium | High |
| **LLM Defect Analyzer** | D04, D05 | Cluster failure patterns from Deals Automated data, identify root causes, auto-generate FAQ entries for KB | Medium | Medium |

### Tier 3: Strategic — Month 2+

| Tool | Actions Covered | What It Does | Setup Effort | ROI |
|---|---|---|---|---|
| **E2E Test Orchestrator** | All A, B, C | Unified framework: read TC from Excel → execute QT → verify Origination → validate Odessa → generate report. Single click per TC | High | Very High |
| **KB Auto-Updater** | D01, D02 | Monitor system schema changes, detect field additions/renames, propose KB updates (Doc 04, 05) for human approval | High | Medium |
| **Regression Classifier** | D06 | Pre-classify 92 regression scenarios for China/HK applicability based on scenario descriptions and Doc 02 business rules | Medium | Medium |

---

## 7.4 Automation Readiness Assessment

### What makes this project highly automatable

1. **Deterministic rules**: 90%+ of validation logic is exact match, conditional rule, or formula calculation — no ambiguity
2. **Structured test data**: Integration Data matrix provides all inputs in tabular form, ready for parameterized scripts
3. **Stable UI**: QT, Origination, Odessa are web-based applications with standard HTML elements
4. **Documented field mappings**: Docs 04-05 provide the complete expected-value dictionary for assertions

### Risks to monitor

1. **UI changes**: If any system undergoes a UI redesign, RPA scripts will break. Mitigate by using stable element selectors (IDs over CSS classes)
2. **New business rules**: New rules not yet in Doc 02 will cause false test failures. Mitigate with KB maintenance protocol (Doc 08 Section 8.3)
3. **Environment instability**: SIT environments may be down or refreshed. Mitigate with retry logic in automation framework
4. **Data dependencies**: Some TCs depend on master data (customer, supplier records). Mitigate by pre-validating master data availability before test run
