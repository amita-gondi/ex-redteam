# C010 — Train through delayed simulator corrections — screen audit
## 1. What the screen claimed
The screen combined correction-aware prioritized sequences, rare-contact/reservoir retention, predecessor replay and recomputed recurrent state. ESTIMATED single/bo4/pass@4/ub95 were 0.46/0.56/0.34/0.72; CONDITIONAL required genuine byte pressure and prospective sufficient-evidence retention. The TSV has no kill category for this survivor. Its old URLs were:
- https://openreview.net/pdf/387fb2fcee8f74c53cf707a9856f40c458f33933.pdf
- https://arxiv.org/abs/1707.01495

## 2. Evidence audit
The old R2D2 PDF fetch returned a browser challenge, not paper content; the author-hosted abstract was successfully fetched below. Hindsight Experience Replay — Marcin Andrychowicz, 2017/2018, fetched at the second URL — demonstrates useful goal relabeling in manipulation. Neither changing a goal nor repairing recurrent-state staleness recovers an already discarded observation needed to reinterpret a delayed contact correction.

Grade: PARTIAL. Recurrent replay and relabeling have real demonstrations, but prospective storage by future correction sensitivity is unsupported on a comparable task. The screen acknowledges this distinction and conditions survival on memory sufficiency; it never shows that a nonanticipatory reference can outperform whole-episode reservoir sampling under a realistic storage allowance.

## 3. Research done now
- Recurrent Experience Replay in Distributed Reinforcement Learning — Steven Kapturowski, 2019 — https://willdabney.com/publication/r2d2/ — fetched — The author's page confirms the study of representational drift and recurrent-state staleness in prioritized replay. This supports recomputation/burn-in, but Atari/DMLab results do not establish retroactive contact correction under byte accounting.
- Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning — Jianlan Luo, 2024, revised 2025 — https://arxiv.org/abs/2410.21845 — fetched — Integrates demonstrations and corrections into efficient vision-based manipulation learning. It raises confidence in the downstream learning stack; human takeovers differ from delayed revision of past truth.
- SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning — Jianlan Luo, 2024/2025 — https://arxiv.org/abs/2401.16013 — fetched — Shows strong practical learning from a carefully engineered off-policy implementation. It raises the conventional floor and emphasizes that replay implementation quality can dominate an apparent algorithmic contribution.
- E2HiL: Entropy-Guided Sample Selection for Efficient Real-World Human-in-the-Loop Reinforcement Learning — Haoyuan Deng, 2026 — https://arxiv.org/abs/2601.19969 — fetched — Improves manipulation sample selection by estimated influence on policy entropy. It strengthens selective replay beyond raw TD error, without predicting which apparently ordinary observation will matter after a future correction.

Searches included delayed contact labels, robot correction learning and recurrent replay. The old PDF remains an explicitly blocked historical citation; no claim relies on its unread body.

## 4. Re-estimated attack
ESTIMATED credits are 0.19 for correcting available local targets, 0.14 for recurrent-context replay and 0.10 for rare-contact/influence-aware memory allocation. Their 0.43 sum leaves substantial uncertainty about long-range retained evidence. Full trajectories and honest compressed observations remain legal alternatives; the analysis does not assume they exceed the as-yet unspecified cap.

ESTIMATED R={0.22,0.43,0.59,0.73}, masses {0.24,0.50,0.20,0.06}, distinguishes missing context, competent local repair, useful prospective coverage and a discovered sufficient representation. Research choices and geometry/seed variation drive the spread. Single=0.24×0.22+0.50×0.43+0.20×0.59+0.06×0.73=0.43, range 0.22–0.73. Bo4=0.73−0.14×0.94^4−0.16×0.74^4−0.21×0.24^4=0.57. Only the top state passes, so pass@4=1−0.94^4=0.22. CDF below it is 0.94, giving ub95=0.73. All are ESTIMATED with independent restarts conditional on a geometry block. Compared with the screen, similar expected maximum coexists with lower repeated-pass probability: many good attempts remain just below the success threshold.

## 4A. Demonstrated capability and subfield SOTA
HIL-SERL reports near-perfect manipulation success after one-to-two-and-a-half hours, while SERL reports strong assembly/routing/relocation policies in twenty-five-to-fifty minutes. The newer E2HiL paper reports improved sample efficiency over its compared HiL baselines. These are strong human-built systems, not evidence for retrospective-truth sufficiency. Anchor the floor to their legal replay ideas plus whole-episode retention; R≈1 requires a measured superior nonanticipatory buffer, which no consulted source supplies for this metric.

