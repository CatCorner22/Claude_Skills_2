# Frontmatter rules (full reference)

## Required fields

### `name`
- 1–64 characters.
- Lowercase letters, digits, and hyphens only.
- No leading, trailing, or consecutive hyphens.
- **Must equal the skill's folder name exactly.**
- Must **not** contain the reserved words `anthropic` or `claude`.
- Must not contain XML tags.
- Prefer gerund-ish or plain task names (`after-action-review`, `percentages-and-proportions`).
  Avoid vague names (`helper`, `utils`, `tools`, `data`).

### `description`
- Non-empty, **maximum 1024 characters**.
- **Third person** (it is injected into the system prompt; first/second person hurts discovery).
- States **both** what the skill does **and** when to use it.
- Leads with the primary use case; ends with a short `Triggers:` list of literal phrases.
- Slightly "pushy" to avoid under-triggering, but specific enough not to over-trigger.
- Must not contain XML tags.
- **Budget reality, re-measured 2026-08-18 (this replaces an earlier ~1%-of-context claim that the
  library's own numbers contradict).** 121 skills' names + descriptions = **≈110,000 chars ≈
  29,700 tokens ≈ 14.9% of a 200K window**, mean ~890 chars per description. Token figures are an
  estimate at ~3.7 chars/token — stated, because an undisclosed divisor is exactly how this
  paragraph and `README.md` came to publish two different percentages. That character estimate
  is also ~30% light against the harness's real tokenizer, which puts the true listing cost at
  **≈38,800 tokens ≈ 19.4% of a 200K window** (`claude plugin details <plugin>` summed across all
  14 plugins; see `docs/live-routing-and-degradation-2026-08-18.md`) — quote that one when the
  size of an install is the point. Both character figures come from
  `python3 scripts/measure-listing-cost.py`; re-run it rather than editing the figure by hand,
  because a hand-kept number in two places is a number that will disagree with itself again. A literal
  1%-of-context listing budget is 8,000 characters, and `scripts/simulate-listing-budget.py` reports
  that it keeps **three** full descriptions here once the 121 bare names are paid for, so ~1% cannot
  describe a full-description listing; it is consistent instead with a listing that has degraded to mostly
  **name-only**, which is the documented failure mode (see below). Keep descriptions tight
  because a tight description routes better — not because trimming fixes the budget. The lever
  that moves real tokens is how many plugins a user installs.
- **The listing degrades silently at scale.** Observed at ~100 installed skills: least-used
  skills' descriptions are trimmed to name-only. There is no error; `/plugin:skill` direct
  invocation still works. So a skill can be fully valid, fully conformant, and unroutable, and
  the author cannot tell from inside their own session. This is why the fresh-session trigger
  test in `review-checklist.md` is the only check that proves a description works.
- A per-skill truncation ceiling (~1536 chars for `description` + `when_to_use` combined) has
  been reported for Claude Code, but it is **not** the binding constraint here: this library's
  1024-char cap is stricter, and no skill in it uses `when_to_use` at all.

## Optional fields used in this library
- `when_to_use`: extra trigger phrases appended to the description (use sparingly).
- `license`, `metadata`: portable extras from the open spec. Put a `version` inside `metadata`
  if you want per-skill versioning (there is no standard top-level `version` for a skill).

### The `metadata` house convention (adopted 2026-08; apply to new and touched skills)
New skills, and existing skills whenever they get a substantive revision, carry:

```yaml
metadata:
  version: "1.0.0"          # bump minor on content revision, patch on typo-grade fixes
  source: >-                # OPTIONAL — only when the skill is built from external research
    One or two sentences naming the research dossier or external spec the skill was built
    from, plus the provenance-mark legend if claims carry marks ([snippet-only] etc.).
```

Do not mass-retrofit untouched skills — the convention rides along with real edits so
diffs stay reviewable. `metadata:` is a bare key on its own line; both `scripts/validate.sh`
and `scripts/gen-catalog.py` handle it (the catalog parser bug that leaked bare keys into
descriptions was fixed 2026-08-11 — keep the key bare, no inline value).

## Claude-Code-only fields (use only for skills that will never run outside Claude Code)
`argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`,
`disallowed-tools`, `model`, `effort`, `context: fork`, `agent`, `paths`, `hooks`, `shell`.
Other agents ignore or may choke on these — keep them out of portable skills.

## YAML tips
- Use a block scalar (`>-`) for multi-line descriptions so they fold to a single line.
- Keep the frontmatter valid YAML: quote values containing colons.
