---
name: standard-work
description: >-
  Documents the current best-known method for a repeatable task as standard work (an SOP), so
  the process is stable enough to improve — the Toyota trio of takt time, work sequence, and
  standard in-process stock, plus the TWI Job Instruction breakdown of steps, key points, and
  the reason behind each; adds visual management so deviations announce themselves, verified
  training, and a review cadence that keeps the standard a living baseline every kaizen updates.
  Fits any recurring task — a weekly report, an intake review, a handoff, a release. Use when
  documenting, standardizing, or stabilizing a process that varies by who does it, capturing
  tribal knowledge, or writing an SOP or work instruction people will follow. Triggers: standard
  work, standardized work, SOP, standard operating procedure, work instruction, standardize a process,
  visual management, TWI, job instruction, job breakdown, takt time, everyone does it
  differently, tribal knowledge.
metadata:
  version: "1.2.0"
---

# Standard work

Standard work is the current best-known way to do a repeatable task, written down so anyone
trained to it gets the same result. The lineage runs through Toyota's standardized work
(takt, sequence, standard in-process stock) and the WWII-era Training Within Industry (TWI)
programs whose Job Instruction breakdown — steps and key points, with the reasons column
added as the format matured — is still the most teachable SOP format there is.

## When to use
- Documenting the current best-known way to do a repeatable task (a weekly report, an
  intake review, a shift handoff, a deployment) so everyone does it the same, correct way.
- Stabilizing a process that varies by who does it, before you try to improve it.
- Capturing what a departing or overloaded expert carries in their head — tribal knowledge —
  as a method others can be trained to.
- Writing an SOP or work instruction that people will actually use.
- Not for: sequencing a whole multi-task close on a calendar → that's a month-end-close calendar
  build — an accounting-domain procedure this library does not carry. To propose
  and align on a specific improvement → see `continuous-improvement-skills:a3-thinking`.
- Not for: finding which task gates a whole multi-step effort → see
  `continuous-improvement-skills:theory-of-constraints`. To see where one task sits in the
  end-to-end stream and whether it's worth standardizing first → see
  `continuous-improvement-skills:value-stream-mapping`.
