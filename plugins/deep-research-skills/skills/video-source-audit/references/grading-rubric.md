# The three-axis grading instrument

A letter grade is a number the audit manufactures about someone else's work. It is only defensible
if two competent auditors reach the same letter from the same evidence. Everything here is designed
for that, and the instrument publishes its own workings so a disputed grade can be argued with.

**Contents**
- §1 Design: why a hybrid, and where caps bite
- §2 Scoring the three axes
- §3 The band tables (one per axis, and why they differ)
- §4 The cap ladder
- §5 INCOMPLETE, NOT-GRADED, and precedence
- §6 Interlock flags — and the ban on a composite grade
- §7 What forces an F; what earns an A+
- §8 The highest-leverage fix, computed
- §9 The output contract
- §10 Reproducibility: how to check this instrument, and its unvalidated claim

---

## §1 Design: why a hybrid, and where caps bite

Two obvious designs both fail:

- **Pure compensatory** (average the claims) is gameable. Ten reversed load-bearing claims plus 390
  accurate asides scores 195/225 = **0.8667 → B**. Padding buys a grade.
- **Pure non-compensatory** (one bad claim caps everything) fails on *reproducibility*: the letter
  becomes a function of whether the auditor happened to find a bad claim, so a deeper audit always
  grades lower and no two audits agree.

**The resolution:** a compensatory weighted *rate* over the whole ledger, capped by a
non-compensatory ladder that fires only on the small, pre-registered set of **load-bearing** claims.

**The second-order rule that makes it reproducible — cap severity tracks coding objectivity.**
The harshest caps sit on the most objectively codeable failures (does the source exist? does its
conclusion invert?), and the gentlest on the most judgment-laden. Let facts cap; let judgments
average.

**Claim weights:** load-bearing **3.0**, supporting **2.0**, aside **0.5**.

**The 25% aside-mass rescale.** If aside weight exceeds 25% of total weight, set
`allowed = 0.25 × non_aside_weight / 0.75` and scale aside points by `allowed / aside_weight`.
On the padded video above: allowed = 0.25 × 30 / 0.75 = 10, aside points 195 → 10, giving
10/40 = **0.2500 → F**. On an honest aside-heavy video (4 load-bearing + 5 supporting + 30 asides,
all faithful) the rescale fires and the score stays **1.0000 → A+**, because rescaling a class whose
fidelity matches the core changes nothing. The cap bites only when aside fidelity diverges from core
fidelity — exactly the case it exists for.

---

## §2 Scoring the three axes

**Grade on rates, never on counts.** Two auditors will split the same 40-minute video into 18 or 31
claims purely from granularity choices; a count threshold ("3+ reversals → C") therefore grades the
auditor. Counts are used *only* inside the cap ladder, where the denominator is the small,
pre-registered load-bearing set.

**Accuracy** — fidelity of representation.
`A_raw = Σ(wᵢ · pᵢ) / Σ(wᵢ)` over all **checkable** claims, where `w` is the weight and `p` the
fidelity score from the ladder (F0 = 1.00, F1 = 0.85, F2/F2u = 0.50, F3/F3s = 0.25, F4 = 0.10,
F5/F6 = 0.00). Claims coded `NC` (not checkable) are **excluded from the denominator**, never scored
zero — an unreachable source is not the video's failure.

**Comprehensiveness** — `C_raw = items satisfied / items applicable` over the bounded checklist in
`claim-audit-method.md` §5, scored per load-bearing claim, `N/A` items dropped from the denominator.

**Statistics** — its own pass, not a derivative of the fidelity codes. Enumerate every statistical
statement in the transcript; score each against the taxonomy: 1.00 clean, 0.50 incomplete
(technically true, materially misleading — e.g. relative with no baseline), 0.00 wrong (a number or
interpretation that is simply incorrect). `S_raw = Σ points / count`. A claim can be F0 on accuracy
and 0.00 here; that independence is the reason the axis exists.

---

## §3 The band tables

Each axis needs its **own** table. Sharing one is a hidden calibration error: the comprehensiveness
checklist is demanding by construction, so genuine well-made explainers land around 25–45%, and
under the accuracy table essentially the whole population would score F. A scale with no
discrimination is not a scale.

