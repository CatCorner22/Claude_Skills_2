# CTP domain map, drills, and technique (reference)

AFP owns the exam content outline, the *Essentials of Treasury Management* (ETM) edition, and
all policies (eligibility, length, calculator, scoring). This file gives the durable structure —
**confirm current specifics against AFP's published outline and candidate handbook.**

## Contents
- Domain-to-library map
- Study-plan template (12-week pattern)
- Practice-question patterns (with model items)
- Computational formula inventory
- Error-log format
- Exam-technique checklist

## Domain-to-library map
Recent outlines cover this ground; adjust rows to the current outline's actual domains/weights.

| Exam ground | Study with (this library) | Typical university-analyst posture |
|---|---|---|
| Treasury function, ethics, organization | skim ETM directly | familiar |
| Working capital management (CCC, trade credit, AR/AP/inventory) | `finance-skills:working-capital-management`, `finance-skills:financial-ratios` | often weak — corporate framing |
| Cash and liquidity management; forecasting | `cash-management-skills:cash-positioning`, `cash-management-skills:cash-forecasting`, `cash-management-skills:liquidity-management`, `banking-skills:bank-account-structure` | strong — daily work |
| Payments and collections; banking relationships | `banking-skills:payment-rails`, `nacha-ach-rules` (this plugin), `banking-skills:bank-fee-analysis`, `banking-skills:kyc-aml-basics` | strong |
| Short-term investing and borrowing; capital markets | `finance-skills:short-term-investments`, `finance-skills:time-value-of-money`, `finance-skills:capital-budgeting`, `treasury-accounting-skills:debt-facilities-and-covenants` | mixed |
| Financial risk management (FX, interest rate, hedging) | `finance-skills:fx-risk-basics`, `treasury-accounting-skills:hedging-and-derivatives` | often weak |
| Treasury operations, technology, controls | `cash-management-skills:cash-management-controls`, `banking-skills:bank-connectivity` | strong |
| Relationship of finance disciplines (accounting, FP&A) | `accounting-skills:financial-statements`, `accounting-skills:double-entry-fundamentals` | mixed |

## Study-plan template (12-week pattern)
Scale to your runway; keep the phase proportions.

| Weeks | Phase | Content |
|-------|-------|---------|
| 1 | Baseline | Confirm current outline; confidence scores; priority = weight × (6 − confidence); schedule built |
| 2–8 | Learn + drill (interleaved) | 2–3 domains in flight at once, highest priority first. Per domain: ETM chapter + mapped skills → one-page concept sheet → drill to ~80%. Weekly: mixed-domain quiz + error-log re-drill |
| 9–10 | Consolidate | Review passes at expanding intervals; drill exclusively from the error log; computational speed runs |
| 11–12 | Mocks + taper | ≥2 timed full-length mocks; review time ≥ test time; light retrieval only in the final days |

Session shape (60–90 min): 5 min recall of last session from memory → 35–60 min new
material/drill → 10 min error-log update → 5 min preview of next session.

## Practice-question patterns (with model items)
Ask for items in these shapes; always demand the why-right *and* why-each-distractor-wrong.

**Pattern 1 — computation with trap distractors**
> A firm has DSO 42 days, DIO 61 days, DPO 38 days. What is its cash conversion cycle?
> (A) 65 days (B) 141 days (C) 19 days (D) 57 days
Answer: A (61 + 42 − 38). B adds all three (forgot to subtract DPO); C subtracts wrongly;
D transposes. Good items make each distractor the output of one specific mistake.

**Pattern 2 — concept discrimination**
> Which payment method gives the beneficiary final, irrevocable funds soonest?
> (A) Same Day ACH credit (B) Fedwire (C) check via lockbox (D) ACH debit origination
Answer: B — wires settle final in real time; Same Day ACH remains returnable. Tests
finality-vs-speed discrimination, a classic exam axis.

**Pattern 3 — scenario/judgment**
> A treasurer must fund a 2:00 p.m. property closing today and learns of it at 11:00 a.m. The
> amount exceeds Same Day ACH limits. The best action is…
Tests applying constraints (limits, cutoffs, finality) rather than recalling definitions.

**Pattern 4 — best-answer among plausible policies**
> Which control most directly addresses payment-fraud risk from a compromised AP email account?
Options are all "good controls"; only one addresses the named risk *most directly*. Trains the
"best answer, not a correct answer" habit.

## Computational formula inventory
Drill until mechanical (confirm conventions — 360 vs 365 day-count — against the current ETM):
- **Cash conversion cycle:** CCC = DIO + DSO − DPO; each component = balance ÷ (annual flow/365).
- **Cost of forgoing a cash discount** (e.g. 2/10 net 30):
  (disc% ÷ (100 − disc%)) × (365 ÷ (net days − disc days)) — annualized, then compare to
  borrowing cost.
- **Money-market yields:** discount rate vs money-market yield vs bond-equivalent yield
  conversions; dollar discount = face × rate × (days/360).
- **Effective annual rate:** EAR = (1 + periodic)^n − 1; nominal-vs-effective discrimination.
- **Earnings credit / collected balances:** required balance = fees ÷ (ECR × days/365);
  compensating-balance vs fee trade-off.
- **Simple FX:** cross rates, points, covered cost comparisons (direction of the quote is the
  usual trap).
- **TVM:** PV/FV/annuities — see `finance-skills:time-value-of-money`.

## Error-log format
One row per miss; review weekly; a concept leaves the log after two consecutive clean hits.

| Date | Domain | Concept | Question gist | Why missed (knowledge / misread / calc slip / pacing) | Re-test dates |
|------|--------|---------|----------------|------------------------------------------------------|---------------|

The "why missed" column is the payload: knowledge gaps get re-study, misreads get technique
work, calc slips get slow-motion drills, pacing gets mock practice.

## Exam-technique checklist
- Compute minutes-per-question from the current exam length; check pace at quarter marks.
- Pass 1: answer everything answerable; flag and move on — no question deserves 5 minutes.
- Eliminate before selecting; with two candidates left, re-read the stem's qualifier ("most
  likely," "best," "first") — it usually decides.
- Write the formula before the numbers; sanity-check magnitude (a CCC of 141 days from those
  inputs should feel wrong).
- If unanswered questions score as wrong (confirm current policy), leave nothing blank.
- Confirm calculator policy in advance and practice on the allowed device only.
- Day before: light retrieval, logistics check, sleep — consolidation beats cramming.
