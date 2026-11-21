# Getting started: running the red-team desk pipeline on YOUR task

> **AIUC-internal, private repo only.** Don't share this repo, its prompts or its run records with labs, GDM or anyone outside the team.

This repo runs three desk-only stages on one RL-environment task:

**screen → anchored re-score → red team (HOLDS / FIX / CUT)**

The **strict** rule is the promotion gate (`config/runner.yaml` → `gate_rule: strict`). The anchored verdict is an **upper bound** on survival (`anchored_upper_bound: true`), not the decision that advances a task. After the anchored re-score, `run.yaml` records both `strict_verdict` (the gate) and `anchored_verdict` (the upper bound). `outcome` follows the strict verdict.

Each stage is a single Codex CLI session that reads your task files and writes one report plus a `run.yaml`. Nothing is trained or rolled out. The two rollout stages (canary, panel) are switched off, and the wrapper refuses to run them.

---

## 1. Prerequisites
| Need | Notes |
|---|---|
| git | to clone this repo and commit your own task/run files on a branch |
| Codex CLI (`codex`) | Install it and log in with **your own** model access. Never commit credentials. Tested with codex-cli 0.163.0. |
| Model and effort | Set in `config/runner.yaml` → `desk_agent`. All imported runs used **`gpt-6.1-sol`, `model_reasoning_effort=high`, `--search` on**. If you don't have that model, set your own and say so in your report (it is recorded in `run.yaml`). |
| Python 3 + PyYAML | `python3 -m pip install --user pyyaml` |
| GPU | **None needed.** Every stage is CPU/desk-only. |


## 2. Add your task: `tasks/<id>/` from `_template`
```bash
cp -r tasks/_template tasks/MYTASK01
$EDITOR tasks/MYTASK01/card.md tasks/MYTASK01/grader.md tasks/MYTASK01/sota_sources.md
```
- **`card.md`**: the problem, the action surface, the reward and the north star (what R≈1 means), the budget, and the anti-shortcut design. Write it so a stranger could build it.
- **`grader.md`**: the grader *interface* only (accepted inputs, scoring, seeds, fail-closed rules, anti-gaming fixtures). The agents see the grader only through this file. Don't link grader internals or private data.
- **`sota_sources.md`**: the evidence the anchored stage is held to (`method/evidence_grounding_rule.md`). It has two parts:
  - **Demonstrated agent results** (≥2): benchmark/system, model + scaffold, time and compute, what was achieved, the gap to your task's attack, and the attack_basis.
  - **Subfield SOTA**: the result, the authors/system, the **year**, the URL, and how your north star is anchored to it.
  - Mark any source you didn't open as unverified.

The task id must be letters, digits, `_` or `-` (e.g. `MYTASK01`).

## 3. Run the stages (CPU/desk only)
Always dry-run first. A dry-run prints the fully rendered prompt and the exact `codex` command, and writes nothing:
```bash
bin/redteam MYTASK01 screen --dry-run
```
Then run the stages in order. Each one blocks until Codex finishes.
```bash
bin/redteam MYTASK01 screen              # -> PASS-SCREEN | CONDITIONAL | CUT
bin/redteam MYTASK01 anchored_rescore    # re-scores the latest runs/MYTASK01/*/screen/screen_card.md (or --prior PATH)
bin/redteam MYTASK01 redteam             # independent; told never to read runs/; -> HOLDS | FIX | CUT
```
Options:
- `--date YYYY-MM-DD` (default: today);
- `--model` / `--effort` to override the config for one run;
- `--force` to re-run into a folder that already has `DONE.txt`.

How to read the results:

| Stage verdict | Outcome |
|---|---|
| PASS-SCREEN / HOLDS | ADVANCE |
| CONDITIONAL / FIX | FIX |
| CUT | CUT |
| any interval touching a kill line | HOLD, not pass |

After an anchored re-score, the **strict** verdict is the gate used for `outcome` and for whether the task is promoted. The anchored verdict is kept as an upper bound: a card that survives only in the anchored reading is not promoted. For LITERATURE-ONLY or ASSUMED attacks, strict uses the evidence-only / pre-anchoring scores (treat the attack as executable by a 12-hour frontier agent). Only DEMONSTRATED-AGENT evidence may lower an attack score below that. See `method/evidence_grounding_rule.md`.

Kill lines (`method/kill_thresholds.md`):
- single run > 0.70
- best-of-4 > 0.60
- pass@4 > 0.50 at R ≥ 0.60
- upper-95% ≥ 0.75

