---
name: chart-of-accounts-design
description: >-
  Designs, extends, and interprets a chart of accounts and its segments — entity/company, cost center,
  natural account, and others — with parent/child hierarchies and rollups for reporting. Use when
  designing or restructuring a COA, adding or mapping accounts, defining segments, or making sense of an
  existing account structure. Triggers: chart of accounts, COA, account segments, accounting flexfield,
  natural account, cost center, account hierarchy, rollup, account mapping, new account request.
---

# Chart of accounts design

## When to use
- Designing a new chart of accounts or restructuring an existing one for a new entity, ERP, or reporting need.
- Defining the segments (entity/company, cost center, natural account, and others) and their hierarchies.
- Adding, mapping, or rationalizing accounts, or governing new-account requests.
- Making sense of an unfamiliar COA — what a given account string means and how it rolls up.
- Not for: drafting the entries that post into these accounts → see `accounting-skills:journal-entries`.
  For the ratios your COA structure needs to support → see `finance-skills:financial-ratios`.

## Do it
1. **Start from the reports you must produce.** List the required outputs first — statutory financials,
   management P&L by department, segment reporting, tax, board packs. The COA has to be able to *slice* to
   each of these; design backward from them, not forward from a blank account list.
2. **Design the segment structure (the account string).** Model the COA as an ordered set of independent
   **segments**, each answering a different question — commonly:
   - **Entity / company** — *whose* books (legal entity or reporting unit; drives consolidation).
   - **Cost center / department** — *who is responsible* (the P&L owner).
   - **Natural account** — *what* it is (cash, AR, revenue, salaries). The one required segment.
   - Optional: **location, product, project, intercompany, future** (a spare segment held in reserve).
   Keep segments **orthogonal**: one segment should never encode another's meaning (don't bake the department
   into the natural account number). This independence is the whole point of the flexfield — see
   `references/segment-design.md`.
3. **Define natural-account ranges by type.** Block out ranges so type is legible from the number, e.g.
   1xxxx assets, 2xxxx liabilities, 3xxxx equity, 4xxxx revenue, 5xxxx–9xxxx expense. Leave gaps inside each
   range for growth so you never have to renumber.
4. **Build parent/child hierarchies and rollups.** Post only to **child (detail)** accounts; report from
   **parent (summary)** accounts. Define rollup trees (e.g. detail expense accounts → "Operating expenses" →
   "Total expenses") so every reporting line is a defined parent, not a spreadsheet sum maintained by hand.
5. **Set up clearing, suspense, and intercompany accounts deliberately.** Clearing/suspense accounts are
   *temporary* holding accounts that must clear to zero (and get reconciled) — see
   `accounting-skills:account-reconciliations`. Intercompany accounts must mirror across entities so they
   **eliminate** cleanly in consolidation.
6. **Govern new accounts.** Before creating an account, check whether an existing account + a segment value
   (a new cost center, a new project) already answers the need — most "new account" requests are really new
   *dimension values*. Require an owner, a definition, and a mapping to the reporting hierarchy for every new
   natural account. This is what keeps the COA from sprawling.
7. **Map between systems when consolidating or migrating.** Maintain a crosswalk from source accounts to the
   target COA, note the many-to-one collapses, and reconcile trial-balance totals by type before and after so
   nothing is lost or reclassified silently.

## Why / learn
The chart of accounts is the **backbone of everything you can report on**: an amount that was never captured on
the right segment can never be reported on that dimension, no matter how good the downstream tools are. That is
why design starts from the reports and why segments matter more than account count — segments are the *axes* you
can pivot on. Think of the account string as a coordinate: entity × cost center × natural account locates every
dollar in a space, and each segment is a dimension you can filter, sum, or drop. Keeping segments **orthogonal**
is what lets you answer questions the designers never anticipated (spend by product *across* entities), because
any combination of coordinates is addressable. **Parent/child hierarchies** are how that coordinate space turns
into statements: posting to detail and reporting from parents means the financials are generated from a defined
tree rather than re-derived by hand each month, so they stay consistent and auditable. The discipline around
**new accounts** exists because a COA degrades by accretion — every redundant or ambiguous account makes mapping,
consolidation, and analysis harder forever — so the cheapest COA decision is the account you *don't* create.
Under both US GAAP and IFRS the COA structure is a management choice, not a prescribed format; the frameworks
constrain *classification and disclosure* of the statements, so build the COA granular enough to satisfy the
strictest disclosure you face and let hierarchies roll it up to each required view.

## Common mistakes
- Encoding one segment inside another (department baked into the account number) → you lose the ability to slice
  independently. Keep segments orthogonal.
- Designing the account list before the target reports → the COA can't produce a view no one designed for. Start from reports.
- No gaps in numbering ranges → you renumber (and remap history) the first time you add an account. Leave room.
- Posting to parent/summary accounts → breaks the rollup and double-counts. Post to detail, report from parents.
- Creating a new natural account when a new segment value would do → COA sprawl. Check dimensions first.
- Intercompany accounts that don't mirror across entities → they won't eliminate in consolidation. Design them in pairs.
- Clearing/suspense accounts with no owner or reconciliation → they silently accumulate. Assign and reconcile them.

## Tailor to your environment
This skill is only as useful as its fit to *your* structure, so capture your real segment design in
`references/your-environment.md` (or `your-environment.private.md` if it holds real entity/account numbers — that
suffix is git-ignored). Record your segment order and widths, the value sets for each segment, your natural-account
ranges, your rollup hierarchies, your intercompany and clearing accounts, and your new-account request process. Once
that is filled in, the generic steps map directly onto your accounting flexfield and reporting trees.

## References
- references/segment-design.md — the accounting-flexfield / segment model, sample structures, and hierarchy patterns
- references/your-environment.md — your real segment structure, value sets, ranges, and governance (add when supplied)
