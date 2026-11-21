# C096: Discover an image representation that retains violated constraints — independent adversarial review

**Verdict: FIX.** A byte-limited representation could face a real tradeoff when small symbols change meaning under the diagram's constraint system. The current proposal leaves open easier routes: answer-only encoding, sparse lossless symbol storage and ordinary task-aware compression. Keep the idea only after the query timeline, complete channel capacity and a learnable semantic rate frontier are fixed.

Source file: `/workspace/task_ideation_v4_creative/cards/C096.md`.

This assessment inspected the card and shared references, without training an encoder or rendering a dataset. Rollout scores, grader noise, observed runs and pass@k observed are **UNMEASURED**; the planned study compares independently trained codecs under a fixed reasoner and fresh diagram/constraint families. All numerical forecasts are ESTIMATED. No actual codec files, byte budget, image schema or downstream reasoner are specified by the source.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Transmit the answer rather than an image | Let the encoder perform violation detection and reasoning before compression; transmit only predicted truth and conclusion labels in its legal fixed-byte output. | ESTIMATED 0.72–0.97 | No query timing or encoder access contract rules this out. | If reusable representation is intended, freeze encoding before independently sampled queries and test many questions from one immutable code; otherwise acknowledge answer prediction as legal. | ESTIMATED 0.45–0.78 | Even query-independent constraint truth vectors may fit easily and remain a lawful sufficient statistic. |
| Sparse exact diagram codec | Parse lines, text, small marks and junctions; encode positions and symbol identities or sparse raster residuals exactly within the byte cap, leaving reasoning to the fixed decoder. | ESTIMATED 0.63–0.93 | Sparse scientific diagrams may be highly compressible; no actual cap or entropy study exists. | Measure lossless/symbolic and multiscale-residual rate frontiers on every family; choose a real semantic bottleneck without banning exact coding. | ESTIMATED 0.63–0.93 | If all relevant structure fits, a learned lossy representation is unnecessary. |
| Count latent values instead of bytes | Store high-precision floating latents, variable-length crop coordinates, hyperprior side information or decoder-selected tables outside the nominal bottleneck. | ESTIMATED 0.77–1.00 | Fixed bytes is named without a serialized channel definition. | Count actual complete serialized payload, metadata, entropy side streams and retained state; canonical finite format and hard allocation at the boundary. | ESTIMATED 0.00 | Metadata can be semantically useful even when small; every transmitted choice contributes capacity. |
| Filesystem/mount/proc/IPC/frozen-asset access | Recover hidden diagram programs or labels from renderer buffers, temporary SVG files or evaluator descriptors; modify the frozen reasoner or base encoder assets. | ESTIMATED 0.90–1.00 | Program-derived labels are requested, but no renderer/evaluator privilege boundary is described. | Raster-only candidate input, private generation outside worker mounts, immutable decoder and separate IPC; proposed `test_diagram_program_boundary` covers proc and shared-memory paths. | ESTIMATED 0.00 | Temporary vector originals or rendering caches can survive nominal raster export. |
| Interface or encoded-state smuggling | Pack hidden diagram answers in model initialization, codec headers or learned external lookup files; reconstruct unreceipted weights through an encoder configuration callback. | ESTIMATED 0.83–1.00 | Headers should be label independent, but weight and auxiliary-state provenance are absent. | Permit ordinary learned bitstreams while authenticating training lineage and forbidding private truth ingress; bound nonimage channels and cold-reconstruct all permitted state. | ESTIMATED 0.00 | Content-dependent encoded bits are the intended representation, so payload scans cannot prohibit useful semantic compression. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Print a correct-looking violation record instead of invoking the reasoner, skip tiny-mark cases, or hash-match canonical clean diagrams and return memorized outcomes. | ESTIMATED 0.85–1.00 | Exact detection is intended but its ownership and fixture independence are undefined. | Parent decodes actual bytes and executes fixed query tests; independent equivalent diagrams are required positives; missing code/query results stay failures. | ESTIMATED 0.00 | A formally exact checker still needs a complete definition of legitimate small symbols. |
| Timing/check-decoupling/branch laundering | Train the reasoner with full-resolution features, grade with purported bottleneck features, retain raw-image embeddings between phases or swap the encoder after reconstruction checks. | ESTIMATED 0.76–0.99 | Matching downstream training is proposed only for the pilot, without an enforced channel cut. | Cold separate encoder/decoder processes, immutable bytes and hashes, no raw-image cache in the reasoner; charge all codec training and selected-state ancestry. | ESTIMATED 0.00 | Hidden per-example caches can masquerade as harmless preprocessing unless cold replay reconstructs everything. |
| Dev-hidden leakage/cue inference | Classify validity from raster metadata, anti-aliasing, renderer version, file size or generator-specific mark style rather than preserving the semantic constraint. | ESTIMATED 0.60–0.92 | Header independence addresses part of this; pixel-level rendering correlations are not addressed. | Cross renderers and visual styles with constraint truth; use paired edits and independent constraint programs, metadata-only and low-frequency-only baselines. | ESTIMATED 0.20–0.53 | A single valid symbol may itself correlate with truth; causal twins must separate its context-dependent meaning. |
| Adaptive aggregate oracle | Change crop priorities or relation-loss weights one class at a time, infer private violation weights from dev scores and share scoring across encoder branches. | ESTIMATED 0.57–0.85 | Matching visual scale/noise is not an information-budget policy. | Global feedback precision/query/cost contract; fresh diagram blocks and adaptive-winner evaluation on untouched systems. | ESTIMATED 0.33–0.65 | Legal tuning may discover a universal high-resolution residual allocation. |
| Slice abandonment/denominator optimization | Detect common large violations, flag every tiny mark as invalid, or omit hard constraint systems from the reasoning average. | ESTIMATED 0.63–0.94 | Semantic weighting is promised without positive/negative balance or family denominators. | Fixed system/query slots, rare-valid-small-symbol controls, false-positive costs and calibrated semantic effect weights; evaluate always-anomaly and common-only anchors. | ESTIMATED 0.21–0.55 | Heavy penalties can encourage broad conservatism unless authorized normal conclusions also carry utility. |
| Strongest lawful combined recipe | Use task-aware rate-distortion training with multiscale residual allocation, patch anomaly features, relation supervision and legal crop selection; compare sparse exact coding and answer/statistic encoding under the same complete byte limit. | ESTIMATED 0.67 (ESTIMATED 0.40–0.90) | The artifact and grading rules admit this complete family. | Measure the best lawful codec at each rate before defining the author reference's residual semantic advantage. | ESTIMATED 0.67 (ESTIMATED 0.40–0.90) | Standard sufficient-statistic compression could solve all private constraint compositions. |

