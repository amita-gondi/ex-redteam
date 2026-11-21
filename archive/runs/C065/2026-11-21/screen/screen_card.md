# C065 — Preserve rotary frequency semantics through low-precision initialization — saturation screen
## 1. What the grader actually rewards
The model must retain declared positional precision through construction, training and cold reload, then achieve useful long-context loss within total memory and time limits. An in-memory frequency table cannot certify a saved model whose reconstruction rounds its inputs. R≈0 is the complete lifecycle-preservation floor and R≈1 the attainable constrained long-context control; all numeric outcomes and allocations below are ESTIMATED, while this loss/memory ladder is UNMEASURED.

The nominal long-context author reference is ESTIMATED R=0.60, a placement unsupported until full lifecycle regeneration leaves a real loss gap.

## 2. Strongest lawful combined attack
Treat rotary frequency construction as an explicitly typed numerical subsystem. Preserve canonical scalar configuration and full-precision frequency inputs outside blanket low-precision initialization, form position products with autocast disabled, and cast only the final rotation factors as permitted by the model contract. This is already visible in public [Transformers DBRX rotary code](https://github.com/huggingface/transformers/blob/main/src/transformers/models/dbrx/modeling_dbrx.py) and [GPT-OSS rotary code](https://github.com/huggingface/transformers/blob/main/src/transformers/models/gpt_oss/modeling_gpt_oss.py), which provide concrete full-precision phase computation patterns. These implementations are verified examples, not measurements on the card.

Install construction and post-load hooks that regenerate derived tables from canonical high-precision inputs; do not merely upcast an already rounded table. Validate nonpersistent buffers, sharded construction, device moves and cold checkpoint reconstruction against an independent phase calculation. Use on-demand or chunked rotation factors to limit long-context cache memory while leaving frequency inputs precise. Then tune the existing allowed positional scaling parameters under the same data and training budget.

ESTIMATED single-run R=0.90, range 0.77–0.97; ESTIMATED best-of-4=0.95; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED upper-95% projection=0.99. These are saturation scenarios relative to a provisional floor, not measured accuracy. The key reason for the high estimate is that preserving a small canonical frequency vector does not broadly inflate model precision; the apparent tradeoff can largely be avoided. Residual context-extrapolation errors may be properties of the model and data, common to every legal repair. Once full lifecycle preservation is correctly included in the floor, the card may have no remaining native research range at all.

## 3. Other routes
A full lifecycle FP32 positional implementation without additional context tuning is the strongest single standard recipe: ESTIMATED R=0.84, range 0.66–0.95. Buffer-only preservation is weaker and should not stand in for this complete control.

Sweep rotation-factor chunking, cache regeneration policy and disclosed scaling settings, validating clean reload after each selected configuration. ESTIMATED R=0.88, range 0.72–0.97. Choosing a public correct implementation wholesale is lawful. A check that merely inspects the saved dtype is a potential shortcut surface, so the forecast assumes the stated functional long-context and reconstruction checks actually run.

## 4. What would lower lawful saturation
A substantive redesign would need a measured phase-accuracy versus rotation-cache bandwidth frontier where on-demand recomputation and precise compact inputs do not remove the cost. Disclose numerical tolerances and hold out position/length compositions with matched development ranges. ESTIMATED revised attack R=0.64–0.80, still likely over a kill line; a new objective may be needed instead of this bug repair. ESTIMATED authoring is 6–10 person-days plus ESTIMATED 384 H100-h for long-context learning checks. More initialization APIs alone do not make precision preservation a research problem.

## 5. Decisive-check GPU-h re-estimate
Old card allocation: ESTIMATED 10 GPU-h. Revised ESTIMATED 384 H100-GPU-h assumes an ESTIMATED 1B model, ESTIMATED 1B continuation tokens with long-context batches, ESTIMATED 3 lifecycle arms×3 seeds×8 cluster-hours×4 H100s=288. Cold-resume continuations and long-context held-out scoring add ESTIMATED 72; initialization, phase probes and memory timing add ESTIMATED 24. Total ESTIMATED 288+72+24=384. Long attention contexts motivate this conservative device-time envelope despite modest parameter count. The old estimate is adequate only for a dtype/phase smoke check, which might already justify cutting before any learning experiment.

## 6. Duplicate check
04B: MODERATE after reading its precision/correction source; both study selective precision with useful learning, but activation-distribution drift is distinct from deterministic positional construction and reload. 05B: MODERATE from its inspected exact-system contract because cold-resume state fidelity and training outcome coincide, though the targeted positional buffer lifecycle is narrower. The source task does not establish the same precise intervention, so this is not a STRONG duplicate cut.

## 7. Verdict
CUT. ESTIMATED single-run reward is 0.20 above the binding line and ESTIMATED best-of-4 is 0.35 above its line. Explicit full-precision phase construction plus canonical regeneration looks like a complete inexpensive repair; the card has not identified a separate hard precision allocation problem after that repair.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent lifecycle repair attempts across construction and reload paths); grader noise UNMEASURED (planned: repeated fixed-artifact continuation and long-context loss evaluation); score ladder UNMEASURED (planned: rounded buffer, buffer-only fix, canonical regeneration, chunked precise phase and attainable context control).

## Screen record
id: C065
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.90
attack_single_range: 0.77-0.97
bo4_est: 0.95
pass4_est: 0.99
ub95_est: 0.99
gpuh_old: 10
gpuh_new_est: 384
duplicate_of: 04B MODERATE; 05B MODERATE
kill_reason: precise compact inputs and regeneration remove the supposed precision tradeoff
souping_flag: no
