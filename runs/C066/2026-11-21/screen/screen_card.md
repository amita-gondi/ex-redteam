# C066 — Adam initialization that preserves the real update clock — saturation screen
## 1. What the grader actually rewards
Before useful-learning speed matters, state construction, dormant-group activation and reload must match a trusted optimizer's weights and update counters. A dummy update that applies decay or bias correction is therefore a semantic failure, even if the initial loss looks healthy. R≈0 is the competent explicit-state implementation and repaired no-op floor; R≈1 is the attainable faster state-management control, with every score and cost forecast below ESTIMATED and the underlying runtime/quality ladder UNMEASURED.

Lazy materialization has an ESTIMATED R=0.60 reference target, although useful runtime separation from correct eager allocation remains to be established.

## 2. Strongest lawful combined attack
Allocate moment tensors and counters directly, without invoking a parameter update. Define clock behavior for absent gradients, zero gradients and newly activated parameters explicitly, then maintain stable parameter identities through serialization. [Adam's original algorithm](https://arxiv.org/abs/1412.6980) makes the bias-correction clock part of the update; [PyTorch's Adam documentation](https://docs.pytorch.org/docs/stable/generated/torch.optim.Adam) documents parameter-group loading behavior and the distinction between absent and zero gradients. These are conventional semantics, not a novel optimization mechanism.

Use eager state creation for small groups and lazy chunked allocation for groups whose future activation is known through the legal schedule. Preserve master weights, moments and per-parameter counters as a transaction, with exact initialization and load comparisons before the first true backward. Group allocation by device and dtype, prefetch only announced imminent groups, and fall back to eager creation when uncertainty has no expected memory benefit. Tune chunking and preallocation against total learning time, including initialization and reload.

ESTIMATED single-run R=0.94, range 0.84–0.99; ESTIMATED best-of-4=0.97; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% bound=1.00. These subjective estimates reflect how completely the stated failure is covered by ordinary state construction, and are not measurements. The tiny residual is allocator synchronization and dormant-state memory. If eager initialization fits the cap, lazy state engineering may have no scientific utility at all. Conversely, incorporating this entire conventional stack into the floor does not create new headroom; it may collapse the task's attainable range.

## 3. Other routes
Correct eager allocation with group-local counters is the strongest single standard recipe, ESTIMATED R=0.88, range 0.72–0.98. It is particularly likely to win when initialization is a small part of a long training campaign.

A sweep over eager/lazy allocation thresholds, moment initialization batch size and documented optimizer backends yields ESTIMATED R=0.92, range 0.80–0.99. Compare actual state transitions before timing, and keep optimizer-step counts fixed. Replacing the entire optimizer wrapper with a mature semantically equivalent implementation is lawful and must be included; the grader cannot insist on retaining the buggy constructor.

## 4. What would lower lawful saturation
Only a genuine memory-latency frontier could justify a revised task: delayed groups must be large enough that correct eager allocation violates a disclosed useful envelope, while future activation can be predicted from legal information. Hold out activation dependencies and retain an executable exact-state control. ESTIMATED combined R after that change is 0.64–0.82, still unsafe. ESTIMATED effort is 5–9 person-days and ESTIMATED 128 H100-h for an allocation/learning pilot. Adding additional resume paths to an otherwise small state machine is unlikely to create dependent scientific insights.

## 5. Decisive-check GPU-h re-estimate
Old amount: ESTIMATED 8 GPU-h. New ESTIMATED 128 H100-GPU-h assumes an ESTIMATED 1B decoder, ESTIMATED 4 allocation arms×3 seeds×8 device-hours of training, activation and resume =96, plus ESTIMATED 24 for cold replay and held-out learning evaluation and ESTIMATED 8 for initialization/master-weight checks. Total ESTIMATED 96+24+8=128 on H100. The state-machine parity check itself is much cheaper and should precede this envelope. The old estimate is plausible for falsifying a bad constructor, but too low for establishing a meaningful learning-time benefit under a restrictive state budget.

## 6. Duplicate check
05B: MODERATE from the inspected distributed-training source; exact optimizer/RNG state and cold resumability are already mandatory there, but this narrower intervention is state allocation before genuine updates. T08: WEAK after reading its continual-update packet because moment transport and reset overlap, yet contract adaptation rather than allocator correctness drives its grader. Neither source demonstrates an identical lazy-activation research task.

## 7. Verdict
CUT, binding single-run forecast ESTIMATED 0.24 above its line. ESTIMATED best-of-4 is 0.37 above its threshold, and both remaining tails also breach. The direct conventional repair is stronger than the author's initial estimate suggests, especially when eager state fits within the deployment memory limit.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent optimizer-wrapper implementations with full activation histories); grader noise UNMEASURED (planned: repeated fixed-state training and reload timing); score ladder UNMEASURED (planned: dummy-step negative, direct eager allocation, correct lazy allocation, tuned batching and attainable exact control).

## Screen record
id: C066
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.94
attack_single_range: 0.84-0.99
bo4_est: 0.97
pass4_est: 0.99
ub95_est: 1.00
gpuh_old: 8
gpuh_new_est: 128
duplicate_of: 05B MODERATE; T08 WEAK
kill_reason: direct state allocation and eager fallback nearly construct the solution
souping_flag: no
