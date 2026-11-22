# ex-redteam (private)

> **Extrapolate-internal. Private repo only.** Task designs, hidden task cards, desk verdicts and method drafts. Do not make the repo public, fork it publicly or share it outside the team without Amita's approval (bar F4).

A **task-agnostic** desk red-team pipeline for RL research tasks. Any task that provides a `task.yaml` and its referenced files runs end to end through one installable CLI:

```
redteam run <task_dir>
```

**New here? Read [GETTING_STARTED.md](GETTING_STARTED.md).** It walks through install, adding a task, and every command and gate.

## What we run, why, and what comes out

**What:** one command, `redteam run <task_dir>`, which puts an LLM desk reviewer (Codex by default, or `stub` for tests) through a fixed sequence of review stages for one task. It reads the task card, the grader interface and the cited sources. It does **not** train models or run rollouts.

**Why:** to kill tasks that a frontier solver (roughly 10T parameters, 12 hours of compute) would saturate, and to find reward hacks *before* anyone spends GPU time building or evaluating a task. A desk review can kill a task but can never clear it. Only measured rollouts can clear one, and those are gated off.

**Output:** for each stage, a folder `runs/<task>/v<version>/<run_id>/<stage>/` holding `prompt.md` (exactly what the reviewer saw), `out/` (its answer), `run.yaml` (verdict, model and input hashes) and logs. There is also one row per stage in `runs/INDEX.tsv`, and `redteam report <task>` prints a markdown summary. Every verdict is labelled **ESTIMATED desk verdict, UNMEASURED**.

| # | Stage | What it asks | Verdict |
|---|---|---|---|
| 1 | `validate` | Is `task.yaml` complete and well formed (`schema/task.schema.json`)? | pass / fail, listing every problem |
| 2 | `screen` | Would a strong lawful solver cross the kill lines? | PASS-SCREEN / CONDITIONAL / CUT |
| 3 | `anchored_rescore` | Rescore anchored to demonstrated agent results | upper bound only |
| 4 | `strict_gate` | **The promotion gate.** Only agent-demonstrated evidence can lower an attack. Literature-only and assumed attacks keep their pre-anchoring scores. | PASS / CONDITIONAL / CUT |
| 5 | `redteam` | An independent reviewer, blind to the earlier verdicts, attacks the task lawfully | HOLDS / FIX / CUT |
| 6 | `probe_blackbox` | Exploit probe: hunt for reward hacks without the grader source | findings list |
| 7 | `probe_whitebox` | Exploit probe: the same hunt with the grader source read-only | findings list |
| 8 | `aggregate` + `index` | Combine into one outcome and update `runs/INDEX.tsv` | final outcome |

`canary` and `panel` (real rollouts) are switched off in `config/runner.yaml`. They refuse to start without a recorded GO.

## Black-box vs white-box

There are two kinds of attacker, and they answer different questions.

| | Lawful attacker (stages 2-5) | Black-box exploit probe (6) | White-box exploit probe (7) |
|---|---|---|---|
| Question | Can a solver legitimately saturate the task? | Can it cheat using only what a solver sees? | Can it cheat if it reads the grader code? |
| Sees | Task card, grader interface, allowed resources | The same | The same, **plus grader source, scoring code and config (read-only)** |
| Never sees | Grader source, hidden data | Grader source, hidden data | Hidden or test data and secret seeds (unless explicitly listed as exposed) |
| Goal | Maximise score by doing the research; any exploit is logged, not used | Score high **without** doing the research | Find grader bugs: fail-open branches, clipping or off-by-one errors, cacheable randomness, parse tricks, paths to hidden data |
| Counts toward saturation? | **Yes** (single run, best-of-4, pass@4, upper 95% bound) | **No.** Findings go to the environment fix list | **No.** Findings go to the environment fix list |
| Output | Scores and a verdict | Findings tagged `mode=blackbox` (reproduction, score, severity, fix, and which defences held) | Findings tagged `mode=whitebox`, plus the grader code location |

By default each task gets one probe of each kind (`probe_modes` in `config/runner.yaml`). The lawful attacker is always black-box. Probes run in a disposable copy of the task with no real credentials, and they stop and report if they reach a real secret. The full prompts are in `method/attacker_prompt.md` (Parts A and B for the lawful attacker, Parts C1 and C2 for the probes).

**Blindness is enforced:** each stage gets an isolated workdir containing only its allowed inputs, sandboxed with `bwrap` when it is available. Without `bwrap` the stage falls back to copied folders, and the run log records that.

## Everything here is an estimate
- Every verdict is an ESTIMATED desk verdict, UNMEASURED (an LLM judgement). No rollout, canary or panel is run.
- A 4x4 panel can kill a task but cannot clear it (`method/kill_thresholds.md`): even 0/16 still leaves pass@4 <= 0.602 at 95%.

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
