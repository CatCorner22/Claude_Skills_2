---
name: deliberate-practice
description: >-
  Designs and runs practice sessions with one specific target at the edge of current
  ability: the assistant builds the drill — a debugging kata, a negotiation roleplay, a
  writing constraint exercise, a cross-examination rehearsal — plays the environment or
  opponent, gives immediate feedback that names the gap, and raises difficulty only on
  demonstrated competence, logging the target → attempt → feedback → next-target chain.
  Honestly distinguishes purposeful practice (self-designed) from deliberate practice
  (expert-designed training) per Ericsson, and corrects the 10,000-hour popularization.
  Use when the user wants to get better at a performable skill — debugging, writing,
  negotiating, arguing, presenting — rather than critique a finished piece of work.
  Triggers: deliberate practice, practice drill, kata, rehearse with me, get better at,
  practice session, play the opponent, stopped getting better.
metadata:
  version: "1.1.0"
---

# Deliberate practice (edge-of-ability drills)

Experience is not practice. Ericsson's research on expert performance found that what
separates experts is not accumulated hours on the job but structured training: one specific
target just beyond current ability, full attention, immediate feedback, and repetition with
refinement. Historically that required a coach and a training environment. This skill has
the assistant supply both: it designs the drill, plays the opponent or the broken system,
and closes the feedback loop in seconds instead of weeks.

## When to use
- Getting measurably better at a performable skill: debugging under pressure, tightening
  prose, holding a position in negotiation, surviving cross-examination, reading unfamiliar
  code fast, delivering a hostile-question briefing.
- Performance has plateaued despite plenty of experience — years in the seat, no longer
  improving.
- The user wants a rehearsal with an opponent or environment the assistant can simulate.
- Not for: critique of a finished work product (a brief, a deck, a codebase) → see
  `coding-agent-skills:sparring-partner` — that skill judges the artifact; this one trains
  the performer before the artifact exists.
- Not for: motivation or drive to execute a plan already chosen → see
  `coding-agent-skills:stay-hard-accountability` — this skill assumes the user shows up and
  supplies the *what to do in the session*, not the push to attend it.
- Retention of the knowledge drills surface (rules, patterns, procedures worth keeping cold)
  → see `learning-skills:spaced-retrieval-learning`. Boundary in one line: that skill trains
  knowing, this one trains doing.

## Do it
Drill patterns by skill type, the session template, difficulty-ladder design, and the
feedback formula are in `references/drill-design.md`.

1. **Name one specific target at the edge of ability.** Not "get better at negotiation" but
   "keep every concession conditional when the other side imposes time pressure." The
   assistant helps decompose the broad ambition into sub-skills and picks *one* — specific
   enough to observe in a single rep, hard enough that current performance is unreliable,
   not so hard that no rep can succeed.
2. **Take a baseline rep.** One unassisted attempt at a representative task, graded bluntly.
   This locates the actual edge (often not where the user thinks) and gives the log its
   starting point.
3. **Build the drill; the assistant plays the environment.** A scenario that isolates the
   target and forces it to happen several times per session: the assistant becomes the
   codebase with the planted bug, the counterparty who escalates, the cross-examining
   counsel, the editor imposing a constraint on the next paragraph. Patterns per skill type
   are in the reference.
