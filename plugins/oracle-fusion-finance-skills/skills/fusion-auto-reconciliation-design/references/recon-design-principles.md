# Reconciliation design principles (in full)

Release note: record layouts and type codes below follow the public BAI2/ISO/SWIFT
standards and Oracle's documented behavior — confirm your bank's actual usage and your
release's field names before building rules on them.

## Contents
- The four architectural principles
- Format-level knowledge: BAI2, CAMT.053, MT940
- Hard settlement patterns
- Module integration flows
- The diagnostic protocol
- Measuring the engine in OTBI

## The four architectural principles

1. **Minimize Transaction Creation Rules.** TCRs create the system-side transaction from
   the statement line. Legitimate uses only: bank fees, interest earned, sweep/ZBA
   transfers, unexpected chargebacks — items that genuinely originate at the bank. A TCR
   that absorbs items AR or AP should have produced hides the upstream defect and breaks
   reconciliation's independence.
2. **Subledger supremacy.** The statement is a mirror. AR receipts (standard receipts,
   lockbox, remittance batches) and AP payments (PPR output) are created in their modules
   and flow to CE *for matching* — never the reverse for business transactions.
3. **Matching hierarchy.** Sequence rules by precision: (1) one-to-one exact on a
   bank-supplied reference; (2) one-to-many / many-to-one with grouping that mirrors how
   the bank bundles money; (3) tolerance-assisted matches last. Each tolerance is a
   controlled loosening — date and amount tolerances buy match rate at false-positive risk.
4. **Clear directionality.** Into CE: AR receipts, AP payments, payroll, journals. Out of
   CE: reconciliation status, and external transactions' accounting via SLA to GL. Know
   which direction is broken before touching anything.

## Format-level knowledge

### BAI2
- **16-record** — transaction detail: type code, amount, funds type, bank reference,
  customer reference, text.
- **88-record** — continuation of the preceding record; this is where invoice numbers,
  merchant IDs, terminal IDs, and remittance text usually live. Parsing the 88-record is
  the highest-leverage move for match rates.
- **Type codes** (standard BAI2; confirm your bank's usage): e.g. 115 lockbox deposit,
  142 ACH credit, 165 pre-authorized draft, 475 check paid. Codes drive transaction-type
  mapping and can scope matching rules.
- Oracle side: **Bank Statement Parsing Rules** extract substrings from statement line
  fields into attributes (including user-defined fields — confirm names in your release)
  that Reconciliation Matching Rules can then reference.

### CAMT.053 (ISO 20022)
- XML entries (`Ntry`) with structured references (`EndToEndId`, `AcctSvcrRef`,
  remittance information elements) — richer than BAI2 when the bank populates them.
- Map elements to statement attributes via parsing configuration; prefer structured
  reference elements over free text when present.

### MT940 (SWIFT)
- Tag-based: `:61:` statement line (with customer/bank references), `:86:` information
  field carrying remittance detail. `:86:` plays the 88-record's role — parse it.

## Hard settlement patterns

### Bulk card settlements
One net ACH deposit represents hundreds of AR receipts, with processor fees deducted at
source. Design choices: match the deposit to an **AR remittance batch** (preferred — the
batch total is the system-side bundle) or many-to-one against grouped receipts by
settlement date + merchant ID (parsed from the addenda); handle the fee as a
bank-originated item (TCR or external transaction) or net-settlement configuration —
never widen the amount tolerance to swallow the fee.

### Lockbox
Bank deposits arrive batched; AR lockbox processing creates the receipts. Match on deposit
date + lockbox batch reference; the fix for unapplied lockbox receipts is in AR lockbox
setup, not in CE rules.

### Checks
One-to-one on check number (parsed or bank-supplied) is near-perfect matching. Layer in
stale-date policy and stop payments: a check paid after a stop is an exception to surface,
not to match away.

### Sweeps / ZBA
Bank-originated by definition — the legitimate TCR home. Match sweep pairs across accounts
by date + amount; keep the TCR scoped to the sweep transaction codes.

## Module integration flows
- **AR:** Receipt Class / Receipt Method determines whether a receipt posts to Cash,
  Cash Clearing, or Unapplied/Unidentified on creation and at remittance — this decides
  *what CE should expect to match*. Remittance batches bundle receipts into the
  bank-visible deposit.
- **AP:** Payment Process Requests produce payments; accounting flows Liability → Cash
  Clearing → Cash **upon reconciliation** (clearing-account configurations vary — confirm
  yours).
- **GL/SLA:** reconciliation and external-transaction accounting generate journals via
  Subledger Accounting; items "stuck in clearing" with matching complete usually mean the
  accounting/SLA step hasn't run or erred.
- **OTBI:** Cash Management subject areas — Bank Statements Real Time (line-level detail
  and reconciliation status), Bank Statement Balances Real Time, Bank Statement Line
  Charges Real Time, External Cash Transactions Real Time. Reconciliation status is an
  attribute inside Bank Statements RT, not its own subject area.

## The diagnostic protocol
1. **Directionality:** unmatched item — is the system-side transaction missing (subledger
   problem) or is the statement line missing/mis-parsed (bank/parsing problem)?
2. **Clearing accounts:** stuck items — unmatched (matching problem) vs matched-but-
   unaccounted (SLA/processing problem)?
3. **Rule precedence:** did a broad rule fire before the precise one? Check rule hit
   counts per run.
4. **Evidence:** raw BAI2 line + its 88-records, the matching-rule configuration
   (criteria, grouping, tolerances, sequence), and the exact error/status — then reason
   from the artifacts, not from memory.

## Measuring the engine in OTBI
- Match rate by account and by rule (which rules do the work; which never fire).
- Orphaned items: statement lines unmatched > N days; system transactions never cleared.
- False-positive audit: sample tolerance-assisted matches periodically.
- Trend after every rule change — a tuning without a before/after number is a guess.
