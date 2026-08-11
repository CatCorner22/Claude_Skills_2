---
name: bank-fee-analysis
description: >-
  Analyzes bank fees from account-analysis statements — decoding AFP Service Codes, EDI 822 and ISO
  20022 camt.086 billing files, and the earnings-credit-rate (ECR) offset against compensating
  balances — to review, benchmark, and reduce bank charges. Use when reviewing bank fees, reading an
  account analysis statement, or preparing a fee negotiation. Triggers: bank fees, account analysis,
  account analysis statement, AFP service codes, EDI 822, camt.086, bank services billing, earnings
  credit rate, ECR, compensating balance, fee reduction, bank billing.
---

# Bank fee analysis

## When to use
- Reviewing a monthly/quarterly **account analysis statement** to understand what a bank is charging.
- Benchmarking fees across banks or over time, or preparing for a pricing negotiation / RFP.
- Deciding whether to pay charges as **hard fees** or offset them with **compensating balances**.
- Not for: deciding target balance levels or where to invest surplus cash → see
  `cash-management-skills:liquidity-management` (fee analysis tells you the ECR trade-off; liquidity
  management decides how much balance to hold and how to invest it).

## Do it
1. **Get the account analysis statement(s)** for the period, per account and consolidated. Prefer a
   machine-readable billing file (EDI **822** or ISO 20022 **camt.086**) over PDF so you can analyze
   at the line-item level. See `references/account-analysis.md` for the statement anatomy.
2. **Read the balance summary.** Note **average ledger balance**, **average collected (available)
   balance**, and the **investable balance** (collected minus any reserve factor the bank applies).
   The earnings credit is computed on the **investable** balance, not the ledger balance.
3. **Compute the earnings credit and the settlement.** `Earnings credit = investable balance × ECR ×
   (days/360 or /365)`. Compare it to **total charges**. If the earnings credit covers charges, the
   account is **balance-compensated**; the shortfall is billed as a **hard charge** (debited). A
   surplus of earnings credit may or may not carry forward — **confirm your bank's rules**.
4. **Decode every service line.** Each service has a **volume**, a **unit price**, and a
   **charge = volume × unit price**. Map lines to **AFP Service Codes** so the same service is
   comparable across banks (e.g. an ACH-origination or lockbox-item code means the same thing at
   every bank that uses the standard). Flag any line you cannot map.
5. **Analyze the drivers.** Sort charges high-to-low and by **volume × unit price**. Look for:
   services you no longer use, unit prices above benchmark, **volume growth** driving cost, duplicate
   or per-account charges that could be consolidated, and one-off/setup fees. Trend each service
   month over month — price creep hides in small per-item increases at high volume.
6. **Test the balance-vs-fee trade-off.** Given the current **ECR**, is it cheaper to leave a
   compensating balance or to pay hard fees and invest the cash elsewhere? Compare the ECR to your
   marginal investment yield: if you earn more investing the cash than the ECR credits, hold less
   balance and pay fees; if the ECR beats your yield, compensate with balances.
7. **Build the negotiation case and act.** Quantify each lever (see `references/account-analysis.md`):
   waive/reduce unit prices on high-volume services, raise the ECR, reduce the reserve factor, bundle
   or consolidate accounts, and benchmark via AFP codes or an RFP. Take the biggest-dollar items
   first, document target prices, and re-check the next statement to confirm the changes landed.

## Why / learn
An account analysis statement is really **two ledgers stapled together**: a list of services you
consumed (volume × unit price) and a **balance credit** the bank gives you for leaving money on
deposit. The concept that ties them is the **earnings credit rate (ECR)** — a *notional* rate the
bank applies to your **investable balance** to generate an **earnings credit** that offsets charges.
It is not interest you receive; it is a discount on fees, which is why banks can offer a competitive
ECR without paying you cash. That single mechanism explains the central decision in fee management:
you can pay the bank in **money (hard fees)** or in **balances (compensation)**, and which is cheaper
depends entirely on the ECR versus what you could earn investing the same cash. If your investment
yield beats the ECR, every dollar of compensating balance is under-earning — pay the fees and invest
instead; if the ECR beats your yield (or you must hold the balance anyway), let it offset charges.
The **reserve factor** matters because the bank credits only the balance it can actually invest, so a
higher reserve factor quietly shrinks your credit. And **AFP Service Codes** are what make any of
this comparable — without a common code, "ACH origination" at one bank and "ACH file item" at another
look like different things; with the code you can benchmark unit prices and spot the outliers. Hold
"services cost volume × price, balances earn a fee-offset at the ECR, and the two settle against each
other" and a fee review becomes arithmetic plus negotiation.

## Common mistakes
- Reading the earnings credit as interest income → it only offsets fees; it is not paid to you (usually). Confirm carry-forward rules.
- Computing the credit on the ledger balance → it is the **investable** balance (collected minus reserve factor).
- Comparing unit prices without AFP codes → you compare different services. Map to the standard first.
- Chasing tiny unit prices while ignoring volume → cost = volume × price; a cheap per-item on huge volume dominates.
- Leaving large compensating balances when your investment yield beats the ECR → under-earning cash. Test the trade-off.
- Reviewing only the PDF total → you miss line-item creep. Use the EDI 822 / camt.086 detail.

## Tailor to your environment
Drop your real setup into `references/your-environment.md` (keep account numbers, real balances, and
negotiated unit prices in `your-environment.private.md`, which is git-ignored). Capture your banks
and accounts, your current ECR(s) and reserve factor, whether you receive EDI 822 or camt.086 files,
your marginal short-term investment yield (for the trade-off), the services you actually use, and
your benchmark unit prices. Reserve requirements, ECR conventions, and carry-forward rules differ by
bank and over time — **confirm the current terms for your bank/region**.

## References
- references/account-analysis.md — statement anatomy, AFP codes, EDI 822 vs camt.086, the ECR math, and negotiation levers
- references/your-environment.md — your banks, accounts, ECR, reserve factor, and benchmark prices (add when supplied)
