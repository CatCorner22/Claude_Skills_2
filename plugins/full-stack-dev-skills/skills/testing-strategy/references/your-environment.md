# Your testing setup (sanitized template)

- **Fixture spine:** <conftest location; test DB engine dev vs CI; sync or async plumbing>
- **Which tests require the production engine:** <constraints, migrations, locking, dialect>
- **Isolation canary:** <where the two canary tests live; last time they were seen to fail>
- **Money-path E2E list:** <the flows that must never break, each one sentence>
- **External boundaries mocked:** <service → mock approach>
- **Suite budgets:** <unit+API target seconds; E2E stage cap>
- **Bug-test convention:** <where regression tests live; naming>
- **Explicit don't-test list:** <your additions to the defaults>
