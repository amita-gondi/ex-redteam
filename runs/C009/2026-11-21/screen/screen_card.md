# C009 — Optimizer state for episodically reactivated modules — saturation screen
## 1. What the grader actually rewards
The submitted configuration must improve post-reactivation loss while preserving dormant skills at equal active FLOPs. It cannot win by never reactivating an expensive module, and correct serialization alone earns no learning credit. ESTIMATED R≈0 means matching the competent clock/reset baseline and ESTIMATED R≈1 the stronger attainable learning trajectory; unchanged global-clock training is provisionally ESTIMATED R=0.00 and the reference ESTIMATED R=0.60, with native loss anchors absent.
## 2. Strongest lawful combined attack
Implement module-local active-update counters, checkpoint them with first and second moments, and compare explicit elapsed-step decay with frozen moments during inactivity. [Adam](https://arxiv.org/abs/1412.6980) gives the verified underlying recurrence; [PyTorch SparseAdam documentation](https://docs.pytorch.org/docs/stable/generated/torch.optim.SparseAdam.html) explicitly distinguishes sparse moment updates from dense Adam behavior. SparseAdam is a control, not a claim that it already implements the desired dormancy clock.

Combine a local learning-rate warm restart with selective first-moment reset and conservative second-moment rescaling. At reactivation, compare the new gradient's norm and alignment with stored moments; retain useful aligned history and damp conflicting history using a bounded scalar rule expressible through configuration if supported. If the configuration cannot inspect gradients, use dormancy-duration and module-activity statistics instead, and search the resulting threshold policy. Tune these choices together on disclosed activation traces rather than independently picking a “best” clock. Validate cold resume because a counter mismatch can masquerade as an optimization insight.

ESTIMATED single-run R=0.80, range 0.60–0.92; ESTIMATED oracle best-of-4=0.87; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED projected upper-95% envelope=0.97. These are stress forecasts on provisional normalization. The card exposes an ordinary stale-state problem with a small family of legal interventions. Local clocks correct bias correction, restart schedules stabilize the first restored steps, and selective resets reduce harmful historical momentum. A residual persists when earlier moments encode transferable task structure, but the source does not specify an activation-history interaction that defeats the combined control. Matching marginal activation statistics in dev also makes threshold transfer favorable.
## 3. Other routes
- Use per-module update clocks and retain moments unchanged while dormant. ESTIMATED R=0.65, range 0.42–0.83. This solves bookkeeping mismatch and may already recover most native loss reserve.
- Enumerate local/global bias correction, inactive decay convention, reset duration and restart length, then refine promising combinations on short reactivation continuations. ESTIMATED R=0.75, range 0.53–0.90. The low-dimensional search is especially threatening because first-restored-step diagnostics are cheap.
- Reset both moments unconditionally on return. ESTIMATED R=0.48, range 0.24–0.73. It discards beneficial history, but its outcome establishes how much sophistication the task really needs.
## 4. What would lower lawful saturation
Author histories with matched dormancy duration and gradient magnitude but different relationships between earlier and returning tasks, so the correct state action cannot be selected from age alone. Expose causal training evidence sufficient to infer that relationship and require the configuration interface to express a legitimate conditional policy. Keep full stale-state repairs in the committed floor. This could bring the attack to ESTIMATED R=0.47, range 0.25–0.69, costing ESTIMATED several weeks of modular-training asset construction and ESTIMATED 288 additional H100 GPU-h for history-crossed controls. More inactive layers without a different useful-state decision would simply repeat the same fix.
## 5. Decisive-check GPU-h re-estimate
The source's old pilot is ESTIMATED 10 GPU-h. Revised ESTIMATED 264 H100 GPU-h assumes an ESTIMATED 1B-parameter modular language learner, ESTIMATED 5 arms (global, local, elapsed decay, unconditional reset, combined rule), ESTIMATED 3 seeds and ESTIMATED 16 H100-hours per complete dormancy/reactivation trajectory, with ESTIMATED 24 GPU-h for loss, retention and cold-resume checks. Arithmetic: ESTIMATED 5×3×16+24=264. Sparse activity does not make the remaining model's forward/backward work disappear; actual active FLOPs must be measured. The old envelope is suitable for optimizer-unit behavior, not a billions-of-token continuation establishing retained learning.
## 6. Duplicate check
v3 04A (`task_design_v3_codex/04_training_fidelity.md`, source opened): WEAK; asynchronous MoE routing/version/cache fidelity differs from dormancy-aware optimizer schedules. FIX T09 (`fix_packets_v4/T09/packet.md`, source opened): MODERATE, because it explicitly preserves coordinate moments and timestamps through sparse returns, but fixes the optimizer recurrence while optimizing sparse support and execution. C009 changes the clock/reset rule and grades learned loss, so the intervention-target pair is not identical.
## 7. Verdict
CUT. ESTIMATED single-run score exceeds its threshold by 0.10, and best-of-four by ESTIMATED 0.27. This is a useful optimizer-control experiment, but local counters, inactive-decay choices and selective restart search appear capable of saturating its stated mechanism.
## 8. Measurement status
Rollouts UNMEASURED (planned: joint clock/reset search with all training charged). Grader noise UNMEASURED (planned: repeated complete activation histories under paired learner seeds). Score ladder UNMEASURED (planned: unchanged clocks, local clocks, resets, combined rule and independently attainable state policy in native resumed loss).
## Screen record
id: C009
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.80
attack_single_range: 0.60-0.92
bo4_est: 0.87
pass4_est: 0.98
ub95_est: 0.97
gpuh_old: 10
gpuh_new_est: 264
duplicate_of: v3-04A WEAK; FIX-T09 MODERATE
kill_reason: small joint clock-decay-reset search repairs the main failure
souping_flag: no
