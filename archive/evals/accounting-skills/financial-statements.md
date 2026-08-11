# Evals — accounting-skills:financial-statements

## 1. Positive trigger (should load the skill)
> "We're profitable but cash keeps dropping. Help me build the cash flow statement by the indirect method
> from net income and tie it back to the balance sheet so I can see where the cash went."

Expected: skill loads; builds the CFS in operating/investing/financing sections; starts operating from net
income, adds back non-cash charges, and adjusts working capital with the correct signs (AR/inventory
increases subtract, AP increases add); runs the articulation checks (net income → retained earnings; change
in cash = ending − beginning BS cash; ending CFS cash = BS cash; A = L + E); explains that profit ≠ cash.

## 2. Near-miss (should NOT load this skill)
> "From these statements, compute the current ratio, gross margin, and return on equity, and tell me whether
> liquidity is improving year over year."

Expected: this is ratio computation and interpretation, which belongs to `accounting-skills:financial-ratios`,
not building or tying out the statements themselves. If financial-statements loads instead, tighten the
description and the "Not for" cross-link. (Reading/building the statements and analyzing them via ratios are
deliberately separate skills.)

## 3. Quality rubric
A good response:
- **Does the task:** produces or reads the correct statement structure; builds the CFS with the right sections
  and working-capital signs; performs the accrual-to-cash / articulation checks; localizes any tie-out break.
- **Teaches:** explains that the three statements are one articulating system and that articulation *is* the
  check — net income lands in retained earnings, the CFS explains the full move in balance-sheet cash — and why
  profit is not cash, rather than just presenting numbers.
- **Safe:** uses the correct working-capital signs; includes dividends in retained earnings; keeps one basis per
  statement; places investing/financing flows out of the operating section; notes GAAP/IFRS differ only on
  classification and presentation while the tie-out logic is identical; never plugs a tie-out difference.