- MLGym — Deepak Nathani, 2025 — https://arxiv.org/html/2502.14499v1 — fetched. o1-preview with the SWE-Agent-based harness reaches reported Mountain Car reward 96.335 from 33.794, with two GPUs and approximately two-hour agent runtimes. This demonstrates PPO training improvement, but omits pixels, delayed corrections and bounded replay storage.
- RE-Bench — Hjalmar Wijk, 2024/2025 — https://arxiv.org/html/2411.15114v2 — fetched. METR-scaffolded Claude 3.5 Sonnet/o1-preview agents outperform average experts at two aggregate hours, but lag at thirty-two. Environments allocate up to six H100s. The gap here is designing and validating a prospective memory statistic, rather than implementing an available replay routine.

Basis LITERATURE-ONLY: KNOWN-RECIPE corrected replay exists, while AGENT-DEMONSTRATED discovery of causal retention under delayed truth does not. Twelve hours must include byte tracing, correction chronology, policy training and fresh-geometry validation.

ANCHORED ESTIMATED distribution puts mass 0.25 at 0.18 for integration failure and mass 0.75 uniformly on [0.32,0.66] for increasingly effective retention. Single=0.25×0.18+0.75×0.49=0.41, range 0.18–0.66. Bo4=0.66−0.14×0.25^4−0.34×(1−0.25^5)/(5×0.75)=0.57. The single-pass probability is p=0.75×(0.66−0.60)/0.34=0.13; using the unrounded p, pass@4=1−(1−p)^4=0.43. Ub95=0.32+0.34×(0.95−0.25)/0.75=0.64. Distribution shape and missing normalization remain assumptions.

## 5. Verdict under the kill lines
Section 4 evidence verdict CONDITIONAL; ANCHORED verdict CONDITIONAL, UNCHANGED. Anchored bo4 has ESTIMATED 0.03 margin, pass@4 0.07, single 0.29 and ub95 0.11. Strong robotics stacks support substantial routine recovery without establishing the prospective sufficiency step. The verdict rests on that capability assumption and the unresolved memory/reference contract, rather than on delay alone creating difficulty.

## 6. Redesign
Cause (a): mature corrected replay defeats a local-window task. Make the survival condition explicit: use a deployment-derived storage envelope, meter encoded observations and recurrent state, and demonstrate that legal compressed whole-episode reservoirs leave recoverable headroom. Include contact revisions whose correct interpretation depends on earlier observable load, compliance or object-state transitions. Show analogous dependencies during development; reveal correction timing rules and never grant the reference future labels.

Require a buffer that retains sufficient causal features before knowing the eventual revision, with fixed learner interfaces and evaluation on new contact geometries. This is useful robotics continual-learning R&D. The strongest re-attack combines episode reservoirs, influence-based priorities, learned keyframe compression and correction-triggered recurrent replay. Basis LITERATURE-ONLY for the complete system. It falls short only if prospective sufficient features generalize better than generic reconstruction or uncertainty sampling; an equal-byte reference must demonstrate that difference. Otherwise either standard storage solves it or the cap destroys feasibility.

ESTIMATED redesign states {0.21,0.39,0.61}, masses {0.38,0.54,0.08}: single=0.38×0.21+0.54×0.39+0.08×0.61=0.34; bo4=0.61−0.22×0.92^4−0.18×0.38^4=0.45; pass@4=1−0.92^4=0.28; ub95=0.61. REDESIGNABLE, with compressed whole-episode storage the decisive bypass risk. Pilot GPU-h ESTIMATED: 100M visuomotor learner, five retention arms×three seeds×eight H100-hours, twelve H100-hours for representation preparation and twenty-four for closed-loop evaluation: 5×3×8+12+24=156.

## 7. Measurement status
Rollouts UNMEASURED (planned chronological buffer policies with complete observation-byte ledgers). Grader noise UNMEASURED (planned repeated simulator/learner seeds and fixed-policy manipulation evaluation). Score ladder UNMEASURED (planned FIFO, corrected recurrent replay, compressed episode reservoir, causal retention and feasible stronger buffer).

## Audit record
id: C010
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 6
sources_fetched_count: 7
old_single: 0.46
old_bo4: 0.56
old_pass4: 0.34
old_ub95: 0.72
new_single: 0.43
new_single_range: 0.22-0.73
new_bo4: 0.57
new_pass4: 0.22
new_ub95: 0.73
new_verdict: CONDITIONAL
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Establish real byte pressure and observable long-range correction dependencies that a feasible prospective causal buffer can retain.
redesign_single: 0.34
redesign_bo4: 0.45
redesign_pass4: 0.28
redesign_ub95: 0.61
redesign_gpuh: 156
attack_basis: LITERATURE-ONLY
demonstrated_ref: MLGym, o1-preview SWE-Agent, 2025; RE-Bench, Claude 3.5 Sonnet and o1-preview METR scaffold, 2024/2025
gap_to_attack: Select sufficient past contact evidence before its delayed correction arrives under a real replay-byte cap
subfield_sota_ref: Manipulation corrections Luo HIL-SERL 2024/2025; sample selection Deng E2HiL 2026
anchored_single: 0.41
anchored_bo4: 0.57
anchored_pass4: 0.43
anchored_ub95: 0.64
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
