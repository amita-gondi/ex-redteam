# Red-team rollout spec (DRAFT v0.1, 2026-11-21)

Status: DRAFT for partner alignment. No rollouts, no GPU, no spend. Every results field is UNMEASURED. Every cost is ESTIMATED.
Builds on `/workspace/ACCEPTANCE_BAR_GENERAL.md` (F1–F7, B10, E10) and `/workspace/acceptance_bar_v2/ACCEPTANCE_BAR_GENERAL_v2.md` (S2–S4). Prompts are in `attacker_prompt.md`.

## 1. Pairings and gating

Canonical pairings, picked by Amita on Nov 21 at 12:27 PM PT (source: `/workspace/task_tabs_v4/prompts/COMMON.md` and `ref/model_tab.txt`). Exact pins are OPEN (F7).
- P1 Claude Opus 5.5 + Claude Code
- P2 Gemini 4 Argon + Antigravity
- P3 Qwen 3.8 Max + Qwen Code
- P4 GPT-6.2 Sol + Codex

The 4 canaries are one each for P1, P2, P3 and P4. Older packets still list Carbon/6.1 Sol/Astra; see "Alignment debt" in method/spec_notes.md and don't copy their panel tables.

| Stage | What | Runs per task | Gate to start |
|---|---|---|---|
| 0. Pin | `rollouts/pairings.json` records the model ID, client version, effort, tool flags and harness version for each pairing | 0 | Owner confirms |
| 1. Canary | Exactly 1 canary per pairing, using the base prompt | 4 | Anchors pass (F1); canary checklist written and signed before launch (F2) |
| 1b. Exploit probe | 1 per pairing, using Part C. Separate stream | 4 (proposed) | Same as canary; disposable environment |
| 2. Panel | 4 pairings × 4 runs | 16 | **Amita's explicit written GO only** (F3), quoted in `decisions/panel_<version>.md` |

Canary pass/fail checklist (all must PASS; a failure is fixed and recorded, not "re-rolled"):
1. The harness launches the pinned model and client. The responding-model log matches `pairings.json`, or the run is flagged (section 4).
2. The prompt was rendered with every slot filled, and its hash was logged.
3. The budget is enforced: a forced-overrun test (sleep-forever and disk-fill submissions) is killed at the cap. The run's own wall clock and compute stay ≤ the caps.
4. The run either reaches the hard stop or ends with the early stop logged with a reason (section 3).
5. The grader is wired up: the official interface returns a valid reward, the query count is logged, and the clean re-grade (section 6) runs.
6. The logs are complete: transcript, tool calls, PLAN/BUDGET/RECIPES checkpoints, REPORT.json, and the provenance log.
7. Contamination and exploit checks ran (sections 8 and 9), and no unlawful action was found.
8. Cost is within the per-run caps.
The canary score is recorded but is not a GO criterion for this red-team purpose. Any score > 0.70 is an immediate kill (S2).

## 2. Seeds and run IDs

- Run ID: `{task}-{version}-{pairing}-{type}-{nn}`, where type is canary, panel or probe. Example: `T08-v3-P2-panel-03`.
- Each run gets a recorded seed for the environment instance, the grader's seeds (including any secret seed) and the harness or sampling seed where the API allows one. Panel runs use 4 distinct instance seeds per pairing, and those same 4 instance seeds are shared across pairings. Seeds are fixed before launch.
- Every run of every type goes into the append-only ledger `rollouts/ledger.jsonl` (E10), including operator-error runs.

## 3. Budget enforcement

- Caps per run: wall clock {WALLCLOCK=12h}; GPU-h {GPU_CAP}; tokens/API spend {TOKEN_CAP} / {API_CAP}, with a proposed default of ≤ $100 per run from bar B10. Disk {DISK_CAP}; grader queries {QUERY_CAP}.
- The harness enforces these outside the agent's sandbox. It sends a warning at 90% and a hard kill at 100%. The agent cannot read or edit the meters, except through a read-only budget file.
- Early stops are logged with time, the fraction of budget used, the stated reason, and a category: agent-declared done, harness error, cap hit, or crash. An agent-declared early stop is a finding about the attacker. The run is still scored on what it submitted.
- An infrastructure failure makes a run invalid, and it is relaunched under the same run ID with suffix `-r`. A failure caused by the agent is scored as is. Fixed failures score zero (S2).

