# Prompt patterns and failure modes

Reusable structures and the fixes for the failures you'll actually hit. Provider-agnostic: the wording
knobs differ across models, but the shapes below transfer. Confirm your model's specific features
(system-message support, structured-output/JSON mode, temperature control) separately.

## Contents
- A reliable prompt skeleton
- Few-shot examples
- Output-format control
- Grounding to reduce hallucination
- Reasoning for hard tasks
- Failure modes → fixes
- Iteration loop

## A reliable prompt skeleton
Order these; keep instructions and data visibly separate.
```
Role/goal:   You are <role>. Your job is <task> for <audience>.
Instructions: 1) ... 2) ... 3) ...   (numbered, imperative)
Context:     <definitions, constraints>
Input:       <<< the document/data to act on, clearly delimited >>>
Output:      Return <exact format>. If <value> is missing, <what to do>. Do not include <X>.
Examples:    <2–5 input→output pairs, if format/style matters>
```
Putting the data in a delimited block (fences, tags, headers) stops the model from confusing *what to
process* with *what to do*.

## Few-shot examples
- Use 2–5 examples; more helps most when the task is stylistic or has tricky edge cases.
- Make examples cover the hard cases: an empty field, an ambiguous input, the "say you don't know" case.
- Keep the example outputs in *exactly* the format you want back — the model copies their shape.
- Inconsistent examples teach inconsistency; make them uniform.

## Output-format control
- State the structure explicitly and show one instance of it.
- For machine-readable output: "Return only valid JSON matching this shape, no prose:" + the shape.
- Say what to emit for missing/unknown values (`null`? `"unknown"`? omit the key?).
- If the model keeps adding a preamble, add "Output only the JSON, nothing before or after" and an example.

## Grounding to reduce hallucination
- Supply the source material in the prompt and instruct: "Answer using only the provided context."
- Add the escape hatch: "If the answer isn't in the context, say you don't know." Without it, models fill gaps.
- Ask for citations/quotes back to the source when you need to verify.

## Reasoning for hard tasks
- For genuine multi-step reasoning, allow the model to work through steps before the final answer.
- When you need a clean final output *and* reasoning, ask for the reasoning first and the answer last in
  a labeled field you can extract — don't force a terse answer on a hard problem.
- Don't add "think step by step" reflexively to simple formatting tasks; it just adds noise and cost.

## Failure modes → fixes
- **Wrong / unspecified format** → specify structure exactly; add an example of the target format.
- **Ignores an instruction** → move it earlier, make it explicit and imperative, or demonstrate it in an example.
- **Inconsistent across runs** → add structure + examples; remove ambiguity; lower temperature if you control it.
- **Hallucinated facts** → ground in provided context; add "if not present, say you don't know."
- **Too verbose / chatty** → "Output only <X>." Set a length limit. Show a concise example.
- **Fails only on edge cases** → add those exact edge cases as few-shot examples.
- **Does part of the task** → decompose; number the steps; or split into separate prompts.

## Iteration loop
1. Gather real inputs, including current failures, with a known-good output for each.
2. Change **one** thing.
3. Run the whole set (not just the example you're staring at).
4. Keep the version that wins across the set; note what the change was for.
5. Repeat. When the set passes, freeze it as a regression check for future edits.
