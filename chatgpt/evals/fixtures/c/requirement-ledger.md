# Requirement ledger

| Requirement / source | Acceptance check | Owner | State / evidence |
| --- | --- | --- | --- |
| request.md: finish draft in place; preserve inputs | Correct result.csv and handoff.md; input hashes unchanged | Builder | Done; before/after hashes recorded in verification.json and handoff.md |
| request.md: settled unique transactions, first record per id | Deduplicate in source order, then require Settled | Builder / reviewer | Done; input.csv lines 2–6; verification.json decisions; independent-review.md |
| Later amendment: October 22, 2026 UTC | Include 00:00:00Z; exclude October 23 00:00:00Z | Builder / reviewer | Done; verification.json UTC window; independent source recomputation |
| Later amendment: transaction_id,amount_usd, two decimals | Exact header/order and amount strings | Builder / reviewer | Done; result.csv exact-byte read-back |
| Earlier id,usd header | Replaced by later amendment | Builder | Superseded |
| request.md: independently recomputed sum, exact scope, source evidence | Read-only reviewer recomputes from raw CSV; document scope and limits | Reviewer / builder | Done; USD 31.00; handoff.md; independent-review.md |
| request.md: brief ledger and QC sweep; no provider-contact claim | Review documents and claims | Builder / reviewer | Done; this ledger, qc-sweep.md, handoff.md |
