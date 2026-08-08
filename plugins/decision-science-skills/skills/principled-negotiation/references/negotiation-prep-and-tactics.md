# Negotiation prep and tactics

The full prep template, the tactic catalog with example lines, a worked bank-fee-increase
example wired to `banking-skills:bank-fee-analysis` outputs, the rehearsal protocol, and
the ethics line. Sources: *Getting to Yes* (Fisher/Ury, Harvard Negotiation Project) for
the strategy layer; *Never Split the Difference* (Voss) for the tactics layer. Both are
practitioner canon — teaching and field practice, not controlled trials.

## Contents
1. [The prep pack template](#1-the-prep-pack-template)
2. [Tactic catalog with example lines](#2-tactic-catalog-with-example-lines)
3. [Worked example: the bank fee increase](#3-worked-example-the-bank-fee-increase)
4. [Rehearsal roleplay protocol](#4-rehearsal-roleplay-protocol)
5. [The ethics line](#5-the-ethics-line)

## 1. The prep pack template
Draft every section before the conversation; mark estimates as estimates.

```
NEGOTIATION PREP — <counterparty> — <subject>

SITUATION
  What they proposed / what happened, in one paragraph. Deadline, if any (and whether
  it is real or asserted).

INTEREST MAP
  Ours:    <ranked interests — total cost, service quality, predictability, ...>
  Theirs:  <inferred interests — revenue target, cost to serve, retention, risk, the
            negotiator's own incentives — each marked (inferred) until tested>

BATNA TREE
  Ours:   Branch A: <alternative, cost, timeline, switching pain> → value: <net>
          Branch B: <...>
          Strongest branch = the walk-away floor: <state it plainly>
          Improvement actions before we talk: <e.g. get a live competing quote>
  Theirs (estimated): what losing us costs them — volume, balances, share of wallet,
          reference value. This is the leverage map.

OBJECTIVE CRITERIA TABLE
  | Item in dispute | Their number | Benchmark / precedent | Source |
  (for bank fees: paste the bank-fee-analysis AFP-coded benchmark table here)

TARGETS
  Open: <ambitious but criterion-defensible>   Target: <expected landing>
  Walk-away: <set by the human, before the conversation, in writing>

ACCUSATION AUDIT
  The worst things they might think or say about us, each with the line that names it.

CALIBRATED-QUESTION BANK
  6–10 how/what questions tailored to their interests (see §2).

CONCESSION PLAN
  What we can give, what each item costs us, and what we require in return for each.
  Nothing on this list moves without a reciprocal.

OPTIONS FOR MUTUAL GAIN
  Pie-expanding trades to raise before dividing value.
```

## 2. Tactic catalog with example lines
| Tactic | What it is | Example line |
|---|---|---|
| Accusation audit | Name their likely objections first, before they do | "You probably think we're a small account that's shopping you on price." |
| Mirror | Repeat their last 1–3 words as a question, then silence | Them: "Costs have gone up across the board." — You: "Across the board?" |
| Label | Name the emotion or position, tentatively | "It seems like this increase is coming from above you." |
| Calibrated question | An open how/what that hands them your problem | "How am I supposed to justify this fee to my board?" |
| Calibrated question (implementation) | Test feasibility without saying no | "What happens to the relationship pricing if we consolidate the other accounts here?" |
| "That's right" | Summarize their view until they confirm it — that, not "you're right", signals real agreement | "So the branch network costs rose and every client is seeing some increase — that's the picture?" |
| Dynamic silence | After a mirror, label, or question — stop talking | (count to four; they fill the space) |
| No-oriented question | Let them say "no" safely; "no" feels protective and starts real talk | "Is it unreasonable to ask where this number comes from?" |
| Anchor to criteria | Tie every number to a benchmark, never to pressure | "The AFP-coded benchmark for this service is $0.09; you're proposing $0.14. Help me understand the gap." |
| Trade, don't give | Every concession carries a reciprocal | "If you hold the unit price, we'll move the operating accounts over." |

Avoid "why" questions — they read as accusations ("Why did you raise this?"). Recast as
"what" or "how" ("What drove the change?").

## 3. Worked example: the bank fee increase
The bank announces a 12% increase on ACH origination and lockbox unit prices.

**Inputs from `banking-skills:bank-fee-analysis`** (run it first — it builds the case):
the AFP-coded unit-price benchmark table, the volume × unit price driver ranking, the
ECR / compensating-balance trade-off math, and the lever list (waive or reduce unit
prices, raise the ECR, cut the reserve factor, consolidate accounts). Those tables *are*
this negotiation's objective criteria.

**Prep pack highlights:**
- Interests — Bank: fee revenue target, cost to serve, keeping deposits and share of
  wallet, the relationship manager's retention numbers (inferred). Us: total relationship
  cost, service quality, price predictability, board-defensible pricing.
- BATNA — Branch A: RFP to two competing banks (realistic 6–9 month switch, conversion
  cost estimated); Branch B: consolidate accounts and shift to balance compensation at
  the current ECR. Strongest branch priced; walk-away set from it by the human.
  Their side: our balances fund their lending; losing the relationship costs more than
  the increase earns.
- Accusation audit — "You probably think we're too small to price like your big
  clients." / "You may think we'd never actually go through an RFP."
- Calibrated questions — "How am I supposed to justify a 12% increase to my board when
  the benchmark for this AFP code is $0.09?" / "What would it take to qualify for the
  pricing tier above ours?"
- Options for mutual gain — a longer relationship commitment for benchmark unit prices;
  moving merchant volume in exchange for a higher ECR; dropping the services the
  driver ranking shows we no longer use.
- Close — accept only a package that beats the strongest BATNA branch; if the bank's
  best offer lands below it, walk to the RFP. No splitting the difference below the line.

## 4. Rehearsal roleplay protocol
Ask the LLM to play the counterpart *from the interest map* — it argues their interests,
not a caricature. Run three passes: (1) cooperative, (2) positional hardliner ("the
increase is non-negotiable"), (3) evasive ("I'll have to check with pricing"). The human
practices mirrors, labels, and calibrated questions out loud; after each pass, debrief
against the prep pack — which interests surfaced, which criteria held, whether any answer
drifted toward the walk-away line. Rehearsal is the LLM's last move: the live
conversation belongs to the human.

## 5. The ethics line
Honest tactics only — this file coaches preparation and empathy, never deception:
- Never claim a BATNA you don't have, invent a competing offer, or cite a fabricated
  benchmark. A bluff discovered destroys the criteria strategy — your numbers stop
  being trusted standards and become noise.
- Tactical empathy is genuine perspective-taking. Mirrors and labels work because they
  are real listening; performed as manipulation, they read as manipulation.
- Most counterparties in this library's domains (banks, processors, carriers, vendors)
  are repeat relationships. Reputation compounds across rounds; a deal extracted
  dishonestly is repaid at the next renewal.
- If the counterpart lies, the response is criteria and BATNA — verify, anchor to the
  benchmark, or walk — not lying back.
