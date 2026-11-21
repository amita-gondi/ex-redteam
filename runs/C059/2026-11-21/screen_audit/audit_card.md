# C059 — Grammar staging after the public fix is already applied — screen audit
## 1. What the screen claimed
The screen advocated whole-backend XGrammar-2 replacement, request-stable parser ownership, reusable staging, overlap and full-versus-delta-mask tuning. Its ESTIMATED single/bo4/pass@4/ub95=0.86/0.92/0.99/0.99 led to CUT, category SYS, on the argument that dynamic grammar support already addressed the residual beyond allocation repair. Old citations:
- https://arxiv.org/abs/2411.15100
- https://arxiv.org/abs/2601.04426
- https://github.com/vllm-project/vllm/issues/49013

## 2. Evidence audit
The source issue exists and reports the staging regression; this audit did not reproduce it. XGrammar demonstrates efficient constrained generation, and XGrammar-2 directly covers within-request structural switching and cross-grammar reuse. Those are materially closer to the card than generic caching citations. However, the complete batch-reorder ownership integration and its gain above an already repaired floor are not demonstrated by the old sources.

Grade: PARTIAL. The human-built dynamic-engine replacement is well supported on its own workload. The claimed near-certain frontier-agent solve and normalized reward above 0.80 were not backed by an unaided integration trial or a measured attainable reserve. “For agentic LLMs” describes workloads, not an agent that invented the engine.

## 3. Research done now
Every audit reward prediction, scenario mass and proposed hardware allocation is ESTIMATED. Source timings and benchmark outcomes remain attributed reports.
- XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models — Yixin Dong et al., 2024, revised 2025 — https://arxiv.org/abs/2411.15100 — fetched — persistent parsing and CPU/GPU overlap support replacing the affected path rather than local allocation tuning.
- XGrammar-2: Dynamic and Efficient Structured Generation Engine for Agentic LLMs — Linzhang Li et al., 2026 — https://arxiv.org/abs/2601.04426 — fetched — dynamic dispatch, shared substructures and adaptive mask caching directly attack changing-schema traffic.
- Structured-output apply_grammar_bitmask staging regression, issue 49013 — vLLM contributors, 2026 — https://github.com/vllm-project/vllm/issues/49013 — fetched — verifies the inherited regression report; provides no independently measured post-fix scientific headroom.
- AutoTuneBench: Trustworthy Measurement for Agent Auto-Tuning of LLM Serving Engines — Li Chen, 2026 — https://arxiv.org/html/2609.18123v1 — fetched — demonstrates how fused ceilings and mismatched baselines can create misleading optimization results; lowers confidence in a large reward reserve.
- KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng et al., PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — profiler-driven kernel improvement raises confidence in a narrow staging optimization, without testing grammar lifetimes.
- RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts — Hjalmar Wijk et al., 2024, revised 2025 — https://arxiv.org/html/2411.15114v2 — fetched — short-loop GPU optimization is demonstrably within agent capability; stateful serving integration is a broader requirement.

## 4. Re-estimated attack
Start from the public allocation repair, then test the latest compatible dynamic parser as a complete replacement. Ensure stable request identity and explicit producer/consumer events before comparing delta masks with full reusable copies. A successful human-integrated path plausibly recovers ESTIMATED 0.31 through parser/cache replacement, 0.23 through identity-safe staging and 0.17 through overlap and profitable mask representation: total 0.71. This is an assumed split of downstream goodput gain; grammar validity earns no standalone reward.

Model the human-integrated mature recipe as ESTIMATED uniform R∈[0.64,0.78]. No rare conceptual breakthrough is required once parser compatibility is solved; variation comes from profitable overlap choices and workload-specific host cost. ESTIMATED single=(0.64+0.78)/2=0.71, range 0.64–0.78. For four uniform draws, ESTIMATED bo4=0.64+0.14×4/5=0.75; every draw clears 0.60, so ESTIMATED p=1.00 and pass@4=1−0.00^4=1.00. ESTIMATED ub95=0.64+0.95×0.14=0.77. This narrower spread produces only approximately 0.04 best-of-four gain, rather than copying the screen's offset.

## 4A. Demonstrated capability and subfield SOTA
The fetched subfield reference is XGrammar-2, reporting over 6× faster grammar compilation than preceding engines and near-zero end-to-end overhead on its dynamic structured-generation workloads. That makes it a mandatory floor/control. It does not give a legal R=1 for the private churn workload: freeze native complete-request goodput after measuring this backend, and reject an anchor whose remaining improvement is only noise or outside deployed resources.

Two agent results constrain implementation forecasts. RE-Bench's o1-preview/AIDE produced a Triton solution beating every human expert; its AIDE evaluations use two-hour attempts on one H100, with larger aggregate budgets selecting across attempts. That demonstrates numeric optimization, not request-lifetime reasoning. KernelAgent's authored orchestration reaches 1.56× mean speedup against torch.compile on its level-one suite using H100 feedback; model identity and fixed whole-run wall budget are not supplied in the fetched account. This supports profiling and local kernels but cannot establish unaided XGrammar integration in twelve hours.

