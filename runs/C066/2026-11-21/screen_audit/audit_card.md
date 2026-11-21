# C066 — Adam initialization that preserves the real update clock — screen audit
## 1. What the screen claimed
Direct moment/counter allocation, group-local clocks, eager fallback, prefetch and transactional reload were said to nearly construct the solution. The screen returned CUT with SYS as kill category and ESTIMATED single 0.94, best-of-four 0.97, pass@4 0.99 and upper-95% 1.00. Its cited sources were:
- https://arxiv.org/abs/1412.6980
- https://docs.pytorch.org/docs/stable/generated/torch.optim.Adam

## 2. Evidence audit
Adam's algorithm defines the counter's mathematical role; PyTorch documents absent gradients, group addition and state loading, with source code exposing lazy allocation. Those sources make the repair conventional but do not show that lazy allocation yields a large learning-per-runtime gain over the card's explicit-state floor. The screen confused completeness of the correctness repair with saturation of an unmeasured normalized performance range. Grade: PARTIAL, with especially weak evidence for the old near-perfect reward rather than for the state-construction recipe itself.

## 3. Research done now
I searched optimizer initialization, graph-safe warmup and state preservation, and inspected concrete implementation paths. Reward projections below are ESTIMATED; benchmark statistics remain attributed source results.
- Adam: A Method for Stochastic Optimization — Diederik P. Kingma and Jimmy Ba, 2014/2015 — https://arxiv.org/abs/1412.6980 — fetched — separates moment initialization from updates, supporting exact semantics without a dummy decay step.
- Adam documentation — PyTorch, 2026 version 2.15 snapshot — https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adam.html — fetched — the old stable URL redirects here; group loading and None-gradient behavior identify necessary tests rather than a research advance.
- torch/optim/adam.py — PyTorch, 2026 main snapshot — https://github.com/pytorch/pytorch/blob/main/torch/optim/adam.py — fetched — explicit lazy state creation provides an immediately usable implementation model, raising the routine-repair threat.
- Low-precision optimizer initialization advances Adam and applies weight decay before training — DeepSpeed issue #8910, 2026 snapshot — https://github.com/deepspeedai/DeepSpeed/issues/8910 — fetched — verifies the actual constructor failure being discussed; an issue report is not an agent success or a measured speed control.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — leading agents preserve master weights during working RL training, while other agents mishandle reloaded optimizer state; both observations matter for clock fidelity.
- GPT-6.2 System Card, research debugging/training results — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — demonstrates capable diagnosis and training-script improvement, without isolating dormant-group allocation.

## 4. Re-estimated attack
The direct construction path plausibly recovers ESTIMATED 0.36 of the provisional target, exact group identities and load clocks ESTIMATED 0.21, and batched allocation or eager fallback ESTIMATED 0.16. The sum is a recipe-level forecast of useful runtime recovery; initialization parity is a gate, not a separate reward term. It could be much less if initialization costs are amortized over long training, in which case the task lacks native reserve rather than becoming harder.

Model this mature recipe with ESTIMATED outcomes R={0.57,0.74,0.81}, probabilities {0.15,0.65,0.20}. Residual variation comes mainly from whether allocator savings survive activation/reload overhead, with less dependence on learner seed than routing tasks. ESTIMATED single=0.0855+0.4810+0.1620=0.73, range 0.57–0.81. ESTIMATED best-of-four=0.81−0.07×0.80^4−0.17×0.15^4=0.78; p=0.85 gives pass@4=1−0.15^4=1.00; upper-95%=0.81. This lowers all old reward projections because mathematical simplicity does not quantify performance above a correct floor.

## 4A. Demonstrated capability and subfield SOTA
For exact Adam state semantics, the strongest directly relevant public control is PyTorch's current implementation, not a leaderboard of alternate optimizers. It already allocates moments and counters without requiring the erroneous wrapper's initialization step. Adam variants that change update equations are not same-contract references. Anchor R≈0 to that complete explicit-state implementation and measure optimized exact allocation against it; no fetched result establishes the present R≈1 runtime control.

Singularity-Bench's Opus 5.5+Claude Code produces working asynchronous policy training with FP32 master weights, completing 111 updates in twelve hours on four GB300s and reaching performance statistically comparable to Miles. This demonstrates preserving useful small updates through a substantial training scaffold. However, the benchmark does not activate fresh parameter groups or require identical Adam counters after arbitrary resumes; its documented optimizer-reload failures in weaker agents warn against universalizing the success. OpenAI's GPT-6.2 Astra tool-enabled NanoGPT evaluation reports 42.87% baseline training-time saved in two hours on one H100. Its end-to-end optimization result supports quick experimentation, with the remaining gap being exact dormant-state transitions rather than faster dense training.

