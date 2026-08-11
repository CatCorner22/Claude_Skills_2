# Evals — accounting-skills:account-reconciliations

## 1. Positive trigger (should load the skill)
> "Reconcile our prepaid insurance GL account to the amortization schedule for June. The GL says 21,300
> and my schedule says 20,800 — help me figure out the difference and whether it's a problem."

Expected: skill loads; states what the rec must prove; treats the amortization schedule as the independent
support; isolates the 500 difference as a reconciling item; classifies it (timing vs error vs unsupported)
and ages it rather than plugging; suggests a roll-forward since prepaids are activity-driven.

## 2. Near-miss (should NOT load this skill)
> "My bank statement shows 482,100 but the GL cash account says 479,650 — help me reconcile the bank and
> find the outstanding items."

Expected: this is a bank statement vs. book cash reconciliation (two records of the same cash), not a GL
balance-to-support rec. The `cash-management-skills:bank-reconciliation` skill should handle it. If
account-reconciliations loads instead, tighten the description and the "Not for" cross-link — the two are
deliberately distinct.

## 3. Quality rubric
A good response:
- **Does the task:** builds/uses independent support, computes GL − supported, classifies and ages reconciling
  items, picks roll-forward vs point-in-time appropriately, and notes risk rating / preparer-reviewer controls.
- **Teaches:** explains the *assurance* purpose (a balance-sheet balance carries forward, so an error persists
  until disproven) and *why* an unexplained item is a finding — not just the arithmetic.
- **Safe:** never plugs the difference; requires support independent of the GL; keeps preparer and reviewer
  separate; notes the discipline is the same under GAAP and IFRS while measurement of the balance may differ.
