---
name: break-glass-playbooks
description: >-
  Arms each foreseeable crisis with a break-glass playbook, channeling documented
  emergency-access procedures (HIPAA; NIST/CIS-mapped testing) and
  regulator-mandated contingency plans with graduated escalation: define the tripwire
  as a number a named person watches on a stated
  cadence, pre-author the first ten moves at calm-headed quality, pre-grant emergency
  authority with automatic expiry and full logging, name the comms tree and the
  decision chair, drill the unsealing on a schedule, and re-arm after every firing.
  Converts pre-mortem failure modes into tripwire-plus-playbook pairs, red-checks each
  tripwire for measurability, drafts the sealed instructions, and simulates the
  unsealing drill. Use when a crisis is foreseeable but the team would be scrambling
  if it hit. Triggers: break glass, break-glass, seldon crisis, what do we do when X
  hits, emergency access, runbook, kill switch, tripwire, covenant trip, we'd be
  scrambling, sealed instructions.
metadata:
  version: "1.1.0"
  source: >-
    Homage to Asimov's Foundation — pre-recorded guidance that unseals when predicted
    crises arrive — an homage only, no affiliation with the estate or rights holders.
    The skill channels the documented practices: break-glass emergency-access
    procedures (Yale's HIPAA procedure; NIST SP 800-53 / CIS-mapped testing
    requirements) and regulator-mandated contingency plans built on early-warning
    indicators, graduated triggers, and pre-approved action menus.
---

# Break-glass playbooks (tripwires and sealed instructions)

