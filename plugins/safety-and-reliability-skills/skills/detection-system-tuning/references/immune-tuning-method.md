# The immune-tuning method: axis, layers, dispositions, tolerance, memory, fuel

Method lineage: the artificial-immune-systems (AIS) engineering literature — negative
selection (Forrest, self/non-self), clonal selection, immune networks, and danger
theory/dendritic-cell algorithm (Aickelin, from Matzinger's danger model) — with documented
intrusion- and anomaly-detection deployments and surveys [snippet-only]. The alarm-fatigue
evidence and its numbers are quoted with their provenance marks; nothing here is rounded
into new claims. Source list at the end of this file.

## Contents
- [The axis, with the documented numbers](#the-axis-with-the-documented-numbers)
- [The layered architecture](#the-layered-architecture)
- [The disposition-audit protocol](#the-disposition-audit-protocol)
- [Worked example — a monitored operations inbox](#worked-example--a-monitored-operations-inbox)
- [The tolerance-list template](#the-tolerance-list-template)
- [Danger-signal gate design](#danger-signal-gate-design)
- [Memory-cell harvesting from postmortems](#memory-cell-harvesting-from-postmortems)
- [Threshold-change simulation](#threshold-change-simulation)
- [The fuel load](#the-fuel-load)
- [Sources](#sources)

## The axis, with the documented numbers

**Autoimmunity** — the system attacks self. False matches, junk exceptions, alarm floods.
Its terminal stage is operator desensitization, and that stage is documented soberly:

- The Joint Commission's Sentinel Event Alert 50 (April 2013) reported **98 alarm-related
  adverse events between January 2009 and June 2012: 80 deaths, 13 permanent losses of
  function** — in hospitals full of working alarms. The same alert reports that **85–99% of
  alarm signals require no clinical intervention** [snippet-only]. The alarms did not fail
  to sound; they sounded so often that trained professionals, rationally, stopped treating
  each one as information. Eighty deaths is why default thresholds are worth an audit.
- Enterprise security operations centers show the same physiology: reported false-positive
  rates **above 50–80%**; **67% of analysts unable to clear their daily alert volume**;
  **63–76% reporting burnout**; roughly **3 hours per day** of manual alert triage
  [snippet-only].
- Financial-crime screening runs the same numbers at industry scale: a PwC-attributed
  benchmark holds that **90–95% of AML transaction-monitoring alerts are false positives**,
  at a manual cost of **$25–50 per alert** [snippet-only]. (Quoted as industry-attributed;
  treat it as an order-of-magnitude anchor, not a measurement of your queue.)

**Immunodeficiency** — the system misses real threats. It gets the headlines, so teams
over-correct toward it, widening rules and lowering thresholds — which feeds autoimmunity,
which desensitizes operators, which produces the very misses the widening was meant to
prevent. A flooded queue is functionally immunodeficient with perfect audit paperwork.

The AIS literature formalizes the trade rather than moralizing it: pure negative selection
("flag whatever isn't self") suffers documented false-positive and detector-scaling
problems (Stibor et al., GECCO 2005) [snippet-only]; danger theory was proposed
specifically to cut false positives by requiring context — damage signals — and not mere
non-self [snippet-only]. Tuning is choosing a position on the axis deliberately, per rule,
with the queue's own disposition history as the evidence.

## The layered architecture

The immune system spends nothing expensive on first contact. Copy the structure:

| Layer | Biological analog | Operational form | Cost per event |
|---|---|---|---|
| 0. Barrier | Skin | Input validation, dedupe, scoping rules that stop junk entering at all | ~zero |
| 1. Innate screen | Innate immunity | Cheap always-on rules; auto-disposition of known patterns; digests | seconds, no human |
| 2. Adaptive investigation | Adaptive immunity | Queue items a named human dispositions; deep checks | minutes–hours, human |
| 3. Page | Inflammation | Interrupt a human now | the most expensive move the system has |

Two routing principles:
1. **Cost scales with evidence.** An event earns its way up the layers by accumulating
   evidence; nothing starts at layer 3.
2. **Each rule is assigned a layer explicitly.** Most floods are rules delivering
   layer-1-quality signal at layer-2 or layer-3 cost. Demoting a rule one layer is often
   the entire fix.

## The disposition-audit protocol

The disposition history is the queue's immune record: what fired, and what a human actually
did about it. The audit turns it into per-rule autoimmunity rates.

1. **Choose the period.** Long enough for each significant rule to fire meaningfully
   (typically a month or a quarter); recent enough to reflect current traffic.
2. **Pull every firing with its disposition.** Normalize dispositions into a small closed
   set, e.g.: `acted` (something real was done), `benign-known` (recognized recurring
   non-issue), `benign-new` (investigated, nothing there), `duplicate`, `unread` (aged out
   with no human touch). `unread` is a disposition — the most alarming one.
3. **Compute per rule:** firings; autoimmunity rate = (benign-known + benign-new +
   duplicate + unread) / firings; flood contribution = that rule's non-actionable firings
   as a share of the queue's total.
4. **Rank by flood contribution** and take the top three rules as the working set.
5. **For each, ask the default question:** who set this threshold or scope, for what
   population, and would anyone set it there today? Prefer recalibrating the default over
   adding intelligence — the Boston Medical Center result (below) is the benchmark for how
   much that one move can carry.
6. **Record the audit** (date, period, rates, actions taken) so the next audit measures the
   change instead of re-arguing it.

No disposition history exists in many teams. Then the audit's step 0 is instrumentation:
one line per firing — rule, timestamp, disposition, initials. A week of honest lines beats
a year of recollection.

## Worked example — a monitored operations inbox

Domain-neutral on purpose: this is any shared inbox or monitoring queue — a firm's intake
mailbox, an analyst's exception feed, a service's alert channel. **All numbers below are
illustrative**, not research findings.

A team's queue received 1,240 firings last quarter across 11 rules. The audit finds:

| Rule | Firings | No action needed | Autoimmunity rate | Flood share |
|---|---|---|---|---|
| R4 "sender not on approved list" | 610 | 588 | 96% | 55% |
| R7 "attachment over size limit" | 240 | 231 | 96% | 22% |
| R2 "keyword: urgent/overdue" | 180 | 121 | 67% | 11% |
| R9 "no response in 48h" | 90 | 31 | 34% | 3% |
| …7 more rules | 120 | 95 | 79% | 9% |

Actions, in method order:
- **R4 — recalibrate the default.** The "approved list" was seeded once at go-live and
  never maintained; 40 recurring legitimate senders were simply never added. Fixing the
  list (the default) removes ~500 firings/quarter at the source. No new detector.
- **R7 — demote a layer.** Oversized attachments never required action within a day;
  route to a weekly digest (layer 1), out of the live queue (layer 2).
- **R2 — split the rule and gate the page.** "Urgent" as a bare keyword is anomaly, not
  danger. The rule splits: keyword alone → queue; keyword + a named deadline or a named
  consequence in the message (a danger signal) → immediate attention.
- **R9 — leave it alone.** 34% autoimmunity at low volume with real catches is a healthy
  adaptive-layer rule. Not every rule needs surgery; the audit also certifies health.

Projected queue after the changes: roughly 450 firings/quarter, with the page tier gated
on danger signals. The team then sets tolerance-list expiries for R4's newly-approved
senders and schedules the next audit — the numbers above are the baseline it will be
measured against.

## The tolerance-list template

Tolerance = the system actively learning not to attack a verified-benign pattern. Every
entry carries its evidence and its expiry; an entry missing either is fuel (see
[The fuel load](#the-fuel-load)).

```
TOLERANCE ENTRY
Pattern:        <exactly what is tolerated — rule + condition, not a vague description>
Suppressed at:  <the source change made — rule retuned/scoped, NOT notifications muted>
Evidence:       <N firings dispositioned benign over <period>, by <role>>
Approved by:    <named role — this is a risk acceptance>
Granted:        <date>
Expires:        <date — re-validation required to renew; expiry ≤ one audit cycle for
                 new entries, longer only after a clean renewal>
Renewal check:  <what re-validation looks at — has the pattern's population changed?>
```

Suppress at the source. A muted notification still burns queue attention downstream and
still trains operators that firings are ignorable; a retuned rule stops the cost where it
starts. Boston Medical Center's move was exactly this — changing default alarm *limits*,
not silencing speakers — and it cut audible alarms **89% in the pilot (12,546 → 1,424 per
day)** and 60% hospital-wide across 310 telemetry beds, **with no missed events reported**
[snippet-only].

## Danger-signal gate design

Matzinger's danger model reframed immunology: the trigger for expensive response is not
"foreign" but "damage" [snippet-only]. Operationally: anomaly says *unusual*; a danger
signal says *harm is plausibly underway*. Only the pair earns an interrupt.

Designing the gate for a given system:
1. **Enumerate the damage evidence available in context.** Examples across domains: a
   transaction that also breaches a hard limit; an anomaly plus an affected party's
   complaint; a failed check plus a production error rate moving; unusual access plus data
   actually leaving; a missed deadline plus a contractual consequence attached.
2. **Write the gate as anomaly AND danger.** The page condition is a conjunction. Anomaly
   alone routes to the queue with a deadline, not to a human's attention now.
3. **Name the fallback.** Some real threats present no early damage signal; that is the
   immunodeficiency risk of the gate. Cover it with the queue's service level (everything
   gets dispositioned within N days) rather than by weakening the gate — the gate protects
   the page tier, the service level protects coverage.
4. **Audit the gate with the same disposition data:** pages that needed no action (gate
   too loose) and incidents that sat in the queue while damage accrued (gate too tight, or
   the danger signal wasn't wired in).

## Memory-cell harvesting from postmortems

A memory cell is a permanent, cheap, specific detector minted from a true incident, so
second exposure is detected fast and precisely — the postmortem → detection-rule lifecycle
documented in SOC practice as detection-as-code [snippet-only].

Add one step to whatever postmortem or after-action form the team already uses:

```
MEMORY CELL
Incident:       <reference>
Signature:      <the cheapest observable that uniquely marks recurrence of THIS pattern>
Detector:       <the rule as implemented — source, condition, layer it routes to>
Specificity:    <why this won't flood: what nearby-benign traffic it will NOT match>
Replay check:   <run over the historical period — it must catch the incident and fire
                 (near-)zero times otherwise>
Owner + review: <role; memory cells enter the same disposition audit as every rule>
```

Two disciplines keep the memory pool healthy. **Specificity:** a memory cell is narrow by
design — generalizing it into a broad heuristic converts memory into autoimmunity; if the
incident suggests a broad detector, that is a new layer-1/2 rule proposal with its own
replay, not a memory cell. **Same audit as everything else:** memory cells rot as systems
change; the disposition audit retires the dead ones.

## Threshold-change simulation

Never change a live threshold on argument alone — replay it. Vaccination, not first
infection: the system meets the change on historical data before it meets production.

1. **Fix the replay set:** the last audit period's raw events, plus every known-true
   incident in reach (however old) as the must-catch list.
2. **Run old and new rule over the same set.** Produce the delta: firings gained, firings
   lost, and — decisive — must-catch incidents still caught.
3. **Read the delta against the axis.** Firings lost are almost all non-actionable (their
   dispositions are on record) → autoimmunity reduced at near-zero coverage cost. Any
   must-catch incident lost → the change buys quiet with immunodeficiency; redesign (often:
   pair the loosened threshold with a new memory cell for the specific incident class).
4. **Stage the rollout** where volume allows: shadow-fire the new threshold (log, don't
   notify) alongside the old for one cycle, then switch.
5. **Log the change** with its replay results, so the next audit can score the prediction
   against what actually happened.

## The fuel load

Fire ecology's suppression bias, folded in per the research verdict: suppressing all small
fires removes mild burning, accumulates fuel, and concentrates burning into extreme
conditions — the suppressed fires are not prevented, they are banked (Nature
Communications, 2024) [snippet-only].

A tuned detection system runs the same budget. Every auto-suppressed exception, every
tolerance entry, every demoted rule is fuel: risk deliberately accepted and stored rather
than burned off. That is not an argument against tolerance — an untuned queue kills
attention today — it is the reason tolerance carries evidence counts and expiry dates.
Tolerance induction **without periodic re-validation** is how small fires convert into the
big one: the pattern's population drifts, the entry stays, and years later the "known
benign" channel is exactly where the real thing walks in.

The prescribed burns, named in the method: expiry dates that force re-validation (tolerance
template), the recurring disposition audit that re-reads what suppression is hiding, and
replay logs that keep every acceptance visible instead of ambient. SRE error budgets are
the same discipline at practice level — a stated allowance of failure deliberately spent so
risk surfaces continuously instead of accumulating [snippet-only]; a tolerance list with
expiries is a detection system's error budget, written down. (For error budgets in software
delivery itself, the library's home is
`continuous-improvement-skills:lean-six-sigma-for-software`.)

## Sources

All marks [snippet-only]: claims cross-checked across independent WebSearch results; direct
fetches were egress-blocked in the research sandbox. Per the library's research dossier
(docs/research/epic-wave-held-research.md, Lane 3, entry 1):

- Joint Commission Sentinel Event Alert 50 (April 2013) — alarm-related adverse events and
  the 85–99% non-actionable figure (via KFF Health News; HCPLive) [snippet-only]
- Boston Medical Center default-recalibration results — 89% pilot reduction, 60%
  hospital-wide, 310 telemetry beds, no missed events reported (via ECRI) [snippet-only]
- SOC alert-fatigue figures — ACM Computing Surveys (2025); CyberDefenders [snippet-only]
- AML false-positive benchmark, PwC-attributed — via Facctum; Unit21 [snippet-only]
- AIS literature — AIS survey (arXiv 1006.4949); negative-selection survey (Science
  Direct); Stibor et al., GECCO 2005 (ACM) [snippet-only]
- Danger theory — Matzinger's danger model; Aickelin's dendritic-cell algorithm
  [snippet-only]
- Detection-as-code / postmortem-to-rule lifecycle — Splunk [snippet-only]
- Suppression bias — Nature Communications (2024) [snippet-only]
- Error budgets — Google SRE book, "Embracing Risk" [snippet-only]
