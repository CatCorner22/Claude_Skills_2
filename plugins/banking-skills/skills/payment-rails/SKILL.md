---
name: payment-rails
description: >-
  Compares and selects payment methods — ACH (including Same Day ACH), Fedwire, CHIPS, RTP,
  FedNow, SWIFT cross-border, and checks — by cost, speed, settlement finality, reversibility,
  amount limits, and cutoff times, and explains how a given rail works. Use when deciding how to
  move money, funding a payment, or explaining the difference between rails. Triggers: ACH, wire,
  Fedwire, CHIPS, RTP, FedNow, SWIFT, MT103, pacs.008, payment rail, same-day ACH, payment method,
  how to send money, wire vs ACH, real-time payment, cross-border payment.
---

# Payment rails

## When to use
- Choosing how to move a specific payment given cost, speed, finality, and reversibility needs.
- Explaining how a rail settles, when it is final, and whether it can be reversed or recalled.
- Comparing rails for a use case (payroll, supplier run, treasury sweep, cross-border, refund).
- Not for: choosing the technical channel that connects you to the bank (SFTP / SWIFT / API /
  portal) → see `banking-skills:bank-connectivity`. For payment approval, dual control, and
  fraud prevention on releasing a payment → see `cash-management-skills:cash-management-controls`.

## Do it
1. **State the payment's requirements.** Amount and currency; how fast funds must be *good* (not
   just sent); whether you need **finality** (no clawback) or can tolerate a reversible rail;
   domestic vs cross-border; recurring vs one-off; and the counterparty's receiving capability.
2. **Decide push vs pull.** A **credit push** (you send from your account) fits payables, payroll,
   and treasury moves. A **debit pull** (payee draws from the payer's account under authorization)
   fits collections/direct debits — only ACH supports pull; wires, RTP, and FedNow are push-only.
3. **Screen by finality and reversibility first, then cost/speed.** If the payment must be
   irrevocable (property closing, margin call, large supplier), use a **wire (Fedwire/CHIPS)** or an
   **instant rail (RTP/FedNow)** — all settle final. If a mistake must be recoverable, **ACH**
   allows returns/reversals within its windows. See `references/rail-comparison.md` for the matrix.
4. **Pick the rail:**
   - **ACH** (batch, low cost): non-urgent, high-volume domestic payables/payroll/collections.
     Use **Same Day ACH** when it must clear today but doesn't need wire-grade finality.
   - **Fedwire**: urgent, final, high-value domestic credit; individual real-time gross settlement.
   - **CHIPS**: large-value/international USD bank-to-bank, netted; used by correspondents.
   - **RTP / FedNow**: instant (24/7/365), final, lower-value credit pushes; good for on-demand and
     off-hours payments where the receiver's bank participates.
   - **SWIFT** (MT103 / ISO 20022 pacs.008): cross-border and FX, settled through correspondent
     banks; confirm the routing chain, charges (OUR/SHA/BEN), and value date.
   - **Check**: only when the counterparty requires paper; slowest, float-prone, fraud-exposed.
5. **Confirm the cutoff and calendar.** Every rail has daily cutoff times and a settlement calendar
   (banking days for ACH/Fedwire/CHIPS; 24/7 for RTP/FedNow). Miss the cutoff and the payment rolls
   to the next processing window. Confirm exact cutoffs and limits **for your bank and region**.
6. **Record what you chose and why.** Note the rail, expected settlement/value date, whether it is
   final, and the all-in cost. This is your audit trail and it sharpens the next decision.

## Why / learn
Rail choice is driven by two things above all: **finality** and the **cost/speed trade-off**.
Finality means the funds cannot be pulled back once settled — wires and instant rails give the
beneficiary certainty, which is exactly why they are used where a reversal would be catastrophic,
and exactly why *you* must get the details right before releasing one: a mis-sent wire is recovered
only if the beneficiary agrees to return it. ACH is the mirror image — it batches and settles later,
which is why it is cheap and why it can be **returned** (unpaid, insufficient funds, or, for
unauthorized consumer debits, disputed within a longer window). That reversibility is a feature for
routine payables and a risk for collections. Instant rails (RTP, FedNow) collapse the trade-off from
one side — they are final *and* fast — but they are push-only, amount-capped, and only work if the
receiving bank participates, so they don't replace wires for very large values or ACH for bulk.
Cross-border adds a layer: **SWIFT is a messaging network, not a settlement rail** — the money
actually moves through a chain of correspondent (nostro/vostro) accounts, so speed, cost (lifting
fees, FX spread), and finality depend on that chain, not on SWIFT itself. Hold the picture "who can
reverse this, how fast are funds good, and what does it cost" and the right rail usually falls out.

## Common mistakes
- Treating "sent" as "settled" → ACH and checks can still be returned. Confirm finality, not dispatch.
- Sending a wire to fix an urgent ACH without checking recoverability → wires are irrevocable; verify the beneficiary first.
- Assuming RTP/FedNow reach everyone → both need the *receiving* bank to participate; confirm reach.
- Ignoring cutoffs → a payment sent after cutoff settles the next window, not today.
- Using SWIFT charge code BEN/SHA when the beneficiary must receive the full amount → use OUR (confirm terms).
- Picking a rail on price alone → the cheapest rail may not clear in time or may be reversible when you need finality.

## Tailor to your environment
Drop your real setup into `references/your-environment.md` (keep sensitive details — bank names,
account numbers, negotiated per-item pricing — in `your-environment.private.md`, which is
git-ignored). Capture the rails your banks support, your exact cutoff times per rail, per-transaction
and daily limits, your negotiated costs, which currencies route via which correspondents, and your
policy for when each rail is required (e.g. wires above a threshold, ACH for payroll). Rail limits,
cutoffs, and return windows are set by scheme rules and your bank and change over time — **confirm
the current numbers for your bank and region** rather than hard-coding them here.

## References
- references/rail-comparison.md — per-rail speed, cost, finality, reversibility, limits, cutoffs, and message types
- references/your-environment.md — your banks, supported rails, cutoffs, limits, and pricing (add when supplied)
