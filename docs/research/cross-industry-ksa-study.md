# Cross-Industry KSA Study: Old Methods × New Capability

> **Status as of 2026-08-11: superseded — the build decision was made and executed.** All of §6's
> ranked rows 1–16 shipped as skills (checklist-design, fmea, competing-hypotheses-analysis,
> reference-class-forecasting, bowtie-barrier-analysis, principled-negotiation,
> theory-of-constraints, sbar-structured-communication, pre-mortem, evolutionary-operation,
> measurement-systems-analysis, design-of-experiments, tabletop-wargaming, qfd-house-of-quality,
> after-action-review, reliability-engineering), and Wave D's reference retrofits are done — the
> human-factors instruments (Fitts, NASA-TLX) into `ui-and-ux-inspection` and Reason's error
> taxonomy into `root-cause-analysis`. The genuinely-still-unbuilt tail is rows 17–19
> (service-recovery, smed-setup-reduction, queueing-methods) plus the tier-3 long tail
> (hoshin-kanri, triz, 5s-digital, quality-circles). Many mount points named below are archived
> plugins (Oracle Fusion/OTBI, cash-management, accounting, banking, public-sector treasury,
> sponsored-projects AR), so the shipped skills were re-aimed at domain-neutral mounts. Retained as
> the research record; the analysis below reflects the library as it stood when the study ran.

**What this is:** a deep study of knowledge, skills, and abilities from industries beyond
this library's current reach — industrial engineering, high-hazard operations, intelligence
analysis, military doctrine, service industries — ranked as candidate Claude Skills.

**Why it matters:** the library's next value frontier is not more domain coverage. It is
**synergy**: proven methods whose historical adoption barrier — a facilitator, a
statistician, a red cell, a workshop nobody re-runs — is exactly what an LLM removes, mounted
onto skills the library already runs daily.

**The decision requested:** pick the skills to build from the ranked table in §6. Eight
top-tier candidates are grouped into three build waves in §7. Every row is self-contained —
any subset builds cleanly.

Study date: 2026-08. Research: five parallel lanes over industry literature (method in §2).
Provenance marking throughout: `[verified-fetch]` = full document read; `[snippet-only]` =
confirmed via search-result snippets from named canonical sources (most industry sites block
automated reads from this environment); `[repo-verified]` = grep/read against this repo.

---

## Contents

§1 Executive summary · §2 Method · §3 The KSA transfer framework · §4 Combination-pattern
taxonomy · §5 Per-lane findings · §6 Ranked candidates + top-tier dossiers · §7 Build-wave
recommendation · §8 Risk & collision register · §9 Sources appendix

---

## §1 Executive summary

The study screened ~28 methods from five research lanes against a 128-skill library. After
merging duplicates, folding weak-standalone candidates into stronger hosts, and applying two
gates (not-already-covered; collision-free triggers), **19 candidates were scored** on six
dimensions with old×new leverage, mount-point strength, and day-job value double-weighted.

**Eight reached top tier** (score ≥39/45, no dimension ≤2):

1. **checklist-design** (45) — aviation→surgery's most famous transfer; 96 library files
   *use* checklists, none *design* them
2. **fmea** (44) — the failure-anticipation grid; mounts on reconciliation break triage,
   payment-fraud controls, and the release gauntlet
3. **competing-hypotheses-analysis** (44) — Heuer's matrix; every unexplained recon break
   has 3–6 candidate causes
4. **reference-class-forecasting** (43) — the outside view; the cash-forecasting skill's
   MAPE/bias history is a ready-made reference class
5. **bowtie-barrier-analysis** (42) — safety-industry barrier logic transplanted onto BEC
   and payment-fraud controls (HAZOP guidewords included as its front end)
6. **principled-negotiation** (41) — Fisher/Ury + Voss; `bank-fee-analysis` names
   "negotiation" six times and contains zero method
7. **theory-of-constraints** (39) — five focusing steps + drum-buffer-rope; the month-end
   close has exactly one constraint task
8. **sbar-structured-communication** (39) — healthcare's handoff protocol (with aviation's
   closed-loop and PACE assertiveness); the strongest outcome evidence in the study

