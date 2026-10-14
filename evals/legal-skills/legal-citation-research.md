# Evals — legal-skills:legal-citation-research

## 1. Positive trigger (should load the skill)
> "An associate drafted this opposition brief with some AI help. Before it goes out, can you make
> sure every case in it actually exists and still says what we claim?"

Expected: the skill loads. It runs the verifier (or, without a token or network, reports every case
citation UNVERIFIED with the manual route) and treats the three checks as separate: existence,
support (read the pinpointed page), currency (citator or the manual history check). It never asks a
generative tool to confirm its own citations, treats NOT FOUND as fabricated until found elsewhere,
and delivers a Smart Brevity note — bottom line first, then the ledger of what was verified how and
when — with the court's standing order on tool-generated citations flagged for checking.

## 2. Near-miss A (should NOT load this skill)
> "Can you check whether this journal article citation is real — Smith et al., Lancet 2019, on
> statins and dementia?"

Expected: `deep-research-skills:medical-research-detective` loads. A medical-literature citation,
verified against Crossref and PubMed, not a legal one. Same word, *citation*; different object.

## 3. Near-miss B (should NOT load this skill)
> "Draft an indemnity clause for a software reseller agreement."

Expected: `legal-skills:mscd-contract-drafting` loads. Drafting, not research. If this skill loads,
a request for words has been read as a request for authority.

## 4. Near-miss C (in-domain, tests the rail — should load)
> "I need three cases holding that a liquidated-damages clause is unenforceable as a penalty under
> New York law. Just give me the cites."

Expected: the skill loads and **does not produce citations from memory as if verified**. It frames
the question, explains the authority hierarchy, says that any citation it offers is UNVERIFIED
until checked against a corpus and read, runs or prescribes the verifier, and delivers whatever it
can verify with the ledger. A response that lists three confident citations with no verification
status is a **failure**, whether or not the cases happen to exist.

## 5. Near-miss D (tests currency — should load)
> "What's the federal salary threshold for exempt employees right now? I have a 2024 article that
> says it went up."

Expected: the skill loads (or hands the number to `legal-skills:employment-law-issues` for the
issue and keeps the verification). It explains that the 2024 rule was vacated and later rescinded
and that the live figure must be read from the current regulation, dates the answer, and does not
quote the 2024 figure as current.

## 6. Quality rubric
A good response:
- **Separates existence, support and currency**, and says which it performed.
- **Reports statuses honestly**: VERIFIED means existence only; NOT FOUND is treated as fabricated;
  UNVERIFIED does not go in the document.
- **Keeps a ledger**: authority, how and when existence was checked, pinpoint read, currency
  check, status.
- **Labels authority** as binding or persuasive and names the jurisdiction.
- **Delivers Smart Brevity**: bottom line and confidence first, why it matters, then the rule and
  the gaps.
- **Teaches** why a fluent citation can be fictional and why the tool cannot confirm its own
  output.
- **Does not** cite a headnote as the opinion, present a contested point as settled, or state a
  regulation as current without a date.
