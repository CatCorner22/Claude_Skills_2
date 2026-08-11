# Investment policy skeleton (reference)

Typical ranges shown; calibrate to your size, risk appetite, and jurisdiction, and have
counsel/board approve.

## Contents
- Policy skeleton
- Permitted instruments table (example shape)
- Compliance-check worksheet
- Exception log format

## Policy skeleton
1. **Purpose & scope** — which entities and cash pools the policy governs.
2. **Objectives** — safety of principal, then liquidity, then yield. One sentence each.
3. **Delegation** — who invests (roles), who approves the policy (board/committee), who checks.
4. **Portfolio tiers** — operating / reserve / strategic, with horizon and instrument mapping.
5. **Permitted instruments** — the table below; everything else prohibited by default, plus a
   named prohibited list (equities, commodities, crypto assets, structured notes, leverage,
   securities lending) to remove argument.
6. **Credit quality** — minimum ratings at purchase; action framework on downgrade.
7. **Concentration & counterparty limits** — per issuer, per fund, per bank group (all products
   aggregated), per asset class.
8. **Maturity limits** — max per instrument; portfolio weighted-average maturity cap.
9. **Reporting & compliance** — check cadence, data source (custody), report recipients.
10. **Exceptions** — passive vs active breach handling, waiver authority, time limits.
11. **Review** — annual re-approval; change log.

## Permitted instruments table (example shape)
| Instrument | Min rating (at purchase) | Max maturity | Max % portfolio | Max per issuer |
|---|---|---|---|---|
| Govt MMFs (stable NAV) | AAA-mmf | n/a (daily) | 100% | 25–50% per fund |
| US T-bills/notes | Sovereign | 12–24 mo | 100% | n/a |
| Bank deposits / CDs | A-1/P-1 issuer | 6–12 mo | 50% | 10–20% |
| Commercial paper | A-1/P-1 | 3–6 mo | 25–50% | 5–10% |
| Agency discount notes | AA+ | 12 mo | 50% | 25% |
| Prime MMFs (floating NAV) | AAA-mmf | n/a | 0–25% (policy call) | 10–25% |
Counterparty limit tiers (bank groups, all products incl. positive derivative MTM):
e.g. AA-tier $X, A-tier 0.6X, below A: exit/no new exposure.

## Compliance-check worksheet
For each position (from custody/portal data, as of check date):
| Position | Instrument permitted? | Rating ≥ floor? | Issuer within limit? | Maturity within cap? |
|---|---|---|---|---|
Portfolio-level: WAM ≤ cap? Tier sizes vs forecast? Asset-class mix within limits?
Sign-off: checker (not the investor), date, result, exceptions raised.
File every run — clean results included.

## Exception log format
| Date | Type (passive/active) | Description | Assessment | Decision & authority | Waiver expiry | Closed |
|---|---|---|---|---|---|---|
Active breaches also route to the controls owner as a control incident, not just a portfolio event.
