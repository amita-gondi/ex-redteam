# C065 — Preserve rotary frequency semantics through low-precision initialization — screen audit
## 1. What the screen claimed
The screen treated canonical high-precision frequency inputs, autocast-disabled phase generation, post-load regeneration and chunked tables as an almost complete inexpensive solution. Its CUT, category SYS, used ESTIMATED single/best-of-four/pass@4/upper-95% of 0.90/0.95/0.99/0.99, reasoning that precision need not be inflated throughout the network. The cited implementations were:
- https://github.com/huggingface/transformers/blob/main/src/transformers/models/dbrx/modeling_dbrx.py
- https://github.com/huggingface/transformers/blob/main/src/transformers/models/gpt_oss/modeling_gpt_oss.py

## 2. Evidence audit
Both fetched files are real implementation evidence for careful rotary phase computation, rather than demonstrations that a model agent repaired every initialization and checkpoint path. Canonical regeneration avoids preserving a huge full-precision cache, but the old forecast also assumes this exhausts the rewarded long-context learning gap. Neither cited file reports that comparison. Grade: PARTIAL: the numerical repair is concrete, while end-to-end reward and twelve-hour autonomous reliability are unsupported.

## 3. Research done now
Searches targeted BF16 rotary failures, lifecycle reconstruction and long-context limitations. All sources below were fetched in this session; forecasts are ESTIMATED and published measurements are explicitly source reports.
- Transformers DBRX implementation — Hugging Face, 2026 main-branch snapshot — https://github.com/huggingface/transformers/blob/main/src/transformers/models/dbrx/modeling_dbrx.py — fetched — provides a transplantable rotary subsystem, strengthening the complete-replacement attack without measuring cold-resume learning.
- Transformers GPT-OSS implementation — Hugging Face, 2026 snapshot — https://github.com/huggingface/transformers/blob/main/src/transformers/models/gpt_oss/modeling_gpt_oss.py — fetched — corroborates selective phase precision as ordinary engineering; it does not establish universal extrapolation quality.
- When Precision Meets Position: BFloat16 Breaks Down RoPE in Long-Context Training — Haonan Wang et al., 2024 — https://arxiv.org/abs/2411.13476 — fetched — documents genuine positional numerical damage and AnchorAttention's training improvements, showing why a buffer-only test would miss relevant behavior.
- RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably — Yufeng Du et al., 2026 — https://arxiv.org/abs/2605.15514 — fetched — identifies intrinsic attention limitations beyond buffer dtype; this cuts against attributing all long-context loss to the repair.
- GPT-6.2 System Card, research assessments — OpenAI, 2026 — https://deploymentsafety.openai.com/gpt-6-2-astra-sol/evaluations-with-challenging-prompts — fetched — strong research-debugging and training-efficiency results support finding precision bugs, but diagnosis credit is not a tested checkpoint repair.
- Singularity-Bench: Can Agents Build Agents? — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — agents integrate low-precision training and inference systems, increasing the plausibility of a straightforward rotary transplant; initialization provenance remains outside the reported objective.

## 4. Re-estimated attack
In a competent-human-recipe scenario, compact canonical storage and regeneration recover ESTIMATED 0.43 of provisional reward, complete phase-path coverage another ESTIMATED 0.18, and cache chunking plus permitted scaling search ESTIMATED 0.09. These contributions concern held-out loss under memory/time limits. Declared dtype correctness is mandatory and should not itself earn gain above a fully corrected floor. Residual loss from attention extrapolation is not automatically accessible to any precision change.

Use an ESTIMATED distribution with R={0.48,0.72,0.82}, probabilities {0.15,0.65,0.20}. The low outcome misses a reconstruction dependency; most runs find a correct compact solution; the high outcome also tunes long-context efficiency. ESTIMATED single=0.072+0.468+0.164=0.70, range 0.48–0.82. ESTIMATED best-of-four=0.82−0.10×0.80^4−0.24×0.15^4=0.78; pass@4=1−0.15^4=1.00, since p=0.85; upper-95%=0.82. The old 0.90 mean overstated evidence for recovering genuine extrapolation loss and understated lifecycle failure risk. Recipe-level CUT nevertheless remains clear.

