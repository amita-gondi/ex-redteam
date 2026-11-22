# ex-redteam (private)

> **AIUC-internal. Private repo only.** Task designs, hidden task cards, desk verdicts and method drafts. Do not make the repo public, fork it publicly or share it outside the team without Amita's approval (bar F4).

A **task-agnostic** desk red-team pipeline for RL research tasks. Any task that provides a `task.yaml` and its referenced files runs end to end through one installable CLI:

```
redteam run <task_dir>
```

**New here? Read [GETTING_STARTED.md](GETTING_STARTED.md).** It walks through install, adding a task, and every command and gate.

## What `redteam run` does
It runs these desk stages in order, writing one record per stage under `runs/<task>/v<version>/<run_id>/<stage>/`:

1. **validate** - `task.yaml` against `schema/task.schema.json`; fails loudly, listing every problem.
2. **screen** - a desk saturation screen against the kill lines -> PASS-SCREEN / CONDITIONAL / CUT.
3. **anchored_rescore** - re-score anchored to demonstrated agent results (`method/evidence_grounding_rule.md`).
4. **strict_gate** - the **promotion gate** (Amita, Nov 21 2026). LITERATURE-ONLY / ASSUMED attacks use the evidence-only (pre-anchoring) scores; only DEMONSTRATED-AGENT evidence may lower an attack. The anchored verdict is kept as an **upper bound** on survival, never the gate.
5. **redteam** - an independent adversarial review (blind to prior verdicts) -> HOLDS / FIX / CUT.
6. **probe_blackbox** + **probe_whitebox** - desk exploit probes (black-box, then white-box with the grader source read-only). Findings are tagged by mode and **never counted toward saturation metrics**.
7. **aggregate** + **index** - the combined verdict, then the `runs/INDEX.tsv` upsert.

**canary** and **panel** (rollouts) are gated OFF and the CLI never launches rollouts (`config/runner.yaml`).

## Everything here is an estimate
- **Every verdict is an ESTIMATED desk verdict, UNMEASURED** (an LLM judgement). No rollout, canary or panel is run.
- A 4x4 panel can **kill** a task but cannot **clear** it (`method/kill_thresholds.md`): 0/16 still leaves pass@4 <= 0.602 at 95%.
- The desk model backend defaults to the Codex CLI; a `stub` backend drives the tests and examples.

## Layout
```
README.md GETTING_STARTED.md
pyproject.toml Makefile .github/workflows/ci.yml
redteam/          the installable package (CLI, pipeline, gate, blindness, checks, backends)
schema/           task.schema.json (the task.yaml contract)
method/           attacker_prompt.md, rollout_spec.md, evidence_grounding_rule.md, kill_thresholds.md,
                  spec_notes.md, verdict_schema.{md,yaml}, prompts/ (stage prompts), refs/
config/           runner.yaml (the single pipeline config) + README
tasks/_template/  copy this to start a task
examples/toy_task/  a task that runs end to end with the stub backend
tests/            unit + end-to-end tests (make test)
tools/            secret_scan.sh
runs/             generated run records (git-ignored); INDEX.tsv
archive/          all imported history (ESTIMATED desk verdicts, UNMEASURED); see archive/README.md
```

## Quickstart
```bash
make install                                   # venv + editable install + dev deps
redteam validate examples/toy_task             # validate a task
redteam run examples/toy_task --backend stub --offline   # full pipeline with the fake agent
redteam status examples/toy_task               # see each stage's verdict
redteam report examples/toy_task               # a markdown summary of the latest run
make test                                      # unit + e2e tests (stub, offline)
```

## Hard rules
No GPU, no rollouts, no souping/merging, nothing shared or sent, no Doc writes, never commit secrets. Label every estimate ESTIMATED and every unmeasured quantity UNMEASURED. See GETTING_STARTED.md section "DO NOT".
