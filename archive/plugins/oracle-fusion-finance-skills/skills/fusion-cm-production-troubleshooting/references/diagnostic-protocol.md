# Diagnostic protocol (in full)

Release note: FSM task names and profile options below are stated as Oracle documents them
in recent releases — confirm exact names, values, and availability in the user's release
before recommending a change.

## Contents
- Intake: what to collect before diagnosing
- Environment-parity checklist (run first)
- Foundational setup validation
- Reconciliation diagnosis detail
- Import/processing error taxonomy
- Output templates

## Intake: what to collect before diagnosing
- **Symptoms:** exact behavior — match-rate numbers (test vs prod), which accounts, since when
- **Errors:** full message text from the Bank Statements and Reconciliation work area, ESS
  job output for AutoReconciliation / import runs, File ID details for failed loads
- **Bank account setup:** every tab — General; GL accounts (cash / cash clearing / charges);
  Controls (auto-reconciliation flags, open interface); Security; Business Unit / Legal
  Entity access; Account Uses (AP, AR, Payroll, Treasury, Payments); Payment Documents
- **Rules:** reconciliation rule set (parent-child structure and sequence), each matching
  rule's type / sources / grouping attributes / criteria, tolerance rules (amount, date,
  percentage), and the rule-set-to-bank-account assignment
- **Statement side:** format (BAI2, MT940, CAMT.053, …), parse rule set, transaction-code
  mappings, code map groups, a sample file (sanitized)
- **Environment delta:** data volume, file source and encoding, patch levels, security
  roles and data-access policies, org structure (LE/BU/ledger), period statuses, recent
  changes or migrations, profile option values

## Environment-parity checklist (run FIRST)
| Dimension | What breaks in prod | Check |
|---|---|---|
| Data volume | Selection thresholds, timeouts, partial passes | Prod transaction counts vs test; threshold-type profile options (e.g. transaction-selection threshold — confirm name in release) |
| Security / data access | Rules can't see candidate transactions | Same role test in prod; data security policies by LE/BU; who ran the job |
| Patch level | Behavior drift between pods | Release/patch versions of both environments |
| Bank feed reality | Encoding, stray codes, reference formats absent from test files | Diff a real prod file vs the test file used in UAT |
| Scheduling | Jobs run in different order/time; statement arrives after recon runs | ESS schedules, job history timestamps |
| Org assignments | Account visible to wrong/no BU or ledger | LE/BU/ledger assignment on the failing account |
| Period status | Posting blocked downstream | GL/subledger period status in prod |

## Foundational setup validation
1. Banks, branches, accounts created and complete (FSM: Manage Banks / Manage Bank
   Branches / Manage Bank Accounts; or the Rapid Implementation spreadsheet).
2. GL accounts populated: cash, cash clearing, bank charges; account uses enabled for the
   flows in play.
3. Bank statement transaction codes defined and mapped — undefined incoming codes are the
   single most common Import Error source.
4. Parse rule set and code map groups assigned to the statement format.
5. Controls tab flags: auto-reconciliation enabled where intended; open-interface setting
   matches the integration design.
6. Profile options at intended values (transaction selection threshold, GL reconciliation
   enablement, country-specific validation toggles — confirm exact names/values in release).
7. FSM task completion: nothing half-migrated from the last configuration export/import.

## Reconciliation diagnosis detail
- **Assignment:** the rule set is assigned to the exact failing bank account (not just
  created).
- **Sequencing:** one-to-one rules keyed on a reference identifier first; broader
  one-to-many/many-to-one next; many-to-many and zero-amount last. Early low-precision
  rules consume transactions that precise rules would have matched.
- **Tolerances:** amount/date/percentage neither so tight that timing differences miss nor
  so loose that false matches post; tolerance applies where the rule type supports it.
- **Criteria vs data:** matching criteria (Amount, Date, Reconciliation Reference,
  Transaction Type, Structured Payment Reference, Value Date, …) must name fields the
  production data actually populates — a criterion on a reference the bank never sends
  matches nothing.
- **Grouping attributes:** wrong grain silently prevents many-sided matches.
- **Advanced criteria:** case sensitivity and data-type comparisons — text-vs-number
  mismatches fail quietly.
- **Sources:** AP payments, AR receipts, Payroll, GL journals (value date, reversal
  exclusion), external transactions — each source enabled where expected.
- **Process:** AutoReconciliation ESS log — what was selected, matched, and skipped; run
  window vs statement arrival.

## Import/processing error taxonomy
| Class | Layer | Typical causes | Fix direction |
|---|---|---|---|
| **Load Error** | Transport/parse | File fetch failure, encoding, structural non-compliance with format | Fix the file/feed or parse rule set; re-load |
| **Import Error** | Functional | Duplicate statement, undefined transaction codes, missing mappings | Define/map the code, resolve the duplicate; re-import from interface |
| **Import Warning** | Data quality | Undefined balance codes (empty descriptions), non-blocking gaps | Map codes; decide whether warning class is acceptable |

Retry mechanics differ: a Load failure means the file never reached the interface tables; an
Import failure retries from the interface without re-loading.

## Output templates

**Executive Summary**
```markdown
1. <Most probable root cause> — probability: high. Evidence: <what points here>.
2. <Second> — probability: medium. Evidence: ...
3. <Third> — probability: low but cheap to rule out. Evidence: ...
```

**Fixes table**
```markdown
| # | Change | FSM task | Before | After | Test first in |
|---|--------|----------|--------|-------|---------------|
| 1 | Resequence rules | Manage Bank Statement Reconciliation Rule Sets | M:M at seq 10 | 1:1-ref at seq 10 | TEST pod |
```

**Validation & Prevention**
- Re-run AutoReconciliation on the affected statement in non-prod with the fix; compare
  match rate against the baseline number from intake.
- Edge cases to check before declaring victory: high-volume statement days, multi-currency
  accounts, zero-amount lines, rejected/reissued payments, duplicate detection.
- Prevention: config export as part of every migration; a parity checklist at go-live; keep
  a before/after record of rule-set changes with dates and reasons.
