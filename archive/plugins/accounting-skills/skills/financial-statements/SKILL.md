---
name: financial-statements
description: >-
  Reads and builds the three core financial statements — balance sheet, income statement, and cash
  flow statement (direct and indirect) — and uses how they articulate to tie them out. Use when
  analyzing, preparing, or tying out the statements, converting accrual results to cash, or building a
  cash flow statement by the indirect method starting from net income. Triggers: financial statements,
  balance sheet, income statement, P&L, cash flow statement, statement of cash flows, indirect method,
  accrual vs cash, articulation, tie out.
---

# Financial statements

## When to use
- Reading, preparing, or reviewing a **balance sheet**, **income statement (P&L)**, or **cash flow statement**.
- Building a cash flow statement by the **indirect** (or direct) method, or converting accrual results to cash.
- **Tying out** the three statements to each other and finding why they do not articulate.
- Not for: computing and interpreting **ratios** (liquidity, leverage, margins, returns) → see
  `accounting-skills:financial-ratios`. For drafting the underlying **journal entries** that feed the
  statements → see `accounting-skills:journal-entries`.

## Do it
1. **Fix the reporting boundary.** State the entity, the period, and the basis (accrual vs. cash). The **balance
   sheet** is a snapshot *as of* a date; the **income statement** and **cash flow statement** cover a *period*
   between two balance-sheet dates.
2. **Build/read the income statement (accrual).** Revenue − cost of goods sold = gross profit; − operating
   expenses = operating income; ± non-operating items (interest, other) = pre-tax income; − income tax = **net
   income**. Recognize revenue when earned and expense when incurred, regardless of cash timing.
3. **Build/read the balance sheet.** Classify **Assets = Liabilities + Equity**, split current vs. non-current.
   Equity carries **retained earnings = beginning retained earnings + net income − dividends**. The two sides
   must be equal — that equality is the statement's built-in check.
4. **Build the cash flow statement in three sections.** **Operating** (cash from the core business),
   **investing** (buying/selling long-term assets), **financing** (debt and equity, dividends). By the
   **indirect method**, operating starts from **net income**, adds back non-cash charges (depreciation,
   amortization, stock comp), and adjusts for **changes in working capital**; the **direct method** instead
   lists actual operating cash receipts and payments. Both produce the *same* operating cash total. See
   `references/articulation-and-cash-flow.md`.
5. **Apply the working-capital signs (indirect method).** An **increase** in a current asset (AR, inventory,
   prepaids) **uses** cash → subtract; a **decrease** frees cash → add. An **increase** in a current liability
   (AP, accrued) is a **source** of cash → add; a **decrease** → subtract.
6. **Articulate and tie out.** Run the four checks: (a) net income (IS) rolls into retained earnings (BS);
   (b) change in cash on the CFS = ending BS cash − beginning BS cash; (c) ending cash on the CFS = the cash
   line on the BS; (d) the balance sheet balances (A = L + E). If any check fails, the break is your finding —
   trace it, do not force it.
7. **Convert accrual to cash where asked.** Take an accrual figure and adjust for the working-capital change
   behind it (e.g. cash collected = revenue − increase in AR). This is the same mechanic the indirect method
   uses line by line.

## Why / learn
The three statements are **one connected system**, not three separate documents — and their connection is exactly
how you check them. Each answers a different question about the same business: the income statement asks *how
profitable was the period*, the balance sheet asks *what does the entity own and owe at a moment*, and the cash
flow statement asks *where did the cash actually go*. They **articulate**: net income earned on the income
statement flows into retained earnings on the balance sheet, and the cash flow statement explains the entire move
in the balance sheet's cash line from one date to the next. That is why a correct set of statements is
self-tying — if net income does not land in equity, or the CFS does not reconcile beginning to ending cash, or
the balance sheet does not balance, something is wrong and the articulation *tells you where to look*. The cash
flow statement earns its place because **profit is not cash**: accrual accounting recognizes revenue when earned
and expense when incurred, so a profitable company can still run out of cash, and a loss-making one can be cash-rich.
The indirect method makes this visible by starting at net income and walking every non-cash and timing difference
back to cash — a large profit alongside a big build-up in receivables is the classic warning the CFS surfaces.
Under **US GAAP and IFRS the articulation is identical**; the differences are presentational and classificational —
IFRS calls the balance sheet the *statement of financial position*, and the two frameworks differ on where interest
and dividends paid/received may sit on the cash flow statement (US GAAP largely fixes them; IFRS allows a policy
choice). Reconcile to the classifications your accounting policy uses; the tie-out logic does not change.

## Common mistakes
- Treating the statements as independent → you lose the tie-out. If they do not articulate, one of them is wrong.
- Reading net income as cash → profit and cash differ by non-cash charges and working-capital timing. Use the CFS.
- Wrong working-capital signs in the indirect method → an asset *increase* subtracts, a liability *increase* adds.
  Getting the sign backwards is the most common CFS error.
- Forgetting dividends in retained earnings → RE = beginning RE + net income − **dividends**, not just + net income.
- Mixing bases within one statement (some lines cash, some accrual) → pick one basis and state it.
- Classifying a financing or investing cash flow as operating (or vice versa) → e.g. buying equipment is investing,
  not an operating expense outflow. Section placement changes what the statement tells a reader.

## Tailor to your environment
Record your real setup in `references/your-environment.md` (or `your-environment.private.md` if it names real
figures or entity data — that suffix is git-ignored, so raw data never gets committed). Capture your reporting
framework (US GAAP / IFRS / other), your statement templates and line-item mapping, whether you present the cash
flow statement by the direct or indirect method, your policy for classifying interest and dividends, your period
calendar, and where each statement is generated. The generic steps then map onto your actual line items and policy.

## References
- references/articulation-and-cash-flow.md — statement structures, the indirect-method template and working-capital signs, the direct method, the articulation/tie-out checklist, and accrual-to-cash conversion
- references/your-environment.md — your framework, templates, cash-flow method, and classification policy (add when supplied)
