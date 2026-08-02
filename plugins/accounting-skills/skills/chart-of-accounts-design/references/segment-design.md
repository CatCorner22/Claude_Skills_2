# Segment design and hierarchies (reference)

## Contents
- The accounting flexfield / segment model
- Common segments and what each answers
- Natural-account ranges
- Parent/child hierarchies and rollups
- Intercompany and clearing accounts
- Anti-patterns

## The accounting flexfield / segment model
A COA account is a **string of independent segments** — the "accounting flexfield" in Oracle terminology; the same
idea appears as dimensions/subaccounts in other ERPs. Each segment has its own **value set** (the list of valid
values) and answers one question. A posted amount carries a value for every segment, so the string is a full
coordinate for that dollar. Example string:

```
  01    -   4200    -   6100   -   50000   -   0000
 Entity     Cost ctr   Region   Natural    Future(spare)
```

## Common segments and what each answers
| Segment | Question it answers | Notes |
|---|---|---|
| Entity / company | Whose books? | Legal entity or reporting unit; drives consolidation & IC elimination |
| Cost center / department | Who is responsible? | The P&L owner; often the management-reporting axis |
| Natural account | What is it? | The one required segment; carries the account type |
| Location | Where? | Optional; site/geography reporting |
| Product / line of business | For what offering? | Optional; margin-by-product analysis |
| Project | For what initiative? | Optional; often better as a subledger/project module dimension |
| Intercompany | Trading with which affiliate? | Enables clean elimination |
| Future / spare | (reserved) | Hold at least one spare segment for needs you can't foresee |

Design principle: **orthogonality** — no segment should encode another's meaning. If "department" is inferable
from the natural account number, you have lost the ability to report the two independently.

## Natural-account ranges (illustrative)
| Range | Type | Normal balance |
|---|---|---|
| 1xxxx | Assets | Debit |
| 2xxxx | Liabilities | Credit |
| 3xxxx | Equity | Credit |
| 4xxxx | Revenue | Credit |
| 5xxxx | COGS | Debit |
| 6xxxx–8xxxx | Operating expense | Debit |
| 9xxxx | Other income/expense, tax | varies |

Leave gaps inside each range so new accounts slot in without renumbering.

## Parent/child hierarchies and rollups
- **Post to detail (child) accounts; report from summary (parent) accounts.** A parent is a defined node in a
  rollup tree, not a spreadsheet subtotal.
- Build one tree per reporting view you need (statutory statements, management P&L, tax). A detail account can
  roll up differently in different trees.
- Example rollup: `61010 Salaries`, `61020 Benefits` → `Payroll` → `Operating expenses` → `Total expenses`.
- Rollups let the same detail generate several statements consistently — change the tree, not the postings.

## Intercompany and clearing accounts
- **Intercompany** receivable/payable accounts must be set up as mirror pairs across entities so equal-and-opposite
  balances **eliminate** on consolidation. A mismatch surfaces as an intercompany out-of-balance in close.
- **Clearing / suspense** accounts are temporary. They hold in-transit or unallocated amounts and must clear to
  **zero** and be reconciled every period; a growing clearing balance is a red flag.

## Anti-patterns
- "Smart-numbering" a segment inside the natural account (dept, region, or entity baked into the account number).
- One giant natural-account list with no segments (forces a new account for every department × account combination).
- Posting to parent accounts (double counts and breaks the tree).
- Ad-hoc account creation with no owner, definition, or hierarchy assignment (COA sprawl).
