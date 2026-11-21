# v2 task re-rank using the red-team verdicts (Nov 20, 2026)

**Everything here is a design judgment plus ESTIMATED compute. No task has been built, run or measured.** Tiers say which tasks are most likely to clear the acceptance bar *after the listed fixes*; "likely-pass" is not a pass.

Inputs: `/workspace/task_design_v2_codex/` (00_overview, 01–08, 99, design_manifest.json, validation_budget.csv), `/workspace/task_design_v2_redteam/` (00_summary.md + 8 primitive reports; attack rows read from the `T` data in `_write_reports.py`, extracted to `_redteam_T_extract.json`), `/workspace/ACCEPTANCE_BAR_GENERAL.md`, `/workspace/task_design_v2_summary.md`.


**Tier rules used.** *likely-pass*: red-team "needs fixes" with no unblocked (block = no) research-depth attack, the red team describes it as among the most defensible/strong candidates, and the fixes are contract/spec work plus one decisive anchor. *at-risk*: red-team "needs fixes" but an unblocked saturation route or an objective that rewards the wrong outcome. *likely-cut*: red-team cut/merge.

Red-team reward notation: F(S) = 0 for S≤b; 0.60(S−b)/(c−b) for b<S≤c; 0.60+0.40(S−c)/(1−c) above c. No numeric b or c exists yet, so every red-team reward is conditional ("R≈0.60 if S≈c"). Quotes below are verbatim.

**Decisive-experiment costing.** One full run (12h solution + grade) = the task's E5 row ÷ 5; one grade = its E1 row ÷ 9 (both checked against the E2/E3 rows: E3 = 6 runs exactly for all 16 tasks). The standard decisive anchor is the red team's strongest combined baseline ×3 seeds vs the executable reference ×3 seeds = 6 runs, i.e. the size of the task's E3 row. All GPU-h are ESTIMATED H100-hours; $ at the design's assumed $3/GPU-h (an estimate, not a quote).

## Ranked table

