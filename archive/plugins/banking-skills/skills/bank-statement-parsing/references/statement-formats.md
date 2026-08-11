# Bank statement formats (reference)

Field-by-field maps for the common bank statement formats and the normalized schema they all target.
Bank-specific transaction/type codes vary — **confirm each bank's code list**.

## Contents
- Normalized target schema
- BAI2
- SWIFT MT940 (prior-day) and MT942 (intraday)
- ISO 20022 CAMT.053 / CAMT.052
- CSV
- Balance types across formats
- Direction / sign conventions
- Code groups (internal category map)
- Validation checks

## Normalized target schema
Every format normalizes to this shape (one balance row set + N transaction rows per account):

| Field | Meaning |
|-------|---------|
| `account_id`, `currency` | Which account and currency the block is for |
| `statement_no`, `as_of_date` | Statement/sequence number and statement date |
| `opening_balance`, `closing_balance` | Ledger balances (with a `balance_type` tag) |
| `opening_available`, `closing_available` | Available/collected balances if provided |
| `value_date`, `booking_date` | When funds are good vs when posted |
| `amount` | Signed to one convention (e.g. inflow +, outflow −) |
| `direction` | `credit` / `debit` (kept explicit even though amount is signed) |
| `bank_transaction_code` | Raw code from the file (type code / txn type / BkTxCd) |
| `internal_category` | Your mapped group (wire in, ACH, fee, …) |
| `reference` | Bank/customer reference |
| `description` | Narrative / remittance text |
| `running_balance` | If the format supplies a per-line balance |
| `is_reversal` | True if the line reverses a prior entry |

## BAI2
Cash Management Balance Reporting; text, comma-delimited fields, records identified by a leading code.
- **01** File Header — sender/receiver, file date/time.
- **02** Group Header — ultimate receiver, originator, as-of date, currency.
- **03** Account Identifier — account number, currency, then **status/summary type codes** with
  amounts. Common type codes: `010` opening ledger, `015` closing ledger, `040` opening available,
  `045` closing available, `100` total credits, `400` total debits.
- **16** Transaction Detail — **type code** (sets credit/debit and activity kind), **amount**
  (unsigned; usually cents, no decimal point), funds-type, bank ref, customer ref, text.
- **88** Continuation — continues the previous record's text.
- **49** Account Trailer — account control total + record count.
- **98** Group Trailer / **99** File Trailer — group/file control totals and counts.
- Direction comes from the **type code**, not the amount sign. Keep a type-code → (credit/debit,
  category) map. Example detail type codes (verify per bank): `301` wire, `142`/`165` lockbox/ACH
  credit, `475` check paid, `451` ACH debit — **bank-specific; confirm.**

## SWIFT MT940 (prior-day) and MT942 (intraday)
Tag-based SWIFT messages. MT940 is the **end-of-day** customer statement; MT942 is the **interim**
(intraday) report.
- `:20:` transaction reference; `:25:` account identification; `:28C:` statement/sequence number.
- `:60F:` **opening balance** — `F` final (`M` intermediate): `D/C mark + date(YYMMDD) + currency +
  amount`. (Amounts use a comma decimal.)
- `:61:` **statement line** — `value date(YYMMDD) + [entry date MMDD] + D/C mark + amount + txn type
  ID code + reference`. Marks: `C` credit, `D` debit, `RC` reversal of credit, `RD` reversal of debit.
- `:86:` information to account owner — narrative/remittance for the preceding `:61:`.
- `:62F:` **closing balance**; `:64:` **closing available**; `:65:` forward available.
- **MT942 differences:** no `:60F:/:62F:` closing balances (it is intraday); adds `:34F:` floor
  limit and `:13D:` date/time stamp; may carry `:90D:`/`:90C:` debit/credit summary counts and sums.
  Treat its figures as provisional.

## ISO 20022 CAMT.053 / CAMT.052
XML. **CAMT.053** = Bank-to-Customer **Statement** (prior-day, final). **CAMT.052** = Bank-to-Customer
**Account Report** (intraday/interim). (CAMT.054 = debit/credit notification.)
- Root: `BkToCstmrStmt` (053) / `BkToCstmrAcctRpt` (052) → `Stmt` / `Rpt`.
- Account: `Stmt/Acct/Id` (IBAN or Othr), `Ccy`.
- **Balances:** repeating `Bal` blocks, each with `Tp/CdOrPrtry/Cd` + `Amt` + `CdtDbtInd` + `Dt`.
  Codes: `OPBD` opening booked, `CLBD` closing booked, `OPAV` opening available, `CLAV` closing
  available, `ITBD` interim booked, `PRCD` previously closed booked, `FWAV` forward available.
- **Entries:** repeating `Ntry` — `Amt` (with `Ccy`), `CdtDbtInd` (`CRDT`/`DBIT`), `Sts`
  (`BOOK` booked / `PDNG` pending), `BookgDt`, `ValDt`, `BkTxCd` (`Domn/Cd` domain, `Fmly/Cd` family,
  `SubFmlyCd`), and `RvslInd` (true = reversal).
- **Entry details:** `Ntry/NtryDtls/TxDtls` — `Refs` (EndToEndId, InstrId, etc.), `RltdPties`
  (debtor/creditor), `RmtInf` (structured/unstructured remittance). One `Ntry` may batch several
  `TxDtls`.
- Direction is the `CdtDbtInd` **element** (never inferred from sign); read the balance `Tp` to know
  ledger vs available.

## CSV
Bank- or portal-specific columnar export. No standard — you must map columns explicitly:
- Identify the date column(s) (value vs posting), the amount column, and how **direction** is
  encoded: a **signed amount**, **separate debit/credit columns**, or a **direction flag**.
- Capture reference/description columns and any running-balance column.
- Watch locale: decimal comma vs point, thousands separators, and date order (DMY vs MDY vs YMD).
- CSV usually lacks control totals — validate against a balance column or a companion statement.

## Balance types across formats
| Balance | BAI2 | MT940/942 | CAMT |
|---------|------|-----------|------|
| Opening ledger | `010` | `:60F:` | `OPBD` |
| Closing ledger | `015` | `:62F:` | `CLBD` |
| Opening available | `040` | — | `OPAV` |
| Closing available | `045` | `:64:` | `CLAV` |
| Intraday/interim | intraday file | MT942 | `ITBD` (052) |
Keep **ledger** and **available** distinct — positioning and reconciliation use different ones.

## Direction / sign conventions
- **BAI2:** unsigned amount; **type code** sets credit/debit; amount usually in cents (implied 2 dp).
- **MT `:61:`:** `C`/`D` mark; `RC`/`RD` = reversals; comma decimal.
- **CAMT:** `CdtDbtInd` = `CRDT`/`DBIT`; `RvslInd=true` = reversal.
- Normalize to one signed convention and **retain the raw code + a reversal flag** so nothing is lost.

## Code groups (internal category map)
Map each format's raw codes into one stable internal set so downstream logic is format-agnostic:
`wire_in, wire_out, ach_credit, ach_debit, check_paid, deposit, lockbox, card_settlement,
fee, interest, tax, return, fx, transfer, other`. Maintain the map centrally; onboarding a new bank =
adding its codes to the map, not changing parsing logic.

## Validation checks
- Per account: `opening + Σcredits − Σdebits = closing` (booked balances).
- Control totals/counts reconcile (BAI2 `49/98/99`; MT `:62F:` vs summed lines; CAMT entry count).
- Every transaction row has date, amount, direction, and a code.
- Reversals are flagged and not double-counted.
- Currency is consistent within an account block.