KNOWN-RECIPE includes direct state construction and correct serialization. Neither demonstration tests the whole activation/resume recipe unaided, so attack_basis=LITERATURE-ONLY. Twelve hours must cover wrapper replacement, master-weight comparisons before the first backward, group-local event traces and an actual runtime gain. The anchored estimate rests on that explicit transfer assumption.

Use anchored ESTIMATED R={0.42,0.59,0.68} with probabilities {0.20,0.55,0.25}. ESTIMATED single=0.0840+0.3245+0.1700=0.58, range 0.42–0.68; best-of-four=0.68−0.09×0.75^4−0.17×0.20^4=0.65. With only the last mode crossing 0.60, ESTIMATED pass@4=1−0.75^4=0.68 and upper-95%=0.68. The substantial medium mass reflects a correct implementation whose performance gain is limited; repeated selection still threatens the task.

## 5. Verdict under the kill lines
The evidence forecast and ANCHORED forecast both say CUT, hence UNCHANGED. The anchored binding line is best-of-four: ESTIMATED 0.65 exceeds 0.60 by 0.05, and pass@4 also exceeds its cutoff. Unlike the old assessment, this does not claim near-certain complete recovery or a demonstrated autonomous solve. It identifies a conventional exact implementation with enough plausible favorable outcomes to fail repeated-search gates under stated assumptions.

## 6. Redesign
Class (a), REDESIGNABLE. Replace constructor debugging with exact optimizer-state residency for conditional training: a sparse 3B-total model activates groups according to disclosed, data-dependent training signals; memory tiers and activation notices are observable. Maintain the original Adam equations and clocks, but permit a residency/prefetch policy to use gradient-activity statistics. Include eager allocation, CPU offload, announced-group prefetch and LRU residency in the floor. Reward held-out learning per full campaign time, charging transfers, replay and policy construction; an exact slower offloaded reference must remain comfortably feasible.

Direct allocation plus eager fallback no longer selects which moments should occupy accelerator memory before future data-dependent activations. The strongest re-attack combines mature offload, activity prediction and a small schedule search; its LITERATURE-ONLY basis has no fetched demonstration of transferable state-residency learning. ESTIMATED R={0.21,0.42,0.63}, probabilities {0.35,0.56,0.09}, yields single=0.37, best-of-four=0.63−0.21×0.91^4−0.21×0.35^4=0.48, pass@4=1−0.91^4=0.31, upper-95%=0.63. Risk: ordinary prefetch may dominate; keep it legal and kill the redesign if so. ESTIMATED decisive cost: three residency arms × three seeds × six hours × four H100s=216 H100-h, plus 40 H100-h of state probes and endpoint evaluation=256 H100-h, using a 3B-total/0.7B-active subject. This is a pilot budget, not spent compute.

## 7. Measurement status
Rollouts UNMEASURED (planned strongest-agent allocator campaigns); grader noise UNMEASURED (planned identical histories with repeated allocation timing); score ladder UNMEASURED (planned dummy-step failure, direct eager, exact lazy, offload/prefetch and learned residency).

## Audit record
id: C066
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.94
old_bo4: 0.97
old_pass4: 0.99
old_ub95: 1.00
new_single: 0.73
new_single_range: 0.57-0.81
new_bo4: 0.78
new_pass4: 1.00
new_ub95: 0.81
new_verdict: CUT
binding_line: single>0.70
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Optimize exact moment residency under observable data-dependent parameter activation with offload and prefetch baselines.
redesign_single: 0.37
redesign_bo4: 0.48
redesign_pass4: 0.31
redesign_ub95: 0.63
redesign_gpuh: 256
attack_basis: LITERATURE-ONLY
demonstrated_ref: Singularity-Bench RL training, Opus 5.5+Claude Code, 2026; NanoGPT, GPT-6.2 Astra, 2026
gap_to_attack: identical dormant-group and resume clocks plus measured allocator gain
subfield_sota_ref: exact lazy Adam state implementation, PyTorch, 2026
anchored_single: 0.58
anchored_bo4: 0.65
anchored_pass4: 0.68
anchored_ub95: 0.68
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
