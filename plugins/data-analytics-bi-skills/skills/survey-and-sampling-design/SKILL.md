---
name: survey-and-sampling-design
description: >-
  Designs the survey instrument and the sampling plan BEFORE any data exists, organized by
  total survey error (Groves): chooses among simple random, stratified, cluster, and
  convenience designs and names what each does to inference; sizes the sample for a
  proportion; plans the nonresponse follow-up against the Literary Digest failure
  (Squire 1988: nonresponse, not just frame bias, sank a 2.4-million-ballot poll); audits every
  question for double-barreled, leading, acquiescence, and order effects (Schuman & Presser);
  and schedules contacts with Dillman's tailored-design discipline. Use when writing a
  questionnaire, sizing a sample, or reviewing a survey before launch — client satisfaction,
  process pain, user research, or litigation-adjacent surveys. Triggers: survey design,
  questionnaire, sample size, sampling plan, response rate, nonresponse bias, stratified
  sampling, quota sampling, convenience sample, question wording, Likert, margin of error.
metadata:
  version: "1.1.1"
  source: >-
    Built from the general-use expansion research dossier
    (docs/research/general-use-expansion-research.md, §3), whose anchors were verified
    before authoring. Provenance legend carried through: [snippet-only] = cross-checked
    WebSearch result blocks (direct fetches egress-blocked); [background — verify] =
    well-known claim not independently confirmed, kept hedged.
---

# Survey and sampling design (total survey error)

In 1936 the Literary Digest mailed ~10 million ballots and got 2,376,523 back — one of the
largest samples ever collected — and called the election for Landon; Roosevelt won with ~61%.
Gallup called it correctly with roughly 50,000 quota interviews [snippet-only]. The lesson is
the founding lesson of this skill: **sample size does not cure selection bias**, and most of
what decides a survey's fate is decided before the first response arrives. This skill does
the before part: the instrument, the sample, and the error budget.

## When to use
- Writing a questionnaire and its sampling plan: a client-satisfaction survey, an internal
  process-pain survey, user research for a product, a pulse check on a team or a customer base.
- A litigation-adjacent survey whose design will be attacked — the consumer-confusion shape:
  the wording-effects literature doubles as a cross-examination checklist.
- Sizing a sample: "how many responses do we need?" — for a proportion, in plain terms.
- Reviewing someone else's survey before launch, or diagnosing why a feedback channel
  (an in-app widget, a comment box) keeps telling a different story than reality.
- Not for: analyzing the data once collected — confidence intervals, hypothesis tests, and
  the sampling distribution belong to `data-analytics-bi-skills:statistical-inference`; this
  skill designs what that skill later analyzes, and a good design names its analysis plan
  before launch.
- Not for: qualitative one-on-one elicitation — the stakeholder interview, the expert
  walkthrough — → `collaboration-skills:disarming-elicitation`. The seam: that skill surfaces
  tacit knowledge from one willing person with an adaptive conversation; this skill fields a
  **standardized instrument** across a sample so answers are comparable and countable. Use it
  first to discover what to ask; use this skill to ask it at scale.
- Not for: selection by lot for governance — who reviews, what gets audited, unriggable
  draws → `safety-and-reliability-skills:sortition-review`. That skill draws for fairness and
  deterrence; this skill samples for **estimation**, and the design criteria differ.

## Do it
Full design mechanics, the worked example, and the question-audit checklist are in
`references/survey-design-method.md`.

1. **State the decision and the target population first.** What decision will the numbers
   feed, and about whom is the claim? Write the target population, then the *frame* — the
   actual list you can sample from — and name the gap between them (coverage error). A survey
   without a decision attached collects opinions; a frame nobody inspected collects bias.
2. **Budget the four error sources before perfecting any one.** Total survey error (Groves)
   splits the ways a survey misleads into **representation** errors (coverage, sampling,
   nonresponse) and **measurement** errors (wording, order, mode, response style)
   [snippet-only]. Spend design effort where your survey is weakest, not where effort is most
   visible — a bigger n fixes only sampling error, the one source that usually matters least.
3. **Choose the sampling design and say what it does to inference.** Simple random: the clean
   default when the frame is one list. Stratified random (Neyman 1934): divide the frame into
   groups that matter, sample within each — guarantees subgroup estimates and usually tightens
   precision [snippet-only]. Cluster: sample groups first (sites, teams), then within — cheaper
   per response, wider error bars for the same n. Convenience (and its cousin quota): whoever
   is easiest to reach — label it honestly as *unquantifiable* inference; it can generate
   hypotheses, never population estimates with a defensible margin of error.
4. **Size the sample in plain terms.** For a proportion at 95% confidence and margin of
   error e: n ≈ 0.96/e² using the worst case p = 0.5 (that is z²·p(1−p)/e² with z = 1.96) —
   so ±5 points needs ~385, ±3 points ~1,068. Apply the finite-population correction when the
   population is small, then **divide by the expected response rate** to get the invitation
   count. Canonical treatment: Cochran's *Sampling Techniques* [background — verify edition
   before citing formally].
