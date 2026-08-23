# Your ML environment (sanitized template)

Fill in your standing parameters so the intake gate starts from facts instead of questions you
have answered before. Keep anything sensitive — credentials, dataset contents, client specifics —
in `your-environment.private.md` (git-ignored). Never commit real data.

- **Compute budget and hardware:** <GPUs/TPUs available, cloud vs. on-prem, spend ceiling, spot vs. reserved>
- **Preferred stack:** <e.g. PyTorch, Hugging Face Transformers/PEFT/TRL, Axolotl, vLLM, llama.cpp>
- **Experiment tracking:** <W&B / MLflow / local — project naming conventions>
- **Data locations and formats:** <where training data lives, formats (JSONL, Parquet, …), size, licensing/provenance notes>
- **Base models you can use:** <licenses cleared, sizes, hosting constraints>
- **Latency / throughput targets:** <p95 latency, tokens/sec, batch vs. interactive>
- **Evaluation metrics that matter here:** <task metrics, plus any regression gates>
- **Safety and compliance requirements:** <data-handling rules, refusal policies, red-team expectations, human-escalation contacts>
- **Deployment target:** <serving stack, quantization constraints, monitoring hooks available>
