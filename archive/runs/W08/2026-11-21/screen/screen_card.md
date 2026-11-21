# W08 — Contrastive retrieval beyond destructive hard negatives — saturation screen

## 1. What the grader actually rewards

The grader retrains the submitted dual-encoder recipe, then measures the fraction of every query's complete positive neighborhood recovered within an equally sized retrieval set, in both directions. Its native utility is `U=(mean_stratum_completeness+minimum_stratum_completeness)/2`, after averaging training seeds; imperfect gallery outputs retain their denominator effects. Under the ESTIMATED design constants, reward is zero below U=0.40, rises linearly to R=0.60 at U=0.78, then to mathematical perfection at U=1, with an ESTIMATED maximum claim deduction of 0.05. No-op zero, competent-recipe reserve, reference feasibility and attainable perfection are all UNMEASURED: the floor and knot are designed, rather than measured anchors, and certification floors do not invalidate an otherwise lawful high-scoring method.

## 2. Strongest lawful combined attack

Every numerical forecast, workload allocation and derived score in this card is **ESTIMATED**, including the bare numeric screen-record values. IDs and source locations identify documents; bar cutoffs are binding requirements. No cited paper measures W08.

Recover each finite caption grammar, preserving directed endpoint roles and quotienting only actual graph automorphisms. The small object bound permits bounded permutation enumeration. Compute canonical keys inside the admitted train-only token graph and propagate caption equivalence through observed image-caption edges. Disconnected pairing edges do not remove the supervision encoded in complete captions.