The central finding is a pattern, not a list: **every top-tier method died in offices for
the same reason — the mechanism was expensive and the artifact was cheap.** Organizations
copied the worksheet and skipped the workshop. An LLM inverts that economics: it supplies
the mechanism (filling the matrix, playing the red cell, drafting the bowtie, restructuring
the rambling escalation) for the cost of a conversation, while the human supplies what the
LLM cannot — ratings adjudication, ownership, and the authority to act. §4 names seven
combination patterns that exploit this, plus the counter-pattern that predicts failure.

---

## §2 Method

**Five parallel research lanes**, each returning a fixed candidate schema (method, origin,
≤5-line procedure, efficacy evidence, library pairings, the adoption barrier the LLM
removes, trigger sketch):

- **Lane A** — industrial engineering & TPS descendants (Goldratt, Shingo, Altshuller,
  ASQ/NIST canon)
- **Lane B** — safety, reliability & high-hazard operations (FAA/NTSB, CCPS, IHI, AIAG-VDA)
- **Lane C** — decision science & intelligence/military analysis (Heuer, Klein, Flyvbjerg,
  Army doctrine)
- **Lane D** — service industries, negotiation & human factors (Fisher/Ury, Voss,
  Parasuraman, Kaiser/I-PASS, Reason)
- **Lane E** — cross-domain transfer synthesis: documented old→new industry transplants and
  the emerging evidence on LLM augmentation of classic methods, including failure modes

**Grounding against this library:** a coverage-map pass first established what is already
covered (frozen as a do-not-propose gate: SPC/control charts, VSM, RCA, kaizen/co-design,
standard work, A3, DMAIC, TPS mechanics, red-teaming/intervention logs, adversarial testing,
Adams writing) and what is genuinely absent (~24 methods with zero occurrences,
grep-verified twice — at reconnaissance and again at scoring). **Every top-tier mount-point
claim was then verified by opening the named file** — e.g., the close checklist exists at
`plugins/accounting-skills/skills/month-end-close/references/close-checklist.md`; the
forecast bias definition at `cash-forecasting/references/forecast-model-and-accuracy.md`
line 47; the unformatted handoff deliverable at `dmaic-problem-solving/references/
phase-toolkit.md` line 51. Unanchorable pairings were downgraded.

**Scoring:** two pass/fail gates (coverage; collision-free triggers), then six dimensions
scored 0–5: gap-genuineness ×1, mount-point strength ×2, old×new creative leverage ×2,
day-job value ×2, teachability ×1, evidence base ×1 (max 45). Top tier ≥39 with no
dimension ≤2.

---

## §3 The KSA transfer framework: why old methods, and why now

**Methods transfer between industries when the mechanism travels, not the artifact.** The
canonical cases, with measured results:

- **Aviation checklists → surgery.** The WHO Surgical Safety Checklist cut in-hospital
  mortality 1.5%→0.8% and complications 11.0%→7.0% across eight global sites (Haynes,
  NEJM) `[snippet-only]`. The decisive control: Ontario *mandated* the same checklist
  across 101 hospitals and measured **no significant change** (Urbach, NEJM)
  `[snippet-only]` — compliance was reported, the team ritual was not enacted. The card is
  not the method; the enacted pause is.
- **Crew resource management → operating rooms.** VA team training across 74 facilities:
  18% annual surgical mortality decline vs 7% in untrained sites, with dose-response
  (Neily, JAMA) `[snippet-only]`. What transferred was legitimized dissent — scripts and
  briefing structure, not cockpit hardware.
- **TPS → healthcare.** Virginia Mason (liability claims −74% over a decade) and ThedaCare
  (cost per patient −15–20%) `[snippet-only]` — the flow/waste lens plus worker-initiated
  stop-and-fix, with "product" redefined as the patient journey.
- **Bowtie → finance/cyber.** Shell's post-Piper-Alpha barrier standard now underpins
  financial-services operational-risk and cyber programs `[snippet-only]` — adoption
  evidence is strong, controlled outcome measurement thin; scored accordingly.
- **Army AAR → corporate.** Shell, BP, GE adopted the four-question rank-free debrief;
  practitioner-attributed savings, no controlled trials `[snippet-only]`.

**Why an LLM skill changes the economics.** Each method's historical failure mode is a
labor or expertise cost at the mechanism layer:

| Method | What killed adoption | What the LLM supplies |
|---|---|---|
| FMEA | Multi-day cross-functional worksheet grind | Pre-drafted failure inventory; humans adjudicate ratings |
| Competing hypotheses | Matrix-cell tedium | Instant evidence×hypothesis fill + sensitivity replay |
| DOE | Needed a statistician for design + ANOVA | Conversational design, aliasing explained, self-run on prompts/configs |
| Bowtie/HAZOP | Facilitator + team for days per hazard | Draft bowtie from a process description in minutes |
| Wargaming | Staffing a red cell | LLM plays red cell and white cell (with discipline — §4 P8) |
| Checklist design | Boorman-level expertise in killer-item selection | 40-step SOP → 7 killer items with rationale per cut |
| QFD | Weeks of matrix workshops | House drafted from interview notes |
| Negotiation prep | Prep documents nobody writes | BATNA trees, accusation audits, rehearsal roleplay |

The division of labor is constant across all eight: **the LLM generates and structures; the
human adjudicates, owns, and acts.** The evidence on LLM augmentation (Lane E) supports
generation quality — LLM-assisted FMEA studies report broader failure-mode discovery,
including novel modes expert teams missed `[snippet-only]` — and warns precisely where the
human gate must sit (§4 P8).

**Fit with the house skill format.** All eight top-tier methods are procedure-shaped
(numbered steps, fixed artifacts, clear stop conditions) — the do+teach format's sweet
spot. Each also carries a genuine "teach": the reasoning that keeps the method honest
(diagnosticity, tampering, barrier independence, killer-item logic).

---

## §4 Combination-pattern taxonomy

Seven patterns describe how an incoming method combines with skills the library already
runs — plus the counter-pattern that predicts failure. These are the study's reusable
vocabulary; the ranked table tags every candidate with its dominant pattern.

**P1 — Instrument-a-loop.** The old method supplies the measurement or feedback instrument
for a loop an existing skill already runs. *DOE* instruments the Improve phase that
`dmaic-problem-solving` runs qualitatively and the prompt-variant testing that
`prompt-engineering` runs one-factor-at-a-time; *reference-class forecasting* instruments
the MAPE/bias review that `cash-forecasting` already schedules. The LLM amplifies P1 by
computing what the loop's owner never had time to compute.

**P2 — Formalize-an-improvisation.** The library already does the thing informally; the
method names it, proceduralizes it, and makes it repeatable. *Checklist-design* over the 96
files that ship checklists nobody engineered; *pre-mortem* over the ad-hoc risk sections in
every charter; *AAR* over unstructured "how did the close go" conversations. P2 candidates
have the shortest distance to value — the habit exists, only the discipline is missing.

**P3 — Barrier-analysis-transfer.** Safety-industry failure logic transplanted onto
financial controls. `cash-management-controls` already lists SOD, dual approval, positive
pay, and BEC callbacks — as a flat list. *Bowtie* rebuilds them as owned, tested barriers on
threat lines to a named top event ("fraudulent payment instruction accepted as genuine");
*HAZOP guidewords* (NO approval, MORE — duplicate file, PART OF — truncated addenda, OTHER
THAN — wrong beneficiary) generate the threat lines from the process description. This is
the study's centerpiece transfer: treasury fraud controls are barriers that have never been
drawn as barriers.

**P4 — Template-injection.** A fixed communication protocol injected into output moments
existing skills already produce. *SBAR* into `dmaic-problem-solving`'s Control-phase
"formal handoff to the process owner" (a named deliverable with no format), into treasury
escalations, into the dental app's front-desk→clinical transitions. Highest evidence
density in the study: I-PASS cut medical errors 23% with no workflow cost (NEJM)
`[snippet-only]`.

**P5 — Lens-swap on an existing map.** A new analytical lens re-aims an artifact the
library already produces. *Theory of Constraints* re-reads `value-stream-mapping`'s
current-state map ("where's the constraint?") and the `month-end-close` calendar
(subordinate everything to the one task that sets close duration); *SMED* re-reads any
runbook as internal-vs-external setup.

**P6 — Adversary/alternative-injection.** A structured opponent or rival explanation added
to analysis the library already performs. *Competing-hypotheses analysis* generalizes
`medical-research-detective`'s disconfirmation pass to reconciliation breaks and prompt
audits; *wargaming* gives `project-command-center`'s red-team doctrine a multi-party
procedure with injects and adjudication.

**P7 — Math-backfill.** A quantitative engine installed under existing qualitative
guidance. *Weibull/MTBF* under `stability-and-redundancy.md`'s "untested failover is
scenery" (parallel-reliability credit requires demonstrated independent switchover — now a
theorem); *queueing* under close-workload and appointment-scheduling intuitions;
*measurement-systems analysis* under every metric the library trusts, including LLM-as-judge
agreement in the repo's own eval system.