## 4A. Demonstrated capability and subfield SOTA
The closest same-phenomenon system result is Wang et al.'s AnchorAttention, tested on three LLM types with reported long-context improvements and more than half the training time removed versus full attention. Its changed attention pattern is not equivalent to exact RoPE lifecycle preservation. Du et al.'s newer limitation result further prevents calling regenerated RoPE an optimal long-context solution. The scientifically justified reference is current precise phase construction with cold regeneration, followed by measured legal long-context controls; R≈1 cannot presently be anchored to a published same-contract optimum.

Two agent demonstrations are relevant but incomplete. GPT-6.2 Astra receives logs/code in OpenAI's Internal Research Debugging setup and earns reported 81.85% rubric credit; the public page does not disclose a comparable execution budget or subject GPU allocation for that diagnostic evaluation. It supports locating a rounded dependency, not validating a repaired checkpoint. In Singularity-Bench, Opus 5.5+Claude Code attains pretraining perplexity 12.77 against the Megatron/OLMo reference's 14.17, within twelve hours on four GB300s. Implementing low-precision training is demonstrated; exact cold-reload positional fidelity is not.

KNOWN-RECIPE is exceptionally strong here. AGENT-DEMONSTRATED coverage remains adjacent, so attack_basis=LITERATURE-ONLY rather than claiming an observed lifecycle solve. An agent still has to trace all canonical inputs, defeat blanket casting legitimately, recreate nonpersistent buffers after load and compare functional phases through training.

The anchored ESTIMATED distribution is {0.31,0.50,0.68} with probabilities {0.24,0.58,0.18}. ESTIMATED single=0.0744+0.2900+0.1224=0.49, range 0.31–0.68; best-of-four=0.68−0.18×0.82^4−0.19×0.24^4=0.60 (unrounded 0.59799); pass@4=1−0.82^4=0.55; upper-95%=0.68. These are judgmental transfer forecasts, not percentages inferred from debugging rubric credit. Modest single-run confidence still allows repeated-search saturation.

## 5. Verdict under the kill lines
Both forecasts give CUT. ANCHORED CUT is UNCHANGED versus the screen, but binds on pass@4, ESTIMATED 0.05 above 0.50, rather than the old single-run claim. The decisive evidence is the availability of a compact exact repair plus demonstrated adjacent debugging/training capability; its task-specific discovery probability remains an assumption. Near equality of rounded best-of-four to its line is not treated as an additional breach.

## 6. Redesign
Cause (a), mature precision/lifecycle engineering, is presumptively fixable; this narrower capability is TRULY-DEAD as an independent R&D task. I considered forcing a cache-accuracy frontier, extending contexts and adding additional construction APIs. Compact precise inputs plus on-demand phase regeneration remain lawful under all three, while the surrounding model and activations can retain low precision. Penalizing that route would create an artificial restriction on the solution.

A task that learns new positional representations or changes attention would instead study a different capability, and the cited limitations give no affordable attainable control for such a replacement here. No resistant redesign preserving this contract is established, so redesign re-attack values are na. This does not assert that long-context modeling is solved: it says faithful reconstruction of a small numerical subsystem offers no demonstrated research reserve after the complete repair enters the floor.

A falsifying check on that conclusion is ESTIMATED 192 H100-h: a 1B model, three lifecycle implementations × two seeds × six hours × four H100s=144, plus 48 H100-h of reload continuation and long-context evaluation. This is an unexecuted diagnostic for the existing task, not a redesign budget.

## 7. Measurement status
Rollouts UNMEASURED (planned independent typed-buffer repair agents); grader noise UNMEASURED (planned fixed-artifact cold-resume loss repetitions); score ladder UNMEASURED (planned rounded construction, precise buffer, canonical regeneration and memory-bounded exact phases).

## Audit record
id: C065
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.90
old_bo4: 0.95
old_pass4: 0.99
old_ub95: 0.99
new_single: 0.70
new_single_range: 0.48-0.82
new_bo4: 0.78
new_pass4: 1.00
new_ub95: 0.82
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: a
redesign_status: TRULY-DEAD
redesign_oneline: Compact exact phase regeneration removes the proposed precision tradeoff within this capability.
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: Internal Research Debugging, GPT-6.2 Astra, 2026; Singularity-Bench pretraining, Opus 5.5+Claude Code, 2026
gap_to_attack: autonomous verification of every positional reconstruction path
subfield_sota_ref: AnchorAttention, Wang et al., 2024; precise RoPE implementations, Hugging Face, 2026
anchored_single: 0.49
anchored_bo4: 0.60
anchored_pass4: 0.55
anchored_ub95: 0.68
anchored_verdict: CUT
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: na
souping_flag: no
