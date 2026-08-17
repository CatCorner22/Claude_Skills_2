# Canonical Finding schema and chair report structure (reference)

Every specialist advisor must emit findings in exactly this schema; the chair normalizes,
merges, and ranks them. The orchestrator (the board-review skill) passes this file's rules
to each advisor with the review package.

## Contents
- The Finding schema
- Severity definitions
- Category definitions and ID prefixes
- The chair's report structure
- Noise caps

## The Finding schema
```markdown
### Finding
- **ID**: PREFIX-XXX
- **Location**: `path/to/file.ext:Lstart-Lend` (function name or character range where sharper)
- **Severity**: Critical | High | Medium | Low
- **Category**: performance | accuracy | structure | clarity | robustness
- **Issue**: Concise description of what is suboptimal and why it matters.
- **Evidence**: Code snippet + reasoning (complexity analysis, failure trace, etc.).
- **Proposed Revision**: Concrete, minimal, behavior-preserving change (prefer before/after code).
- **Impact on Goals**: Explicit preservation statement: "Preserves original goals because..."
- **Expected Gain**: Quantified where possible (speed: "O(n²) → O(n log n)"; accuracy: "fixes wrong results on X").
- **Confidence**: High | Medium | Low
- **Trade-offs**: Costs introduced (complexity, memory, migration effort, verbosity).
```

## Severity definitions
| Severity | Meaning |
|---|---|
| Critical | Produces wrong results now, or a crash/corruption path on realistic inputs |
| High | Likely wrong results on plausible edge inputs, or a major performance cliff on the hot path |
| Medium | Meaningful gain or risk-reduction available; not currently causing damage |
| Low | Worth noting; fix opportunistically |
Accuracy findings that can produce incorrect results are Critical or High by definition.

## Category definitions and ID prefixes
| Category | Prefix | Owner advisor |
|---|---|---|
| performance | PERF- | performance-advisor |
| accuracy | ACC- | accuracy-correctness-advisor |
| structure | STR- | structure-architecture-advisor |
| clarity | CLR- | clarity-maintainability-advisor |
| robustness | ROB- | robustness-edgecase-advisor |
The chair's merged revisions use R-XXX and cite the source IDs they merge.

## The chair's report structure
```markdown
# Board of Advisors – Optimization Review
## Goals Restatement
## Findings Summary            (total after dedup; by severity; by category)
## Prioritized Proposed Revisions
### Revision R-XXX (from original IDs ...)
  Location / Primary Category / Severity / Issue / Proposed Change /
  Expected Gain / Goal Preservation Check / Trade-offs / Confidence /
  Recommended Verification
## Implementation Order Recommendation
## Residual Risks & Items Intentionally Deferred
## Next Steps
```
Priority order (strict): (a) Critical/High accuracy → (b) goal-preserving high-impact
performance → (c) structure that unlocks speed or protects accuracy → (d) robustness of
speed/accuracy under real conditions → (e) clarity that reduces future accuracy risk.

## Noise caps
- Specialists: top 8–12 findings each; "No significant <domain> issues found." is a valid,
  preferred response when true.
- Chair: roughly ≤15–20 ranked revisions; merge duplicates; drop low-value items into
  "Intentionally Deferred" with one line of why.
- Nobody invents findings during synthesis — merge, reframe, or drop only.
