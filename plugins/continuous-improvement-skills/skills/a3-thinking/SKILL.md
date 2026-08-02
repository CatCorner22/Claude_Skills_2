---
name: a3-thinking
description: >-
  Structures a problem, its analysis, and countermeasures on a single A3 page using the PDCA cycle, as
  a thinking and alignment tool rather than a form to fill. Use when proposing an improvement, telling a
  problem-solving story on one page, building consensus around a change, or running a PDCA cycle.
  Triggers: A3, A3 report, PDCA, plan do check act, problem solving, countermeasure, one-page proposal.
---

# A3 thinking

## When to use
- Proposing an improvement or a change and needing to bring people along with the reasoning, not just
  the conclusion.
- Telling a complete problem-solving story — background through follow-up — on a single page.
- Running a **PDCA** cycle and wanting a living document that carries it.
- Not for: the deep cause hunt that feeds the analysis box → see
  `continuous-improvement-skills:root-cause-analysis`. For a full measured project with baselines and
  controls → see `continuous-improvement-skills:dmaic-problem-solving` (an A3 can summarize it).

## Do it
Fill the A3 boxes in order, left column top-to-bottom then right column. Keep the whole thing to **one
page** — the constraint is the point. See `references/a3-template.md` for the layout.
1. **Title + background (Plan).** Name the problem and why it matters *to the business/customer* — the
   context a reader needs to care. One or two sentences.
2. **Current condition (Plan).** Show what's happening now *with data and a simple visual* (a small
   chart, a sketch of the process, the defect count). Facts from the gemba, not impressions. This box
   usually persuades more than any other.
3. **Goal / target condition (Plan).** State the measurable target and by when. "Reduce X from a to b
   by <date>." A target, not a wish.
4. **Root-cause analysis (Plan).** Show *why* the gap exists — a 5 Whys chain or a fishbone, verified,
   not asserted (borrow `continuous-improvement-skills:root-cause-analysis`). The countermeasures must
   visibly follow from this box.
5. **Countermeasures (Plan → Do).** Propose changes that address the *causes* you just found, each
   traceable to a cause. Countermeasures, not "solutions" — you're counter-acting a specific cause.
6. **Implementation plan (Do).** Who does what by when — an owned, dated action table. This is where
   Plan becomes Do.
7. **Follow-up / check + adjust (Check → Act).** State how and when you'll confirm the target was hit
   (the measure and the date), what you learned, and what standardizes or what you'll try next. Leave
   room to write the *actual* results later — the A3 is filled in over time, not at the start.

## Why / learn
The A3 is a *thinking process*, not a form — its value is the dialogue it forces, and that reframes how
to use it. The single-page limit isn't a formatting rule; it's a thinking discipline. Forcing the whole
story — problem, evidence, cause, countermeasure, plan, follow-up — into one page makes you distinguish
what actually matters from what merely fills space, and a reader can hold the entire argument at once. The
strict left-to-right flow builds a chain a skeptic can walk: current condition (with data) earns the
right to a target; root-cause analysis earns the right to countermeasures; and because every
countermeasure traces back to a named cause, no one can smuggle in a pet solution that answers no cause on
the page. That visible logic is what builds **consensus** — people align with a change when they can see
the reasoning, not when they're handed a conclusion, so the A3 is really a tool for shared understanding
between the author and everyone whose buy-in the change needs. Underneath sits **PDCA**: Plan (background
through countermeasures), Do (implement), Check (did it hit the target?), Act (standardize the win or
adjust and cycle again). Because you fill in the Check and Act boxes with *real* results later, the A3 is a
living record of a learning loop, not a proposal frozen at kickoff — and the honesty of writing down what
actually happened, including misses, is where the learning comes from. Author it *with* the people
involved, not for them; the drafting conversation is most of the value.

## Common mistakes
- Writing it as a status report or a sell → it's a thinking tool. Show the reasoning, not just the ask.
- Spilling past one page → you've stopped prioritizing. The constraint forces clarity; respect it.
- Current-condition box with no data → opinion, not evidence. Bring facts and a small visual.
- Countermeasures that don't trace to a cause → a pet solution. Every one must answer a named cause.
- Filling every box at kickoff and never returning → skips Check/Act. Update with real results.
- A goal with no number or date → you can't check it. Make the target measurable and dated.
- Authoring it alone and presenting it → no consensus. Draft it *with* the affected people.

## Tailor to your environment
Record your real A3 practice in `references/your-environment.md` (use `your-environment.private.md`,
git-ignored, if it names real people, systems, or numbers). Capture your A3 template/tooling, your
audience and review ritual (who you walk the A3 with), your data sources for the current-condition box,
and how A3s get stored and revisited. Never commit real problem data that names clients or staff — keep
examples sanitized to structure.

## References
- references/a3-template.md — the one-page A3 box layout mapped to PDCA
- references/your-environment.md — your A3 template, audience, and data sources (add when supplied)
