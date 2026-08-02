# Target balances and sweeps (reference)

## Contents
- Minimum vs. target balance
- Sweep structures
- Buffer sizing
- Facilities and deployment

## Minimum vs. target balance
- **Minimum balance** — the floor an account must not drop below: enough to cover its intraday
  outflow peak and avoid overdraft/returned items. Driven by that account's own payment pattern.
- **Target balance** — the level a sweep leaves in (or tops up to). For a pure disbursement account
  the target may be zero (ZBA); for an operating account it is the minimum plus a working margin.
- Set both from the account's **outflow behavior** (largest day, timing spikes), not a round number.
- A compensating-balance requirement or bank minimum, where one exists, sets a hard floor under the target.

## Sweep structures
- **Zero-balance account (ZBA)** — the account is swept to (or funded to) **zero** each day against a
  master concentration account. Common for disbursement and collection accounts; keeps operating cash
  in one place.
- **Target-balance sweep** — sweep to a **set target** rather than zero, leaving a working buffer in
  the account.
- **Concentration account** — the master account balances sweep into; the single point at which the
  group's drag-vs-risk and invest/borrow decisions are made.
- **Notional vs. physical pooling** — physical pooling moves cash (sweeps); notional pooling offsets
  balances for interest without moving cash (needs a legal right of set-off). Cross-entity pooling has
  intercompany-loan and tax consequences — see `cash-management-skills:intercompany-cash-netting`.

## Buffer sizing
- Size the group buffer to a **defined stress**, e.g.:
  - **Days-of-outflows** — hold *N* days of average net outflows.
  - **Peak-shortfall** — hold the largest projected shortfall over the forecast horizon plus a margin.
  - **Stress overlay** — add a shock (slow collections, delayed receipt, pulled line) on top.
- The buffer is **liquid and safe** — its job is availability, not yield. Only cash **above** the
  buffer is investable.

## Facilities and deployment
- **Committed facility** (e.g. revolving credit) — the lender is contractually bound to lend up to the
  limit; you pay a commitment fee for reliability. Use it as the buffer's backstop.
- **Uncommitted facility** (e.g. money-market line) — cheaper, but the lender can decline; treat as
  opportunistic, never as core backup.
- **Deficit coverage order:** internal transfer / sweep-in → committed facility draw → uncommitted /
  market funding. Match funding tenor to how long you are short.
- **Surplus deployment:** above the buffer, invest per policy (tenor-laddered to forecast needs).
  Instrument selection (MMFs, T-bills, deposits) belongs to `finance-skills:short-term-investments`.
