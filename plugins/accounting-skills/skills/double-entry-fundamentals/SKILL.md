---
name: double-entry-fundamentals
description: >-
  Applies the accounting equation, debit/credit rules, normal balances, T-accounts, and the
  accounting cycle to record a transaction correctly and prove the books balance. Use when unsure
  how to book a transaction, which side is the debit and which the credit, what an account's normal
  balance is, or how the accounting cycle flows from journal to ledger to trial balance to statements.
  Triggers: double entry, debit, credit, accounting equation, normal balance, T-account, trial
  balance, accounting cycle, assets liabilities equity.
---

# Double-entry fundamentals

## When to use
- Deciding how to book a transaction — which accounts it touches and which side (debit or credit) each takes.
- Checking an account's **normal balance**, posting to **T-accounts**, or reading a **trial balance**.
- Understanding where a step sits in the **accounting cycle** (journal → ledger → trial balance → statements).
- Not for: drafting a specific standard/accrual/deferral/reversing **journal entry** → see
  `accounting-skills:journal-entries`. For reading or building the resulting **financial statements** → see
  `accounting-skills:financial-statements`.

## Do it
1. **Anchor on the accounting equation.** Everything ties back to **Assets = Liabilities + Equity**. Revenue,
   expenses, and owner draws/dividends are just movements *inside* equity, so the working form is
   **A = L + E + (Revenue − Expenses − Draws/Dividends)**. A transaction is valid only if it leaves this equal.
2. **Classify each account you touch into one of five types.** Asset, liability, equity, revenue, or expense.
   The type — not intuition — sets the normal balance. See `references/debit-credit-rules.md`.
3. **Look up the normal balance and which side increases it.** **Debit-normal:** assets, expenses (and
   draws/dividends). **Credit-normal:** liabilities, equity, revenue. You *increase* an account with an entry
   on its normal side and *decrease* it on the other side. Contra accounts flip (accumulated depreciation is a
   credit-normal contra-asset).
4. **Find both sides and book them so debits = credits.** Every transaction hits **at least two** accounts.
   Ask "what did the business receive, and what did it give up or owe?" — one becomes a debit, the other a
   credit. Total debits must equal total credits to the cent.
5. **Post to the ledger / T-accounts.** For each account draw a T: debits on the left, credits on the right.
   Post each entry line to its account and net the two sides to get the running balance.
6. **Follow the accounting cycle in order.** transaction → journal entry → post to ledger → **unadjusted trial
   balance** → adjusting entries → **adjusted trial balance** → financial statements → closing entries →
   post-closing trial balance. Each period repeats it.
7. **Prove it with a trial balance.** List every account's ending balance in a debit or credit column and total
   each column — they **must** be equal. If they are not, a posting is wrong, one-sided, or transposed. A
   balanced trial balance is *necessary but not sufficient* (see Common mistakes).

## Why / learn
Double-entry is **self-checking**, and that is the whole reason it has survived for 500 years. Every transaction
is recorded as two equal and opposite effects — a debit and a matching credit — precisely so the accounting
equation stays in balance no matter what you book. "Debits equal credits" is not an arbitrary bookkeeping rule;
it is the arithmetic expression of **A = L + E staying true**. If you buy a $10,000 machine with cash, one asset
rises and another falls by the same $10,000, so the equation never moves; if you buy it on credit, an asset and a
liability both rise by $10,000, and again it balances. Because the two sides must always agree, the system
catches a whole class of errors on its own: a one-sided posting or a transposed figure shows up immediately as a
trial balance that does not tie. The normal-balance rules fall straight out of the equation — debits raise the
left side (assets, expenses), credits raise the right side (liabilities, equity, revenue) — which is why memorizing
"debit = left, credit = right" plus the equation beats memorizing dozens of cases. This is the **foundation the
other accounting skills build on**: a journal entry is just an application of these rules, a trial balance is the
proof step, and the financial statements are the equation and the period's flows re-expressed for a reader. The
mechanics are identical under US GAAP and IFRS — double-entry is bookkeeping, not a reporting framework — so the
model transfers everywhere.

## Common mistakes
- Thinking debit always means "decrease" and credit "increase" (or vice versa) → the direction depends on the
  account type. Debit *increases* assets/expenses; credit *increases* liabilities/equity/revenue.
- Reading "debit/credit" like a bank statement → a bank *credits* your account when it adds cash because on the
  bank's books your deposit is a liability. From your books, cash is a debit-normal asset. Opposite perspective.
- Trusting a balanced trial balance as proof of correctness → it will still balance through an omitted entry, a
  posting to the wrong account, or two errors that offset. It proves arithmetic, not judgment.
- Recording only one side of a transaction → the entry cannot post and the trial balance breaks. Always find both.
- Confusing an account's **normal balance** with the side a *specific* transaction uses → a credit to Cash is
  normal (a decrease), even though Cash is debit-normal.

## Tailor to your environment
Record your real setup in `references/your-environment.md` (or `your-environment.private.md` if it names real
account numbers or entity data — that suffix is git-ignored, so raw data never gets committed). Capture your GL/ERP,
your chart-of-accounts numbering, which accounts are contra, your fiscal calendar and cutoff, and whether you close
monthly or only at year-end. The generic rules above then map onto your actual accounts and cycle.

## References
- references/debit-credit-rules.md — the five account types, normal balances, contra accounts, worked T-account postings, a trial balance, and the accounting cycle
- references/your-environment.md — your GL/ERP, chart of accounts, and fiscal calendar (add when supplied)