- Not for: boiling an existing SOP down to the few steps people actually skip → see
  `safety-and-reliability-skills:checklist-design` (a checklist rides on top of standard
  work; it doesn't replace it).
- Not for: standardizing *data* instead of work — this skill standardizes how a task is
  performed, not the values in a table. Normalizing messy category values, formats, and types
  in a dataset → see `data-analytics-bi-skills:data-cleaning`; z-score standardizing or
  scaling model features → see `machine-learning-skills:feature-engineering`.
- Not for: deciding which *document* should exist, what type it is, and where it lives — tutorial
  vs how-to vs reference vs explanation, ADRs, and the owner/cadence/last-verified mechanism that
  keeps it true → see `writing-skills:technical-documentation`. This skill owns the one right way
  to do a task; that one owns the documentation set around it.

## Do it
`references/sop-template.md` has the fillable template, a worked example, and the TWI
breakdown format.
1. **Pick one repeatable task and its trigger.** Name where it starts, where it ends, and
   what event kicks it off. Standard work is for repeatable, cyclical work — not one-offs.
2. **Observe the current best method at the gemba.** Watch it done (ideally by the most
   reliable performer), and document *what actually works today*, not an idealized or
   aspirational version.
3. **Record the three elements of standard work.** (a) **Sequence** — the steps in order;
   (b) **timing** — cycle time per step and, where demand-paced, the **takt** (available
   time ÷ demand) it must fit; (c) **standard inputs/WIP** — what must be on hand to start.
   This is the classic Toyota trio: takt, sequence, and standard in-process stock.
4. **Capture key points and the reason for each.** For every step note the **key point**
   (the quality, safety, or ease detail that makes it come out right) *and why* it matters —
   the TWI Job Instruction breakdown. The "why" is what makes a standard teachable and keeps
   people from silently dropping steps they don't understand.
5. **Make it visual.** Add a one-page work instruction with screenshots/photos and visual
   controls (color-coding, a done/not-done board, exception flags) so the right way is the
   obvious way and deviations are visible at a glance. If the failure mode is *skipping*
   known steps under pressure rather than not knowing them, design a proper checklist for
   the killer items (`safety-and-reliability-skills:checklist-design`).
6. **Train to the standard and confirm it takes.** Use the Job Instruction pattern: prepare
   the learner, present the task (steps → key points → reasons), have them try it while
   explaining it back, then follow up. Verify they can perform it *and* explain the key
   points. For building the underlying skill a step demands (not just the sequence), drill
   it deliberately (`learning-skills:deliberate-practice`). A standard nobody was trained to
   is a document, not a practice.
7. **Make deviations visible and set a review cadence.** Define how an exception or a better
   idea gets surfaced (not hidden), and put a date/owner on reviewing and updating the
   standard. It is a **living document**: every improvement updates it — a kaizen event's
   first deliverable is the revised standard (`continuous-improvement-skills:kaizen-and-codesign`) —
   and a stale binder is worse than none.

## Why / learn
You cannot improve a process that isn't stable — that is the whole reason standard work comes
first. If five people do a task five different ways, a change to it improves nothing
measurable, because there is no baseline: the variation *is* the noise that hides whether
anything got better. A standard fixes the method so that outcomes become repeatable, and once
outcomes are repeatable, the effect of a change is legible. So the standard is the baseline
every improvement measures against — and the moment you find a better way, the standard
*becomes* it. The maxim "without a standard there can be no improvement" is widely attributed
to Taiichi Ohno; the primary source is hard to pin down, so treat it as the movement's
proverb rather than a verified quotation — the logic stands on its own.

That reframes what an SOP is for. It is not a compliance binder written once and shelved; it
is the current best-known method, held only until someone finds better. This is why capturing
the **reason** behind each key point matters more than the step list — reasons let people
adapt correctly and spot when a step no longer serves its purpose, whereas a reasonless step
gets dropped or cargo-culted. That insight is TWI's: Job Instruction's breakdown sheets
(the reasons column a later addition to the original two) came out of wartime US industry
training, were carried to Japan during the postwar rebuilding, and were absorbed into
Toyota's training practice — the SOP format outlived the war by earning it. A terminology note worth knowing:
in Toyota usage, "standardized work" means specifically the takt/sequence/standard-WIP trio
for cyclical work; office SOPs borrow the spirit and the breakdown format even where takt is
approximated by volume. Visual management makes the standard *self-policing*: when the
correct state is visible, a deviation announces itself, and problems surface while they're
small. The paradox worth keeping: standardization isn't the enemy of improvement — it's its
prerequisite, and its scoreboard.

## Common mistakes
- Writing the aspirational method instead of what actually works → nobody follows it. Document reality first.
- Listing steps with no "why" → people drop steps they don't understand. Capture the reason per key point.
- Treating the SOP as write-once → it goes stale and misleads. Set a review cadence; update on every kaizen.
- No visual management → the right way isn't obvious and deviations hide. Make state visible.
- Skipping training verification → a filed document isn't a practiced standard. Watch them do it.
- Standardizing a genuinely one-off task → standard work is for repeatable, cyclical work only.
- Locking it so tightly no one can suggest better → kills improvement. Build in a path to surface ideas.
- Writing a 30-page SOP when the failure is skipped steps → that's a checklist-design problem
  riding on a one-page standard, not more prose.
- Confusing the standard with the person → the method is documented so it survives turnover;
  if only one person can execute it, the capture isn't done.

## Tailor to your environment
Wire in your current role here — standard work is domain-neutral by design and attaches to
whatever repeatable tasks your job holds now and next. In `references/your-environment.md`,
record your SOP template and where standards live, your naming/version conventions, how takt
or volume applies to your work, your visual-management tools, and your training and review
cadence. Keep the committed file structural; real system names, accounts, credentials, or
people go in `your-environment.private.md`, which is git-ignored and never committed.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/standard-work.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/sop-template.md — the fillable standard-work/SOP template (sequence, timing,
  key points, reasons), the TWI Job Instruction breakdown and 4-step training method, a
  worked domain-neutral example, visual management options, and canon notes
- references/your-environment.md — your SOP conventions, storage, and cadence (add when supplied)
