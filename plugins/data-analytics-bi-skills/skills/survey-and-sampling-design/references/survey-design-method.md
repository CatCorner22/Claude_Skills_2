# Survey and sampling design — full method

Contents: 1. The total-survey-error map · 2. Sampling designs and their inference
consequences · 3. Sample size in plain terms (worked) · 4. The nonresponse playbook
(Literary Digest and 1948 told correctly) · 5. The question-audit checklist ·
6. Worked end-to-end example: an internal process-pain survey · 7. The
litigation-adjacent shape · 8. Provenance notes

## 1. The total-survey-error map

Total survey error (Groves, *Survey Errors and Survey Costs*, 1989; Groves & Lyberg, *Public
Opinion Quarterly* 2010) decomposes everything that can make a survey wrong into two sides
[snippet-only]:

**Representation side** — does the sample stand for the population?
- **Coverage error**: the frame (the list you sample from) misses part of the target
  population, or contains people outside it. The Digest's auto/telephone/subscriber lists
  are the canonical example — but see §4 for why coverage was not the decisive failure.
- **Sampling error**: the only error the margin-of-error formula measures — the noise from
  observing a sample instead of everyone. Shrinks with √n; the *only* error that does.
- **Nonresponse error**: the people who answer differ from the people who don't, on the
  thing you are measuring. Not a function of response rate alone — a 24% response rate is
  fatal or harmless depending on *who* the 24% are.

**Measurement side** — do the answers mean what you think?
- **Measurement error**: wording, question order, scale construction, mode effects
  (people answer differently to a person than to a form), and response styles
  (acquiescence, social desirability).
- **Processing error**: coding, keying, cleaning mistakes downstream.

Design rule: write one line per error source before drafting a single question — "our
biggest exposure is ___, and the design spends against it by ___." A design that spends
everything on n is optimizing the one line that √-decays anyway.

## 2. Sampling designs and their inference consequences

| Design | How it selects | What it does to inference |
|---|---|---|
| Simple random (SRS) | Every frame member has equal, known chance | Clean textbook inference; needs one complete frame list |
| Stratified random | Split the frame into strata; random sample *within* each | Guarantees subgroup estimates; usually tighter precision than SRS at equal n; strata must be assignable from the frame |
| Cluster | Randomly pick groups (sites, teams, classrooms), then sample within | Cheaper per response; *wider* error bars at equal n (people within a cluster resemble each other — the design effect) |
| Systematic | Every k-th from an ordered list, random start | Behaves like SRS unless the list order has a cycle that matches k |
| Convenience | Whoever is easiest to reach (a link on a webpage, a widget) | No known selection probabilities → no defensible margin of error; hypothesis generation only |
| Quota | Convenience selection until demographic quotas fill | Looks representative on the quota margins; selection *within* quotas is still biased — the 1948 failure mode |

Stratification is Neyman's contribution ("On the Two Different Aspects of the
Representative Method," *JRSS* 1934), the paper that also discredited purposive selection
[snippet-only]. Two allocation rules:
- **Proportional**: each stratum gets sample in proportion to its population share. Default.
- **Neyman (optimal)**: allocate ∝ stratum size × stratum standard deviation — sample more
  where answers vary more. Needs variance estimates (from a pilot or a prior wave).

Honesty rule for convenience samples: report them as "of those who responded to X," never
as population estimates. The in-app feedback widget is a self-selection machine — it
oversamples the delighted, the furious, and the heavy user. The fix is not to discard it
but to *calibrate* it: run a small probability-sample pulse check on the same questions and
compare; the widget then becomes a cheap change-detector between calibrations.

## 3. Sample size in plain terms (worked)

For estimating a proportion at 95% confidence with margin of error e:

- **Base formula**: n₀ = z²·p(1−p)/e², with z = 1.96 and p = 0.5 as the worst case
  (p(1−p) is largest at 0.5, so this never under-sizes). Plain version: **n₀ ≈ 0.96/e²**.
  - ±5 points → n₀ = 1.96² × 0.25 / 0.05² = 384.2 → **385**
  - ±3 points → 1,068 · ±10 points → 97
- **Finite-population correction** (population N is small): n = n₀ / (1 + (n₀−1)/N).
  For N = 1,200: n = 384.2 / (1 + 383.2/1200) = 384.2 / 1.319 ≈ **292**.
- **Invitation math**: divide by the expected response rate. At 40%: 292 / 0.40 = **730
  invitations**. If the whole population is only 1,200, invite everyone and spend the
  budget on follow-up instead — the census-with-follow-up often beats the sample.
- Canonical citation for the formula family: Cochran, *Sampling Techniques*
  [background — verify the edition/page before citing formally].