KNOWN-RECIPE is very strong, yet the complete attack_basis=LITERATURE-ONLY. The agent still has to preserve exact decode semantics, cancellation ownership and timing boundaries while adapting an external backend. Treating every human engine result as AGENT-DEMONSTRATED would repeat the screen's central error.

ANCHORED ESTIMATED R is uniform on [0.47,0.63]. Reusable public engines support fairly consistent partial integration; the missing agent demonstration reduces the whole interval rather than introducing an invented discovery bonus. ESTIMATED single=(0.47+0.63)/2=0.55; ESTIMATED bo4=0.47+0.16×4/5=0.60, unrounded 0.5980. ESTIMATED p=(0.63−0.60)/0.16=0.19, using unrounded p=0.1875 in pass@4=1−0.8125^4=0.56. ESTIMATED ub95=0.47+0.95×0.16=0.62. This distribution describes implementation/workload variation, not a measured timing interval; independent restarts and fixed reward anchors remain assumptions.

## 5. Verdict under the kill lines
Evidence re-estimate: CUT. ANCHORED result: CUT, UNCHANGED, binding ESTIMATED pass@4=0.56, approximately 0.06 above its line. Unrounded bo4 remains just below 0.60, while single and ub95 clear their cutoffs. XGrammar-2's directly relevant dynamic semantics support retaining a meaningful upper implementation tail; its frequency is assumed, so this does not demonstrate a measured breach.

## 6. Redesign
Cause class (a), mature structured-serving stack. REDESIGNABLE, with an explicit new workload rather than extra schema churn. Use exact speculative tree decoding where each live branch owns parser state, shares immutable grammar substructures and may be accepted, rolled back or cancelled as verification changes the active frontier. Reward end-to-end exact accepted-token goodput under a realistic memory envelope, including parser cloning, host/device mask work and rollback costs. Publish matching development branch-lifetime semantics and retain complete backend replacement.

The combined XGrammar-2/cache/pinned-staging/identity/event recipe enters the floor. Its strongest extension adds copy-on-write parser trees and adaptive sparse-mask batching. The hypothesized residual is jointly scheduling parser-state materialization and GPU verification so that useful sharing survives changing branch acceptance. No required information is hidden; the reference must demonstrate native throughput reserve against that extension.

ESTIMATED re-attack states 0.31/0.48/0.67 at probabilities 0.19/0.68/0.13 reflect incorrect rollback sharing, safe but expensive trees and useful joint scheduling. ESTIMATED single=0.19×0.31+0.68×0.48+0.13×0.67=0.47; bo4=0.31+0.17(1−0.19^4)+0.19(1−0.87^4)=0.56; pass@4=1−0.87^4=0.43; ub95=0.67. Basis LITERATURE-ONLY, CONDITIONAL near bo4. Risk: persistent parser stacks may make copy-on-write branch handling routine too; that control is decisive.

ESTIMATED pilot budget: 8B target plus 1B draft on one H100, four implementations × three branch/workload seeds × two hours=24 H100-GPU-h; eight hours for independent serial-reference checking, compilation and warmed timing gives 32. This increases the old screen pilot to cover exact branch rollback.

## 7. Measurement status
Rollouts UNMEASURED (planned: full-budget backend integration attempts). Grader noise UNMEASURED (planned: interleaved warmed complete-request timing and token replay). Score ladder UNMEASURED (planned: repaired staging, XGrammar-2, identity-safe overlap, tree sharing and independent stronger exact control).

## Audit record
id: C059
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.86
old_bo4: 0.92
old_pass4: 0.99
old_ub95: 0.99
new_single: 0.71
new_single_range: 0.64-0.78
new_bo4: 0.75
new_pass4: 1.00
new_ub95: 0.77
new_verdict: CUT
binding_line: single>0.70
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Couple exact speculative branch lifetimes to grammar-state sharing and end-to-end mask scheduling.
redesign_single: 0.47
redesign_bo4: 0.56
redesign_pass4: 0.43
redesign_ub95: 0.67
redesign_gpuh: 32
attack_basis: LITERATURE-ONLY
demonstrated_ref: RE-Bench kernel task, o1-preview AIDE, 2024; KernelAgent, model unspecified, 2026
gap_to_attack: exact stateful grammar-backend integration under twelve-hour budget
subfield_sota_ref: dynamic compilation over 6x and near-zero overhead, XGrammar-2 Li et al., 2026
anchored_single: 0.55
anchored_bo4: 0.60
anchored_pass4: 0.56
anchored_ub95: 0.62
anchored_verdict: CUT
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
