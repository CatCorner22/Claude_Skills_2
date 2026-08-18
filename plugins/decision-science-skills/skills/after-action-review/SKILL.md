---
name: after-action-review
description: >-
  Facilitates the Army's four-question after-action review (AAR): a blameless, rank-free
  team debrief asking what was SUPPOSED to happen, what ACTUALLY happened (ground truth
  before interpretation), WHY the difference, and what to SUSTAIN and IMPROVE — roughly a
  quarter of the time on each of the first two questions and half on causes and fixes.
  The LLM reconstructs the what-actually-happened timeline from logs, emails, and
  tickets, keeps discussion on the four rails, and converts sustain/improve items into
  standard-work updates; it facilitates and never adjudicates blame. Use after a project
  milestone, a period-end close, an incident or process break, or a system go-live.
  Owns team and event debriefs — an assistant's own self-retrospective belongs to
  reflective-learner instead. Triggers: after-action review, AAR, hot wash, team debrief,
  sustain and improve, what should we do differently next close.
---

# After-action review (AAR)

## When to use
- A team event just ended and you want the learning before it evaporates: a project
  milestone (post-milestone review in
  `continuous-improvement-skills:project-command-center`), a month-end close, a
  reconciliation incident or break, a system-configuration go-live, a payment-fraud
  near-miss.
- Immediately after the event as a short "hot wash," or scheduled within days while the
  artifacts (logs, emails, tickets) are still warm.
- When sustain/improve findings should flow somewhere durable: the next iteration's plan,
  `continuous-improvement-skills:standard-work` updates, and the repo's MEMORY.md
  crystallization pass.
- Recurring events pay the most — an AAR after every close makes each close's output the
  next close's plan, which is the loop the format was built for.
- The boundary is crisp: this skill owns TEAM and EVENT debriefs.
  `metacognition-skills:reflective-learner` owns SELF-retrospectives — the assistant
  processing its own corrections. A person or team looking at their event → here; the
  assistant looking at itself → there.
- Not for: self-reflection on the assistant's own mistakes → see
  `metacognition-skills:reflective-learner`. Deep causal drill-down on ONE defect → see
  `continuous-improvement-skills:root-cause-analysis` — an AAR often SPAWNS an RCA when
  question 3 hits a stubborn defect; say so and hand off. Imagining failure BEFORE the
  plan runs → see `decision-science-skills:pre-mortem`.

## Do it
The four questions expanded, the ground rules to read aloud, the facilitation guide, and the
timeline-reconstruction protocol are in `references/aar-method.md`.

1. **Frame the session.** State the event under review, the ground rules (blameless,
   rank-free, everyone talks, no grades), and the four questions on the wall. Budget the
   time roughly 25% / 25% / 50% across supposed-to / actually-happened / why-plus-fixes.
2. **Question 1 — what was SUPPOSED to happen?** Restate the plan, the standard, or the
   close checklist as it existed before the event. Pull the actual documents; memory of
   the plan is already contaminated by the outcome.
3. **Question 2 — what ACTUALLY happened?** Establish ground truth before any
   interpretation. This is the LLM's heavy lift: reconstruct the timeline from logs,
   emails, tickets, job histories, and bank statements — timestamped, sourced, in order.
   Facts only; the words "because" and "should have" are out of bounds until the timeline
   stands. Disagreements about facts get resolved by artifacts, not seniority.
4. **Question 3 — WHY the difference?** Compare plan to timeline gap by gap. Ask why
   each divergence occurred — process, information, timing, tools, assumptions. Keep it
   causal and systemic, not personal; if one defect demands real depth, spawn an RCA
   rather than stretching the AAR.
5. **Question 4 — what do we SUSTAIN and what do we IMPROVE?** Sustain: what worked and
   must be kept deliberately (it worked for a reason — name it). Improve: specific
   changes with owner and date. Convert each improve item into its durable home — a
   standard-work / SOP edit, a checklist line, the next plan — and each sustain item into
   the standard so it survives staff turnover. Prefer three owned items to ten orphaned
   ones; "communicate better" is not an item, "bank-rec status posted to the close
   channel by 10:00 daily, owner named" is.
6. **Keep everyone on the rails.** The LLM facilitates: tracks which question is live,
   parks blame and solutioning that arrive early, ensures quieter voices are asked, and
   drafts the output record — but it never adjudicates whose fault something was. The
   blameless norm is human culture; the facilitator protects it, no one enforces blame.
7. **Close the loop.** Publish the one-page record (four answers, owners, dates), file it
   with the project, and feed durable lessons to the MEMORY.md crystallization pass. At
   the next event of the same kind, open by reading the last AAR's improve items — an
   unread record is the format's most common death.

## Why / learn
The AAR comes from the U.S. Army's *A Leader's Guide to After-Action Reviews* (TC 25-20),
built on a blunt observation: units that talked honestly about what just happened got
better faster than units that graded each other. The four questions are a machine for
making honesty cheap. Separating "supposed to" from "actually happened" defuses the
argument before it starts — most debrief fights are two people interpreting different
facts, so the AAR refuses interpretation until the facts are established. Rank-free and
blameless are not niceness; they are data-quality controls: the private who saw the
problem speaks only if speaking is safe, and a debrief that assigns blame teaches
everyone to hide next time. The 25/25/50 split forces the payoff — most groups spend the
whole hour relitigating what happened and never reach what to change. Sustain matters as
much as improve: what worked was usually someone's unrecorded judgment, and unless it
enters the standard it leaves with them. Shell, BP, and GE adopted the practice for
knowledge management [snippet-only: practitioner provenance — corporate adoption reports,
no controlled trials; be candid about that when asked for evidence].

## Common mistakes
- Interpreting before the facts are set → arguments about blame disguised as analysis.
  Timeline first; artifacts settle factual disputes.
- Letting rank talk first or grade the event → juniors go silent and the data dies.
  Facilitator asks the quietest, most junior observers early.
- Skipping question 1 → without the plan-as-written there is no "difference" to explain.
- Spending the hour on what happened → enforce the 25/25/50 split; the value is in Q3/Q4.
- Improve items with no owner or home → they evaporate. Every item lands in a standard,
  a checklist, or the next plan, with a name and date.
- Recording only failures → sustain items are half the output; unrecorded success is
  luck next time.
- Using an AAR to fix one deep defect → wrong tool; spawn
  `continuous-improvement-skills:root-cause-analysis` from question 3.
- Running the assistant's self-critique as an "AAR" → that seam belongs to
  `metacognition-skills:reflective-learner`.

## Tailor to your environment
Record in `references/your-environment.md`: the events that always get an AAR (each
close, each go-live, each incident), your timeline sources (job logs, ticket queues,
email lists, bank portals), who facilitates, where records are filed, and which standards
receive the sustain/improve output. If entries would name real people or incidents, put
them in `your-environment.private.md` (git-ignored). Never commit real client or bank
data — sanitize to structure.

## References
- references/aar-method.md — the four questions expanded, facilitation guide,
  timeline-reconstruction protocol, ground rules, and the corporate-adoption evidence
  with its provenance stated honestly
- references/your-environment.md — your standing AAR events, sources, and filing (fill in)
