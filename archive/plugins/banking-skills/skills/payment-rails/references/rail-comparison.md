# Payment rail comparison (reference)

Numbers below are directional and set by scheme rules and your bank; **confirm current limits,
cutoffs, and return windows for your bank and region** before relying on them.

## Contents
- At-a-glance matrix
- Rail-by-rail notes
- Push vs pull
- Finality and reversibility
- SWIFT cross-border and correspondent banking
- Choosing quickly

## At-a-glance matrix
| Rail | Speed (funds good) | Direction | Finality | Reversible? | Typical cost | Amount profile |
|------|--------------------|-----------|----------|-------------|--------------|----------------|
| ACH (standard) | 1–2 banking days | Push or pull | Not final until return window passes | Yes — returns/reversals | Cents/item | Low-to-mid, high volume |
| Same Day ACH | Same banking day (settlement windows) | Push or pull | Same as ACH | Yes | Low, small premium | Per-item cap (confirm) |
| Fedwire | Seconds–minutes, same day | Push only | Final on settlement | No (only by beneficiary consent) | High ($/wire) | Any; used for high value |
| CHIPS | Same day (netted) | Push only | Final on release/settlement | No | Lower/item at volume | Large-value, international USD |
| RTP (TCH) | Seconds, 24/7/365 | Push only (RfP for request) | Final/irrevocable | No | Low flat | Capped (confirm) |
| FedNow | Seconds, 24/7/365 | Push only (RfP for request) | Final/irrevocable | No | Low flat | Capped, raisable (confirm) |
| SWIFT (cross-border) | Minutes to days | Push (MT101 to instruct) | Depends on correspondent settlement | Recall request only | FX spread + lifting fees | Any; cross-currency |
| Check | Days (+ float) | Pull-like (payee deposits) | Not final; can bounce | Yes — stop payment / return | Low/item, high handling | Any; declining use |

## Rail-by-rail notes
- **ACH** (NACHA-governed, US): batched credit/debit transfers. Settles next banking day standard,
  or same day via **Same Day ACH** settlement windows. Cheap and reversible: returns carry reason
  codes (e.g. R01 insufficient funds, R02 account closed); unauthorized *consumer* debits can be
  disputed within an extended window. Ideal for payroll, supplier runs, and direct-debit collections.
- **Fedwire Funds Service** (Federal Reserve): real-time gross settlement — each wire settles
  individually and **finally** on the central bank's books, same day, within operating hours.
  Push-only credit transfer. Highest per-item cost; used where speed and finality matter.
- **CHIPS** (The Clearing House): large-value system that **multilaterally nets** and settles with
  finality; heavily used for international USD and correspondent flows. Bank-to-bank, not a
  corporate-facing rail — you reach it through your bank.
- **RTP** (The Clearing House) and **FedNow** (Federal Reserve): instant credit-push rails running
  24/7/365 with immediate **finality**. Both support a **Request for Payment (RfP)** message so a
  biller can ask to be paid (the payer still pushes). Amount caps apply and both require the
  *receiving* institution to participate. Great for on-demand, off-hours, and gig/refund payments.
- **SWIFT**: a secure **messaging** network, not a settlement system. **MT103** (customer credit
  transfer) / ISO 20022 **pacs.008** carry the instruction; **MT101** requests a transfer; money
  settles through **correspondent banking** nostro/vostro accounts. SWIFT **gpi** adds end-to-end
  tracking. Charge codes: **OUR** (sender pays all), **SHA** (shared), **BEN** (beneficiary pays).
- **Check**: paper instrument the payee deposits; slow, exposed to float and fraud. Controls:
  **positive pay** and stop-payment. Use only when the counterparty cannot accept electronic.

## Push vs pull
- **Credit push:** the payer's bank sends funds to the payee. Fedwire, CHIPS, RTP, FedNow, and ACH
  credits are pushes. The payer controls timing and amount.
- **Debit pull:** the payee, with prior authorization, draws funds from the payer's account. Only
  **ACH debits** do this among these rails (checks are pull-like on deposit). Pull enables
  autopay/direct debit but carries return/dispute risk — hence authorization and mandate rules.

## Finality and reversibility
- **Final / irrevocable:** Fedwire, CHIPS, RTP, FedNow. Once settled, funds return only if the
  **beneficiary agrees**. This is why beneficiary/account verification must happen *before* release.
- **Reversible within rules:** ACH (returns and NACHA reversal entries within defined windows) and
  checks (stop payment, return unpaid). Convenient for routine payments, risky for collections.
- **Recall (SWIFT):** you can send a recall/return request through the correspondent chain, but
  actual return depends on the beneficiary bank and customer — treat cross-border as effectively
  final once the beneficiary is credited.

## SWIFT cross-border and correspondent banking
Because SWIFT only moves messages, a cross-border payment travels a **correspondent chain**: your
bank debits your account and instructs its correspondent, which credits the beneficiary bank (or
another correspondent) via their mutual **nostro/vostro** accounts. Each hop can deduct a **lifting
fee** and apply an **FX spread**, and each adds time and a point where the payment can be queried
for sanctions/compliance. Confirm the routing (BIC chain), the charge option, and the value date up
front. ISO 20022 (**pacs.008**) is replacing MT103 on the interbank leg — same facts, richer
structured data (especially remittance and party information).

## Choosing quickly
1. Must it be irrevocable and same-day, high value? → **Fedwire** (or CHIPS via your bank).
2. Must funds arrive instantly, any hour, modest value, receiver participates? → **RTP / FedNow**.
3. Routine, domestic, cost-sensitive, can wait a day (or same-day at low premium)? → **ACH / Same Day ACH**.
4. Collecting under a mandate/autopay? → **ACH debit** (pull).
5. Cross-border or cross-currency? → **SWIFT** — confirm correspondents, charges, and value date.
6. Counterparty requires paper? → **Check**, with positive pay.
