# C087 — Prior-support diagnostics that unlock genuinely new RL behavior — saturation screen
## 1. What the grader actually rewards
The executable outcome is post-training success coverage over fresh mechanism combinations, with the diagnostic used to select exploration training. R≈0 means no coverage improvement beyond a competent exploration/curriculum floor, and R≈1 means an attainable policy covering the protected compositions. Provisionally the unchanged policy is ESTIMATED R=0.00 and the reference is ESTIMATED R=0.60; finite absence of initial successes cannot establish mathematically zero prior support and must not create a separate novelty bonus.
## 2. Strongest lawful combined attack
Use the support, entropy and prompt-distribution analysis in verified [Demystifying RL Post-Training](https://arxiv.org/abs/2608.24949) to stratify base-policy sampling, then adapt sampling temperature and prompt diversity before declaring a precursor missing. Combine that audit with verifier-filtered self-training in the style of [STaR](https://arxiv.org/abs/2203.14465), curriculum over legal simpler mechanisms, entropy-preserving RL and replay of newly successful compositions. The stack learns from training successes and authorized precursors; it never consumes protected final solutions.

A larger researcher could also use a symbolic training-only solver where the task interface permits one, execute its candidate traces and distill valid demonstrations. That is a lawful baseline rather than an exploit. The difficult remainder is choosing informative precursors when apparently similar mechanism families need different missing representations, especially when expensive support sampling competes with the training budget. ESTIMATED single-run R=0.47, range 0.26–0.64; ESTIMATED best-of-4=0.57; ESTIMATED pass@4 at R≥0.60=0.29; ESTIMATED projected upper-95% bound=0.72. Those values assume the metric rewards actual transferable coverage. A novelty score based simply on “not seen before” could be saturated by rare preexisting trajectories and would require immediate redesign.
## 3. Other routes
- Verifier-filtered self-training with an easy-to-hard curriculum is ESTIMATED R=0.40, range 0.20–0.60. It can expand measured coverage without estimating the full prior support at all.
- Sweep entropy coefficients, temperatures, precursor mixtures and replay frequencies with shared-budget sampling: ESTIMATED R=0.44, range 0.22–0.63. Search is useful, but repeated expensive base audits reduce the number of policy updates available.
- Training-only program synthesis followed by imitation is ESTIMATED R=0.45, range 0.18–0.68 when authorized examples expose executable semantics. Its broad range reflects whether demonstrations generalize to the protected mechanisms rather than merely fitting training layouts.
## 4. What would lower lawful saturation
Define discovery operationally as independently verified transfer to withheld mechanism compositions, accompanied by uncertainty-aware baseline support estimates; remove any claim that sampling proves support is exactly absent. Require the diagnostic to beat a matched-compute curriculum that receives the same precursor access, and include solver-generated demonstrations in that baseline. ESTIMATED attack could drop to R=0.37–0.50. ESTIMATED author effort is two weeks and ESTIMATED additional validation is 128 H100 GPU-h. The exact required change is the observable transfer metric plus a causal diagnostic ablation, not simply increasing the number of rollout samples until a desirable novelty label appears.
## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 14 GPU-h. Revised ESTIMATED total: 352 H100 GPU-h. Assume an ESTIMATED 7B subject, with ESTIMATED 4 training strategies × 2 seeds × 4 H100s × 8 hours = 256 GPU-h; baseline-support generation adds ESTIMATED 64 GPU-h and protected transfer evaluation adds ESTIMATED 32 GPU-h. All generated trajectories, including failed support probes, are charged. A smaller ESTIMATED 1B model can debug the harness, but cannot substitute for the decisive scale if the missing mechanism is already present there. The old number omits both the support audit and substantial independent post-training.
## 6. Duplicate check
Catalog T06 — MODERATE: its inspected packet preserves coverage and repeated-run reliability, whereas this artifact diagnoses precursor support to direct exploration. v3 02A — MODERATE: its opened task learns beyond a success frontier using intermediate signals, but does not make a support-measurement instrument the submitted intervention. These are close conceptual neighbors, not demonstrated same-intervention duplicates; excluded parameter-combination routes in historical sources are disregarded.
## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 and upper-bound margins are each 0.03. Require transfer-defined discovery, support uncertainty and a matched diagnostic-versus-curriculum ablation with lawful training-only demonstrations included. Finite sampling novelty by itself cannot sustain this card's scientific claim.
## 8. Measurement status
Rollouts UNMEASURED (planned: support-guided training and demonstration/curriculum bypasses); grader noise UNMEASURED (planned: base-sampling and training-seed replication); score ladder UNMEASURED (planned: unchanged policy, resampling, self-training, diagnostic reference and attainable transfer control).
## Screen record
id: C087
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.47
attack_single_range: 0.26-0.64
bo4_est: 0.57
pass4_est: 0.29
ub95_est: 0.72
gpuh_old: 14
gpuh_new_est: 352
duplicate_of: catalog T06 MODERATE; v3 02A MODERATE
kill_reason: novelty requires observable transfer and matched diagnostic ablation
souping_flag: no