Use the [OpenCLIP loss implementation](https://github.com/mlfoundations/open_clip/blob/main/src/open_clip/loss.py) as an implementation reference, translating into the trusted DAG rather than loading new code into grading. Compare two complete objective families: [supervised contrastive learning](https://arxiv.org/abs/2004.11362), treating every key-matched item as positive, and [SigLIP](https://arxiv.org/abs/2303.15343), replacing diagonal-only targets with semantic pair targets and balancing pair weights. [False Negative Cancellation](https://arxiv.org/abs/2011.11765) supplies elimination/attraction alternatives; exact keys replace its uncertain identification step. Jointly fine-tune both backbones and bounded attention pooling, emphasize existing same-attribute/different-role negatives, and compare queue-free against age-weighted detached student-feature queues. Queue entries retain trusted tokens so their semantic keys remain exact. This changes pair weights, without generating examples or changing stream order.

Run ESTIMATED seven complete configurations at both public seeds: `7×2×2 A100×2.5h=70 A100-h`, plus ESTIMATED 6 A100-h protected dev and 20 A100-h compilation, diagnostics and contingency, totaling the task's ESTIMATED 96 A100-h reservation. ESTIMATED four concurrent two-device jobs require four training waves, or 10h before scheduling overhead. Tune objective, queue age, pooling, temperature and learning rate together; each completed two-seed configuration gets the real-utility proxy. No branch receives extra final training.

My ESTIMATED central native outcome is mean completeness 0.87 and weakest-stratum completeness 0.78: U=0.825 and R≈0.68 with accurate receipts. **ESTIMATED single-run R: 0.68, range 0.48–0.86; oracle best-of-four mean: 0.80; pass@4 at R≥0.60: 0.94; projected upper-95% planning bound: 0.94.** The latter is a subjective uncertainty allowance, not a fitted confidence limit. For scale, an ESTIMATED independent-attempt success probability of 0.50 gives pass@4≈0.94; shared family failures could make that estimate optimistic. Best-of-four assumes occasional configurations raise the weakest stratum, rather than merely improve easy queries.

Residual errors concern visual endpoint binding, patch resolution, paraphrase generalization and stale queue geometry. Exact training labels do not solve those problems, and the worst-stratum term makes connector failures expensive. I therefore discount §10's ESTIMATED balanced R≈0.74545 point: equal quality across all strata is an optimistic central assumption. Nevertheless, the shallow fully supervised graphs, pretrained encoders and several complete trials make crossing the repeated-search line more plausible than preserving a large research reserve. This is the same lawful-combination failure mode seen in the reviewed T02/T08/T18 packets, without importing their reward estimates.

## 3. Other routes

- **Single recipe:** canonical-caption supervised sigmoid training with ordinary global pooling and no queue. ESTIMATED R=0.52, range 0.30–0.70. It removes false-negative gradients immediately but may leave global embeddings insensitive to role order. The [ARO/NegCLIP paper](https://arxiv.org/abs/2210.01936) establishes that compositional failures and negative-based remedies are known; its results do not establish W08 completeness.
- **Search route:** enumerate a compact objective/temperature/learning-rate/queue grid, keeping the inherited pooling and selecting on protected U. ESTIMATED R=0.61, range 0.38–0.78. The same ESTIMATED seven-configuration budget fits; selection can find a sufficiently good known combination without reconstructing the proposed insight chain. Fresh proxy banks constrain item memorization but preserve lawful method selection.
- **Lawful-looking grading shortcut:** copy authenticated mandatory observations and label untested extrapolations as predictions, omitting optional empirical claims. Applied to the combined learner, ESTIMATED R remains 0.68, range 0.48–0.86; it avoids an ESTIMATED deduction of up to 0.05 without improving retrieval. This is legitimate reporting and makes the W3 term weak. Sacrificing one entire stratum is no longer a saturation shortcut: the revised formula assigns ESTIMATED R≈0.06 to otherwise perfect performance with one zero stratum.

## 4. What would lower lawful saturation

First test a new training-view contract in which individually supplied captions omit complementary relation clauses, while evaluation captions and graph truth remain complete. Publish the shift and retain all canonicalization that is possible from legal evidence. This could lower the combined score by ESTIMATED 0.08–0.18, to ESTIMATED R=0.50–0.60, but changes the distribution and requires fresh observability/proxy validation. Cost: ESTIMATED 10–15 author-days plus 128 H100-h for feasibility comparisons; it is not a certified repair.

Within the existing complete-caption premise, author denser coupled endpoint compositions and cross nuisance renders with every relation assignment, preserving visibility and tokenizer limits. ESTIMATED reduction is only 0.04–0.10; ESTIMATED cost is 5–8 author-days and 96 H100-h for matched learnability checks. Neither change clearly clears every kill line. Raising the reward floor or withholding predictive dev would conceal the recipe's success rather than create native reserve.

## 5. Decisive-check GPU-h re-estimate

W08 §7, lines 219–220, labels its broad cheap-anchor tranche **“6,660 /9,000”** expected/cap GPU-h; these are ESTIMATED A100 allocations, not a narrowly isolated decisive experiment. The same section gives **“36 expected;72 hard cap”** for a seed-inclusive complete grade. There is no separately priced minimal saturation check.

After the CPU canonicalizer/ABI gate, my narrower check is **ESTIMATED 259 H100-h**:

- Calibration search: ESTIMATED seven configurations × two public seeds × two H100s × 1.75h = **49 H100-h**.
- Freeze two complete objective stacks, default CLIP and the author's reference. Across ESTIMATED three independent content blocks, three training seeds per arm, two H100s and 1.75h per run: `4×3×3×2×1.75` = **126 H100-h**.
- ESTIMATED twelve artifact/block grades × 6 H100-h of gallery evaluation, bound claim replay, dtype/memory checks and cold reconstruction = **72 H100-h** beyond the training already counted.
- ESTIMATED 12 H100-h for initial throughput/compiler profiling and failed-work allowance.

The subject is the inherited ESTIMATED 150M-parameter ViT-B/32 dual encoder with bounded added pooling, not a larger replacement. The ESTIMATED H100 runtime is a profiling hypothesis, not a measured A100 conversion; all fixed updates and galleries remain intact. This battery can reject reserve or show a stack's mean already above the best-of-four cutoff; it cannot certify tail safety or measure a hypothetical researcher's scaling. Corpus construction, the larger-model scale check and full certification are excluded from this minimal estimate.

## 6. Duplicate check

Source contracts were opened rather than relying on W08's dedupe table.

- **v3 01A — WEAK:** changes corpus preprocessing/weights across learning stages; W08 fixes examples and changes embedding training.
- **FIX T11 — MODERATE:** learns grounded static relations and temporal evidence, but permits scene interventions and grades VLM answers rather than complete cross-modal retrieval.
- **Catalog T19 — MODERATE:** shares equivalence-aware geometry and role-sensitive ranking; its learned satisfaction evaluator and independent-producer selection target differ from retrieving every equivalent item in both modalities.
- **D20 — WEAK:** source-grounded synthetic-content fidelity can preserve compositional relations, but its editable artifact is generated training content, not fixed-stream encoder geometry.
- **Creative C096 — MODERATE:** representation learning must retain small diagram violations; its bottleneck/detection outcome differs from neighborhood alignment. **C003 — WEAK:** changes image-caption selection and scores relation tuples, so its shared spatial-grounding motivation does not make the intervention identical.
- **Sibling W02 — MODERATE:** jointly trains retrieval and reading through evidence/index revisions; W08 has static evidence and directly grades two encoder spaces.

No inspected predecessor has both the same intervention and grader target. Duplicate strength does not bind this cut.

## 7. Verdict

**CUT.** Binding line: **oracle best-of-four mean >0.60**; ESTIMATED attack 0.80 exceeds it by ESTIMATED 0.20. The single-run point is below its cutoff, but stronger successful attempts and the ESTIMATED upper planning bound also threaten the absolute limits. The revision repairs the critique's abandoned-stratum arithmetic, optional-filler dilution and missing dev/no-call semantics on paper. It leaves the central objection unresolved: complete captions provide exact lawful supervision, and no measured native reserve or necessary dependent insight chain survives a competent joint stack. This is a desk rejection, not an observed empirical breach; no souping/merging dependency is present.

## 8. Measurement status

Rollouts **UNMEASURED** (planned: independent full-budget attempts after the recipe gate, retaining failures and block-level best-of-four statistics). Grader noise **UNMEASURED** (planned: fixed-artifact regrades separating seed, semantic-block and host variance). Score ladder **UNMEASURED** (planned: category-only, single-positive, canonicalized sigmoid, full-stack and reference artifacts under the revised mean/worst utility). Competent-recipe anchor **UNMEASURED** (planned: canonical-key confusion audit followed by the matched objective/search battery above; retain raw stratum completeness and native gaps).

## Screen record

Numbers below are ESTIMATED.

id: W08
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.68
attack_single_range: 0.48-0.86
bo4_est: 0.80
pass4_est: 0.94
ub95_est: 0.94
gpuh_task_stated: 6660-9000
gpuh_new_est: 259
duplicate_of: v3-01A WEAK; FIX-T11 MODERATE; catalog-T19 MODERATE; D20 WEAK; C096 MODERATE; C003 WEAK; W02 MODERATE
kill_reason: exact-caption supervision plus joint recipe/search exceeds repeated-search cutoff
souping_flag: no
