# Your ML serving setup (sanitized template)

Never commit real prediction data or artifacts trained on sensitive data.

- **Models in production:** <model → serving pattern (batch/realtime) → owner>
- **Artifact store:** <where versioned artifacts live; promotion mechanism>
- **Feature code sharing:** <the module both training and serving import>
- **Prediction log:** <table/location; retention; sensitive-input hashing>
- **Drift monitoring:** <features watched, thresholds, alert channel>
- **Retrain triggers:** <schedule and/or drift conditions you committed to>
- **Rollback triggers:** <what flips the pointer back, and who may>
- **Rollout convention:** <shadow first? canary slice size?>
