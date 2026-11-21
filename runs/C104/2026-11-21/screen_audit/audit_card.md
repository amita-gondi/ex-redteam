# C104 — A compression method that changes the optimal curriculum — screen audit
## 1. What the screen claimed
GPTQ/AWQ sensitivity analysis, mixed precision, teacher disagreement sampling and quantization-aware recovery were jointly searched. The screen forecast ESTIMATED single 0.79, bo4 0.86, pass@4 0.98 and ub95 0.96, then CUT in category DUP because T21 already co-designs compressed representation and recovery. The cited URLs were:
- https://arxiv.org/abs/2210.17323
- https://arxiv.org/abs/2306.00978
- https://aclanthology.org/2024.findings-acl.26/

## 2. Evidence audit
GPTQ and AWQ demonstrate strong compression; LLM-QAT demonstrates recovery using generated teacher data. None establishes that a development agent can jointly discover a curriculum responding to changing feature loss, preserve all retention slices and optimize actual packed execution within twelve hours. Measuring teacher disagreement supplies a useful heuristic, not proof that the highest-disagreement samples have the greatest recovery value.

Grade: PARTIAL. Newly fetched autonomous compression evidence substantially strengthens the compression component, while leaving the adaptive learning component unproven. The inspected T21 artifact boundary already includes recovery recipes, training pools, conditional allocation and packed deployment, supporting the screen's independent duplicate finding.

## 3. Research done now
- *GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers* — Elias Frantar et al., 2022, revised 2023 — https://arxiv.org/abs/2210.17323 — fetched — Establishes a strong one-shot compressor, but not curriculum optimization after representation damage.
- *AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration* — Ji Lin et al., 2023, revised 2026 — https://arxiv.org/abs/2306.00978 — fetched — Activation-sensitive allocation makes naive compression a weak floor; it does not settle training-dependent changes in sample value.
- *LLM-QAT: Data-Free Quantization Aware Training for Large Language Models* — Zechun Liu et al., 2024 — https://aclanthology.org/2024.findings-acl.26/ — fetched — Teacher-generated recovery improves low-bit models, validating a major recipe ingredient without showing a dynamic curriculum reversal.
- *ParetoQ: Improving Scaling Laws in Extremely Low-bit LLM Quantization* — Zechun Liu et al., 2025 — https://arxiv.org/abs/2502.02631 — fetched — The reported representation transition between lower-bit regimes supports a real scientific interaction, while also providing a stronger training-aware baseline.
- *CompressionBench: How can your coding agents compress LLMs?* — Xinrui Zhong et al., 2026 — https://arxiv.org/html/2611.06858v1 — fetched — Agents build verified compressed models under explicit storage and time limits. This raises attack credibility much more directly than citing a quantizer repository.
- *TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration* — Xuannan Liu et al., 2026 — https://arxiv.org/html/2611.20430v1 — fetched — Demonstrates training strategy revision, but combining that skill with compression and a moving recovery curriculum remains a separate integration claim.

## 4. Re-estimated attack
The ESTIMATED recipe gain budget is 0.30 for a competent compressed representation, 0.24 for teacher-guided recovery and 0.14 for adapting data allocation and precision to measured losses: single 0.68. Existing papers directly support the first two mechanisms, with weaker support for the last. Packing costs and retention must constrain all three; restoring quality through a hidden full-precision service is outside the allowed solution.

ESTIMATED outcomes place probability 0.15 at R=0.42 for a valid but poorly recovered model, 0.65 at 0.68 for successful conventional joint tuning and 0.20 at 0.85 for effective adaptive recovery. Mean=0.15×0.42+0.65×0.68+0.20×0.85=0.68, range 0.42–0.85. Bo4=0.42+0.26(1−0.15⁴)+0.17(1−0.80⁴)=0.78; p=0.85 yields pass@4=1−0.15⁴=1.00; ub95=0.85. Differences between compression choices dominate run spread, with recovery seeds and packed-runtime interactions contributing secondary variation. The old mean and bo4 were too high, but the recipe-level distribution remains above the kill boundaries. No measured seed variance or physical ceiling is being claimed.

