# C011 — Precision rescue for discrete routing boundaries — screen audit
## 1. What the screen claimed
The screen combined local router widening, stable top-k, uncertain-boundary recomputation and dev tuning, leaving communicated expert tensors narrow. Its ESTIMATED single/bo4/pass@4/ub95 were 0.86/0.91/0.99/0.99; verdict CUT, category TRAIN, because published selective precision appeared to remove the central tradeoff. The cited URLs were:
- https://www.jmlr.org/papers/volume23/21-0998/21-0998.pdf
- https://arxiv.org/abs/2202.08906
## 2. Evidence audit
Switch Transformers demonstrates local float32 routing with narrow communication and comparable learning to wider arithmetic. It does not cover the boundary-dense distributions, transferred-byte constraint or adaptive error-bound implementation proposed here.

ST-MoE's loss interventions may exceed a kernel-only interface. Neither citation establishes the best learning/load trajectory. Grade: PARTIAL: precision repair is demonstrated, while congestion gains and normalized reward remain extrapolations.
## 3. Research done now
- Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity — William Fedus et al., 2022 — https://www.jmlr.org/papers/volume23/21-0998/21-0998.pdf — fetched — Its selective-precision experiment directly strengthens the local-widening attack; it does not establish reward under the proposed transition workload.
- ST-MoE: Designing Stable and Transferable Sparse Expert Models — Barret Zoph et al., 2022 — https://arxiv.org/abs/2202.08906 — fetched — Confirms stability deserves explicit controls, with loss changes treated as conditional on edit permissions.
- DeepSeek-V3 Technical Report — DeepSeek-AI, 2024, revised 2025 — https://arxiv.org/abs/2412.19437 — fetched — Large-scale mixed-precision MoE training makes a blanket claim that narrow expert computation cannot coexist with stability less credible; its complete training stack is broader than the permitted kernel patch.
- Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts — Lean Wang et al., 2024 — https://arxiv.org/abs/2408.15664 — fetched — Demonstrated expert-bias feedback strengthens a redesigned task's lawful baseline; it is not automatically legal in the original numerical-kernel interface.
- When Are Experts Misrouted? Counterfactual Routing Analysis in Mixture-of-Experts Language Models — Youngsik Yoon et al., 2026 — https://arxiv.org/abs/2605.07260 — fetched — Finds token-dependent useful alternatives that standard routes miss, lowering confidence that faithful top-k alone solves utility-aware routing. Its frozen-model reasoning evaluation is counterevidence by mechanism, not a comparable training-transition result.

Search covered router precision and load balancing; Switch offers the closest numerical-repair evidence.
## 4. Re-estimated attack
All reward allocations, probabilities and resource allowances are ESTIMATED. Local wide selection plausibly recovers 0.46 reward; narrow dispatch adds 0.18; threshold/layout search contributes 0.11 marginally. Dense fallbacks, load feedback and unknown native headroom remain.

Represent a full attempt by three outcomes: R=0.58 with probability 0.20 when fallback dominates; R=0.76 with probability 0.55 when straightforward widening works; R=0.88 with probability 0.25 when tuning also removes material overhead. This discretization models workload/implementation uncertainty, with learner seed variation folded into each scenario; grader noise is not known. ESTIMATED single = 0.20×0.58+0.55×0.76+0.25×0.88 = 0.75, range 0.58–0.88. Under independent restart draws, ESTIMATED bo4 = 0.58×0.20^4+0.76×(0.75^4−0.20^4)+0.88×(1−0.75^4) = 0.84. ESTIMATED p=0.80, hence pass@4=1−0.20^4=1.00 rounded; ESTIMATED upper-95% quantile=0.88 because cumulative probability at 0.76 is 0.75.

Compared with the old estimates, single and upper tail fall because no study validates adaptive fallback under the target transition; repeated success remains high because two ordinary implementation outcomes cross the success threshold. The quantile is a forecast of single-run reward, not a fitted S4 scaling confidence bound. Shared instance uncertainty could correlate restarts, so empirical blockwise estimates remain necessary.
## 4A. Demonstrated capability and subfield SOTA
Subfield anchor: DeepSeek-V3 (DeepSeek-AI, 2024/2025, fetched above) demonstrates mixed-precision sparse training at production scale; Switch supplies the closer selective-routing learning comparison. They anchor a native target of wide-router learning quality with narrow communication. Neither establishes this workload's attainable byte/loss frontier, so R≈1 and the reference reward remain uncalibrated, rather than a newly invented superior controller.

- KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration — Kaiming Cheng et al./PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched. The reported Opus-4.5 case uses four workers and eight rounds on H100, improving a matrix-vector kernel over torch.compile; wall time is undisclosed. This demonstrates profile-driven kernel integration, but neither MoE training nor learning-preserving boundary decisions.
- GPT-6.2 System Card, AI self-improvement evaluations — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-used-to-assess-high-ai-self-improvement-capabilities — fetched. Astra's evaluation agent saved a reported 42.87% training time in NanoGPT with two hours and one H100; detailed scaffold configuration is unreported. It validates training-code optimization, leaving expert-routing dynamics and charged multi-device transition validation untested.

