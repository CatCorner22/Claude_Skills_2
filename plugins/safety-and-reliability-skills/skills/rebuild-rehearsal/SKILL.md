---
name: rebuild-rehearsal
description: >-
  Keeps critical capabilities alive by rehearsing the rebuild on a cadence shorter than
  anyone's tenure, channeling the Ise Grand Shrine's Shikinen Sengu (rebuilt in full every
  20 years since 690 CE; carpenters learn, lead, then teach; a ~120-year lapse after the
  Ōnin War proved the cycle needs a funding owner): census what lives only in heads,
  pick a real rebuild unit (restore from backup, recreate the deliverable from raw inputs,
  rebuild the environment from docs alone), rotate learn-lead-teach so last time's
  apprentice leads, harvest every exposed gap into the docs, and name who funds the cycle.
  The assistant simulates the rebuild, interrogates the docs for gaps, and plays the
  newcomer with only the written record. Use when knowledge lives in one head or docs have
  never been proven by use. Triggers: rebuild drill, restore drill, if she left tomorrow,
  are the docs enough to recreate this, it only lives in his head, bus factor, knowledge
  refresh, could a newcomer run this, disaster recovery rehearsal.
metadata:
  version: "1.5.1"
---

# Rebuild rehearsal (the Shikinen Sengu pattern)

The Ise Grand Shrine in Japan is dismantled and rebuilt, in full, every 20 years — the
Shikinen Sengu, practiced since 690 CE [snippet-only]. The buildings are not the point;
the *builders* are. A miyadaiku carpenter takes part two or three times in a working
life: apprentice on the first cycle, lead on the second, teacher on the third — so the
craft never has to survive a gap longer than one generation of hands. The operation even
grows its own inputs: a 200-year in-house forestry plan (begun 1923) raises the hinoki
its future rebuilds will need [snippet-only].

And the cycle *broke*. After the Ōnin War, the Inner Shrine went roughly 120 years
without rebuilding (1462–1585); the practice was revived only when the fundraising nuns
of Keikō-in raised money across the country for decades, with warlord endowment behind
them — Oda Nobunaga began funding the shrine again in 1569 and died in 1582, so the 1585
rebuild was carried through by his successors [snippet-only]. That lapse is not a
blemish on the story — it is half the lesson: a renewal cycle without a funding owner
silently lapses, no matter how sacred everyone agrees it is. (The shinise
footnote makes the same point from commerce: Kongō Gumi, temple builders founded 578,
operated independently until liquidation in 2006, longevity built on single-craft focus
and flexible succession [snippet-only].)

The mechanism this skill installs: **knowledge survives only if it is exercised on a
schedule shorter than a career** — rebuild the real thing while the last builders are
alive to correct the next ones. The artifact is disposable; the capability is the asset.

## When to use
- A capability your team depends on lives in one or two heads: only Maria can produce
  the monthly deliverable, only Dev knows how the environment is stood up, only the
  senior attorney has run this filing end to end.
- Runbooks, wikis, or backup procedures exist but have never been proven by actually
  using them — "we have docs" is a claim, not a test.
- Someone is likely to leave, retire, or rotate within a year, and you want their
  capability to survive them — or a newcomer just arrived and nobody can say whether
  the written record would be enough for them.
- A restore-from-backup, environment-from-scratch, or process-from-runbook question has
  no recent answer: "when did we last actually do this without the expert?"
- Not for: deciding what automated tests a codebase needs → see
  `full-stack-dev-skills:testing-strategy`; this skill exercises *people and docs*, not
  test suites.
- Not for: drilling the unsealing of a crisis response → see
  `safety-and-reliability-skills:break-glass-playbooks`. The seam: a crisis drill
  rehearses the *emergency* (find the sealed moves, exercise the authority, fast); this
  skill rehearses the *capability* (could we still build the thing at all, slow and
  thorough). A team can pass one and fail the other.
- Not for: one person retaining studied material → see
  the archived `learning-skills:spaced-retrieval-learning`; successive relearning is this skill's
  personal-scale twin — same mechanism (exercise before the memory dies), different
  unit (a fact in a head vs. a capability in a team).
