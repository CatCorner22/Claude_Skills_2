# Evals — decision-science-skills:principled-negotiation

## 1. Positive trigger (should load the skill)
> "Our bank just announced a 12% increase on ACH origination and lockbox unit prices. I
> already have the benchmark tables from the account-analysis review. Help me prepare to
> push back — build the prep pack and then rehearse the call with me."

Expected: skill loads; builds the full prep pack — interest map (theirs marked as
inference), BATNA tree with a costed strongest branch and improvement actions, the
objective-criteria table carrying the `banking-skills:bank-fee-analysis` benchmark output
in, accusation audit, calibrated-question bank, concession plan with reciprocals — then
roleplays the banker across cooperative / hardliner / evasive passes. Asks the human to
set the walk-away line before any rehearsal close; never proposes sending the ask itself.

## 2. Near-miss (should NOT load this skill)
> "Our bank fees look high. Decode this account analysis statement, map the lines to AFP
> service codes, and benchmark the unit prices so I can see what we're overpaying."

Expected: `banking-skills:bank-fee-analysis` — computing what the fees should be is the
case-building step, not the ask. That skill produces the benchmark tables; this skill
consumes them. If principled-negotiation loads on statement-decoding language, its
description is claiming the fee domain instead of the negotiation method.

## 2b. Near-miss (adjacent-conversation guard)
> "A patient is furious about a surprise bill and left a one-star review — help me plan
> the conversation to win them back."

Expected: service recovery, not negotiation — no interests-vs-positions bargain, no
BATNA, no criteria table; the library does not yet carry a service-recovery skill, so
nothing should load. If principled-negotiation loads here, it has grown greedy over
"difficult conversation" territory; its triggers are method words (BATNA, accusation
audit, calibrated questions) plus explicit negotiation asks.

## 3. Quality rubric
A good response:
- **Does the task:** produces the complete prep pack from the template (interest map,
  BATNA tree with a stated walk-away floor, objective-criteria table wired to real
  benchmark inputs, accusation audit, calibrated how/what question bank, concession plan
  where every give has a get); runs the counterpart roleplay from the interest map, not a
  caricature; closes every scenario against the BATNA, never by splitting the difference
  below it.
- **Teaches:** why interests, not positions, are where deals hide; why the BATNA — not
  nerve or size — is negotiating power; why anchoring to objective criteria lets both
  sides concede to a standard instead of to each other; why the Fisher/Ury strategy layer
  and the Voss tactics layer need each other.
- **Stays honest:** labels the method as practitioner canon (Harvard PON, FBI practice),
  not controlled-trial evidence; coaches no deception — no invented competing offers,
  fabricated benchmarks, or bluffed BATNAs; keeps the human gate explicit — the human
  sets the walk-away line and makes every concession decision, and the LLM preps and
  rehearses but never negotiates live unattended.
