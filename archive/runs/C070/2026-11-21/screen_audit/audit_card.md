# C070 — Resolve competing causes of on-policy logprob drift — screen audit
## 1. What the screen claimed
Factorial shape/order/backend probes, immutable rollout identities, a batch-invariant control and selective numerical repair were the old strongest attack; mismatch correction was conditional on objective permission. CUT/EXP used ESTIMATED single 0.75, best-of-four 0.84, pass@4 0.94 and upper-95% 0.95, arguing that standard experiments bypassed the intended diagnosis difficulty. It cited:
- https://docs.vllm.ai/en/latest/features/batch_invariance/
- https://docs.nvidia.com/nemo/rl/nightly/guides/grpo.html

## 2. Evidence audit
The documentation supports available invariance and correction mechanisms, not guaranteed equality between arbitrary trainer and sampler paths. Batch invariance alone omits prefill/decode and cross-device reduction differences; an ordering fix also does not repair arithmetic. The screen's high score lacked a result integrating the needed probes, repair and learning-time evaluation. Grade: PARTIAL, though newly fetched operator-level consistency work is substantially closer than those documentation citations.

## 3. Research done now
I searched current trainer/rollout mismatch research and fetched system reports alongside the original documentation. All reward distributions and proposed costs are ESTIMATED; numerical source results below are reported by their authors.
- Batch Invariance — vLLM project, 2026 documentation snapshot — https://docs.vllm.ai/en/latest/features/batch_invariance/ — fetched — supports a conservative batch-shape control, but not universal engine parity.
- An In-depth Walkthrough of GRPO in NeMo RL — NVIDIA, 2026 snapshot — https://docs.nvidia.com/nemo/rl/nightly/guides/grpo.html — fetched — clarifies correction machinery; it does not authorize changing this card's frozen PPO contract.
- Finish RL Training Faster: Bitwise-Consistent, High-Performance, Agent-Driven — Yan Bai and Ao Shen, 2026 — https://vllm-project.github.io/2026/10/14/train-inference-consistency.html — fetched — directly reports operator alignment, unchanged post-update comparison and substantial retained throughput; human review and missing total-time measurements limit the autonomous saturation inference.
- Unlocking Stable On-Policy RL on TPU with Bitwise-Zero Train–Inference Mismatch — Yuxuan Zhang et al./Google, 2026 — https://developers.googleblog.com/unlocking-stable-on-policy-rl-on-tpu-with-bitwise-zero-traininference-mismatch/ — fetched — demonstrates parity over a multi-host TPU mesh, strengthening feasibility while leaving GPU transfer work.
- GPT-6.2 System Card, Internal Research Debugging — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — actual diagnosis performance supports separating competing causes, but rubric credit does not prove a validated fast repair.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — agents record token sampling probabilities and build mismatch-aware RL training, making the basic controlled-probe attack credible within the time limit.

## 4. Re-estimated attack
ESTIMATED 0.25 of provisional reward can come from correct token/weight identity and replay localization, ESTIMATED 0.22 from shared/invariant numerical paths, and ESTIMATED 0.15 from selectively recovering throughput. These are expected downstream utility gains, not reward for a convincing explanation. Behavior logprobs remain immutable. Treat correction as a separate optional arm only after the task explicitly allows it; this estimate can use exact shared kernels instead.

The recipe-level ESTIMATED mixture is R={0.42,0.64,0.79}, probabilities {0.20,0.55,0.25}. Low outcomes find the fault but incur global-invariance costs; favorable ones isolate a cheap selective repair. ESTIMATED single=0.0840+0.3520+0.1975=0.63, range 0.42–0.79. ESTIMATED best-of-four=0.79−0.15×0.75^4−0.22×0.20^4=0.74. With p=0.80, ESTIMATED pass@4=1−0.20^4=1.00; upper-95%=0.79. Relative to the screen, weaker confidence in complete performance recovery lowers the mean, while explicit outcome probabilities replace its unexplained tail offset.

## 4A. Demonstrated capability and subfield SOTA
The closest GPU system anchor is Bai/Shen's aligned vLLM/Megatron implementation: reported zero discrepancy through 100 DeepSeek-V4-Flash training steps at 91.3% of baseline rollout throughput, followed by a Nemotron hybrid transfer. The authors explicitly leave complete wall-clock gain for later and compare only single baseline configurations. Google's Zero-TIM verifies equality across 64 TPU-v5p chips, an independent feasibility result on different hardware. These anchor a serious exact-consistency control; neither supplies the card's measured R≈1 policy-gain/runtime ceiling.

The report's Agent+skill workflow actually localized divergences and aligned Nemotron operators, but the model identity and autonomous development duration are undisclosed, and humans review baseline, precision choices and progression. The described transport mistake consumed two days. It is therefore a human-supervised system demonstration, not proof of unaided twelve-hour completion.