KNOWN-RECIPE precision rescue is established; AGENT-DEMONSTRATED end-to-end rescue on comparable sparse training is absent. attack_basis=LITERATURE-ONLY. In twelve hours the attacker must integrate precision changes and verify post-transition loss, not merely pass a kernel oracle. This missing transfer makes the headline verdict assumption-dependent.

ANCHORED ESTIMATED R distribution: 0.31/0.50/0.69 with probabilities 0.30/0.60/0.10, reflecting failed trajectory validation, effective local repair and successful joint tuning. ESTIMATED single=0.30×0.31+0.60×0.50+0.10×0.69=0.46, range 0.31–0.69; bo4=0.31×0.30^4+0.50×(0.90^4−0.30^4)+0.69×(1−0.90^4)=0.56; pass@4=1−0.90^4=0.34; ub95=0.69. Integration uncertainty explains the downward adjustment; these are not benchmark percentages remapped into reward.
## 5. Verdict under the kill lines
Section 4's recipe-conditioned verdict is CUT. The headline ANCHORED verdict is CONDITIONAL, FLIPPED CUT→CONDITIONAL: ESTIMATED bo4 clears by 0.04 and ub95 by 0.06. KernelAgent and NanoGPT demonstrate nearby engineering competence, but neither measures boundary-heavy MoE learning recovery; retention requires native frontier calibration and a twelve-hour cold integration check.
## 6. Redesign
Potential cause (a): selective precision may consume the frontier. Measure the complete recipe and byte/loss reserve first; this REDESIGNABLE fallback has LITERATURE-ONLY re-attack support, without demonstrated budgeted agent discovery.

Replace numerical fidelity optimization with joint precision and utility-aware routing during observable domain transitions. Expose expert loss probes, router margins and load traces; allow router policy as well as kernels to change. Charge actual device memory traffic, communication, probe work and training compute. Use naturally capacity-constrained expert groups and domain mixtures whose informative rare tokens compete with popular experts. Publish representative transition mechanisms on dev and hold out independently authored mixtures, not undisclosed hardware rules. Reward held-out learning progress per total device time subject to retention and byte constraints; route agreement becomes a diagnostic only.

The floor combines local float32, stable selection, adaptive recomputation, loss-free balancing and layout search. The strongest re-attack adds expert probes and a utility predictor; allocating probes as experts change remains costly. Counterfactual learning value matters for frontier MoE training, with all required signals exposed.

ESTIMATED redesigned outcomes are 0.27/0.45/0.64 with probabilities 0.45/0.49/0.06: predictor overhead dominates, local benefits transfer, or a coupled policy generalizes. ESTIMATED single=0.45×0.27+0.49×0.45+0.06×0.64=0.38; bo4=0.27×0.45^4+0.45×(0.94^4−0.45^4)+0.64×(1−0.94^4)=0.48; pass@4=1−0.94^4=0.22; ub95=0.64 since cumulative mass below that outcome is 0.94. This plausibly clears every line, conditional on attainable reserve. The chief risk is that bias feedback plus a simple margin heuristic already captures the counterfactual value.

Decisive pilot: ESTIMATED 8B-total/1B-active MoE, 4 arms, 3 seeds, 6 hours per trajectory using 4 H100s gives 4×3×6×4=288 H100 GPU-h; ESTIMATED evaluation overhead 32 gives total 320 GPU-h. This compares the complete floor, probing attack, proposed controller and independent stronger control; it is not the full saturation panel.
## 7. Measurement status
Rollouts UNMEASURED (planned paired transition runs with all failed kernels retained). Grader noise UNMEASURED (planned repeated loss and traffic measurements on identical artifacts). Score ladder UNMEASURED (planned native loss/time anchors including the full selective-precision stack and feasible stronger routing).
All reward-valued record entries below are ESTIMATED.
## Audit record
id: C011
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 5
sources_fetched_count: 7
old_single: 0.86
old_bo4: 0.91
old_pass4: 0.99
old_ub95: 0.99
new_single: 0.75
new_single_range: 0.58-0.88
new_bo4: 0.84
new_pass4: 1.00
new_ub95: 0.88
new_verdict: CUT
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Optimize counterfactual learning value and precision jointly under fully charged routing probes and observed domain transitions.
redesign_single: 0.38
redesign_bo4: 0.48
redesign_pass4: 0.22
redesign_ub95: 0.64
redesign_gpuh: 320
attack_basis: LITERATURE-ONLY
demonstrated_ref: KernelAgent, Opus-4.5, 2026; NanoGPT, GPT-6.2 Astra, 2026
gap_to_attack: learning-preserving sparse routing through a capacity transition
subfield_sota_ref: mixed-precision MoE training, DeepSeek-V3, 2024/2025
anchored_single: 0.46
anchored_bo4: 0.56
anchored_pass4: 0.34
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
