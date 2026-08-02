# Your prompting environment (sanitized template)

Fill in your real specifics. Keep proprietary prompt content and real customer data in
`your-environment.private.md` (git-ignored). Commit only sanitized structure here.

- **Model / runtime:** <which model(s), which SDK or platform — confirm current version/features>
- **Provider features you use:** <system message? temperature/top-p control? structured-output/JSON mode?>
- **Recurring task types you prompt for:** <e.g. classify tickets, extract invoice fields, summarize notes>
- **House output formats:** <the exact JSON schemas / table shapes / bullet styles you standardize on>
- **Tone / audience conventions:** <who reads the output; required disclaimers or forbidden content>
- **Grounding sources:** <where the model gets facts from, and the "if not present, say so" rule>
- **Where eval cases live:** <folder/table of real inputs + known-good outputs, including known failures>
- **Guardrails:** <length limits, banned outputs, PII handling — describe structurally, no real PII here>