**P8 — Counter-pattern: artifact-without-mechanism.** Copying the visible artifact while
dropping the authority/feedback mechanism reliably nulls the result — Ontario's checklists,
the 1980s U.S. quality-circle wave. Applied to LLM-era skills, the mechanism risks are
documented: rating inconsistency (LLM S/O/D scores must not be trusted raw), sycophancy
(challenger roles need explicit anti-agreement design), escalation instability (an LLM red
cell is a scenario generator, never a decision-maker), and hallucinated risk entries
(human review gates before anything enters a register) `[snippet-only]`. **Every skill
built from this study must encode its human gate in the Do-it steps, not the fine print.**

---

## §5 Per-lane findings

### Lane A — Industrial engineering (11 researched, 8 survived)
FMEA leads: its mount points (recon break triage, auto-recon rule design, the release
gauntlet) are load-bearing daily skills, and the 2019 AIAG-VDA shift from RPN multiplication
to an Action Priority table — adopted because Severity-9 failures could score "low" on
arithmetic quirks — is itself a transferable lesson in metric gaming. Theory of Constraints
carries the lane's best evidence (an 80+ application meta-analysis: ~70% mean lead-time
reduction `[snippet-only]`). The surprise: **Gage R&R's attribute-agreement variant maps
one-to-one onto LLM-as-judge validation** — an 80-year-old AIAG procedure is arguably the
missing rigor in the repo's own skill-eval system. Cut: work measurement/PMTS (Taylorist
baggage, treacherous for knowledge work; its useful residue lives inside TOC and SMED).
Trigger landmines found: "pooling" (cash pooling), bare "setup" (Oracle configuration).

### Lane B — Safety & reliability (6 researched, all survived; 2 merged)
The lane's spine is one transfer: high-hazard industries manage risk as explicit, owned,
tested barriers — and treasury fraud controls are exactly such barriers, currently stored
as flat lists. Bowtie (fed by HAZOP deviations as its front end — merged into one skill)
turns them into an auditable defense architecture. Checklist-design is the library's
biggest internal mount (96 artifact files). CRM's graded-assertiveness ladder (PACE)
merged into the SBAR skill as the escalation rung — and can never claim its acronym
("CRM" = customer relationship management in the dental-app context). Reliability math
rounds out the set: β from a Weibull fit decides burn-in vs run-to-failure vs scheduled
replacement, and availability arithmetic turns SLO targets into downtime budgets.

### Lane C — Decision science & intelligence (6 researched + 2 fold-ins)
Competing-hypotheses analysis is the lane's strongest pick — and carries a hard naming
constraint: the three-letter abbreviation is banned repo-wide (Automated Clearing House owns
it across banking skills). The lane's sharpest insight: **reference-class forecasting is not
a new practice for this user — the cash-forecasting skill's MAPE/bias history is a
ready-made reference class**, so the skill closes a loop already running. Pre-mortem
(prospective hindsight improves failure identification ~30% `[snippet-only]`) and AAR (the
Army's four questions; the TEAM counterpart to the existing self-facing reflective-learner)
fill the before/after of project-command-center's during. Commander's intent folds into the
wargaming skill as a reference (thin standalone trigger surface). Tetlock's forecasting
practices and Klein's decision journal fold into reference-class-forecasting.

### Lane D — Service, negotiation & human factors (4 researched, 3 survived + 1 fold-in)
Negotiation is a verified method-shaped hole: `bank-fee-analysis` says "negotiation" six
times and contains zero method — it builds the case; the new skill runs the ask. The
Fisher/Ury strategy layer and Voss tactics layer ship as one skill. SBAR/I-PASS carries the
study's single strongest evidence (NEJM: −23% medical errors, −30% preventable adverse
events, no workflow cost) but the study's worst collision surface ("handoff" appears in 17
files as an ordinary step word) — its description binds on structured/escalation
vocabulary. Service recovery (HEARD/LAST + the SERVQUAL gap lens) is dental-first and
already circulates in dental office-manager training. Human-factors measurement
(Fitts/NASA-TLX/error taxonomy) has strong mounts but weak standalone triggering —
recommended as reference retrofits into `ui-and-ux-inspection` and `root-cause-analysis`
rather than a skill.