| Rank | Task | Tier | One-line reason | Strongest red-team attack (est. reward) | Decisive experiment | Est. GPU-h | Est. $ |
|---|---|---|---|---|---|---:|---:|
| 1 | **04A** Recover useful asynchronous MoE learning across version, routing and cache boundaries | **likely-pass** | Red team calls it “one of the more defensible candidates”; no attack is rated unblocked (all yes/partly), and v2 lists it 2nd in build order; the open question is purely whether a tuned healthy synchronous/off-policy stack erases the gap. | SAT-2: versioned recomputation plus standard off-policy correction (blocked: partly) → R≈0.60 if it attains c; R=0 if it is the best default floor | Tuned synchronous fallback + versioned recompute/IMPALA-style correction stack ×3 seeds vs executable reference ×3 seeds, full 12h at 32×H100 | 5,376 | $16,128 |
| 2 | **05B** Accelerate a distributed training graph while preserving updates and resumable state | **likely-pass** | Red team: “clear accepted-profile fit and strong observable invariants”; v2 build-order #3; all threats are contract/verification gaps (bind checks to timed work, cold resume, tolerance bounds) plus one formula fix (per-family floors). | GAME-1: execute correctly only for checks (blocked: partly) → R can approach 1 without valid work if a separate correctness pass certifies unchecked timing blocks (conditional); unblocked GAME-3: S≤0.75, F(0.75) | Stock tuned compatible stack (TorchTitan-class) ×3 vs faster legal reference ×3 under the exact reduction/RNG contract | 2,688 | $8,064 |
| 3 | **05A** Increase exact useful serving capacity across coupled sessions, adapters and model shapes | **likely-pass** | Red team: “remains a strong candidate for a systems task”; cheapest task in the ledger (62,488 GPU-h, 12 GPU-h per grade); its one unblocked issue (demand-limited grading) is a grader-load fix, not a research-depth flaw. | GAME-3: compile/search outside the timed window (blocked: partly) → R=F(S_warm_optimized), ≈0.60–1 if warmup work is unbounded | Complete tuned serving engine + joint topology/cache/scheduler autotuner ×3 vs reference ×3, graded with a load sweep | 1,224 | $3,672 |
| 4 | **01A** Reconstruct a training corpus whose apparent quality rankings reverse across stages | **likely-pass** | Only research (non-systems) task with no unblocked attack; red team keeps it (“retain as a design to fix”), v2 build order includes it, and it absorbs 08B’s downstream-adaptation test. Lowest-confidence of the four: its risk is saturation by outcome-only mixture search. | SAT/GAME-3: universal generator solving (blocked: partly) → R≈0.60–1 only if algorithmic training drives S from c toward 1 (to verify) | DoGE-style stage-conditioned reweighting combined with Hyperband outcome-only schedule search, one combined recipe ×3 seeds vs reference ×3 | 2,400 | $7,200 |
| 5 | **06A** Build a recoverable compressed attention state across long-context workloads | **at-risk** | Highest strategic value (matches GDM’s KV request; v2 build-order #1) but TurboQuant-style data-oblivious quantization is rated UNBLOCKED with R≈0.60–1; a cheap grade-only test decides it. | SAT-2: TurboQuant/data-oblivious rotation recipe (blocked: no) → R≈0.60–1 if it fits the 1/4 cap at target quality (unverified) | Grade-only physical anchor: apply KIVI-2bit, KVQuant-3bit and a TurboQuant-style quantizer (training-free) at the 1/4 envelope, 3 grader seeds each | 2,304 | $6,912 |
| 6 | **02B** Train a research agent to assign credit across delayed and irreversible tool actions | **at-risk** | v2 build-order pick with a real long-horizon credit problem, but two structural gaps: executable memory can host a planner (R≈1) and the convex all-eight term (q) rewards abandoning hard graphs (unblocked). | GAME-1: move the planner into memory-update code (blocked: partly) → a≈q≈1, R≈1 if memory can observe state and emit plans (to verify) | Planner+recovery demonstration SFT (comparable data/compute) ×3 vs reference ×3, after the memory-API spec (CPU) | 2,688 | $8,064 |
| 7 | **07A** Repair an RL measurement ecosystem and prove that optimization learns the intended skill | **at-risk** | Addresses the actual review failures (v2 build-order #4) and has a strong outer executable-truth architecture, but GAME-1 is unblocked: 60% of S is checker credit, so ≥0.20 raw can come with zero learning gain. | GAME-1: win checker terms without improving learning (blocked: no) → S=0.60+0.40a0 with no learning gain; ≥0.20 raw possible, R possibly ≥0.60 | Universal isolation + exact semantic checker baseline ×3 vs reference ×3, after the reward re-weighting (CPU) | 2,688 | $8,064 |
| 8 | **02A** Create transferable learning signal beyond a policy’s success frontier | **at-risk** | Plausible RSI role, but STaR-style rationalization / oracle-planner demonstrations may solve the zero-success barrier directly; the loss-plugin boundary is unspecified; conditional merge with 01B. | SAT-1: rationalize then train without hints (blocked: partly) → R≈0.60; 0.80–1 only with higher S; nothing measured supports near-full | Faithful STaR rationalization → hint-free SFT with iterative correction ×3 vs reference ×3 | 2,400 | $7,200 |
| 9 | **01B** Acquire RL experience that remains useful as the learner changes | **at-risk** | Fresh learner replay and full acquisition charging are sound, but a universal controller (SAT-2) and four-checkpoint gaming (GAME-1) are both UNBLOCKED; merge candidate into 02A. | SAT-2: learn a universal controller on legal proxies (blocked: no) → R≈0.60–0.80; near-full needs S≥c+0.875(1−c) | Combined nonstationary cost-aware bandit + prerequisite replay ×3 vs reference ×3, scored on a dense author-only learning curve as well as the 4 checkpoints | 2,112 | $6,336 |
| 10 | **07B** Train an evidence evaluator that remains useful when researchers optimize against it | **at-risk** | Executable outer labels make it potentially valid, but the renderer can become the checker (R≈1), score flattening defeats the fixed optimizer, and evidence sufficiency is unproven. | GAME-1: renderer becomes the hidden checker (blocked: partly) → d≈z≈v≈1, R≈1 if evidence suffices and renderer can execute semantics | Canonical renderer + hard-negative SFT ×3 vs reference ×3 (an oracle-evidence control reuses the reference runs’ grades) | 2,400 | $7,200 |
| 11 | **03B** Learn a reasoning policy that allocates variable inference budgets without losing coverage | **at-risk** | Objective mismatch: the score rewards capped correctness, so always spending the full cap is rational and can win (GAME-1 and GAME-3 unblocked); must be re-specified before any GPU evidence means anything. | GAME-1: always spend the full request cap (blocked: no) → R≈0.60–1 without efficient stopping if correctness matches reference | After the objective rewrite (CPU), shortest-correct SFT + on-policy distillation ×3 vs reference ×3 on the revised frontier | 2,400 | $7,200 |
| 12 | **04B** Co-design precision and correction for a learner whose activation distribution drifts | **at-risk** | Closest to cut among the at-risk set: red team shows analytically that equal-quality speedup gives ΔS ≤ 0.20(1−e0) < 0.20, so the physical-headroom gate is unreachable unless real learning gains exist; current FP8 scaling may already remove drift. Merge candidate into 04A. | SAT-2: tolerance-driven auto mixed precision (blocked: partly) → R≈0.60–0.80 (SAT-2); and pure-speed ΔS ≤ 0.20(1−e0) < 0.20 (GAME-1, analytic) | Current scaling + selective high-precision fallback + tolerance-driven auto-mixed-precision ×3 vs reference ×3, scored on the accuracy term a | 5,376 | $16,128 |
| 13 | **08A** Design proxy experiments that transfer a continued-pretraining policy across scale and horizon | **likely-cut** | Red-team CUT; v2 itself calls it the highest-risk metric. exp(−loss) compresses the core science (a 3.0→2.8 loss gain is worth ≈0.0055 raw) and the controller can run its own search inside the 25h grader replay. Largest ledger line (477,280 GPU-h). | GAME-2: perform research inside the 25h grader replay (blocked: partly) → R≈0.60–1 if per-grade online search finds a near-optimal policy; loss term worth ≈0.0055 raw | Already decided analytically (0 GPU-h): the red-team exp(−loss) calculation. Re-entry experiment (unfunded): target-only feedback controller ×3 vs reference ×3. | 0 | $0 |
| 14 | **08B** Co-design midtraining for the downstream learning it enables | **likely-cut** | Red-team CUT/merge into 01A: final capability cannot distinguish a better starting model from a more trainable one (GAME-1 unblocked, +0.15 raw from pre-capability alone), and its stage space overlaps 01A. | SAT-2: legal algorithmic pre-adaptation (blocked: partly) → R≈0.60–1 if broad legal preparation transfers; GAME-1: +0.15 raw from starting competence alone | Merge decision needs no GPU (0 GPU-h). Re-entry experiment (unfunded): matched starting-capability control vs reference ×3 each. | 0 | $0 |
| 16 | **06B** Train one elastic model whose representations survive several deployment envelopes | **likely-cut** | Red-team CUT: MatFormer/DynaBERT-style nested training is the task’s core recipe, the shared parameterization can hide partitioned independent submodels, and the shared frontier is unknown. | GAME-1: one shared container, effectively separate submodels (blocked: partly) → R≈0.60–1 if the cap permits partitioned capacity | Unfunded re-entry experiment: named MatFormer-style nested baseline ×3 vs reference ×3 + disjoint-capacity control. | 0 | $0 |


Sum of decisive experiments, funded: likely-pass anchors (inside Stage 1a, = their E3 rows) 11,688 GPU-h; at-risk slice 22,368 GPU-h; likely-cut 0 (analytic/merge decisions; re-entry anchors unfunded).

## Per-task line items

### 1. 04A — Recover useful asynchronous MoE learning across version, routing and cache boundaries  ·  **likely-pass**

- **Red-team verdict:** needs fixes. “A healthy synchronous/off-policy stack may erase the chain; sampled probes leave counterfeiting risk.”
- **Reason:** Red team calls it “one of the more defensible candidates”; no attack is rated unblocked (all yes/partly), and v2 lists it 2nd in build order; the open question is purely whether a tuned healthy synchronous/off-policy stack erases the gap.
- **Strongest attack:** **SAT-2: versioned recomputation plus standard off-policy correction** (blocked: partly). Red-team estimate: “Estimate R≈0.60 if this composed standard recipe attains c; R=0 if it is genuinely the best default floor. Fresh seeds do not make this general protocol obsolete.”
- **Fixes required to reach likely-pass:**
  - Run the complete correctness-first synchronous fallback and versioned-recompute + standard off-policy stack at equal total cost (incl. cache rebuilds) and keep the task only with a raw ≥0.20 advantage (A5).
  - Define a valid update by exact tokens/batch weighting/optimizer transition (blocks GAME-2 micro-update inflation).
  - Secret post-execution probe selection on real training updates (GAME-1).
  - Fix the quality/rate weights or show quality gains: at fixed a, max gain is 0.25(1−e0) (<0.20 if e0>0.20, GAME-3).
  - Record upstream-diff provenance; whole-stack replacement baseline (SAT/GAME-4).
- **Cheapest decisive experiment:** Tuned synchronous fallback + versioned recompute/IMPALA-style correction stack ×3 seeds vs executable reference ×3 seeds, full 12h at 32×H100. Kill if reference − baseline < 0.20 raw (A5) or lower CI ≤ 0.
  - ESTIMATED 5,376 H100 GPU-h ($16,128 at $3/h). Derivation: 6 full runs × 896 GPU-h/run (= 04A E5 4,480 ÷ 5); same size as the 04A E3 row (5,376).
- **Full v2 ledger for this task (for comparison):** 346,528 GPU-h.

### 2. 05B — Accelerate a distributed training graph while preserving updates and resumable state  ·  **likely-pass**

- **Red-team verdict:** needs fixes. “Timed/check-path separation, tolerance accumulation and exactness restrictions require a concrete contract.”
- **Reason:** Red team: “clear accepted-profile fit and strong observable invariants”; v2 build-order #3; all threats are contract/verification gaps (bind checks to timed work, cold resume, tolerance bounds) plus one formula fix (per-family floors).
- **Strongest attack:** **GAME-1: execute correctly only for checks** (blocked: partly). Red-team estimate: “Estimate R=0 if every credited timed transition is validated from trusted captured state. If a separate correctness pass certifies unchecked timing blocks, e_f can approach 1 and R can approach 1 without valid work; this is a conditional implementation threat.” Unblocked formula route: **GAME-3: only optimize three families** (blocked: no). Red-team estimate: “Estimate S≤0.75 if the three e_f reach 1 and the fourth is 0; reward is F(0.75), potentially high depending on b,c. This is an objective-aligned specialization under the written score, not a sandbox breach.”
- **Fixes required to reach likely-pass:**
  - Bind state comparisons to exact timed transitions with server-issued batch IDs and secret post-hoc sampling (GAME-1).
  - Publish per-tensor tolerances and sequence-level bounds; compare long trajectories and post-resume state (GAME-2).
  - Add disclosed per-family service floors or a smooth balanced utility (GAME-3, unblocked).
  - Cold-process resume in a new sandbox from the frozen checkpoint (GAME-4).
  - Demonstrate a faster legal reference + stronger control so exactness does not freeze the space (SAT-2).
- **Cheapest decisive experiment:** Stock tuned compatible stack (TorchTitan-class) ×3 vs faster legal reference ×3 under the exact reduction/RNG contract. Kill if reserve < 0.20 raw or the legal speed frontier is flat (SAT-2).
  - ESTIMATED 2,688 H100 GPU-h ($8,064 at $3/h). Derivation: 6 full runs × 448 GPU-h/run (= 05B E5 2,240 ÷ 5); same size as the 05B E3 row (2,688).
- **Full v2 ledger for this task (for comparison):** 143,136 GPU-h.

### 3. 05A — Increase exact useful serving capacity across coupled sessions, adapters and model shapes  ·  **likely-pass**

- **Red-team verdict:** needs fixes. “Selective service and check/timing splits threaten goodput; exactness and demand may cap headroom.”
- **Reason:** Red team: “remains a strong candidate for a systems task”; cheapest task in the ledger (62,488 GPU-h, 12 GPU-h per grade); its one unblocked issue (demand-limited grading) is a grader-load fix, not a research-depth flaw.
- **Strongest attack:** **GAME-3: compile/search outside the timed window** (blocked: partly). Red-team estimate: “Estimate R=F(S_warm_optimized); it may reach ≈0.60–1 if warmup has unbounded candidate work. If only bounded declared compilation is allowed, excess work should yield R=0. The packet does not give a complete warmup cap.” Unblocked: **SAT/GAME-5: exploit demand-limited grading** (blocked: no). Red-team estimate: “Estimate maximum e_f≤offered_reference_work_rate/B_f even for zero processing time. If the starter already achieves those caps, ΔS≈0 for every true speedup and the task is saturated/flat before normalization.”
- **Fixes required to reach likely-pass:**
  - Replace fixed offered load with a disclosed load search spanning saturation (SAT/GAME-5, unblocked).
  - Per-stratum completion/admission obligations so request shedding does not pay (GAME-1).
  - Bounded, charged compile/warmup budget (GAME-3).
  - Same execution path and external check on every timed request; pin the exactness equivalence class (GAME-2).
  - Isolated verification address space/immutable inputs (GAME-4); whole-engine + joint autotuner baseline (SAT-1).
- **Cheapest decisive experiment:** Complete tuned serving engine + joint topology/cache/scheduler autotuner ×3 vs reference ×3, graded with a load sweep. Kill if raw reserve < 0.20 or score is flat in speed (demand cap).
  - ESTIMATED 1,224 H100 GPU-h ($3,672 at $3/h). Derivation: 6 full runs × 204 GPU-h/run (= 05A E5 1,020 ÷ 5); same size as the 05A E3 row (1,224).
- **Full v2 ledger for this task (for comparison):** 62,488 GPU-h.

### 4. 01A — Reconstruct a training corpus whose apparent quality rankings reverse across stages  ·  **likely-pass**

- **Red-team verdict:** needs fixes. “Stage-dependent mixture search may bypass the diagnosis chain; learner/variant floors are incomplete.”
- **Reason:** Only research (non-systems) task with no unblocked attack; red team keeps it (“retain as a design to fix”), v2 build order includes it, and it absorbs 08B’s downstream-adaptation test. Lowest-confidence of the four: its risk is saturation by outcome-only mixture search.
- **Strongest attack:** **SAT/GAME-3: universal generator solving** (blocked: partly). Red-team estimate: “Estimate R≈0.60–1 only if algorithmic training drives S from c toward 1; actual coverage and student learnability are to verify. Merely recognizing a family yields no guaranteed reward.” Most likely route: **SAT-1: transfer-aware reweighting recipe** (blocked: partly). Red-team estimate: “Estimate S≈c and R≈0.60 if the recipe matches the reference; R≥0.80 only if S≥(1+c)/2. Near-full reward is unverified. If this precise recipe is genuinely included in b, estimate R=0 instead.”
- **Fixes required to reach likely-pass:**
  - Add DoGE-style stage-conditioned reweighting and outcome-only low-dimensional schedule search (Hyperband) as full-budget defaults in b (SAT-1/SAT-2).
  - Independently authored held-out algorithms/content, not just seeds; solver-generated legal-corpus baseline (SAT/GAME-3).
  - Specify learner weights and per-learner×domain floors with smooth penalties (GAME-1).
  - Identical normalization of anchors and candidates (GAME-4); charge actual post-normalization tokens (GAME-2).
  - Fold in 08B’s downstream-adaptation evaluation as a transfer slice.
- **Cheapest decisive experiment:** DoGE-style stage-conditioned reweighting combined with Hyperband outcome-only schedule search, one combined recipe ×3 seeds vs reference ×3. Kill if the combined baseline is within 0.20 raw of the reference on any target learner.
  - ESTIMATED 2,400 H100 GPU-h ($7,200 at $3/h). Derivation: 6 full runs × 400 GPU-h/run (= 01A E5 2,000 ÷ 5); same size as the 01A E3 row (2,400).
- **Full v2 ledger for this task (for comparison):** 151,472 GPU-h.

### 5. 06A — Build a recoverable compressed attention state across long-context workloads  ·  **at-risk**

- **Red-team verdict:** needs fixes. “The quarter-size KV envelope has strong known quantization attacks; the fixed schema limits novel research.”
- **Reason:** Highest strategic value (matches GDM’s KV request; v2 build-order #1) but TurboQuant-style data-oblivious quantization is rated UNBLOCKED with R≈0.60–1; a cheap grade-only test decides it.
- **Strongest attack:** **SAT-2: TurboQuant/data-oblivious rotation recipe** (blocked: no). Red-team estimate: “Estimate R≈0.60–1 if this data-oblivious method fits the 1/4 state cap and preserves the target quality/rate; unverified for Qwen3, full accountant and kernels. The literature result is not a v2 reward measurement.”
- **Fixes required to reach likely-pass:**
  - Faithful 2/3-bit KIVI/KVQuant and TurboQuant-style controls with full accounting (SAT-1/SAT-2).
  - Resolve persistent-vs-transient memory accounting; continuous cgroup/device high-water marks (GAME-2).
  - Decide legality of recomputation and baseline chunked recompute (GAME-1).
  - Private long-document tasks with distributed dependencies (GAME-3).
  - If known quantizers are near-lossless at 1/4, change the envelope (with evidence) or cut.
- **Cheapest decisive experiment:** Grade-only physical anchor: apply KIVI-2bit, KVQuant-3bit and a TurboQuant-style quantizer (training-free) at the 1/4 envelope, 3 grader seeds each. Kill/re-envelope if any is within 0.20 raw of the attainable quality/rate ceiling.
  - ESTIMATED 2,304 H100 GPU-h ($6,912 at $3/h). Derivation: 9 complete grades × 256 GPU-h/grade (= 06A E1 2,304 ÷ 9); no solver phase needed for training-free quantizers.
- **Full v2 ledger for this task (for comparison):** 173,264 GPU-h.

### 6. 02B — Train a research agent to assign credit across delayed and irreversible tool actions  ·  **at-risk**

- **Red-team verdict:** needs fixes. “Planner demonstrations, executable memory and convex all-eight reliability can bypass credit research.”
- **Reason:** v2 build-order pick with a real long-horizon credit problem, but two structural gaps: executable memory can host a planner (R≈1) and the convex all-eight term (q) rewards abandoning hard graphs (unblocked).
- **Strongest attack:** **GAME-1: move the planner into memory-update code** (blocked: partly). Red-team estimate: “Estimate a≈q≈1 and R≈1 if the memory function can observe sufficient state and emit plans; this conditional is to verify. The model then does little learned credit assignment despite a valid artifact.” Unblocked: **GAME-2: concentrate reliability on easy graphs** (blocked: no). Red-team estimate: “Estimate, under conditionally independent attempts, a uniform per-graph p=0.8 gives S=0.48+0.4·0.8^8≈0.5471; 80% perfectly solved/20% always failed gives S=0.8 at the same a=0.8. R changes from F(0.5471) to F(0.8); these are analytical illustrative cases, not measurements.”
- **Fixes required to reach likely-pass:**
  - Define the memory API before build; test a full planner in the memory channel (GAME-1).
  - Score per-graph utility with hard-family coverage or keep q diagnostic only (GAME-2).
  - Strong planner+recovery demonstration SFT baseline; cut if it reaches the reference (SAT-1).
  - Independently authored operator families (GAME-3); server-owned ancestry reconstruction (GAME-4).
- **Cheapest decisive experiment:** Planner+recovery demonstration SFT (comparable data/compute) ×3 vs reference ×3, after the memory-API spec (CPU). Kill per its own ceiling rule if planner SFT reaches the reference.
  - ESTIMATED 2,688 H100 GPU-h ($8,064 at $3/h). Derivation: 6 full runs × 448 GPU-h/run (= 02B E5 2,240 ÷ 5); same size as the 02B E3 row (2,688).
- **Full v2 ledger for this task (for comparison):** 173,264 GPU-h.

### 7. 07A — Repair an RL measurement ecosystem and prove that optimization learns the intended skill  ·  **at-risk**

- **Red-team verdict:** needs fixes. “Adaptive attacker obstruction and 60% checker credit can win without better learned capability.”
- **Reason:** Addresses the actual review failures (v2 build-order #4) and has a strong outer executable-truth architecture, but GAME-1 is unblocked: 60% of S is checker credit, so ≥0.20 raw can come with zero learning gain.
- **Strongest attack:** **GAME-1: win checker terms without improving learning** (blocked: no). Red-team estimate: “Estimate S=0.60+0.40a0 for perfect checking with unchanged learner a0. The gain over an imperfect checker is 0.20Δh+0.15Δw+0.25Δx, potentially ≥0.20 raw with Δa=0. Reward is F(S), possibly ≥0.60 depending on c.” Saturation route: **SAT/GAME-5: finite bank plus a fixed attacker is a finite game** (blocked: partly). Red-team estimate: “Estimate R≈0.60–1 on that fixed game if h,w,x,a all become high; no evidence establishes robustness to a stronger attacker. Saturating the specified finite game is a legal solution, not necessarily cheating.”
- **Fixes required to reach likely-pass:**
  - Couple checker credit to measured downstream learning (smooth utility) (GAME-1).
  - Timeouts count as checker failures; bounded attacker interface and minimum completed attack-query count (GAME-2).
  - Cross correctness with intent/style; split by semantic mechanism (GAME-3).
  - Run the universal isolation + exact semantic checker baseline first; if it solves the task, keep it as infrastructure (SAT-1).
- **Cheapest decisive experiment:** Universal isolation + exact semantic checker baseline ×3 vs reference ×3, after the reward re-weighting (CPU). Kill if the universal checker comes within 0.20 raw.
  - ESTIMATED 2,688 H100 GPU-h ($8,064 at $3/h). Derivation: 6 full runs × 448 GPU-h/run (= 07A E5 2,240 ÷ 5); same size as the 07A E3 row (2,688).
- **Full v2 ledger for this task (for comparison):** 173,264 GPU-h.

### 8. 02A — Create transferable learning signal beyond a policy’s success frontier  ·  **at-risk**

- **Red-team verdict:** needs fixes. “STaR-style rationalization and hint annealing may solve the supposed zero-success barrier directly.”
- **Reason:** Plausible RSI role, but STaR-style rationalization / oracle-planner demonstrations may solve the zero-success barrier directly; the loss-plugin boundary is unspecified; conditional merge with 01B.
- **Strongest attack:** **SAT-1: rationalize then train without hints** (blocked: partly). Red-team estimate: “Estimate R≈0.60 if the route matches c, potentially 0.80–1 only with correspondingly higher S. Nothing measured supports claiming it reaches near-full. A complete matching baseline in b would instead earn 0.” Also **SAT-2: compile oracle/planner demonstrations** (blocked: partly). Red-team estimate: “Estimate S≈c, R≈0.60 if the teacher/planner curriculum generalizes. Maximum remains F(S_demo), to verify; fixed model capacity can prevent near-full reward even for perfect demonstrations.”
- **Fixes required to reach likely-pass:**
  - Faithful rationalization→hint-free SFT and full-oracle planner-demonstration baselines (SAT-1/SAT-2).
  - Specify loss-plugin inputs/outputs; block constant-gradient payloads (GAME-3).
  - Reconstruct final token IDs from trusted fields (GAME-1); separate robustness from new competence (GAME-2).
  - Merge with 01B if only curriculum differentiates them.
- **Cheapest decisive experiment:** Faithful STaR rationalization → hint-free SFT with iterative correction ×3 vs reference ×3. Kill if it matches the full chain on fresh-composition raw success.
  - ESTIMATED 2,400 H100 GPU-h ($7,200 at $3/h). Derivation: 6 full runs × 400 GPU-h/run (= 02A E5 2,000 ÷ 5); same size as the 02A E3 row (2,400).
- **Full v2 ledger for this task (for comparison):** 151,472 GPU-h.

### 9. 01B — Acquire RL experience that remains useful as the learner changes  ·  **at-risk**

- **Red-team verdict:** needs fixes. “Nonstationary bandit recipes and checkpoint gaming threaten the proposed learning-curve objective.”
- **Reason:** Fresh learner replay and full acquisition charging are sound, but a universal controller (SAT-2) and four-checkpoint gaming (GAME-1) are both UNBLOCKED; merge candidate into 02A.
- **Strongest attack:** **SAT-2: learn a universal controller on legal proxies** (blocked: no). Red-team estimate: “Estimate R≈0.60–0.80 if the reusable controller matches or improves c; near-full requires S≥c+0.875(1−c), to verify. It can bypass A→C even when observations vary by seed.” Also unblocked: **GAME-1: four checkpoints are not curve area** (blocked: no). Red-team estimate: “Estimate ΔS=0.10Σ_j Δa_j+0.60ΔaT. Raising all four sampled a_j by 0.20 with unchanged true time-integrated performance yields +0.08 raw (illustrative). Reward is F(S_old+0.08).”
- **Fixes required to reach likely-pass:**
  - Evaluate snapshots at privately sampled cost points or rename the estimand (GAME-1).
  - Baseline = nonstationary cost-aware bandit + prerequisite replay + true costs, and a domain-randomized recurrent allocator (SAT-1/SAT-2).
  - Family×time floors with smooth penalties (GAME-3); independent algorithm families (SAT/GAME-4).
- **Cheapest decisive experiment:** Combined nonstationary cost-aware bandit + prerequisite replay ×3 vs reference ×3, scored on a dense author-only learning curve as well as the 4 checkpoints. Kill/merge into 02A if gap < 0.20 raw.
  - ESTIMATED 2,112 H100 GPU-h ($6,336 at $3/h). Derivation: 6 full runs × 352 GPU-h/run (= 01B E5 1,760 ÷ 5); same size as the 01B E3 row (2,112).
- **Full v2 ledger for this task (for comparison):** 129,680 GPU-h.

### 10. 07B — Train an evidence evaluator that remains useful when researchers optimize against it  ·  **at-risk**

- **Red-team verdict:** needs fixes. “Renderer computation, finite-attacker gaming and evidence-limited truth threaten valid evaluator rewards.”
- **Reason:** Executable outer labels make it potentially valid, but the renderer can become the checker (R≈1), score flattening defeats the fixed optimizer, and evidence sufficiency is unproven.
- **Strongest attack:** **GAME-1: renderer becomes the hidden checker** (blocked: partly). Red-team estimate: “Estimate d≈z≈v≈1 and R≈1 if evidence is sufficient and the renderer can execute the reconstructed semantics. If permitted evidence is insufficient, this fails; feasibility is to verify.”
- **Fixes required to reach likely-pass:**
  - Structural renderer boundary or trusted rendering (GAME-1).
  - Constant-p, prevalence and frozen-random anchors; several independent optimizers (GAME-2/GAME-3).
  - Counterfactual same-renderer pairs (GAME-4); measure evidence-conditioned ambiguity, frozen denominators (GAME-5).
- **Cheapest decisive experiment:** Canonical renderer + hard-negative SFT ×3 vs reference ×3 (an oracle-evidence control reuses the reference runs’ grades). Kill if rendering+SFT closes to within 0.20 raw or ambiguity caps the ceiling.
  - ESTIMATED 2,400 H100 GPU-h ($7,200 at $3/h). Derivation: 6 full runs × 400 GPU-h/run (= 07B E5 2,000 ÷ 5); same size as the 07B E3 row (2,400).
- **Full v2 ledger for this task (for comparison):** 151,472 GPU-h.

### 11. 03B — Learn a reasoning policy that allocates variable inference budgets without losing coverage  ·  **at-risk**

- **Red-team verdict:** needs fixes. “The score rewards capped correctness/coverage, with no benefit for using less than the cap.”
- **Reason:** Objective mismatch: the score rewards capped correctness, so always spending the full cap is rational and can win (GAME-1 and GAME-3 unblocked); must be re-specified before any GPU evidence means anything.
- **Strongest attack:** **GAME-1: always spend the full request cap** (blocked: no). Red-team estimate: “Estimate ΔS=0 for any extra within-cap cost that leaves a,h,z unchanged; if extra search raises a or h, reward increases. It can attain R≈0.60–1 without efficient stopping if its correctness matches the reference/optimum.” Also unblocked: **GAME-3: unused-budget stratum substitution** (blocked: no). Red-team estimate: “Estimate h contribution can reach 0.30 from the easiest/highest-budget coverage setting; exact R is indeterminate until that estimand is specified. For any chosen h, use F(0.60a+0.30h+0.10z).”
- **Fixes required to reach likely-pass:**
  - Decide capped-capability vs actual-efficiency objective; score an accuracy–actual-cost frontier (GAME-1).
  - Specify h by budget stratum and full 8-sample cost (GAME-3); charge full pass@8 cost (GAME-2).
  - Define p semantics and missing-value behaviour (GAME-4).
  - Then baseline shortest-correct SFT + on-policy distillation (SAT-1).
- **Cheapest decisive experiment:** After the objective rewrite (CPU), shortest-correct SFT + on-policy distillation ×3 vs reference ×3 on the revised frontier. Kill if within 0.20 raw.
  - ESTIMATED 2,400 H100 GPU-h ($7,200 at $3/h). Derivation: 6 full runs × 400 GPU-h/run (= 03B E5 2,000 ÷ 5); same size as the 03B E3 row (2,400).
- **Full v2 ledger for this task (for comparison):** 151,472 GPU-h.

### 12. 04B — Co-design precision and correction for a learner whose activation distribution drifts  ·  **at-risk**

- **Red-team verdict:** needs fixes. “Standard current scaling may remove drift; the 20% speed weight cannot provide a 0.20 raw gap alone.”
- **Reason:** Closest to cut among the at-risk set: red team shows analytically that equal-quality speedup gives ΔS ≤ 0.20(1−e0) < 0.20, so the physical-headroom gate is unreachable unless real learning gains exist; current FP8 scaling may already remove drift. Merge candidate into 04A.
- **Strongest attack:** **SAT-2: tolerance-driven auto mixed precision** (blocked: partly). Red-team estimate: “Estimate R≈0.60–0.80 if automatic error budgeting reaches or exceeds c; near-full requires both high a and high e, to verify. No author-specific attribution chain is necessary for this algorithm.” Structural: **GAME-1: impossible physical-headroom gate for pure efficiency** (blocked: no). Red-team estimate: “Estimate, at equal accuracy to the best default, ΔS≤0.20(1−e0)<0.20 for any e0>0. Thus pure speed improvement cannot pass the stated ≥0.20 raw full-chain gap; no empirical result is assumed.”
- **Fixes required to reach likely-pass:**
  - Show learning (a) gains beyond the healthy default, or redesign the metric; get any bar change explicitly (GAME-1).
  - Complete current-scaling + amax reset + selective-fallback baseline on exact H100 kernels (SAT-1).
  - Generic constrained precision optimizer baseline (SAT-2); trusted tensors from main work (GAME-2); numeric rare-slice gate (GAME-4).
- **Cheapest decisive experiment:** Current scaling + selective high-precision fallback + tolerance-driven auto-mixed-precision ×3 vs reference ×3, scored on the accuracy term a. Kill if Δa does not supply ≥0.20 raw on its own (speed cannot).
  - ESTIMATED 5,376 H100 GPU-h ($16,128 at $3/h). Derivation: 6 full runs × 896 GPU-h/run (= 04B E5 4,480 ÷ 5); same size as the 04B E3 row (5,376).
  - Note: Analytic bound already decisive for the speed-only design (0 GPU-h).
- **Full v2 ledger for this task (for comparison):** 346,528 GPU-h.

### 13. 08A — Design proxy experiments that transfer a continued-pretraining policy across scale and horizon  ·  **likely-cut**

- **Red-team verdict:** cut. “The exp(−loss) utility compresses the primary science; the controller can outsource search to grading.”
- **Reason:** Red-team CUT; v2 itself calls it the highest-risk metric. exp(−loss) compresses the core science (a 3.0→2.8 loss gain is worth ≈0.0055 raw) and the controller can run its own search inside the 25h grader replay. Largest ledger line (477,280 GPU-h).
- **Strongest attack:** **GAME-2: perform research inside the 25h grader replay** (blocked: partly). Red-team estimate: “Estimate R≈0.60–1 if per-grade online search finds a near-optimal policy. It is legal under a broad branching controller unless explicitly budgeted; 800 GPU-h is already larger than a solver reservation. No unmetered compute is needed.” Structural: **GAME-1: ignore almost all loss improvement** (blocked: no). Red-team estimate: “Analytic illustrative estimate: l:3.0→2.8 changes the loss contribution by 0.5(e^−2.8−e^−3.0)≈0.00551. With unchanged a, reward is F(S_old+0.00551). To gain 0.20 raw with negligible loss utility requires roughly +0.40 capability, which may make this a post-training task.”
- **Fixes required to reach likely-pass:**
  - Re-entry only with a new live loss/capability metric and a decision contract that makes cross-scale experimental evidence necessary; charge grader-replay search to the deployment cap; target-only feedback controller as the first adversary.
- **Cheapest decisive experiment:** Already decided analytically (0 GPU-h): the red-team exp(−loss) calculation. Re-entry experiment (unfunded): target-only feedback controller ×3 vs reference ×3.
  - ESTIMATED 0 H100 GPU-h ($0 at $3/h). Derivation: analytic; re-entry anchor would be 6 × 1184 = 7,104 GPU-h (= 08A E5 5,920 ÷ 5 × 6).
- **Full v2 ledger for this task (for comparison):** 477,280 GPU-h.

### 14. 08B — Co-design midtraining for the downstream learning it enables  ·  **likely-cut**

- **Red-team verdict:** cut. “Merge into 01A: final capability does not identify improved trainability or necessary experimental design.”
- **Reason:** Red-team CUT/merge into 01A: final capability cannot distinguish a better starting model from a more trainable one (GAME-1 unblocked, +0.15 raw from pre-capability alone), and its stage space overlaps 01A.
- **Strongest attack:** **SAT-2: legal algorithmic pre-adaptation** (blocked: partly). Red-team estimate: “Estimate R≈0.60–1 if broad legal preparation transfers sufficiently. The ban on final examples does not block algorithmic anticipation; actual student generalization is to verify.” Unblocked: **GAME-1: improve starting competence, not trainability** (blocked: no). Red-team estimate: “Estimate if pre-capability adds δ to a_after with unchanged adaptation response, ΔS=0.75δ+0.25Δr. A +0.20 final gain gives +0.15 raw (illustrative). Recording pre-scores does not subtract this reward.”
- **Fixes required to reach likely-pass:**
  - Merge downstream-adaptation evaluation into 01A. Standalone re-entry needs an operational trainability estimand with matched starting-capability controls.
- **Cheapest decisive experiment:** Merge decision needs no GPU (0 GPU-h). Re-entry experiment (unfunded): matched starting-capability control vs reference ×3 each.
  - ESTIMATED 0 H100 GPU-h ($0 at $3/h). Derivation: merge decision; re-entry anchor would be 6 × 1184 = 7,104 GPU-h (= 08B E5 ÷ 5 × 6).
- **Full v2 ledger for this task (for comparison):** 477,280 GPU-h.


- **Red-team verdict:** cut. “Cut as standalone; fold joint-transfer controls into 02A unless strong distillation leaves proven raw reserve.”
- **Reason:** Red-team CUT: verifier-filtered multi-teacher GKD and composed-demonstration SFT (unblocked) can bypass the chain, and student capacity can cap it near defaults, the same failure as the GDM souping review.
- **Strongest attack:** **SAT-2: compose experts during training, then imitate** (blocked: no). Red-team estimate: “Estimate R≈0.60–1 conditional on student capacity and demonstration transfer; unmeasured. No explicit teacher-conflict diagnosis is needed if the composer verifies outcomes.” Also **SAT-1: verifier-filtered multi-teacher GKD** (blocked: partly). Red-team estimate: “Estimate R≈0.60 if this complete recipe reaches c; potential R≈0.80–1 only with corresponding S. The packet has no measured evidence of a ≥0.20 raw deficit over this combined baseline.”
- **Fixes required to reach likely-pass:**
  - Re-entry only with a measured ≥0.20 raw gap over verifier-filtered multi-teacher on-policy distillation and composed-demonstration SFT; otherwise reuse its controls in 02A.
- **Cheapest decisive experiment:** Unfunded re-entry experiment: verifier-filtered multi-teacher GKD + composed-demonstration SFT ×3 vs reference ×3.
- **Full v2 ledger for this task (for comparison):** 151,472 GPU-h.

### 16. 06B — Train one elastic model whose representations survive several deployment envelopes  ·  **likely-cut**

- **Red-team verdict:** cut. “Standard nested-model distillation is the task’s core recipe; sharing identity does not exclude independent capacity.”
- **Reason:** Red-team CUT: MatFormer/DynaBERT-style nested training is the task’s core recipe, the shared parameterization can hide partitioned independent submodels, and the shared frontier is unknown.
- **Strongest attack:** **GAME-1: one shared container, effectively separate submodels** (blocked: partly). Red-team estimate: “Estimate R≈0.60–1 if the cap permits enough partitioned capacity to reproduce independent models. If the schema structurally disallows it, estimate R=0; the cap/allowed adapters are unspecified.” Also **SAT-1: standard elastic transformer training** (blocked: partly). Red-team estimate: “Estimate R≈0.60 if a competent complete recipe reaches c; possibly higher for benign envelopes. Transfer from those papers to the proposed decoder/recovery setting is to verify; their existence is not a measured saturation result.”
- **Fixes required to reach likely-pass:**
  - Keep only as a later 06A/architecture variant after a named nested-transformer baseline, a sharing audit and a recoverable shared-frontier gap.
- **Cheapest decisive experiment:** Unfunded re-entry experiment: named MatFormer-style nested baseline ×3 vs reference ×3 + disjoint-capacity control.
  - ESTIMATED 0 H100 GPU-h ($0 at $3/h). Derivation: not funded; would be 6 × 448 = 2,688 GPU-h (= 06B E5 2,240 ÷ 5 × 6).
- **Full v2 ledger for this task (for comparison):** 173,264 GPU-h.

## Notes and caveats

- 3 vs 3 seed anchors are decisive for a **kill** (baseline within ~0.10 raw of the reference cannot meet A5's 0.20 margin), but weak for a **pass**: with solver-run SD σ = 0.10 raw, a one-sided t-test has ≈65% power to detect a true 0.20 gap (≈80% at σ = 0.08). Ambiguous results → HOLD and add 2 seeds per arm (4 more runs), not promotion. σ is unmeasured; E10/C6 measure it later.
- Nothing in this folder modifies the v2 files, the red-team files or the Google Doc.