## Published recipe shortcut — web checked

- [Variational image compression with a scale hyperprior](https://arxiv.org/abs/1802.01436): primary search material establishes learned rate-distortion coding and side information as a conventional compression baseline.
- [Lossy Compression for Lossless Prediction](https://arxiv.org/abs/2106.10800): the primary abstract explicitly studies predictive-task-preserving compression rather than reconstruction alone.
- [Towards Total Recall in Industrial Anomaly Detection](https://arxiv.org/abs/2106.08265): primary search material establishes patch-level anomaly representation as an available baseline ingredient; industrial anomaly success is not transferred to scientific symbols.
- [V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs](https://arxiv.org/abs/2312.14135): the checked primary abstract supports guided detail acquisition as an existing alternative to uniformly downsampling the image.

Verification consists of primary abstracts/search excerpts, not complete method reproduction or a codec implementation audit. A V*-inspired crop route must pay for its pixels, models, indices and encoded metadata; it gets no larger byte or inference allowance. Task-aware losses and sparse coding are adversarial engineering combinations, with no claim that any cited paper already solves C096. Combined forecast: **ESTIMATED 0.67 (ESTIMATED 0.40–0.90)**.

The source's focus on perceptual reconstruction is an incomplete baseline. A codec trained for downstream prediction can deliberately sacrifice visually large normal regions to preserve a decisive small mark. Whether that is enough depends on the number of potentially relevant marks, semantic systems and queries sharing one code. Those are missing task parameters, not intrinsic limitations of task-aware compression.

## Saturation against the hypothetical 10T researcher / 12h

A strong researcher can jointly tune semantic loss, residual allocation and rate, or derive a symbolic scene representation from a constrained diagram grammar. It can also notice that an answer or a vector of constraint truth values is a sufficient statistic when the downstream queries are known. Requiring a “representation” does not by itself require reconstruction, and reconstruction is only diagnostic in this card.

For the uncorrected proposal I estimate **ESTIMATED single-run maximum 0.84 versus the >0.70 gate**, **ESTIMATED oracle best-of-4 mean 0.78 versus >0.60**, **ESTIMATED pass@4 0.86 versus >0.50 at R≥0.60**, and **ESTIMATED projected upper-95% 0.96 versus ≥0.75**. These are likely absolute breaches, stated as scenarios rather than empirical outcomes or fitted intervals. The broad lower recipe range reflects possible genuine semantic interference at an actually binding byte rate.

S1 remains OPEN: a cap could be generous enough for near-lossless structure or too severe for any legal encoder to retain the decisive evidence. Neither regime demonstrates a mid-range reference with attainable reserve. S7 needs the independently measured same-rate achievable ceiling and uncertainty; visual reconstruction quality cannot substitute for that semantic ceiling. If the stronger control uses extra pixels, state or bytes, it is diagnostic rather than an attainable bound.

All observed saturation metrics are UNMEASURED. A suitable future study would use independent constraint-system blocks, separate encoder/decoder reset, fixed downstream learner seeds and byte rates chosen before private evaluation. Researcher inference, codec training, reasoner fitting and evaluation must be charged separately. Budget sweeps and stronger-tier projections follow only after the known-method frontier leaves native reserve; confidence intervals touching a line stay HOLD. Present-model misses of tiny details, cited in weakness reports, offer no resistance evidence for the target researcher.

## Revised estimate versus the source card

The source's **ESTIMATED 0.43** includes an autoencoder, residuals, anomaly sampling and relation loss. My **ESTIMATED 0.67 (ESTIMATED 0.40–0.90)** adds the crucial alternatives of predictive compression, sparse exact structure and answer-only coding where currently legal. The card's rare-valid-symbol example does not defeat direct semantic supervision; it mainly shows why anomaly scores alone are insufficient.

I retain FIX because query-independent preservation across changing constraint meanings could create a real information-allocation problem. The fix must keep legal parsing, task-aware training and lossless coding, then establish a residual at a feasible rate. Moving the rate after observing successful hidden results or banning symbolic encodings would be artificial rescue. The moderate combined-recipe calibration examples support skeptical whole-method testing without dictating this task's estimate.

## Boilerplate and missing build content

Generic prose accounts for **ESTIMATED 30–40%**, and **ESTIMATED 60–70%** identifies the small-mark semantic bottleneck. It is not mostly boilerplate, but lacks a buildable codec contract. Missing items include image resolution/noise, diagram grammar, constraint semantics, annotation rights, byte cap and serialization, query reveal timing, encoder-side access to text, decoder architecture and all persistent-state rules.

Also absent are training labels and privileges, semantic effect weights, exact violation/correct-conclusion predicates, false-positive costs, rate selection procedure, attainable upper/lower bounds and an executable author reference. Program truth is only valid if the rendered image preserves the necessary distinctions; multiple programs rasterizing identically with opposite labels would make the target unobservable. Paired tiny edits should be independently inspected for actual raster distinguishability before any GPU work.

## Duplicate check

Checked T11 FIX material already uses direct visual labels, counterfactual changes and strong joint visual/temporal learning. C096 differs by forcing all downstream evidence through a serialized fixed-byte channel, which could be a substantive distinct intervention if enforced. Checked T10 covers paid visual acquisition and is a neighboring baseline rather than the same artifact. No checked source establishes a duplicate; unread catalog or creative tasks are outside that conclusion.

## Verdict, required fixes and cheapest decisive check

**FIX** through the following concrete contract changes:

1. Declare whether encoding precedes unknown queries, define which constraint-system information is visible, and require a single immutable code for the intended downstream query set.
2. Count all transmitted bytes and cold-persisted state, including crop positions and entropy side information; prevent raw pixels or feature caches reaching the reasoner outside that code.
3. Build task-aware, sparse exact and sufficient-statistic baselines. Show a feasible semantic rate interval where they do not already attain the reference.
4. Create independently authored constraint/raster families with context-changing symbol meanings, valid unusual marks and image-observable truth; freeze effect weights and false-positive treatment.

The cheapest decisive check is CPU information accounting on the proposed diagram grammar: determine whether a complete symbolic parse or truth vector fits the intended serialized budget, and whether every opposite-truth pair is distinguishable in the raster. **ESTIMATED 0 H100-hours**. This directly kills an unbinding or impossible bottleneck before encoder training. A later GPU comparison needs actual codec/reasoner architecture and corpus size; the card's generic allowance cannot be responsibly validated from the current inputs.

Required R2 release work includes live rendering-sidecar and descriptor attacks, hidden-state/encoded-weight PoCs, parent-owned program truth, independent equivalent positive diagrams and same-byte downstream execution tests. Portable isolated startup, no solver secrets/egress, bounded parser behavior, full branch/seed costs and complete private archive reconciliation remain unbuilt. Satisfying these security requirements would not suppress a lawful semantic codec's score.

## Verdict record
id: C096
source_group: creative_v4
verdict: FIX
strongest_attack: ESTIMATED 0.67 (0.40–0.90)
combined_recipe_attack: ESTIMATED 0.67 (0.40–0.90)
best_of_4: ESTIMATED 0.78
pass_at_4: ESTIMATED 0.86
single_run_max: ESTIMATED 0.84
upper95_projected: ESTIMATED 0.96
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: query timeline; complete byte channel; symbolic and predictive codec floor; raster-observable semantic families
main_kill_reason: answer or sparse exact encoding may bypass representation tradeoff
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 4
