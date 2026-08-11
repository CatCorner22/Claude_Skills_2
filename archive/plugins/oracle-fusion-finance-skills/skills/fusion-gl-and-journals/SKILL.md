---
name: fusion-gl-and-journals
description: >-
  Works General Ledger in Oracle Fusion Cloud — reads the ledger and chart-of-accounts structure
  (segments, value sets, hierarchies, cross-validation rules), creates manual and spreadsheet
  (ADFdi) journals, routes them through approval, posts them, and troubleshoots unposted or
  rejected journals. Use when entering or fixing a journal in Fusion GL, explaining a ledger/COA
  setup, or diagnosing why a journal won't post. Triggers: fusion journal, GL journal entry,
  create journal in fusion, ADFdi journal, spreadsheet journal, journal approval, post journal,
  journal won't post, cross-validation rule, chart of accounts segments, fusion ledger.
---

# Oracle Fusion GL and journal entry

## When to use
- Creating, approving, posting, or fixing a journal in Oracle Fusion Cloud General Ledger
  (manual UI entry or the ADFdi "Create Journal" spreadsheet).
- Understanding a ledger's structure: chart of accounts segments, value sets, hierarchies,
  cross-validation rules, and how they gate what you can book.
- Not for: bulk journal loads through the GL interface → see
  `oracle-fusion-finance-skills:fusion-fbdi-data-loading`. For debit/credit logic itself → see
  `accounting-skills:journal-entries`.

## Do it
1. **Read the ledger context first.** A journal lands in one **ledger** (a 4-C combination of
   Chart of accounts + Calendar + Currency + accounting Convention). Confirm which ledger and
   period you're booking into (Navigator → General Accounting → Journals), and that the period
   status is **Open** — journals cannot post to Closed or Never Opened periods.
2. **Build the account combination segment by segment.** A Fusion account is an ordered string of
   COA segments (typically company/entity, cost center, natural account, intercompany, and one or
   more "future"/detail segments). Each segment draws from a **value set**; the natural-account
   segment carries the account type (asset/liability/expense/revenue) that drives balance behavior.
   Ask for the segment order and separator if you don't know it — never guess positions.
3. **Expect cross-validation rules (CVRs) to reject bad combinations.** CVRs block combinations
   like a balance-sheet account with a live cost center. If entry fails with a combination error,
   read the CVR message: fix the *combination*, don't hunt for a different screen.
4. **Choose the entry route by volume.**
   - A few lines → **Create Journal** UI: journal name, ledger, period, category (source stays
     "Manual"), then lines with account, debit/credit, description.
   - Dozens–hundreds of lines → **Create Journal in Spreadsheet** (ADFdi Excel add-in): download
     the workbook, fill lines, and submit from Excel; it validates combinations on upload.
   - Recurring/allocations → recurring journal or allocation rules, not re-keying.
5. **Balance it before saving.** Total debits equal total credits per balancing segment value —
   Fusion enforces balancing by the balancing segment (usually company/entity); an entry spanning
   two companies will generate **intercompany balancing lines** automatically if intercompany
   balancing is enabled. Don't fight auto-generated lines; verify them.
6. **Route and post.** If journal approval is enabled, submitting sends it via BPM workflow
   (approval rules usually key on amount/category/source); it posts only after approval. Post
   manually (Actions → Post) or let AutoPost pick it up. Confirm status moves
   **Unposted → (Approval) → Posted**, then verify the impact in the trial balance or
   Account Inspector.
7. **Troubleshoot unposted journals** with the status and the posting-error message: period not
   open, unbalanced entry, invalid/end-dated account combination, failed CVR, or stuck approval.
   `references/journal-troubleshooting.md` maps the common errors to fixes.

## Why / learn
Fusion GL is a *rules engine around a string*: everything about a journal reduces to whether each
line's segment combination is valid (value sets + CVRs), whether the entry balances by the
balancing segment, and whether the period is open. Once you internalize that, every posting
failure becomes a lookup, not a mystery — the error always names which of the three gates failed.
The segment design also explains why finance teams guard the natural-account and company segments:
account type drives how balances roll into statements, and the balancing segment defines the legal
entity boundary that intercompany lines protect. ADFdi exists because the UI and the interface
table are two doors into the same validation engine — the spreadsheet is not a bypass, it just
batches the same checks, which is why a combination that fails online fails there too.

## Common mistakes
- Booking into the wrong ledger or a closed period → check ledger and period status before entering lines.
- Guessing segment order or reusing a combination from another entity → ask for the COA layout; validate one line first.
- Treating a CVR rejection as a system bug → the rule is the control; change the combination or request a rule review.
- Keying 200 lines in the UI → use the ADFdi spreadsheet journal; same validation, far less error surface.
- Forgetting approval workflow → the journal sits "Pending approval," not lost; check BPM worklist before re-entering.
- Deleting auto-generated intercompany balancing lines → they keep each company in balance; verify, don't remove.

## Tailor to your environment
Record your real GL layout in `references/your-environment.md` (or the git-ignored
`your-environment.private.md`): ledger names, COA segment order and labels, balancing segment,
key natural-account ranges, journal categories you use, whether approval is on and its thresholds.
Keep it structural — **never commit real company codes tied to real balances or live account
combinations with amounts**.

## References
- references/journal-troubleshooting.md — posting/approval errors mapped to causes and fixes
- references/your-environment.md — your ledgers, segment order, categories, approval rules (fill in)
