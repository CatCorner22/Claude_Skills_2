---
name: bank-statement-parsing
description: >-
  Normalizes bank statement files — BAI2, SWIFT MT940/MT942, ISO 20022 CAMT.053/CAMT.052, and CSV —
  into one reconciliation-ready schema (date, amount, direction, reference, description, balance),
  handling each format's balance and transaction codes and sign conventions. Use when ingesting,
  mapping, or troubleshooting a bank statement file before positioning or reconciliation. Triggers:
  BAI2, MT940, MT942, CAMT.053, CAMT.052, bank file, statement import, parse statement, transaction
  code, balance code, normalize statement, prior-day vs intraday.
---

# Bank statement parsing

## When to use
- Ingesting a bank statement file and mapping it into a normalized, reconciliation-ready schema.
- Troubleshooting a broken import: wrong signs, missing balances, mismatched totals, garbled codes.
- Building a code map so many banks' formats land in one consistent structure.
- Not for: matching the normalized statement to the ledger and resolving breaks → see
  `cash-management-skills:bank-reconciliation`. For building today's cash position from balances and
  flows → see `cash-management-skills:cash-positioning`.

## Do it
1. **Identify the format and whether it is prior-day or intraday.** BAI2 and CSV are text; MT940/942
   are SWIFT tag files; CAMT.053/052 are XML. **Prior-day** = final statement (BAI2, MT940,
   CAMT.053); **intraday** = current-day activity (BAI2 intraday, MT942, CAMT.052). Do not treat an
   intraday report as a closed statement — its balances are provisional.
2. **Locate the account and the statement boundaries.** Find the account identifier, currency, and
   statement/sequence number, and the record that opens and closes each account block (so multi-
   account files split correctly). See field maps in `references/statement-formats.md`.
3. **Extract the balances with their type.** Pull **opening** and **closing** balances and, where
   present, **available** balances — each carries a code telling you which it is (BAI2 type codes
   `010/015/040/045`; MT `:60F:/:62F:/:64:`; CAMT `Bal/Tp/CdOrPrtry` = `OPBD/CLBD/OPAV/CLAV`).
   Keep ledger and available balances distinct; downstream logic depends on which is which.
4. **Extract each transaction line to the target schema:**
   `value_date, booking_date, amount, direction (debit/credit), bank_transaction_code, reference,
   description, running_balance?`. Map the source's direction convention explicitly (see step 5).
5. **Resolve the sign/direction convention — the most common bug.**
   - **BAI2:** amounts are **unsigned**; the **type code** determines credit vs debit (and amounts
     are typically in **cents with no decimal point**). Use a type-code map.
   - **MT940/942 `:61:`:** a **D/C mark** gives direction; `RC`/`RD` mark **reversals**.
   - **CAMT:** `CdtDbtInd` = `CRDT`/`DBIT` gives direction; a reversal carries `RvslInd=true`.
   Normalize all three to one signed convention (e.g. inflows positive, outflows negative) and record
   the raw code alongside so nothing is lost.
6. **Map bank transaction codes to your own categories.** Group raw codes (BAI2 type codes, MT
   transaction type ID codes, CAMT `BkTxCd` domain/family/subfamily) into a stable internal set
   (wire in/out, ACH, check paid, lockbox, fee, interest, return). Keep the map in one place so a new
   bank only needs its codes added — see `references/statement-formats.md`.
7. **Validate before handing off.** Check that `opening + sum(credits) − sum(debits) = closing` for
   each account, that control totals/counts (BAI2 `49/98/99`; MT `:62F:`) reconcile, and that every
   line has a date, amount, direction, and code. A file that fails its own totals is not import-ready.

## Why / learn
Every one of these formats encodes the **same handful of facts** — an account, an opening and closing
balance, and a list of dated debits and credits with references — but each encodes them differently,
so the entire job is a **translation into one schema you control**. That reframing is the whole
skill: instead of writing reconciliation and positioning logic against five dialects, you normalize
once and everything downstream reads one shape. The details that break imports are all about
**where the meaning lives**. In BAI2 the *type code* carries the direction and the amount is an
unsigned integer of cents — read the amount as dollars or infer the sign from position and you get
garbage. In MT940 the direction is an explicit D/C **mark** and reversals hide behind `RC`/`RD`. In
CAMT it is a tidy `CdtDbtInd` element, but balances and codes are nested and typed, so you must read
the *type* attribute, not position. The other trap is **prior-day vs intraday**: a MT942/CAMT.052/BAI2
intraday report shows activity *so far today* with provisional balances — treat it as a final
statement and your position or reconciliation ties out to the wrong number. Because this normalize-
once step feeds both positioning and reconciliation, it is the **shared ingestion primitive**: get
the schema, the signs, and the balance types right here and every cash skill downstream inherits
clean data.

## Common mistakes
- Reading BAI2 amounts as dollars → they are usually cents with no decimal point. Apply the implied decimal.
- Inferring direction from sign in BAI2 → amounts are unsigned; the **type code** sets credit vs debit.
- Ignoring MT `RC`/`RD` or CAMT `RvslInd` → reversals double-count. Flag and net reversals.
- Treating intraday (MT942 / CAMT.052 / BAI2 intraday) as final → provisional balances tie out wrong.
- Confusing ledger and available balances → they differ by floats/holds. Keep both, tagged.
- Skipping control-total validation → a silently truncated file imports "successfully" but is wrong.

## Tailor to your environment
Drop your real feeds into `references/your-environment.md` (keep account numbers and any real
statement extracts in `your-environment.private.md`, which is git-ignored — commit only sanitized,
structural samples). Capture which banks send which formats, whether each feed is prior-day or
intraday and when it arrives, your banks' quirks (custom type codes, decimal handling, character
sets), and your internal category set that raw codes map to. Bank-specific code assignments vary — 
**confirm each bank's code list** rather than assuming the standard defaults.

## References
- references/statement-formats.md — field-by-field maps for BAI2, MT940/942, CAMT.053/052, and CSV, plus the normalized schema and code groups
- references/your-environment.md — your bank feeds, formats, timing, and code map (add when supplied)
