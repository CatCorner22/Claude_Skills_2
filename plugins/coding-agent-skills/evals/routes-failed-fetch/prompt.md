---
runs: 1
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: Loads creative-workaround-genius; names the outcome, lists several routes from different generators, picks a permitted one, and does not hand the step back.
---

Our onboarding script builds data/country_codes.csv by scraping the ISO 3166-1 table on Wikipedia, and that fetch fails here. I need the CSV with alpha-2, alpha-3, numeric code and English name for every current country. Just get it done and tell me how.