| Band | Accuracy | Comprehensiveness | Statistics |
| :--- | ---: | ---: | ---: |
| A+ | ≥ .98 | ≥ .90 | ≥ .95 |
| A | ≥ .95 | ≥ .82 | ≥ .90 |
| A- | ≥ .92 | ≥ .75 | ≥ .85 |
| B+ | ≥ .88 | ≥ .68 | ≥ .79 |
| B | ≥ .84 | ≥ .62 | ≥ .73 |
| B- | ≥ .80 | ≥ .56 | ≥ .67 |
| C+ | ≥ .74 | ≥ .50 | ≥ .60 |
| C | ≥ .68 | ≥ .44 | ≥ .53 |
| C- | ≥ .62 | ≥ .38 | ≥ .46 |
| D+ | ≥ .55 | ≥ .32 | ≥ .39 |
| D | ≥ .48 | ≥ .26 | ≥ .32 |
| D- | ≥ .40 | ≥ .20 | ≥ .25 |
| F | < .40 | < .20 | < .25 |

Worked check: `C_raw = 7/28 = 0.2500` scores **F** on the accuracy table and **D-** on the
comprehensiveness table. D- is the informative answer — it leaves room below it for a video that
discloses nothing at all.

**Know the scale's asymmetry.** A through D- are 0.03–0.08 wide; F absorbs the whole bottom 0.40.
Two videos at 0.39 and 0.05 are both F and are not remotely alike, so an F must always be reported
with its score and its cause, never as a bare letter.

---

## §4 The cap ladder

Caps apply to the **load-bearing** set. Take the worst that fires; the final letter is
`worse(band(score), lowest applicable cap)`.

| Trigger (on a load-bearing claim) | Axis | Cap | Why this severity |
| :--- | :--- | :--- | :--- |
| F6 fabricated — source does not exist, reachability confirmed | Accuracy | **F** | Maximally objective: it exists or it does not |
| F5 reversed | Accuracy | **F** if ≥50% of load-bearing claims, else **D** | Objective: the conclusion inverts or it does not |
| F4 unsupported, ≥2 claims | Accuracy | **C-** | Objective, but a single instance can be an honest miss |
| F3/F3s scope- or strength-inflated, ≥2 claims | Accuracy | **C+** | Partly judgment |
| Statistical statement flatly wrong (0.00) | Statistics | **D** | Objective |
| Relative effect with no baseline anywhere in the video | Statistics | **C** | Objective and central |
| Asymmetric framing (benefit relative, harm absolute) | Statistics | **C+** | Objective once tabulated |
| O7 relies on retracted/superseded source without noting it | Comprehensiveness | **D** | Objective |
| O5 contrary literature omitted on a load-bearing claim | Comprehensiveness | **C** | Judgment; gentler cap |

---

## §5 INCOMPLETE, NOT-GRADED, and precedence

**NOT-GRADED** — the audit could not run: video unreachable, no transcript obtainable, or the video
makes no checkable claims (a vlog, an opinion piece, entertainment). This is not a bad grade; it is
the wrong instrument or a missing input, and the report says which.

**INCOMPLETE** — the audit ran but the evidence is too thin for a rate: fewer than 5 checkable
claims, or more than 50% of load-bearing sources at tier T0/T1 (see acquisition §4).

**Precedence, applied in this order — caps override INCOMPLETE downward; INCOMPLETE overrides
scores upward:**

1. If a hard cap fires on **verified** evidence, emit that letter regardless of the sample floor,
   annotated *"cap-derived on a thin sample"*.
2. Else, if a precondition fails, emit `NOT-GRADED` or `INCOMPLETE`.
3. Else emit `worse(band(score), lowest applicable cap)`.

The asymmetry is deliberate: **proven failure is knowledge; thin evidence is not.** A 90-second
short with three claims, one citing a paper that does not exist, gets an F on accuracy with the
thin-sample annotation — reporting INCOMPLETE there would hide a proven fabrication. But a thin
sample may **never** manufacture a *high* grade.

---

## §6 Interlock flags — and the ban on a composite grade

**Emit no composite letter. Ever.** The technically-true cherry-picker scores accuracy A+ (every
claim verbatim faithful to real papers), statistics A, comprehensiveness C- (three fringe papers
out of a literature of forty). Averaging the band indices: (0 + 1 + 8)/3 = 3.00 → **B+**. That single
letter is the most misleading output this instrument could produce. Say so explicitly in the report,
because a downstream reader or summariser will otherwise compute one.

Cross-axis information is carried by **named flags**, printed above the grades:

- **SELECTION-DISTORTED** — accuracy ≥ A- while comprehensiveness ≤ C+. Faithful representation of
  an unrepresentative source set. This is the cherry-picker.
- **FAITHFUL-TO-BAD-SOURCE** — accuracy ≥ B+ while a load-bearing source is retracted or has a
  documented failed replication. The video reported honestly; the evidence base did not hold.
- **TRIVIALLY-ACCURATE** — accuracy in the A range on fewer than 10 checkable claims. Accurate about
  very little.
- **UPSTREAM-DISTORTION** — the exaggeration is present in the source's own press release and the
  video repeated it. A failure to check, not an act of invention.

---

## §7 What forces an F; what earns an A+

**Forces an F:** any fabricated load-bearing claim; reversal on ≥50% of load-bearing claims; or a
score below the axis floor (accuracy < .40, comprehensiveness < .20, statistics < .25).

**Earns an A+ — all four, so it is achieved rather than defaulted:**
1. Score at or above the A+ threshold for that axis.
2. Zero F2-or-worse codes in **any** weight class.
3. At least 10 checkable claims audited.
4. The video must **affirmatively do the good thing**, not merely avoid the bad one:
   - *Accuracy* — volunteers at least one limitation of its own source.
   - *Comprehensiveness* — steelmans the opposing view at least once.
   - *Statistics* — translates its own headline statistic to an absolute scale in its own words
     (baseline plus absolute change, or an NNT, or natural frequencies).

Both ends must be reachable, or the scale is decoration.

---

## §8 The highest-leverage fix, computed

Do not guess what the creator should fix. **Compute it:** for each claim and each statistical
statement, re-run the score with that unit set to clean, re-apply the cap ladder, and report the
unit whose repair produces the largest band gain.

This is not busywork — it routinely overturns the intuitive answer. In testing, repairing the
*obvious* defect (adding the baseline risk alongside the relative figure) gained **zero bands**,
because a separate wrong-number cap survived the repair; a different, less obvious repair moved the
grade four bands. An auditor eyeballing "what should they fix" would have given the wrong advice
with complete confidence.

---

## §9 The output contract

Every letter is printed with its **provenance**, so a reader can argue with the right thing:

```
Accuracy:          C-  (score 0.637 → band C-; cap C- from 2 unsupported load-bearing
                        claims; both mechanisms agree)
                       boundary case: 0.017 above the C-/D+ line — one reclassified
                       claim moves this
Comprehensiveness: D-  (C_raw 0.250 = 7 of 28 applicable items)
Statistics:        D   (S_raw 0.587 → band C; capped at D by one flatly wrong figure)

FLAGS: SELECTION-DISTORTED
NO COMPOSITE GRADE — see §6.
```

**Boundary rule:** if a score is within 0.02 of a band boundary, say so. Without that disclosure,
two auditors who differ by a single claim look like they disagree about the grade when they
actually agree about the video.

The full report additionally carries the logical-form summary, the claim ledger, the scored
checklist, the statistics findings with plain-language translations, the computed highest-leverage
fix, the limitations, and the further-reading set.

---

## §10 Reproducibility: how to check this instrument, and its unvalidated claim

**Stated plainly so it is not inherited as a stronger claim than it is: this rubric's inter-rater
reproducibility has not been validated.** It was designed for reproducibility and its arithmetic,
cap interactions, and band behaviour were verified by execution — but no two independent auditors
have run it on a real video. Treat the agreement targets below as design goals, not measurements,
and say so if you report a grade to someone who might treat it as calibrated.

**Do not gate this instrument on kappa alone.** Grade distributions are skewed — most audited videos
land B through C — and weighted kappa collapses on skewed marginals. A rater pair agreeing exactly
85% of the time and within one band 100% of the time can produce κ_w = 0.000, while the *same* rater
behaviour on a spread corpus gives κ_w ≈ 0.98. This is the high-agreement/low-kappa paradox that
`continuous-improvement-skills:measurement-systems-analysis` documents for measurement systems
generally; it lands squarely on grading rubrics.

**Acceptance criteria, if you validate it:** within-one-band agreement ≥ 90%; exact-band agreement
≥ 60%; per-claim fidelity-code agreement ≥ 80%. Report κ_w only alongside the band distribution that
produced it.

**Segment long videos.** Above roughly 45 minutes or 60 claims, grade segments separately and report
the worst segment beside the whole. Otherwise the arithmetic averages a fabricated core claim
against two hours of accurate conversation, and the single letter describes neither.
