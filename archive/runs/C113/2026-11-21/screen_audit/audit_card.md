# C113 — An agent that upgrades its numerical debugging instrument — screen audit
## 1. What the screen claimed
The screen CUT, category TRAIN, combined scale-aware comparison, first-divergence localization, bounded tensor capture and selective wider replay, with generic stable replacement as a bypass. ESTIMATED single/bo4/pass@4/ub95 were 0.61/0.71/0.77/0.88. Sources: https://arxiv.org/abs/1705.10416, https://arxiv.org/abs/2102.12782 and https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/.
## 2. Evidence audit
Finding Root Causes of Floating Point Error with Herbgrind — Alex Sanchez-Stern, 2017, revised 2018 — first URL, fetched, establishes shadow computation and numerical attribution. NSan: A Floating-Point Numerical Sanitizer — Clement Courbet, 2021 — second URL, fetched, provides LLVM-based numerical debugging. Compute Sanitizer — NVIDIA, documentation accessed 2026, publication date unspecified — third URL, fetched, diagnoses memory/race problems rather than floating-point accuracy.

Grade PARTIAL. These methods support instrument design, but neither CPU shadow system demonstrates a GPU tensor debugger that preserves dispatch and improves a reset research agent's learning repairs. Local numerical disagreement may be harmless, while an apparently smaller update error may redirect later optimization. The final diagnosis-to-repair-to-learning link is a separate empirical claim.
## 3. Research done now
- Numerical Errors, CUDA Graph Best Practices for PyTorch — NVIDIA, current docs accessed 2026, original year unspecified — https://docs.nvidia.com/dl-cuda-graph/latest/troubleshooting/numerical-errors.html — fetched — graph execution can alter numerical behavior without an explicit exception, reinforcing actual-path validation.
- Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference — Jiayi Yuan, 2025 — https://papers.nips.cc/paper_files/paper/2025/hash/f80094a824ba5912d4a2de169c404a40-Abstract-Conference.html — fetched — changing hardware/batching can change outcomes, weakening naive inference from wider replay.
- CUDABeaver: Benchmarking LLM-Based Automated CUDA Debugging — Shiyang Li, 2026 — https://arxiv.org/html/2605.08455v1 — fetched — real broken kernels expose weak iterative repair and performance-destroying substitutions, directly cutting against the generic stable-repair bypass.
- GPT-6.2 System Card — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — high research-debugging rubric credit raises the diagnosis baseline, without measuring repaired learning.
- From GPU to TPU with Coding Agents: What Works, What Fails, and What It Costs — Hui Sun, 2026 — https://arxiv.org/html/2610.34422v2 — fetched — agent migrations can run successfully while silently changing training quality; human interventions limit its autonomy evidence.

Search covered numerical accuracy, low-precision training and autonomous CUDA repair. Eight cited sources were fetched; unavailable timing details remain unknown rather than estimated measurements.
## 4. Re-estimated attack
Use real-path captures, cancellation/scale diagnostics, divergence bisection, and selective arithmetic references, then ask the reset agent to test small causal repairs. ESTIMATED central recovery credits are 0.23 from localization, 0.18 from scale/precision diagnosis and 0.13 from validated repair selection: total 0.54. This concerns useful learning gain above the competent debugger floor, not a count of detected differences. Generic precision promotion remains legal, but its cost must be charged and it must beat a properly optimized stable baseline.

ESTIMATED complete-run outcomes 0.32/0.54/0.78 have probabilities 0.25/0.57/0.18. The low case finds symptoms but changes dispatch, the middle fixes familiar numerical incidents, and the high case preserves the causal failure while selecting a productive repair. Mean=0.53, range 0.32–0.78. Bo4=0.78−0.24×0.82^4−0.22×0.25^4=0.67; p=0.18 gives pass@4=1−0.82^4=0.55; q95=0.78. Instrumentation interference and repair choice cause the broad distribution; ordinary tensor-comparison determinism does not remove agent/learner variance. The old mean and tail overstate how automatically localization produces learning.
## 4A. Demonstrated capability and subfield SOTA
NSan/Herbgrind remain verified mature numerical-analysis comparators, while NVIDIA's actual-path advice addresses GPU-specific behavior. Yuan's LayerCast is a concrete stability response for inference, not a universal training repair. No verified leaderboard ranks reusable GPU numerical instruments by downstream research-agent learning gain. Therefore the task reference must outperform these tools and a generic stable implementation in the same instrument-to-learning experiment. R≈1 cannot be anchored to diagnosis coverage alone.

