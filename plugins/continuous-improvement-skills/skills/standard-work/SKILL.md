---
name: standard-work
description: >-
  Documents the current best-known method for a repeatable task as standard work (an SOP) — capturing
  sequence, timing, and the key points and reasons — with takt/cycle context and visual management, so
  the process is stable enough to improve. Use when documenting, standardizing, or stabilizing a
  process, or writing an SOP or work instruction. Triggers: standard work, standardized work, SOP,
  standard operating procedure, work instruction, standardize, visual management.
---

# Standard work

## When to use
- Documenting the current best-known way to do a repeatable task (a close task, a reconciliation, a
  payment run) so everyone does it the same, correct way.
- Stabilizing a process that varies by who does it, before you try to improve it.
- Writing an SOP or work instruction that people will actually use.
- Not for: sequencing a whole multi-task close on a calendar → see
  `accounting-skills:month-end-close`. To propose and align on a specific improvement → see
  `continuous-improvement-skills:a3-thinking`.

## Do it
1. **Pick one repeatable task and its trigger.** Name where it starts, where it ends, and what event
   kicks it off. Standard work is for repeatable, cyclical work — not one-offs.
2. **Observe the current best method at the gemba.** Watch it done (ideally by the most reliable
   performer), and document *what actually works today*, not an idealized or aspirational version.
3. **Record the three elements of standard work.** (a) **Sequence** — the steps in order; (b)
   **timing** — cycle time per step and, where demand-paced, the **takt** (available time ÷ demand) it
   must fit; (c) **standard inputs/WIP** — what must be on hand to start. This is the classic Toyota
   trio: takt, sequence, and standard in-process stock.
4. **Capture key points and the reason for each.** For every step note the **key point** (the quality,
   safety, or ease detail that makes it come out right) *and why* it matters. The "why" is what makes a
   standard teachable and keeps people from silently dropping steps they don't understand — see
   `references/sop-template.md`.
5. **Make it visual.** Add a one-page work instruction with screenshots/photos, a checklist, and visual
   controls (color-coding, a done/not-done board, exception flags) so the right way is the obvious way
   and deviations are visible at a glance.
6. **Train to the standard and confirm it takes.** Teach it, watch the person do it, and verify they
   can perform it *and* explain the key points. A standard nobody was trained to is a document, not a
   practice.
7. **Make deviations visible and set a review cadence.** Define how an exception or a better idea gets
   surfaced (not hidden), and put a date/owner on reviewing and updating the standard. It is a **living
   document**: every improvement (kaizen) updates it; a stale binder is worse than none.

## Why / learn
You cannot improve a process that isn't stable — that is the whole reason standard work comes first. If
five people do a reconciliation five different ways, a change to it improves nothing measurable, because
there is no baseline: the variation *is* the noise that hides whether anything got better. A standard
fixes the method so that outcomes become repeatable, and once outcomes are repeatable, the effect of a
change is legible. So the standard is the baseline every kaizen measures against — improvement is the
gap between the current standard and a better one, and the moment you find a better way, the standard
*becomes* it. That reframes what an SOP is for. It is not a compliance binder written once and shelved;
it is the current best-known method, held only until someone finds better, which is why capturing the
**reason** behind each key point matters more than the step list — reasons let people adapt correctly and
spot when a step no longer serves its purpose, whereas a reasonless step gets dropped or cargo-culted.
Visual management and takt/cycle context make the standard *self-policing*: when the correct state is
visible, a deviation announces itself, and problems surface while they're small. The paradox worth
keeping: standardization isn't the enemy of improvement — it's its prerequisite, and its scoreboard.

## Common mistakes
- Writing the aspirational method instead of what actually works → nobody follows it. Document reality first.
- Listing steps with no "why" → people drop steps they don't understand. Capture the reason per key point.
- Treating the SOP as write-once → it goes stale and misleads. Set a review cadence; update on every kaizen.
- No visual management → the right way isn't obvious and deviations hide. Make state visible.
- Skipping training verification → a filed document isn't a practiced standard. Watch them do it.
- Standardizing a genuinely one-off task → standard work is for repeatable, cyclical work only.
- Locking it so tightly no one can suggest better → kills improvement. Build in a path to surface ideas.

## Tailor to your environment
Record your real standards setup in `references/your-environment.md` (use `your-environment.private.md`,
git-ignored, if it names real systems, accounts, or people). Capture your SOP template and where
standards live, your naming/version conventions, how takt or volume applies to your work, your visual-
management tools, and your training and review cadence. Never commit real account, client, or credential
data — keep examples sanitized to structure.

## References
- references/sop-template.md — a fillable standard-work / SOP template (sequence, timing, key points, reasons)
- references/your-environment.md — your SOP conventions, storage, and cadence (add when supplied)
