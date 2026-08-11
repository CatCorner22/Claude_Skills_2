# Evals — treasury-accounting-skills:accruals-and-prepaids

## 1. Positive trigger (should load the skill)
> "Set up our month-end accrual process — last quarter the auditors found two big invoices that
> should have been accrued, and our prepaid balance doesn't tie to anything."

Expected: skill loads; builds the completeness driver list (open POs, vendor calendar, payroll
stub, contracts) rather than relying on memory; documented estimation bases on the workpaper;
auto-reversing entries with a monthly true-up report; prepaid amortization schedules whose sum
is the GL reconciliation; cutoff testing from post-period invoices.

## 2. Near-miss (should NOT load this skill)
> "What's the journal entry format for an accrual — which account do I debit and credit and
> how do I document it?"

Expected: entry mechanics — `accounting-skills:journal-entries`. If this skill loads, tighten
the process/completeness framing.

## 3. Quality rubric
A good response:
- **Does the task:** driver checklist, workpaper with bases, reversal discipline, true-up
  report, schedule-equals-GL prepaid reconciliation, and a two-direction cutoff test.
- **Teaches:** why completeness is the hard direction (missing accruals leave no ledger trace),
  the self-correcting reversal loop, service-date-not-invoice-date, and stale accruals as
  disguised misstatements.
- **Safe:** no undocumented plugs, no cookie-jar reserves, materiality-proportional effort,
  and real vendor data kept out of committed files.
