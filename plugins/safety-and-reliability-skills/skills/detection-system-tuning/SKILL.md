---
name: detection-system-tuning
description: >-
  Tunes detection systems — monitors, exception queues, spam filters, code-review bots,
  compliance screens — along the immune system's axis: between autoimmunity (false matches
  that desensitize operators) and immunodeficiency (missed threats). Measures each rule's
  empirical false-positive rate, recalibrates defaults before adding detectors, layers cheap
  screens ahead of costly investigation, gates human paging on danger signals, maintains
  expiring tolerance lists for verified-benign patterns, converts every true incident into a
  permanent detector, simulates threshold changes against historical firings before going
  live. Use when queues drown operators, real signals get buried, or systems need tuning.
  Triggers: alarm fatigue, detection tuning, autoimmunity, immune system, too many false
  matches, exception queue drowning, tune the alerts, memory cell, everything is an
  exception, nobody looks at the alerts anymore.
metadata:
  version: "1.4.1"
  source: >-
    Built from the library's biological-systems research dossier
    (docs/research/epic-wave-held-research.md, Lane 3 top pick). The mechanism is the
    documented artificial-immune-systems engineering literature (negative selection, clonal
    selection, danger theory) plus quantified alarm-fatigue evidence; all external claims
    carry their provenance marks ([snippet-only] = cross-checked search snippets). The
    fire-ecology fuel-load section is folded in per the same dossier's verdict.
---

# Detection-system tuning (between autoimmunity and immunodeficiency)

Every detection system — an uptime monitor, an exception queue, a spam filter, a code-review
bot, a compliance screen, an intake inbox with routing rules — lives on one axis. At one end,
**autoimmunity**: the system attacks self — false matches, junk exceptions, alarm floods — and
the flood desensitizes the operators. At the other, **immunodeficiency**: the system misses
real threats. The desensitized operator, not the missed detector, is the documented killer:
the Joint Commission's Sentinel Event Alert 50 (April 2013) counted **98 alarm-related adverse
events from January 2009 to June 2012, 80 of them deaths**, against a background in which
**85–99% of alarm signals required no clinical intervention** [snippet-only]. This is not
metaphor borrowed from biology: artificial immune systems (AIS) is an established engineering
literature — negative selection (Forrest's self/non-self work, 1990s), clonal selection,
immune networks, and danger theory — with documented intrusion- and anomaly-detection
deployments, and it documents exactly this failure trade [snippet-only].

## When to use
- A queue, channel, or screen is drowning its operators: everything fires, so nothing gets
  read — an analyst's exception list, an attorney's conflict-check hits, an operations
  manager's monitoring channel, a developer's CI failure feed.
- A real incident slipped through a system that "should have caught it" — and it did catch
  it, buried in a flood nobody reads anymore.
- Before adding a new rule or detector to an already-noisy system, or before changing any
  threshold that is live.
- On a schedule: the periodic disposition audit that keeps the tuned system tuned.
- Not for: building the detectors or models themselves → `machine-learning-skills:anomaly-detection`
  owns detector construction, threshold statistics, and the "alert fatigue" concern for a
  single detector's output stream. The seam: that skill builds and tunes one detector; this
  skill operates the whole layered system around detectors from any source — queue economics,
  disposition audits, tolerance induction, memory formation.
- Not for: watching a process metric for stability → SPC/control charts live in
  `continuous-improvement-skills:dmaic-problem-solving` (Control phase) and
  the archived `continuous-improvement-skills:lean-six-sigma-for-software`; whether a measurement can be
  trusted at all → `continuous-improvement-skills:measurement-systems-analysis`.
- Not for: diagnosing why one alarm fired or why one incident happened →
  `continuous-improvement-skills:root-cause-analysis`.
- Not for: what happens after a legitimate page lands — sealed emergency response and
  pre-granted authority → `safety-and-reliability-skills:break-glass-playbooks`; paging,
  rollback, and observability plumbing → `full-stack-dev-skills:deploy-and-operate`.

## Do it
The disposition-audit protocol, worked example, templates, and the evidence retold in full
are in `references/immune-tuning-method.md`.

1. **Measure the empirical autoimmunity rate per rule — as a band, not a number.** Pull a
   period of firings (a month, a quarter) with their dispositions — what a human actually did
   with each. Per rule, the **floor** is firings *confirmed* to need no action, over firings;
   the **ceiling** adds the firings that aged out unread. Report both, because **`unread` is
   unknown, not benign**: counting it as a false alarm asserts the alert was harmless on the
   evidence that nobody looked, and that error is biggest in the most flooded queue — the one
   whose alerts age out. Since a high rate is this skill's argument for widening a threshold,
   a point estimate hands the worst-drowned queue the strongest case for switching detection
   off. **A rule may only be loosened or retired on floor evidence.** A wide band is itself
   the finding: sample 30–50 unread firings, adjudicate them properly, and place the true
   rate before any threshold moves. No dispositions recorded? Start recording them today; a
   one-line disposition per firing is the cheapest instrumentation this skill ever asks for.
2. **Rank rules by alarm-flood contribution.** Confirmed non-actionable firings × volume —
   rank on the floor, so a rule cannot climb the work list on firings nobody read. Three
   rules usually produce most of the flood; those three are the work. What a large unread
   count *does* justify right away is routing (batch, digest, demote, give it an owner):
   load comes down, coverage does not.
3. **Recalibrate defaults before adding smarts.** The highest-leverage move on record is not
   a better detector — it is fixing default thresholds that were never set for this
   population. Boston Medical Center recalibrated *default* alarm limits and cut audible
   alarms **89% in the pilot (12,546 → 1,424/day)** and 60% hospital-wide across 310
   telemetry beds, with no missed events reported [snippet-only]. Ask of every flooding
   rule: who chose this threshold, for what population, and would anyone choose it now?
4. **Layer the system like the immune system.** Cheap, broad, always-on innate screens run
   first and handle volume; costly adaptive investigation (a human, a deep check) runs only
   on what the innate layer passes through. Route each rule's output to the layer its
   precision deserves — a log line, a daily digest, a queue item, or a page are four
   different costs, not one.
5. **Install the danger-signal gate on human paging.** Pages — the interrupt-a-human tier —
   require a danger signal: evidence of damage or consequence in context, not mere anomaly.
   "Unusual" goes to the queue; "unusual AND a customer/counterpart/system is visibly
   affected" pages. This is danger theory operationalized (Matzinger's danger model; the
   dendritic-cell algorithm of Greensmith, Aickelin & Cayzer, ICARIS 2005), which exists
   specifically to cut false positives by requiring damage context rather than mere
   non-self [snippet-only].
