# C021 — Design experiments that expose architecture–data complementarity — saturation screen
## 1. What the grader actually rewards
The experiment plan and selected architecture/data program earn credit through final held-out language-model loss after all failed probes and final training have consumed the shared budget. Finding an interaction in a report receives nothing unless enough budget remains to deploy it. ESTIMATED R≈0 is the complete interaction-search floor and ESTIMATED R≈1 an attainable stronger final training outcome; inherited one-factor rejection is tentatively ESTIMATED R=0.00 and reference ESTIMATED R=0.60, with no native loss anchors yet frozen.
## 2. Strongest lawful combined attack
Immediately test the named losing edits jointly: the prompt itself makes positive complementarity the leading hypothesis. Expand to a compact factorial design over admissible architecture/data edits, including interaction terms in a surrogate rather than using coordinate descent. [SMAC3](https://arxiv.org/abs/2109.09831), verified by web search, provides conditional configuration optimization; [BOHB](https://proceedings.mlr.press/v80/falkner18a.html) provides resource-aware multi-fidelity search. [RegMix](https://arxiv.org/abs/2407.01492) verifies cheap proxy experiments for data-mixture response modeling, although architecture changes require separately validating proxy transfer.

The frontier researcher combines domain reasoning about the architecture's representational bottleneck with pairwise screening, retains uncertain slow starters and fits learning-curve features conditional on both edits. Reserve a final continuation tranche before exploratory runs. Promote combinations on evidence of complementary gradients or emerging representations, not only early absolute loss; a small set of long probes guards against misleading short-fidelity rankings. Every branch and checkpoint continuation is charged. This stack can discover a joint winner without separately reconstructing the author's intended insight chain.

ESTIMATED single-run R=0.65, range 0.40–0.84; ESTIMATED oracle best-of-4=0.75; ESTIMATED pass@4 at R≥0.60=0.84; ESTIMATED upper-95% projection envelope=0.92. These are unmeasured forecasts. A large fraction of the apparent reference advantage may be gained simply by refusing the inherited one-factor conclusion and trying the joint edit. The residual is an informative feature that appears only after substantial combined training, making cheap proxies unreliable. That could produce a hard research problem, but the card does not instantiate a constrained search space, proxy failure or transferable selection rationale that defeats the full interaction-aware stack.
## 3. Other routes
- A small factorial experiment followed by a full run of the best joint candidate: ESTIMATED R=0.56, range 0.29–0.78. It is stronger than the card's coordinate-descent foil and requires little specialized tooling.
- Multi-fidelity Bayesian search over edit pairs and continuation duration, with an explicit exploration reserve for poor early losses: ESTIMATED R=0.62, range 0.36–0.82. This outcome-only route can exploit the same interaction without mechanistic diagnosis.
- Directly synthesize a data representation aligned with the proposed architectural inductive bias, then train that pair. ESTIMATED R=0.58, range 0.27–0.85. Strong paper recall and code inspection make this a credible route when candidate edits reveal the missing representation.
## 4. What would lower lawful saturation
Replace a disclosed pairwise reversal with families whose early observations support multiple scientific hypotheses, each recommending a different affordable joint probe. Give a reusable legal diagnostic that predicts which long training experiment is worth funding; include complete pairwise and conditional multi-fidelity search in the floor. Require the reference's advantage to survive longer continuations at the same deployed budget. Forecast revised attack: ESTIMATED R=0.39, range 0.20–0.61. Cost is ESTIMATED several researcher-months to build actual mechanism families and ESTIMATED 960 H100 GPU-h for proxy-to-final validation. A hidden winning pair among many arbitrary knobs would create expensive guessing rather than an identifiable research task.
## 5. Decisive-check GPU-h re-estimate
Old allowance: ESTIMATED 14 GPU-h. Revised ESTIMATED 480 H100 GPU-h assumes an ESTIMATED 1B-parameter language learner, ESTIMATED 4 architecture/data combinations, ESTIMATED 3 seeds and ESTIMATED 24 H100-hours for each billions-of-token continuation: ESTIMATED 4×3×24=288. Add ESTIMATED 8 proxy configurations×3 seeds×6 H100-hours=144 GPU-h, plus ESTIMATED 48 GPU-h for independent final-loss and longer-continuation checks. Total ESTIMATED 288+144+48=480. Both edits and their combination must be trained, not inferred from short loss traces. The old budget might spot a toy reversal but cannot validate its survival at a representative learning scale.
## 6. Duplicate check
Catalog T03 (`task_catalog_v3_full/packets/T03.md`, source opened): MODERATE. It already optimizes adaptive experiments across projects, including contextual multi-fidelity bypasses, but does not fix architecture/data complementarity as its scientific intervention. FIX T02 (`fix_packets_v4/T02/packet.md`, previously inspected): WEAK, since data/optimizer retention interactions differ from structural architecture/data choice. C021 is a narrower opportunity within the research-controller family rather than an established STRONG duplicate.
## 7. Verdict
CUT. The ESTIMATED best-of-four breach is 0.15 and projection breach ESTIMATED 0.17. The disclosed joint reversal is too directly attacked by factorial and interaction-aware search to support a low saturation forecast without concrete proxy-failure evidence.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete experiment plans with final-training budget reserved). Grader noise UNMEASURED (planned: paired data/initialization seeds across all interaction cells). Score ladder UNMEASURED (planned: no edit, each isolated edit, direct joint run, search-selected pair and stronger mechanistic control).
## Screen record
id: C021
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.65
attack_single_range: 0.40-0.84
bo4_est: 0.75
pass4_est: 0.84
ub95_est: 0.92
gpuh_old: 14
gpuh_new_est: 480
duplicate_of: catalog-T03 MODERATE; FIX-T02 WEAK
kill_reason: disclosed complementarity invites direct joint and factorial search
souping_flag: no
