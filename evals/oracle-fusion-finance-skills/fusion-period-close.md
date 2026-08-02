# Evals — oracle-fusion-finance-skills:fusion-period-close

## 1. Positive trigger (should load the skill)
> "It's Day 2 of close and Fusion won't let us close the AP period — and GL is showing
> untransferred subledger accounting. What order should we be doing this in?"

Expected: skill loads; establishes subledgers-before-GL sequencing; runs the AP exception sweep
(unvalidated invoices, unaccounted transactions, in-flight PPRs); Create Accounting final +
transfer; confirms no unposted GL journals; then control-account reconciliations before closing
GL.

## 2. Near-miss (should NOT load this skill)
> "Help me design our month-end close checklist and decide which accruals we should book."

Expected: close *content and checklist design* — `accounting-skills:month-end-close`. If this
skill loads, sharpen the Fusion-mechanics framing.

## 3. Quality rubric
A good response:
- **Does the task:** unblocks the module close via its exception reports, sequences the close
  correctly, and proves subledger = GL control account before sign-off.
- **Teaches:** close order as data dependency, period statuses as controls, why closing around
  unaccounted transactions is dishonest, and why reopens are expensive.
- **Safe:** treats Permanently Closed as irreversible, logs reopens as control exceptions, and
  never suggests manual journals to control accounts as a shortcut.
