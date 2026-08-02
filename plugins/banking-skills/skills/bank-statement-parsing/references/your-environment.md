# Your bank-statement-parsing environment (sanitized template)

Fill in your real setup. Keep real statement files and account numbers in
`your-environment.private.md` (git-ignored) — commit only structural notes and a
redacted sample layout.

- **Formats received (by bank):** <BAI2 / MT940 / MT942 / CAMT.053 / CAMT.052 / CSV>
- **Feed timing:** <prior-day vs intraday; delivery times; delivery channel>
- **Balance codes in use:** <e.g. BAI 010/015/040/045; how you map them>
- **Transaction / type codes you care about:** <BAI type codes; your code map group>
- **Sign / direction convention:** <how credits/debits are encoded in your files>
- **Target schema:** <the normalized columns you map into: date, amount, direction, reference, description, balance>
- **Redacted sample:** <paste a scrubbed few lines of a real file>
