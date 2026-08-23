# General-use expansion wave — research-verification dossiers (8 skills)

> **Status as of 2026-08-11: superseded — all 8 planned skills shipped.** causal-inference,
> ab-test-design, and survey-and-sampling-design (data-analytics-bi-skills); bayesian-updating
> (decision-science-skills); technical-documentation (writing-skills); executive-briefing and
> stakeholder-mapping (collaboration-skills); reproducible-analysis (data-tools-skills). The
> misattribution warnings verified here became load-bearing skill content, and the shipped skills
> were later line-checked by the adversarial and arithmetic review passes. Retained as the research
> record; the analysis below reflects the library as it stood when the study ran.

**Status: research complete, nothing built** *(historical — see the status block above)*. Commissioned for the general-use / career-portable
expansion wave (post "no more Oracle work" directive). Eight domain-neutral skills planned across
five existing plugins; every anchor below was verified before authoring begins, per the house
pattern (3rd+ application): **research-verify anchors first; misattribution warnings are
load-bearing teaching content.**

House research standards apply throughout: provenance marks on every external claim.
**[snippet-only]** = verified via WebSearch result blocks cross-checked across independent
results; direct fetches were egress-blocked in this sandbox (diataxis.fr, cognitect.com,
keepachangelog.com all blocked — same proxy behavior as prior waves). **[background — verify
at authoring]** = well-known claim not independently confirmed this session; do not put it in
a skill without checking. Where a fact is contested or soft, the dossier says so — those
warnings become skill content, not footnotes.

Audience constraint carried through all worked-example shapes: an analyst, attorney,
ops lead, or developer in **any** role — no treasury/Oracle mounts.

---

## Contents

