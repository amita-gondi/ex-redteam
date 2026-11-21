# C003 — Repair image-caption pair selection after OCR shortcut learning — saturation screen
## 1. What the grader actually rewards
Selection code is judged by spatial tuples produced by a retrained VLM on scenes whose printed text does not determine geometry. OCR and object recognition remain mandatory checks, so throwing away every text-rich image can reduce utility. ESTIMATED R≈0 is performance at the healthy selection floor and ESTIMATED R≈1 is the stronger attainable acquisition control; no-op is provisionally ESTIMATED R=0.00 and the intended reference ESTIMATED R=0.60, subject to missing anchor measurements.
## 2. Strongest lawful combined attack
The useful attack retains difficult text-bearing images while balancing their relation labels. Parse candidate captions into subject, relation and object; estimate which label is predictable from text alone; then select complementary image-caption records with matched words and different geometry. [Making the V in VQA Matter](https://arxiv.org/abs/1612.00837) verifies that complementary-image balancing is an established intervention against language priors. [Overcoming Language Priors with Self-supervised Learning](https://www.ijcai.org/proceedings/2020/151) verifies related balanced-data construction. Those results motivate the acquisition stack, not a claimed score on this card.

Combine relation-frequency balancing with candidate image embeddings, caption disagreement checks and quotas for examples where text is genuinely needed to identify an object. Use OCR-derived masks only in analysis to test sensitivity; the submission selects existing pairs and does not silently acquire permission to edit images or invent labels. A strong researcher can inspect the renderer family through public examples, recognize simple diagram relations and find a useful subset without solving unrestricted natural-image understanding. Short VLM continuations compare the full selector with blunt OCR rejection, with all selection and training work charged.

ESTIMATED single-run R=0.72, range 0.50–0.86; ESTIMATED best-of-4 mean=0.80; ESTIMATED pass@4 at R≥0.60=0.93; ESTIMATED upper-95% projection envelope=0.93. These estimates concern the uncalibrated current design. Geometry balancing should recover a large fraction of the gap between OCR-ranked data and the reference, while preserving a text-needed quota avoids the obvious retention penalty. Residual errors come from incorrect relation extraction and genuine ambiguity about which labels name which objects. The source specifies matched rendering families, making broad visual domain transfer an unavailable hardness argument.
## 3. Other routes
- OCR-confidence rejection plus uniform relation balancing is the strongest simple selector: ESTIMATED R=0.55, range 0.32–0.75. Its principal weakness is discarding useful textual grounding along with the shortcut.
- Enumerate OCR thresholds, text-only predictability cutoffs, relation quotas and ordinary-image fractions. Rank candidates on protected dev aggregates after low-fidelity continuation, then replay the winner fully. ESTIMATED R=0.66, range 0.44–0.83; selection uncertainty remains part of this forecast.
- Caption-template balancing without any visual parser could be a lawful shortcut if relation words identify the relevant training strata. ESTIMATED R=0.47, range 0.23–0.72. Crossed image/label controls must test this before treating visual analysis as necessary.
## 4. What would lower lawful saturation
Introduce relation-identification interactions in which printed text selects an entity and geometry supplies its relation, with counterbalanced distractors and shared caption vocabulary. Hold out authored role-binding compositions, rather than object names, while showing analogous interactions in dev. Require an equal-data selector to preserve OCR-dependent grounding across these compositions. Expected composite after that redesign is ESTIMATED R=0.46, range 0.25–0.67; simple complementary-pair quotas would no longer specify the complete answer. Cost: ESTIMATED a month of generator and annotation work plus ESTIMATED 240 H100 GPU-h for crossed selectors and retention checks. Increasing diagram variety without changing the binding problem would mostly add nuisance variation.
## 5. Decisive-check GPU-h re-estimate
Old estimate: ESTIMATED 10 GPU-h. Revised ESTIMATED 204 H100 GPU-h uses an ESTIMATED 3B-parameter VLM, ESTIMATED 4 selector arms, ESTIMATED 3 seeds per arm and ESTIMATED 15 H100-hours per continuation, plus ESTIMATED 24 GPU-h for relation/OCR/object evaluation and selection-feature extraction: ESTIMATED 4×3×15+24=204. The arms are inherited OCR ranking, blunt filtering, full balancing and independently selected reference. Training resolution and image count must be profiled before interpreting this allowance; it is a pilot envelope, not a throughput measurement. The original budget could test selectors on labels but is thin for learned multimodal retention.
## 6. Duplicate check
FIX T11 (`fix_packets_v4/T11/packet.md`, source opened): MODERATE. It shares counterfactual grounded visual outcomes, but permits objective/sampler interventions whereas C003's scientific artifact is pair-acquisition code. Catalog T11 belongs to that same lineage; novelty therefore rests on enforcing the selection-only interface, not renaming spatial reasoning as curation. No STRONG duplicate is asserted from matching outcome metrics alone.
## 7. Verdict
CUT, with ESTIMATED best-of-four margin 0.20 above the kill threshold. The single-run point also exceeds its line by ESTIMATED 0.02. Known complementary-data balancing plus retention-aware quotas appears sufficient to recover the disclosed failure without a new learning mechanism.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete lawful selectors under the task's training budget). Grader noise UNMEASURED (planned: retraining seeds and paired geometry edits). Score ladder UNMEASURED (planned: OCR ranking, text rejection, caption balancing, geometry balancing and stronger acquisition control with native tuple accuracies).
## Screen record
id: C003
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.72
attack_single_range: 0.50-0.86
bo4_est: 0.80
pass4_est: 0.93
ub95_est: 0.93
gpuh_old: 10
gpuh_new_est: 204
duplicate_of: FIX-T11 MODERATE; catalog-T11 MODERATE
kill_reason: complementary-pair selection already targets the OCR shortcut
souping_flag: no