Two demonstrated model results pull in opposite directions. OpenAI reports GPT-6.2 Astra at 81.85% mean rubric credit on internal research debugging, covering real experimental failures. Scaffold internals, runtime and accelerator consumption for that row are not reported; identifying/explaining a resolution is easier than executing a reusable instrument and validating learning. CUDABeaver's GPT-5.4 fixer obtains 17.1% debug recovery under a five-attempt feedback loop, with 29.1% pass@5 in its default snapshot. The paper mentions RTX PRO 6000/H200 while its reproducibility appendix distinguishes a Blackwell pilot and future expanded hardware coverage; full-campaign compute/time are unresolved. It demonstrates constrained kernel repair, not autonomous debugger construction.

KNOWN-RECIPE supports selective shadow replay. AGENT-DEMONSTRATED does not cover the full instrument intervention with reset-agent evaluation within twelve hours. attack_basis=LITERATURE-ONLY. The key missing work is validating a diagnostic counterfactual that preserves low-precision execution and actually improves learning after repair. Sun's human-assisted migrations supply a warning, not another unaided success.

ANCHORED ESTIMATED distribution: 0.23/0.45/0.70 at masses 0.30/0.58/0.12. Typical credits become 0.21 localization, 0.15 diagnosis and 0.09 verified useful repair. Mean=0.41, range 0.23–0.70; bo4=0.70−0.25×0.88^4−0.22×0.30^4=0.55; pass@4=1−0.88^4=0.40; q95=0.70. The probabilities are assumed, particularly transfer from supplied-bug debugging to instrument development. They are not derived by mapping rubric percentages into reward.
## 5. Verdict under the kill lines
Section 4 gives CUT, bo4 approximately 0.07 over. ANCHORED verdict CONDITIONAL, FLIPPED CUT→CONDITIONAL: bo4 margin is approximately 0.05 and ub95 margin 0.05. The newer evidence shows substantial diagnosis competence but also performance-sensitive repair failures, making a straightforward mature-tool kill less certain than the screen claimed. A specific interaction family and causal tool ablation are required before proceeding.
## 6. Redesign
Class (a), mature numerical tooling/training repairs. REDESIGNABLE. Use provenance-backed training incidents where scale changes, fused reduction behavior and optimizer state interact; expose permitted tensor probes and reproduce the failure on the real dispatch. Generic precision promotion and stable operator replacement remain permitted and explicitly costed. Grade held-out learning after a reset agent uses the debugger, with an ablation removing only its proposed diagnostic capability.

The combined attack uses selective shadow arithmetic, first divergence, scale perturbations and stable replacements. It falls short when the earliest visible mismatch is benign and the harmful accumulated state is revealed only by a targeted intervention. Supply predictive dev incidents so that localization is a scientific inference problem rather than guessing a secret bug catalogue. A frontier lab would value tools that distinguish consequential numerical drift from harmless implementation differences. Residual risk: a conservative optimizer/precision policy may recover nearly all utility without the instrument.

Redesign attack basis LITERATURE-ONLY. ESTIMATED 0.20/0.40/0.61 outcomes at 0.28/0.65/0.07 yield mean 0.36; bo4=0.61−0.21×0.93^4−0.20×0.28^4=0.45; pass@4=1−0.93^4=0.25; q95=0.61. ESTIMATED decisive budget: 1B learner and fixed 4B diagnostic agent, four instruments × two mechanisms × two seeds × four hours × one H100=64 GPU-h; captures/replays=16; agent inference=16; final learning and repeat grades=16. Total 112 H100 GPU-h, subject to confirming this continuation length exposes the real mechanism.
## 7. Measurement status
Rollouts UNMEASURED (planned: independent instrument construction followed by reset-agent repair). Grader noise UNMEASURED (planned: replay captures and repeat agent/learner seeds). Score ladder UNMEASURED (planned: starter comparison, mature sanitizer, selective replay, generic stable repair, causal instrument and stronger feasible recovery).
## Audit record
id: C113
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 5
sources_fetched_count: 8
old_single: 0.61
old_bo4: 0.71
old_pass4: 0.77
old_ub95: 0.88
new_single: 0.53
new_single_range: 0.32-0.78
new_bo4: 0.67
new_pass4: 0.55
new_ub95: 0.78
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Require actual-dispatch causal numerical probes and ablate their effect on learning repairs across optimizer-state interactions.
redesign_single: 0.36
redesign_bo4: 0.45
redesign_pass4: 0.25
redesign_ub95: 0.61
redesign_gpuh: 112
attack_basis: LITERATURE-ONLY
demonstrated_ref: Internal Research Debugging, GPT-6.2 Astra, 2026; CUDABeaver, GPT-5.4, 2026
gap_to_attack: reusable numerical instrument causally improving reset-agent learning repairs
subfield_sota_ref: NSan, Courbet, 2021; Herbgrind, Sanchez-Stern, 2017/2018; CUDA Graph numerical guidance, NVIDIA, accessed 2026
anchored_single: 0.41
anchored_bo4: 0.55
anchored_pass4: 0.40
anchored_ub95: 0.70
anchored_verdict: CONDITIONAL
anchored_binding_line: none
anchored_flip: CUT->CONDITIONAL
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
