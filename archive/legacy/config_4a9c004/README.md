# config/runner.yaml

One config drives the desk pipeline:

1. **screen**: a CPU-only desk saturation screen of a task card against the kill lines.
2. **anchored re-score**: re-estimates the attack under the evidence grounding rule (DEMONSTRATED-AGENT / LITERATURE-ONLY / ASSUMED), recording subfield SOTA and the gap. `gate_rule: strict` is the promotion gate: LITERATURE-ONLY and ASSUMED attacks use the evidence-only / pre-anchoring verdict; only DEMONSTRATED-AGENT evidence may lower an attack score. The anchored verdict is recorded as an upper bound (`anchored_upper_bound: true`).
3. **red team**: an independent adversarial review (it must not read earlier verdicts). Possible verdicts are HOLDS, FIX and CUT.
4. **canary** and **panel**: rollout stages. Both are **disabled** (`enabled: false`, `gates: OFF`) and require Amita's GO. Their procedure is `method/rollout_spec.md`.

No runner is included. Earlier runs used per-job Codex sessions supervised by a watcher: at most N concurrent sessions, stall detection on session-log idle time, and resume of the same session up to 4 times. Each stage writes one `run.yaml` per task in the shape of `method/verdict_schema.yaml`. `tools/import_runs.py` shows how the existing records were mapped.
