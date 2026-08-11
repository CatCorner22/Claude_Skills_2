# Evals — sponsored-projects-ar-skills:revenue-billing-reconciliation

## 1. Positive trigger (should load the skill)
> "Our unbilled receivable account shows $2.3M but I can't substantiate it — reconcile PPM
> recognized revenue against what we've actually billed by contract, and check nothing is
> over the sponsor funding limits."

Expected: skill loads; builds the per-contract waterfall (revenue − net billed, credits/
rebills netted, same as-of date both streams); separates positives (unbilled) from negatives
(deferred); ties Σ positives to the GL unbilled account and decomposes any difference;
runs funding-ceiling checks on both streams; explains variances by cause with the aged
unexplained unbilled flagged for escalation.

## 2. Near-miss (should NOT load this skill)
> "Why are these invoices stuck in Error status and what's sitting in Ready to Bill?"

Expected: pipeline operations — `sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon`.
If this skill loads instead, sharpen the accounting-vs-operations split.

## 3. Quality rubric
A good response:
- **Does the task:** per-contract identity computed, GL tie-out both sides (unbilled and
  deferred), funding-limit flags, and cause-decomposed variance explanations.
- **Teaches:** revenue and billing as two designed-independent streams off one contract, the
  unbilled account as the ledger's memory of the divergence, and per-contract-type normals.
- **Safe:** same as-of date for both streams, credits netted by linked transaction, no
  netted-total substantiation hiding offsetting errors, over-billing treated as refund
  exposure not noise.
