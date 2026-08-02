# Your anomaly-detection setup (sanitized template)

Fill this in with your real setup. If any value is sensitive (real transactions, counterparties, amounts,
account identifiers, sample rows), keep it in `your-environment.private.md` instead — that suffix is
git-ignored. Commit only sanitized, structural examples.

- **What "anomalous" means here:** <e.g. a fee far above the rate card; a payment out of pattern; a recon break>
- **Fields monitored:** <amount, counterparty, GL account, channel, hour, currency, …>
- **Single-feature or multivariate:** <one quantity vs a combination of fields>
- **Time series involved?** <yes — series, frequency, seasonality; or no>
- **Labels available?** <none | a few confirmed cases | a labeled history>
- **Alert budget:** <how many alerts/day the team can investigate>
- **Cost of a missed anomaly vs a false alarm:** <business terms>
- **Known-benign recurring patterns to suppress:** <scheduled transfers, expected month-end movements>
- **Method preference / tooling:** <robust z / IQR, isolation forest, LOF; scikit-learn, PyOD>
- **Feeds which process?** <bank-reconciliation break ranking, controls review, fraud queue>
