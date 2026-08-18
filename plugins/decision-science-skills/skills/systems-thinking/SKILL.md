---
name: systems-thinking
description: >-
  Maps the feedback structure behind a recurring mess: identifies the stocks (accumulations) and
  flows (rates), drafts the causal-loop diagram from the user's prose —
  nodes, signed links, loop polarity, rendered as Mermaid for the human to correct — classifies
  loops as reinforcing or balancing, finds the delays that produce oscillation and overshoot,
  checks the classic archetypes (fixes-that-fail, shifting-the-burden, limits-to-growth,
  escalation), locates interventions on a simplified Meadows leverage ladder, anticipates policy
  resistance, and names what to measure to see whether the loop actually moved. Use when a
  problem keeps coming back after being fixed, a fix bred new problems elsewhere, growth stalled
  against an unseen limit, or two sides keep escalating. Triggers: systems thinking, feedback
  loop, stock and flow, leverage point, unintended consequences, vicious cycle, virtuous cycle,
  second-order effects, the problem keeps coming back, policy resistance.
metadata:
  version: "1.1.0"
---

# Systems thinking (the structure behind recurring problems)

System dynamics is Jay Forrester's field; Donella Meadows' *Thinking in Systems* is its most
accessible statement, and her leverage-points essay is the canonical ladder of intervention
points (this skill uses a simplified form of it and says so). Peter Senge's *The Fifth
Discipline* popularized the system archetypes. The working core they share: when a problem keeps
happening, the cause is a structure — stocks, flows, feedback loops, delays — not an event, and
not a person.

## When to use
- A problem that keeps coming back after being "fixed," or a fix that bred new problems somewhere
  else — the tell that a loop, not an event, is in charge.
- Turning a described mess into an explicit structure: the assistant does the diagramming labor
  (stocks and flows, causal-loop diagram, signed links, loop polarity) from the user's prose, and
  the human corrects it.
- Choosing where to intervene when candidate fixes compete — a parameter tweak vs. a new
  information flow vs. a rule or goal change.
- Before pushing a policy, anticipating who will push back and how (policy resistance).
- Not for: single-bottleneck throughput improvement → see
  `continuous-improvement-skills:theory-of-constraints`. A bottleneck is one kind of leverage
  point; use this skill first when you don't yet know which kind you face.
- Not for: one incident's causal chain → see `continuous-improvement-skills:root-cause-analysis`.
  When the "chain" bites its own tail — the fifth why lands back on the first — come here.
- Not for: whether a plan should continue as evidence changes → see
  `decision-science-skills:the-challenger`; imagining discrete ways a plan fails → see
  `decision-science-skills:pre-mortem`.
- Related: a value-stream map is a specific, quantified flow diagram of one process →
  `continuous-improvement-skills:value-stream-mapping`; estimates that come out of any
  intervention plan get anchored by `decision-science-skills:reference-class-forecasting`.

## Do it
The full stock/flow drill, causal-loop drafting protocol with Mermaid conventions, a worked
support-ticket example, the archetype field guide, and the leverage ladder with worked
intervention choices are in `references/systems-method.md`.

1. **Restate the mess as behavior over time.** Not "who did what last week" but "what pattern
   repeats": growth that stalls, a metric that oscillates, a fix that decays. Sketch or describe
   the trajectory. If the user offers only the latest event, ask for the history — structure
   shows up only across time.
2. **Separate stocks from flows.** A stock is an accumulation you could measure at a frozen
   instant (a balance, a backlog, headcount, trust); a flow is a rate per unit time that fills or
   drains it (a payment run, ticket arrivals, hires, resolutions). Confusing them is a whole
   error class: a stock keeps rising as long as inflow exceeds outflow, even while everyone
   celebrates that the inflow "improved." Name each stock with the flows that feed and drain it.
3. **Draft the causal-loop diagram from the user's prose.** This is the assistant's labor: pull
   out the causal claims, make each a node, link them with signed edges (`+` = same direction,
   `−` = opposite), and close the loops. Render as Mermaid where a picture helps. Then hand it
   to the human to correct — they live in the system; the diagram is a proposal, not a verdict.
4. **Classify each loop and mark the delays.** Count the `−` links around a loop: an even count
   (or zero) makes it reinforcing (R — amplifies, compounds, spirals), an odd count makes it
   balancing (B — seeks a level, resists change). Then mark every delay explicitly: delays are
   where oscillation and overshoot come from, because actors keep pushing on a loop whose
   response hasn't arrived yet.