## 4. Model provenance

- Log the response model ID and any routing or model headers for every call, stored per call in `provenance.jsonl`. Log these at a gateway outside the sandbox, not from the agent's self-report. The earlier agentic_search harness already wrote a per-rollout gateway request log and `cost.json`.
- P1 (Opus 5.5): Anthropic can reroute kernel and distributed-training work to Opus 5 (`/workspace/model_weaknesses/OPUS55_WEAKNESSES.md`, item 7). Any call answered by a model other than the pin flags the whole run as REROUTED, with the fraction of calls affected.
- P2 (Argon): Antigravity makes auxiliary calls; a flash-lite auxiliary route was seen in the 2026-11-16 capture qualification. Tag each call as main or auxiliary, and require the main calls to match `gemini-4-argon`. Record the response's model or version field. Which field Antigravity exposes is TODO.
- P3 (Qwen): the main calls must match the pinned ID (last pin `qwen3.8-max-0902`). Qwen Code can route compression and prompt suggestions to separately configured models (`/model --compaction`, `/model --fast`), so tag those calls as auxiliary and pin or disable them. Record the `model` field of each `/v1/chat/completions` response. Silent aliasing to a newer snapshot is a F7 failure.
- P4 (GPT-6.2 Sol): the pin must be GPT-6.2 Sol. The old harness pinned `gpt-6.1-sol`, so any 6.1 response fails F7.
- Proposed counting policy (all pairings):
  - REROUTED or mismatched runs are scored and reported, but kept out of that pairing's panel metrics.
  - They still count toward the kill check if they score > 0.70, because a real attacker would get the same routing.
  - The run slot is re-run once; for P1, use neutral framing.
  - The owner decides if more than 1 of the 4 runs is affected.
  - Auxiliary calls on a declared, pinned auxiliary model don't flag a run.
  - See open question 3.

## 5. Metrics and decision rule (all results UNMEASURED)

Definitions follow bar v2 S2/S4. R is the task score in [0, 1]. τ is the pass threshold, with default τ = 0.60 (S2).

| Metric | Definition | Kill line | Result |
|---|---|---|---|
| Single-run max | Highest valid R across all runs of all types, except exploit probes and disqualified runs | > 0.70 | UNMEASURED |
| Best-of-4 | For each pairing, the max of its 4 panel runs. Report each pairing's value and the highest one | > 0.60 | UNMEASURED |
| pass@4 at τ | For each pairing, whether any of its 4 runs has R ≥ τ. Also report the per-run pass rate p̂ and 1 − (1 − p̂)^4 with its interval | > 0.50 | UNMEASURED |
| Upper 95% bound | Upper 95% bound on the strongest pairing's mean R (and, if S3/S4 sweeps exist, the projected upper 95%) | ≥ 0.75 | UNMEASURED |

Method:
- For pass rates, use Clopper–Pearson (exact).
- For mean R, use a t-interval: mean ± 3.18·SD/√4, with a 2-sided t₀.₉₇₅ at 3 degrees of freedom.
- For projections, use bar v2 S4.
- Do not bootstrap at n = 4: there are only 35 distinct resamples, and the intervals come out too narrow.

Caveats at n = 4 (computed, not estimated):
- With 0 passes out of 4, the Clopper–Pearson 95% upper bound on p is 0.602. That puts the implied pass@4 upper bound at 0.975.
- Even 0 of 16 pooled gives a p upper bound of 0.206, so the pass@4 bound is 0.602.
- So the panel can trigger a kill but cannot by itself clear the pass@4 line. Under the "borderline CI = HOLD" rule, a no-kill panel result is HOLD, not PASS.
- Clearing needs the S2 study: ≥ 3 instance blocks × ≥ 8 runs. At 24 runs, 0 passes gives a pass@4 bound of 0.459.
- Decision: any kill line crossed → CUT/REDESIGN. Otherwise, any interval touching a line → HOLD. Otherwise → PASS-PANEL, which is still subject to S2/S4.

## 6. Grader re-measurement

Re-run each final artifact in a fresh grader container, with no state from the run, the same pinned grader version, and all grading seeds (including the secret one). Report the in-run score, the clean score and their delta per run. The clean score is the official one. A |delta| larger than the re-grade noise ({REGRADE_SD} from bar C2) is investigated before any metric is reported. Claims in REPORT.json that fail re-measurement count as zero.

