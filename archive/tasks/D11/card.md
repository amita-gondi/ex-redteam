# D11 — Learn when a streaming visual assistant should respond or wait

**Generator:** recovered temporal-policy sketch. **Stage × artifact:** training × model weights. **Modality:** visual event streams.

## Problem

A visual assistant reacts correctly to isolated frames but responds too early, repeats a completed response or misses an overlapping event. Train a streaming wait/respond policy from inherited session traces. [Suite 7.8](/workspace/task_suites_claude.md:8512) makes the complete event-time session the unit of success, including restraint after a valid response.

## Why known recipes plateau

Finite-state event tracking, temporal detectors, explicit response suppression and demonstration-trained waiting are complete recipes. A hypothesized plateau requires partial observations where waiting changes what can be identified before the opportunity closes. It is unproved that this exceeds ordinary event detection plus a state machine.

## Deterministic grader

Use a trusted event clock, exact event identities and published response windows. Credit each scheduled opportunity only when the correct response occurs in its legal interval; duplicate or premature responses incur their disclosed local cost. U averages opportunity utility across complete sessions, with quiet intervals and overlapping-event strata retained. Hidden state establishes truth but never enters the policy. Apply F_D11.

## Hidden-score design

Independently authored visual event compositions alter causal ordering rather than just appearance. Strict dev fidelity covers visibility, event density, window widths and response costs. A protected composition proxy checks that dev ranking predicts private timing performance; clean/failed sessions share rendering and packaging conventions.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D11(U_detector+FSM).** If event identities become observable before their response deadlines, a trained detector with a deterministic pending/responded state machine may attain reference utility. Always-wait and immediate-response baselines expose denominator tricks. Policy-controlled timestamp claims must not override the trusted event clock.

## Saturation note vs 10T / 12h

A strong solver can synthesize the event machine and generate timing demonstrations. Real reserve would require learned evidence accumulation and response control to interact beyond that composite. Larger streams alone do not help; index S2/S4/S7 remain hard gates with no measured pass.

## Cheapest decisive check

**ESTIMATED: 12 GPU-h** for detector training, policy continuations and full-session replay. Compare the complete detector/state-machine recipe against end-to-end waiting on observation-matched ambiguous events; stop if only threshold tuning remains.

## GDM Round 2 compliance and shape

Compared with inference_optimization, this optimizes a learned temporal decision rather than throughput. R1 demands real completion rather than proxy return. R2's meaningful-efficiency lesson requires calibrated response windows and actual latency fidelity, without rewarding an inactive timing term.

## DISTINCTNESS NOTE

**Wrong parent: v3 02B. Nearest other: [T10](/workspace/task_catalog_v3_full/packets/T10.md).** Delayed workflow credit lacks visual wait/respond windows; T10 chooses observations for answers, while D11 controls proactive session responses and post-response restraint.

## Verdict

**conditional** — Keep only if partial visual evidence creates a learned timing problem that detector-plus-state-machine control cannot resolve.