Three plain-terms facts worth teaching whenever someone asks "how many":
1. Precision buys quadratically: halving the margin of error quadruples n.
2. Population size barely matters once N is large — 385 covers ±5 points for a city or a
   country alike; the FPC only helps when n is a noticeable fraction of N.
3. n is the *completed-response* count, not the invitation count — and no n repairs a
   biased selection mechanism (§4).

## 4. The nonresponse playbook (the two stories, told correctly)

**Literary Digest, 1936.** ~10 million ballots mailed to auto-registration and telephone
lists plus its own subscribers; 2,376,523 returned; predicted a Landon landslide; Roosevelt
won ~61% of the vote. The folklore blames the rich frame. Squire (*Public Opinion
Quarterly* 1988), using a 1937 Gallup survey that asked respondents about their Digest
participation, showed **both** biases operated and that **nonresponse was decisive**: had
everyone polled responded, the Digest would have called Roosevelt the winner — Landon
supporters returned their ballots at much higher rates [snippet-only]. Teaching points:
- Response rate ≈ 24% of a huge mailing still failed: **sample size does not cure
  selection bias** — Gallup called the race with ~50k quota interviews.
- Nonresponse bias = (nonresponse rate) × (difference between responders and
  non-responders on the measured thing). Attack either factor.
- A modern coda ("the big data paradox": data quality dominates data quantity) is commonly
  attached to this story [background — verify before citing].

**"Dewey Defeats Truman," 1948.** Gallup, Roper, and Crossley predicted Dewey by roughly
5, 15, and 5 points; Truman won by ~5. Two documented failure modes [snippet-only, incl.
Roper Center]:
1. **Quota sampling**: interviewers filled demographic quotas but chose *whom* to approach
   within them — selection drifted toward accessible, disproportionately
   Republican-leaning respondents. Quotas control the margins; they do not randomize the
   choosing.
2. **Stopping too early**: Roper suspended presidential polling at the end of September;
   Gallup and Crossley were largely done by mid-October — the late swing went unmeasured.
The SSRC post-mortem committee (1949 report; Mosteller among the authors) drove the
industry shift to probability sampling. Keep both failure modes: folklore keeps the quota
story and drops the timing story, and the timing story generalizes to every pulse survey
fielded weeks before the decision it feeds.

**Dillman's tailored-design contact discipline** (Total Design Method 1978; renamed and
revised as the Tailored Design Method across the 2000/2009/2014 editions, the last with
Smyth & Christian) [snippet-only, incl. WSU SESRC]:
- Grounded in social exchange: each contact should lower the perceived **cost** of
  responding (short, easy, mobile-friendly), raise the **reward** (show why it matters,
  who will act on it), and build **trust** (real sender, confidentiality stated honestly).
- Multiple contacts, varied in appeal — e.g., prenotice → invitation → reminder →
  replacement questionnaire → final different-mode appeal. The variation matters: a
  repeated identical nag re-reaches the same inclined people.
- The mature method's goal is **reducing all four error sources** (sampling, coverage,
  measurement, nonresponse), not maximizing response rate — later editions demote response
  rate explicitly. "Dillman = chase response rate" is anachronistic [snippet-only].

**Nonresponse diagnostics to pre-plan:**
- Compare respondents vs the frame on every variable known for both (unit, role, region,
  tenure). Divergence = weight or re-field, and *say so* in the report.
- Compare early vs late responders; late responders proxy for non-responders — if answers
  drift across waves, the non-responders likely sit further along the drift.
- Keep a small reserve budget for an intensive follow-up of a random subsample of
  non-responders; even 30 conversions measure the responder/non-responder gap directly.

## 5. The question-audit checklist

The experimental canon: Schuman & Presser, *Questions and Answers in Attitude Surveys*
(1981) — wording, form, and context effects demonstrated by split-ballot experiments
[snippet-only]. Audit every item:

- **Double-barreled**: two ideas, one answer box. "Was the staff fast and courteous?" —
  fast-but-rude has no honest answer. Split it.