1. [causal-inference](#1-causal-inference-data-analytics-bi-skills) (data-analytics-bi-skills)
2. [ab-test-design](#2-ab-test-design-data-analytics-bi-skills) (data-analytics-bi-skills)
3. [survey-and-sampling-design](#3-survey-and-sampling-design-data-analytics-bi-skills) (data-analytics-bi-skills)
4. [bayesian-updating](#4-bayesian-updating-decision-science-skills) (decision-science-skills)
5. [technical-documentation](#5-technical-documentation-writing-skills) (writing-skills)
6. [executive-briefing](#6-executive-briefing-collaboration-skills) (collaboration-skills)
7. [stakeholder-mapping](#7-stakeholder-mapping-collaboration-skills) (collaboration-skills)
8. [reproducible-analysis](#8-reproducible-analysis-data-tools-skills) (data-tools-skills)
9. [Collision scan](#9-collision-scan) (method, known-constraint verification, conflict table)
10. [Summary](#10-summary--strongest-honesty-points-and-verification-failures)

---

## 1. causal-inference (data-analytics-bi-skills)

### Verified anchors

- **Pearl's graphical framework.** "Causal diagrams for empirical research," *Biometrika*
  82(4):669–688 (1995) — causal DAGs and the do-calculus; the **back-door criterion** appears in
  Pearl's 1993 work and is restated there: an adjustment set Z is valid if (i) no node in Z is a
  descendant of treatment and (ii) Z blocks every path into treatment. Colliders and confounders
  are structural roles in the DAG, not statistical labels. Lay canon: *The Book of Why* (Pearl &
  Mackenzie, 2018). [snippet-only, incl. the Biometrika PDF listing at bayes.cs.ucla.edu]
- **Regression discontinuity.** Thistlethwaite & Campbell, "Regression-Discontinuity Analysis:
  An Alternative to the Ex Post Facto Experiment," *Journal of Educational Psychology*
  51(6):309–317 (Dec 1960) — the first RD paper: near-winners of the 1957 National Merit
  program (5,126 Certificate of Merit recipients vs 2,848 commendation-letter recipients),
  assignment by test-score threshold. Note the author's name is spelled "Thistlewaite" in some
  bibliographic records — cite carefully. [snippet-only]
- **Difference-in-differences (modern canon).** Card & Krueger, "Minimum Wages and Employment:
  A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania," *AER* 84(4) (1994):
  NJ raised its minimum wage $4.25→$5.05 on 1992-04-01; PA did not; 331 NJ + 79 eastern-PA
  fast-food restaurants surveyed Feb and Nov 1992; DiD estimate ≈ +2.75 FTE — no detectable
  employment loss. [snippet-only] Card shared the 2021 Nobel (with Angrist & Imbens taking the
  methodological half) [background — verify at authoring]. DiD itself is far older than 1994 —
  John Snow's 1855 cholera comparison is the commonly cited proto-DiD [background — verify at
  authoring]; Card & Krueger are the *lineage* anchor, not the inventors.
- **Instrumental variables.** Philip G. Wright, *The Tariff on Animal and Vegetable Oils*
  (1928), **Appendix B** — structural supply/demand equations, identification, weather as an
  instrument, even an early path/DAG-style diagram. Long-running authorship question (was it
  really his son, path-analysis inventor Sewall Wright?) settled by Stock & Trebbi,
  "Retrospectives: Who Invented Instrumental Variable Regression?," *J. Economic Perspectives*
  (2003), via stylometric analysis: **Philip wrote Appendix B** (Sewall had used IV-like
  analysis on corn/hog cycles ~1925). [snippet-only, incl. scholar.harvard.edu/stock]
- **Hill's viewpoints.** Austin Bradford Hill, "The Environment and Disease: Association or
  Causation?," *Proceedings of the Royal Society of Medicine* 58(5):295–300 (1965) — nine
  considerations: strength, consistency, specificity, temporality, biological gradient,
  plausibility, coherence, experiment, analogy. See honesty point below for what he actually
  claimed for them. [snippet-only, incl. the Sage reprint]

### Misattribution warnings / honesty points

- **Hill never said "criteria."** He called them "viewpoints" and wrote: *"None of my nine
  viewpoints can bring indisputable evidence for or against the cause-and-effect hypothesis and
  none can be required as a sine qua non"* — and explicitly disclaimed "hard-and-fast rules of
  evidence." The all-nine-boxes checklist is folklore that inverts his position. In the same
  lecture he also cautioned against over-reliance on significance tests. Teach the checklist
  *as* the misreading. [snippet-only, multiple convergent incl. Kleinberg's "use and abuse"
  paper]
- **"Correlation is not causation" has no author.** The aphorism appears in print by the
  1880s–1890s, contemporaneous with the birth of correlation itself (Galton/Pearson); logician
  Alexander Bain warned of the confusion in 1870. It is not a quotable line from Pearson or
  Fisher. Bonus irony for teaching: Pearson (1911) dismissed *causation* as "another fetish
  amidst the inscrutable arcana of even modern science" — the correlation pioneer thought
  causation was the confused idea. [snippet-only, incl. Slate's history piece]
- **Card & Krueger is canonical, not settled.** The finding was and is contested (Neumark &
  Wascher's payroll-data re-analysis and two decades of debate). The honest teaching frame: the
  *method* — credible design from a policy discontinuity — survived the fight and reshaped
  empirical economics; the specific employment estimate remains argued. [snippet-only via the
  EPI study-design piece; the broader debate is background — verify before quantifying]
- **The IV authorship story is itself a provenance lesson**: a 75-year misattribution question
  resolved by *stylometry* — evidence-based citation hygiene in action.

### Worked-example shapes (domain-neutral)

1. **"Did the policy change work?"** (analyst/ops): a fee/process change hits one unit or date
   but not another → DiD with an explicit parallel-trends check and a placebo period.
2. **"Draw the DAG before you argue"** (attorney/analyst): a causation claim (discipline
   disparities, toxic exposure, vendor blame) → map confounders vs colliders; show how
   conditioning on a collider *manufactures* correlation; walk Hill's viewpoints as argument
   structure, not checklist.
3. **"The threshold is your experiment"** (developer/ops): any score/date/size cutoff that
   assigns treatment (accounts above X got the feature; tickets after date Y got the new
   routing) → regression discontinuity at the cutoff.

### Candidate triggers (scan status)

causal inference (FREE) · correlation vs causation / "correlation is not causation" (FREE) ·
confounder / confounding (FREE) · difference-in-differences (FREE) · instrumental variable
(FREE) · regression discontinuity (FREE) · natural experiment (FREE) · does X cause Y (FREE) ·
collider bias (FREE). **Do not claim:** bare "root cause" — CONFLICT(continuous-improvement-
skills:root-cause-analysis); bare "hypothesis test" / "significance" / "A/B test" —
CONFLICT(data-analytics-bi-skills:statistical-inference). Seam notes: systems-thinking owns
causal-*loop* diagrams (feedback structure); this skill owns acyclic causal identification.

---

## 2. ab-test-design (data-analytics-bi-skills)

### Verified anchors

- **The canon.** Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments: A Practical
  Guide to A/B Testing* (Cambridge UP, 2020); predecessor survey: Kohavi et al., "Controlled
  experiments on the web: survey and practical guide," *Data Mining and Knowledge Discovery*
  18(1):140–181 (2009). [snippet-only]
- **Sample ratio mismatch (SRM).** Observed assignment split differs from designed split →
  invalidates the scorecard. Fabijan et al., "Diagnosing Sample Ratio Mismatch in Online
  Controlled Experiments: A Taxonomy and Rules of Thumb for Practitioners," KDD 2019,
  pp. 2156–2164 — taxonomy from 4 companies / 25+ products; practitioner write-ups report SRM
  in roughly 6–10% of tests (soft figure — self-reported platform experience, mark it as such).
  [snippet-only]
- **The peeking problem.** Johari, Koomen, Pekelis & Walsh, "Peeking at A/B Tests: Why It
  Matters, and What To Do About It," KDD 2017, pp. 1517–1525 — continuous monitoring of a
  fixed-horizon test inflates Type I error to ~5× nominal; their mSPRT ("always-valid
  p-values") shipped in Optimizely from Jan 2015. Popular precursor: Evan Miller, "How Not To
  Run An A/B Test" (2010). [snippet-only]
- **MDE / sizing.** Kohavi, Deng, Longbotham & Xu, "Seven Rules of Thumb for Web Site
  Experimenters," KDD 2014 — rule-of-thumb n ≈ 16σ²/δ² per arm (two-sided α=0.05, 80% power);
  Kohavi's practice guidance: relative MDEs above ~5% are wishful (Bing's average effect across
  tens of thousands of experiments was rarely above 0.3%). [snippet-only]
- **OEC + guardrails.** "Overall Evaluation Criterion" — the single (possibly composite)
  decision metric — plus guardrail metrics that must not degrade; terminology popularized by
  the Kohavi line of papers and the 2020 book. [snippet-only]
- **Twyman's law.** "Any figure that looks interesting or different is usually wrong" — named
  for UK media/market researcher Tony Twyman (1934–2014); the surviving formulation is
  **Ehrenberg's**, in *Data Reduction* (1975); Twyman apparently never published it himself.
  Kohavi et al. devote book chapter 3 to it as the trust reflex. [snippet-only]
- **A/A tests.** Run the experiment machinery against itself; a correctly operating system
  shows p<0.05 ~5% of the time — validates instrumentation and randomization (2009 survey
  paper; book). [snippet-only]
- **Novelty & primacy effects.** Treatment effects that decay (novelty) or grow (primacy) with
  exposure; when suspected, run long enough to estimate the asymptote — 2009 survey paper;
  formal estimator in Sadeghi et al., "Novelty and Primacy: A Long-Term Estimator for Online
  Experiments," *Technometrics* 64(4) (2022). [snippet-only]
- **Humbling base statistics.** Microsoft: ~⅓ of ideas positive, ⅓ flat, ⅓ negative; optimized
  domains (Bing, Google): ~10–20% success; reported failure rates range 66% (Microsoft) to 92%
  (Airbnb). The Bing long-ad-titles change: rated low, sat in the backlog 6+ months, then
  produced +12% revenue (>$100M/yr US) — the canonical "nobody can pick winners" story (Kohavi
  & Thomke, "The Surprising Power of Online Experiments," *HBR* Sept–Oct 2017). [snippet-only]

### Misattribution warnings / honesty points

- **Twyman's law is an attribution onion**: named for a man who never wrote it down, preserved
  by Ehrenberg, popularized by Kohavi. A skill about distrusting interesting numbers gets to
  open with an interesting attribution that is itself folklore-adjacent — teach the chain.
- **"Peeking is cheating" is only half true.** Peeking at a *fixed-horizon* test and stopping
  on significance is the sin (Type I ~5× nominal); peeking under sequential designs
  (mSPRT/always-valid inference, group-sequential plans) is legitimate by construction. The
  discipline is "decide the stopping rule before the data," not "never look."
- **The success-rate statistics are self-reported** by the platform owners (Microsoft/Bing,
  Airbnb) — directionally convergent across companies, but not independently audited numbers.
  Cite as reported experience, never as measured industry constants.
- **SRM discipline over outcome excitement**: a 50.2/49.8 split on a large sample is not
  "close enough" — it is a failed chi-square on assignment and a voided test (Fabijan
  taxonomy). Twyman's law applied to your own scorecard.

### Worked-example shapes

1. **Dunning-letter / outreach-template test** (analyst/attorney/ops): two letter variants →
   OEC (payment/response within 30 days), guardrail (complaint rate), MDE from historical
   variance via 16σ²/δ², pre-registered stop date.
2. **Feature-flag rollout as experiment** (developer): flag assignment = randomization unit;
   SRM check on exposure logs; A/A test on the flag system before trusting the first A/B.
3. **Queue/process pilot** (ops): new routing on a random half of cases; peeking discipline on
   the weekly dashboard — either sequential method or hands off until the planned horizon;
   novelty-effect check before declaring victory in week one.

### Candidate triggers (scan status)

design an A/B test (FREE — the required qualified form) · experiment design (FREE by scan, but
see seam: continuous-improvement-skills:design-of-experiments owns "design of experiments/DOE/
factorial"; prefer **online experiment design**) · online controlled experiment (FREE) · sample
ratio mismatch / SRM (FREE) · peeking (FREE) · minimum detectable effect / MDE (FREE) ·
guardrail metric (FREE — bare "guardrails" CONFLICT(coding-agent-skills:agentic-workflow-design))
· A/A test (FREE) · overall evaluation criterion / OEC (FREE) · Twyman's law (FREE) · novelty
effect (FREE — bare "novelty detection" CONFLICT(machine-learning-skills:anomaly-detection)).
**Do not claim:** bare "A/B test" — CONFLICT(data-analytics-bi-skills:statistical-inference,
explicit trigger); statistical-inference keeps *analysis* of a finished test, this skill owns
*designing and trust-auditing* one. Route seam sentence required in both descriptions.

---

## 3. survey-and-sampling-design (data-analytics-bi-skills)

### Verified anchors

- **Dillman.** *Mail and Telephone Surveys: The Total Design Method* (Wiley, 1978) → renamed
  and revised as the **Tailored Design Method**: 2000 (Mail & Internet), 2009 (3rd), 2014 (4th,
  with Smyth & Christian — *Internet, Phone, Mail, and Mixed-Mode Surveys*). Grounded in social
  exchange theory (trust/reward/cost of responding); later editions explicitly reframe the goal
  from maximizing response rate to reducing four error sources: sampling, coverage,
  measurement, nonresponse. [snippet-only, incl. WSU SESRC]
- **Total survey error.** Groves, *Survey Errors and Survey Costs* (1989); Groves & Lyberg,
  "Total Survey Error: Past, Present, and Future," *Public Opinion Quarterly* 74(5):849–879
  (2010) — the measurement-side vs representation-side error decomposition. [snippet-only]
- **Stratified sampling's founding paper.** Neyman, "On the Two Different Aspects of the
  Representative Method," *JRSS* 97(4):558–606 (1934) — stratified random sampling with optimal
  ("Neyman") allocation; discredited purposive selection. [snippet-only]
- **Literary Digest 1936.** ~10 million ballots mailed (auto/telephone lists and its
  subscribers), **2,376,523 returned**; predicted a Landon landslide; Roosevelt won ~61%.
  Squire, "Why the 1936 Literary Digest Poll Failed," *POQ* 52(1):125–133 (1988), using a 1937
  Gallup survey that asked about Digest participation: **both** frame bias and nonresponse bias
  operated, and *had everyone polled responded, the Digest would have called Roosevelt the
  winner* — Landon supporters returned ballots at much higher rates. [snippet-only]
- **1948 "Dewey Defeats Truman."** Gallup, Roper, Crossley predicted Dewey by ~5, ~15, ~5
  points; Truman won by ~5. Two documented failure modes: **quota sampling** (interviewer
  discretion within quotas skewed selection toward accessible, disproportionately
  Republican-leaning respondents) and **stopping too early** (Roper suspended presidential
  polling at the end of September; Gallup and Crossley largely done by mid-October — missing
  the late swing). The SSRC's post-mortem committee (Mosteller among the authors, 1949 report)
  drove the shift to probability sampling. [snippet-only, incl. Roper Center]
- **Question-wording effects.** Schuman & Presser, *Questions and Answers in Attitude Surveys:
  Experiments on Question Form, Wording, and Context* (Academic Press, 1981) — the experimental
  canon for acquiescence, wording, and order effects. Double-barreled and leading questions are
  standard-textbook categories hung on this anchor. [snippet-only]
- **Sample size for proportions.** n = z²·p(1−p)/e² and finite-population correction —
  standard-textbook material; canonical citation Cochran, *Sampling Techniques* (3rd ed. 1977)
  [background — verify the edition/page at authoring].

### Misattribution warnings / honesty points

- **The Literary Digest folklore is half wrong.** The story usually told — "they sampled
  car and phone owners, so the frame was rich and Republican" — is only part of it; Squire's
  evidence makes **nonresponse bias the decisive killer** (a 24% response rate whose
  respondents differed from non-respondents). A 2.4-million-person sample produced one of
  polling's great failures while Gallup called it with ~50k quota interviews: **sample size
  does not cure selection bias.** (Modern coda: Meng's "big data paradox" generalizes this
  [background — verify at authoring].)
- **1948 wasn't only a sampling failure** — the polls also *stopped polling* weeks before the
  election. Folklore keeps quota sampling and drops the timing failure; keep both.
- **Response-rate worship is anachronistic Dillman.** Dillman's own later editions demoted
  response rate from goal to one error source among four — citing "Dillman says maximize
  response rate" misstates the mature method.

### Worked-example shapes

1. **Internal survey with teeth** (analyst/ops): employee or customer questionnaire —
   stratify by unit, plan the nonresponse follow-up wave, and compute the honest n for a
   proportion with the finite-population correction; audit each question for double-barreled/
   leading/acquiescence traps.
2. **Survey evidence under attack** (attorney): trademark-confusion or class-cert survey —
   use the wording-effects literature as a cross-examination checklist; Literary Digest and
   1948 as precedent stories for challenging convenience/quota-style designs.
3. **The in-app feedback trap** (developer/ops): a feedback widget is a self-selection
   machine — diagnose who it silently samples, then design the probability-sample pulse check
   that calibrates it.

### Candidate triggers (scan status)

survey design (FREE) · questionnaire (FREE) · sample size (FREE) · sampling plan (FREE — never
bare "sampling": CONFLICT(data-analytics-bi-skills:statistical-inference, triggers "sampling,
sampling distribution")) · response rate (FREE) · nonresponse bias (FREE) · stratified sampling
(FREE) · quota sampling (FREE) · convenience sample (FREE) · question wording (FREE) · Likert
(FREE) · margin of error (FREE by scan — add a cross-link to statistical-inference, which owns
confidence intervals).

---

## 4. bayesian-updating (decision-science-skills)

### Verified anchors

- **The real history (the honesty anchor).** Thomas Bayes died 1761; "An Essay towards solving
  a Problem in the Doctrine of Chances" was found in his papers by **Richard Price**, who
  substantially edited it, replaced the introduction, added an appendix, and communicated it to
  the Royal Society (read Dec 1763; *Philosophical Transactions* 53:370–418). **Laplace
  independently rediscovered and generalized** the result ("Mémoire sur la probabilité des
  causes par les événements," 1774; modern formulation in *Théorie analytique des
  probabilités*, 1812). The theorem as used today is substantially Laplace's; Price's role was
  large enough that historians debate near-co-authorship. [snippet-only, incl. Royal Society
  and the Diniz *Significance* piece "Bayes and Price: when did it start?"]
- **Natural frequencies.** Gigerenzer & Hoffrage, "How to Improve Bayesian Reasoning Without
  Instruction: Frequency Formats," *Psychological Review* 102(4):684–704 (1995): across 15
  problems (incl. mammography), Bayesian answers rose from ~16% to ~46% when probabilities were
  recast as natural frequencies ("out of 10,000 people…"); Hoffrage & Gigerenzer (1998)
  replicated the gain in experienced physicians. The effect is computational: the format makes
  the arithmetic shallow. [snippet-only]
- **Base-rate neglect / the cab problem.** Tversky & Kahneman's taxicab problem (posed early
  1970s; canonical print treatment in the 1982 *Judgment under Uncertainty* collection): 85%
  Green / 15% Blue cabs, witness 80% reliable, witness says Blue → P(Blue|says Blue) =
  12/(12+17) ≈ **41%**; most subjects answer ≥80% — the base rate vanishes. [snippet-only]
- **Update discipline.** Tetlock & Gardner, *Superforecasting* (2015); Good Judgment Project in
  the IARPA ACE tournament. Verified traits: superforecasters update **often and in small
  increments**, and "perpetual beta" — commitment to belief-updating and self-improvement — was
  the single strongest predictor of superforecaster status. [snippet-only]
- **Bayes factors at intuition level.** Jeffreys' evidence grades (*Theory of Probability*,
  1939/1961); simplified by Kass & Raftery, "Bayes Factors," *JASA* 90:773–795 (1995) — a BF of
  ~3 is barely worth mentioning, ~20 positive, ~150 strong. Use as vocabulary for "how much
  should this evidence move me," not as a computation requirement. [snippet-only]

### Misattribution warnings / honesty points

- **"Bayes' theorem" is a textbook Stigler's-law case.** Bayes never published it in his
  lifetime, never wrote the modern form, and never named it; the published essay is partly
  Price's work; the general theorem and its applications are Laplace's. A skill that teaches
  belief revision should model honest attribution in its own foundations.
- **The famous "superforecasters beat intelligence analysts with classified access by ~30%"
  claim is *reported*, not published**: it traces to journalistic accounts of a classified
  internal comparison (widely repeated via Tetlock's book). Teach it as a reported claim with
  its provenance visible — exactly the discipline the skill preaches. [snippet-only for the
  claim's ubiquity; the underlying data is not public]
- **Natural frequencies help; they don't fix.** 16%→46% means a majority *still* failed. Claim
  "roughly triples correct reasoning," never "solves base-rate neglect."
- **The cab problem itself carries implicit assumptions** (e.g., that the witness error rate is
  color-symmetric and context-free) — critics have noted the setup smuggles modeling choices.
  One honest sentence inoculates against treating any single worked number as gospel.

### Worked-example shapes

1. **Alert triage by 10,000-count table** (analyst/ops/developer): a fraud flag, monitor
   alarm, or failing check with a known false-positive history → natural-frequency grid →
   posterior; decision threshold made explicit.
2. **Evidence weight without theatrics** (attorney): a witness/document with known
   reliability → likelihood-ratio framing ("this evidence is 5× more likely under story A than
   story B"), and the prosecutor's-fallacy guard on inverted conditionals.
3. **The update journal** (any role): a live forecast ("will the vendor deliver by Q3?")
   maintained superforecaster-style — small, frequent, logged updates with the triggering
   evidence, scored at resolution.

### Candidate triggers (scan status)

bayesian updating (FREE) · update my beliefs (FREE) · belief revision (FREE) · likelihood ratio
(FREE — seam: probability-fundamentals owns conditional-probability teaching;
competing-hypotheses-analysis owns evidence-matrix workflow) · Bayes factor (FREE) · posterior
probability (FREE) · prior probability (FREE) · superforecasting / superforecaster (FREE) ·
perpetual beta (FREE) · how much should this evidence move me (FREE). **Do not claim:** bare
"Bayes" / "Bayes' theorem" — CONFLICT(math-foundations-skills:probability-fundamentals,
explicit trigger); "base rate" / "base-rate anchor" — CONFLICT(decision-science-skills:
reference-class-forecasting; also appears in minority-report and probability-fundamentals);
"base rate neglect" — CONFLICT(probability-fundamentals, explicit trigger); "natural
frequencies" — CONFLICT(probability-fundamentals, in-description); "outside view" —
CONFLICT(reference-class-forecasting); "diagnostic evidence" — CONFLICT(competing-hypotheses-
analysis); bare "forecast" — CONFLICT(reference-class-forecasting, time-series-forecasting).
Seam design: probability-fundamentals teaches the *math*; reference-class-forecasting supplies
the *prior*; this skill owns the *ongoing update discipline for a live decision*.

---

## 5. technical-documentation (writing-skills)

### Verified anchors

- **Diátaxis.** Author: **Daniele Procida**. Ideas crystallized while he was at Divio
  (presented at conferences in early 2017, incl. "What nobody tells you about documentation,"
  PyCon Australia 2017; written up as "the Divio documentation system," later named Diátaxis at
  diataxis.fr). Four forms from two axes (action/cognition × acquisition/application):
  **tutorials** (learning-oriented), **how-to guides** (task-oriented), **reference**
  (information-oriented), **explanation** (understanding-oriented). Adoption commonly cited at
  Django, Canonical/Ubuntu (Procida later directed documentation practice at Canonical),
  Cloudflare, Gatsby; the Python project ran a public discussion about adopting it
  (discuss.python.org, 2022). [snippet-only — diataxis.fr itself egress-blocked]
- **ADRs.** Michael Nygard, "Documenting Architecture Decisions," Cognitect blog, **Nov 15,
  2011** — short, immutable records in Alexandrian-pattern style; template sections
  Title/Status/Context/Decision/Consequences; ThoughtWorks Technology Radar moved ADRs to
  "Adopt" (~2018). [snippet-only]
- **Keep a Changelog.** **Olivier Lacan** (then at Code School), published 2014; tagline
  "Don't let your friends dump git logs into changelogs"; fixed categories
  (Added/Changed/Deprecated/Removed/Fixed/Security), newest first, ISO-8601 dates; the spec
  itself follows SemVer. [snippet-only — keepachangelog.com egress-blocked]
- **Semantic Versioning.** Tom Preston-Werner (GitHub co-founder), ~2010, semver.org —
  MAJOR.MINOR.PATCH keyed to breaking/feature/fix. Companion anchor: his "Readme Driven
  Development" essay (2010): "Until you've written about your software, you have no idea what
  you'll be coding." [snippet-only]
- **Docs as code.** Anne Gentle, *Docs Like Code* (1st ed. 2017; 3rd ed. 2022) + the Write the
  Docs community guide: documentation in version control, reviewed and built like software.
  [snippet-only]

### Misattribution warnings / honesty points

- **Diátaxis is one named author and recent** — not an anonymous timeless standard. Present it
  as Procida's framework (2017→), with named adopters, not as "the industry has always done
  this."
- **The Django relationship runs both ways in folklore.** Django's docs have long used a
  similar four-part organization, and Procida is a long-time Django community figure; the
  framework systematized and generalized existing practice rather than Django "implementing
  Diátaxis" one day. Don't overclaim the adoption direction without checking current Django
  docs. Likewise Python *discussed* adoption — "considered/partially applied," not "restructured
  wholesale." [snippet-only]
- **ADR ≠ design doc ≠ RFC**: an ADR records *one decision and its consequences*, is short, and
  is superseded rather than edited — Nygard's core claim is that "large documents are never
  kept up to date; small modular documents have at least a chance."
- **Out-of-repo routing hazard**: the user's environment also carries a global
  `doc-coauthoring` skill (claude.ai-level) that triggers on documentation-writing requests —
  keep this repo-skill's triggers artifact-specific (README/ADR/changelog/Diátaxis) so the two
  can coexist.

### Worked-example shapes

1. **Docs audit by quadrant** (developer): take an existing README/wiki and sort every section
   into tutorial/how-to/reference/explanation; the misfiled sections (how-to steps buried in
   explanations) become the fix list; write ADR-0001 for the next real decision.
2. **The recurring analysis, documented** (analyst): method note = explanation; run-sheet =
   how-to; data dictionary = reference; first-time walkthrough = tutorial; changelog entries
   whenever the method version changes.
3. **Practice/process knowledge base** (attorney/ops): matter playbooks or SOPs restructured on
   the same axes, with decision memos as the ADR-analogue (what we chose, context,
   consequences) so successors inherit the *why*.

### Candidate triggers (scan status)

technical documentation (FREE) · README (FREE) · architecture decision record / ADR (FREE) ·
changelog (FREE) · Diátaxis (FREE) · how-to guide (FREE) · docs as code (FREE) · semantic
versioning / semver (FREE — note incidental "versioning" mentions in data-file-hygiene and
ml-in-production; not conflicts) · tutorial vs reference (FREE — "tutorial" appears only as
incidental prose in defect-epidemiology). **Do not claim:** bare "documentation" —
CONFLICT(writing-skills:adams-smart-brevity "documentation writing"; coding-agent-skills:
script-wizard deliverables list); "runbook" — CONFLICT(safety-and-reliability-skills:
break-glass-playbooks, explicit trigger; seam: break-glass owns crisis playbooks with tripwires
and sealed authority — this skill covers routine operational procedure docs and hands off
anything crisis-shaped); "explain it well" / explanation-design territory —
CONFLICT(writing-skills:explanation-design owns the *craft of explaining*; this skill owns the
*information architecture* and cross-links for the explanation quadrant).

---

## 6. executive-briefing (collaboration-skills)

### Verified anchors

- **BLUF / Army writing.** DA Pam 600-67, *Effective Writing for Army Leaders* (issued
  **2 June 1986**; rescinded 2013): staff-writing standard mandating the bottom line up front
  and defining "the standard for Army writing" as clear, concise, organized, right to the
  point, understandable "in a single rapid reading." AR 25-50, *Preparing and Managing
  Correspondence* (first published 1988, multiple revisions): the two non-negotiables — main
  point at the beginning (bottom line up front) and active voice. [snippet-only]
- **SCQA / Pyramid Principle.** Barbara Minto: **first female MBA-hire at McKinsey** (joined
  1963 in Cleveland; London 1966–1973; one of eight women in her HBS class of ~600); developed
  the Pyramid Principle at McKinsey; ran Minto International from 1973. SCQA =
  Situation–Complication–Question–Answer as the narrative entry to a pyramid whose apex is the
  governing thought, supported MECE below (Minto also claims MECE: "I invented it"). Editions:
  first editions circulated from 1978/1981; Pearson mass edition 1987; the authoritative
  revision is *The Minto Pyramid Principle* (1996). [snippet-only, incl. McKinsey alumni
  profile]
- **Completed staff work.** The doctrine memo — "study a problem and present a solution in such
  form that all that remains… is to indicate approval or disapproval of the completed action" —
  drafted for the Provost Marshal General by **Archer L. Lerch** (then Deputy PMG) and
  published in the *Army and Navy Journal*, January 1942. [snippet-only]

### Misattribution warnings / honesty points

- **The BLUF acronym is younger than the doctrine.** The bottom-line-up-front *rule* is 1986
  doctrine (DA Pam 600-67); claims that the literal acronym "BLUF" entered AR 25-50 only in the
  2001 revision rest on weak secondary sources in this session's search results — verify against
  the regulation text before dating the acronym in a skill. Safe claim: "Army writing doctrine
  since the 1980s; the acronym came later." [snippet-only, weak on the 2001 detail]
- **Completed staff work has a rival attribution**: the memo also circulates credited to
  Brig. G.E.R. Smith (First Canadian Army, 1943), and even friendly reprints concede "the
  original source is unclear." Lead with Lerch/Jan-1942 as best-documented; keep the
  uncertainty visible.
- **Minto's book dates are genuinely messy** (1978/1981/1985/1987 editions across sources).
  Cite the 1996 edition for anything load-bearing. And credit *Minto by name* — "McKinsey's
  method" erases the named female author the firm itself celebrates.
- **BLUF's virtue has a documented failure mode**: answer-first only works when the
  recommendation is actually supported beneath — SCQA and completed-staff-work are the
  anti-"hot take" governors; pair them rather than teaching BLUF alone.

### Worked-example shapes

1. **The one-page decision memo** (any role): variance finding, legal risk, incident, or build
   recommendation → BLUF line, SCQA framing, options with a recommendation, the explicit ask,
   and completed-staff-work test: could the reader just sign?
2. **IRAC vs BLUF** (attorney): re-lead a client advisory answer-first — the law-school habit
   buries the conclusion; show the same memo both ways.
3. **Brief-up from a working artifact** (analyst/developer/ops): turn a 20-page analysis or
   design doc into the one-pager that survives the executive's single rapid reading, with the
   pyramid mapping each summary line to its supporting section.

### Candidate triggers (scan status)

executive summary (FREE) · executive briefing (FREE) · BLUF (FREE) · bottom line up front
(FREE) · decision memo (FREE) · one-pager (FREE) · SCQA (FREE) · pyramid principle (FREE —
never bare "pyramid": CONFLICT(full-stack-dev-skills:testing-strategy, test pyramid)) ·
completed staff work (FREE). **Handle with care:** "briefing"/"brief" appear in
assertion-evidence-deck and principled-negotiation descriptions — keep this skill's trigger
forms qualified ("executive briefing," "brief the board"); "escalate" —
CONFLICT(safety-and-reliability-skills:sbar-structured-communication owns upward escalation
communication; seam: SBAR is the *spoken/urgent* channel, this skill is the *written decision
document*); "report writing" — CONFLICT(writing-skills:adams-smart-brevity, explicit trigger;
seam: smart-brevity owns sentence-level clarity and scanning structure — this skill owns the
decision-document architecture; the two compose and both descriptions should say so).

---

## 7. stakeholder-mapping (collaboration-skills)

### Verified anchors

- **Mendelow 1981.** A. L. Mendelow, "Environmental Scanning—The Impact of the Stakeholder
  Concept," *Proceedings of the 2nd International Conference on Information Systems* (ICIS),
  Cambridge, MA, 1981 (paper 20 in the AIS eLibrary). See honesty point: what the paper
  actually contains vs what is cited to it. [snippet-only]
- **Freeman 1984.** R. Edward Freeman, *Strategic Management: A Stakeholder Approach* (Pitman,
  1984) — the foundational stakeholder-theory text; the term "stakeholder" itself traces to an
  internal Stanford Research Institute (SRI) working group, ~1963, which Freeman credits.
  [snippet-only]
- **Power-interest grid (the version everyone draws).** Documented print sources: Eden &
  Ackermann, *Making Strategy: The Journey of Strategic Management* (Sage, 1998 — grid at
  p. 349), and Johnson & Scholes' *Exploring Corporate Strategy* (1999 edition), which adapted
  Mendelow's model by replacing the dynamism axis with interest. [snippet-only]
- **RACI.** Responsibility assignment matrices descend from **Linear Responsibility Charting**
  (documented from the 1950s) via 1970s "responsibility assignment matrix"/"decision rights
  matrix" practice; the RACI acronym has **no named inventor and no canonical origin paper**.
  [snippet-only, multiple convergent]
- **Influence without authority.** Allan R. Cohen & David L. Bradford, "Influence without
  authority: the use of alliances, reciprocity, and exchange to accomplish work,"
  *Organizational Dynamics* 17(3), 1989, 5–17 — the model's first publication. The book of
  the same name followed from Wiley, catalogued 1990 though its copyright year is 1989, so
  some vendor records carry the earlier date; **cite the article for 1989 and the book by
  its edition** (2nd ed. 2005, 3rd ed. 2017). An earlier line here read "Wiley, 1989",
  which conflates the two. — exchange and the law of reciprocity; "currencies"
  (inspiration, task, position, relationship, personal) as the medium of influence; a 4-step
  ally-building model. [snippet-only]

### Misattribution warnings / honesty points

- **The "Mendelow matrix" is the library's cleanest often-cited-rarely-read case.** Secondary
  sources that actually engage the 1981 paper report its matrix as **power/dynamism** — a
  contingency model for *environmental scanning* — while the **power/interest** grid attributed
  to him across the internet is the later Johnson & Scholes adaptation (1999), with Eden &
  Ackermann (1998) publishing the power-interest grid independently. Teaching rule: cite the
  grid to Johnson & Scholes or Eden & Ackermann; cite Mendelow for the idea that stakeholder
  power should drive scanning priority. (This dossier verified the discrepancy via convergent
  secondary sources, not the ICIS paper text itself — [snippet-only]; fetching the AIS eLibrary
  PDF at authoring time would upgrade this to primary evidence.)
- **Freeman did not coin "stakeholder"** — SRI 1963; Freeman himself says so. Crediting Freeman
  as coiner is the standard error.
- **RACI's origin is unknown — say so.** Vendor and consultancy pages confidently narrate
  inventors and dates that don't survive checking; "no canonical source; descends from 1950s
  linear responsibility charting" is the honest sentence.

### Worked-example shapes

1. **Change with opponents** (ops/analyst): a process/system migration → power-interest grid
   with named engagement moves per quadrant (manage closely / keep satisfied / keep informed /
   monitor), plus a RACI on the workstreams so "consulted" stops meaning "surprised."
2. **Multi-party matter** (attorney): a deal or dispute — separate decision-makers from
   influencers from blockers; map whose approval is legally required vs politically required;
   currencies-of-exchange plan for the party you cannot compel.
3. **Deprecation without authority** (developer): sunsetting an internal API — who can block,
   who must be informed, what currencies (roadmap help, migration labor, credit) buy the
   laggard team's cooperation.

### Candidate triggers (scan status)

stakeholder map / stakeholder mapping (FREE) · stakeholder analysis (FREE) · power-interest
grid (FREE) · RACI (FREE) · responsibility matrix (FREE) · influence without authority (FREE) ·
buy-in (FREE) · who needs to sign off (FREE — seam: decision-science-skills:skin-in-the-game
owns "who signs their name"/consequence design; this skill owns the map, that one the
accountability binding) · stakeholder management (FREE). **Do not claim:** "stakeholder
interview" — CONFLICT(collaboration-skills:disarming-elicitation, explicit trigger; seam
sentence: once the map says *who* matters, disarming-elicitation is *how to talk to them*);
bare "stakeholder" — three incidental description hits (sparring-partner, pre-mortem,
disarming-elicitation) make the bare token unsafe as a primary trigger.

---

## 8. reproducible-analysis (data-tools-skills)

### Verified anchors

- **Ioannidis 2005.** "Why Most Published Research Findings Are False," *PLoS Medicine*
  2(8):e124 — the metascience landmark arguing that low priors, small samples, flexibility, and
  bias make most claimed findings false. [snippet-only]
- **The empirical replication estimate.** Open Science Collaboration, "Estimating the
  reproducibility of psychological science," *Science* 349(6251):aac4716 (2015): 100 studies
  from three top psychology journals; **97% of originals had significant results; 36% of
  replications did; replication effect sizes averaged about half the originals.** [snippet-only]
- **Literate programming.** Knuth, "Literate Programming," *The Computer Journal* 27(2):97–111
  (1984) — programs as works of literature for humans, with the WEB system; the intellectual
  ancestor of notebooks/R Markdown/Quarto. [snippet-only]
- **FAIR.** Wilkinson et al., "The FAIR Guiding Principles for scientific data management and
  stewardship," *Scientific Data* 3:160018 (2016) — Findable, Accessible, Interoperable,
  Reusable, with distinctive emphasis on **machine-actionability**. [snippet-only]
- **Ten Simple Rules.** Sandve, Nekrutenko, Taylor & Hovig, "Ten Simple Rules for Reproducible
  Computational Research," *PLOS Computational Biology* 9(10):e1003285 (2013), in the
  journal's long-running "Ten Simple Rules" series (edited by Philip E. Bourne). Rules include:
  track how every result was produced, avoid manual manipulation, version everything, record
  seeds, archive exact environments. [snippet-only; the series' 2005 start date is background —
  verify at authoring]
- **Terminology history.** Claerbout & Karrenbach (1992): *reproduce* = same code + same data;
  *replicate* = new implementation/new data. The **ACM used the two words with swapped meanings
  from 2013 until Aug 24, 2020**, when it re-aligned with Claerbout. Plesser, "Reproducibility
  vs. Replicability: A Brief History of a Confused Terminology," *Front. Neuroinform.* 11:76
  (2018) is the map of the mess. [snippet-only]

### Misattribution warnings / honesty points (what's solid vs contested)

- **"Most findings are false" is a model, not a measurement.** Goodman & Greenland's published
  critique ("Problems in the Analysis," *PLoS Med* 2007): the title's "proof" is partly
  circular — the conclusion follows from the assumed priors and bias parameters. Solid version:
  the *mechanisms* (underpowering, flexibility, publication bias) are real and quantifiable;
  the headline percentage is an assumption-driven illustration.
- **The 36% figure is contested in magnitude, not in direction.** Gilbert, King, Pettigrew &
  Wilson's 2016 *Science* comment argued error, low power, and replication infidelities biased
  the OSC estimate downward; the OSC replied. Uncontested across both camps: **published effect
  sizes overstate** (the ~half-size shrinkage), and "36% replicated" must never be flipped into
  "64% of psychology is false" — a replication failure is not a disproof.
- **Even the field's two key words are unstable**: for seven years the ACM officially used
  "reproducible" and "replicable" backwards relative to most of computational science. Any
  reproducibility document must define its terms at the top — the confusion is institutional,
  not personal.
- **Practitioner translation is the skill's job**: seeds, pinned environments, raw/derived
  separation, one-command rebuild, and lineage notes are the analyst-grade payload; the crisis
  literature is the *why*, not the *how*.

### Worked-example shapes

1. **The month-end analysis, rebuilt cold** (analyst): take a recurring spreadsheet/notebook
   product and make it rerunnable from raw inputs in one command — seed recorded, environment
   pinned, every figure traceable to code + data version (Sandve rules as the checklist).
2. **Could the other side rerun your expert's model?** (attorney): damages or exposure model
   audited for reproducibility as a credibility/discovery issue — data provenance, versioned
   assumptions, deterministic reruns; the OSC/Ioannidis story as the cautionary frame for
   "peer-reviewed therefore true."
3. **"Worked on my machine" post-mortem** (developer/ops): a report or job that produces
   different numbers on rerun → hunt the seedless randomness, floating environment, and
   silently mutated source table; leave behind a lineage note and a pinned manifest.

### Candidate triggers (scan status)

reproducible analysis (FREE) · reproducibility crisis / replication crisis (FREE) · random seed
(FREE) · data lineage (FREE) · literate programming (FREE) · FAIR data (FREE) · can someone
rerun this / rerun the analysis (FREE) · data provenance (FREE as exact phrase — bare
"provenance" appears in five description texts; keep qualified). **Do not claim:** bare
"reproducible" — appears in coding-agent-skills:python-for-analysts ("clean, reproducible
Python… runs the same way twice"), data-analytics-bi-skills:data-cleaning ("reproducible,
non-destructive workflow"), and continuous-improvement-skills:measurement-systems-analysis
(Gage "repeatability and reproducibility" — a different technical sense entirely); bare
"replicate/replication" — design-of-experiments uses replication in the DOE-runs sense; "pinned
dependencies"/"virtualenv" — python-for-analysts owns the Python-environment mechanics (seam:
python-for-analysts = write the code well in Python; this skill = the cross-tool reproducibility
discipline and audit, whatever the tool). Required cross-links: python-for-analysts,
data-file-hygiene (raw/processed separation, file versioning), split-tally-evidence
(tamper-evidence vs rerunnability).

---

## 9. Collision scan

### Method

Extracted YAML frontmatter (name + description through the `Triggers:` list; `metadata:`
source notes excluded as non-routing surface) from all **115 SKILL.md files across the 15
active plugins** (`plugins/*/skills/*/SKILL.md`; `archive/` ignored). Every candidate trigger
above was matched case-insensitively with word boundaries and whitespace normalization (YAML
line-wrapping had hidden one true conflict: "stakeholder interview" wraps across lines in
disarming-elicitation's trigger list — naive grep misses it). Substring false positives were
manually cleared (e.g. "raci" inside "tracing," "prior" inside "priority").

### Known constraints from the brief — all verified

| Claimed constraint | Verified? | Evidence |
|---|---|---|
| "A/B test" owned by data-analytics-bi-skills:statistical-inference | **CONFIRMED** | explicit trigger "A/B test" + "running an A/B test" in Use-when |
| "documentation writing" in writing-skills:adams-smart-brevity | **CONFIRMED** | "…clinical, and documentation writing" in description (also: script-wizard lists "documentation" among deliverables) |
| "runbook" owned by safety-and-reliability-skills:break-glass-playbooks | **CONFIRMED** | explicit trigger "runbook" |
| "stakeholder interview" owned by collaboration-skills:disarming-elicitation | **CONFIRMED** | explicit trigger (line-wrapped — found only after whitespace normalization) |
| "sampling distribution" inside data-analytics-bi-skills:statistical-inference | **CONFIRMED** | triggers "sampling, sampling distribution" — bare "sampling" is also claimed there |
| "base rate"/"outside view" owned by decision-science-skills:reference-class-forecasting | **CONFIRMED** | triggers "outside view … base-rate anchor, base rate"; additionally "base rate" appears in minority-report and probability-fundamentals ("base rate neglect" is an explicit probability-fundamentals trigger) |
| "Bayes" in math-foundations-skills:probability-fundamentals | **CONFIRMED** | triggers "Bayes, Bayes' theorem"; description also claims "natural frequencies" |

### Conflicts found beyond the brief (each with the proposed resolution)

| Candidate phrase | Owner (active) | Resolution for the new skill |
|---|---|---|
| bare "root cause" | continuous-improvement-skills:root-cause-analysis (+ metacognition incidentals) | causal-inference never claims it; cross-link instead |
| "experiment design" (near-miss) | continuous-improvement-skills:design-of-experiments owns "design of experiments/DOE/factorial" | use "design an A/B test," "online experiment design"; seam sentence: DOE = multi-factor physical/process tuning; ab-test-design = two-variant online/field tests |
| bare "guardrails" | coding-agent-skills:agentic-workflow-design (trigger) | claim only "guardrail metric" |
| "novelty detection" | machine-learning-skills:anomaly-detection (trigger) | claim only "novelty effect" |
| "diagnostic evidence" | decision-science-skills:competing-hypotheses-analysis (trigger) | bayesian-updating drops it; cross-link |
| bare "forecast" | reference-class-forecasting, time-series-forecasting, others | claim only "superforecaster/superforecasting" |
| bare "pyramid" | full-stack-dev-skills:testing-strategy (test pyramid) | claim only "pyramid principle" |
| "escalate" | safety-and-reliability-skills:sbar-structured-communication | executive-briefing hands spoken/urgent escalation to SBAR |
| "report writing" | writing-skills:adams-smart-brevity (trigger) | executive-briefing claims "decision memo"/"executive summary" only; compose-with seam in both descriptions |
| bare "briefing" | assertion-evidence-deck, principled-negotiation (descriptions) | qualified forms only ("executive briefing") |
| bare "stakeholder" | sparring-partner, pre-mortem, disarming-elicitation (descriptions) | qualified forms only ("stakeholder map/analysis") |
| bare "reproducible" | python-for-analysts, data-cleaning, measurement-systems-analysis (Gage R&R sense), ui-and-ux-inspection | claim "reproducible analysis," "reproducibility crisis" |
| "pinned dependencies" | python-for-analysts (description) | reproducible-analysis defers Python-env mechanics; cross-link |
| bare "replication" | design-of-experiments (DOE runs sense) | claim "replication crisis," "replicate the analysis" |
| bare "provenance" | five descriptions (incl. split-tally-evidence, weak-signal-navigation) | claim "data provenance" only |
| bare "tutorial" | (incidental prose only, defect-epidemiology) | safe in qualified form "tutorial vs how-to" |

**Environment-level (out of repo, recorded for routing honesty):** the user's claude.ai-level
skills include `doc-coauthoring` (triggers on writing documentation/specs/decision docs),
`validation-design` (pilots/POC/UAT), and `learn` — the new technical-documentation and
executive-briefing skills should keep triggers artifact-anchored (README, ADR, BLUF, SCQA,
decision memo) so repo skills and platform skills stay separable.

**All-clear list (fully FREE, no qualification needed):** causal inference, confounder,
difference-in-differences, instrumental variable, regression discontinuity, natural experiment,
collider; sample ratio mismatch, SRM, peeking, minimum detectable effect, MDE, A/A test, OEC,
Twyman's law; survey design, questionnaire, response rate, nonresponse bias, stratified
sampling, quota sampling, Likert, question wording, margin of error, sample size; Bayesian
updating, likelihood ratio, Bayes factor, posterior, belief revision, perpetual beta; README,
changelog, ADR, Diátaxis, docs as code, semantic versioning, how-to guide; executive summary,
BLUF, SCQA, decision memo, one-pager, completed staff work; stakeholder map, power-interest
grid, RACI, influence without authority, buy-in; replication crisis, random seed, data lineage,
literate programming, FAIR data.

---

## 10. Summary — strongest honesty points and verification failures

**Strongest honesty points found (build these into the skills as teaching content):**

1. **Hill's "criteria" aren't criteria** — his own words: none "can be required as a sine qua
   non"; the checklist reading inverts the 1965 lecture, which also warned against
   significance-test worship.
2. **The Mendelow matrix isn't in Mendelow** — the 1981 ICIS paper's matrix is power/*dynamism*;
   the power/*interest* grid everyone draws is Johnson & Scholes (1999) / Eden & Ackermann
   (1998). The library's cleanest "often cited, rarely read" exhibit.
3. **Bayes' theorem is barely Bayes'** — posthumous, heavily shaped by Richard Price,
   independently generalized by Laplace (1774/1812), whose form we actually use: the skill
   about honest updating opens on a Stigler's-law case study.
4. **The Literary Digest died of nonresponse, not just frame bias** — Squire (1988): had all
   10M recipients answered, the Digest calls FDR correctly. 2.4M responses lost to ~50k quota
   interviews: sample size doesn't cure selection.
5. **Twyman's law was never written by Twyman** — the "any interesting figure is usually wrong"
   law survives only in Ehrenberg's 1975 formulation; an attribution onion atop the very skill
   of distrusting surprising numbers.
6. **The ACM used "reproducible" and "replicable" backwards for seven years** (2013–2020) —
   institutional-grade terminology confusion; and both flagship crisis numbers are contested:
   Ioannidis's title is a model not a measurement (Goodman & Greenland), and the OSC's 36% was
   formally disputed in *Science* (Gilbert et al.) — while effect-size shrinkage stands.
7. **"Correlation is not causation" has no author** — an 1880s–90s folk aphorism; and Pearson
   (1911) actually dismissed *causation* as the fetish.
8. **Completed staff work carries a dual attribution** (Lerch 1942 / Smith 1943 — "original
   source unclear" even in friendly reprints), and **RACI has no inventor at all** — both taught
   as provenance lessons, not suppressed.
9. **The superforecasters-beat-classified-analysts "30%" is reported, not published** — teach
   it with its provenance chain visible.

**Anchors that failed or wobbled under verification (none fatal; all handled in-dossier):**

- *BLUF acronym dating*: the 1986 DA Pam 600-67 doctrine is solid; the claim that the literal
  acronym entered AR 25-50 in 2001 rests on weak secondary sources — skill must date the
  doctrine, not the acronym, unless the regulation text is checked.
- *Minto first-edition date*: sources split across 1978/1981/1985/1987 — cite the 1996 edition
  for anything load-bearing.
- *Mendelow paper contents*: the power/dynamism finding is convergent-secondary, not primary —
  fetch the AIS eLibrary paper at authoring time to upgrade provenance.
- *Diátaxis ↔ Django direction*: adoption lists are real, but Django's similar structure
  predates the framework; do not claim wholesale "Django adopted Diátaxis" (and Python only
  *discussed* adoption). diataxis.fr itself was egress-blocked — all Diátaxis claims are
  [snippet-only].
- *Soft numbers to keep hedged*: SRM incidence "6–10%," experiment success rates (self-reported
  platform figures), the Literary Digest's prior correct-call streak (1916–1932, commonly
  reported, unverified this session), Cochran-1977 as the sample-size-formula citation, and the
  Ten-Simple-Rules series start date.

**Provenance note:** every external claim in this dossier is [snippet-only] (cross-checked
WebSearch results); all attempted direct fetches (diataxis.fr, cognitect.com,
keepachangelog.com) were egress-blocked by the sandbox proxy, matching the epic-wave research
experience.
