# C011 — Precision rescue for discrete routing boundaries — saturation screen
## 1. What the grader actually rewards
Routing kernels must preserve useful learning through a load transition while respecting the transferred-byte budget; reference route agreement is a correctness diagnostic rather than the reward itself. ESTIMATED R≈0 is the complete competent selective-precision floor and ESTIMATED R≈1 an attainable stronger loss/communication operating point. The inherited narrow router would provisionally receive ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60, but neither held-out loss nor physical bandwidth reserve has been measured.
## 2. Strongest lawful combined attack
Keep expert activations and communication buffers narrow, cast only local routing arithmetic to a wider format, and perform stable top-k selection with a deterministic tie convention. [Switch Transformers](https://www.jmlr.org/papers/volume23/21-0998/21-0998.pdf) explicitly verifies this selective-precision pattern while recasting communication tensors to a narrow format. This is almost exactly the escape route the card needs to survive, not merely a loosely related numerical trick.

Add an error-bound screen around the top-k boundary: compute inexpensive narrow scores, recompute uncertain candidates with wider reductions, and fall back to a fully widened local router when too many scores are close. Search the threshold and fused layout jointly on boundary-heavy dev batches, then compare full learning trajectories with identical offered examples. [ST-MoE](https://arxiv.org/abs/2202.08906) verifies router-stability interventions, but its z-loss is only an additional lawful control if the kernel-edit contract allows changing training mathematics; the principal attack does not rely on that permission. Independent checks must validate assignments from the exact kernels used during credited updates.

ESTIMATED single-run R=0.86, range 0.69–0.96; ESTIMATED oracle best-of-4=0.91; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% envelope=0.99. These are estimates of a vulnerable design, not measured speedups. Local routing is usually much smaller than expert communication, making selective widening a credible way to preserve most bandwidth benefit while recovering assignment fidelity. Residual cost comes from dense boundary batches that trigger fallback and from genuinely coupled routing/load effects. However, a kernel-only edit cannot invent an unrestricted load policy, and the current grader does not instantiate a byte constraint under which widened local routing is inadequate.
## 3. Other routes
- Widen the entire router but no expert tensors. ESTIMATED R=0.78, range 0.56–0.93. This direct published pattern may be sufficient without any adaptive recomputation.
- Autotune router tile layout, accumulation format, candidate shortlist and near-tie threshold, rejecting any configuration whose actual timed assignments fail conformance. ESTIMATED R=0.82, range 0.62–0.95. This search targets the narrow remaining implementation frontier efficiently.
- Use deterministic full-width top-k on narrow transported scores. ESTIMATED R=0.57, range 0.32–0.79. It cannot recover precision already lost before selection, so its result would localize which rounding stage matters.
## 4. What would lower lawful saturation
First put selective local widening into the floor. Then construct a real operating regime where locally widening the complete routing score tensor consumes material allowed memory traffic and near-tie fallback interacts with expert congestion. Publish the supported byte accounting and allow a kernel-level solution without silently requiring an uneditable scheduler change. Forecast after a successful redesign is ESTIMATED R=0.50, range 0.28–0.73. Cost is ESTIMATED a month of profiled multi-expert workload construction plus ESTIMATED 384 extra H100 GPU-h for byte-frontier and load-transition studies. Tightening an arbitrary router-byte cap without a credible serving/training analogue would manufacture difficulty.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 12 GPU-h. Revised ESTIMATED 320 H100 GPU-h uses an ESTIMATED 8B-total/1B-active MoE subject, ESTIMATED 4 kernel arms, ESTIMATED 3 seeds and ESTIMATED 6 elapsed hours per trajectory on ESTIMATED 4 H100s. Training is ESTIMATED 4×3×6×4=288 GPU-h; boundary microbenchmarks and byte/conformance checks add ESTIMATED 8 GPU-h, and loss evaluation adds ESTIMATED 24 GPU-h: ESTIMATED total 320. The architecture is a planning assumption, not a verified asset. The old budget is defensible for a routing microbenchmark but omits learning through the transition that defines this card's outcome.
## 6. Duplicate check
v3 04B (`task_design_v3_codex/04_training_fidelity.md`, source opened): MODERATE, since both co-design precision and recovery but its target is drifting activation distributions rather than discrete routing fidelity. v3 04A in the same source: MODERATE, sharing MoE routing and useful learning while emphasizing asynchronous policy/version/cache state. No STRONG claim is needed; the published selective-router baseline independently threatens saturation.
## 7. Verdict
CUT. The ESTIMATED single-run breach is 0.16 and best-of-four breach ESTIMATED 0.31. An established selective-precision implementation directly addresses the claimed bandwidth-versus-routing dilemma before more elaborate research is necessary.
## 8. Measurement status
Rollouts UNMEASURED (planned: exact kernel edits with full transition training). Grader noise UNMEASURED (planned: replicated loss trajectories and repeated transferred-byte timing). Score ladder UNMEASURED (planned: narrow router, local widening, adaptive recomputation and independently feasible stronger control).
## Screen record
id: C011
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.86
attack_single_range: 0.69-0.96
bo4_est: 0.91
pass4_est: 0.99
ub95_est: 0.99
gpuh_old: 12
gpuh_new_est: 320
duplicate_of: v3-04B MODERATE; v3-04A MODERATE
kill_reason: published selective router precision preserves narrow communication
souping_flag: no
