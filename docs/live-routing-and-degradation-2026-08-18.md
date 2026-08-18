# Live routing and listing-degradation findings — 2026-08-18

This document replaces folklore with measurement. Everything in it was produced by the real
Claude Code harness — the actual skill-loading mechanism and the actual `Skill` tool — not by a
simulation. Method, tooling, and every number are recorded so the next person can reproduce or
falsify any of it.

## 0. How this was run

`claude plugin eval` and `claude plugin marketplace` are real, shipped commands
(`claude plugin --help` lists them), gated behind a per-organization early-access flag. The gate
can be opened for a single shell via `CLAUDE_CODE_WALNUT_SPIRE=1`, set in the environment — not
committed to any repo settings file, which is why this file records the *finding*, not the
enablement mechanism, as the thing to reuse.

Setup performed:
```bash
CLAUDE_CODE_WALNUT_SPIRE=1 claude plugin marketplace add /home/user/Claude_Skills_2
CLAUDE_CODE_WALNUT_SPIRE=1 claude plugin install <plugin>@treasury-analyst-skills   # all 14
```
All 14 plugins were installed at `user` scope, so this session's real skill listing genuinely
carried all 121 skills, exactly as an end user's would after `/plugin install` on every plugin
in this marketplace — plus this session's own separately-installed personal skill set (~20-30
skills, not inventoried here), which competes for the same budget.

Total real spend across everything below: **≈ $0.93** (one $0.33 baseline run before a target
was correctly resolved, plus seven $0.06–$0.11 live routing cases). Disclosed in full because
`claude plugin eval` spends real money per run and the number should be checkable.

## 1. The real degradation mechanism — not what the record said

`MEMORY.md` carried a single anecdotal lesson from 2026-07-18, from an unrelated prior project:
*"With ~100 installed skills, the skill-listing context budget trims least-used descriptions to
name-only."* That claim was never tested against this repository's own skills. It is now
corrected on two counts.

