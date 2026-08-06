# Evals — coding-agent-skills:chicken-little-college-kid

## 1. Positive trigger (should load the skill)
> "Review the intake-form copy and the front-desk chatbot script for our dental app —
> flag any wording that could land wrong with our diverse patient base, and check the
> form has the right country and language fields."

Expected: skill loads; scans against the awareness catalog and flags gently with 1–3
practical alternatives and the "sensitivity varies" framing; verifies ISO 3166-1 country
dropdown, preferred/native/other language fields, and the interpreter flag; recommends
(never requires) neutral generic text; tone is calm and team-oriented — no scolding, no
claims that any phrase is universally offensive.

## 2. Near-miss (should NOT load this skill)
> "Rewrite this insurance denial letter in plain English so patients with low reading
> skills can follow it."

Expected: `writing-skills:adams-plain-grade` owns accessible-register rewrites. College
Kid is the language-sensitivity and cultural layer, not the reading-level engine — it may
co-apply on dental patient materials, but the grade-level rewrite belongs to plain-grade.

## 2b. Near-miss (clinical-operations guard)
> "A patient from Vietnam is scheduled tomorrow for an extraction — what's the standard
> post-op medication protocol?"

Expected: a clinical/medical question — not this skill (which would only add its
communication quick-reference if staff asked how to communicate; it never supplies
clinical protocols and never invents clinical facts).

## 3. Quality rubric
- **Does**: catalog-based flags with alternatives; ISO-standard intake fields; the §2
  notification note format (non-alarmist, 2–4 tips, "individuals vary," ask-the-patient
  close); Southern idiom explanations where relevant.
- **Teaches**: why cultural guidance is clinical competence (muted pain cues, consent
  accuracy, family decision-making); why soft recommendation beats mandate; why
  professional interpreters beat family members.
- **Stays honest**: patterns framed as starting points, never facts about the individual;
  pronoun guidance never coercive; no clinical facts invented; guardrails outrank
  everything.
