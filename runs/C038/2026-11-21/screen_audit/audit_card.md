# C038 — Make decoding batch-invariant without widening the whole model — screen audit
## 1. What the screen claimed
A compatible batch-invariant backend, fixed-order reductions, stable kernel choices and targeted fallback were treated as a near-direct replacement. The screen's ESTIMATED single/bo4/pass@4/ub95=0.87/0.92/0.99/0.99 gave CUT/SYS because public deterministic runtime support supplied the intervention. Its URLs were:
- https://docs.vllm.ai/en/v0.31.0/features/batch_invariance/
- https://docs.vllm.ai/en/latest/api/vllm/model_executor/determinism/batch_invariant/

## 2. Evidence audit
Both pages expose actual batch-invariant execution machinery; this is more concrete than an unsupported algorithm name. However, documented operator invariance does not ensure that cache splits, engine dispatch and an independently prescribed arithmetic contract agree everywhere. Grade: PARTIAL: a compatible replacement is well supported, but the screen did not establish its compatibility or efficient full-engine behavior on near-tie inputs. Newly fetched formal and agent research makes those distinctions testable instead of hypothetical.

## 3. Research done now
- Batch Invariance — vLLM project, 2026 versioned documentation — https://docs.vllm.ai/en/v0.31.0/features/batch_invariance/ — fetched — The mode covers supported models and execution paths, raising confidence that basic batch dependence is removable without single-request service.
- batch_invariant implementation reference — vLLM project, 2026 — https://docs.vllm.ai/en/latest/api/vllm/model_executor/determinism/batch_invariant/ — fetched — Fixed execution/accumulation machinery is available for inspection and reuse. It does not by itself establish agreement with every legal declared arithmetic convention.
- God Does Not Play Dice: Enforcing Batch Invariance in Agentic Kernel Generation — Youwei Bao et al., 2026 — https://arxiv.org/html/2610.36623v1 — fetched — BIEvolve adds static/dynamic invariance gates to kernel agents and materially improves final invariant-kernel success while retaining speed. This directly raises the autonomous attack rather than merely supplying another human recipe.
- Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed — Peixu Xin et al., 2026 — https://arxiv.org/abs/2611.10611 — fetched — Controlling dispatch dependencies yields invariant multi-GPU serving close to ordinary latency on evaluated dense and MoE deployments. The attainable subfield frontier is substantially stronger than conservative invariant mode.
- Vosti: Specifying, Implementing, and Verifying Deterministic LLM Inference — Jianxing Qin et al., 2026 — https://arxiv.org/abs/2609.38981 — fetched — Finds production-mode logit inconsistencies under execution changes, then provides a verified engine specification and implementation. This lowers blind faith in flags while strengthening a principled correctness baseline.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou with eighteen coauthors, 2026 — https://arxiv.org/html/2611.16591v2 — fetched — Its completed serving-engine demonstrations support integration of individually validated numerical components; invariance is an additional objective, not a result inferred from throughput.

## 4. Re-estimated attack
Use ESTIMATED opportunity shares 0.60 replacing serial/conservative execution, 0.25 dispatch/graph tuning and 0.15 exact-contract edge cases. Recovery fractions ESTIMATED 0.98/0.85/0.37 give 0.60×0.98+0.25×0.85+0.15×0.37=0.86. The residual deliberately includes upstream numerical drift that a final-logit near-tie check cannot repair.

ESTIMATED recipe scores 0.76/0.85/0.90 occur with probabilities 0.10/0.60/0.30. Once compatibility is established, a mature deterministic path makes outcomes relatively concentrated; remaining variation comes from profiling and model-shape coverage. ESTIMATED single=0.10×0.76+0.60×0.85+0.30×0.90=0.86, range 0.76–0.90; bo4=0.90−0.05×0.70^4−0.09×0.10^4=0.89; pass@4=1−0^4=1.00 as p=1.00; ub95=0.90. The small best-of-four gap follows this narrow distribution. It differs from the screen's broad tail because the real uncertainty is compatibility, rather than an almost arbitrary projected perfect score.

## 4A. Demonstrated capability and subfield SOTA
Detent is the best full-serving performance result consulted: its reported latency is close to stock while maintaining batch-invariant outputs on large dense/MoE deployments. Vosti supplies stronger specification discipline, with a different performance point. Anchor the reference to the faster compatible invariant configuration from these systems; R≈1 requires an attained improvement beyond it. A serial starter cannot define a serious research floor, and native headroom may already be exhausted.

Two fetched demonstrations concern the actual attack components. Bao et al.'s BIEvolve uses Gemini 3.7 Flash inside K-Search/Iterative/Evolve agents on H100 NVL, with twenty or twenty-five optimization turns. It reports improved batch-invariance pass rates with substantial speed retention; elapsed search hours are unspecified. Zhou et al.'s Singularity-Bench gives Opus 5.5+Claude Code twelve hours on four GB300s and demonstrates a serving engine above SGLang's income. Together they establish invariant kernel optimization and integrated serving, while their combination under this arithmetic oracle remains untested.

