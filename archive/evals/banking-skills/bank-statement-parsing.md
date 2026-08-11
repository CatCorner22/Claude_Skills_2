# Evals — banking-skills:bank-statement-parsing

## 1. Positive trigger (should load the skill)
> "Our import of the bank's BAI2 file is showing every amount 100x too big and some debits as
> credits. Can you help me map the file correctly?"

Expected: skill loads; identifies the BAI2 implied-decimal (cents) issue and the type-code-driven
direction convention (amounts unsigned; type code sets debit/credit); maps to the normalized schema;
points to the field maps in `references/statement-formats.md`; recommends control-total validation.

## 2. Near-miss (should NOT load this skill)
> "The statement is parsed fine now — help me match these transactions against the GL and figure out
> the $2,450 unreconciled difference."

Expected: parsing is done; this is reconciliation, handled by
`cash-management-skills:bank-reconciliation`. If bank-statement-parsing loads instead, tighten the
"Not for" cross-link. (Positioning from the parsed balances would go to `cash-positioning`.)

## 3. Quality rubric
A good response:
- **Does the task:** identifies the format, extracts balances with their type and transactions to a
  normalized schema (date/amount/direction/reference/description/balance), resolves the sign/direction
  convention, and maps bank codes to internal categories.
- **Teaches:** explains that every format encodes the same facts differently so you normalize once,
  and why prior-day vs intraday and ledger vs available balances must be kept distinct.
- **Safe:** validates opening + credits − debits = closing and control totals before handing off;
  flags reversals so they aren't double-counted.
