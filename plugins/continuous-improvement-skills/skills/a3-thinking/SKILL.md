---
name: a3-thinking
description: >-
  Structures a problem, its analysis, and countermeasures on a single A3 page using the PDCA
  cycle, as a thinking and alignment tool rather than a form to fill — the Toyota practice
  codified by Sobek & Smalley and Shook. Seven boxes read left to right: background,
  data-backed current condition, measurable target, verified root cause, countermeasures
  traced to causes, an owned implementation plan, and follow-up filled in later with actual
  results. Drafted with the affected people, nemawashi-style, so consensus
  is built before the decision meeting; fits any problem story — an analyst's
  process fix, an attorney's intake bottleneck, an ops manager's error spike, a developer's
  flaky pipeline. Use when proposing an improvement, telling a problem-solving story on one
  page, building consensus around a change, or running a PDCA cycle. Triggers: A3, A3
  report, A3 problem solving, PDCA, plan do check act, problem solving, countermeasure,
  one-page proposal, nemawashi.
metadata:
  version: "1.1.0"
---

# A3 thinking

The A3 is a one-page problem-solving storyboard, named for the paper size it fits on. The
practice grew inside Toyota and was codified for English-speaking readers by Sobek &
Smalley (*Understanding A3 Thinking*) and Shook (*Managing to Learn*). Its point is not the
form: it is the reasoning discipline the single page forces, and the conversations the
draft creates on its way to a decision.

## When to use
- Proposing an improvement or a change and needing to bring people along with the reasoning,
  not just the conclusion — an analyst pitching a process fix, an attorney tightening an
  intake step, an ops manager attacking an error spike, a developer proposing a pipeline
  change.
- Telling a complete problem-solving story — background through follow-up — on a single page.
- Running a **PDCA** cycle and wanting a living document that carries it.
- Not for: the deep cause hunt that feeds the analysis box → see
  `continuous-improvement-skills:root-cause-analysis`. For a full measured project with
  baselines and controls → see `continuous-improvement-skills:dmaic-problem-solving` (an A3
  can summarize it). To find *which* problem to attack across a whole end-to-end process →
  see `continuous-improvement-skills:value-stream-mapping` first.

## Do it
Fill the A3 boxes in order, left column top-to-bottom then right column. Keep the whole thing
to **one page** — the constraint is the point. `references/a3-template.md` has the layout,
box-by-box guidance, and a worked example.
1. **Title + background (Plan).** Name the problem and why it matters *to the
   business/customer* — the context a reader needs to care. One or two sentences.
2. **Current condition (Plan).** Show what's happening now *with data and a simple visual*
   (a small chart, a sketch of the process, the defect count). Facts from the gemba, not
   impressions. Choose summaries that won't mislead — a median beats a mean on skewed
   queue-time data (`data-analytics-bi-skills:descriptive-statistics`). This box usually
   persuades more than any other.
3. **Goal / target condition (Plan).** State the measurable target and by when. "Reduce X
   from a to b by <date>." A target, not a wish.
4. **Root-cause analysis (Plan).** Show *why* the gap exists — a 5 Whys chain or a fishbone,
   verified, not asserted (borrow `continuous-improvement-skills:root-cause-analysis`). The
   countermeasures must visibly follow from this box.
5. **Countermeasures (Plan → Do).** Propose changes that address the *causes* you just
   found, each traceable to a cause. Countermeasures, not "solutions" — you're counter-acting
   a specific cause. When the countermeasure needs the team to design it, run a workshop with
   the people who do the work (`continuous-improvement-skills:kaizen-and-codesign`).
6. **Implementation plan (Do).** Who does what by when — an owned, dated action table. This
   is where Plan becomes Do.
7. **Follow-up / check + adjust (Check → Act).** State how and when you'll confirm the
   target was hit (the measure and the date), what you learned, and what standardizes
   (`continuous-improvement-skills:standard-work`) or what you'll try next. Leave room to
   write the *actual* results later — the A3 is filled in over time, not at the start.

Then socialize the draft **nemawashi-style**: walk it person-by-person past everyone whose
work it touches *before* any formal review, and revise as you go. The meeting confirms a
consensus that already exists; it doesn't create one.

## Why / learn
The A3 is a *thinking process*, not a form — its value is the dialogue it forces, and that
reframes how to use it. The single-page limit isn't a formatting rule; it's a thinking
discipline. Forcing the whole story — problem, evidence, cause, countermeasure, plan,
follow-up — into one page makes you distinguish what actually matters from what merely fills
space, and a reader can hold the entire argument at once. The strict left-to-right flow
builds a chain a skeptic can walk: current condition (with data) earns the right to a
target; root-cause analysis earns the right to countermeasures; and because every
countermeasure traces back to a named cause, no one can smuggle in a pet solution that
answers no cause on the page. That visible logic is what builds **consensus** — people align
with a change when they can see the reasoning, not when they're handed a conclusion. The
nemawashi rounds (literally "going around the roots" before transplanting) are where objections
surface cheaply and early, one conversation at a time.

Underneath sits **PDCA**: Plan (background through countermeasures), Do (implement), Check
(did it hit the target?), Act (standardize the win or adjust and cycle again). The cycle is
the Shewhart/Deming loop — Deming himself credited it to Shewhart and later preferred "Study"
over "Check" (PDSA), an attribution tangle worth knowing so you don't present the cycle as
Toyota's invention. Because you fill in the Check and Act boxes with *real* results later,
the A3 is a living record of a learning loop, not a proposal frozen at kickoff — and the
honesty of writing down what actually happened, including misses, is where the learning
comes from. One more piece of lore to hold loosely: the story that Toyota chose A3 because
it was the largest sheet that fit through a fax machine is widely repeated but poorly
sourced. The load-bearing fact is the one-page constraint, not the paper's history.

## Common mistakes
- Writing it as a status report or a sell → it's a thinking tool. Show the reasoning, not just the ask.
- Spilling past one page → you've stopped prioritizing. The constraint forces clarity; respect it.
- Current-condition box with no data → opinion, not evidence. Bring facts and a small visual.
- Countermeasures that don't trace to a cause → a pet solution. Every one must answer a named cause.
- Filling every box at kickoff and never returning → skips Check/Act. Update with real results.
- A goal with no number or date → you can't check it. Make the target measurable and dated.
- Authoring it alone and presenting it → no consensus. Draft it *with* the affected people.
- Unveiling a finished A3 at the review meeting → objections arrive at the worst moment.
  Nemawashi first; the meeting confirms.
- Polishing the document instead of the thinking → a beautiful A3 with an unverified cause is
  still wrong. Spend the effort on boxes 2 and 4.

## Tailor to your environment
Wire in your current role here — the A3 is domain-neutral by design and moves with you to
whatever job you hold next. In `references/your-environment.md`, record your A3
template/tooling, your audience and review ritual (who you walk the A3 with, in what order),
your data sources for the current-condition box, and how A3s get stored and revisited. Keep
the committed file structural; real names, systems, numbers, or client situations go in
`your-environment.private.md`, which is git-ignored and never committed.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/a3-thinking.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/a3-template.md — the one-page layout, PDCA mapping, box-by-box guidance, a
  worked domain-neutral example, reviewer's walk, and canon/misattribution notes
- references/your-environment.md — your A3 template, audience, and data sources (add when supplied)
