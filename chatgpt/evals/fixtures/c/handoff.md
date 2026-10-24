# Handoff

Corrected result.csv contains 2 settled unique transactions for October 22, 2026 UTC. **Independently recomputed sum: USD 31.00** (10.25 + 20.75). The read-only reviewer independently parsed input.csv and confirmed the saved CSV matches its recomputation exactly.

Exact scope: all 5 supplied source records; first occurrence per id before filtering; exact Settled status; UTC interval [2026-10-22T00:00:00Z, 2026-10-23T00:00:00Z); amended transaction_id,amount_usd header/order; two-decimal amounts; unique output ids; LF CSV bytes; source/output counts, total, decisions and hashes. The reviewer executed 12 read-only assertions, all passing with exit 0. This verifies these fixture records, not a general transformation implementation or unprovided cases such as conflicting duplicates or non-Z timezone offsets.

Source evidence: input.csv line 2 includes A at the opening midnight (10.25); line 3 includes the first B (20.75); line 4 is the duplicate B; line 5 is C at the excluded following midnight; line 6 is Pending D. request.md lines 7–9 supply the UTC and final-schema amendment. verification.json records row decisions and SHA-256 hashes; independent-review.md records the fresh review; requirement-ledger.md and qc-sweep.md record requirements and category checks.

Input preservation: the builder captured input.csv and request.md SHA-256 values before editing and matched them after editing. The independent reviewer verified current files agree with those recorded hashes; it did not observe their pre-edit state.

All verification was local to the fixture files. No bank or provider was contacted; no external settlement validation was performed.