### Lane E — Transfer synthesis (thesis evidence + 4 missed candidates)
Delivered §3's transfer cases, §4's counter-pattern P8 with its LLM-failure evidence, and
four candidates the specialist lanes missed. Two scored well: **EVOP** (Box's evolutionary
operation — continuous small experiments on live processes within safe bounds; a
near-perfect fit for recon-tolerance and forecast-parameter tuning, whose only historical
barrier was a resident statistician) and **hoshin kanri** (the strategic layer above
project-command-center; catchball is expensive facilitation the LLM can simulate). Quality
circles scored low (the documented Western failure mode is management non-response — a
mechanism no LLM supplies). Deming's funnel rules fold into reference-class-forecasting as
the tampering guard: re-tuning the forecast after every single-period miss is Rule 2, and
it doubles variance.

---

## §6 Ranked candidates

Gates applied: G1 coverage (all rows carry explicit boundaries against adjacent existing
skills), G2 triggers (all lead triggers grep-verified zero-collision; constrained tokens
noted). Scores: six dimensions, max 45. **Bold** = top tier (≥39, no dimension ≤2).

| # | Candidate skill | Origin | Pattern | Primary mounts (verified) | Proposed home | Score |
|---|---|---|---|---|---|---|
| 1 | **checklist-design** | Aviation 1935 → surgery 2009 | P2 | month-end-close, 96 checklist artifacts, dental workflows, wire release | safety-and-reliability-skills (new) | 45 |
| 2 | **fmea** | US military 1949 → NASA → AIAG-VDA | P3 | bank-reconciliation triage, fusion-auto-reconciliation-design, LSS gauntlet, cash controls | continuous-improvement-skills | 44 |
| 3 | **competing-hypotheses-analysis** | CIA (Heuer) 1970s–80s | P6 | recon break diagnosis, fusion-cm-production-troubleshooting, master-prompt-architect audits, RCA complement | decision-science-skills (new) | 44 |
| 4 | **reference-class-forecasting** | Kahneman/Tversky → Flyvbjerg | P1 | cash-forecasting MAPE/bias loop, project estimation | decision-science-skills (new) | 43 |
| 5 | **bowtie-barrier-analysis** (incl. HAZOP guidewords) | ICI 1970s → Shell post-Piper-Alpha | P3 | cash-management-controls, kyc-aml-basics, audit findings, BAI2 feed pipeline | safety-and-reliability-skills (new) | 42 |
| 6 | **principled-negotiation** (Fisher/Ury + Voss) | Harvard 1981 / FBI 2016 | P1 | bank-fee-analysis (×6 mentions, zero method), merchant-services-and-pci, dental insurance carriers | decision-science-skills (new) | 41 |
| 7 | **theory-of-constraints** | Goldratt 1984 | P5 | value-stream-mapping future state, month-end-close calendar, AR pipeline | continuous-improvement-skills | 39 |
| 8 | **sbar-structured-communication** (incl. PACE, closed-loop) | Kaiser 2002 / aviation | P4 | dmaic Control handoff, treasury escalation, dental team, coverage handoffs | safety-and-reliability-skills (new) | 39 |
| 9 | pre-mortem | Klein 2007 | P2 | project-command-center, go-lives, FBDI runs | decision-science-skills (new) | 38 |
| 10 | evolutionary-operation | Box 1957 | P1 | recon-tolerance tuning, forecast parameters, dunning cadence | continuous-improvement-skills | 38 |
| 11 | measurement-systems-analysis (Gage R&R + Cp/Cpk) | AIAG / Juran-Kane | P7 | recon match-rate trust, LLM-as-judge eval rigor | continuous-improvement-skills | 38 |
| 12 | design-of-experiments | Fisher 1920s → Box → Taguchi | P1 | dmaic Improve, prompt-engineering evals, recon rule factors | continuous-improvement-skills | 37 |
| 13 | tabletop-wargaming (incl. commander's intent) | Kriegsspiel → MDMP → CISA | P6 | project-command-center, BEC/outage drills; seam vs validation-design | decision-science-skills (new) | 36 |
| 14 | qfd-house-of-quality | Akao/Mizuno 1960s–72 | P1 | kaizen-codesign VOC → LSS CTQs bridge, dental feature priority | continuous-improvement-skills | 36 |
| 15 | after-action-review | US Army TC 25-20 | P2 | project-command-center milestones, close review, MEMORY loop; TEAM counterpart to reflective-learner | decision-science-skills (new) | 35 |
| 16 | reliability-engineering | Weibull 1951 → Abernethy | P7 | stability-and-redundancy SLO math, Oracle interface MTBF | safety-and-reliability-skills (new) | 33 |
| 17 | service-recovery | Parasuraman 1985–88 / Disney | P4 | dental complaints + GRO vocabulary, bank-relationship scoring | writing-skills or future dental plugin (user call) | 33 |
| 18 | smed-setup-reduction | Shingo 1950s–69 | P5 | deploy windows, close-as-changeover, context switching | continuous-improvement-skills | 33 |
| 19 | queueing-methods | Erlang 1909 → Kingman | P7 | close workload, dental scheduling (M/M/c), AP queues | continuous-improvement-skills | 33 |

**Long tail (tier 3, not recommended this cycle):** hoshin-kanri (32 — real method, thin
personal-scale value; revisit if strategy-cascade need emerges), triz (30 — highest
abstraction, weakest evidence sourcing), 5s-digital (29), quality-circles (26 — the missing
mechanism is management response, which no LLM supplies).

**Fold-ins (no new skills):** human-factors instruments (Fitts/NASA-TLX) → reference
retrofit into `ui-and-ux-inspection`; Reason's error taxonomy → reference retrofit into
`root-cause-analysis`; HAZOP → inside bowtie; PACE/closed-loop → inside SBAR; commander's
intent → inside wargaming; Tetlock practices + decision journal + Deming funnel rules →
inside reference-class-forecasting. **Cut:** work measurement/PMTS.

### Top-tier dossiers

**1. checklist-design (45) — safety-and-reliability-skills.** Select killer items only
(steps that cause serious harm if missed AND are actually skipped); choose read-do vs
do-confirm; fix a natural pause point; 5–9 items, one page; field-test and revise. Verified
mounts: `month-end-close/references/close-checklist.md` (redesign against killer-item
standards); 96 files shipping checklist artifacts; dental sterilization/handoff (literal
WHO-checklist territory); wire release as a do-confirm card. Evidence: WHO checklist NEJM
mortality data + the Ontario null result as the built-in teach ("the ritual, not the
card"). Triggers: design a checklist, read-do, do-confirm, killer items, pause point, "our
checklist isn't working." Constraint: bare "checklist" never triggers (96-file collision) —
design/diagnosis intent required.

**2. fmea (44) — continuous-improvement-skills.** Decompose the process; enumerate failure
modes per step; rate Severity/Occurrence/Detection 1–10; prioritize by Action Priority
table (not raw RPN — the multiplication flaw is part of the teach); act; re-rate. Verified
mounts: `bank-reconciliation/references/matching-and-tolerance.md` (break types as failure
modes ordering investigation); `fusion-auto-reconciliation-design` (Detection maps onto
"will this surface in the unreconciled report or silently mis-match?");
`dmaic-problem-solving/references/phase-toolkit.md:46` (named, undefined); the LSS
adversarial gauntlet. Human gate: LLM drafts the inventory, humans adjudicate every rating
(P8). Boundary: "Not for: one-off cause hunts → root-cause-analysis."

**3. competing-hypotheses-analysis (44) — decision-science-skills.** Brainstorm the full
hypothesis set; list evidence; mark each cell consistent/inconsistent; judge by
disconfirmation — the winner has the least evidence against it; drop non-diagnostic
evidence; sensitivity-check the load-bearing items; report all hypotheses' likelihoods;
name what would change the answer. Verified mounts: every unexplained recon break (timing,
duplicate, rule gap, bank error, keying error — a natural hypothesis set);
`medical-research-detective`'s disconfirmation pass (medical frame → general);
`master-prompt-architect` audits; complements 5-whys (which assumes one causal chain).
Naming: never the three-letter abbreviation — banking owns it.

**4. reference-class-forecasting (43) — decision-science-skills.** Identify the reference
class of comparable past cases; get its outcome distribution; anchor on the base rate;
adjust inside-view only with explicit justification (or apply a required uplift at chosen
certainty). Verified mount: `cash-forecasting/references/forecast-model-and-accuracy.md`
line 47 defines signed bias — the skill turns that history into next-cycle uplifts per
driver. References carry Tetlock's practices, the decision journal, and Deming's funnel
rules (the tampering guard: re-tuning after every single-period miss is Rule 2 and doubles
variance). Triggers avoid bare "forecast" (owned by two existing skills).

**5. bowtie-barrier-analysis (42) — safety-and-reliability-skills.** Name the hazard and
top event; draw threat lines (HAZOP guidewords generate them: NO approval, MORE — duplicate
file, PART OF — truncated addenda, OTHER THAN — wrong beneficiary); place preventive
barriers per line and mitigative barriers per consequence; add escalation factors; assign
every barrier an owner and an assurance test. Verified mounts:
`cash-management-controls/references/sod-and-control-catalog.md` (the flat list becomes a
defense architecture for top event "unauthorized payment released"); `kyc-aml-basics`;
audit-findings classification (finding = missing/failed barrier). The teach: a barrier
nobody tests is scenery — same doctrine as the library's failover rule.

**6. principled-negotiation (41) — decision-science-skills.** Prep: interests behind
positions, BATNA (yours and theirs), objective criteria; draft the accusation audit;
converse: mirror, label, calibrated how/what questions; invent options before dividing
value; close against BATNA, never split the difference below it. Verified mount:
`bank-fee-analysis` (six "negotiation" mentions, zero method — it builds the case, this
runs the ask; its benchmark tables feed the objective-criteria step); merchant/PCI
processor pricing; dental insurance-carrier fee schedules. LLM leverage: the prep documents
nobody writes, plus counterpart roleplay.

**7. theory-of-constraints (39) — continuous-improvement-skills.** Identify the
constraint; exploit it; subordinate everything else to its pace; elevate only if still
binding; repeat, fighting inertia. Drum-buffer-rope for scheduling. Verified mounts:
`value-stream-mapping` (finds the bottleneck; TOC says what to do with it — its
your-environment.md already prompts for waits); `month-end-close` (the calendar has one
constraint task; subordinate everything to it). Evidence: the 80+ application meta-analysis
`[snippet-only]`. Trigger constraint: bare "constraint" collides with database skills —
"bottleneck," "focusing steps," "drum-buffer-rope" lead.

**8. sbar-structured-communication (39) — safety-and-reliability-skills.** SBAR for
escalations (Situation, Background, Assessment, Recommendation); I-PASS for handoffs
(severity, summary, actions, contingencies, receiver synthesis/read-back); closed-loop for
instructions; PACE for graded assertiveness (Probe → Alert → Challenge → Emergency — the
junior analyst challenging a suspicious approved wire is the human barrier on the BEC
bowtie). Verified mount: `dmaic-problem-solving/references/phase-toolkit.md:51` — "owner
handoff" is a named deliverable with no format. Strongest evidence in study (I-PASS NEJM).
Trigger discipline: binds on SBAR/escalation/structured-handoff vocabulary — bare "handoff"
appears in 17 files.

---

## §7 Build-wave recommendation

Grouped so any subset builds cleanly; each wave is one PR-sized unit with one version bump.

**Wave A — continuous-improvement-skills 0.4.0 → 0.5.0 (6 skills, existing plugin).**
`fmea`, `theory-of-constraints`, `design-of-experiments`, `evolutionary-operation`,
`measurement-systems-analysis`, `qfd-house-of-quality`. Rationale: all sit inside the
plugin's Lean/Six Sigma charter; several are already name-checked by its skills; takes the
plugin from 11 to 17 skills — within house norms (largest plugins run 13).

**Wave B — NEW plugin `safety-and-reliability-skills` (4 skills, category: operations).**
`checklist-design`, `bowtie-barrier-analysis`, `sbar-structured-communication`,
`reliability-engineering`. Rationale: barrier/failure/communication logic from high-hazard
industries has no home plugin; stuffing it into continuous-improvement would blur a crisp
Lean/TPS theme; the writing-skills precedent supports founding small themed plugins. Three
of its four skills are top-tier.

**Wave C — NEW plugin `decision-science-skills` (6 skills, category: research).**
`competing-hypotheses-analysis`, `reference-class-forecasting`, `pre-mortem`,
`after-action-review`, `tabletop-wargaming`, `principled-negotiation`. Rationale:
structured-judgment methods share tradecraft DNA (hypotheses, base rates, adversaries,
debriefs) and a common teach (protecting conclusions from the person reaching them);
three top-tier anchors.

**Wave D — reference retrofits (no new skills, two version bumps).** Fitts/NASA-TLX
instruments → `ui-and-ux-inspection` references; Reason's slips/lapses/mistakes/violations
taxonomy → `root-cause-analysis` reference (it literally is "how to go past human error").

Suggested build order: **B → C → A** (B and C are all-new capability with the highest
top-tier density; A enriches an already-strong plugin), or cherry-pick the top tier across
waves (8 skills ≈ one build session at house pace). `service-recovery` awaits a placement
decision (writing-skills vs a future dental plugin).

---

## §8 Risk & collision register

- **Naming**: the Heuer method never uses its three-letter abbreviation (Automated Clearing
  House owns it); crew-resource-management content never claims "CRM" (customer
  relationship management in the dental context); "pooling" (cash pooling), bare "setup"
  (Oracle config), bare "constraint" (database), bare "forecast" (two skills), bare
  "checklist"/"handoff"/"report"/"review" — all constrained; lead triggers chosen
  collision-free and grep-verified (bowtie, pre-mortem, BATNA, SBAR, reference class,
  focusing steps: zero occurrences).
- **Boundaries against existing skills** (each future SKILL.md carries the Not-for line):
  FMEA vs root-cause-analysis (anticipation grid vs one-off cause hunt); competing
  hypotheses vs 5-whys (rival explanations vs single chain); pre-mortem vs
  project-command-center red-teaming (team's prospective hindsight vs adversary attack);
  AAR vs reflective-learner (team/event vs self); wargaming vs validation-design
  (run/facilitate vs audit-the-design); SBAR vs adams-smart-brevity (protocol vs prose
  register); reference-class forecasting vs cash-forecasting/time-series-forecasting
  (outside-view anchor vs the forecast engines themselves).
- **P8 discipline** encoded in every build: LLM drafts, human adjudicates ratings and owns
  actions; anti-sycophancy prompts in challenger roles; LLM red cell generates scenarios,
  never decides; nothing enters a register without human review.
- **Evidence honesty**: bowtie and AAR are adoption-strong but measurement-thin; negotiation
  is practitioner canon, not trials; scored accordingly and stated in dossiers.

---

## §9 Sources appendix

All research conducted through search-result snippets with named canonical sources
(`[snippet-only]`) because the environment's egress proxy blocks most industry sites
(NEJM, CIA.gov, HBR, arXiv, NIST, IHI among those confirmed blocked); no full-document
fetches succeeded. Repo claims are `[repo-verified]` by grep/read. Key sources by lane:

- **Lane A**: Mabin & Balderstone TOC meta-analysis (IJOPM); HBR "The House of Quality"
  (Hauser/Clausing); NIST/SEMATECH e-Handbook; Kingman's formula literature; Kane (JQT) on
  Cpk; AIAG MSA manual; Shingo's SMED case (4 hours → 3 minutes).
- **Lane B**: Haynes et al. NEJM (WHO checklist); Urbach et al. NEJM (Ontario null); Neily
  et al. JAMA (VA team training); CCPS *Bow Ties in Risk Management*; Kletz *Hazop &
  Hazan*; Weibull (ASME 1951); Abernethy's *New Weibull Handbook*; AIAG-VDA FMEA handbook
  (Action Priority).
- **Lane C**: Heuer *Psychology of Intelligence Analysis* ch. 8; Flyvbjerg reference-class
  papers + UK DfT/Green Book uplift mandates; Klein HBR pre-mortem + Mitchell/Russo/
  Pennington prospective-hindsight study; Army TC 25-20; CISA Tabletop Exercise Packages;
  ADP 6-0 (commander's intent).
- **Lane D**: Fisher/Ury *Getting to Yes*; Voss *Never Split the Difference*; Starmer et
  al. NEJM (I-PASS); Kaiser SBAR provenance; Parasuraman/Zeithaml/Berry SERVQUAL; service
  recovery paradox meta-analysis ("true but overrated"); Fitts 1954 + ISO 9241-9; Hart &
  Staveland NASA-TLX; Reason *Human Error*.
- **Lane E**: Virginia Mason/ThedaCare lean-healthcare outcomes; DevOps Handbook (andon →
  CI); El Hassani et al. (LLM-assisted FMEA, *Design Science*); Rivera et al. (LLM wargame
  escalation); IUI'24 LLM devil's-advocate experiment; Antagonistic AI; Box *Evolutionary
  Operation*; Lawler & Mohrman "Quality Circles After the Fad" (HBR); Deming Institute
  funnel experiment.

Full URLs live in the lane transcripts; the companion synergy map is at
`docs/research/ksa-synergy-map.md`.