5. **Plan the nonresponse follow-up before launch — this is the step the Digest skipped.**
   Dillman's tailored-design discipline: multiple contacts (prenotice, invitation, reminders,
   a final different appeal), each written as a social exchange — lower the cost of
   responding, raise the visible reward and trust [snippet-only]. Pre-plan the diagnostics:
   compare respondents to the frame on known variables, and early responders to late ones
   (late responders stand proxy for non-responders).
6. **Audit every question.** One idea per question (no double-barreled "fast and courteous");
   neutral stems (no leading); balanced agree/disagree alternatives or item reversal
   (acquiescence — some respondents agree with anything); order checked (earlier questions
   contaminate later ones); Likert scales labeled at every point, with a considered
   don't-know policy. The experimental canon is Schuman & Presser [snippet-only]. Pretest on
   a handful of real respondents thinking aloud before fielding.
7. **Precommit the analysis plan and hand off.** Name the estimates, subgroups, and
   comparisons before data arrives, then run the analysis under
   `data-analytics-bi-skills:statistical-inference` — margins of error and confidence
   intervals are its property, and they are only honest if steps 1–6 held.

## Why / learn
Total survey error is the organizing frame because it converts a vague worry ("is this survey
any good?") into a budget with line items (Groves & Lyberg 2010) [snippet-only]. The deep
teaching is that the line items trade off: doubling n halves nothing but sampling error, while
the same money spent on one more follow-up contact attacks nonresponse — usually the bigger
number.

The Literary Digest story earns its place only when told correctly. The folklore says the
frame was rich (auto and telephone lists), so the sample skewed Republican. Squire (1988)
showed, using a 1937 Gallup survey that asked people about their Digest participation, that
**nonresponse was the decisive killer**: had everyone polled responded, the Digest would have
called Roosevelt the winner — Landon supporters simply returned their ballots at much higher
rates [snippet-only]. A 24% response rate whose respondents differ from its non-respondents
poisons any sample size; 2.4 million responses lost to ~50k interviews. (A modern
generalization — the "big data paradox" — is often cited here; treat it as background and
verify before leaning on it.)

Then 1948 broke the winners. Gallup, Roper, and Crossley all called Dewey; Truman won by ~5.
Two documented failures, and folklore keeps only one: **quota sampling** let interviewer
discretion inside the quotas skew selection toward accessible, disproportionately
Republican-leaning respondents — quota controls the margins but not the choosing — and the
pollsters **stopped polling too early** (Roper by end of September, Gallup and Crossley
largely by mid-October), missing the late swing. The SSRC post-mortem (1949, Mosteller among
the authors) drove the field to probability sampling [snippet-only]. Moral: a measurement plan
includes *when* you measure.

Dillman deserves his honest reading too: his later editions demote response rate from the goal
to one error source among four (sampling, coverage, measurement, nonresponse) [snippet-only].
"Dillman says maximize response rate" misstates the mature method — a high response rate from
the wrong frame, answering loaded questions, is a precisely measured wrong answer.

## Common mistakes
- Trusting a big sample over a good one → the Digest failure; representativeness beats volume.
- Reading a margin of error off a convenience sample → the formula assumes probability
  sampling; without it the ± is decoration.
- Confusing quota sampling with stratified sampling → strata are sampled *randomly within*;
  quotas are filled by interviewer/self-selection — 1948's first failure mode.
- Worshipping response rate → anachronistic Dillman; audit *who* responded, not just how many.
- Double-barreled, leading, or unbalanced questions → each one converts measurement error
  into confident-looking numbers; run the step-6 audit.
- No nonresponse plan until responses disappoint → follow-up waves and diagnostics must be
  designed (and budgeted) before launch.
- Fielding once and assuming opinions hold still → 1948's second failure mode; time the
  measurement to the decision.
- Skipping the pretest → the first ten respondents always find an ambiguity; better they find
  it before 1,000 do.

## Tailor to your environment
Record in `references/your-environment.md`: the populations you survey repeatedly and the
frames (lists) that reach them, typical response rates by audience (they set your invitation
math), your house contact cadence and survey tool, standing strata that matter (unit, region,
customer tier), and where past instruments and their results live so wording stays comparable
across waves. Keep the committed file structural — real client names, respondent-level data,
or live results belong in `your-environment.private.md` (git-ignored), never in a committed
file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/survey-and-sampling-design.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/survey-design-method.md — the total-survey-error map, sampling designs with
  their inference consequences, plain-terms sample-size math with a worked end-to-end
  example, the nonresponse playbook (Literary Digest and 1948 told correctly), the
  question-audit checklist, and the litigation-adjacent survey shape
- references/your-environment.md — your populations, frames, response-rate history, and
  house conventions (fill in)
