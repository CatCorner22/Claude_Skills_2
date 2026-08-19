---
name: weak-signal-navigation
description: >-
  Estimates a current position or state when the usual instrument — a dashboard, tracker,
  status report, or data feed — is down, stale, or untrusted, by fusing many weak
  independent cues (last known-good state, scheduled events that must have fired,
  historical rhythms, side channels, absence of expected noise) into a continuously
  re-estimated belief with a stated confidence band; narrates which cue the position
  leans on hardest, updates as cues arrive, and defines what will confirm or deny the
  belief when the instruments return (the method of Polynesian/Micronesian wayfinding
  and etak — Hokule'a, Mau Piailug, Hutchins' distributed-cognition analysis). Use when
  a decision needs the position anyway and the authoritative number is missing or
  disbelieved. Triggers: wayfinding, weak signals, estimate blind, the dashboard is
  down, I don't trust this number, navigate without instruments, what would we expect
  to see, position without the data, dead reckoning.
metadata:
  version: "1.1.0"
  source: >-
    Built from the library's operational-wisdom research lane
    (docs/research/epic-wave-held-research.md, Lane 1 entry 1). The mechanism is
    documented practice, not legend: the 1976 Hokule'a voyage navigated by Mau Piailug,
    the etak technique recorded by David Lewis (We, the Navigators), and Edwin Hutchins'
    distributed-cognition analysis — all [snippet-only] provenance, cross-checked across
    independent sources.
---

# Weak-signal navigation (wayfinding without instruments)

In 1976 the voyaging canoe Hokule'a sailed from Hawaii to Tahiti — roughly 2,500
nautical miles in 31 days — with no compass, sextant, or chart, navigated by Mau
Piailug of Satawal, trained in the Weriyeng school from age four; landfall at Mataiva
was predicted a day out by three navigators using different methods [snippet-only].
The technique behind it, etak, was recorded by David Lewis (*We, the Navigators*) and
analyzed by Edwin Hutchins as a working system of distributed cognition [snippet-only].
Nothing here is legend — this is the rare case where the romantic version is the
documented one. The method transfers whole: when your instrument is down or lying and
a decision still needs to know where you are, hold the position as a belief fused from
many weak, independent cues, and keep re-estimating it as cues arrive.

## When to use
- An instrument you normally steer by — a project tracker, a monitoring dashboard, a
  status report, a data feed — is down, stale, or giving a number you have concrete
  reason to distrust, and a decision needs the position anyway.
- Typical shapes, in any role: a project's true status when the tracker has not been
  updated in weeks; a matter's posture when the other side has gone quiet; when money
  in flight will actually land while the payment system is down; whether last night's
  deploy succeeded while monitoring is out.
- Early warning: you suspect something has drifted but no instrument has said so yet,
  and you want to ask "what would we expect to see if things were fine?"
- Not for: disciplining a single-quantity estimate against comparable past outcomes →
  see `decision-science-skills:reference-class-forecasting`.
- Not for: building an automated detector for unusual patterns → see
  `machine-learning-skills:anomaly-detection` (it builds the instrument; this skill
  operates without one).
- Not for: quick solo Fermi bounding of a static quantity → see
  `math-foundations-skills:number-sense-and-estimation`. The seam: that skill brackets
  a number that holds still ("roughly how many X are there?"); this skill runs a live
  position from streaming weak cues — the belief is re-estimated every time a cue lands.
- Not for: building structured futures for a decision → see the sibling
  `decision-science-skills:minority-report` (it branches what may happen next; this
  skill estimates where you are right now).

## Do it
The full cue taxonomy, weighting method, fusion protocol, worked example, and
commentary format are in `references/wayfinding-method.md`.

1. **Name the blind spot.** Write down: which instrument is down or untrusted, what it
   normally tells you, and — the part that makes this navigation rather than waiting —
   what decision needs the position before the instrument returns. No decision, no
   voyage; just wait for the fix.
