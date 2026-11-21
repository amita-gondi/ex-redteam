# C060 — Sampler consensus without serializing tensor parallelism — screen audit
## 1. What the screen claimed
The screen combined admission-time configuration normalization, authoritative-rank selection and compact NCCL token broadcast, then tuned shared RNG identities and safe fallback transitions. ESTIMATED single/bo4/pass@4/ub95=0.84/0.91/0.99/0.98 produced CUT, category SYS, because a tiny token receipt seemed close to the service ceiling. Its URLs were:
- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html
- https://docs.pytorch.org/docs/main/distributed/tensor.html

## 2. Evidence audit
NCCL documents correct collective use, not the overhead of a sampler embedded in this engine. DTensor's randomness support does not imply that distinct backends consume randomness or evaluate probabilities identically. Authoritative token distribution avoids rank disagreement, but the screen itself defines the repaired floor to include authoritative selection: that repair cannot also supply nearly all positive normalized reward.

Grade: PARTIAL. Compact broadcast is a solid known recipe and correct sampler semantics are essential. Evidence for a large *incremental* service gain after the repaired baseline is missing. Vocabulary-sharded logits and configuration transitions create real work beyond sending the chosen token, so calling the remaining communication negligible needs measurement.

## 3. Research done now
Audit distributions, performance forecasts and future run budgets are ESTIMATED. Reported benchmark scores are observations from the linked source, not C060 measurements.
- Collective Operations — NVIDIA NCCL, 2026 documentation snapshot — https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html — fetched — confirms consistent rank/count/type ordering requirements; supports token broadcast without quantifying residual goodput.
- torch.distributed.tensor — PyTorch, 2026 documentation snapshot — https://docs.pytorch.org/docs/main/distributed/tensor.html — fetched — provides distributed tensor/RNG machinery, not arbitrary backend equivalence.
- TP ranks can silently sample different tokens when their sampler configuration differs, issue 66912 — vLLM contributors, 2026 — https://github.com/vllm-project/vllm/issues/66912 — fetched — verifies the source failure report, while leaving the post-repair capacity question open.
- FlashSampling: Fast and Memory-Efficient Exact Sampling — Tomas Ruiz et al., 2026 — https://arxiv.org/html/2603.15854v4 — fetched — fused LM-head sampling and small cross-rank summaries provide a stronger concrete performance attack than token broadcast alone.
- ParallelKernelBench: Frontier LLMs can't write fast multi-GPU kernels (yet) — Together AI, 2026 — https://www.together.ai/blog/parallelkernelbench — fetched — distributed correctness and performance remain difficult, lowering confidence in effortless sampler-fusion integration.
- InferenceBench — InferenceBench team, 2026 — https://inferencebench.ai/ — fetched — agents can deploy strong serving combinations quickly; exact-sequence multi-rank transitions are outside its demonstrated target.

## 4. Re-estimated attack
Normalize sampler state and establish a correct authoritative path first, then profile the *remaining* bottleneck. Test fused local selection with compact candidate reductions where the authoritative random-number mapping and numeric semantics permit it; retain the correct baseline on other paths. Do not substitute distributional equality for the card's committed sequence semantics.

On a competent known-recipe path, ESTIMATED 0.18 comes from avoiding redundant sampler work beyond the repaired floor, 0.21 from fused vocabulary-parallel selection and 0.19 from overlap/capture across safe transitions: total 0.58. This is an assumed recovery of native goodput reserve, not credit for agreeing on the wrong token. A workload in which authoritative token broadcast already hits the physical ceiling has no such reserve and must be rejected at calibration.

Use ESTIMATED states 0.37/0.58/0.76 with probabilities 0.22/0.53/0.25. Exact-RNG failures create the low mode; full fusion without transition regressions creates the upper one. ESTIMATED single=0.22×0.37+0.53×0.58+0.25×0.76=0.58, range 0.37–0.76; ESTIMATED bo4=0.37+0.21(1−0.22^4)+0.18(1−0.75^4)=0.70; ESTIMATED pass@4=1−0.75^4=0.68; ESTIMATED ub95=0.76. The old 0.84 center effectively counted the competent repair as a new improvement and assumed backend equivalence.

## 4A. Demonstrated capability and subfield SOTA
FlashSampling is the closest inspected exact-sampling SOTA: it avoids full-logit materialization, demonstrates tensor-parallel operation through eight GPUs and reports up to 10% end-to-end output-token latency reduction in vLLM. Its exact categorical distribution does not itself promise identical draws under a different backend's seed mapping. Anchor the reference to the best compatible implementation with C060's actual RNG contract, and record native service reserve; do not turn a small residual into an arbitrary R=1.

Two model/agent results frame the engineering gap. InferenceBench gives agents two hours to submit a serving implementation; Claude Opus 5.5 Max in Claude Code leads its reported aggregate at 12.08× the naive baseline, while simple engine search is already highly competitive. Hardware totals are not specified on the fetched overview. Separately, ParallelKernelBench reports GPT-5.5 correct on 28 of 87 single-shot problems and faster on 22, with repeated samples improving but not solving most cases. Its illustrated kernels use four H100s; overall inference wall time is not given. Those model results bear directly on rank coordination but are not a twelve-hour sampler-integration trial.

