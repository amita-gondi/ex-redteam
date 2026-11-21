# C096 — Discover an image representation that retains violated constraints — screen audit
## 1. What the screen claimed
ViT/MAE initialization, counterfactual diagram supervision, relation losses and structural-plus-residual coding formed the old attack. The screen forecast ESTIMATED single/bo4/pass@4/ub95 of 0.47/0.57/0.28/0.72 and kept CONDITIONAL, with a blank TSV kill category: a sparse symbolic description might eliminate the supposed information bottleneck. The old source URLs were:
- https://arxiv.org/abs/2010.11929
- https://arxiv.org/abs/2111.06377

## 2. Evidence audit
ViT establishes a scalable image architecture; MAE establishes effective masked-image pretraining. Neither paper demonstrates retention of tiny falsifying marks through a specified byte channel, counterfactual constraint transfer, or the proposed symbolic supervision pipeline. The strongest bypass was therefore more specific than its evidence.

Grade: ASSUMED. Even the central channel capacity is absent, so neither successful graph compression nor unavoidable information loss follows. Modern diagram evidence makes parsing a credible baseline while contradicting any presumption that precise structural extraction is already uniformly reliable.

## 3. Research done now
- *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale* — Alexey Dosovitskiy et al., 2020 — https://arxiv.org/abs/2010.11929 — fetched — Confirms the encoder family, without a semantic compression result; it cannot carry the claimed attack score.
- *Masked Autoencoders Are Scalable Vision Learners* — Kaiming He et al., 2021 — https://arxiv.org/abs/2111.06377 — fetched — Supports initialization and reconstruction learning, not preservation of a conclusion-reversing pixel feature.
- *Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams* — Weihao Bo et al., 2026 — https://vi-ocean.github.io/projects/diagram-mmu/index.html — fetched — Separates diagram parsing from answering and tests tool-supported settings. Imperfect parsing lowers confidence in a lossless graph shortcut.
- *STRUDEL: Unrolling a Benchmark for Evaluating Vision-Language Models on Structured Diagram Understanding across Domains* — Daniel Steinigen et al., 2026 — https://aclanthology.org/2026.lrec-1.866/ — fetched — Formal diagram representations are useful supervision, but identification and quantification remain weaknesses; supports both the bypass and its unresolved precision requirement.
- *MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering* — Chan Jun Shern et al., 2024 — https://arxiv.org/html/2410.07095v1 — fetched — Demonstrates autonomous supervised-model development; no fixed-byte violation-preserving encoder is evaluated.
- *PaperBench: Evaluating AI's Ability to Replicate AI Research* — Giulio Starace et al., 2025 — https://arxiv.org/html/2504.01848v1 — fetched — Research-code reproduction is possible but incomplete, lowering certainty that an agent will build and validate a new codec/reasoner jointly within this deadline.

## 4. Re-estimated attack
Use downstream exact utility, not reconstruction quality, as the reward target. Under a literature-composition reading, allocate ESTIMATED 0.24 to a trained multiscale encoder, 0.15 to paired mark/relationship supervision and 0.10 to symbolic distillation plus byte allocation. These are overlapping engineering contributions expressed as a sequential gain budget, not benchmark measurements. Residual loss is failure to predict which details become decisive under new rule compositions.

An ESTIMATED distribution places probability 0.20 at 0.28 for poor latent allocation, 0.60 at 0.49 for useful semantic coding, and 0.20 at 0.72 when a compact near-lossless graph fits. Single=0.20×0.28+0.60×0.49+0.20×0.72=0.49, range 0.28–0.72. Bo4=0.28+0.21(1−0.20⁴)+0.23(1−0.80⁴)=0.63; p=0.20 gives pass@4=1−0.80⁴=0.59; ub95=0.72. Run spread chiefly reflects finding a sufficient symbolic representation, not random visual noise. Relative to the old estimate, the larger best-of-four gap exposes a plausible shortcut branch that its narrow pass@4 obscured. This evidence-only recipe forecast would CUT.

## 4A. Demonstrated capability and subfield SOTA
No fetched work establishes SOTA for exact violation retention at this unspecified bitrate. Diagram-MMU's published parsing comparator reaches 56.97 in its “All” column with Kimi-K2.5, while answering and spatial parsing differ substantially. Those source-reported metrics are not this card's rewards. A north star must instead be a measured byte-constrained codec with verified semantic sufficiency; uncompressed program answers provide correctness labels but cannot establish a legal attainable R≈1.

For autonomous engineering, o1-preview+AIDE in MLE-bench earns medals on 16.9% of tasks with 24 hours and one A10. That demonstrates training/search execution, with twice this wall budget and no representation-channel requirement. Separately, o1+IterativeAgent obtains 24.4% PaperBench rubric credit in twelve hours on one A10: implementing research is demonstrated, but complete codec construction is not inferred from partial rubric credit. Diagram-MMU's MCP-based syntax assistance supplies an additional domain-specific tool experiment; its engineering-session time and accelerator cost are unreported, and using that tool is not autonomous encoder research.

