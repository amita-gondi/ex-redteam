# C097 — A speedup claim that must survive changed training arithmetic — screen audit
## 1. What the screen claimed
The attack replaced the suspect trainer with TorchTitan, checked DDP reduction semantics against receipts, optimized valid execution and confirmed a conservative forecast independently. It assigned ESTIMATED single 0.78, bo4 0.86, pass@4 0.97 and ub95 0.96, then CUT under category DUP because v3 05B already optimizes semantically valid training. The cited URLs were:
- https://github.com/pytorch/torchtitan
- https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html

## 2. Evidence audit
DDP documentation directly supports the concern about summed losses combined with averaged distributed gradients. TorchTitan provides a serious replacement implementation, but neither source shows autonomous receipt reconciliation, faster exact training and calibrated forecasting together. Replacing an incorrect engine can restore validity without creating any time-to-quality gain over the competent valid floor.

Grade: PARTIAL. Arithmetic repair is well grounded; the large reward assigned to subsequent optimization was extrapolated. Duplicate evidence is stronger: the opened local 05B problem, environment, verification and reward sections already require fixed updates, trusted timed-state capture and resumable optimizer semantics.

## 3. Research done now
- *TorchTitan* — PyTorch, 2026 repository snapshot — https://github.com/pytorch/torchtitan — fetched — Confirms a usable full-stack candidate; importing it is not evidence of gain over an already tuned, compatible incumbent.
- *DistributedDataParallel* — PyTorch, 2026 documentation snapshot — https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html — fetched — Explicit gradient-averaging guidance validates the screen's reduction check, while saying nothing about the final optimization reward.
- *TorchTitan Update: New SOTA Models, Performance at Scale, TitanRL* — PyTorch, 2026 — https://pytorch.org/blog/torchtitan-update-new-sota-models-performance-at-scale-titanrl/ — fetched — Contemporary communication and training support raises the replacement floor; heterogeneous model results cannot anchor one exact-update workload's ceiling.
- *Singularity-Bench: Can Agents Build Agents?* — Yang Zhou et al., 2026 — https://arxiv.org/html/2611.16591v2 — fetched — Budget-matched autonomous training succeeds, but architecture and optimizer freedom make its strongest gains inapplicable to an exact-update contract.
- *KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration* — Kaiming Cheng et al./PyTorch, 2026 — https://pytorch.org/blog/kernelagent-hardware-guided-gpu-kernel-optimization-via-multi-agent-orchestration/ — fetched — Verified kernel optimization supports a component attack; whole-trajectory optimizer parity and forecast calibration remain separate work.

## 4. Re-estimated attack
All reward estimates are ESTIMATED on a provisional scale. Sequential contributions are 0.08 from restoring valid arithmetic, 0.42 from compatible fusion/layout/overlap, and 0.19 from workload selection and credible timing. The first allocation must vanish if parity repair is already in the floor. The second is the most optimistic extrapolation: source-backed component performance does not guarantee whole-job benefit. Forecast accuracy deserves only the disclosed utility weight; no unique scalar score exists until that weight is frozen.

Represent literature-level integration with probabilities 0.10 at 0.36, 0.65 at 0.69 and 0.25 at 0.84. These branches distinguish a correct but unimproved replacement, useful systems tuning and a broadly effective optimized graph. ESTIMATED single=0.10×0.36+0.65×0.69+0.25×0.84=0.69, range 0.36–0.84. Bo4=0.36+0.33(1−0.10⁴)+0.15(1−0.75⁴)=0.79; p=0.90 yields pass@4=1−0.10⁴=1.00; ub95=0.84. Variation is integration and workload fit, followed by uncertain full-training timing; measurement noise has not been estimated. The screen's mean and upper bound decline, but the assumed recipe distribution still kills through bo4. These discrete tails are hypotheses, not a confidence interval from executed runs.