4. **Run short reps with immediate, specific feedback.** After each rep — not at the end of
   the session — feedback that names the gap and its location ("the turn-3 concession came
   with nothing asked in return"), states what the stronger move was, and gives exactly one
   instruction for the next rep. Feedback names the behavior, never the person.
5. **Raise difficulty only on demonstrated competence.** Define the ladder up front: which
   dimension scales (time pressure, ambiguity, opposition quality, scaffolds removed) and
   what earns the next rung — typically two or three *consecutive* clean reps. Failure at a
   new rung means stepping back down, not pushing through; flailing reps train flailing.
6. **Log the chain: target → attempt → feedback → next target.** One line per rep is enough
   (template in the reference). The log is the curriculum — the next session starts where
   the chain left off, and recurring feedback themes become future targets.
7. **Label the practice honestly.** Per Ericsson, *deliberate practice* strictly means
   training designed by a qualified coach in a field with established training methods (music
   performance, chess, athletics). Most of what this skill builds is *purposeful practice*:
   self-designed, feedback-rich, edge-targeted — genuinely effective, but the assistant is an
   approximation of a coach, not one. Say so, and name where a real coach, a validated
   curriculum, or field-specific training would beat this setup.
8. **Hand the keepable knowledge over.** Rules, patterns, and procedures the drills surface
   go to `learning-skills:spaced-retrieval-learning` so they don't decay between sessions.

**Division of labor.** The assistant designs the drill, plays the environment, keeps the
feedback loop tight, and holds the ladder's gate; the user supplies real attempts at full
attention and honest self-report on what felt automatic versus effortful. Gate decisions
come from observed reps, not self-assessment — "that felt fine" is fluency talking, and
fluency is exactly the cue that misleads (see the sibling skill's treatment of it). What the
user never has to supply is the historically scarce part: a sparring opponent with infinite
patience and zero scheduling cost.

## Why / learn
**Why experience plateaus and structured practice doesn't.** Skills automate. Once
performance reaches "acceptable," execution moves to autopilot — which is efficient and
exactly why it stops improving: automatic execution generates no new learning signal. This
is why years of experience often stop predicting performance in a field. Practice works by
de-automating on purpose: isolate one component, push it past the comfortable version, and
force conscious control where autopilot used to run. The discomfort is not a side effect; it
is the mechanism engaging.

**Mental representations are the actual product.** Ericsson's account of expertise is not
"faster reflexes" but richer internal models — representations that let an expert see
structure where a novice sees noise, chunk situations, anticipate, and self-diagnose. Every
drill here is really an exercise in building a representation; every piece of feedback is a
correction to one. That is also why watching, reading about, or being adjacent to expert work
builds so little: representations form from one's own attempts being corrected.

**Feedback latency is the active ingredient.** A representation updates against the attempt
it just produced; the longer the gap between attempt and correction, the weaker the update
and the longer a wrong pattern gets to consolidate. Most professional skills have miserable
natural feedback loops — a negotiation tells you how it went weeks later, vaguely. The
assistant-as-environment collapses that loop to seconds, which is the single biggest thing
this skill buys.

**The 10,000-hour correction.** The "10,000-hour rule" is a popularization (Gladwell's
*Outliers*) of Ericsson's violinist research, and Ericsson himself disputed it: the figure
was an *average* accumulated by one group at one age, not a threshold, and the hours that
mattered were hours of structured, effortful, feedback-guided practice — not hours of
anything. There is no magic number; practice quality and structure are the variables. Naive
hours don't just fail to help — by deepening automaticity, they entrench the plateau.

## Common mistakes
- Practicing what already goes well → comfortable reps feel great and change nothing; the
  target lives where performance is currently unreliable.
- A vague target ("get better at writing") → undecomposable and unobservable; pick one
  sub-skill visible in a single rep.
- Marathon sessions → attention is the fuel; short reps at full focus beat hours of sloppy
  volume.
- End-of-session feedback summaries → too late for every rep before the last; correct after
  each rep.
- Feedback about the person ("weak negotiator") → names no gap and trains nothing; name the
  behavior, its location, and the stronger move.
- Advancing the ladder on schedule rather than competence → reps at a rung not yet earned
  train error patterns; two or three clean reps buy the next rung.
- Counting hours → count targeted reps that received feedback; hours measure exposure, not
  practice.
- Calling it deliberate practice when no expert designed it → label it purposeful practice
  and note where real coaching would beat this; honesty about the label keeps expectations
  calibrated.
- Using drills to evaluate a finished artifact → that's a critique job; see
  `coding-agent-skills:sparring-partner`.

## Tailor to your environment
Record your standing setup in `references/your-environment.md`: the skills you're training,
each one's current ladder rung, where the rep log lives, and any real-world materials drills
should mimic (your codebase's stack, your counterparties' styles, your court's format). Keep
committed content structural — real case details, counterparty names, or client material
belongs in `your-environment.private.md` (git-ignored), never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/deliberate-practice.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/drill-design.md — drill patterns by skill type (analysis, writing, argument,
  code), the session template, difficulty-ladder design, and feedback that names the gap
- references/your-environment.md — your training targets, ladder positions, and rep log
  location