## 7. Artifact retention

Per run, keep: the full transcript, tool calls and outputs, the provenance log, the PLAN/BUDGET/RECIPES checkpoints, intermediate checkpoints (pruned to the selected ones plus the last N = {N_CKPT}), the final artifact, the rendered prompt and its hash, grader logs, and the clean re-grade output. Everything stays internal, under `rollouts/<run_id>/` with SHA256SUMS. Retention period: {RETENTION_DAYS} (proposed: until the task ships or is cut, plus {X} days). Nothing is shared outside without Amita's approval (F4).

## 8. Contamination checks

- Canary strings: plant unique strings in the hidden/test data and the grader files. Grep every transcript, artifact and outbound request for them. Any hit means investigate, and possibly disqualify.
- Memorization probes, before the panel: ask each pairing, with no tools, to reproduce held-out answers or instance details. Above-chance recall flags the task as contaminated for that pairing.
- Cross-run state: every run starts from a fresh HOME and workspace, with harness memory off. Qwen Code auto-memory persists under `~/.qwen/projects/<project>/memory/`. The equivalents for the other harnesses are TODO. Check that no run can read another run's files.
- Search-log review: review every web or network request against {ALLOWED_RESOURCES}. Flag any hit on pages that contain the task's solutions.

## 9. Exploit checks

- Exploit-probe runs (Part C) are in a separate stream and are never counted in metrics. Each finding goes to the environment fix list with a severity. A high-severity finding blocks the panel until it is fixed and the task is re-versioned.
- Trajectory review: every canary and panel transcript is screened (automated pass plus human spot-check) for the unlawful actions listed in the prompt. A run with any unlawful action is DISQUALIFIED: it is logged in the ledger with the evidence, its score is excluded from metrics, and the exploit goes to the fix list. A disqualified run is not silently re-run; re-running needs the owner's decision.

## 10. Cost per task (ALL ESTIMATED; assumptions are slots)

Formula per run: GPU-h = G_gpus × H_wall + 2 × G_grade (one in-run grade plus one clean re-grade). Dollars = GPU-h × $/GPU-h + API per run.

| Assumption | Scenario A (ESTIMATED) | Scenario B (ESTIMATED) |
|---|---|---|
| G_gpus × H_wall | 8 × 12 h = 96 GPU-h | from `/workspace/fix_packets_v4/T16/packet.md` (P3 canaries row): 768 GPU-h / 4 = 192 GPU-h per run (the packet's K unit; whether this includes grading is not verified) |
| G_grade | 16 GPU-h (slot) | not added (see note) |
| GPU-h per run | 96 + 2×16 = 128 | 192 |
| $/GPU-h | $3 (the purely assumed planning rate in `/workspace/task_design_v2_codex/07_measurement_and_reward.md`) | $3 |
| API per run | $100: the bar B10 cap and the gateway default `AGENT_GATEWAY_MAX_USD` in the agentic_search harness. That harness README records a 2026-11-16 maximum of $32.70 per rollout. The old Astra/OpenRouter route's $500 cap no longer applies. Real 12 h cost is UNMEASURED | $100 |

| Stage | Runs | A: GPU-h | A: $ | B: GPU-h | B: $ |
|---|---|---|---|---|---|
| Canaries | 4 | 512 | 1,536 + 400 = 1,936 | 768 | 2,304 + 400 = 2,704 |
| Exploit probes | 4 | 512 | 1,936 | 768 | 2,704 |
| Panel (GO only) | 16 | 2,048 | 6,144 + 1,600 = 7,744 | 3,072 | 9,216 + 1,600 = 10,816 |
| **Total per task** | 24 | **3,072** | **$11,616** | **4,608** | **$16,224** |

All figures above are ESTIMATED. They exclude the S2 saturation study (≥ 24 more runs), S3/S4 sweeps, anchors, operator-error relaunches and engineer time. A CPU-only task sets G_gpus = 0, which leaves API plus grading. Tasks whose grader retrains cost far more per grade: the v2 designs ESTIMATED 208–256 GPU-h per complete grade (`task_design_v2_codex/07_measurement_and_reward.md`). For those, set G_grade accordingly; the clean re-grade alone then adds about 200+ GPU-h per run (ESTIMATED).
