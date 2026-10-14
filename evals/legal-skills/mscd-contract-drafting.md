# Evals — legal-skills:mscd-contract-drafting

## 1. Positive trigger (should load the skill)
> "Here's the services agreement the other side sent over. Can you go through it and tell me where
> the wording is ambiguous or could be tightened, and give me suggested replacements I can paste
> into a markup?"

Expected: the skill loads. It fixes the frame first (governing law, whether the instrument is under
negotiation — so contested items become flags), runs the linter and reads the `shall` ratio before
any finding, classifies sentences by category of contract language with the *has a duty to* test,
proposes replacements keyed to sections, **flags rather than cuts** anything in a risk-allocation
provision (*indemnify, defend and hold harmless*: *defend* is never cut) or in prescribed wording
(an all-capitals disclaimer is not de-capitalised), and delivers a Smart Brevity cover note that
leads with what changed and why it matters and lists what needs the reader's call. It says when a
position is Adams's rather than settled.

## 2. Near-miss A (should NOT load this skill)
> "Tighten this email to the client so it reads clearly and gets to the point."

Expected: `writing-skills:adams-smart-brevity` loads. Prose, not a contract. If this skill loads,
its contract vocabulary is reaching past its object.

## 3. Near-miss B (should NOT load this skill)
> "Rewrite this benefits summary so a new hire with no legal background can follow it."

Expected: `writing-skills:adams-plain-grade` loads. Accessible register for a non-lawyer; nothing to
redline.

## 4. Near-miss C (in-domain, must respect the rail — should load)
> "This indemnity says 'indemnify, defend, and hold harmless from any and all claims'. Clean it up
> to plain English."

Expected: the skill loads and **does not excise**. It explains that *defend* is a distinct and often
broader duty in many jurisdictions and that whether *hold harmless* adds anything is contested;
proposes the clearer version alongside the original with the risk of each cut; applies the safe
edits (*any and all* → *all*, structure, white space) as proposals; and routes the decision to a
lawyer in the governing jurisdiction. A response that simply returns "indemnify Acme from all
claims" is a **failure**.

## 5. Near-miss D (tests the category test — should load)
> "Is it right to say 'This Agreement shall be governed by Delaware law'? Something about it reads
> oddly."

Expected: the skill loads and answers with the test: an agreement cannot *have a duty to* be
governed, so this is language of policy and takes the present tense — *This agreement is governed
by Delaware law* — and it explains why `shall` is reserved for a party's duty.

## 6. Quality rubric
A good response:
- **Classifies before it edits**: every proposed change names the category (obligation, policy,
  discretion, declaration …) or the usage rule it applies.
- **Keys findings to sections** and distinguishes *edit* (apply as written) from *flag* (a decision).
- **Never cuts on its own authority** inside risk allocation or prescribed wording; proposes
  alongside and names the risk of each cut.
- **Marks contested positions as contested** (*represents and warrants*, *hold harmless*, efforts
  standards, *shall*/*must*).
- **Delivers Smart Brevity**: what changed, why it matters, what needs a call, what was left and why.
- **Teaches**: the *has a duty to* test and the reason behind at least one rule appear in the
  answer, so the reader can apply them next time.
- **Does not** invent governing-law facts, assert that litigated language is safe because it was
  litigated, or reformat a conspicuous disclaimer.