5. **Check the archetypes.** Compare the structure against the classic recurring shapes:
   *fixes-that-fail* (the quick fix relieves the symptom now and feeds it later),
   *shifting-the-burden* (the symptomatic fix works just well enough that the fundamental fix
   never happens and capability atrophies), *limits-to-growth* (a reinforcing engine slows
   against a balancing limit; pushing the engine harder doesn't move the limit),
   *tragedy-of-the-commons* (individually rational draws deplete a shared stock),
   *escalation* (each side responds to the other's last move; each sees defense, the system
   spirals), and *success-to-the-successful* (early winners get more resources, so they keep
   winning regardless of merit). A match imports known traps and known escape routes.
6. **Locate the intervention on the leverage ladder** (simplified from Meadows' twelve points):
   parameters < buffers < feedback loops < information flows < rules < goals. State which rung
   each candidate fix sits on. Higher rungs beat parameter-tuning because loops compensate for
   parameter changes — the structure that produced the old number reasserts itself — while
   changing what a loop sees (information), what is permitted (rules), or what the system is
   for (goals) changes what every parameter below does.
7. **Anticipate policy resistance.** The system pushes back: the current level of a stock is
   usually being *held* there by actors' goals. Ask who benefits from the current level, and who
   will compensate when you push it — more pressure on a stock actors are defending yields
   effort spent on both sides and a stock that barely moves.
8. **State what to measure.** Both flow rates separately (never just the stock — a stock can
   flatline while both its flows double), the stock's trajectory, the length of the key delay,
   and one loop-specific tell (e.g., a reopen rate for a fixes-that-fail structure). Route the
   quantitative test — did the loop actually move? — to
   `data-analytics-bi-skills:statistical-inference` or your data-analysis skills.

**Division of labor.** The assistant proposes structure — stocks, flows, loops, polarity,
archetype matches, candidate rungs — because that labor is mechanical once the prose is parsed.
The human corrects the diagram and owns the intervention choice: a causal-loop diagram is a
hypothesis about structure, and only someone inside the system (or data) can say whether the
hypothesized links are real.

## Why / learn
**Event-thinking misses structure.** "Who did what" explains one occurrence; it cannot explain
recurrence. If the same failure happens under different people on different days, the people are
not the variable — the structure is. Systems thinking swaps "why did this happen?" for "what
makes this keep happening?", which is a different question with a different kind of answer.

**The bathtub intuition.** A stock changes *only* through its flows — the water level responds
to nothing but the faucet and the drain. Most magical-seeming system behavior is bathtub
arithmetic: the backlog grows though everyone works harder (inflow still exceeds outflow); debt
rises though the deficit fell (the inflow shrank but never went below the outflow). Anyone who
holds the bathtub picture stops being surprised by these.

**Delays make "we fixed it" and "it's back" both true.** A balancing loop with a delay
overshoots: you act, nothing visibly changes (the response is in transit), you act harder, then
both responses land at once. The fix worked *and* the oscillation it caused brought the problem
back. Without the delay marked on the diagram, each swing looks like a fresh, unrelated event.

**Unintended consequences are usually a balancing loop you didn't draw.** When a change produces
an opposite, compensating reaction — traffic returns after the road widens, spend returns after
the cut — that is not bad luck; it is a loop that was always there, invisible until you pushed
on it. Drawing the mess *before* intervening is how you meet those loops on paper instead of in
production.

**Honest limits.** A causal-loop diagram is qualitative: it says which loops exist and in which
direction they push, not which loop dominates or when. Two people can agree on the diagram and
disagree on the outcome, because dominance depends on strengths and delays the picture doesn't
carry. Treat the diagram as a hypothesis to test — with the measurements from step 8 and the
data skills — never as proof. That honesty is what separates using the diagram from decorating a
prior belief with arrows.

## Common mistakes
- Managing the stock by staring at the stock → set targets on the flows; only a flow can move a
  stock, and name *which* flow the fix changes.
- Calling a stock a flow or vice versa ("revenue" when you mean cash on hand; "we cut the
  backlog" when arrivals merely dipped) → apply the instant test: measurable at a frozen moment
  = stock; only per-interval = flow.
- Drawing only the reinforcing loop → every growth episode looks permanent and every decline
  looks fatal; find the balancing loop that will eventually bind (limits-to-growth).
- Leaving delays off the diagram → oscillation gets diagnosed as randomness and answered with
  overcorrection, which feeds the oscillation.
- Tuning parameters because they're the visible knobs → loops compensate; climb the ladder and
  say explicitly why you're intervening at the rung you chose.
- Labeling every loop "vicious" → check polarity honestly; some cycles are balancing loops doing
  their job, and "fixing" those creates the real problem.
- Treating the diagram as proof → it is a hypothesis about structure; state the measurements
  that would falsify it and route the test to the data skills.
- Archetype-spotting as the finish line → the archetype names the trap; you still have to locate
  the intervention rung and define the measurement.

## Tailor to your environment
Record your recurring messes in `references/your-environment.md`: the stocks your organization
actually tracks (and the flows nobody measures), fixes that were tried and decayed, the actors
known to compensate when policy pushes, and where the behavior-over-time data lives. Keep
committed content structural — real figures, names, or client data belong in
`your-environment.private.md` (git-ignored), never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/systems-thinking.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/systems-method.md — the stock/flow identification drill, the causal-loop drafting
  protocol with Mermaid conventions and a worked support-ticket backlog example, the archetype
  field guide, and the leverage ladder with worked before/after intervention choices
- references/your-environment.md — your recurring messes, measured stocks and unmeasured flows,
  decayed fixes, and known compensating actors
