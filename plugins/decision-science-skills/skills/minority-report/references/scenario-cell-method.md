# The scenario-cell method (full protocol)

Contents: 1. Framing · 2. Variable sorting · 3. Scenario construction (worked) ·
4. The minority-report rule · 5. The one-variable turn · 6. Reflexivity patterns ·
7. Probability discipline · 8. Tripwires · 9. The decision log · 10. Provenance notes

## 1. Framing
Three lines before any futures get written:
- **Decision:** the choice this cell serves ("commit to rebuilding the scheduling
  module this quarter, or defer").
- **Horizon:** how far out the futures run (a quarter, a year, five years — pick the
  horizon the decision actually spans; scenario drift begins where the horizon blurs).
- **Good outcome:** what winning means, stated before the futures exist, so scenario
  quality can't quietly redefine it (the Kirk move belongs in
  `decision-science-skills:no-win-drills`, declared — not here, hidden).

## 2. Variable sorting
List every variable that materially shapes the outcome. Sort into:
- **Near-certainties** — trends stable across the horizon (demographics, signed
  contracts, physics, the fiscal calendar). These appear identically in every
  scenario; disagreement about them means someone is planning on hope.
- **Critical uncertainties** — variables that could genuinely resolve multiple ways
  AND move the outcome materially. Rank by (impact × genuine uncertainty); the top
  two or three become scenario axes.
Test for miscategorized hope: for each "certainty," ask what evidence would make it
uncertain. If the evidence is cheap and nobody has looked, it is not a certainty yet.

## 3. Scenario construction — worked example (domain-neutral)
Decision: a two-person practice is deciding whether to build custom scheduling
software or keep the commercial tool. Horizon: 18 months. Critical uncertainties:
(A) practice growth (flat vs. +50%), (B) vendor trajectory (improves vs. stagnates
vs. raises prices sharply).

Build 3–5 futures where the uncertainties resolve DIFFERENTLY — each named, coherent,
concrete:

- **"Steady State"** — growth flat, vendor stagnates but stays cheap. A Tuesday here:
  the tool is mildly annoying, twice a week someone double-books, the workaround
  wiki grows. Custom build would have been a luxury.
- **"Growth Squeeze"** — +50% growth, vendor stagnates. A Tuesday: front desk spends
  90 minutes on manual conflict resolution; the tool's limits now cost real revenue.
  The build pays for itself; every month of deferral hurts.
- **"Vendor Rescue"** — growth either way, vendor ships the two missing features.
  A Tuesday: the pain is gone; a custom build would now be a liability someone must
  maintain. Deferral was free money.
- **"Price Cliff"** (minority report — the room is leaning build-or-keep, and this
  future says the REAL variable was never features) — vendor triples prices at
  renewal, betting on lock-in. A Tuesday: the practice is hostage-negotiating with
  its own calendar. Neither building nor keeping was the decision that mattered;
  DATA PORTABILITY was, and it had to be arranged a year before renewal.