After a red-team run, two optional checks:
```bash
python3 tools/wording_check.py runs/MYTASK01        # repeated-boilerplate check across reports (<10% per file)
python3 tools/independence_check.py runs/MYTASK01/<date>/redteam/codex_events.jsonl   # bin/redteam also runs this
```

## 4. Where outputs land
```
runs/<task>/<YYYY-MM-DD>/<stage>/
  prompt.md            exact rendered prompt (hash in run.yaml)
  screen_card.md | audit_card.md | redteam.md    the report, ending in a machine-readable record block
  DONE.txt             written by the agent when finished
  run.yaml             written by bin/redteam: status, model, effort, prompt sha256, repo commit,
                       parsed record, verdict -> outcome, label "ESTIMATED desk verdict, UNMEASURED"
  last_message.md      Codex's final message
  codex_events.jsonl, codex.log    raw session output (git-ignored; never commit them)
```
`run.yaml` reads `IN-PROGRESS` while the stage runs. It becomes `COMPLETE` if Codex exited 0 and the record block parsed, and `INCOMPLETE` otherwise. If you get `INCOMPLETE`, read `codex.log` and re-run with `--force`.

## 5. Gates: canary and panel stay OFF
`config/runner.yaml` has `gates: {canary: OFF, panel: OFF, publish_or_share: OFF}` and empty `gate_go_records`. `bin/redteam <id> canary|panel`:
- exits with code 3 (REFUSED) while the gate is OFF;
- still refuses if the gate is ON but the `gate_go_records.<stage>` entry lacks who/when/source for **Amita's GO**;
- even with both in place, does not run rollouts (exit 4). Rollouts follow `method/rollout_spec.md` by hand, and only after Amita's GO.

Don't flip a gate yourself.

## 6. Pairing set
For any later rollout, use the **canonical Task Tabs set** only (settled by Amita, Nov 21, 2026; exact version pins are still OPEN). It's also in `config/runner.yaml` → `pairings`.

| ID | Model | Harness |
|---|---|---|
| P1 | Claude Opus 5.5 | Claude Code |
| P2 | Gemini 4 Argon | Antigravity |
| P3 | Qwen 3.8 Max | Qwen Code |
| P4 | GPT-6.2 Sol | Codex |

The desk agent (`desk_agent.model`) is a separate setting. It is the reviewer, not a pairing under test.

## 7. DO NOT
- **No GPU.** No training jobs, no paid compute.
- **No rollouts.** Canary and panel need Amita's GO, and that GO is recorded in config by her side, not yours.
- **No sharing** of this repo, its prompts, runs or verdicts with labs, GDM or anyone outside the team. No public posts.
- **No souping or merging** (model soups, weight averaging, task arithmetic, TIES/DARE). It's out of scope for attacks, fixes and tasks alike.
- **No grader access** beyond the interface written in `grader.md`. No hidden seeds, internals or private data.
- **Never commit secrets:** no API keys, tokens, `.env` files, auth headers, cookies or session logs. `.gitignore` covers `*.jsonl`, `*.log` and `.env*`, but check `git diff --cached` before every commit anyway.
- **Label every estimate ESTIMATED**, and every unmeasured quantity UNMEASURED (with the planned measurement). Desk verdicts aren't measurements.
- Don't edit `method/` prompts in a way that changes kill lines or record keys without telling Amita. Record the change in your report.

## 8. Worked example: C010 ("Train through delayed simulator corrections")
`tasks/C010/card.md` is the real v4 creative card. It predates `_template`, so `grader.md` and `sota_sources.md` are missing, and the wrapper warns about that. Its history is already in the repo from the imported Nov 21 runs, all of them **ESTIMATED desk verdicts, UNMEASURED**:

| Stage | Path | Verdict → outcome | Key numbers (ESTIMATED) |
|---|---|---|---|
| screen | `runs/C010/2026-11-21/screen/` (`screen_card.md`, `run.yaml`) | CONDITIONAL → FIX | single 0.46 (0.25–0.64), bo4 0.56, pass@4 0.34, ub95 0.72 |
| anchored re-score (imported as `screen_audit`; this audit was still running when imported) | `runs/C010/2026-11-21/screen_audit/` (`audit_card.md`, `run.yaml`) | **strict (gate)** CONDITIONAL → FIX, same as the evidence-only verdict (attack_basis is LITERATURE-ONLY, so the gate cannot use the lowered anchored scores). Anchored upper bound is also CONDITIONAL, binding bo4>0.60 | evidence-only single 0.43, bo4 0.57, pass@4 0.22, ub95 0.73; anchored single 0.41, bo4 0.57, pass@4 0.43, ub95 0.64 (ESTIMATED). The verdict rests on assumption. A later wrapper run would record both `strict_verdict` and `anchored_verdict` in `run.yaml` |
| red team (v4 independent) | `runs/C010/2026-11-21/redteam/` (`redteam.md`, `run.yaml`) | FIX → FIX | single max 0.82, bo4 0.74, pass@4 0.84, ub95 0.93. Required fixes listed in `run.yaml` |