## 4A. Demonstrated capability and subfield SOTA
TorchTitan's current supported training stack is a relevant public reference, not a universal speed record. No fetched source supplies the fastest legal process for this card's unspecified model, topology, tolerance and protected quality target. R≈1 and the claim-error tradeoff therefore cannot yet be anchored numerically; a tuned exact trainer and an independently faster parity-valid control must establish them.

Singularity-Bench reports Opus 5.5+Claude Code reaching validation perplexity 12.77 in twelve hours on four GB300s. That published result demonstrates complete training, but its Muon/model-size changes violate C097's fixed arithmetic. KernelAgent reports correct kernels across 250 tasks and a reported average 1.56× speedup over torch.compile on its level-one subset; the fetched article does not identify campaign wall time or the underlying language-model version. It demonstrates local optimization with hardware feedback, not unaided twelve-hour semantic auditing of distributed learning.

Thus KNOWN-RECIPE applies to reduction checks, mature trainers and confirmation timing. AGENT-DEMONSTRATED does not cover their joint exact-training payoff. attack_basis=LITERATURE-ONLY. Remaining autonomous work includes binding receipts to the timed path, preserving moments through every optimization and verifying the claimed gain after the full learning horizon.

The ANCHORED ESTIMATED distribution assigns 0.25 to R=0.23, 0.60 to 0.49 and 0.15 to 0.68. Single=0.45, range 0.23–0.68; bo4=0.23+0.26(1−0.25⁴)+0.19(1−0.85⁴)=0.58; pass@4=1−0.85⁴=0.48; ub95=0.68. Reduced integrated success reflects the permission and validation gaps, not assumed model incompetence. Quantitative saturation remains assumption-dependent; the duplicate decision does not depend on these probabilities.

## 5. Verdict under the kill lines
Section 4 is CUT on ESTIMATED bo4, exceeding its line by 0.19. The ANCHORED numerical forecast alone is CONDITIONAL, with bo4 clearance 0.02 and pass@4 clearance 0.02. The headline ANCHORED verdict nevertheless remains CUT, UNCHANGED, binding on duplicate: 05B's submitted graph, useful-valid-training target and timed state verification encompass this intervention. The added numerical forecast is a valuable reporting requirement, not a separate ML research capability.

## 6. Redesign
DUPLICATE-STAYS-CUT. Class (d), substantive intervention/target duplication. The local source explicitly covers changed loss reductions, optimizer-state preservation and binding actual measured transitions to correctness; C097 would contribute semantic-substitution fixtures and forecast checks to that existing task. Creating a separate task by adding a calibrated-claim term would retain the same experimental object. No redesigned attack or GPU allocation is proposed, because the duplicate exception applies even after the saturation forecast is corrected.

## 7. Measurement status
Rollouts UNMEASURED (planned only within a consolidated 05B study, including mature replacement controls). Grader noise UNMEASURED (planned paired time-to-quality repeats and separate forecast-confirmation runs). Score ladder UNMEASURED (planned parity repair, tuned exact graph and stronger valid execution, with claim weight fixed first).

## Audit record
id: C097
old_verdict: CUT
evidence_grade: PARTIAL
sources_old_count: 2
sources_new_count: 3
sources_fetched_count: 5
old_single: 0.78
old_bo4: 0.86
old_pass4: 0.97
old_ub95: 0.96
new_single: 0.69
new_single_range: 0.36-0.84
new_bo4: 0.79
new_pass4: 1.00
new_ub95: 0.84
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
demonstrated_ref: Singularity-Bench pretraining, Opus 5.5+Claude Code, 2026; KernelAgent, backbone unspecified, 2026
gap_to_attack: unchanged-update optimization with trajectory-bound semantic and forecast validation
subfield_sota_ref: TorchTitan current training systems comparator, PyTorch, 2026
anchored_single: 0.45
anchored_bo4: 0.58
anchored_pass4: 0.48
anchored_ub95: 0.68
anchored_verdict: CUT
anchored_binding_line: duplicate
anchored_flip: none
verdict_rests_on_assumption: no
redesign_attack_basis: na
souping_flag: no
