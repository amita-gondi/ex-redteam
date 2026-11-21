# C030 — Serve hybrid recurrent states after canceled generations — saturation screen
## 1. What the grader actually rewards
The useful outcome is service throughput after cancellation while every later output matches isolated eager execution and state-copy limits remain satisfied. A fast canceled request earns nothing if its abandoned recurrence corrupts the reused slot. ESTIMATED R≈0 is the corrected safe-serving floor, ESTIMATED R≈1 an attainable exact implementation under the same memory cap; the unmodified leaky server may be invalid, and the intended reference is provisionally ESTIMATED R=0.60.
## 2. Strongest lawful combined attack
Separate committed recurrent checkpoints from uncommitted input buffers, tag slots by generation, and commit only the state corresponding to verified tokens. [ReplaySSM](https://arxiv.org/abs/2610.13778) explicitly describes checkpoint-plus-input buffering and pointer-based speculative rollback; [vLLM's Mamba utilities](https://docs.vllm.ai/en/latest/api/vllm/v1/worker/mamba_utils/) expose hybrid-state lifecycle support. These are unusually close recipes for the stated bottleneck. Use buffered replay where the recurrence admits it and bounded double-buffering or copy-on-write for other layers.

Combine that representation with cancellation fences, stream-event ordering, generation-tagged ownership and delayed slot recycling. Sweep checkpoint interval and speculation length against the full memory ledger, then batch active requests without letting a canceled writer publish into a new owner. If replay arithmetic changes numerical order, retain eager-order reconstruction for the relevant layers; an algebraically equivalent recurrence need not satisfy an exact output contract automatically.

ESTIMATED single-run R=0.82, range ESTIMATED 0.58–0.94; ESTIMATED best-of-4=0.89; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED upper-95% projection=0.98. The high estimate reflects a public representation that avoids cloning full recurrent state at every speculative step, coupled with conventional ownership correctness. Remaining costs include noninvertible or unsupported updates, replay during long rollback and barriers at dense cancellation bursts. Those costs may leave very little deployable improvement for the author either, which makes a measured physical ceiling indispensable.
## 3. Other routes
Bounded committed/speculative double-buffering is the strongest isolated method: ESTIMATED R=0.66, range ESTIMATED 0.41–0.84. It can fit a modest copy cap while retaining batching, but heavy recurrent state may force smaller batches.

An exhaustive development sweep over checkpoint spacing, replay windows, batch size and cancellation fencing reaches ESTIMATED R=0.74, range ESTIMATED 0.49–0.91. This search needs no new scientific insight once safe state ownership is established. Serving cancellation-prone requests without speculation is also legal, ESTIMATED R=0.42, range ESTIMATED 0.20–0.64; its score depends on whether canceled work meaningfully dominates the native denominator.
## 4. What would lower lawful saturation
Specify a mixed recurrent workload where checkpoint buffering and conventional double-buffering demonstrably encounter different binding constraints, with an attainable exact control outperforming both. Private transition graphs must change useful representation decisions while preserving disclosed recurrence semantics. ESTIMATED attack R might fall to 0.53–0.66, with ESTIMATED three engineer-weeks and ESTIMATED 48 H100 GPU-h for realistic lifecycle traces. Simply tightening copies until no method can batch destroys attainable reserve; it does not strengthen the research task. This redesign remains unlikely to clear the repeated-search gates without a concrete additional mechanism.
## 5. Decisive-check GPU-h re-estimate
Old card figure: ESTIMATED 7 GPU-h. Revised ESTIMATED 18 H100 GPU-h assumes an ESTIMATED 7B hybrid subject, ESTIMATED five arms, ESTIMATED three cancellation traces per arm, and ESTIMATED 0.6 H100-hour per trace: ESTIMATED 5×3×0.6=9. Add ESTIMATED 4 GPU-h for isolated eager truth, ESTIMATED 3 GPU-h for cold slot-reuse replays and ESTIMATED 2 GPU-h for matched warmup. No learned component is trained. The smaller figure can expose one corruption bug but underprices the public buffered-state replacement and copy-cap frontier.
## 6. Duplicate check
05A: MODERATE, because its read serving contract already requires exact session-state management but does not isolate canceled recurrent writes. 06A: WEAK, since its source changes compressed attention representation with recovery learning rather than exact recurrent transactions. The new trigger is sufficiently specific to avoid declaring a duplicate solely from shared cache terminology.
## 7. Verdict
CUT. ESTIMATED best-of-four exceeds its line by 0.29; ESTIMATED single-run excess is 0.12. The verified checkpoint-and-replay recipe directly weakens the card's claim that full recurrent copying is the only conventional safe option.
## 8. Measurement status
Rollouts UNMEASURED (planned: repeated cancellation and later slot ownership changes). Grader noise UNMEASURED (planned: identical traces under warmed and fresh workers). Score ladder UNMEASURED (planned: invalid starter, safe snapshots, bounded buffers, buffered-replay runtime).
## Screen record
id: C030
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.82
attack_single_range: 0.58-0.94
bo4_est: 0.89
pass4_est: 0.98
ub95_est: 0.98
gpuh_old: 7
gpuh_new_est: 18
duplicate_of: 05A MODERATE; 06A WEAK
kill_reason: buffered recurrent replay already targets rollback bottleneck
souping_flag: no