So the screen, the evidence-only re-estimate and the anchored upper bound all put C010 just under the best-of-4 line. Because the attack_basis is LITERATURE-ONLY, the strict gate is the evidence-only CONDITIONAL, not a more optimistic anchored reading. The independent red team found a combined replay/reconstruction recipe that breaches all four lines. The outcome is FIX: redesign before any GO.

Re-running C010 with the wrapper (these are the real dry-run outputs, Nov 21, 2026):
```bash
$ bin/redteam C010 screen --dry-run --date 2026-11-22
WARN: tasks/C010/grader.md missing; the prompt tells the agent to say so
WARN: tasks/C010/sota_sources.md missing; the prompt tells the agent to say so
=== RENDERED PROMPT (C010 / screen, sha256 …) ===
You are doing a CPU-only DESK SATURATION SCREEN of one RL-environment research task. Task: C010. …
=== COMMAND (not executed; --dry-run) ===
cd <repo> && codex --search exec -m gpt-6.1-sol -c model_reasoning_effort=high --skip-git-repo-check \
  -s workspace-write -C <repo> --json -o runs/C010/2026-11-22/screen/last_message.md \
  "$(cat runs/C010/2026-11-22/screen/prompt.md)" > runs/C010/2026-11-22/screen/codex_events.jsonl 2> runs/C010/2026-11-22/screen/codex.log
would create: runs/C010/2026-11-22/screen/{prompt.md,run.yaml,screen_card.md,last_message.md,codex_events.jsonl,codex.log}

$ bin/redteam C010 anchored_rescore --dry-run --date 2026-11-22   # prompt names: runs/C010/2026-11-21/screen/screen_card.md
$ bin/redteam C010 redteam --dry-run --date 2026-11-22            # -> runs/C010/2026-11-22/redteam/
$ bin/redteam C010 canary
bin/redteam: REFUSED: stage 'canary' is gated and gates.canary is OFF in config/runner.yaml. …   (exit 3)
```
Without `--dry-run`, the three commands would produce `runs/C010/2026-11-22/{screen,anchored_rescore,redteam}/`, each with a report and a `run.yaml`. That is the same layout as the imported runs; the only difference is that the new anchored stage is named `anchored_rescore`, not `screen_audit`.

## 9. Known gaps (be honest about these in your report)
- **No stall watcher or auto-resume.** The wrapper runs a session once and blocks. If Codex stalls or dies, `run.yaml` stays `IN-PROGRESS` or `INCOMPLETE`. Re-run with `--force`, or resume by hand with `codex exec resume <session-id> …`. The program used per-batch watchers (`stall_minutes`, `max_resumes` in config), and those aren't included.
- **Checks are partial.** `tools/wording_check.py` (the boilerplate check) is a generic copy. There is no URL-liveness checker: verify cited URLs yourself.
- **Independence is not sandbox-enforced.**
  - Red-team blindness, and "write only to your run folder", are enforced by prompt instructions plus a post-hoc check (`tools/independence_check.py` scans the saved JSONL for `runs/` access and recursive searches).
  - `-s workspace-write -C <repo>` lets the agent write anywhere in the repo, so review `git status` after each run.
- **Aggregation is task-family-specific.** The program's aggregation scripts (rankings, flip tables) were written per task family, so they aren't included. `runs/INDEX.tsv` was produced by `tools/import_runs.py` for the imported runs only; it isn't updated by `bin/redteam`.
- **Verdicts are LLM desk judgments, not measurements.** Every number is ESTIMATED. A panel of 4×4 rollouts could later kill a task but never clear it (0/16 still leaves pass@4 ≤ 0.602 at 95%; see `method/kill_thresholds.md`).
- **The record parser is simple.** It reads `key: value` lines after the record heading. If an agent formats the block differently, the parsed fields are empty, and status becomes `INCOMPLETE` even though the report exists.
- **Desk-agent model.** The imported runs used gpt-6.1-sol. Runs on a different model aren't directly comparable.
