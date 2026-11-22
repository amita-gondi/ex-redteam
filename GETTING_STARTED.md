# Getting started: running the red-team desk pipeline on YOUR task

> **AIUC-internal, private repo only.** Don't share this repo, its prompts or its run records with labs, GDM or anyone outside the team.

This repo runs a CPU-only desk pipeline on one RL-environment task, end to end, through a single installable CLI:

```
validate -> screen -> anchored re-score -> strict gate -> red team -> desk exploit probes (black-box + white-box) -> aggregate -> INDEX
```

The **strict** rule is the promotion gate (`config/runner.yaml` -> `gate_rule: strict`). The anchored verdict is an **upper bound** on survival (`anchored_upper_bound: true`), not the decision that advances a task. Nothing is trained or rolled out. The two rollout stages (canary, panel) are gated OFF and the CLI refuses to run them.

---

## 1. Prerequisites
| Need | Notes |
|---|---|
| Python 3.10+ | `python3 --version` |
| git | to commit your own task/run files on a branch |
| Codex CLI (`codex`) | Only for real desk runs (`--backend codex`, the default). Install it and log in with **your own** model access. Never commit credentials. Tested with codex-cli 0.163.0. Not needed for `--backend stub`. |
| bubblewrap (`bwrap`) | Optional but recommended: enables OS-level blindness (`isolation.mode: auto`). Without it the pipeline falls back to copy-only isolation. |
| GPU | **None.** Every stage is CPU/desk-only. |

```bash
make install          # creates .venv, installs the package (editable) + dev deps
# or: python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
```
After install the `redteam` command is on the venv's PATH (`.venv/bin/redteam`). Run it from inside the repo, or set `REDTEAM_ROOT=/path/to/repo`, or pass `--root`.

## 2. Add your task: `tasks/<id>/` from `_template`
```bash
cp -r tasks/_template tasks/MYTASK01
$EDITOR tasks/MYTASK01/task.yaml tasks/MYTASK01/card.md tasks/MYTASK01/grader_interface.md tasks/MYTASK01/sota_sources.md
```
`task.yaml` is the single contract (schema: `schema/task.schema.json`). Fill in, at minimum:
- **id / version / owner**; **title**.
- **card**: goal, start state, allowed resources, **network_allowlist**, compute budget, wallclock (default 12h), submission format, and the `card.md` prose.
- **grader**: `interface_file` (the black-box interface, shown to every stage) and `source_path` (the grader source, shown **read-only to the white-box probe only**; hidden data and secret seeds under `secret_globs` are withheld).
- **reward**: definition, frozen scale, R~1 reference, R~0 baselines, and `grader_noise` (`UNMEASURED` + a plan if not measured).
- **evidence**: >=1 agent-demonstrated result (model/scaffold/time/compute/gap/year/url) and the subfield SOTA with its year; or a `not_found_reason`.
- **known_lawful_recipes**, **hidden_data** (with a unique `canary_string`), **contamination** notes.
- `souping_dependency: false` (souping/merging is excluded entirely).

Then:
```bash
redteam validate tasks/MYTASK01      # lists EVERY missing/invalid field at once; exit 2 if invalid
```

## 3. Run the pipeline (CPU/desk only)
Always dry-run first. A dry-run prints each rendered prompt, the isolated workdir contents and the exact command, and writes nothing:
```bash
redteam run tasks/MYTASK01 --dry-run
```
Then run for real:
```bash
redteam run tasks/MYTASK01                 # full pipeline, Codex backend
redteam run tasks/MYTASK01 --backend stub  # dry pipeline with the deterministic fake agent (no cost)
```
Useful flags:
- `--stage screen` (repeatable) - run only some stages;
- `--resume` - continue the agent session of a stalled/partial stage;
- `--force` - re-run a stage fresh (the old attempt is kept under `<stage>/.superseded/`);
- `--continue-on-cut` - run the red team and probes even when the strict gate is CUT;
- `--run-id ID` / `--new-run`; `--model` / `--effort` / `--backend`; `--offline` (skip URL checks).

Re-runs are **idempotent**: a stage that is COMPLETE and whose inputs are unchanged is skipped.

## 4. Read the results
```bash
redteam status tasks/MYTASK01     # per-stage status + verdicts + checks
redteam report tasks/MYTASK01     # markdown report of the latest run
```
How verdicts map:

| Stage verdict | outcome |
|---|---|
| PASS-SCREEN / HOLDS | ADVANCE (the next stage may look at it; never "cleared") |
| CONDITIONAL / FIX | FIX |
| CUT | CUT |
| any interval touching a kill line | HOLD, not pass |

The **aggregate** outcome is the worse of the strict gate and the red team. Probe findings are reported separately (tagged by mode) and set `environment_fix_required`; they are never counted toward saturation.

Kill lines (`method/kill_thresholds.md`): single > 0.70, best-of-4 > 0.60, pass@4 at R >= 0.60 > 0.50, upper-95% >= 0.75. A task may override them in `task.yaml` **with a reason**.

## 5. Where outputs land
```
runs/<task>/v<version>/<run_id>/
  RUN.yaml                        run-level provenance (task hash, repo commit, kill lines, pairings, outcome)
  <stage>/
    prompt.md                     the exact rendered prompt (hash in run.yaml)
    run.yaml                      status, backend, prompt/inputs hashes, parsed record, verdict -> outcome,
                                  checks (wording/urls/independence), label "ESTIMATED desk verdict, UNMEASURED"
    out/<report>.md               the hand-written report (screen_card.md / audit_card.md / redteam.md / probe_*.md)
    out/DONE.txt                  written by the agent when finished
    codex_events.jsonl, codex.log raw session output (git-ignored; never commit)
runs/INDEX.tsv                    one row per (task, version, run, stage)
```
`runs/` is git-ignored: run records are local working state. Provenance in each `run.yaml` records the backend, model, effort, prompt hash, inputs hash, timings, and both `strict_verdict` and `anchored_verdict`, plus probe findings by mode.