## 4A. Demonstrated capability and subfield SOTA
ParetoQ reports a ternary 600M model outperforming its previous ternary 3B comparator; that is an actual human-built compression/training advance, not a general guarantee for the present model. CompressionBench includes released quantizations and stronger agent artifacts at matched package limits. Its comparison is the closest fetched deployment reference, but neither it nor ParetoQ anchors an optimum for C104's unspecified retention and recovery costs. R≈1 needs an independently attainable compressed-and-recovered control in those native units.

Two distinct CompressionBench agent results are directly relevant. Sonnet 5.5+Claude Code obtains Qwen3.8-27B PPL 3.253 at the looser storage limit; Opus 5.5 in the same scaffold obtains 3.272. Each receives eight hours and one H200 NVL; the paper reports verified executable artifacts. Those measurements demonstrate autonomous compression design at larger scale than the proposed small recovery pilot. They do not demonstrate discovering a changing curriculum, and decode speed is outside that benchmark's reward. Treating their PPL scores as C104 reward would be invalid.

KNOWN-RECIPE covers quantization and recovery; AGENT-DEMONSTRATED covers compression, not the entire adaptive curriculum attack. Therefore attack_basis=LITERATURE-ONLY for the combined claim. TrainExplorer adds corroboration for training agency, but separate demonstrations cannot be multiplied into a proven integrated result. The missing twelve-hour step is diagnosing changing recovery value and validating retention on the actual compressed execution path.

ANCHORED ESTIMATED probabilities 0.25 at 0.25, 0.60 at 0.54 and 0.15 at 0.74 give single 0.50, range 0.25–0.74. Bo4=0.25+0.29(1−0.25⁴)+0.20(1−0.85⁴)=0.63; pass@4=1−0.85⁴=0.48; ub95=0.74. CompressionBench supports preserving a consequential upper branch, while the unverified curriculum integration lowers its frequency. These reward and probability mappings remain assumptions.

## 5. Verdict under the kill lines
Section 4 CUTs through ESTIMATED bo4 0.78 and other lines. The ANCHORED numerical forecast also CUTs, with bo4 approximately 0.03 above its line and ub95 close to its threshold. The headline remains CUT, UNCHANGED, binding on duplicate: T21 explicitly allows the same compression assignments and recovery recipe and grades compressed capability under real resource limits. The published autonomous compression results strengthen saturation concerns without being necessary for that structural decision.

## 6. Redesign
DUPLICATE-STAYS-CUT. Class (d): the scientific artifact and deployment objective duplicate T21. Reading T21's actual interface matters: it does not freeze recovery data into an immutable generic schedule, and its proposed control already adapts recovery to conditional representation damage. C104's desired reversal could be a valuable mechanism-validity instance inside T21, but calling its recovery policy a curriculum does not create an independent task. No duplicate redesign or new GPU-h allowance is proposed.

## 7. Measurement status
Rollouts UNMEASURED (planned joint quantization/recovery/curriculum searches within T21 if consolidated). Grader noise UNMEASURED (planned recovery-seed repeats and independently restarted packed inference). Score ladder UNMEASURED (planned calibrated PTQ, training-aware low-bit recovery, adaptive data selection and stronger same-resource compressed control).

## Audit record
id: C104
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.79
old_bo4: 0.86
old_pass4: 0.98
old_ub95: 0.96
new_single: 0.68
new_single_range: 0.42-0.85
new_bo4: 0.78
new_pass4: 1.00
new_ub95: 0.85
new_verdict: CUT
binding_line: bo4>0.60
flip: none
kill_cause_class: d
redesign_status: DUPLICATE-STAYS-CUT
redesign_oneline: na
redesign_single: na
redesign_bo4: na
redesign_pass4: na
redesign_ub95: na
redesign_gpuh: na
attack_basis: LITERATURE-ONLY
demonstrated_ref: CompressionBench, Sonnet 5.5+Claude Code, 2026; CompressionBench, Opus 5.5+Claude Code, 2026
gap_to_attack: compression-dependent adaptive recovery curriculum with retained-skill validation
subfield_sota_ref: ParetoQ low-bit training, Liu et al., 2025; CompressionBench packed comparisons, Zhong et al., 2026
anchored_single: 0.50
anchored_bo4: 0.63
anchored_pass4: 0.48
anchored_ub95: 0.74
anchored_verdict: CUT
anchored_binding_line: duplicate
anchored_flip: none
verdict_rests_on_assumption: no
redesign_attack_basis: na
souping_flag: no
