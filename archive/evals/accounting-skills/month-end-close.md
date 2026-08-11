# Evals — accounting-skills:month-end-close

## 1. Positive trigger (should load the skill)
> "We're starting the June close and it's a mess — no calendar, accruals get missed, and flux takes forever.
> Help me build a close checklist with owners and sequence the tasks so we hard close by WD5."

Expected: skill loads; lays tasks on business-day offsets with owners/reviewers and dependencies; puts cutoff
and completeness first; sequences subledger close → GL/accruals → subledger-to-GL tie-out → reconciliations →
intercompany → flux → lock; explains what flux review is for.

## 2. Near-miss (should NOT load this skill)
> "Reconcile the prepaid expense account to its supporting amortization schedule for June and age any
> reconciling items."

Expected: this is a single balance-sheet account reconciliation, not running the overall close. The
`accounting-skills:account-reconciliations` skill should handle it. If month-end-close loads instead, tighten
the description and cross-links. (A bank statement rec should route to `cash-management-skills:bank-reconciliation`.)

## 3. Quality rubric
A good response:
- **Does the task:** produces a calendar/checklist with owners and dependencies, enforces cutoff/completeness,
  covers accruals, subledger-to-GL tie-outs, balance-sheet recs, intercompany tie-out, and flux above a
  materiality threshold, ending in a locked period with an archived binder.
- **Teaches:** explains *why* cutoff and completeness are unrecoverable later and *why* flux is the reasonableness
  test that tie-outs alone can't provide — not just a task list.
- **Safe:** doesn't hard close before recons/flux are reviewed; fixes intercompany out-of-balances before
  consolidating; notes the close discipline is framework-neutral (GAAP/IFRS differ on measurement, not on close).
