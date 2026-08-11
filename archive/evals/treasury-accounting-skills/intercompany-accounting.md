# Evals — treasury-accounting-skills:intercompany-accounting

## 1. Positive trigger (should load the skill)
> "Consolidation is blocked — our intercompany eliminations don't net to zero and entity B's
> payable to A is $340k off from A's receivable. Untangle this."

Expected: skill loads; builds/uses the pairwise IC matrix; decomposes the difference in order
(timing → FX rate mismatch → error → dispute) and fixes at the broken pair rather than booking
a consolidation plug; checks IC activity isn't hiding in trade AR/AP; recommends symmetric
booking and a settlement calendar to stop recurrence.

## 2. Near-miss (should NOT load this skill)
> "Design our multilateral netting cycle so subsidiaries stop wiring each other money every
> week."

Expected: cash settlement machinery — `cash-management-skills:intercompany-cash-netting`. If
this skill loads, tighten the accounting/reconciliation framing.

## 3. Quality rubric
A good response:
- **Does the task:** matrix built from trial-balance extracts, difference decomposed and
  resolved at the entity that erred, eliminations then proven to net.
- **Teaches:** why IC decays without external counterparty pressure (and how each discipline
  substitutes for it), eliminations as a proof not a procedure, and the transfer-pricing/
  agreement layer's tax audience.
- **Safe:** never plugs elimination differences, uses one FX rate source for both sides, flags
  undocumented or interest-free IC loans, keeps agreements and balances out of committed files.
