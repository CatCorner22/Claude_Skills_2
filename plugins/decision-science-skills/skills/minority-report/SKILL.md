---
name: minority-report
description: >-
  Runs a precognition cell over any decision: builds three to five named, internally
  coherent, structurally different future scenarios (Shell-lineage scenario planning —
  never best/expected/worst on one axis), turns one variable at a time to find which
  single change flips the outcome ranking, and always files the minority report —
  the dissenting future given full voice, because suppressing it is the failure the
  namesake story is about. Adds the reflexivity check (acting on a forecast changes
  the futures it forecast), probabilities only via reference-class base rates with
  honest bands, and ends with per-scenario tripwires and a decision log. Scenarios
  are rehearsals, not predictions — the human owns the choice. Use when weighing
  future outcomes, testing what happens if a variable changes, or deciding under
  uncertainty. Triggers: precog, precognition, minority report, run the scenarios,
  future outcomes, what happens if X changes, scenario planning, branch the futures.
metadata:
  version: "1.1.0"
  source: >-
    Commissioned by the user, inspired by the precogs of Minority Report (Philip K.
    Dick's story and the film — homage in triggers and teaching only; no affiliation).
    The mechanism is documented practice: Shell-lineage scenario planning
    (Wack/Schwartz), sensitivity analysis, and Merton's reflexivity. The name is also
    the pre-existing parliamentary term — a dissenting committee report — which is
    exactly the artifact this skill refuses to suppress.
---

# Minority Report (the precog cell)

Three precogs, one tank — and the system's fatal flaw was never the visions. It was
the filing cabinet: when the three reports disagreed, the majority went to the ball
and the minority report went in a drawer. This skill is that machine rebuilt with the
drawer welded open. It generates multiple realistic futures for whatever you are
deciding, shows you which variable each future turns on, and treats the dissenting
scenario as the most valuable page in the file — because the futures you rehearse are
the ones that cannot ambush you.

## When to use
- A decision needs its future outcomes explored: a project direction, an offer, a
  launch, a career move, an architecture choice, a case strategy.
- The user asks "what happens if X changes" — a variable (funding, timeline, a
  ruling, a hire, demand) needs turning to see which outcomes flip.
- A plan rests on one confident picture of the future and nobody has written down
  what else could happen.
- Not for: playing a thinking adversary move-by-move →
  `decision-science-skills:tabletop-wargaming`; imagining the causes of one failure
  before commitment → `decision-science-skills:pre-mortem` (a scenario cell holds
  futures where things go RIGHT differently, too); base-rate estimates for a single
  quantity → `decision-science-skills:reference-class-forecasting` (it feeds this
  skill's probability discipline); statistical extrapolation from history →
  `machine-learning-skills:time-series-forecasting`; deciding mid-flight whether a
  committed plan still deserves its timeline → `decision-science-skills:the-challenger`
  (this skill runs BEFORE commitment and re-arms it with tripwires).

## Do it
Framing, variable sorting, a domain-neutral worked scenario construction, the minority-report
rule, and the one-variable turn are in `references/scenario-cell-method.md`.

1. **Frame the decision, not the future.** Write the decision this cell serves, the
   time horizon, and what would count as a good outcome. Scenario work without a
   decision attached produces interesting fiction; the decision is what makes it
   precognition.
2. **Sort the driving variables.** List everything that materially shapes the
   outcome, then split: NEAR-CERTAINTIES (trends you can bank on across the horizon)
   versus CRITICAL UNCERTAINTIES (variables that could genuinely go multiple ways and
   matter most). The uncertainties become the scenario axes; the certainties appear
   in every scenario. If systems structure is doing the driving, draft the loops
   first (`decision-science-skills:systems-thinking`).
3. **Build 3–5 structurally different futures.** Not best/expected/worst — that is
   one future at three volumes. Take the two or three critical uncertainties and
   build scenarios where they resolve DIFFERENTLY: each future internally coherent,
   named memorably (names are handles for meetings), narrated concretely (what a
   Tuesday looks like inside it), with its winners, losers, and second-order effects
   (the LLM drafts; the human corrects — the correcting is where the thinking
   happens).
4. **File the minority report — always.** One scenario must be the dissenter: the
   future that disagrees with where the room is already leaning, argued at FULL
   strength, not straw-manned into a token risk paragraph. It gets equal narrative
   quality, equal indicator coverage, and it is never deleted to make the deck
   cleaner. The namesake story is about exactly this suppression; the cell exists to
   make it impossible.
5. **Turn one variable.** The sensitivity pass, and the user's founding ask: put the
   scenarios in a working plausibility order first (step 7 disciplines it; a rough order
   is enough to see movement), then hold everything else fixed, change ONE variable
   (the deadline slips a quarter; the ruling goes the other way; the key person leaves;
   demand halves), and record which scenario rankings flip. Variables whose turn reorders
   the outcomes deserve monitoring money; variables that flip nothing can stop
   consuming meeting time. Then list the ROBUST MOVES — actions that pay off in every
   scenario, the minority report included. These are the cell's highest-value product:
   decisions you can make now without resolving any uncertainty (in the reference's
   worked case, negotiating data export wins whether you build, keep, or get squeezed).
6. **Run the reflexivity check.** Acting on this report changes the futures it
   reports — announce a downturn plan loudly enough and you can cause the downturn;
   prepare visibly for a risk and you may prevent it (which then looks like the
   forecast was wrong). For each scenario ask: does the action this report
   recommends make this future MORE or LESS likely? Predictions that alter their own
   outcome aren't failures — they are the point. That is Anderton's problem, and it
   is a real, named property of social prediction (Merton's self-fulfilling and
   self-defeating prophecies), not a paradox to fear.
7. **Attach probabilities honestly or not at all.** If a reference class exists,
   anchor each scenario's likelihood to base rates
   (`decision-science-skills:reference-class-forecasting`) and give bands, not
   point percentages. If no reference class exists, RANK the scenarios by
   plausibility and say plainly that the ranking is judgment. A confident fake
   percentage is worse than an honest ordering.
8. **Arm the tripwires and log the decision.** Each scenario gets 2–3 observable
   EARLY INDICATORS — things the world would show soon if that future is arriving —
   plus who watches each one and the threshold that fires it (feed
   `safety-and-reliability-skills:break-glass-playbooks` where a fired tripwire
   needs pre-authored moves). Close with the decision log: what was chosen, which
   scenario it bets on, which robust moves were taken, what evidence would revisit it,
   and the next review trigger
   (`decision-science-skills:the-challenger` takes it from there).

## Why / learn
The real-world anchor is documented practice, not fiction: scenario planning as
developed at Royal Dutch Shell (Pierre Wack's planning group; Peter Schwartz's *The
Art of the Long View*) — famously credited with preparing Shell for the 1970s oil
shock — replaced single-point forecasts with a small set of structurally different,
internally coherent futures, because the value of scenarios is not predicting which
one arrives but making the organization UNSURPRISABLE across the set. The method's
core insight survives every domain transfer: separating what is effectively certain
from what is critically uncertain forces the discovery that most planning conflates
the two. Sensitivity analysis supplies the second blade — one-variable-at-a-time
turning is how engineers find which inputs actually govern a system — and reflexivity
supplies the third: Robert Merton named the self-fulfilling prophecy, and every
social forecast lives with it (the PKD story dramatizes it perfectly: Anderton's own
foreknowledge changes what he does). The fiction contributes the honesty rule. In
Dick's story, the three precogs' reports disagreed, and the system filed the
majority and buried the dissent — the plot IS the discovery that the buried minority
report was load-bearing. So this cell's non-negotiable is structural: the dissenting
scenario is always filed, at full strength, by name. And the fiction contributes one
moral, stated once: precrime convicted people for futures that hadn't happened. A
scenario cell informs choices; it never convicts anyone — not a person, not a
project — on an unhappened future. Forecast to choose, never to punish the
prediction. Humans adjudicate; the cell drafts.

## Common mistakes
- Best/expected/worst → one future at three volumes; build futures that differ in
  STRUCTURE (different uncertainties resolving differently), not amplitude.
- Suppressing or straw-manning the dissenting scenario to keep the deck clean → the
  namesake failure; the minority report ships at full strength or the cell is
  theater.
- Scenario fiction without a decision attached → frame the decision first; the cell
  serves a choice.
- Point probabilities from nowhere ("Scenario B: 35%") → base-rate bands or honest
  ranking; never decorative precision.
- Skipping the reflexivity check → the report's own publication is an intervention;
  ask which futures the recommended action feeds.
- Scenarios without early indicators → futures you can't see arriving are futures
  you can't act on; every scenario gets watchable tripwires.
- Treating the cell's output as a verdict on people or projects → the precrime
  moral; forecasts inform, humans decide, nothing unhappened convicts.
- Re-running the cell forever instead of deciding → the log and the next review
  trigger close the loop; deciding is the deliverable.

## Tailor to your environment
Record in `references/your-environment.md`: the standing decisions this cell serves
(and their horizons), your reference classes and where their base rates live, who
watches which tripwires, and where scenario decks and decision logs are filed.
Sensitive specifics go in `*.private.md` (git-ignored).

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/minority-report.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/scenario-cell-method.md — the full protocol: variable sorting, scenario
  construction with a worked domain-neutral example, the minority-report rule, the
  one-variable turn table, reflexivity patterns, probability discipline, tripwire
  design, and the decision-log template
- references/your-environment.md — your decisions, reference classes, watchers,
  filing (fill in)
