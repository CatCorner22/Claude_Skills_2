# Evals — writing-skills:explanation-design

## 1. Positive trigger (should load the skill)
> "I need to explain database indexing to our new paralegals so they understand why some
> case-search queries are instant and others take minutes. They're smart but have never touched
> SQL — make this intuitive, and give me an analogy that won't mislead them later."

Expected: skill loads and designs the explanation rather than transcribing expertise. It writes
the one-sentence audience model first (a new paralegal who knows legal reference books and needs
to understand query speed); generates 2–3 candidate analogies from domains that audience owns
and, for the chosen one (e.g., a back-of-book index), maps the source→target correspondences AND
marks the breaks — especially that a book's index is printed once while a database index must be
updated on every write — stating the top break inside the explanation itself; orders the
material concrete-first (walk one real search as a full scan, then via the index, then the
principle, then boundary cases), never definition-first; runs a Feynman pass flagging jargon and
hand-waves as the author's gaps, labeling the method honestly as distilled from accounts of
Feynman's practice; strips curse-of-knowledge tells ("simply," undefined abbreviations, skipped
steps — Pinker's framing); and closes with a teach-back plan, offering to simulate the newcomer
and the teach-back itself.

## 2. Near-miss (should NOT load this skill)
> "Rewrite this patient billing letter at a 5th-grade reading level — keep the meaning exact,
> just make it easy to read."

Expected: `writing-skills:adams-plain-grade` owns register and grade-level rewriting. The letter
already says what it needs to say; the ask is accessible wording, not the design of an
explanation for building new understanding. If explanation-design loads on a readability
rewrite, its description is over-triggering.

## 2b. Near-miss (closer — should NOT load this skill)
> "Tighten this project update for the leadership channel — most important point first, why it
> matters, scannable bullets, cut everything nonessential."

Expected: `writing-skills:adams-smart-brevity` owns attention-first professional structure. The
readers already have the background; the job is helping a busy reader decide and act, not
building a newcomer's understanding. "Make it land" language can sound like explanation work,
but no concept is being taught.

## 2c. Near-miss (should NOT load this skill)
> "I finally understand how hearsay exceptions work, but I keep forgetting them after a few
> weeks. Set me up with a retention schedule so it sticks."

Expected: `learning-skills:spaced-retrieval-learning` owns making understood material stick over
time. Explanation-design gets a concept in; retention scheduling keeps it there. (If that skill
is not yet installed, the response should still not load explanation-design for this ask.)

## 3. Quality rubric
A good response:
- **Does the task:** writes the audience model before any content and checks terms and depth
  against it; produces candidate analogies with an explicit correspondence map and a ranked
  break list, marking the top break inside the explanation itself rather than a footnote;
  orders worked example → general principle → boundary cases; runs the Feynman loop as a
  gap-finding procedure (marked stumbles reattributed to the author, re-learning named) rather
  than a style rewrite; sweeps the specific curse-of-knowledge tells and rewrites them; and
  verifies by generation — a teach-back with a transfer case and an analogy-edge probe — with
  distortions mapped back to passages of the explanation.
- **Teaches:** explains why definition-first fails (a definition is a compression of
  understanding the reader doesn't yet have), why generating an explanation is a stronger test
  than recognizing one, why analogies are load-bearing and dangerous in proportion (they
  transfer an inference engine whose warranty the reader can't see), and why the curse of
  knowledge is a systematic bias fixed by procedure, not intention.
- **Stays honest:** labels the Feynman technique as posthumously distilled from accounts of
  Feynman's practice, not a protocol he wrote; credits the curse-of-knowledge framing to Pinker;
  invents no statistics or research claims; keeps the audience-model and final analogy choices
  with the human; and treats a simulated teach-back as a filter, stating plainly that a real
  learner is the final test.
