---
name: video-source-audit
description: >-
  Audits a video against the primary sources it cites — pulls the transcript, traces every
  linked and spoken source to the literature, reads what those sources actually say, then
  grades the video A+ to F on three separate axes: fidelity to its sources, comprehensiveness,
  and portrayal of statistics. Translates every statistic into plain language, absolute risk
  beside relative. Use for a YouTube, podcast, lecture, or conference-talk link whose claims
  need checking, or when a video's numbers look too good; for a clinical symptom question see
  deep-research-skills:medical-research-detective. Triggers: youtube, fact check this video,
  audit this video, check this video's sources, is this video accurate, grade this video, does
  this video misrepresent the study, debunk this video.
metadata:
  version: "1.0.0"
  source: >-
    Built from a seven-stream research pass with adversarial verification. Statistical
    arithmetic independently recomputed; citations verified against retrieved index data
    only (see references/further-reading.md on why the distinction matters).
---

# Video source audit

Takes a video and the sources it claims to rest on, reads both, and reports where they diverge.
The output is an audit: a claim-by-claim ledger, three independent letter grades, and an evidence
trail a reader can check without rewatching anything.

**The discipline this skill exists to enforce:** it is easy to watch a video and form an opinion
about it. This produces a *finding* about the video, which means every judgment traces to a named
source, a timecode, and a stated rule — and the skill refuses to grade when it cannot reach the
evidence, rather than producing a confident letter out of vibes.

## When to use
- A video makes empirical claims and you want to know whether its sources say what it says they
  say — a health or nutrition explainer, a science-communication channel, a documentary segment,
  a conference talk, a podcast episode with citations on screen.
- A video's numbers look too good: "cuts your risk in half", "doubles your chances", "studies show".
- You are deciding whether to trust a creator, and want the reasoning rather than the verdict.
- You already have the paper and want to know whether the video represented it faithfully.
- Not for: a clinical symptom cluster, drug interaction, or "what could link these" literature
  case file → `deep-research-skills:medical-research-detective`. Training, nutrition, or
  supplement protocols for a healthy person → `coding-agent-skills:fitness-nutrition-science`.
  Turning a meeting recording into decisions and owners → `collaboration-skills:meeting-design`.
  A statistics question with no video attached → `data-analytics-bi-skills:statistical-inference`.
  Auditing your own project's metrics and benchmark claims →
  `continuous-improvement-skills:project-command-center`.
- **Not a summarizer.** Summarizing is step 2 of nine, not the deliverable. If someone wants a
  plain recap with no source-checking, give them that and do not run the audit machinery.

## Do it

Work the nine stages in order. Stages 1 and 4 can fail, and failing them honestly is the point —
a grade issued without reaching the sources is the exact output this skill exists to prevent.

1. **Preflight, and be willing to stop here.** Probe reachability *before* promising an audit.
   Run the recipes in `references/acquisition-and-sources.md` §1. Three outcomes, and they must
   never be conflated:
   - **Reachable with captions** → continue.
   - **Reachable, no captions** → say so; offer to audit from a transcript the user pastes.
   - **Not reachable** (network policy, region block, private/removed video) → **stop and say so.**
     Do not reconstruct the video from its title, from memory, or from what similar videos say.
     A blocked fetch and a nonexistent source produce identical-looking failures, so the skill
     must distinguish them by *mechanism*, not by result.

2. **Summarize in logical form.** Not a recap — a structure: the thesis, the claims offered in
   support of it, the evidence offered for each claim, and the action the video wants the viewer
   to take. Note explicitly what the video asserts without support. This structure is what the
   rest of the audit is run against, so build it before looking at any source.

3. **Build the claim ledger.** Decompose the transcript into atomic, checkable claims with
   timecodes, and assign each a **weight class** — *load-bearing* (the thesis depends on it;
   pre-register 3–5 of these before auditing), *supporting*, or *aside*. Method, claim typology,
   and what does not count as a claim: `references/claim-audit-method.md` §1–2.
   Weight classes are not decoration — the grading instrument uses them to stop a video from
   diluting one fabricated core claim with thirty accurate asides.