6. **Induce tolerance at the source, with evidence and expiry.** For each verified-benign
   recurring pattern, add a tolerance-list entry carrying: the pattern, the evidence count
   (how many firings were dispositioned benign), the approver, and an **expiry date** that
   forces re-validation. Then suppress at the source — retune or scope the rule so it stops
   firing — not at the notification layer, where the firing still burns queue attention and
   still trains operators to ignore.
7. **Convert every true incident into a memory cell.** After each real catch (or real miss),
   mint a permanent, cheap, specific detector for that exact pattern, so second exposure is
   detected fast and precisely. This is documented SOC practice — the postmortem → detection
   rule lifecycle, detection-as-code [snippet-only]. A postmortem that fixes the incident but
   mints no detector leaves the system as naive as before.
8. **Simulate every threshold change against historical firings before going live.** Replay
   the proposed rule over the last period's data: what would it have fired on, what would it
   have missed, which known-true incidents would it still catch? A change that cannot be
   replayed is a guess wearing a config change.
9. **Re-audit on a schedule — and account for the fuel load.** Every auto-suppressed
   exception and every unreviewed tolerance entry is accumulated fuel: fire ecology
   documents that suppressing all small fires concentrates burning into extreme conditions
   (suppression bias) [snippet-only]. Expiring tolerance entries (step 6) and the periodic
   disposition audit (step 1, repeated) are the prescribed burns. SRE error budgets are the
   same idea at practice level — accept small failures continuously so risk surfaces instead
   of accumulating [snippet-only].

**Deliverable.** A dated tuning audit: the period, the per-rule table (firings, confirmed
non-actionable, unread, the autoimmunity band floor–ceiling,
flood contribution), the layer each rule now routes to, the tolerance entries with evidence counts
and expiry dates, the memory cells minted, the replay result behind every threshold change, and the
next audit date. It is the baseline the next audit is scored against.

**Division of labor.** The assistant reads the disposition history and computes per-rule
autoimmunity bands, drafts the tolerance list with evidence counts, converts postmortems into
memory-cell rule drafts, and runs the threshold-change replay. The human owns every
suppression decision and every expiry date — turning a detector down is a risk acceptance,
and risk is accepted by people, not by tooling.