- Not for: writing or fixing the documentation itself → see
  `writing-skills:explanation-design`; this skill *finds* the gaps by rehearsal and
  hands them to the writer.

## Do it
The census template, rebuild-unit patterns, scheduling rules, rotation mechanics,
gap-harvest protocol, and a worked example are in `references/rebuild-method.md`.

1. **Run the bus-factor census.** For each capability the operation depends on, record
   four facts: who can do it today, who could learn it, what written record exists, and
   when it was last done by someone other than the primary. The assistant drafts the
   census by interviewing you ("what would stop shipping if X were unreachable for a
   month?") and flags every row where the answer to the first question is one name.
2. **Pick the rebuild unit per capability** — the smallest exercise that produces the
   real thing from the surviving record, not a walkthrough of it. Patterns: restore the
   actual backup to a scratch location; recreate the monthly deliverable from raw inputs
   with only the runbook; stand up the environment from the docs alone; run the process
   end to end with a newcomer driving. If the unit can't fail, it isn't a rebuild.
3. **Schedule rehearsals on a cadence shorter than tenure.** Ise's rule — 20 years,
   because a career spans two or three cycles — scales down: set each capability's
   cadence so that everyone who should hold it gets at least two rehearsals before they
   could plausibly leave. In practice: quarterly for capabilities that would halt the
   operation, annually for the rest. Cadence longer than tenure means someone will
   depart having never taught.
4. **Rotate learn → lead → teach.** Each rehearsal, last time's apprentice leads and a
   genuine newcomer apprentices; the veteran attends only to correct, not to drive.
   Three rehearsals turn a newcomer into a teacher — that rotation, not the docs, is
   what actually moves the capability between generations.
5. **Run it for real, newcomer driving.** The person with the least knowledge executes
   from the written record alone; the veteran stays silent until something goes wrong,
   then corrects out loud — **except at a step whose effect leaves the building**, where the
   corrector speaks *before* it runs. Classify the runbook first: money moved, a filing
   submitted, a client or counterparty contacted, a credential rotated, a record the retention
   schedule locks — those are declared and simulated, never executed, and a past period or a
   sandbox instance is preferred to the live one. State an abort trigger before starting: hand
   back to the veteran the moment a real client, deadline or counterparty is affected, or the
   driver cannot tell whether the next step is reversible. Handing back is a rehearsal that
   found its limit, not a failed one. (The screen is in `references/rebuild-method.md`; every
   other rebuild pattern here is safe by construction, this one is not.)
   Every question the driver has to ask a human is a gap in
   the docs — log each one verbatim as it happens.
6. **Harvest every gap into the record.** The rehearsal is the documentation's test:
   each logged question, missing step, stale credential, or dead link becomes a doc fix
   before the rehearsal is closed. A rehearsal whose gaps stay in a notebook bought
   nothing durable.
7. **Name the funding owner of the cycle itself.** The Ōnin lesson: someone — a named
   role, with time or budget authority — owns keeping the rehearsals scheduled and
   resourced. Renewal is the first thing cut when quarters get busy, and it fails
   silently: nothing breaks on the day you skip it. If no one can say who funds the
   next rehearsal, the cycle has already lapsed; it just hasn't been noticed yet.
8. **Use the assistant to make rehearsal affordable.** Historically, rehearsing a
   rebuild cost nearly as much as the rebuild — the barrier Ise paid thirteen centuries
   of treasure to clear. The assistant collapses that cost: it simulates the rebuild
   step by step from the docs before anyone books a room, interrogates the record
   ("step 4 assumes an access nobody named — who grants it?"), and plays the apprentice
   who has *only* the written record, asking every question a cold newcomer would.
   Division of labor: the assistant finds doc gaps cheaply and often; the humans still
   run the real rehearsal on schedule, because only reality tests the backup, the
   access, and the hands.

   **Exercise control applies whenever a drill touches real people, real systems, or a real
   third party.** Mark every artifact `EXERCISE EXERCISE EXERCISE — NO REAL ACTION`; name one
   person who can call ENDEX, with an abort phrase (**"REAL WORLD, REAL WORLD"**) anyone may
   use; write a no-play list of systems, accounts, and people the drill may not touch; declare
   and adjudicate any action with an irreversible external effect instead of executing it; and
   pre-notify any third party whose name or number appears in the scenario. The full section is
   in `decision-science-skills:tabletop-wargaming`'s `references/exercise-design.md` — one
   discipline, shared by every exercise in this library.

## Why / learn
Capability decays by a mechanism, not by bad luck. Skills that aren't exercised fade;
docs that aren't executed rot silently as systems drift around them; and the people who
could correct both eventually leave. Ise's insight is that all three decay curves are
beaten by one move: rebuild the real thing on a fixed schedule, timed so the people who
did it last are still present to correct the people doing it next. Why exactly 20 years is
not settled — thatch and timber durability and ritual renewal are all offered — but the
property that makes it work as a pattern is generational overlap: 20 years is short enough
that a working life spans two or three cycles. That is the property to scale, not the
number: if analysts stay three years, a three-year cadence guarantees nothing.

The inversion worth internalizing: **the artifact is disposable; the capability is the
asset.** Ise does not preserve thousand-year-old buildings — it preserves the ability to
produce them, which is why the buildings are always new and the craft is always old. In
an operation, that means the monthly deliverable, the environment, even the backup file
matter less than the demonstrated ability to produce them again from what would survive
a departure. Protecting the artifact while the capability decays is embalming.

The rehearsal doubles as the only honest test of documentation. Docs are written by
people who already know the material, so they systematically omit what the author cannot
see they know — the curse of knowledge. No amount of review by knowledgeable colleagues
finds those holes; only execution by someone without the knowledge does. That is why the
newcomer drives and the veteran only corrects: the configuration maximizes gap discovery
while the correction is still available.

Finally, the honest half of the Ise story: the cycle ran on treasure, and when war
destroyed the funding, the cycle stopped for four generations — revived not by
reverence but by nuns who fundraised for decades and warlords who paid, across more than
one lifetime [snippet-only]. Renewal work never defends itself in a budget fight,
because skipping it costs nothing today. It survives only as someone's named, funded
responsibility. Budget the renewal or it silently lapses.

## Common mistakes
- Treating written docs as proof of survivability → docs are a claim; only a rebuild
  by someone who doesn't already know the material tests them.
- Letting the veteran drive the rehearsal → the expert's hands hide every gap; the
  newcomer drives, the veteran corrects.
- Walkthroughs instead of rebuilds → talking through the restore finds nothing; the
  unit must produce the real artifact and be able to fail.
- Cadence set by convenience rather than tenure → if people leave faster than they get
  two rehearsals, the rotation never completes and the capability walks out the door.
- Simulating forever → the assistant's dry-run finds doc gaps cheaply, but only the
  real rehearsal tests the backup media, the access grants, and the hands; alternate,
  don't substitute.
- Gaps noticed but never harvested → close each rehearsal only when every logged
  question has become a doc fix, or the next rehearsal rediscovers the same holes.
- No funding owner → the Ōnin failure mode: the cycle lapses silently the first busy
  quarter, and nobody notices until the departure it existed to survive.
- Rehearsing the emergency instead of the capability → crisis-response mechanics belong
  to `safety-and-reliability-skills:break-glass-playbooks`; passing a fire drill says
  nothing about whether you could rebuild the building.

## Tailor to your environment
Record your standing cycle in `references/your-environment.md`: the capability census
(who can do it, who could learn it, what record exists), each capability's rebuild unit
and cadence, the learn-lead-teach roster, and the named funding owner. Keep the
committed file structural — roles and capability types, not names, system identifiers,
or access details. Real names, system paths, and anything sensitive belong in
`your-environment.private.md`, which is git-ignored and never committed.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/rebuild-rehearsal.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/rebuild-method.md — the bus-factor census template, rebuild-unit patterns
  by capability type, scheduling rules (cadence shorter than tenure), the
  learn-lead-teach rotation, the gap-harvest protocol, the funding-owner rule with the
  Ōnin lapse told honestly, and a worked domain-neutral example
- references/your-environment.md — your census, rebuild units, cadences, roster, and
  funding owner (sanitized stub; sensitive detail goes in the `.private.md` twin)