KNOWN-RECIPE and AGENT-DEMONSTRATED overlap here more closely than elsewhere in this batch. attack_basis=DEMONSTRATED-AGENT for the comparable serving/kernel capability, not a claim that this card has been run. A twelve-hour agent still must check the declared arithmetic convention and cache transitions. The quantitative forecast assumes that convention matches a public invariant family; the verdict therefore rests on that explicit compatibility assumption.

ANCHORED ESTIMATED R=0.68/0.79/0.84 at probabilities 0.12/0.63/0.25 represents conservative integration, successful invariant serving and useful dispatch tuning. ESTIMATED single=0.12×0.68+0.63×0.79+0.25×0.84=0.79, range 0.68–0.84. ESTIMATED bo4=0.84−0.05×0.75^4−0.11×0.12^4=0.82; pass@4=1−0^4=1.00 with p=1.00; ub95=0.84. Compatibility failures outside this conditional model must be measured, not called numerical noise.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT at ESTIMATED bo4=0.89. ANCHORED verdict: CUT, UNCHANGED, with ESTIMATED single exceeding its line by 0.09, bo4 by 0.22, pass@4 by 0.50 and ub95 by 0.09. Unlike a literature-only kill, this has direct agent evidence for the invariant-kernel component and matched-budget server integration. Vosti's counterexamples require actual checking; Detent also threatens the existence of enough native research reserve beyond the competent floor.

## 6. Redesign
Cause (a): mature deterministic serving. REDESIGNABLE only by moving beyond invariance inside a fixed deployment: require reproducible inference across disclosed changes in tensor-parallel partition and prefill/cache partitioning while preserving a public arithmetic specification. This targets reproducible distributed RL/debugging after repartitioning. Supply exact operator semantics, executable truth, all layouts in development and adequate memory; do not demand arbitrary agreement with an undocumented vendor kernel.

The strongest attack is Detent-style dispatch stabilization, Vosti-style state invariants, BIEvolve numerical gates and fixed-order collective/reduction kernels. Its fixed-deployment guarantees do not establish equal reduction semantics after sharding changes. A candidate must jointly optimize reproducible accumulation, communication and selective exact replay. A slow legal reproducible implementation must fit the same deployment budget, and a faster independent control must establish reserve above the full public combined floor. Otherwise this redesign is infeasible and should be retired.

Re-attack basis=LITERATURE-ONLY: kernel-generation success has not demonstrated cross-partition exact serving optimization. ESTIMATED scores 0.30/0.49/0.67 with probabilities 0.40/0.50/0.10 yield single=0.40×0.30+0.50×0.49+0.10×0.67=0.43, range 0.30–0.67; bo4=0.67−0.18×0.90^4−0.19×0.40^4=0.55; pass@4=1−0.90^4=0.34; ub95=0.67. This is borderline CONDITIONAL at the best-of-four margin. Generic reproducible BLAS or a canonical layout fallback may still dominate, and a scientifically unnecessary arithmetic restriction would invalidate the design.

Pilot ESTIMATED GPU-h: a 32B decoder on four H100s, five numerical/runtime arms, three input-layout seeds, one hour per execution gives 5×3×1×4=60.00. Add ESTIMATED 16.00 for arithmetic truth and 8.00 for timed-path replay, totaling 84.00 H100 GPU-h; those are future costs, with no kernels executed here.

## 7. Measurement status
Rollouts UNMEASURED (planned compatible public-mode substitutions and partition-changing candidates). Grader noise UNMEASURED (planned repeated exact logit checks alongside serving timing). Score ladder UNMEASURED (planned stock invariant, dispatch-tuned, verified and attained portable-arithmetic paths).

## Audit record
id: C038
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.87
old_bo4: 0.92
old_pass4: 0.99
old_ub95: 0.99
new_single: 0.86
new_single_range: 0.76-0.90
new_bo4: 0.89
new_pass4: 1.00
new_ub95: 0.90
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Preserve disclosed reproducible arithmetic across tensor-parallel and cache partition changes at useful serving throughput.
redesign_single: 0.43
redesign_bo4: 0.55
redesign_pass4: 0.34
redesign_ub95: 0.67
redesign_gpuh: 84
attack_basis: DEMONSTRATED-AGENT
demonstrated_ref: BIEvolve, Gemini 3.7 Flash plus K-Search and iterative/evolution agents, 2026; Singularity-Bench, Opus 5.5 plus Claude Code, 2026
gap_to_attack: invariant kernels and integrated serving are demonstrated separately
subfield_sota_ref: Detent near-stock invariant multi-GPU serving, Xin et al., 2026
anchored_single: 0.79
anchored_bo4: 0.82
anchored_pass4: 1.00
anchored_ub95: 0.84
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