## Why / learn
The axis is the whole model. Push any detection system toward catching everything and it
attacks self: the false-match flood rises until operators stop looking, at which point the
system has quietly crossed to the other end of the axis — functional immunodeficiency with
perfect paperwork. That is why the flood is the killer and not just a nuisance: the Joint
Commission's 80 deaths were not caused by missing alarms but by alarms so abundant
(85–99% needing no action) that the true ones died in the noise [snippet-only]. The same
economics show up wherever detection is operated: enterprise SOC studies report
false-positive rates above 50–80%, 67% of analysts unable to clear their daily alerts, and
63–76% reporting burnout, with roughly 3 hours a day spent on manual alert triage
[snippet-only]; an industry-attributed (PwC) benchmark puts **90–95% of AML
transaction-monitoring alerts as false positives** at $25–50 of manual cost per alert
[snippet-only]. Different domains, one disease.

The immune system's answer is architectural, not heroic. It does not make one perfect
detector; it layers a cheap, fast, unspecific innate response in front of an expensive,
slow, specific adaptive one, so cost scales with evidence. Negative selection alone — flag
everything that isn't self — provably floods (Stibor et al. showed the false-positive and
detector-scaling problems, GECCO 2005 [snippet-only]); danger theory was added precisely
because *anomalous* is not *harmful*, and paging a human is the adaptive system's most
expensive move, so it should require evidence of damage, not just strangeness. Tolerance is
the mirror discipline: the body actively learns not to attack self, and a queue must too —
but at the source, with evidence and expiry, because tolerance without re-validation is how
fuel accumulates. And memory cells are why second infections are mild: a true incident is
the most expensive training datum the system will ever receive, so converting it into a
permanent cheap detector is the only way the cost is ever repaid. Defaults matter most of
all because they are the thresholds nobody chose: BMC's 89% reduction came from
recalibration, not intelligence — most floods are configuration, not fate [snippet-only].

## Common mistakes
- Adding a smarter detector to a flooded queue → measure dispositions and recalibrate
  defaults first; a better detector feeding a dead queue detects nothing.
- Treating every firing as sacred ("we can't turn that off — it might matter") → with
  85–99% of firings non-actionable, the flood is what hides the ones that matter
  [snippet-only]; the risk is already being taken, just unmanaged.
- Suppressing at the notification layer while the rule keeps firing → operators still
  triage the noise and still learn to ignore; retune the rule at the source.
- Tolerance entries without evidence counts or expiry → that is fuel accumulation, not
  tuning; every entry states why it is benign and when it must re-prove it.
- Paging humans on anomaly alone → route anomaly to the queue; page only with a danger
  signal (damage or consequence in context).
- Changing a live threshold without replaying it against history → simulate first: what
  fires, what goes quiet, which known-true incidents survive the change.
- Closing postmortems without minting the memory cell → the incident's cost is paid; the
  detector it should have bought was not collected.
- Measuring detector precision but never queue economics → the operating question is
  firings per operator-day versus what operators can genuinely disposition; precision per
  rule is an input, not the answer.
- Counting `unread` firings as benign → an alert nobody opened is *unknown*, not a false
  alarm; report the rate as a floor–ceiling band and loosen only on the floor.
- Retiring a rule because most of its firings were never read → that is manufacturing a
  coverage gap and calling it tuning; sample 30–50 of the unread, adjudicate, then decide.
- Treating a wide band as a measurement nuisance → it is the headline finding: the queue
  outran its humans, which is a triage and staffing answer, not a threshold answer.
- Tuning once and declaring victory → populations drift and rules rot; the disposition
  audit is a cycle, not a project.

## Tailor to your environment
Wire in your current role here — this skill is deliberately domain-neutral, and it attaches
to whatever detection system you operate wherever you work next. In
`references/your-environment.md`, record: the systems you operate (queue, inbox, monitor,
screen), where each rule lives and who may change it, where dispositions are (or will be)
recorded, the paging path and what counts as a danger signal in your context, the tolerance
list's home and its expiry convention, and the re-audit cadence. Keep the committed file
structural. Real rule names, thresholds, incident details, and anything client- or
employer-identifying belong in `your-environment.private.md`, which is git-ignored and
never committed.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/detection-system-tuning.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/immune-tuning-method.md — the axis with the documented numbers
  (provenance-marked), the layered architecture, the disposition-audit protocol with a
  worked domain-neutral example, the tolerance-list template with expiry, danger-signal
  gate design, memory-cell harvesting from postmortems, threshold-change simulation, and
  the fuel-load section
- references/your-environment.md — your queues, rules, disposition source, paging path,
  and audit cadence (sanitized stub; live detail goes in the `.private.md` twin)