KNOWN-RECIPE includes authoritative broadcast, coordinated RNG and now fused sampling. The whole attack remains LITERATURE-ONLY because no fetched agent result validates exact sampler transitions and service gains together. The missing twelve-hour integration must reconcile numeric ordering, request counters, backend epochs and collective lifetimes.

ANCHORED ESTIMATED distribution has two modes: 0.33 with probability 0.86 for useful configuration/receipt changes without validated fusion, and 0.68 with probability 0.14 when the agent reconciles canonical RNG, numeric ordering and transition lifetimes. ParallelKernelBench motivates a large integration-failure mode; its reported rates are not copied into these subjective probabilities. ESTIMATED single=0.86×0.33+0.14×0.68=0.38, range 0.33–0.68; bo4=0.33+0.35(1−0.86^4)=0.49; pass@4=1−0.86^4=0.45; ub95=0.68. The large best-of-four gain follows the discrete integration hurdle. Restarts and calibrated anchors are assumptions; timing noise is unmeasured.

## 5. Verdict under the kill lines
The evidence recipe estimate is CUT. The ANCHORED verdict is CONDITIONAL, FLIPPED CUT→CONDITIONAL, binding ESTIMATED pass@4=0.45, approximately 0.05 below its line. ESTIMATED single/bo4/ub95 margins are 0.32/0.11/0.07. FlashSampling strengthens the *available* attack, but ParallelKernelBench prevents treating multi-rank integration as an automatic agent capability. The condition also requires measurable native reserve over compact authoritative selection; without it the task has no meaningful reference target.

## 6. Redesign
Class (a): mature distributed serving and sampling primitives. REDESIGNABLE. Make the target an exact vocabulary-sharded sampler with disclosed top-k/top-p constraints, dynamic request migration and backend transitions. Supply full configuration histories and a canonical RNG/cumulative-probability contract. Put normalized admission, authoritative token broadcast, shared request-position counters and compatible fused sampling in the floor. Reward complete service throughput after full-sequence verification, with real matched topology and no fictional full-logit communication charge.

The strongest re-attack combines hierarchical candidate summaries, fused projection/sampling and safe authoritative fallback. The intended residual is choosing when a global truncation boundary requires additional shard information while preserving canonical draws across migration. A frontier lab would benefit from that capability, but a measured stronger exact control must first establish feasibility and reserve.

ESTIMATED redesigned outcomes 0.21/0.44/0.66 at probabilities 0.33/0.59/0.08 represent broken transitions, safe local improvements and successful exact global coordination. ESTIMATED single=0.33×0.21+0.59×0.44+0.08×0.66=0.38; bo4=0.21+0.23(1−0.33^4)+0.22(1−0.92^4)=0.50; pass@4=1−0.92^4=0.28; ub95=0.66. Basis LITERATURE-ONLY. Risks: distributed top-k may already be sufficient, or canonical arithmetic may erase all fusion benefit. Neither can be fixed by quietly weakening semantics.

ESTIMATED decisive budget: 8B subject over four H100 ranks; three sampler arms × three workload/RNG seeds × 1.5 cluster-hours × four devices=54 H100-GPU-h. Receipt verification, transition coverage and repeated timing add ten, total 64. A single-GPU timing test cannot replace this topology.

## 7. Measurement status
Rollouts UNMEASURED (planned: full distributed sampler development attempts). Grader noise UNMEASURED (planned: fixed-RNG sequence replay plus interleaved topology-matched timing). Score ladder UNMEASURED (planned: repaired authority, compact receipts, canonical shared RNG, fused selection and stronger exact sharded control).

## Audit record
id: C060
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.84
old_bo4: 0.91
old_pass4: 0.99
old_ub95: 0.98
new_single: 0.58
new_single_range: 0.37-0.76
new_bo4: 0.70
new_pass4: 0.68
new_ub95: 0.76
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Establish exact sharded truncation and migration reserve beyond authoritative receipts and compatible fused sampling.
redesign_single: 0.38
redesign_bo4: 0.50
redesign_pass4: 0.28
redesign_ub95: 0.66
redesign_gpuh: 64
attack_basis: LITERATURE-ONLY
demonstrated_ref: InferenceBench, Opus 5.5 Max Claude Code, 2026; ParallelKernelBench, GPT-5.5, 2026
gap_to_attack: canonical sampler semantics across multi-rank backend transitions
subfield_sota_ref: exact fused TP sampling up to 10 percent TPOT reduction, FlashSampling Ruiz et al., 2026
anchored_single: 0.38
anchored_bo4: 0.49
anchored_pass4: 0.45
anchored_ub95: 0.68
anchored_verdict: CONDITIONAL
anchored_binding_line: pass4>0.50
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