KNOWN-RECIPE covers task supervision and formal diagram coding. The claimed integration of selective compression, unseen constraint composition and learned reasoning lacks an AGENT-DEMONSTRATED counterpart. attack_basis=ASSUMED. The missing twelve-hour accomplishment is discovering a sufficient representation and proving its byte-accounted generalization.

The ANCHORED ESTIMATED distribution is 0.20 at 0.23 for training/interface failure, 0.66 at 0.45 for effective imported supervision, and 0.14 at 0.69 for successful graph distillation. Single=0.44, range 0.23–0.69; bo4=0.23+0.22(1−0.20⁴)+0.24(1−0.86⁴)=0.56; pass@4=1−0.86⁴=0.45; ub95=0.69. These probabilities express uncertain transfer, not measured agent frequencies. The verdict rests on assumption, especially the unknown bytes-to-information ratio.

## 5. Verdict under the kill lines
Section 4 gives CUT through ESTIMATED bo4 0.63 and pass@4 0.59. The headline ANCHORED verdict is CONDITIONAL, UNCHANGED from the old screen, because demonstrated engineering falls short of the combined attack and bo4 clearance is only 0.04. Neither the lack of an agent demonstration nor imperfect general diagram parsing proves resistance.

## 6. Redesign
Class (c): a compiler-compatible diagram language could expose a sufficient compact representation. REDESIGNABLE. Freeze a numerical byte cap only after comparing lossless raster, sparse graph, multiscale residual and learned task codecs. Make the encoder observe the current constraint specification, and construct scientific diagram families where the same visible mark participates in different disclosed relational contexts. Use executable constraint programs for labels and predictive dev compositions at matching resolution. Select a regime in which a stronger legal codec retains the important relations, while a complete graph exceeds the channel for a real information reason; abandon regimes without that feasibility witness.

This defeats the specific recipe of universal graph extraction plus lossless serialization only when relation-conditioned selection is necessary. It does not ban parsing or conceal rules. Efficient transmission of scientific evidence remains a useful frontier capability. The best re-attack is graph-supervised coding with query-conditioned residual selection; its basis stays ASSUMED, and the main risk is that a simple relevance filter already suffices.

ESTIMATED redesign outcomes: probability 0.25 at 0.21, 0.65 at 0.39, 0.10 at 0.62. Single=0.37; bo4=0.21+0.18(1−0.25⁴)+0.23(1−0.90⁴)=0.47; pass@4=1−0.90⁴=0.34; ub95=0.62. Proposed decisive compute is ESTIMATED 3 codec arms×2 seeds×(10 encoder-training hours+4 reasoner hours)×1 H100=84 GPU-h for a 100M encoder and 300M reasoner, plus 12 for exact decoding and counterfactual evaluation: 96 H100 GPU-h. That pilot tests the bottleneck, not large-VLM training claims.

## 7. Measurement status
Rollouts UNMEASURED (planned full-budget codec development with symbolic supervision allowed). Grader noise UNMEASURED (planned independent encoder/reasoner seeds and repeat decoding). Score ladder UNMEASURED (planned native accuracy-versus-bytes curves including the graph baseline and feasible selective control).

## Audit record
id: C096
old_verdict: CONDITIONAL
evidence_grade: ASSUMED
sources_old_count: 2
sources_new_count: 4
sources_fetched_count: 6
old_single: 0.47
old_bo4: 0.57
old_pass4: 0.28
old_ub95: 0.72
new_single: 0.49
new_single_range: 0.28-0.72
new_bo4: 0.63
new_pass4: 0.59
new_ub95: 0.72
new_verdict: CUT
binding_line: bo4>0.60
flip: CONDITIONAL->CUT
kill_cause_class: c
redesign_status: REDESIGNABLE
redesign_oneline: Establish a feasible numerical channel where observable rule-conditioned retention outperforms a complete sparse graph codec.
redesign_single: 0.37
redesign_bo4: 0.47
redesign_pass4: 0.34
redesign_ub95: 0.62
redesign_gpuh: 96
attack_basis: ASSUMED
demonstrated_ref: MLE-bench, o1-preview+AIDE, 2024; PaperBench, o1+IterativeAgent, 2025
gap_to_attack: validated semantic codec discovery at a specified byte rate
subfield_sota_ref: Diagram-MMU parsing comparison, Bo et al., 2026; exact channel SOTA unverified
anchored_single: 0.44
anchored_bo4: 0.56
anchored_pass4: 0.45
anchored_ub95: 0.69
anchored_verdict: CONDITIONAL
anchored_binding_line: bo4>0.60
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: ASSUMED
souping_flag: no