2. **Inventory every weak signal available.** Work the five cue classes so none is
   forgotten: (a) the last known-good state and its age; (b) scheduled events that
   must have happened since (jobs that run on cron, meetings held, deadlines passed);
   (c) historical rhythms (what this process usually does over such an interval);
   (d) side-channel indicators (activity in adjacent systems, message volume, who has
   been asking questions); (e) absence-of-noise signals (the complaints, escalations,
   or alarms that would exist if things were bad, and don't). Weak cues are admissible
   here — that is the point. What matters is how many you have and how independent they are.
3. **Weight each cue by independence and reliability, then fuse.** Ask of each cue:
   does it share a source with another cue (two dashboards fed by one pipe are one
   cue), and how often has it been wrong before? Then state the fused position WITH a
   confidence band, never a bare point: "between X and Y, most likely Z, because..."
4. **Run the navigator's commentary.** Say out loud which cue the position leans on
   hardest and what would be true if that cue were wrong. This is what makes a failed
   estimate legible afterward — you can trace it to the cue that lied, instead of
   shrugging at "the estimate was off."
5. **Update as cues arrive.** Each new cue re-estimates the belief; a cue class dying
   (the side channel goes quiet too) narrows the inventory but does not sink the
   method — the remaining classes still hold a position. Hold the position as a
   relationship ("ahead of where the plan needs us, by about a week"), not a false
   coordinate.
6. **Define confirm/deny, then check.** Before the instruments return, write what
   reading would confirm the fused position and what would refute it. When the
   instrument comes back, actually compare — log the hit or miss and which cue earned
   or lost trust. This calibration step is what makes the next blind stretch safer.

**Division of labor.** Humans under stress fuse two or three signals, badly, and
anchor on the loudest one. The assistant's job is the full enumeration (all five cue
classes, nothing forgotten), the explicit weighting, the fusion into a banded
position, and the running commentary. The human supplies cues the assistant cannot
see, challenges the independence claims, and owns the decision taken on the position.

## Why / learn
Etak, honestly explained: a Micronesian navigator holds course by picturing a
reference island off to the side of the route, and tracking which star bearing that
island sits under as the voyage proceeds — the canoe is imagined still while the
island moves through star positions [snippet-only]. It sounds exotic; the engineering
insight is plain. Position is not stored as a coordinate the navigator could read off
an instrument — there is no instrument. It is maintained as a *relationship* between
the voyage and its references, continuously re-derived from whatever cues the
environment offers: star bearings, the feel of swell trains through the hull, birds
that sleep ashore, cloud stacks over unseen land. No single cue is trusted, and that
is the design, not a weakness. Overcast kills the stars; the swells remain. A cue
class dying degrades the fix gracefully instead of sinking it — compare the
instrument-shaped alternative, where one dashboard IS the position and its outage is
total blindness.

The independence weighting is the load-bearing step, and the one intuition skips.
Confidence should grow with *independent* agreement: five cues that all descend from
the same source are one cue wearing five costumes, and counting them separately
manufactures false certainty. This is also why absence-of-noise is a legitimate cue
rather than wishful thinking — silence is evidence exactly when trouble would have
been loud, and worthless when nobody would have spoken anyway. Stating which cue the
position leans on hardest (Hutchins' navigators talked their reckoning aloud; the crew
could hear the reasoning, not just the heading [snippet-only]) buys the same thing in
any domain: when the position turns out wrong, the failure is legible — *that* cue
lied — and the cue's weight is corrected for next time, instead of the whole method
being abandoned.

The confirm/deny step closes the loop. A fused position that is never checked against
the returned instrument teaches you nothing about your own cue weights, and untested
navigators drift toward overconfidence. Checking is cheap — the instrument comes back
anyway — and it converts each outage from a scramble into a calibration run.

## Common mistakes
- Waiting for the instrument when the decision cannot wait → the decision gets made
  blind by default; name the blind spot and navigate it instead.
- Anchoring on the single loudest cue → that is one costume short of instrument
  worship; the method is fusion, and step 3 exists to dilute any one cue.
- Counting correlated cues as independent confirmation → two reports fed by the same
  upstream source are one cue; trace each cue to its source before weighting.
- Stating a point instead of a band → false precision invites decisions the evidence
  cannot carry; the band is the honest deliverable.
- Skipping the navigator's commentary → when the position fails, nobody can tell which
  cue lied, so nothing is learned and the method takes the blame.
- Treating absence-of-noise as comfort everywhere → silence is evidence only where
  trouble would have been loud; ask who would have spoken, and check they could.
- Never checking against the returned instrument → uncalibrated navigators grow
  overconfident; compare, log, and re-weight the cues.
- Rebuilding this as a permanent detector → if the blind spot recurs on schedule, the
  fix is an instrument, and building one belongs to
  `machine-learning-skills:anomaly-detection`.

## Tailor to your environment
This skill ships domain-neutral on purpose — wire in your current role in
`references/your-environment.md`: the instruments you actually steer by, the decision
each one feeds, the weak cues available when each goes dark, known correlations among
your cues (which ones share a source), and where you log calibration checks. Keep the
committed file structural — system names and cue types, no live figures. Anything
sensitive (real balances, client or matter names, incident details) goes in
`your-environment.private.md`, which is git-ignored and never committed.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/weak-signal-navigation.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/wayfinding-method.md — the etak mental model explained honestly, the
  five-class cue inventory taxonomy, independence/reliability weighting, the fusion
  protocol with a worked example (project status with the tracker stale for two
  weeks), the navigator's-commentary format, and the calibration follow-up
- references/your-environment.md — your instruments, per-instrument cue inventories,
  known cue correlations, and calibration log (fill in)
