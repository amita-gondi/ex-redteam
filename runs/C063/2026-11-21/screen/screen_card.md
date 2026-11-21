# C063 — Make MTP gradients correct and cheap across sequence shards — saturation screen
## 1. What the grader actually rewards
The sharded implementation must propagate the intended shifted embedding gradients and improve held-out learning per complete training time. A forward-correct gather with detached backward ancestry earns no valid acceleration, and suppressing the auxiliary objective changes the task. R≈0 is the repaired differentiable-gather floor and R≈1 the attainable exact training control; all score, model and compute quantities in this review are ESTIMATED pending measured native anchors.

Boundary-aware MTP communication is provisionally the ESTIMATED R=0.60 reference, pending measured learning-time separation from the corrected gather stack.

## 2. Strongest lawful combined attack
Implement an explicit autograd communication operator whose forward exchanges only embedding positions needed by the shifted prediction depths and whose backward accumulates the exact adjoint contributions to their owning shards. Batch overlapping horizon halos, reduce duplicate transfers, and overlap boundary exchange with interior computation. [Megatron Core's MTP documentation](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/multi_token_prediction.html) describes the depth-dependent causal chain; its [implementation API](https://docs.nvidia.com/megatron-core/developer-guide/nightly/apidocs/core/core.transformer.multi_token_prediction.html) exposes packed sequence boundaries and context-parallel layouts. These make dependency accounting a concrete engineering problem rather than hidden scientific semantics.

Compare a corrected full gather, boundary exchange, and selective recomputation of remote embeddings. Derive the backward from the forward index map, then check scalar losses, embedding gradients and actual subsequent updates against the unsharded reference. Tune exchange granularity and overlap only after parity holds. Packed-document masks and horizons crossing multiple shards require care, but their dependency sets can be computed exactly from public batch structure.

ESTIMATED single-run R=0.76, range 0.55–0.89; ESTIMATED best-of-4=0.85; ESTIMATED pass@4 at R≥0.60=0.95; ESTIMATED upper-95% projection=0.95. These are conditional desk forecasts above fixed competent controls. The residual is communication latency and work whose dependencies cover most of the sequence, where halos provide little advantage. That physical limit lowers every implementation's speed and must not be normalized into artificial headroom. Variable horizons add bookkeeping; they do not by themselves force new learning insights.

## 3. Other routes
A differentiable full gather with communication overlap is the strongest single standard recipe: ESTIMATED R=0.61, range 0.39–0.80. It may already be fast enough if embedding exchange is a small fraction of the total MTP step.

A topology-aware sweep over full gather, indexed halos, recomputation and overlap chunking has ESTIMATED R=0.72, range 0.50–0.87. Selection uses matched development partitions and real gradient checks. Exhaustively deriving required indices is lawful algorithmic synthesis, even if it avoids the designer's preferred diagnosis sequence.

## 4. What would lower lawful saturation
First establish a real native loss/time gap after the complete communication stack. A possible redesign couples horizon allocation with a fixed auxiliary compute budget and held-out data regimes, so deciding which future targets to train matters in addition to moving their tensors. That changes the scientific intervention and must state the new objective openly. ESTIMATED attack on that revised task is 0.48–0.64. ESTIMATED cost is 10–14 person-days and ESTIMATED 336 H100-h for an initial learning-scale check. Adding more partition layouts to the unchanged exact-index problem is unlikely to reduce lawful saturation substantially.

## 5. Decisive-check GPU-h re-estimate
Original estimate: ESTIMATED 12 GPU-h. Revised ESTIMATED 336 H100-GPU-h assumes an ESTIMATED 1B decoder trained for ESTIMATED 2B tokens per run, ESTIMATED 4 communication arms×3 seeds×6 cluster-hours×4 H100s=288. Gradient/reference probes, held-out evaluation and communication profiling add ESTIMATED 48, totaling ESTIMATED 336. An ESTIMATED six-operations-per-parameter-token approximation gives ESTIMATED 12×10^18 training operations per run; the assumed cluster time therefore requires a plausible but unprofiled sustained training rate. The old amount can expose missing gradients on a fixture, not validate a quality-per-time gain over billions of tokens.

## 6. Duplicate check
05B: MODERATE after inspecting its exact-training source. Both submit execution changes and grade preserved updates plus useful training speed, but the older task's distributed graph/resume contract does not specify cross-shard shifted-objective communication. 04A: WEAK from its asynchronous-learning source because gradient fidelity is common, while policy-version/routing interactions differ from MTP halos. There is no STRONG duplicate finding.

## 7. Verdict
CUT. ESTIMATED best-of-4 exceeds its binding line by 0.25 and the ESTIMATED single-run forecast exceeds 0.70 by 0.06. The strongest route is the exact adjoint of a public index mapping plus conventional overlap, and the card does not demonstrate a residual beyond that stack.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent full-budget sharded MTP optimization attempts); grader noise UNMEASURED (planned: repeated complete training/evaluation for fixed implementations); score ladder UNMEASURED (planned: detached negative control, repaired gather, overlap, exact halos, recomputation and attainable training control).

## Screen record
id: C063
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.76
attack_single_range: 0.55-0.89
bo4_est: 0.85
pass4_est: 0.95
ub95_est: 0.95
gpuh_old: 12
gpuh_new_est: 336
duplicate_of: 05B MODERATE; 04A WEAK
kill_reason: exact halo adjoint plus overlap likely captures communication reserve
souping_flag: no
