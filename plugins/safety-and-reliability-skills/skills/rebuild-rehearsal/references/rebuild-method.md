# The rebuild-rehearsal method: census, units, cadence, rotation, harvest, funding

Method lineage: the Shikinen Sengu of the Ise Grand Shrine — full reconstruction every
20 years since 690 CE, carpenters participating two or three times per working life
(learn → lead → teach), a 200-year in-house forestry plan begun 1923, and a ~120-year
lapse after the Ōnin War (Inner Shrine 1462–1585) revived by the fundraising nuns of
Keikō-in with warlord endowment behind them — Oda Nobunaga from 1569, though he died in
1582 and the 1585 rebuild fell to his successors [snippet-only: japanfs.org, Smithsonian,
woodcentral, Wikipedia]. Shinise footnote: Kongō Gumi, temple builders founded 578,
independent until liquidation in 2006 [snippet-only: Wikipedia, INSEAD]. The pattern is
domain-neutral: exercise the capability on a schedule shorter than a career, with the
last builders present to correct the next ones.

## Contents
- [The bus-factor census template](#the-bus-factor-census-template)
- [Rebuild-unit patterns by capability type](#rebuild-unit-patterns-by-capability-type)
- [Scheduling rules: cadence shorter than tenure](#scheduling-rules-cadence-shorter-than-tenure)
- [The learn-lead-teach rotation](#the-learn-lead-teach-rotation)
- [The gap-harvest protocol](#the-gap-harvest-protocol)
- [The funding-owner rule (the Ōnin lapse, told honestly)](#the-funding-owner-rule-the-ōnin-lapse-told-honestly)
- [Worked example: a two-person team](#worked-example-a-two-person-team)
- [Sources](#sources)

## The bus-factor census template

One row per capability the operation depends on. A capability is anything with the
property "if nobody here could do this, something we owe someone would stop."

| Capability | Who can do it | Who could learn it | Written record | Last done by a non-primary | Criticality |
|---|---|---|---|---|---|
| Produce the monthly deliverable | (role/name) | (role/name) | runbook? where? | date or "never" | halts / degrades / annoys |
| Restore the shared drive from backup | | | | | |
| Stand up the working environment | | | | | |
| Run the intake process end to end | | | | | |

Census questions the assistant asks to fill it: What would stop shipping if X were
unreachable for a month? What did the last new joiner have to ask a human to get
running? Which artifacts does someone outside the team receive on a schedule, and who
can produce each? What has never been done twice by two different people?

Red flags to mark: any row where "who can do it" is one name (bus factor 1); any row
where the written record exists but "last done by a non-primary" is "never" (docs are
untested claims); any row where the record is a person's private notes.

## Rebuild-unit patterns by capability type

The rebuild unit is the smallest exercise that produces the real artifact from the
surviving record. It must be able to fail — an exercise that cannot fail measures
nothing. Pick per capability type:

- **Stored data / backups** → restore the actual backup to a scratch location and open
  the result. Not "confirm the backup job ran": jobs run green for years while writing
  garbage. Success test: a named file opened, a named record read back.
- **Recurring deliverable** (a monthly report, a filing, an invoice run, a board pack)
  → recreate one past period's deliverable from raw inputs using only the runbook, then
  diff against what was actually sent. Success test: differences are explainable.
- **Environment / tooling** (a dev environment, an analysis toolchain, a case-management
  configuration) → stand it up from the docs alone on a clean machine or account.
  Success test: the standard task runs end to end in the fresh copy.
- **Process** (client intake, onboarding, month-end close, matter opening) → run one
  real or realistic instance with the runbook and a newcomer driving. Success test:
  completion without an undocumented human intervention — every intervention is a
  logged gap. **Screen the runbook for irreversibility first** — see below; this is the
  one pattern in this list that can reach outside the rehearsal.

### The irreversibility screen (Process rehearsals only)

Every other pattern here is safe by construction: restores go to a scratch location,
deliverables recreate a *past* period and diff, environments stand up on a clean machine.
The Process pattern is the exception — it puts a newcomer, following a document, in the live
system with real authority, on processes named as client intake, onboarding, month-end close
and matter opening. Those contain steps that leave the building.

Before the rehearsal, walk the runbook and mark every step:

| Class | Examples | In rehearsal |
|---|---|---|
| Reversible | internal record created, draft saved, checklist ticked | **Execute** |
| External, reversible with effort | an internal notification, a calendar hold | Execute only if the recipient is briefed |
| **External and irreversible** | money moved, a filing submitted, a client or counterparty contacted, a record the retention schedule locks, a credential rotated, anything a regulator or third party sees | **Declare and simulate — never execute** |

Two rules follow, and they invert the ordinary rehearsal discipline:

- **The corrector speaks *before* an irreversible step, not after.** The default rule — stay
  silent until the driver errs, then correct out loud — is exactly right for reversible work,
  because the error is the finding. At an irreversible step the error is not recoverable, so
  the corrector confirms the driver's intent before it executes. The gap is still logged; it is
  simply logged without being paid for.
- **Prefer a past period or a sandbox instance.** Re-running last month's intake against a
  copy, or a genuinely fictitious matter marked as such, tests the same runbook with the
  external edges removed. Use a live instance only when nothing else exercises the step, and
  then only with the irreversible steps simulated.

**Abort trigger, stated before the start:** the rehearsal hands back to the veteran the moment
a real client, a real deadline, or a real counterparty is affected, or the driver cannot tell
whether the next step is reversible. Handing back is a successful rehearsal that found its
limit, not a failed one — and "we weren't sure, so we kept going" is the sentence this trigger
exists to prevent.
- **Relationship / negotiation knowledge** (the vendor history, the regulator context)
  → hardest to rebuild; the unit is a briefing the newcomer writes from the record and
  the veteran corrects. Weakest pattern; flag these rows for deliberate shadowing.

## Scheduling rules: cadence shorter than tenure

Ise's 20-year interval works because a craftsman's working life spans two or three
cycles — the number is set by the career, not the calendar. Scaled rules:

1. **The two-rehearsal rule.** Everyone who should hold the capability gets at least
   two rehearsals (once apprenticing, once leading) within their realistic tenure. If
   people typically stay three years, an annual cadence is the *maximum* interval.
2. **Criticality shortens it.** Would a loss halt the operation? Quarterly. Degrade
   it? Annually. Merely annoy? Rehearse opportunistically — each real occurrence with
   a newcomer driving counts.
3. **Change shortens it.** A capability whose surrounding systems change monthly rots
   faster than tenure alone predicts; rehearse after major changes, not just on the
   calendar.
4. **Put it on the calendar as a standing series, owned by the funding owner.** An
   unscheduled rehearsal is a good intention; the Ōnin section explains what happens
   to those.
5. **Alternate simulated and real.** The assistant's simulated rebuild (below) can run
   monthly at near-zero cost; the real rehearsal anchors the cycle. Simulation between
   real runs, never instead of them.

## The learn-lead-teach rotation

Each rehearsal has three seats:

- **Driver (apprentice):** the person with the *least* knowledge executes from the
  written record alone. Their questions are the yield.
- **Lead:** last rehearsal's driver. Plans the rehearsal, sets the success test,
  decides when to break silence. Leading is the second exposure — it converts
  familiarity into ownership.
- **Corrector (veteran/teacher):** the current primary. Stays silent until the driver
  errs or stalls, then corrects *out loud* so the correction is heard and logged.
  Teaching is the third exposure — and the veteran's exit interview, run early and
  repeatedly, while they still work here.

Rotation rule: after each rehearsal everyone shifts one seat (driver → lead → corrector
→ out). Three cycles turn a newcomer into a teacher. In a two-person team the seats
compress — the newcomer drives, the primary corrects, and "lead" alternates — but the
principle survives: the person who knows least executes; the person who knows most only
corrects.

The assistant takes the driver's seat between real rehearsals: given only the written
record, it simulates executing each step and asks the questions a cold newcomer would
("step 3 says 'load the file as usual' — which file, from where, with what tool?").
Every question it cannot answer from the record is a gap harvested for free.

## The gap-harvest protocol

The rehearsal is the documentation's test; the harvest is what makes the test pay.

1. **Log during, verbatim.** Every question the driver asks a human, every step that
   needed an intervention, every stale credential, dead link, renamed system, and
   missing prerequisite — logged as it happens, in the driver's words.
2. **Triage within a week**, while memory is fresh: each gap becomes a doc fix, a
   process fix (the doc was right; the system drifted), or an accepted risk with a
   name on it.
3. **Fix the record before closing.** The rehearsal closes only when every logged gap
   is resolved or explicitly accepted. Passing this to
   `writing-skills:explanation-design` is the natural handoff for gaps that are
   explanation problems rather than missing facts.
4. **Keep a one-line log per rehearsal:** date, capability, driver, time to complete,
   gaps found, gaps fixed. The trend line is the health of the record: gap counts
   should fall rehearsal over rehearsal; a rising count means the system is drifting
   faster than the docs are maintained.

## The funding-owner rule (the Ōnin lapse, told honestly)

The Ise cycle is often told as thirteen unbroken centuries. It was not. After the Ōnin
War devastated the shrine's economic base, the Inner Shrine went roughly 120 years
without rebuilding (1462–1585). What revived it was not reverence — reverence had never
left — but money and named sponsorship, sustained across generations: the nuns of
Keikō-in fundraised across the country for decades (the Uji bridge in 1545, the Outer
Shrine in 1563), and warlord endowment backed them — Oda Nobunaga resumed funding the
shrine in 1569 and died in 1582, so the 1585 Inner Shrine rebuild was completed by his
successors [snippet-only]. That the revival outlasted its own patron is the point: it
took a funding line, not one benefactor. The practice survived because someone made
funding it their job — and kept making it someone's job.

The transferable rule: **a renewal cycle without a funding owner silently lapses.**
Renewal work has a structural weakness in every budget fight — skipping it costs
nothing today, so it is the first casualty of a busy quarter, and the lapse produces no
alarm. The countermeasure is not enthusiasm but ownership:

- Name a role (not a hero) who owns the rehearsal calendar and its resourcing.
- Give the cycle a standing budget line — hours count as budget; "when we have time"
  is the lapse in written form.
- Make the lapse visible: the one-line rehearsal log has a date column, and a gap in
  the dates is the alarm. Ise's modern rebuilds are visible national events partly
  because visibility is itself protection.
- On any ownership transition, the cycle transfers explicitly — the most common
  modern lapse is the owner leaving and the calendar series dying with their account.

## Worked example: a two-person team

Setup: an office of two — a manager and an analyst — owns a shared drive and a monthly
deliverable assembled from raw inputs (exports from two systems, one spreadsheet of
manual adjustments). The analyst built the process; the manager has never run it. The
census shows two bus-factor-1 rows: "produce the monthly deliverable" and "restore the
shared drive."

- **Rebuild units.** (1) Restore last month's shared-drive backup to a scratch folder
  and open three named files from it. (2) Recreate last month's deliverable from the
  raw inputs using only the runbook, and diff it against the version actually sent.
- **Cadence.** Deliverable: quarterly (a halting capability; analyst tenure is
  uncertain). Restore: twice a year, plus after any change to the backup arrangement.
- **Rotation, compressed for two.** The manager drives with the runbook; the analyst
  sits behind, silent until a stall, correcting out loud. Between quarters, the
  assistant plays driver: given the runbook alone, it simulates the rebuild and
  returns its blocked-step questions ("the runbook says 'apply the usual adjustments'
  — where is the adjustments file and what makes an adjustment 'usual'?").
- **First rehearsal, typical yield.** The manager stalls at step 2 (an export filter
  that lives only in the analyst's saved view), step 5 ("reconcile the two totals" —
  no stated tolerance for what counts as reconciled), and step 7 (a distribution list
  that exists only in the analyst's mail client). Three gaps, logged verbatim, fixed
  in the runbook within the week.
- **Diff test.** The recreated deliverable differs from the sent one in one column —
  traced to a manual adjustment that was never written down. That adjustment now has a
  documented rule.
- **Funding owner.** The manager — the person who *can't* yet do the work — owns the
  calendar and the hours, which is the right assignment: the owner of the cycle should
  be the person most exposed by its lapse.
- **Second rehearsal.** Two new gaps (one system renamed a menu), zero repeats. The
  trend line points the right way, and the manager has now produced the deliverable
  twice: the capability exists in two heads and one tested record.

## Sources

All external claims [snippet-only] — WebSearch snippets cross-checked across
independent results; see the repo's research dossier
(`docs/research/epic-wave-held-research.md`, Lane 1 entry 3) for the full provenance
notes.

- Japan for Sustainability on the Shikinen Sengu — the 20-year cycle, its rationale,
  and the forestry plan
- Smithsonian and Wood Central coverage of the rebuild practice and the in-house
  hinoki forestry program
- Wikipedia: Ise Grand Shrine (the Ōnin-era interruption and 1585 revival; Keikō-in's
  fundraising; Oda Nobunaga's endowment from 1569 and his death in 1582), Kongō Gumi
  (founded 578; 2006 liquidation; Takamatsu subsidiary)
- INSEAD on shinise longevity — single-craft focus and flexible succession
