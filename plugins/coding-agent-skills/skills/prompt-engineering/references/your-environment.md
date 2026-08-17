# Your prompting environment (sanitized template)

Fill in your real specifics. Keep proprietary prompt content and real customer data in
`your-environment.private.md` (git-ignored). Commit only sanitized structure here.

Mechanism support changes by model generation, so record **when you last checked** each line against
the provider's own reference rather than treating it as settled.

- **Models / runtimes:** <which model(s), which SDK or platform — and the date each was verified>
- **Output contract mechanism:** <schema-constrained output available? forced-tool-call schema?
  neither, so prompt-level shaping is the fallback? name the exact parameter you use>
- **Reasoning configuration:** <does this model have a thinking mode? is it on by default? which
  effort/depth setting do you run per route? what did you delete when you migrated?>
- **Sampling parameters:** <accepted, ignored, or rejected on your model? if rejected, note that
  variance is measured rather than switched off>
- **Caching:** <is prompt caching in use? where do the breakpoints sit? what is the minimum
  cacheable prefix on your model, and what is your cache-read rate today?>
- **Recurring task types you prompt for:** <e.g. classify tickets, extract invoice fields, summarize notes>
- **House output schemas:** <the exact JSON schemas / table shapes / bullet styles you standardize on>
- **Tone / audience conventions:** <who reads the output; required disclaimers or forbidden content>
- **Grounding sources:** <where the model gets facts from, native citations or prose quotes, and the
  "if not present, say so" rule>
- **Untrusted input surfaces:** <which inputs come from outside your trust boundary (web, email,
  retrieved docs, tool results, other users), which tools are exposed alongside them, and which
  actions require human confirmation>
- **Where eval cases live:** <folder/table of real inputs + known-good outputs, including known
  failures — and the repeat count you run per case>
- **Judging:** <who or what scores the outputs? if a model judges, has its agreement been qualified
  (repeat runs, second judge, human reference, agreement statistic)?>
- **Guardrails:** <length limits, banned outputs, PII handling — describe structurally, no real PII here>
- **Sign-off:** <who approves a prompt that touches customers, money, or a system of record>
