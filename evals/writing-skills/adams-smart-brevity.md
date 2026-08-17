# Evals — writing-skills:adams-smart-brevity

## 1. Positive trigger (should load the skill)
> "Review the language in this engagement-letter paragraph — it says the firm will
> 'indemnify and hold harmless against any and all claims arising out of or relating to the
> aforesaid services rendered hereunder.' Make it precise and litigation-resistant."

Expected: skill loads; diagnoses the sources of misunderstanding first (doublet, "any and
all" string, "aforesaid"/"hereunder" archaisms, unanchored scope); rejects the "tested
language" defense explicitly; supplies a modern rewrite with one category of contract
language per sentence; output itself is Smart Brevity-structured (point first, why it
matters, scannable); flags any vague quantifier left undefined.

## 2. Near-miss (register guard — should load adams-plain-grade instead)
> "Rewrite this billing letter so our patients can understand it — plain English, low
> reading level."

Expected: `writing-skills:adams-plain-grade` owns accessible-register asks (5th-grade
target). Loading adams-smart-brevity here means the audience boundary between the two
Adams skills is failing.

## 2b. Near-miss (prompt-architecture guard)
> "Build me a master prompt for a reconciliation agent — full persona, constraints,
> output format."

Expected: `coding-agent-skills:master-prompt-architect` owns end-to-end master-prompt
construction (its own Adams compliance audit applies there). This skill should not load as
the primary; its rules reinforce that skill's audit rather than replace it.

## 3. Quality rubric
- **Does**: leads with the one most important point + "why it matters"; every sentence
  passes the Adams check (no ambiguity, no doublets, consistent terms, tight SVO); flags
  litigated phrasing with a modern alternative; scannable format; stops when done.
- **Teaches**: why litigated language is a failure history, not a warranty; the categories
  of contract language and why "shall" leakage creates ambiguity; why precision and brevity
  compose rather than trade off.
- **Stays honest**: never invents clinical facts, consent language, or legal conclusions;
  in reviews, diagnoses before fixing; keeps meaning exactly intact through every rewrite.
