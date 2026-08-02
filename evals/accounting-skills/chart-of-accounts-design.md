# Evals — accounting-skills:chart-of-accounts-design

## 1. Positive trigger (should load the skill)
> "We're standing up a new ERP and need to design our chart of accounts. We have three legal entities and
> report a management P&L by department. How should the segments and account numbering be structured?"

Expected: skill loads; starts from the required reports; proposes a segment structure (entity, cost center,
natural account, spare); blocks natural-account ranges with gaps; defines parent/child rollups; covers
intercompany and new-account governance.

## 2. Near-miss (should NOT load this skill)
> "Book the depreciation journal entry for July and make sure the debits and credits balance."

Expected: this is drafting a journal entry, not designing or interpreting the account structure. The
`accounting-skills:journal-entries` skill should handle it. If chart-of-accounts-design loads instead,
tighten the description and cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** designs orthogonal segments, ties the design to the required reports, sets natural-account
  ranges with growth gaps, defines rollup hierarchies (post to detail, report from parents), and addresses
  intercompany/clearing accounts and new-account governance.
- **Teaches:** explains *why* the COA is the backbone of what you can report on and *why* orthogonal segments are
  the axes you pivot on — not just a list of accounts.
- **Safe:** notes that COA structure is a management choice under both GAAP and IFRS (frameworks constrain
  statement classification/disclosure), without over-claiming a prescribed format; steers new requests toward
  segment values before new accounts.