Construction rules: each future is internally coherent (its pieces cause each
other); each names winners, losers, and one second-order effect; each is narrated at
Tuesday-level concreteness (abstract futures can't be recognized when they arrive);
names are short enough to say in a meeting ("we're drifting into Growth Squeeze").

## 4. The minority-report rule
One scenario must dissent from the room's lean — and it is built to the SAME quality
bar as the favorites:
- Full narrative, full indicator set, full sensitivity treatment. A one-paragraph
  "risks" appendix is a suppressed minority report wearing a disguise.
- It is presented by name in any readout, never merged "for simplicity."
- The test: if the dissenting future arrived, would the file have warned you in
  time, in detail, with tripwires? If not, the cell replicated the namesake failure.
- Dissent content rules: it disagrees STRUCTURALLY (a different variable governs,
  a different mechanism dominates), not just in degree; and it is argued as its best
  self — the strongest honest case that the majority view is wrong. (The
  steelman-the-dissent norm is shared with `decision-science-skills:the-challenger`,
  which restates objections before deciding.)

## 5. The one-variable turn
Hold all else fixed; turn one variable; record what flips. What flips is the CHOICE,
not the scenario label: turning a variable that is itself a scenario axis relocates
you between scenarios by construction (growth flat → +50% with the vendor held at
"stagnates" *is* the move from Steady State to Growth Squeeze), so a row written in
scenario names can only ever read YES and says nothing about whether the variable
earns monitoring. Rank the options under each resolution instead. Table format:

| Variable turned | Turn applied | Best choice before | Best choice after | Flips? |
|---|---|---|---|---|
| Growth | flat → +50% | keep (a build would be a luxury) | build (it now pays for itself) | YES |
| Vendor prices | stable → 3× at renewal | keep | portability first | YES |
| One dev leaves | staffed → short | build | keep (a build is unviable short-staffed) | YES |
| Office paint color | any | — | — | no |

Read the table two ways: variables that change the best choice deserve monitoring and
option-preserving moves (the "Price Cliff" flip says: negotiate data export NOW,
regardless of the build decision — a robust move that wins across futures);
variables that flip nothing are officially allowed to stop consuming attention.
Robust moves — actions that pay off across ALL scenarios — are the cell's best
product; list them explicitly.

## 6. Reflexivity patterns
For each scenario ask: does the ACTION this report recommends feed or starve this
future? Named patterns to check:
- **Self-fulfilling** — preparing loudly for a price war can start one; forecasting
  attrition and hiring backups can signal distrust that causes attrition.
- **Self-defeating** — the risk you visibly prepare for gets prevented, making the
  forecast look wrong; budget for looking wrong this way (it is success).
- **Observer effects on counterparties** — a scenario deck that leaks becomes a
  signal; decide what this file would mean if the other side read it.
The check's output is one line per scenario: "acting as recommended makes this
future [more/less/un] likely, because…" (Merton's self-fulfilling prophecy is the
named social-science anchor; the PKD dramatization is Anderton acting on his own
foreknowledge.)

## 7. Probability discipline
- Reference class exists → base-rate bands: "projects of this type slip their first
  ship date in roughly 6 of 10 comparable cases" beats "70%."
  (`decision-science-skills:reference-class-forecasting` owns the base-rate craft.)
- No reference class → rank scenarios by plausibility, in words, and label the
  ranking as judgment. Ordinal honesty beats cardinal theater.
- Never: point percentages with no lineage, probabilities that sum to a tidy 100%
  because the deck wanted them to, or precision that outruns the horizon.

## 8. Tripwires
Each scenario gets 2–3 early indicators, each passing the quality bar:
- **Observable** — a number or event the world will actually show, soon enough to
  act ("vendor renewal terms arrive with >20% increase" beats "vendor gets greedy").
- **Watched** — a named person checks it on a named cadence.
- **Thresholded** — the value that fires it is written down now, calm-headed, so the
  future room doesn't renegotiate it under pressure.
A fired tripwire should land somewhere prepared:
`safety-and-reliability-skills:break-glass-playbooks` pre-authors the first moves;
`decision-science-skills:the-challenger` owns the revision review it obligates.

## 9. The decision-log template
```
DECISION: <what was chosen>
DATE / CHAIR: <who owned it>
BETS ON: <which scenario(s) this choice performs best in>
EXPOSED TO: <which scenario(s) it performs worst in — include the minority report>
ROBUST MOVES TAKEN: <actions that pay off across futures>
WOULD REVISIT IF: <evidence, thresholds>
TRIPWIRES ARMED: <indicator — watcher — threshold>
NEXT REVIEW TRIGGER: <date or event; hands to the-challenger>
```

## 10. Provenance notes
Scenario planning's Shell lineage (Pierre Wack's group; Peter Schwartz, *The Art of
the Long View*) and its oil-shock reputation are standard, well-documented business
history — cited here at practice level. Merton named the self-fulfilling prophecy in
1948. The fiction: Philip K. Dick's "The Minority Report" (1956 story; 2002 film) —
homage only, no affiliation; the parliamentary sense of "minority report" (a
dissenting committee report) long predates the story, which is why the skill can
wear the name as a mechanism description. The precrime moral is the story's, kept
deliberately: nothing unhappened convicts anyone here.
