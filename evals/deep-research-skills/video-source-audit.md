# Evals — deep-research-skills:video-source-audit

## 1. Positive trigger (should load the skill)
> "Someone sent me this youtube video claiming a supplement cuts heart attack risk by 40%, and it
> links three papers in the description. Can you check whether the papers actually say that?"

Expected: skill loads and works the full pipeline. It runs the reachability preflight **first** and
says which of the three outcomes occurred; summarizes the video in logical form (thesis → claims →
evidence) before opening any source; builds a claim ledger with timecodes and pre-registered
load-bearing claims; resolves the three linked papers to identifiers and records the depth tier at
which each was read; **locks the comparison to each source's prespecified primary analysis** before
classifying; runs the fidelity ladder with the conclusion-change test at the F1/F2 boundary; scores
the bounded comprehensiveness checklist; runs the statistics pass as its own instrument — starting
with the asymmetric-framing check — and reconstructs absolute risk from the 40% relative figure plus
the control-arm event rate; emits **three separate letter grades** with provenance lines and any
interlock flags; and states explicitly that it is not producing a composite grade. Every statistic
is translated into natural frequencies. It then runs the **independent literature pass** — searching
the claim rather than the video's citations — to establish whether those three papers are
representative of the evidence. The response is delivered as the **six mandated sections**:
executive summary, hyper-thorough analysis, grade and reasoning, statistics breakdown, additional
research findings, and a conclusion linking both the video's sources and the independent research.

## 2. Near-miss A (should NOT load this skill)
> "Summarize this 40-minute conference talk for me — I just want the main points."

Expected: a plain summary from the assistant's general capability. No source-tracing, no ledger, no
grades. The skill's own description says it is not a summarizer, and its `When to use` says so
explicitly. If the audit machinery fires here, the description is over-triggering on video
vocabulary and the "Not a summarizer" boundary needs to move into the description itself.

## 3. Near-miss B (should NOT load this skill)
> "I've had fatigue and numbness for months, I'm on metformin, and my B12 is low. What could link
> these?"

Expected: `deep-research-skills:medical-research-detective` loads. This is a clinical case file with
no video in it. **This is the highest-risk seam in the library for this skill** — same plugin,
adjacent vocabulary — and the two are separated by whether a video is the object of the analysis.
If this skill loads, the seam must move into both descriptions, not just the bodies.

## 4. Near-miss C (in-domain, but must refuse to grade — should load)
> "Here's a link to a video that's been taken down / is region-locked. Grade it for accuracy anyway
> based on what the title and comments suggest it said."

Expected: the skill loads and **declines to grade**. It emits `NOT-GRADED`, names the observed
failure mechanism, and explains why reconstructing a video from its title is exactly the output the
skill exists to prevent. Offers the paste path. **Any letter grade in this response is a failure**,
however hedged — as is asserting that a source "does not exist" when what happened was that a fetch
was blocked.

## 5. Near-miss D (the video is right and the source is wrong — should load)
> "This video accurately describes a 2011 study, but I heard the study was retracted. How should
> that affect how much I trust the video?"

Expected: the skill loads and applies the routing rule rather than blurring it: faithful
representation of a retracted source is **not** an accuracy failure. It codes the retraction as
comprehensiveness omission O7, caps that axis, and raises the `FAITHFUL-TO-BAD-SOURCE` interlock
flag so the accuracy letter cannot be read alone. A response that downgrades *accuracy* for this has
misunderstood the axis and is a failure.

## 6. Quality rubric
A good response:
- **Delivers all six sections, in order, under their own headings:** (1) plain-language executive
  summary, (2) hyper-thorough analysis, (3) grade and reasoning, (4) statistics breakdown,
  (5) additional research findings, (6) conclusion with working links to both the video's sources
  and the independent research. A report missing a section is a **failure** even if everything
  present is correct — and section 5 is the one most likely to be skipped, because it is the only
  one that requires searching beyond what the video cited.
- **Keeps the structure when the audit fails:** a `NOT-GRADED` or `INCOMPLETE` response still
  carries all six headings, saying under each what could not be determined. Collapsing to a
  one-line apology is a failure. Section 5 in particular is usually still possible — the topic can
  be researched even when the video cannot be read — and should be attempted and labelled as
  answering the topic rather than auditing the video.
- **Runs the independent pass as an audit, not a prosecution:** section 5 characterises the
  evidence rather than building a rival case, reports the wider literature *supporting* the video
  as prominently as a contradiction, discloses its search stopping point, and keeps work published
  after the video out of the accuracy grade while still reporting it to the reader.
- **Does the task:** preflight before promising anything; logical-form summary before opening
  sources; claim ledger with timecodes and weight classes; sources resolved to identifiers; depth
  tier recorded per source; comparison target locked before classification; three axes scored
  separately.
- **Refuses honestly:** distinguishes "no captions", "video unreachable", and "network blocked" by
  mechanism, and never converts a tooling failure into a claim that a source does not exist. Emits
  `INCOMPLETE`/`NOT-GRADED` where the preconditions fail rather than manufacturing a letter.
- **Grades defensibly:** every letter carries its provenance (score, band, which cap fired, whether
  the mechanisms agree); boundary cases within 0.02 of a band edge are disclosed; **no composite
  grade is emitted**, and the report says why.
- **Handles statistics correctly:** absolute alongside relative with the baseline, never one alone;
  natural frequencies in the plain-language layer; odds ratios not read as risk ratios; the
  asymmetric-framing check actually run as a table rather than assumed.
- **Verifies rather than recalls:** citations resolved against retrieved records; a search tool's
  generated prose is never treated as evidence; anything unresolvable is dropped or labelled
  unverified, never quietly included.
- **Teaches:** explains *why* the comparison target must be locked first, why the three axes are not
  averaged, and why a relative risk reduction is incomplete rather than false.
- **Proportionate:** an audit of three claims is reported as an audit of three claims, not as a
  verdict on a creator. States what it could not check.

## 7. Script checks
- `fetch_transcript.py --self-test` prints `all offline logic checks passed` with 0 failures and
  exits 0. (The script counts its own checks; assert the pass line and the exit code, not a
  hard-coded total.)
- **De-duplication is real, not claimed.** On the bundled rolling-caption fixture, the collapsed
  text contains each phrase exactly once and is materially shorter than the raw cue text — the
  self-test asserts a reduction ratio, because the whole reason the function exists is that raw
  auto-captions cost on the order of 15-20x the tokens of the de-duplicated text.
- **Human (non-rolling) captions pass through unchanged**, and a genuine repeated phrase that is not
  a scrolling overlap survives — the self-test carries that negative control.
- **Failure classification never invents a dead video.** A proxy/policy block classifies as exit 4
  (network unavailable), a private or removed video as exit 3, and an unrecognised error as 4 —
  never as 3. Misreporting a blocked fetch as a removed video is the defect this check exists for.
- With no captions available the script exits **2** and says so, rather than emitting an empty
  transcript that a caller could mistake for a silent video.
