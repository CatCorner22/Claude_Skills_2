---
name: checklist-design
description: >-
  Designs checklists that actually get used — selecting only killer items (steps that cause serious
  harm if missed AND are skipped in practice), choosing read-do vs. do-confirm format, anchoring the
  card to a natural pause point, holding it to 5–9 imperative items on one page, and field-testing it
  in the real workflow — and diagnoses why an existing checklist is ignored or produced no
  improvement. Use when designing a wire-release, sterilization, patient-handoff, or close-task
  checklist, cutting a bloated one down, or fixing one that people skip; running an existing
  checklist stays with the skill that owns that process. Triggers: design a checklist, read-do,
  do-confirm, killer items, pause point, our checklist isn't working, people skip the checklist,
  checklist too long, redesign the checklist.
metadata:
  version: "1.1.1"
---

# Checklist design

## When to use
- Designing a new checklist for a high-stakes step that people demonstrably skip — releasing a wire,
  sterilizing instruments, handing off a patient, locking a close task.
- Redesigning an existing checklist that has grown too long, serves auditors instead of the crew, or
  gets skipped under pressure.
- Diagnosing why a mandated checklist produced no measurable improvement.
- **Not for:** *running* an existing checklist — that belongs to whoever owns the process
  (e.g. a month-end close checklist is run by the close process's owner, not redesigned here;
  the close procedure itself is accounting-domain work this library does not carry). Not for documenting a full
  method with sequence, timing, and key points → see `continuous-improvement-skills:standard-work`.
- A bare mention of "checklist" is not a trigger: this skill is for *designing or diagnosing* one.

## Do it
1. **Select killer items only.** Walk the SOP or process and keep a step only if it passes both
   tests: (a) missing it causes serious harm, and (b) it is actually skipped in practice. Omit what
   people never forget — an item nobody misses dilutes attention from the ones that kill. Working
   from a long SOP, have the model propose the cut: give it the full procedure and require the killer
   shortlist *with a written rationale per cut*, then challenge every rationale yourself. Heuristics
   in `references/checklist-design-method.md`.
2. **Choose the format: read-do or do-confirm.** *Read-do*: read each item aloud, do it, in order —
   for infrequent, interruptible, or novel work where sequence matters. *Do-confirm*: the team works
   from memory and flow, then stops at the pause point and verifies the killer items — for skilled
   crews doing routine flow-critical work (a wire release is a do-confirm card). Decision table in
   the reference.
3. **Fix a natural pause point.** Anchor the checklist to a moment where the team *already* stops —
   before incision, before pressing "release payments", before the patient leaves the operatory. A
   checklist with no natural pause point never runs; one bolted mid-flow gets skipped first.
4. **Draft to the discipline: 5–9 items per pause point, one page, imperative wording.** The count
   is per card, not per process — the 19-item WHO checklist is three cards at three pause points, so
   a list that won't fit in 9 usually wants a second pause point, not a longer card. One verifiable
   action per line ("Confirm beneficiary against the vendor master", not "Beneficiary considerations"). Precise
   nouns, no paragraphs; the response to each line is a check or a challenge, not an essay.
5. **Field-test in the real workflow and revise.** Run it live with the crew that will use it. Time
   it, watch for skipped lines, wrong-order items, ambiguous wording, a pause point the team blows
   through. Revise and re-test until it runs clean. A checklist is a device you iterate, not a
   document you publish. Protocol in the reference.
6. **Hand the ritual to the team — the human gate.** The model (or you) drafts; the *team* enacts.
   Name who calls the checklist, rehearse it, and review skip data on a cadence. A mandated card
   without an enacted team ritual is the Ontario null result (see Why / learn).

## Why / learn
A checklist is not a summary of the process — it is a net under the fatal steps. The discipline was
born when Boeing's Model 299 (the B-17 prototype) crashed on its 1935 demonstration flight because
the gust locks were left engaged: the verdict was "too much airplane for one man to fly", and the
pilots' answer was not more training but a short pre-flight card. Degani & Wiener's human-factors
work for NASA and Boorman's design practice at Boeing formalized what makes such cards work, and
Gawande's *The Checklist Manifesto* carried it into medicine and beyond.

The evidence teaches both halves of the lesson. The WHO surgical checklist study (Haynes, NEJM 2009;
eight cities, ~7,700 patients) saw deaths fall from 1.5% to 0.8% and complications from 11.0% to
7.0% — a two-minute card outperforming most drugs. But when Ontario *mandated* surgical checklists
across 101 hospitals (Urbach, NEJM 2014), outcomes did not significantly change. Same artifact, null
result. The difference is the enacted ritual: teams that pause together, speak the items aloud, and
are licensed to challenge, versus a form filed for compliance. The checklist is the visible tip of a
team behavior — design the behavior, not just the card. Full evidence with provenance in
`references/checklist-design-method.md`.

Why this skill pairs well with a model: killer-item selection historically demanded Boorman-level
knowledge of how the process fails — which steps have killed, which get skipped under load. A model
can take a 40-step SOP and return the 7 killer items with a rationale per cut in minutes, and flag
where evidence for a cut is thin. That moves the scarce human work to where it belongs: challenging
the cut, field-testing the card at the real pause point, and owning the ritual. The model drafts;
the team enacts — a checklist nobody rehearses is Ontario.

## Common mistakes
- Too long → nobody runs it. Cut to killer items; the rest lives in the SOP and training.
- No pause point → skipped under pressure. Anchor to a stop the team already makes.
- Never trialed → ambiguous lines, wrong order, wrong length. Field-test and revise before rollout.
- Designed for auditors, not the crew → box-ticking theater. Write for the people at the pause point.
- Mandated without the ritual → the Ontario null result. Name a caller, rehearse, watch skip data.
- Read-do handed to expert crews (insulting, ignored) or do-confirm to novices (they need the
  sequence) → match format to who runs it, step 2.
- Including items nobody ever misses → attention tax on the killer items. Omit them.
- Treating the card as finished → processes drift. Re-run the field test when the process changes.

## Tailor to your environment
Record your redesign targets and live checklists in `references/your-environment.md`; anything
naming real people, accounts, or incidents goes in `your-environment.private.md` (git-ignored).
Known mounts, by format:
- **Do-confirm** — a payment or wire release at the "before send" pause point; a period-end close
  (which close tasks are killer items, at which pause points? bring your own close calendar — the
  checklist craft is here, the close procedure is not).
- **Read-do** — rotating-staff, sequence-critical work: instrument sterilization, patient handoff,
  a system cutover.

Capture your pause points, callers, and skip-data source.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/checklist-design.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/checklist-design-method.md — killer-item selection heuristics, read-do vs. do-confirm
  decision table, pause-point identification, drafting rules, field-test protocol, failure catalog,
  and the B-17 / WHO / Ontario evidence base with provenance
- references/your-environment.md — your checklists, pause points, callers, and redesign targets
