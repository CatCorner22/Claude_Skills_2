# The break-glass method: tripwires, sealed instructions, drills, re-arm

Method lineage: break-glass emergency-access procedures in healthcare compliance —
documented, pre-staged, logged, and tested emergency accounts (Yale's HIPAA break-glass
procedure) [gov/compliance], with testing requirements mapped to NIST SP 800-53 and CIS
controls [framework]; and regulator-mandated contingency funding plans built from
early-warning indicators, graduated stress triggers, and pre-approved action menus
[regulatory]. The anatomy — indicator → graduated trigger → pre-authored actions →
logged, expiring authority → scheduled testing — is domain-neutral. Source links at the
end of this file.

## Contents
- [The tripwire quality bar](#the-tripwire-quality-bar)
- [The sealed-instructions template](#the-sealed-instructions-template)
- [The authority grant](#the-authority-grant)
- [The drill protocol and drill log](#the-drill-protocol-and-drill-log)
- [The re-arm / feedback loop](#the-re-arm--feedback-loop)
- [Failure-mode table](#failure-mode-table)
- [Sources](#sources)

## The tripwire quality bar

A tripwire passes only if all five hold:

1. **Measurable** — a number or an unambiguous binary event, never a mood. "Queue age
   over 48 hours" passes; "the queue feels out of control" fails.
2. **Watched** — a named watcher, by role, whose routine actually includes looking.
   If watching is nobody's job, the tripwire does not exist.
3. **Cadenced** — the watch frequency is stated and is faster than the crisis develops.
   A weekly glance cannot catch a four-hour failure.
4. **Thresholded** — the firing value is written down in advance, so two people would
   agree it tripped without a meeting.
5. **Located** — the number lives in a stated place the watcher can reach; a metric
   that requires an engineer to compute is not watched, it is commissioned.

**Graduation** (from contingency-plan practice [regulatory]): where the crisis develops
in stages, set two levels — an *early-warning* level that alerts the watcher and the
chair, and a *firing* level that unseals the playbook. The alert level buys preparation
time; the firing level removes the "is this really it?" debate.

**Red-check script** (the assistant runs this on every candidate): who watches this
number? how often? where does it live? what exact value fires it? what could cross the
threshold without being the crisis (false trip), and what crisis could arrive without
crossing it (silent failure)? A candidate that fails the last question needs a second,
independent tripwire on the same crisis.

## The sealed-instructions template

One playbook per crisis. Header first, moves second, nothing else required.

```
PLAYBOOK: <crisis name>                        Version / date / author
TRIPWIRE: <metric, threshold, watcher role, cadence, location>
UNSEALS:  <who may declare the trip — usually watcher + chair concurrence>
CHAIR:    <role that chairs decisions this playbook does not cover>
AUTHORITY:<what is pre-granted, to which role, expiry period, where logged>
COMMS:    <who is told, in what order, via what channel; the out-of-band fallback>
FOUND AT: <primary and secondary storage — at least one reachable if the
           affected system is down>

FIRST TEN MOVES (read-do; a cold reader under stress is the audience)
 1. <verb-first, specific, executable without the author>
 2. ...
10. <the tenth move is almost always: convene the chair and decide what the
    playbook cannot — with moves 1–9 done, that conversation starts ahead>
```

Rules for the moves:

- **Read-do form** — each step read aloud, done, confirmed, in order; the form and its
  killer-item discipline come from the checklist-design skill.
- **Ten moves buys the first hour.** The playbook is not a script for the whole
  crisis; it is the bridge from alarm to functioning command.
- **Each move names its actor** (role) and its "done" condition.
- **No move may depend on calm-time resources** — the authoring system, the author's
  memory, a login nobody else holds.
- **Write at drafting quality.** Full sentences, exact names of things, no "assess" or
  "communicate appropriately." The value banked is precisely the quality that will be
  unavailable later.

## The authority grant

What the first ten moves need is granted in advance, break-glass style
[gov/compliance]:

- **Scope**: the minimum that moves 1–10 require — access, spend limit, the power to
  halt a process or invoke a rollback path. Enumerate it; "whatever it takes" is not
  a grant, it is an abdication.
- **Sealed until fired**: usable only on a declared trip; the declaration itself is
  logged (who, when, which tripwire value).
- **Fully logged in use**: every action under the grant leaves a record — that audit
  trail is what makes the pre-grant defensible.
- **Automatic expiry**: the grant re-locks on a timer (hours to days, stated in the
  header). Extending it is a chair decision, made on the record — never a default.
- **Re-verified at every drill**: expired credentials and moved systems are the most
  common drill findings.

## The drill protocol and drill log

Cadence: quarterly is the practice-level default; never less than the rate at which
your people and systems change. The drill tests the *mechanics of unsealing*, not
adversarial play (that is tabletop-wargaming's job).

Protocol, timed end to end:

1. Inject a simulated tripwire reading to the watcher through the normal channel.
2. Watcher recognizes the trip, declares it, and names the playbook's location cold.
3. Reader — someone who did not write the playbook — retrieves it and walks the first
   moves (execute harmless ones; state-changing ones are walked to the brink and
   confirmed executable).
4. Authority is exercised far enough to prove it works: the access opens, the log
   writes, the expiry is set.
5. Comms tree is exercised at least one hop, including the out-of-band fallback.
6. Debrief in one page: what stalled, what was stale, what the cold reader could not
   parse.

Drill log, one line per drill — kept with the playbook:

```
DATE | playbook | time-to-unseal | authority worked? (Y/N) | stale items found |
fixes filed | next drill date
```

A playbook with an empty drill log is unarmed regardless of how good its prose is.

## The re-arm / feedback loop

After every real firing — and every drill that found anything:

1. Run the after-action ritual (the after-action-review skill owns the format): what
   was supposed to happen, what actually happened, why the difference.
2. Update the moves where reality diverged; retire moves nobody used; add the move
   everyone improvised.
3. Re-check the tripwire against how the crisis actually announced itself — thresholds
   are usually set too high the first time, cadences too slow.
4. Reset the authority (close the grant, confirm re-lock, re-verify credentials).
5. Bump the version, re-seal, and set the next drill date.

Skipping re-arm is the quiet failure: the playbook still exists, still looks armed,
and now defends against the previous crisis.

## Failure-mode table

| Failure mode | What it looks like | The fix |
|---|---|---|
| Vibes tripwire | "We'll know it when we see it" | Metric + threshold + named watcher + cadence + location; two people would agree it tripped |
| Unwatched number | Metric exists, nobody's routine includes it | Watching named in a role's standing duties; drill injects test the channel |
| Untested seal | Playbook written, never drilled | Drill date set at authoring time; empty drill log = unarmed |
| Authority without expiry | Emergency access that never re-locked | Automatic expiry + full logging; extension is a logged chair decision |
| Playbook nobody can find | Stored only on the system that is down, or in the author's drive | Two locations, one out-of-band; watcher names them cold at every drill |
| Author-dependent instructions | Steps only the writer can execute | Cold-reader drill; each move names an actor role and a done-condition |
| Vague moves | "Assess the situation and communicate" | Read-do specificity per checklist-design; verb-first, executable |
| Never re-armed | Fired once, never updated | Re-arm loop after every firing; version bump + new drill date |

## Sources
From the library's research dossier (Lane 2); provenance marks as recorded there:

- Yale HIPAA break-glass procedure:
  [hipaa.yale.edu](https://hipaa.yale.edu/security/break-glass-procedure-granting-emergency-access-critical-ephi-systems)
  [gov/compliance]
- Break-glass testing mapped to NIST SP 800-53 / CIS 17:
  [hoop.dev overview](https://hoop.dev/blog/break-glass-access-under-the-nist-cybersecurity-framework/)
  [framework]
- Regulator-mandated contingency funding plans (early-warning indicators, graduated
  triggers, pre-approved action menus):
  [Fed SR 10-6](https://www.federalreserve.gov/boarddocs/srletters/2010/sr1006.htm),
  [interagency update](https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20230728a1.pdf)
  [regulatory] — cited at practice level; the mechanism is domain-neutral.
