# The escheatment lifecycle (reference)

Structure-first reference. Dormancy periods, thresholds, deadlines, and formats are set by
each state's unclaimed-property act and are amended over time — confirm current values with
the state administrator (for Tennessee, the Treasury's unclaimed-property division) before
filing anything.

## Contents
- Dormancy screening worksheet
- Priority rules: which state
- Due-diligence letter skeleton
- Accounting entries through the lifecycle
- Holder report and remittance checklist
- Audit readiness
- Source-reduction playbook

## Dormancy screening worksheet

Build one row per open item; the goal is a defensible split into *not yet dormant*,
*approaching dormancy* (chase now), and *dormant* (enter the reporting pipeline).

| Field | Notes |
|---|---|
| Property type | payroll check, vendor check, student refund, credit balance, deposit, ... |
| Issue / last-activity date | dormancy clock start; "activity" means owner-initiated contact |
| Owner name + last known address | drives priority rules and due diligence |
| Amount | compare to the state's due-diligence de minimis threshold |
| Dormancy period for this type | from the state's current table — record source and date checked |
| Dormancy date | start + period |
| Status | not dormant / approaching / dormant |
| Disposition | chase early / due diligence / reissue / report |

Common type distinctions to expect in state tables: wages/payroll (often shorter), vendor
obligations, refunds/credit balances, deposits, securities-related property. Never reuse
last year's table without re-checking.

## Priority rules: which state

From the U.S. Supreme Court's Texas v. New Jersey framework (stable doctrine; the details of
each state's adoption live in its act):

1. **First priority:** the state of the owner's **last known address** as shown in the
   holder's records.
2. **Second priority:** if no address, or the address is in a foreign country, the property
   goes to the **holder's state of domicile** (state of incorporation/organization).

Practical consequences: report line-by-line by owner address state (most holders file in
multiple states or use reciprocal filing where offered); an address you failed to record is
an obligation you route by default to your domicile state; address hygiene at payee
onboarding is therefore a compliance control, not a courtesy.

## Due-diligence letter skeleton

Check the state's requirements for timing window, amount threshold, and any required content
or delivery method; then send, and log every attempt.

> Our records show that we are holding [property description, e.g. uncashed check #____
> dated ____] payable to you in the amount of $____. If we do not hear from you by
> [response deadline], we are required by state law to transfer these funds to the
> [State] unclaimed property program, after which you may claim them from the state.
> To claim the funds now, [response instructions — verify identity; do not ask the owner to
> "confirm" bank details cold, and validate any payment-instruction change independently].

Log: date sent, method, address used, returned/undeliverable flag, response, and resolution.
The log is part of the holder report's support.

## Accounting entries through the lifecycle

Illustrative shapes (map to your chart of accounts):

1. **Void a stale check** (removes it from outstanding, recognizes the obligation):
   `Dr Cash (restore) / Cr Unclaimed property liability` — never `Cr Income`.
2. **Owner responds — reissue:**
   `Dr Unclaimed property liability / Cr Cash` (new payment, with the void-reissue trail).
3. **Remit to state:**
   `Dr Unclaimed property liability / Cr Cash` (remittance accompanies the holder report).
4. **Owner surfaces after remittance:** direct them to the state's claims process — the
   liability has legally moved to the state's custody.

The liability account should reconcile to the item-level pipeline at all times; a balance
without a supporting item list is an audit finding waiting to happen.

## Holder report and remittance checklist

- [ ] Dormancy screen complete, using the current year's verified dormancy table.
- [ ] Priority-rule split by state done from last-known addresses.
- [ ] Due diligence sent within the statutory window, above-threshold items only, attempts logged.
- [ ] Responses processed (reissues cleared out of the report population).
- [ ] Report built in the state's required format (most states: NAUPA standard electronic file).
- [ ] Owner records complete: name, last address, property type code, amount, dates.
- [ ] Aggregate/under-threshold items handled per the state's rules.
- [ ] Negative report filed where the state requires one even with nothing to remit.
- [ ] Remittance matches the report total; liability account clears item-for-item.
- [ ] Full package archived: report file, remittance proof, due-diligence log, item detail —
      kept for the state's retention period.

## Audit readiness

States examine holders, sometimes via third-party (contingent-fee) auditors, with long
lookback periods; where records are missing they may estimate liability. Your defenses are
records and consistency: the item-level pipeline, filed reports (including negative ones),
due-diligence logs, and a written procedure you actually follow. Also confirm your
institution's status: some states run special processes for their own agencies and
instrumentalities — verify with the administrator rather than assuming either exemption or
standard treatment.

## Source-reduction playbook

- **Payee data quality:** validate name/address (and banking for e-payments) at onboarding;
  re-verify on returned mail immediately, while the trail is warm.
- **Prefer e-payments:** ACH/wire and payroll direct deposit cannot go stale in a drawer;
  every check you do not write is escheatment you will never process.
- **Chase early:** contact payees of uncashed checks at 30/60/90 days — response rates fall
  as items age; escalate student refunds through existing student-contact channels.
- **Design refunds to avoid orphan credits:** default refunds to the original payment method
  or verified banking; sweep small credit balances into a review queue instead of letting
  them age.
- **Coordinate with HR** on final paychecks and unclaimed wages (often the shortest dormancy).
- **Measure it:** track dollars and counts entering the pipeline per cycle; a falling intake
  curve is the proof the playbook works.