**The real settings**, read directly from the compiled CLI's own settings schema (`claude plugin
--help` documents the commands; the settings themselves surface via their `describe()` text):

- `skillListingBudgetFraction` — default `0.01` (1% of the context window, **measured in
  characters**) reserved for the skill listing sent to Claude.
- `skillListingMaxDescChars` — default `1536` characters per-skill description cap.
- Official behavior, quoted verbatim: *"When the listing exceeds this, descriptions are
  shortened to fit."*

**What was actually observed live, today, does not match "least-used" or "shortened."** A
fresh non-interactive session (`claude -p "..."`) was asked to read its own current skill
listing — not recall from training — and report, skill by skill, whether each of the 121
marketplace skills carries a real description or has been reduced to a bare name. Full
methodology: ask for `plugin:skill<TAB>FULL|NAMEONLY` pairs explicitly (a first attempt that
asked for unlabeled status lines produced answers that could not be reliably aligned back to
skill names — recorded as a methodology note in §4).

**Result: 101 of 121 NAMEONLY, 19 FULL, 1 not applicable.**

The one not applicable is `machine-learning-skills:bespoke-llm-architect`, which sets
`disable-model-invocation: true` — it does not appear in the general listing at all, consistent
with its by-design invoke-only status (already known from the trigger-test protocol's Tier D
exclusion).

The 19 FULL skills are **not** the shortest, the most-triggered, or in any way distinguished by
content:

| Plugin | Full | Total |
|---|---:|---:|
| `writing-skills` | 5 | 5 |
| `coding-agent-skills` | 14 | 20 |
| every other plugin (12 of them) | 0 | 96 |

Within `coding-agent-skills`, the 14 FULL skills are exactly its first 14 skills in alphabetical
directory order, and the 6 NAMEONLY ones are exactly the last 6. Sorting the entire 121-skill set
by description length shows FULL and NAMEONLY interleaved at every length from 484 to 1019
characters — length does not predict the outcome. Install order does: `writing-skills` was
installed first (during initial tool setup), `coding-agent-skills` second, and the other 12
followed in a loop. The pattern is a **sequential fill in listing order, with a hard cutoff** —
everything before the cutoff keeps its full text, everything after loses it entirely — not a
priority ordering by usage, importance, or size.

**Reproducibility check.** A second, differently-worded query without explicit name-tagging
produced answers that did not match the first scan — investigated, and the mismatch was a
methodology defect (the model's unlabeled reply couldn't be reliably position-matched to the
four skills asked about), not evidence that the underlying state is unstable. Re-run with
explicit `name<TAB>status` pairs required for every answer, the second query reproduced the
first exactly (`gonzo`=FULL, `sparring-partner`=NAMEONLY, `agent-harness-config`=FULL,
`value-stream-mapping`=NAMEONLY, matching the full scan). **Lesson for reuse: never ask this kind
of live-introspection question in a form that lets the model drop the label — the three prior
occurrences in this protocol of "the test prompt was the defect" all trace to the same root
cause, an under-specified prompt.**

## 2. The measured floor, and why "~100 skills" understates the real risk

Summing the name+description character length of exactly the 19 FULL skills: **17,104
characters** — about **2.3% of a 200K-token window** at this repo's own 3.7 chars/token
estimate, and that is a *lower* bound, since this session's own ~20-30 personal skills also
compete for the same budget and were not separately measured.

Two things follow, and both matter more than the number itself:

1. **The old framing ("past ~100 skills, some get name-only'd") is not wrong in direction but is
   wrong in mechanism and severity.** It is not a graceful degradation that spares the
   important ones. In this exact, realistic full-install configuration, **83% of the library's
   skills carry zero routing signal beyond their bare name** — far more severe than "~100" as a
   count-based threshold suggests, because the real constraint is a *character budget*, and 121
   skills' worth of good-faith, information-dense descriptions blow through it after roughly
   one and a half plugins' worth of content.
2. **Which skills survive is arbitrary, not meaningful.** It is a function of install order, not
   of what a person actually needs. A user who installs `math-foundations-skills` first would
   see an entirely different 19 survive. There is no way to install "the important skills first"
   as a mitigation, because nothing in the product surfaces this ordering to the installer.

## 3. Real token cost, cross-checked against a second, independent measurement

`claude plugin details <plugin>` reports a harness-computed "always-on" token cost per plugin,
using the actual tokenizer rather than a chars-per-token estimate. Summed across all 14 plugins:

| Plugin | Always-on (real tokenizer) |
|---|---:|
| coding-agent-skills | ~6,806 |
| collaboration-skills | ~1,727 |
| continuous-improvement-skills | ~5,152 |
| data-analytics-bi-skills | ~3,595 |
| data-tools-skills | ~2,087 |
| decision-science-skills | ~4,932 |
| deep-research-skills | ~346 |
| full-stack-dev-skills | ~3,102 |
| learning-skills | ~892 |
| machine-learning-skills | ~2,047 |
| math-foundations-skills | ~2,000 |
| metacognition-skills | ~1,188 |
| safety-and-reliability-skills | ~3,319 |
| writing-skills | ~1,611 |
| **Total** | **~38,804** |

This repo's own `scripts/measure-listing-cost.py` estimated **29,638–29,718 tokens** for the same
121 skills across this session's measurements, using a 3.7-characters-per-token approximation.
The real, tokenizer-computed figure is **≈ 30% higher**. Spot-checking five individual skills
(writing-skills' full component breakdown) shows the same ~27–29% gap consistently — this is not
noise in one plugin, it is a systematic property of this prose style under the real tokenizer
(heavy use of em dashes, backticks, and punctuation that a flat chars/token ratio undercounts).

**Corrected headline: a full install costs not 14.8% but closer to 19.4% of a 200K window**
(38,804 / 200,000), using the harness's own accounting rather than this repo's estimate. The
`3.7 chars/token` divisor `measure-listing-cost.py` uses is documented as an *estimate*, and this
is the first time it has been checked against the real tokenizer — the check shows the estimate
runs consistently light for this library's prose. Every place this repo quotes 14.8%/14.9% is
now corrected to cite both figures, with the real one primary.

## 4. Live routing tests via the real `Skill` tool — 7 cases, real agent turns

Beyond listing visibility, seven cases were run as genuine agent turns (`claude plugin eval
<plugin> --runs 1 --ablation none --case <name>`), each grading on `tool_used: Skill,
input_match: <skill>` against the actual tool-call transcript. This is the harness's own
mechanism, not a text-matching stand-in.

| Case | Prompt (abridged) | Target | Target's live status | Result |
|---|---|---|---|---|
| d1-live | "Get gonzo on this quarterly report…" | `writing-skills:gonzo` | FULL | **Skill called 1×. PASS.** |
| d2-live | "…bring it up to the bar you'd hold yourself to." | `full-stack-dev-skills:elite-python-engineer` | NAMEONLY | Skill called 0×. |
| a1-live | "Review this Python module… principal engineer…" | `full-stack-dev-skills:elite-python-engineer` | NAMEONLY | Skill called 0×. |
| c10-live | "Refactor this paragraph so it reads better." | must NOT be `elite-python-engineer` | NAMEONLY | Skill called 0× (guard held, but uninformative — see below). |
| d9-live | "Tear our new pricing model apart…" | `coding-agent-skills:chicken-little-executive-advisor` | **FULL** | Skill called 0×. |
| c13-live | "…dates come in three different formats. Clean this up." | must NOT be `script-wizard` | FULL | Skill called 0× (guard held). |
| c16-live | "Our refund policy has an edge case… Stress test it." | must NOT be `script-wizard` | FULL | Skill called 0× (guard held). |

**The load-bearing result is d2-live and a1-live.** Both prompts are the exact repaired-seam
prompts from the Tier D re-run, which the blind-simulation method scored as fixed (43/45,
description-level repair confirmed). Run for real, against a session where
`elite-python-engineer`'s description is currently invisible, **both fail with zero Skill calls
— not a wrong pick, an absent one.** This directly confirms, with the real mechanism, the thing
the whole simulation-based trigger-test protocol could never test: **a routing fix verified by
simulation is conditional on the description being visible at all, and in a realistic full
install, it frequently is not.** Every "PASS" this protocol has recorded to date was measured
against a full, undegraded listing — an upper bound the live deployment does not reliably meet.

**d9-live is a second, weaker finding, reported at its true confidence.** Its target
(`chicken-little-executive-advisor`) *is* FULL in this session, yet the live agent still did not
invoke `Skill` for a prompt the repaired description should match ("business model...process...
attacked whole"). This is one data point (n=1) and is not treated as a confirmed pattern — it
may be prompt-specific (the agent judged it could just answer the critique directly without a
formal tool call, since nothing about the task *requires* the tool to satisfy the user) rather
than a routing failure in the same sense as the invisible-description cases. Recorded as an open
question, not a conclusion: **does the real agent under-invoke `Skill` even for visible,
matching descriptions, separately from the listing-truncation risk?** This needs more than one
live sample to answer and was not pursued further here on cost grounds.

**c10/c13/c16 "PASS" results are real but weaker than they look.** In two of the three
(`c13`/`c16`), the grader itself was authored with a bug (`max: 0` alone, without an explicit
`min: 0`, silently produced an impossible `1..0` expected range) — the printed score was FAIL
regardless of actual behavior, but the raw "Skill called 0×" trace is the real signal and shows
the guard held. `c10` targeted an already-invisible skill, so its "0 calls" proves nothing new.
Recorded so the grader bug is not repeated: **`tool_used` graders asserting absence need `min: 0`
stated explicitly.**

## 5. Item 3 — checked, not extended

Before writing more Tier C guards on the pattern that caught `script-wizard`, the library was
searched for a second skill carrying the same defect signature: an explicit, unqualified
breadth claim in the description ("any work of real substance," "even when phrased casually," or
equivalent). Only `script-wizard` carries it. The next-broadest candidate,
`coding-agent-skills:sparring-partner` ("any work product"), was checked against the same
standard that flagged `script-wizard` and found meaningfully different: it already carries two
reciprocal boundary clauses repaired this session (against `script-wizard` itself and against
`chicken-little-executive-advisor`), and no narrower same-purpose sibling exists in this library
for generic single-artifact critique — unlike `script-wizard`, whose breadth competed directly
with specific-purpose siblings that own more precise vocabulary (`data-cleaning`,
`git-and-code-review`, `rule-stress-testing`, `value-stream-mapping`).

**Conclusion: no second skill warrants a new guard row.** This check is recorded so a future
pass does not re-run the same search and re-derive the same negative result.

## 6. What this changes going forward

1. `README.md`, `MEMORY.md`, `docs/library-review-2026-08.md`, and `docs/trigger-test.md` are
   corrected to cite the real mechanism (character-budget sequential fill, not usage-based
   name-only trimming) and the real cost figure (harness-tokenizer-computed, ~30% above this
   repo's own chars/token estimate).
2. Every PASS this protocol has ever recorded — including the freshly-repaired D2/D9 seams — is
   now understood to be conditional on full-listing visibility, which a realistic full install
   does not provide. This is the single most consequential correction from this pass: **the
   trigger-test protocol has never once tested the condition its own users will actually be
   in.**
3. A live sampling method now exists and is documented (`claude plugin eval` under
   `CLAUDE_CODE_WALNUT_SPIRE=1`) for anyone who wants to extend this beyond the seven cases run
   here. It costs real money per run; budget accordingly.
