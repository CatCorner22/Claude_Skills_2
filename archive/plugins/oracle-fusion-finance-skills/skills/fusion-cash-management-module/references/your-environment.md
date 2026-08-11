# Your Fusion Cash Management environment (sanitized template)

Fill in your real setup. Account numbers, IBANs, and statement files stay in
`your-environment.private.md` (git-ignored).

- **Banks / branches / accounts:** <sanitized list: bank, currency, owning LE, purpose>
- **Statement format per bank:** <e.g. Bank A camt.053 v2, Bank B BAI2>
- **Delivery channel:** <UCM upload, H2H/SFTP, connectivity service; timing>
- **Intraday feeds:** <which accounts, camt.052/BAI2 intraday>
- **Transaction-code map:** <key codes → types you rely on>
- **Rule set order:** <your rules, strictest first, with tolerances>
- **External-transaction conventions:** <what gets created manually vs by creation rules>
- **GL cash / cash-clearing accounts:** <combinations per bank account, sanitized>
- **Auto-match rate benchmark:** <your normal %, so regressions stand out>
