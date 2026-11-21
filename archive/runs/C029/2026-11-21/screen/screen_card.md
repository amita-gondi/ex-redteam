# C029 — Exact speculative decoding across tool-boundary rollback — saturation screen
## 1. What the grader actually rewards
Only committed tokens generated under the realized tool-result prefix count, divided by metered target-model work that includes discarded verification and reconstruction. ESTIMATED R≈0 represents the best competent exact-decoding floor, including safe flushing, and ESTIMATED R≈1 the stronger attainable throughput control. The starter's incorrect reuse must receive no benefit; a repaired full-flush runtime plausibly earns ESTIMATED R=0.00, with the proposed reference around ESTIMATED R=0.60 before calibration.
## 2. Strongest lawful combined attack
Compose exact speculative verification with immutable prefix identities and copy-on-write cache branches. [Leviathan et al.](https://proceedings.mlr.press/v202/leviathan23a.html) provides the exact speculative-decoding algorithm; [SGLang](https://arxiv.org/abs/2312.07104) provides a concrete prefix-tree reuse architecture. Index each draft and target state by model version, full token ancestry, position and relevant tool state. A revision truncates to the last common valid prefix, invalidates dependent descendants, and retains unchanged ancestors.

Then tune speculative depth from observed acceptance and pending tool hazard, batch verification for surviving branches, and disable speculation when its work is predictably wasted. A frontier researcher can implement these transaction invariants without discovering a new approximation theorem. For a token-equality grader, use the disclosed deterministic decoder and stable random-stream contract; distributional exactness alone does not imply identical sampled trajectories. Numerical differences must be checked on the timed path.

ESTIMATED single-run R=0.79, range ESTIMATED 0.57–0.92; ESTIMATED best-of-4=0.86; ESTIMATED pass@4 at R≥0.60=0.97; ESTIMATED projected upper-95% bound=0.97. The forecast assumes conventional ancestry invalidation captures most attainable improvement over full flush and that scheduler tuning recovers additional avoided target work. The remaining gap is the actual compute required after changed prefixes: transformer suffix state generally cannot be reused exactly across changed ancestors. That physical restriction limits both attacker and author, so it cannot be counted as exclusive research headroom.
## 3. Other routes
A single radix-tree cache with conservative descendant invalidation reaches ESTIMATED R=0.70, range ESTIMATED 0.47–0.86. It preserves correctness and all straightforward reuse while leaving speculative work allocation untuned.

A discrete sweep of draft length, rollback-risk thresholds and verification batch size gives ESTIMATED R=0.74, range ESTIMATED 0.51–0.90. Every branch's target executions remain charged, including candidates discarded by tuning. Turning speculation off on tool-heavy intervals is a lawful specialization route, ESTIMATED R=0.48, range ESTIMATED 0.24–0.69; if that wins broadly, the task's supposed speculative opportunity was overstated.
## 4. What would lower lawful saturation
Introduce a validated memory-versus-recomputation frontier with asynchronous tool rejoins, eviction pressure and heterogeneous shared branches. Hold semantic correctness fixed and require a feasible control that beats tuned ancestry caching in native useful throughput. ESTIMATED attack reward could drop to R=0.54–0.67, costing ESTIMATED two systems-author weeks and ESTIMATED 32 H100 GPU-h to characterize traces. Even this does not clearly survive repeated selection, and it moves toward the existing exact-serving task. Merely deepening rollback or changing tool text leaves the prefix invariant unchanged.
## 5. Decisive-check GPU-h re-estimate
Old pilot: ESTIMATED 5 GPU-h. New ESTIMATED 12 H100 GPU-h: an ESTIMATED 7B target with ESTIMATED 0.5B draft fits the assumed single H100 runtime; test ESTIMATED four engine arms on ESTIMATED three independently authored tool trees at ESTIMATED 0.5 hour each. That is ESTIMATED 4×3×0.5=6 GPU-h, plus ESTIMATED 3 GPU-h for full target-only token truth and ESTIMATED 3 GPU-h for warmup, cold replay and timing replication. No training is needed. The old value is plausible for one bug demonstration but not a meaningful combined-stack comparison.
## 6. Duplicate check
V3 05A: MODERATE. Its source already grades exact serving across coupled session state and permits whole-engine replacement, but does not specifically make tool-prefix rollback the intervention. V3 05B: WEAK, since its adjacent contract preserves training updates and resume state rather than committed inference tokens. The rollback construct is narrower enough to avoid a STRONG finding.
## 7. Verdict
CUT: ESTIMATED single-run excess 0.09 and best-of-four excess 0.26. Conventional exact ancestry management is too close to the proposed solution, and unreusable changed suffixes constrain the author equally.
## 8. Measurement status
Rollouts UNMEASURED (planned: fresh rollback trees with the full runtime stack). Grader noise UNMEASURED (planned: repeated warmed throughput and token-truth replay). Score ladder UNMEASURED (planned: target-only, flush, ancestry cache, adaptive speculative control).
## Screen record
id: C029
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.79
attack_single_range: 0.57-0.92
bo4_est: 0.86
pass4_est: 0.97
ub95_est: 0.97
gpuh_old: 5
gpuh_new_est: 12
duplicate_of: 05A MODERATE; 05B WEAK
kill_reason: exact prefix caching plus adaptive speculation saturates
souping_flag: no
