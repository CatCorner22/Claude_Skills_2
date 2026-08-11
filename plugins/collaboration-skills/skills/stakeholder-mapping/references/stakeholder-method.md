# Stakeholder method — grid, RACI, currencies, re-map

Depth for `collaboration-skills:stakeholder-mapping`. Everything here is structural;
worked-example figures and names are illustrative by construction. Provenance:
[snippet-only] = verified via cross-checked search snippets, not primary documents.

## Contents
1. [Build the list](#1-build-the-list)
2. [The power-interest grid — and who actually published it](#2-the-power-interest-grid--and-who-actually-published-it)
3. [Quadrant engagement moves](#3-quadrant-engagement-moves)
4. [RACI — rules and the no-inventor note](#4-raci--rules-and-the-no-inventor-note)
5. [Currencies of exchange](#5-currencies-of-exchange)
6. [The re-map protocol](#6-the-re-map-protocol)
7. [Worked example — a system migration](#7-worked-example--a-system-migration)
8. [Two more shapes — multi-party matter, deprecation without authority](#8-two-more-shapes--multi-party-matter-deprecation-without-authority)
9. [Privacy — never commit a real power map](#9-privacy--never-commit-a-real-power-map)

## 1. Build the list

Prompts that surface stakeholders the org chart hides:

- Who must **approve** — formally (signature, budget, legal) and politically (the
  person whose silence reads as veto)?
- Whose **behavior must change** for the work to succeed? (They hold operational veto
  regardless of rank.)
- Who **benefits from the status quo** the work disturbs?
- Who **owns an adjacent system or process** the work touches?
- Who was **burned last time** something similar was tried?
- Who will **inherit** the result — maintenance, support, audit?
- Who talks to whom? (An influencer with the decision-maker's ear is a stakeholder even
  with no formal role.)

For each entry record: role, stake (what they gain or lose), current stance
(supporter / neutral / opponent / unknown), and the evidence for that stance. Stance
without evidence is an inference — tag it as one.

## 2. The power-interest grid — and who actually published it

Two axes: **power** (capacity to help or block the work) and **interest** (how much the
outcome touches them). Each stakeholder lands in one of four quadrants:

```
            high power
        ┌────────────┬────────────┐
        │   KEEP     │   MANAGE   │
        │ SATISFIED  │  CLOSELY   │
 low ───┼────────────┼────────────┤─── high
interest│  MONITOR   │    KEEP    │  interest
        │            │  INFORMED  │
        └────────────┴────────────┘
            low power
```

**The attribution record**, which this library teaches openly because the folklore
version fails checking:

- **A. L. Mendelow, 1981** — "Environmental Scanning—The Impact of the Stakeholder
  Concept," *Proceedings of the 2nd International Conference on Information Systems*
  (ICIS), Cambridge MA. Secondary sources that actually engage the paper report its
  matrix as **power/dynamism** — a contingency model for environmental scanning — not
  power/interest [snippet-only, convergent secondary; the ICIS paper itself (AIS
  eLibrary, paper 20) was not fetched — reading it would upgrade this to primary].
- **Eden & Ackermann, 1998** — *Making Strategy: The Journey of Strategic Management*
  (Sage), power-interest grid at p. 349 [snippet-only].
- **Johnson & Scholes, 1999** — *Exploring Corporate Strategy*, which adapted
  Mendelow's model by replacing the dynamism axis with interest [snippet-only].
- **Lineage**: R. Edward Freeman, *Strategic Management: A Stakeholder Approach*
  (Pitman, 1984) is the foundational stakeholder-theory text; the word "stakeholder"
  traces to a Stanford Research Institute working group, ~1963 — Freeman credits it,
  and crediting Freeman as coiner is the standard error [snippet-only].

Citation rule: **grid → Johnson & Scholes or Eden & Ackermann; Mendelow → the idea that
stakeholder power should drive scanning priority; Freeman → the theory, not the word.**

Placement discipline:
- Rate power and interest **relative to this work**, not to the org at large — a CFO
  with no stake in your migration is high power in general and possibly "monitor" here.
- Tag each placement *evidence* or *inference*. Inferences get tested (often via a
  conversation — `collaboration-skills:disarming-elicitation`) before a move rests on
  them.
- Date the grid. A snapshot without a date pretends to be a truth.

## 3. Quadrant engagement moves

The four labels — manage closely, keep satisfied, keep informed, monitor — are
**folk-simplifications layered onto the grid**: memorable defaults from the teaching
tradition, not part of the cited sources. Use them as effort allocations with the
following honest content:

| Quadrant | Default move | What it actually means | Failure if botched |
|---|---|---|---|
| High power, high interest | **Manage closely** | Partner status: involve in shaping, not just deciding; designed decision forums; early sight of problems | They discover a problem late and use their power on the process, not the substance |
| High power, low interest | **Keep satisfied** | Identify their few actual concerns and pre-empt them; short, rare, high-signal contact | Newsletter spam breeds annoyance; silence breeds ambush when interest awakens |
| Low power, high interest | **Keep informed** | Honest, regular, effortful communication; they are the work's chorus and early-warning net | Neglected, they become the opposition's best-informed recruits |
| Low power, low interest | **Monitor** | Watch for quadrant movement; no proactive investment | Effort spent here is taken from the quadrants that decide the outcome |

Instruments for the moves: decision forums → `collaboration-skills:meeting-design`;
learning what a stakeholder knows → `collaboration-skills:disarming-elicitation`;
behavior conversations → `collaboration-skills:feedback-that-lands`; bargaining with a
counterpart → `decision-science-skills:principled-negotiation`.

## 4. RACI — rules and the no-inventor note

**Provenance honesty**: responsibility assignment matrices descend from **linear
responsibility charting**, documented from the 1950s, through 1970s responsibility
assignment / decision-rights matrix practice. The RACI acronym itself has **no named
inventor and no canonical origin paper** — vendor and consultancy pages confidently
narrate inventors and dates that do not survive checking [snippet-only, multiple
convergent]. "No canonical source" is the honest sentence.

| Letter | Meaning | Rule |
|---|---|---|
| **R** — Responsible | Does the work | At least one per row; several is fine |
| **A** — Accountable | Answers for the outcome | **Exactly one per row** — two accountables is zero |
| **C** — Consulted | Two-way, **before** the decision | If they learn of the decision after it's made, the C was a lie |
| **I** — Informed | One-way, **promptly after** | Late "informed" is how allies become opponents |

Construction rules:
- Rows are workstreams or decisions, not job titles.
- Write it *with* the mapped stakeholders' knowledge, not about them in secret — a
  RACI nobody agreed to assigns obligations nobody accepted.
- Cross-check against the grid: every manage-closely stakeholder should hold an A, R,
  or C somewhere; a high-power stakeholder who is only ever "I" is a placement error in
  one of the two artifacts.
- The C/I distinction is the whole tool: "consulted" means input while the decision is
  still open. Most RACI failures are C's treated as I's — hence the skill's slogan,
  *"consulted" stops meaning "surprised."*

## 5. Currencies of exchange

Allan R. Cohen & David L. Bradford, *Influence Without Authority* (Wiley, 1989; 2nd ed.
2005): influence over people you cannot command is **exchange**, powered by the law of
reciprocity, denominated in currencies — what the other party actually values
[snippet-only]. Their five families:

| Currency family | Examples you can genuinely offer |
|---|---|
| **Inspiration** | The work's meaning; the chance to matter; alignment with a value they hold |
| **Task** | Help with their workload; resources; faster turnaround on what they need from you; migration labor |
| **Position** | Visibility with their leadership; credit given publicly; association with a win |
| **Relationship** | Being heard; inclusion; gratitude that costs you effort, not words |
| **Personal** | Ownership of a piece; the chance to learn something; fewer interruptions |

Building the plan for a stakeholder you cannot compel:
1. Name what you are actually asking for (specific behavior, by when).
2. Diagnose their world: what do they get measured on, what is scarce for them, what
   have they asked for lately?
3. Find the currencies you can genuinely pay — offers you can keep, made openly.
4. Open the exchange as a colleague, not a bargainer: state your ask, offer your side,
   let them counter.

The rail: exchange is done **in the open** — both sides could name the trade without
embarrassment. A trade that requires concealment is not influence; it is politics, and
it converts to opposition on discovery.

## 6. The re-map protocol

The map is a snapshot, not a truth. Re-draw it:

- **At named milestones** — scope freeze, budget approval, pilot, go-live: each shifts
  who has power over what remains and whose interest awakens.
- **At any reorganization** — placements inherit from roles; when roles move, the grid
  is stale by construction.
- **On contradiction** — a stakeholder's behavior contradicts their placement (the
  "monitor" who suddenly asks detailed questions is telling you their quadrant).
- **After a pre-mortem** — run `decision-science-skills:pre-mortem` with
  stakeholder-shaped failure narratives ("it failed because the keep-satisfied
  executive was ambushed by X"); every credible narrative revises a placement or move.

Each re-map records the deltas: who moved, which way, on what evidence. The deltas are
the intelligence — a stakeholder drifting toward high interest ahead of a milestone is
the early warning the first map existed to buy.

## 7. Worked example — a system migration

An ops manager migrates intake from a shared mailbox to a routed-queue system. Roles
only — a real map with names goes in the git-ignored private file. All placements
illustrative.

| Stakeholder (role) | Power | Interest | Quadrant | Stance (evidence?) |
|---|---|---|---|---|
| COO (sponsor) | High | Med-high | Manage closely | Supporter (approved memo) |
| Claims team lead | Med-high | High | Manage closely | Opponent (said so — evidence) |
| Finance director | High | Low | Keep satisfied | Neutral (inference) |
| Legal/compliance | High | Low→? | Keep satisfied | Unknown — not yet told |
| Intake staff (3 teams) | Low-med | High | Keep informed | Mixed (survey) |
| IT platform owner | Med | Med | Manage closely (borderline) | Supporter if scoped (evidence) |
| Audit (inheritor) | Med | Low | Monitor → re-map at go-live | Unknown |

Moves that follow:
- **Claims team lead (opponent, manage closely)**: not a broadcast target — a
  conversation. First elicitation (what does the current mailbox flow do for claims
  that the design misses? → `collaboration-skills:disarming-elicitation`), then, if a
  genuine trade is needed, currencies: task currency (migration labor for their queue
  rules), position currency (named co-designer in the go-live note).
- **Finance director (keep satisfied)**: one page, pre-empting their one real concern
  (does the queue change how intake costs are allocated?) — not weekly updates.
- **Legal untold** is the map's loudest finding: high power, interest currently low
  only because they don't know. Brief them before they discover it — surprise converts.
- **RACI extract** (rows = workstreams): Routing rules — A: ops manager, R: IT
  platform owner, C: claims lead + team leads, I: intake staff. Cost allocation note —
  A: finance director, R: analyst, C: ops manager, I: COO. Go-live comms — A: ops
  manager, R: team leads, C: legal, I: all.
- **Pre-mortem narrative that changed the map**: "it failed because audit's
  record-retention requirement surfaced in week ten" → audit moved from monitor to
  keep-informed with a consultation before the routing rules froze.
- **Re-map triggers**: pilot end, go-live, and any reorg of the three intake teams.

## 8. Two more shapes — multi-party matter, deprecation without authority

**Attorney, multi-party matter.** Separate the *legally required* approvals (signature
authority, board consent, regulator) from the *politically required* ones (the
co-counsel whose silence kills momentum, the client-side executive who was burned by
the last deal). Grid both kinds; the legally required are fixed points, the politically
required are where quadrant moves and currencies operate. For the party you cannot
compel — opposing counsel's cooperative scheduling, a third party's estoppel letter —
build the currencies plan; when they become a true counterpart, hand off to
`decision-science-skills:principled-negotiation`.

**Developer, deprecation without authority.** Sunsetting an internal API: consumer
teams hold operational veto (they can simply not migrate). Grid them by power (traffic
share, escalation reach) and interest (how much the migration costs them). Currencies
that work here: task (migration PRs written for them, shims maintained), position
(their name on the design doc), relationship (a real deprecation timeline honored).
The laggard team with high traffic and zero interest is the classic keep-satisfied
trap — their concern is "zero work for us," so the winning trade is usually labor, not
persuasion. RACI the cutover; re-map when traffic crosses each threshold.

## 9. Privacy — never commit a real power map

A power-interest grid of real colleagues is a written record of who you consider
powerful, indifferent, or opposed — org politics on the record. Leaked, it damages
every relationship on it, including the accurate rows.

- Committed files carry **roles and structure only** (as in §7).
- Real names, actual placements, stance evidence, currencies plans, and anything about
  live org dynamics go in `your-environment.private.md` / `*.private.md` — patterns the
  repo `.gitignore` already excludes.
- The same rule extends to exports: no real map into shared drives, tickets, or slides
  without deliberately deciding who may read it.