When a predicted crisis lands, the quality of the response is set by what already
exists — the moves that were written, the access that was granted, the number someone
was watching — because nothing written during the alarm will match calm-headed quality.
Two documented practice families supply the pattern. Healthcare compliance requires
break-glass emergency-access procedures: pre-staged, logged emergency accounts that are
documented and *tested*, not merely declared (Yale's HIPAA break-glass procedure)
[gov/compliance], with testing requirements mapped to NIST SP 800-53 and CIS controls
[framework]. Banking supervision mandates contingency funding plans built from
early-warning indicators, graduated stress triggers, and pre-approved action menus
[regulatory]. The anatomy is the same in both and is domain-neutral — indicator →
graduated trigger → pre-authored actions → logged, expiring authority → scheduled
testing — so it transfers to any operation that can foresee its crises.

The design question throughout: **what must already exist when the alarm sounds?**

## When to use
- A pre-mortem — or bitter experience — has produced a list of foreseeable crises, and
  none of them has an armed response: "if that hits, we'd be scrambling."
- Someone asks "what do we do when X hits" and the honest answer is that it lives in
  one person's head, or nowhere.
- An emergency-access path, kill switch, or continuity runbook exists but has never
  been tested, has no owner watching its trigger, or grants authority that never
  expires.
- A threshold breach with contractual or regulatory consequence (for example a covenant
  trip) needs a pre-agreed response instead of an improvised one.
- Natural downstream of `decision-science-skills:pre-mortem`: that skill finds and
  ranks the failure modes; this one converts each surviving failure mode into a
  tripwire-plus-playbook pair. Run them as a pair — a pre-mortem without this stage
  produces a list; this stage without a pre-mortem produces playbooks for the wrong
  crises.
- Sibling `safety-and-reliability-skills:bowtie-barrier-analysis` places these
  playbooks on the map: they are recovery-side (mitigative) barriers on the consequence
  side of the bowtie, and drawing them there exposes which consequence lines still have
  no barrier at all.
- Not for: finding the failure modes in the first place → see
  `decision-science-skills:pre-mortem`.
- Not for: the checklist form of the steps themselves → see
  `safety-and-reliability-skills:checklist-design`; a playbook's read-do steps follow
  its rules (killer items only, imperative voice, anchored pause points).
- Not for: rehearsing against an adaptive adversary → see
  `decision-science-skills:tabletop-wargaming`; the drill here tests the *unsealing
  mechanics*, not adversarial play.
- Not for: deploy/rollback mechanics themselves → see
  `full-stack-dev-skills:deploy-and-operate`, which owns the rollback path and kill-
  switch plumbing; this skill arms the decision to invoke them.
- Not for: keeping the *capability* alive rather than the procedure — periodically rebuilding the
  thing from scratch so the skills, tooling, and documentation are proven by use → see
  `safety-and-reliability-skills:rebuild-rehearsal`. A playbook you can read is not the same as
  a team that has recently done it.

## Do it
The tripwire quality bar, the sealed-instructions template, the drill protocol and log,
and the failure-mode table are in `references/break-glass-method.md`.

1. **Source the crisis list from pre-mortem output.** Take the ranked failure modes
   from `decision-science-skills:pre-mortem` (run one first if none exists) and keep
   the ones that are foreseeable, consequential, and fast-moving enough that improvised
   response would be too slow. Each surviving mode becomes one tripwire-plus-playbook
   pair. The per-scenario tripwires that close a
   `decision-science-skills:minority-report` exercise are prime candidates too — a
   crisis a dissenting future already predicted deserves an armed playbook standing
   behind its tripwire.
2. **Define the tripwire as a number someone actually watches.** Not vibes — a metric
   with a threshold, a named watcher (role, not hero), a stated cadence, and a stated
   place the number lives. Red-check every candidate: who watches this number? how
   often? where? would two people agree it tripped? Add graduation where useful — an
   early-warning level that alerts and a firing level that unseals — the
   graduated-trigger pattern from contingency-plan practice [regulatory].
3. **Pre-author the first ten moves at calm-headed quality.** These are the sealed
   instructions: the first ten concrete moves, written now, while heads are cool, in
   read-do form (`safety-and-reliability-skills:checklist-design` supplies the form).
   Write for a cold reader under stress — the author may be on a plane when it fires.
   Ten moves buys the first hour; it does not script the whole crisis.
4. **Pre-grant the emergency authority — with automatic expiry and full logging.**
   Whatever the first ten moves need (access, spend, the power to halt a process) is
   granted *in advance*, break-glass style: sealed until the tripwire fires, fully
   logged when used, and re-locking automatically after a stated period
   [gov/compliance]. Authority that must be requested at 2 a.m. is the slowest step;
   authority that never expires is a standing hole.
5. **Name the comms tree and the decision chair.** Who is told, in what order, through
   what channel — and who chairs the decisions the playbook does not cover. One named
   chair ends the "who's deciding?" minute that every unowned crisis begins with.
6. **Test the unsealing on a schedule.** A quarterly drill: the watcher recognizes a
   simulated trip, finds the playbook, exercises the authority, and walks the first
   moves. An untested break-glass procedure is decoration — the compliance versions
   make testing a requirement, not a nicety [framework]. Log every drill: date, time
   to unseal, what failed, what was fixed.
7. **After any real firing, feed the after-action findings back.** Run
   `decision-science-skills:after-action-review` on the response, then re-arm: update
   the instructions, reset the authority, confirm the tripwire threshold still sits
   where the crisis actually announced itself, and re-seal. A fired playbook that is
   never re-armed protects against the previous crisis.
8. **Division of labor.** The assistant converts pre-mortem failure modes into
   candidate tripwire-plus-playbook pairs, red-checks each tripwire for measurability,
   drafts the sealed instructions at calm quality, and simulates the unsealing drill by
   playing the cold reader. The humans own the thresholds, the authority grants, the
   chair, and the drill calendar — arming a playbook is a command decision.

## Why / learn
Pre-authoring works because judgment quality is a perishable resource: the same person
writes better instructions on a quiet Tuesday than mid-alarm, so the playbook banks
calm-headed quality and spends it during the crisis. That is the entire trade — effort
now for quality then — and it is why the skill insists the moves be written at
*drafting* quality, not bullet-point intentions. Ten specific moves that a cold reader
can execute beat a page of "assess the situation and communicate appropriately."

The tripwire exists because the hardest question during an emerging crisis is not "what
do we do?" but "is this really it?" — and that argument consumes the hours when acting
is cheapest. A numeric threshold crossed removes the argument; graduation (alert level,
firing level) lets the response scale without reopening the debate at each step, which
is exactly why supervisory contingency plans pair early-warning indicators with
graduated triggers rather than a single alarm [regulatory]. The named watcher matters
as much as the number: an unwatched metric is a tripwire in a forest.

The authority grant resolves a real tension rather than pretending it away. Standing
emergency power erodes control — that is how privileged access sprawls — but requesting
power during the emergency is the slowest step in the response. Break-glass practice
threads it: generous in the moment, sealed until needed, fully logged, and re-locking
on a timer [gov/compliance]. The expiry is not bureaucracy; it is what makes the
generosity affordable.

Drills exist because sealed things decay silently: people leave, systems move,
credentials rotate, storage links die. A playbook fails in exactly one of two visible
ways — at the drill, cheaply, or at the crisis, expensively — and the drill is how you
choose which. The compliance framing (testing mapped to NIST SP 800-53 / CIS controls)
is useful precisely because it converts "we should test it sometime" into a scheduled
obligation [framework]. The feedback loop closes the design: each drill and each real
firing is the only ground truth the playbook ever receives, and a playbook that does
not absorb it is aging fiction with a good filing system.

## Common mistakes
- Vibes tripwire ("we'll know it when we see it") → a metric with a threshold, a named
  watcher, a cadence, and a location; two people must agree it tripped.
- Untested seal → schedule the first drill the day the playbook is written; no drill
  date on the calendar means the playbook is decoration.
- Authority without expiry → automatic re-lock plus full logging; emergency power that
  lingers becomes standing power nobody remembers granting.
- Playbook nobody can find → store it where the crisis cannot take it down (not solely
  on the system whose outage it handles) and make the watcher name its location cold
  in every drill.
- Instructions that assume the author responds → write for a cold reader; run the
  drill with someone who did not write them.
- Ten vague moves → read-do specificity, per checklist-design; "assess and
  communicate" is not a move.
- Confusing the unsealing drill with adversarial rehearsal → the drill tests
  mechanics; playing a thinking adversary belongs to
  `decision-science-skills:tabletop-wargaming`.
- Never re-arming after a firing → the playbook now protects against the previous
  crisis; after-action findings feed the update, then re-seal.
- Arming playbooks for crises nobody foresaw in a structured way → garbage in; run
  `decision-science-skills:pre-mortem` first so the list is worth arming.

## Tailor to your environment
Record your standing arsenal in `references/your-environment.md`: the crisis list and
which pre-mortem produced it, the tripwire registry (metric, threshold, watcher role,
cadence, location), where playbooks are stored, the drill calendar and its owner, and
how expiring authority is implemented in your systems. Keep the committed file
structural — roles and mechanisms, not live thresholds. Real trigger values, system
names, account identifiers, and access paths belong in `your-environment.private.md`,
which is git-ignored and never committed.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/break-glass-playbooks.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/break-glass-method.md — the tripwire quality bar, the sealed-instructions
  template (first ten moves, authority grant with expiry, comms tree, decision chair),
  the drill protocol and drill log, the re-arm/feedback loop, and the failure-mode
  table, with sources
- references/your-environment.md — your crisis list, tripwire registry, storage, and
  drill calendar (sanitized stub; live values go in the `.private.md` twin)
