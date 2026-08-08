# Your experimentation environment (sanitized template)

Fill this in with your real setup. If any value is sensitive (real account structures, rule
configurations, live data), keep it in `your-environment.private.md` instead — that suffix is
git-ignored. Commit only sanitized, structural examples.

- **Responses you tune:** <e.g. auto-match rate; eval pass rate; close cycle time — and exactly
  how each is measured>
- **Candidate factors and authorized ranges:** <factor → low/high levels → who set the safety
  limit; e.g. tolerance width 0–$5, date window 1–5 days>
- **Where runs execute:** <test instance / statement-month copy / eval harness — never live
  production for designed bursts>
- **Replication convention:** <n seeds or repeats per cell for nondeterministic responses; which
  eval set or data month is the fixed test bed>
- **Blocking factors:** <what can't be randomized — data months, statement sources — and is
  blocked instead>
- **Noise factors for robustness runs:** <input mix, volume spikes, paraphrase sets, temperature>
- **Sign-offs:** <who authorizes factor levels; who decides whether results change production>
- **Records:** <where designs, run logs, and conclusions (with alias caveats) are kept>
- **Hand-off to live tuning:** <how a designed-experiment winner enters evolutionary operation:
  step sizes, monitoring, reversal criteria>