- **Leading / loaded**: the stem signals the wanted answer ("How much do you agree that
  our award-winning support…"). Neutral stems; name both sides ("Some people think X,
  others think Y — which comes closer to your view?").
- **Acquiescence**: some respondents agree with almost any statement. Mitigate with
  balanced forced-choice items or reversed-keyed pairs; never score an all-"agree" battery
  at face value.
- **Order effects**: earlier questions set context for later ones (asking about specific
  problems before overall satisfaction depresses the overall score). Put general before
  specific; randomize blocks where order is contested.
- **Recall and telescoping**: bound the period ("in the past 30 days"), anchor to events.
- **Likert construction**: label every scale point with words; keep direction consistent
  across a battery; 5 or 7 points is conventional; decide the midpoint/don't-know policy
  deliberately (a missing "don't know" manufactures opinions).
- **Sensitive items**: place late in the instrument, state confidentiality honestly, and
  prefer self-administered modes.
- **Pretest**: 5–10 members of the real population, thinking aloud. Every instrument has
  an ambiguity; the pretest decides whether 10 people find it or 1,000 do.

## 6. Worked end-to-end example: internal process-pain survey

Setting (domain-neutral): an ops lead wants to know what share of a 1,200-person
organization loses ≥2 hours/week to a broken internal process, and where the pain
concentrates. Decision attached: which of three candidate fixes gets funded.

1. **Population & frame**: all current staff; frame = the HR roster (complete → coverage
   error ≈ 0; note contractors excluded and say so in the report).
2. **Error budget**: biggest exposure = nonresponse (the busiest people — the likeliest
   sufferers — are the least likely to answer) and measurement (leading questions about a
   process everyone loves to hate). Design spends on follow-up waves and a neutral
   instrument, not on extra n.
3. **Design**: stratified random by unit — Operations 600, Sales 400, Support 200 —
   proportional allocation, which buys the tightest *overall* estimate. The price is
   per-unit precision: at n = 146/97/49 the per-unit margins are roughly ±7 / ±9 / ±12
   points (1.96·√(0.25/n)·FPC), not ±5. If each unit's estimate must stand on its own at
   ±5, use equal or minimum-n allocation instead — and note that ±5 in Support means ~132
   completes from a unit of 200, a near-census of that stratum.
4. **Size**: ±5 points at 95% → n₀ = 385; FPC at N = 1,200 → 292. Proportional split:
   146 / 97 / 49. Historical response rate 40% → invite 730 (365 / 243 / 122). Sanity
   check: inviting 730 of 1,200 is close to a census — consider inviting all 1,200 and
   banking the surplus for follow-up.
5. **Nonresponse plan**: prenotice from a trusted sender; invitation; two reminders (the
   second reworded around "your unit's results will be acted on"); early-vs-late
   comparison pre-registered; respondent-vs-roster check on unit and tenure.
6. **Instrument audit**: "How many hours per week do you lose to rework or workarounds on
   process X?" (bounded recall, no leading adjective); pain items split per process step
   (no double-barrels); two reversed items guard acquiescence; overall-satisfaction item
   placed *before* the specific-problem battery.
7. **Analysis plan, precommitted**: estimate the ≥2-hours proportion overall and per
   stratum with 95% intervals (per-stratum intervals are the wide ones from step 3);
   compare units. Analysis itself runs under
   `data-analytics-bi-skills:statistical-inference`.

## 7. The litigation-adjacent shape (generically framed)

Surveys enter disputes as evidence — consumer confusion, deceptive-labeling perception,
community attitudes — and the opposing expert's job is to break the design. The same
checklist above, read adversarially, is the attack surface; run it against your own design
before the other side does:
- **Universe and frame**: does the sampled population match the legally relevant
  population (actual/prospective purchasers, not the general public)? A mismatch is a
  coverage attack.
- **Selection**: convenience panels and mall-intercept quotas invite the Digest/1948
  precedent stories; probability designs, or at minimum documented quota procedures with
  screening questions, survive better.
- **Wording**: leading stems and missing "don't know / no opinion" options are the classic
  cross-examination targets — a confusion estimate without a don't-know option
  manufactures confusion.
- **Controls**: perception questions need a control condition (a control label, a control
  mark) so the measured effect isn't just background noise — the survey analog of a
  placebo arm.
- **Order and demand effects**: does the questionnaire telegraph the sponsor's theory by
  the third question? Blind the interviewers and the respondents to sponsorship.
Document every design choice contemporaneously; in this shape the design memo *is* the
deliverable.

## 8. Provenance notes

- Groves 1989; Groves & Lyberg 2010 (total survey error) — [snippet-only].
- Neyman 1934, *JRSS* 97(4):558–606 (stratification; against purposive selection) —
  [snippet-only].
- Literary Digest figures (~10M mailed, 2,376,523 returned) and Squire 1988, *POQ*
  52(1):125–133 (nonresponse decisive; all-respond counterfactual calls FDR) —
  [snippet-only].
- 1948: Gallup/Roper/Crossley margins, quota-selection and early-stopping failure modes,
  SSRC 1949 post-mortem (Mosteller) — [snippet-only, incl. Roper Center].
- Dillman 1978 → Tailored Design Method editions 2000/2009/2014 (with Smyth & Christian);
  social-exchange grounding; response rate demoted to one of four error sources —
  [snippet-only, incl. WSU SESRC].
- Schuman & Presser 1981 (wording/order/acquiescence experiments) — [snippet-only].
- Sample-size formula family attributed to Cochran, *Sampling Techniques* —
  [background — verify edition/page before formal citation].
- The "big data paradox" coda — [background — verify before citing].
- All worked arithmetic in §3 and §6 recomputed at authoring time.
