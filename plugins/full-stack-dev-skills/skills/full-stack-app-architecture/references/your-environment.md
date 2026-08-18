# Your architecture (sanitized template)

Fill in per app (copy the one-page template from architecture-decisions.md):

- **Stack and why:** <backend / frontend / db / hosting, one line each>
- **Layout:** <feature folders? deviations?>
- **Module boundaries:** <features and their public interfaces>
- **Config/secrets:** <settings object, secret mechanism>
- **Rendering split:** <htmx / React / hybrid, and where>
- **Split criteria on record:** <each one as measurement + threshold + where the number comes
  from — not "when we need to scale">
- **Boundary enforcement:** <where the import test lives; the allowlist file and its current
  line count, if you are mid-migration>
- **Config inventory:** <every variable: name, type, secret or not, default — and confirmation
  that .env.example matches the Settings fields exactly>
- **Per-tenant values:** <which table holds behaviour that differs per customer, so the next
  request for one does not become an env var>
- **Shared-kernel baseline:** <platform lines / feature lines, with the date — the direction of
  this ratio is the early warning that the layout is reverting to layer-first>
- **Known debt:** <where the current shape violates the rules, and the plan or the explicit,
  attributed acceptance>