## 6. Enforced blindness (how a stage is kept honest)
Each desk stage runs in a fresh, disposable workdir **outside** the repo, containing ONLY the inputs it may see:
- all stages: `task/` (card, grader interface, sota, public task.yaml, extras), the named `method/` files, `peers/` (other tasks' cards for duplicate checks);
- `anchored_rescore` also gets `prior/screen_card.md`;
- `probe_whitebox` also gets `grader_src/` (read-only; hidden data and secret seeds removed);
- the red team and the probes never see `runs/`, prior verdicts, the originating repo or hidden data.

With `isolation.mode: auto` and bubblewrap present, the agent process additionally runs in a mount namespace that masks the repo, the task dir, the grader source, every `hidden_data` path and other workdirs with empty tmpfs. A post-hoc independence check scans the session log for forbidden-path access and for any hidden-data canary string (values never printed).

## 7. Gates: canary and panel stay OFF
`config/runner.yaml` has `gates: {canary: OFF, panel: OFF, publish_or_share: OFF}` with empty `gate_go_records`. `redteam run <task> --stage canary|panel`:
- exits 3 (REFUSED) while the gate is OFF;
- still exits 3 if the gate is ON but `gate_go_records.<stage>` lacks who/when/source for Amita's GO;
- even with both in place, exits 4 and launches no rollout. Rollouts follow `method/rollout_spec.md` by hand, only after Amita's GO.

Don't flip a gate yourself.

## 8. Pairings
Any later rollout uses the canonical Task Tabs set (`config/runner.yaml` -> `pairings`): P1 Opus 5.5 + Claude Code, P2 Gemini 4 Argon + Antigravity, P3 Qwen 3.8 Max + Qwen Code, P4 GPT-6.2 Sol + Codex. Exact version pins are OPEN (bar F7). The desk backend (`desk_agent.model`) is the reviewer, not a pairing under test.

## 9. Worked example: `examples/toy_task`
A tiny classifier task with a real grader source and hidden labels. It runs the whole pipeline with the stub backend:
```bash
redteam run examples/toy_task --backend stub --offline --new-run
redteam status examples/toy_task
```
With the stub it lands: screen CONDITIONAL, anchored PASS-SCREEN (upper bound), **strict gate CONDITIONAL** (LITERATURE-ONLY, so the anchored PASS-SCREEN does NOT promote it), red team FIX, one white-box probe finding (uncounted), aggregate **FIX**. These are stub outputs to exercise the pipeline, not desk judgements. `make test` runs this end to end plus the unit tests.

## 10. Tests and checks
```bash
make test          # unit tests + end-to-end toy run (stub, offline)
make lint          # ruff
make secret-scan   # scan the tree for secrets (never prints values)
make e2e           # just the toy end-to-end run
```

## 11. DO NOT
- **No GPU, no rollouts, no paid compute.** Canary/panel need Amita's recorded GO.
- **No sharing** of this repo, its prompts, runs or verdicts with labs, GDM or anyone outside the team. No public posts.
- **No souping or merging** (model soups, weight averaging, task arithmetic, TIES/DARE), as attack, fix or task.
- **No grader access** beyond the interface in `grader_interface.md` (the white-box probe's read-only `grader_src/` is the one exception; hidden data/seeds stay withheld).
- **Never commit secrets:** no API keys, tokens, `.env`, cookies or session logs. `.gitignore` covers `*.jsonl`, `*.log`, `.env*`; run `make secret-scan` and check `git diff --cached` before every commit.
- **Label every estimate ESTIMATED** and every unmeasured quantity UNMEASURED. Desk verdicts are not measurements.
- Don't change kill lines or record keys in `method/` without telling Amita; record any such change in your report.

## 12. Known gaps / still not generic (be honest)
- **Desk verdicts are LLM judgements, not measurements.** Every number is ESTIMATED and UNMEASURED. A panel can kill but never clear.
- **The strict gate trusts the agent's `attack_basis`.** A mislabelled LITERATURE-ONLY vs DEMONSTRATED-AGENT changes the gate; the pipeline records the basis and flags disagreements but cannot verify the evidence for you.
- **The record parser is tolerant but not magic.** Wildly malformed record blocks parse as INCOMPLETE; re-run with `--force`.
- **URL liveness is best-effort.** Bot-walls (401/403/429/999) are reported as "blocked", not "dead"; verify cited URLs yourself when it matters. `enforce: false` by default.
- **Blindness without bubblewrap is weaker.** Copy-only isolation plus the prompt and the post-hoc check still let a determined agent run a recursive search; the independence check flags it after the fact. Install `bwrap` for OS-level masking.
- **The desk-agent model matters.** Runs on different models aren't directly comparable; the model is recorded in `run.yaml`.
- **Aggregation is per-run.** Cross-task rollups (rankings, flip tables, strict-view summaries) are not rebuilt here; `runs/INDEX.tsv` is the per-stage index. The historical cross-task summaries live in `archive/`.
- **Imported history isn't re-runnable.** `archive/tasks/*` cards have no `task.yaml`; write one to run them through the new CLI.
- **The method prompts are drafts.** `attacker_prompt.md`/`rollout_spec.md` carry open questions and TODO harness pins (bar F7).
