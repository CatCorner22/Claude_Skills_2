# Your EVOP candidates (sanitized template)

Fill this in with the live processes you would tune. If any value is sensitive (real rule names,
system identifiers, actual bounds), keep it in `your-environment.private.md` instead — that suffix
is git-ignored. Commit only sanitized, structural examples.

- **Process 1:** <e.g. auto-reconciliation matching>
  - Factors you can set: <e.g. amount tolerance, date window>
  - Improvement response + where measured: <e.g. auto-match rate, from the recon summary>
  - Guard response + hard limit + independent measurement: <e.g. false-match rate ≤ …%, from the
    audit pass>
  - Owner who sets limits and ratifies center shifts: <role>
  - Current operating center: <settings>
- **Process 2:** <e.g. cash-forecast model parameters — smoothing constants, driver weights;
  response: forecast error; guard: bias limit>
- **Process 3:** <e.g. dunning cadence — days-to-first-notice, escalation interval; response:
  days-to-pay; guard: sponsor-complaint / relationship limit>
- **Cycle unit and cadence:** <what one cycle is — a day, a statement file, a dunning batch — and
  how often the log is reviewed>
- **Known upsets to pause for:** <fiscal close, bank format changes, term start>
- **Where the EVOP log lives:** <path / sheet>
