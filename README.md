# AI Evaluation & Agent Lab

A reproducible AI systems lab for **bounded agents, structured outputs, tool-path evaluation, traces, fixed datasets, and regression gates**.

## 30-second read

The important unit is not “did the model produce a good sentence?” It is the **system trace**: what context was used, which tool was called, how many steps occurred, and whether the final result satisfies the task contract.

This repo includes a deterministic/mock mode so the evaluation suite does not require a paid model API.

## Run it

- [GitHub Codespaces](https://codespaces.new/MountainBridge/AIEvaluationAgentLab) — full environment.

```bash
python -m unittest discover -s tests
PYTHONPATH=src python src/evaluate.py
```

## Evaluation model

1. Fixed dataset defines expected behavior.
2. Agent produces a bounded trace.
3. Evaluator checks both final answer semantics and tool path.
4. CI fails when a regression is introduced.
5. Production traces can later become new regression cases.

## Why LLM-as-a-judge is not enough

A judge can score a final answer highly even when the agent used the wrong tool, stale context, excessive steps, or an unsafe path. The lab therefore treats **trajectory/tool-path correctness as first-class evidence**.

## Next extensions

- Add an actual model adapter behind a stable interface.
- Add JSON Schema structured output validation.
- Add cost/latency/token telemetry.
- Add MCP tool boundary with least-privilege authorization.
- Add judge calibration and human agreement measurement.
- Add trace replay and golden regression datasets.