4. **Trace every source.** Description links, pinned comment, spoken references ("a 2019 Lancet
   paper"), chapter titles, linked companion articles. Resolve each to a durable identifier
   through the resolver ladder in `references/acquisition-and-sources.md` §2–3.
   **State the on-screen limit plainly**: citations that appear only as text in the video frame
   are invisible to a transcript-based audit. If a video cites on screen, say that the source list
   is incomplete and that the comprehensiveness grade is affected.

5. **Read the sources, and record how deeply.** An audit built on abstracts is not the same
   artifact as one built on methods and results, and the report must say which it is. Abstracts
   systematically overstate. Where full text is unreachable, mark the claim
   `SOURCE-NOT-READ` and exclude it from the graded denominator rather than guessing.

6. **Lock the comparison target.** Before classifying anything, fix *what in the source* the claim
   is being compared against — the source's own **prespecified primary analysis**. This is the
   single highest-leverage rule in the method: the same video claim classifies as faithful or as
   overstated depending only on which slice of the source you hold it against, so the slice is
   chosen once, in advance, and recorded. `references/claim-audit-method.md` §3.

7. **Classify fidelity, then measure omission.** Run each claim down the precedence ladder
   (fabricated → reversed → unsupported → scope-inflated → strength-inflated → overstated →
   imprecise → faithful, plus *understated*, which most taxonomies forget). Resolve the
   overstated/imprecise boundary with the **conclusion-change test** — would a viewer of the video
   reach a different practical conclusion than a reader of the source? — because that is a binary
   two auditors can agree on, where "is this overstated?" is a matter of taste. Then score the
   bounded comprehensiveness checklist. Both in `references/claim-audit-method.md` §4–5.

8. **Audit the statistics as its own instrument.** A claim can be perfectly faithful and still be
   the video's worst statistical act — "cuts risk 25%" against a source reporting a 25% relative
   reduction is faithful *and* misleading. So the statistics axis has its own detection pass, not
   a derivative of the fidelity codes. Work the taxonomy in `references/statistics-taxonomy.md`,
   which carries for each move: the definition, the arithmetic, the plain-language translation,
   and the literal question that detects it in a transcript. Start with the asymmetric-framing
   check — relative for the benefit, absolute for the harm — because it catches videos in which
   every individual number is correct.

9. **Grade, flag, and report.** Three letters, one per axis, each with its provenance. Apply the
   cap ladder and the interlock flags; emit `INCOMPLETE` or `NOT-GRADED` where the preconditions
   fail. **Never emit a composite grade** — averaging the three axes hands a textbook
   cherry-picking video a B+. Instrument and output contract: `references/grading-rubric.md`.
   Close with the plain-language statistics translations and the further-reading set from
   `references/further-reading.md`.

**Deliverable contract.** The report carries, in this order: the logical-form summary; the three
letter grades with provenance lines; any interlock flags; the claim ledger (timecode, claim,
weight, source, fidelity code, evidence); the comprehensiveness checklist scored; the statistics
findings with plain-language translations; the single highest-leverage fix, *computed* by re-running
the score with each unit set to clean rather than guessed at; limitations and what could not be
checked; and the verified further-reading list. A reader must be able to disagree with any grade by
pointing at a specific row.

## Why / learn

**The audit's whole value is the comparison, not the opinion.** A viewer can tell that a video
*feels* overconfident. What they cannot do cheaply is open the cited paper, find the primary
endpoint, and discover that the video quoted a secondary outcome in a subgroup. That gap — between
what a source says and what a video says it says — is where nearly all science-communication
distortion lives, and it is invisible without doing the retrieval. This is also why the skill
refuses to grade unreachable sources: an audit that skips the comparison is just an opinion wearing
an audit's formatting.

**Distortion mostly enters upstream of the video.** Sumner et al.'s BMJ study of health-science
news found that exaggeration in news coverage was strongly associated with exaggeration already
present in the *academic press release* — when the release exaggerated, the news usually did too;
when it did not, news exaggeration rates were far lower. A replication reported the same pattern.
The practical consequence for this skill is a rule: before grading a creator harshly, check whether
they faithfully repeated a press release that was already wrong. That is a different, lesser
failure than inventing the distortion, and the rubric routes it differently — which is why
"the video is wrong" and "the source is wrong and the video reported it faithfully" are separated
by design, and why a faithful report of a retracted study is a *comprehensiveness* failure rather
than an accuracy one.

**Three axes, never averaged, because they fail independently.** A video can be scrupulously
faithful to three cherry-picked papers out of a literature of forty: accuracy A+, comprehensiveness
C-. The average is a B+, and the B+ is the most misleading number the instrument could produce.
Separate letters preserve the information that the video's problem is *selection*, not *fidelity* —
and the interlock flags name that combination explicitly so nobody has to notice it themselves.

**Grade on rates, cap on load-bearing claims.** Pure averaging is gameable: pad a video with
accurate asides and a core reversal dilutes away. Pure capping is also broken — it makes the grade
a function of how hard the auditor looked, so a deeper audit always scores lower. The hybrid fixes
both, and the second-order rule is what makes it reproducible: **the harshest caps sit on the most
objectively codeable failures.** Whether a cited source exists is a fact; whether a claim is
"overstated" is a judgment. Let the facts cap and let the judgments average.

**Absolute versus relative is the centerpiece because it is where honest numbers mislead.** A
relative risk reduction is not false — it is incomplete, and it is often the more transferable
number across populations. The failure is presenting it *alone*, because the same "50% reduction"
is life-changing at a 20% baseline and irrelevant at a 0.002% one. The corrective is never to
replace relative with absolute; it is to require the baseline alongside, so the viewer can compute.
And the reason the plain-language layer uses natural frequencies ("90 of the 1,080 people who test
positive actually have it") rather than percentages of percentages is that this is a measured
comprehension effect, not a stylistic preference.

## Common mistakes
- Grading a video you could not actually fetch → the two failures look identical in the output and
  must be distinguished by mechanism. Stop and say which one happened.
- Reading a search tool's generated summary as evidence → the retrieved link list is data; the
  prose beneath it is generated and will state a confident publisher, year, and DOI for a source
  that returned no supporting link. Verify against the returned records, never the summary.
- Auditing against whichever part of the source fits → lock the comparison to the prespecified
  primary analysis first, or the classification is chosen rather than found.
- Averaging the three grades → hands a cherry-picking video a B+. Report three letters, always.
- Counting claims instead of weighting them → counts measure how finely the auditor split the
  transcript, so a count-based rule grades the auditor.
- Treating "the video is wrong" and "the source is wrong" as the same failure → they grade on
  different axes and deserve different language.
- Calling a claim unsupported when the source was merely unreachable → mark `SOURCE-NOT-READ` and
  drop it from the denominator.
- Fixing the obvious statistical defect and assuming the grade moves → compute the highest-leverage
  repair by re-scoring; the intuitive fix frequently gains nothing because a cap still holds.
- Letting the audit's own confidence exceed its evidence → an audit of three claims is not a
  verdict on a creator. Say what the sample was.

## Tailor to your environment
Record in `references/your-environment.md`: the creators, channels, and subject domains you audit
repeatedly; your standing evidence bar (does a preprint count?); whether you have institutional
full-text access, which decides how much of stage 5 is reachable; your preferred report length; and
any severity weighting your audience needs (a clinical audience weights harm claims differently
than a general one).

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/video-source-audit.md` works well —
fill it in there, and point this skill at that copy. Your specifics then survive updates and stay
somewhere you own rather than in a cache you may not realise is disposable.

**Never commit a real person's identifying detail into an audit file.** Auditing a named creator is
ordinary criticism of published work; keep it to what they published, and keep private individuals
out of it entirely.

## References
- references/acquisition-and-sources.md — reachability preflight, transcript fetch and
  de-duplication, the source-tracing pipeline, the resolver ladder, and how each step fails
- references/claim-audit-method.md — claim decomposition, the claim typology, locking the
  comparison target, the fidelity precedence ladder with the conclusion-change test, and the
  bounded comprehensiveness checklist
- references/statistics-taxonomy.md — the misrepresentation taxonomy: definition, arithmetic,
  plain-language translation, and transcript-detection question for each move, with
  absolute-vs-relative worked in full
- references/grading-rubric.md — the three-axis instrument: weighted rates, per-axis band tables,
  the cap ladder, interlock flags, the INCOMPLETE/NOT-GRADED path, and the output contract
- references/further-reading.md — verified books and articles, with the verification standard
  used and the candidates that were dropped for failing it
- references/your-environment.md — your creators, domains, evidence bar, and access (fill in)

## Scripts
> Paths use `${CLAUDE_PLUGIN_ROOT}` so they resolve from **any** working directory once the plugin
> is installed. A bare `scripts/…` path only works inside a clone of the marketplace repo, which is
> not where a user runs these.
- `python3 "${CLAUDE_PLUGIN_ROOT}/skills/video-source-audit/scripts/fetch_transcript.py" <url>` —
  probes reachability, fetches the transcript and metadata via yt-dlp, and collapses YouTube's
  rolling auto-caption format into clean timecoded lines. That collapse is not cosmetic: measured
  on real auto-caption files, the rolling format repeats each line across successive cues and costs
  on the order of 15-20x the tokens of the de-duplicated text (the exact multiple depends on
  whether you compare against plain or timecoded text). Exits non-zero and says which failure occurred
  when the video is unreachable, so an audit can never silently proceed without a transcript.
  `--self-test` runs the offline parsing tests.
- Citation resolution reuses this plugin's existing verifier, which lives under the same plugin root:
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/medical-research-detective/scripts/verify_citation.py" --doi <doi>`