Two identifiable agent results provide adjacent anchors. OpenAI reports GPT-6.2 Astra at 81.85% mean rubric credit on real research-debugging cases; its public evaluation omits the corresponding runtime and GPU budget, and explanation scores do not imply executed fixes. Singularity-Bench's GPT-6.1 Sol+Codex builds working synchronous RLOO with stored behavior logprobs, FP32 master weights and a mismatch parity gate, reaching 0.530 versus Miles' 0.539 after twelve hours on four GB300s. That demonstrates validation-informed learner construction but permits rejecting mismatched updates instead of eliminating every cause.

KNOWN-RECIPE is now strongly supported; AGENT-DEMONSTRATED coverage does not include the full exact repair/performance campaign in a comparable unaided budget. attack_basis=LITERATURE-ONLY. The remaining challenge is integrating independently useful controls and preserving speed, rather than inventing the factorial experiment.

Anchored ESTIMATED R={0.49,0.58,0.70}, probabilities {0.30,0.53,0.17}, gives single=0.1470+0.3074+0.1190=0.57, range 0.49–0.70. ESTIMATED best-of-four=0.70−0.12×0.83^4−0.09×0.30^4=0.64; pass@4=1−0.83^4=0.53; upper-95%=0.70. The upper atom reflects economical exact alignment, not a grader-noise windfall. Its assumed probability drives the repeated-search cut.

## 5. Verdict under the kill lines
Both forecasts return CUT, anchored UNCHANGED. ESTIMATED anchored best-of-four exceeds 0.60 by 0.04, and pass@4 exceeds 0.50 by 0.03; the single forecast and upper-95% do not breach. Current exact-consistency systems strengthen the attack more directly than the old documentation, but no fetched source calibrates the autonomous probability. The headline is consequently an assumption-dependent CUT with narrow repeated-search margins.

## 6. Redesign
Class (b), REDESIGNABLE. Move the parity checklist into the floor and expose a joint operator/backend scheduling problem across attention and recurrent blocks. The candidate selects an exact shared numerical path per operator and schedules state transport; the objective remains real PPO success per campaign time. Publish all dispatch contracts and provide matching development workloads. Include current shared-kernel alignment, full invariance and a profile-guided static selector as legal controls. Require an attainable selective schedule that measurably outperforms those controls before the task exists.

The stronger attack combines the released consistency recipe with ordinary kernel tuning and static schedule search. What remains is a coupled scheduling choice: an operator's cheap exact path may force expensive layouts in adjacent recurrent blocks. This is useful frontier systems R&D if demonstrated, not merely extra causes on a checklist. Re-attack basis LITERATURE-ONLY. ESTIMATED R={0.30,0.47,0.66}, probabilities {0.35,0.56,0.09}, yields single=0.43, best-of-four=0.66−0.19×0.91^4−0.17×0.35^4=0.53, pass@4=1−0.91^4=0.31, upper-95%=0.66. A compiler finding one universally fast layout is the principal residual threat. ESTIMATED pilot: 3B actor plus required reference/value models, four schedules × three seeds × nine hours × four H100s=432; no-update probes 24 and endpoint evaluation 72 total 528 H100-h. Do not proceed if only crippling the safe control creates reserve.

## 7. Measurement status
Rollouts UNMEASURED (planned independent diagnosis and scheduling attempts); grader noise UNMEASURED (planned fixed repaired PPO campaigns and timing repeats); score ladder UNMEASURED (planned identity fix, exact shared path, invariant stack, static selector and coupled control).

## Audit record
id: C070
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.75
old_bo4: 0.84
old_pass4: 0.94
old_ub95: 0.95
new_single: 0.63
new_single_range: 0.42-0.79
new_bo4: 0.74
new_pass4: 1.00
new_ub95: 0.79
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: b
redesign_status: REDESIGNABLE
redesign_oneline: Optimize coupled exact operator paths and state-transport schedules above complete shared-kernel parity controls.
redesign_single: 0.43
redesign_bo4: 0.53
redesign_pass4: 0.31
redesign_ub95: 0.66
redesign_gpuh: 528
attack_basis: LITERATURE-ONLY
demonstrated_ref: Internal Research Debugging, GPT-6.2 Astra, 2026; Singularity-Bench RLOO, GPT-6.1 Sol+Codex, 2026
gap_to_attack: unaided exact alignment and complete learning-time validation
subfield_sota_ref: bitwise vLLM alignment, Bai and Shen, 2026; Zero-TIM, Google, 2026
anchored_single: 0.57
anchored_bo4: 0.64
anchored_pass4: 0.53
anchored_ub95: 0.70
anchored_verdict: CUT
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
