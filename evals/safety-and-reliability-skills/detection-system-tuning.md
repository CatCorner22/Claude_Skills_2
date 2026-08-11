# Evals — safety-and-reliability-skills:detection-system-tuning

## 1. Positive trigger (should load the skill)
> "Our team's exception queue is drowning us — hundreds of items a week, and honestly
> nobody looks at the alerts anymore. Last month a real problem sat in there for nine days.
> Don't build us a fancier detector; help us tune the whole thing so the queue means
> something again."

Expected: skill loads; asks for (or asks the user to start recording) a period of firings
with dispositions; computes per-rule empirical autoimmunity rates and ranks by flood
contribution; attacks defaults before proposing smarter detectors (cites the Boston Medical
Center default-recalibration result with its provenance mark, not rounded); assigns rules
to layers (log/digest/queue/page); gates paging on a danger signal (anomaly AND damage
evidence); drafts tolerance-list entries with evidence counts and expiry dates, suppressed
at the source; proposes memory cells for the incident that sat nine days; replays any
threshold change against the historical firings before recommending it go live; schedules
the re-audit and names the fuel-load risk of unreviewed suppression; leaves suppression
decisions and expiry dates to the human as explicit risk acceptances.

## 2. Near-miss (detector-building guard)
> "I've got a table of transactions and I want to flag unusual ones — can you set up an
> isolation forest or a robust z-score and pick a sensible threshold for the alerts?"

Expected: `machine-learning-skills:anomaly-detection` owns building detectors, method
choice, and threshold statistics for a single detector's output (including its
alert-fatigue concern). detection-system-tuning operates the layered system *around*
detectors from any source — queue economics, disposition audits, tolerance, memory
formation — and should route there rather than load. If it loads on a build-me-a-model
ask, the seam is failing.

## 2b. Near-miss (single-alarm diagnosis guard)
> "One of our monitors fired at 2 a.m. Tuesday and we still don't understand why — walk me
> through figuring out what actually caused it."

Expected: `continuous-improvement-skills:root-cause-analysis` owns diagnosing why one
alarm/incident happened. detection-system-tuning is population-level (rates, floods, queue
economics), not one causal chain, and should not load.

## 3. Quality rubric
- **Does**: produces per-rule autoimmunity rates from real dispositions (or installs the
  one-line disposition log first); ranks by flood contribution and works the top rules;
  recalibrates defaults before adding smarts; assigns explicit layers; writes the paging
  gate as anomaly AND danger signal, with the queue service level named as the coverage
  fallback; tolerance entries carry pattern, source-level suppression, evidence count,
  approver, and expiry; every true incident yields a memory-cell rule with a specificity
  argument and a replay check; every threshold change is simulated against historical
  firings with a must-catch list before going live; a re-audit date exists.
- **Teaches**: the autoimmunity/immunodeficiency axis and why a flooded queue is
  functionally immunodeficient; why operator desensitization — not the missing detector —
  is the documented killer; why cost must scale with evidence (innate before adaptive);
  why danger theory gates the page tier (anomalous is not harmful); why tolerance without
  expiry is fuel accumulation (suppression bias; error budgets as the practice-level
  twin); why a true incident must be converted into a memory cell to repay its cost.
- **Stays honest**: the load-bearing numbers are quoted exactly with their provenance
  marks — Joint Commission Sentinel Event Alert 50 (98 alarm-related adverse events
  2009–2012, 80 deaths, 85–99% non-actionable) [snippet-only]; Boston Medical Center's
  89% pilot / 60% hospital-wide reduction via default recalibration, no missed events
  reported [snippet-only]; SOC false-positive/burnout figures [snippet-only]; the AML
  90–95% benchmark stated as industry-attributed [snippet-only] — never rounded into new
  claims; worked-example numbers labeled illustrative; boundaries respected — detector
  building to anomaly-detection, SPC/control charts to dmaic-problem-solving and
  lean-six-sigma-for-software, metric trust to measurement-systems-analysis, one alarm's
  cause to root-cause-analysis, post-page response to break-glass-playbooks and
  deploy-and-operate.
