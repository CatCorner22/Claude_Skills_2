# Revision review method — protocol, the record, the literature, worked example

Contents: §1 Facilitation script · §2 The Challenger record, held soberly · §3 The bias
literature · §4 Worked example: the go-live that should slip · §5 Decision-log template

## §1 Facilitation script (a fired trigger convenes it)

1. **Open with the trigger**: read the condition that fired, verbatim from the plan.
   State the rule: past this trigger, continuation carries the burden of proof.
2. **Zero-base round**: each participant answers in writing, before discussion —
   "Starting today, knowing what we know, would you choose this plan and this date?"
   (Written-first prevents the room from converging on the senior voice; same mechanic
   as the pre-mortem's silent round.)
3. **Deviance scan**: list anomalies now treated as routine; for each, read what the
   first report said. Ask: what changed — the evidence, or our tolerance?
4. **Both-branch costing**: revision costs (contracts, dependencies, credibility) and
   continuation-while-wrong costs (retrofit clock, blast radius), forward-looking only,
   each anchored to base rates ("the last three times we compressed testing, what
   happened?").
5. **Option widening**: slip / descope / phase / attack-the-constraint / open criteria
   change. Write at least three before comparing any.
6. **Dissent restatement**: the decision-maker restates each written objection to the
   objector's satisfaction. Only then: the decision.
7. **Log it** (§5 template) with the next trigger. Adjourn.

Timebox: 60–90 minutes. The LLM's role: draft the zero-base summaries, reconstruct the
anomaly first-reports from tickets/logs, compute the base rates, and steelman BOTH
branches — with the standing anti-sycophancy rule: it must argue the unpopular branch
at least as well as the popular one. The humans own the decision.

## §2 The Challenger record, held soberly

Seven crew members died on 1986-01-28. The elements this skill borrows are documented
in the Rogers Commission report and the subsequent sociology [snippet-only]:

- **Schedule pressure**: a high-visibility launch window and a program sold on flight
  cadence created "launch fever" — the date had constituencies the evidence didn't.
- **The burden inversion**: in the eve-of-launch teleconference, engineers who had
  always been required to prove it safe to fly were instead pressed to prove it unsafe.
  Morton Thiokol's Roger Boisjoly and colleagues objected to launching at
  unprecedented cold; management "took off the engineering hat" and reversed the
  no-launch recommendation.
- **Normalization of deviance** (Diane Vaughan's term from her study of the decision):
  O-ring erosion and blow-by, alarming when first observed, had recurred without
  catastrophe until it became "within the experience base" — tolerance grew while the
  physics stayed the same.
- **Feynman's appendix** to the Commission report closed: "For a successful technology,
  reality must take precedence over public relations, for nature cannot be fooled."

Held soberly: this skill borrows the decision-structure lessons. It does not borrow
drama, and it does not caricature the people — several of whom fought the launch and
carried it for the rest of their lives.

## §3 The bias literature

- **Sunk cost** (Arkes & Blumer, "The psychology of sunk cost" [snippet-only]): prior
  investment increases willingness to continue, though it is identical on every branch.
  The "Concorde fallacy" is biology's name for the same error — the project so famous
  for flying on sunk costs that it named the bias.
- **Escalation of commitment** (Staw, "Knee-deep in the Big Muddy" [snippet-only]):
  decision-makers responsible for a failing course allocate MORE to it than fresh
  decision-makers — self-justification compounds. Countermeasure: the Grove question
  (Grove & Moore, deciding Intel's exit from memories: "If we got kicked out and the
  board brought in a new CEO, what would he do?" — then walk out the door, come back
  in, and do it) [snippet-only].
- **Plan-continuation bias**: aviation human-factors term for continuing an original
  plan despite changed conditions; overrepresented in approach-and-landing accidents,
  strengthening near the destination ("get-there-itis") [snippet-only]. The nearer the
  date, the stronger the pull — hence triggers installed when the date was far.

## §4 Worked example: the go-live that should slip

A reconciliation-rules engine go-live dated for quarter-start. Trigger fired:
parallel-run match rate 84% against a 97% acceptance criterion two weeks out. Momentum's voice: "we've
been at this five months; the team's booked; we'll tune rules in production."

- Zero-base: starting today, no one would choose a quarter-start cutover at 84%.
- Burden check: the room was asking the engine lead to PROVE production tuning would
  fail — inverted; reset so continuation must show how 84→97 happens before the date.
- Deviance scan: "parallel-run mismatches are mostly timing noise" had become routine;
  first report had called the same pattern "unexplained variances requiring analysis."
- Both branches: slip = one quarter of dual maintenance (real, priced); continue-wrong
  = mis-matched records through a quarter-end close plus the retrofit clock on trust in
  the new engine. Base rate: the last two "tune it in production" plans took 9 and 14
  weeks.
- Options: full slip; phased go-live (one account family at 97%+ now, rest next
  quarter); descope (auto-match only, manual queue for the tail); criteria change
  (accept 90% with a documented manual-workload plan) — logged openly if chosen.
- Decision (example): phased go-live; next trigger = any account family below 95% at
  week 2. Dissent (the operations manager wanted full slip) restated and logged.

## §5 Decision-log template

```
REVISION REVIEW — <project>            Date: <date>   Chair: <name>
Trigger fired: <verbatim condition from the plan>
Zero-base result: <would we choose this plan today? summary of written round>
Deviance scan: <anomalies re-examined; tolerance vs evidence>
Branch costs (forward-looking): revise = <...> | continue = <...> | base rates: <...>
Options considered: <≥3>
Dissent(s) restated: <who, what, restatement confirmed Y/N>
DECISION: <continue / slip to <date> / descope <what> / phase <how> / stop>
Rests on: <the evidence>     Would have changed it: <the evidence that didn't appear>
Expected outcome: <what we now predict>
NEXT TRIGGER: <the condition that reconvenes this review>
```
