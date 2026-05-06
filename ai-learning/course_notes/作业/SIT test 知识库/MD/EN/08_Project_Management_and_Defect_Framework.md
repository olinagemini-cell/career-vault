# 08 — Project Management & Defect Framework

> **Audience**: 甲方 PM + QA Lead  
> **Maintainer**: 甲方 PM  
> **Update Frequency**: Per Sprint  
> **Related Docs**: 07 (Automation Strategy), 06 (Action Playbook)

---

## 8.1 Defect Classification Decision Tree

When a field validation fails during SIT, use this decision tree to determine the defect type and responsible party:

```
Validation Failed
│
├─ Expected value exists in Origination but WRONG in Odessa
│  └─ INTEGRATION DEFECT
│     Owner: 乙方
│     Fix: Data mapping logic or API transformation in Origination→Odessa interface
│
├─ Expected value WRONG in Origination (but correct in QT)
│  └─ ORIGINATION DEFECT
│     Owner: 乙方
│     Fix: QT→Origination mapping or Origination business logic
│
├─ Expected value WRONG in QT itself
│  └─ TEST DATA ISSUE
│     Owner: 甲方
│     Fix: Update Integration Data sheet with correct test data
│
├─ Default value incorrect (e.g., ZhongDeng ≠ Pending, Serviced ≠ Yes)
│  └─ CONFIGURATION DEFECT
│     Owner: 乙方
│     Fix: System configuration or seed data setup
│     Reference: Doc 02 Section 2.2 for complete default value list
│
└─ Calculated value incorrect (e.g., Maturity Date off by 1 day)
   └─ CALCULATION DEFECT
      Owner: 乙方
      Fix: Formula logic in application code
      Reference: Doc 02 Section 2.3 for expected formulas
```

### Defect Priority Guidelines

| Priority | Definition | Examples |
|---|---|---|
| P1 - Critical | Blocks all test execution or causes data corruption | Contract cannot land in Odessa at all; Payment Schedule completely missing |
| P2 - High | Specific contract type or field category broken | All Floating rate fields show Fixed values; Fundings tab completely empty |
| P3 - Medium | Individual field incorrect but workaround exists | Tax Code shows wrong value; Manufacturer parsed incorrectly |
| P4 - Low | Cosmetic or non-functional issue | Display formatting; field label mismatch |

---

## 8.2 Current Test Execution Status

### Deal Status Summary (from Deals Automated sheet)

| Status | Count | % | Action Required |
|---|---|---|---|
| ✅ Done + Landed in Odessa | 7 | 18% | Use as benchmark / reference test cases |
| ⚠️ Done + Landing Failed | 6 | 16% | Integration defects — prioritize root cause analysis |
| ⚠️ Workflow Not Completed | 9 | 24% | Blocked at business workflow — check if credit approval or checklist is incomplete |
| 🔴 No Status Yet | 16 | 42% | Not yet executed — priority backlog |
| **Total** | **38** | **100%** | |

### Key Observations

1. **42% of test cases have not been started** — this is the primary schedule risk
2. **6 deals landed but failed validation** — indicates systematic integration defects that need root-cause analysis before running more TCs
3. **9 deals stuck at workflow** — likely blocked on credit approval (B13) or checklist completion; check with business team
4. **Only 7 fully successful deals** — insufficient for SIT sign-off; need at least 1 successful deal per contract type

### Recommended Priorities

1. **Immediate**: Root-cause the 6 Failed landings — likely a common defect pattern that affects multiple TCs
2. **This week**: Unblock the 9 workflow-incomplete deals — coordinate with business for approvals
3. **Next sprint**: Execute the 16 untouched TCs, ideally with Tier 1 automation from Doc 07

---

## 8.3 Regression Scenario Status

92 regression scenarios from the global template. Current classification:

| Status | Count | Details |
|---|---|---|
| Marked applicable to China/HK | 18 | Mainly BS (Business Services): Paydown/PayOff, Lease Rebook |
| Unmarked / not applicable | 73 | Mostly COL (Collections) for UK/EU regulated products |

### Applicable Regression Scenarios

Key applicable scenarios by department:

| Department | Applicable Scenarios | Count |
|---|---|---|
| BS - Corporate | Paydown Quote & Early Termination (Unregulated Loan), PayOff Quote & Early Termination, Lease Rebook (FL & HP) | 8 |
| BS - SME | TBD | TBD |
| COL | Asset Rebate | 1 |
| GL | TBD | TBD |
| TAX | TBD | TBD |
| Others | TBD | ~9 |

**Action needed**: Use LLM classifier (Doc 07, Tier 3) to pre-classify the 73 unmarked scenarios, then business team confirms. Many COL scenarios reference "Regulated HP" or "Regulated Lease" which are UK-specific concepts and likely not applicable.

---

## 8.4 Knowledge Base Maintenance Protocol

| Trigger | Action | Owner | How |
|---|---|---|---|
| New defect found | Add to defect log with classification (8.1) and root cause | QA Lead | Defect tracking tool |
| 乙方 asks question not in KB | Answer → record → add to appropriate KB doc | 甲方 PM | Update Docs 01-05 as needed |
| System field added or renamed | Update field mapping in Doc 04 or 05 | 甲方 PM + BA | Compare release notes with current KB |
| Business rule changed | Update Doc 02, get stakeholder sign-off, notify 乙方 | 甲方 PM | Doc 02 Change Log |
| New contract type added | Add to Doc 01 contract type table, update Integration Data | 甲方 PM | Doc 01 + source Excel |
| Sprint retrospective finds knowledge gap | Create new section or expand existing doc | 甲方 PM | Any doc in KB |
| Test case automated | Update classification in Doc 06 action table | 甲方 PM | Doc 06 |

### Quarterly Health Check

Every quarter (or at major milestones), review:
- [ ] Are all field mappings in Docs 04-05 still accurate?
- [ ] Have any business rules in Doc 02 changed without KB update?
- [ ] Is the automation classification in Doc 07 still current?
- [ ] Are there recurring 乙方 questions that should be added to the KB?
- [ ] Is the defect classification tree (8.1) still complete?

---

## 8.5 Weekly Status Report Template

```markdown
## SIT Weekly Status — [Week of YYYY-MM-DD]

### Test Execution Progress
- TCs executed this week: X
- TCs passed (Done + Landed): X
- TCs failed (Done + Failed): X
- TCs blocked: X
- Cumulative pass rate: X%

### Defect Summary
- New defects raised: X (P1: X, P2: X, P3: X)
- Defects resolved: X
- Open defects: X
- Top defect category: [Integration / Configuration / Calculation]

### Blockers & Risks
1. [Description] — Impact: [X TCs blocked] — Mitigation: [action]

### Automation Progress
- Actions automated this week: X
- Total automated: X/51 (X%)
- Next automation target: [action IDs]

### KB Updates
- Docs updated: [list]
- New FAQ entries: X

### Next Week Plan
- TCs to execute: [list]
- Focus areas: [...]
```
