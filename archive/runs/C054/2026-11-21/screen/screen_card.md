# C054 — Search through figures whose causal labels must be read — saturation screen
## 1. What the grader actually rewards
The grader checks whether the retrieved curve really belongs to the named treatment, whether extracted values match its private rendering table, and whether the resulting intervention answer and recipe choice are correct. R≈0 is the committed competent extraction-and-search floor, with the inherited caption-led pipeline contributing no gain; R≈1 reaches an attainable figure-grounded decision control. All numerical reasoning below is ESTIMATED because tolerances, role weights and native floor/control values remain UNMEASURED.

The trace-grounded reference pipeline is provisionally targeted at ESTIMATED R=0.60, without a demonstrated correspondence or recipe-utility score.

## 2. Strongest lawful combined attack
Retrieve page images as well as text using [ColPali](https://arxiv.org/abs/2407.01449), then isolate the relevant panel, legend and axis labels. Apply a plot-to-table model such as [DePlot](https://aclanthology.org/2023.findings-acl.660/), but do not trust its treatment names without a separate visual join. Build that join from legend swatch color, line style, marker shape, panel coordinates and surrounding report context. A fixed VLM checks each proposed correspondence on a magnified crop; disagreement triggers another crop or conservative re-extraction, within the common token budget.

Reconstruct an explicit table keyed by panel, series appearance and treatment identity before doing arithmetic. Validate curve ordering and interventions against nearby tables when available. Development search varies crop resolution, independent checking depth and the threshold for escalating ambiguous legends. This is a competent chart-analysis pipeline, not a claim that either cited system alone solves causal attribution.

ESTIMATED single-run R=0.72, range 0.53–0.86; ESTIMATED oracle best-of-4=0.81; ESTIMATED pass@4 at R≥0.60=0.93; ESTIMATED upper-95% projection=0.94. The forecast assumes most figures preserve readable redundant visual cues. Cross-panel identity switches, overlapping traces and context-dependent treatment semantics leave a residual, but the card does not establish that such cases consume most attainable utility. These values describe a search-strengthened transfer attack above a frozen floor; including the identical pipeline in that floor would make its calibration reward zero and require measuring a new reserve.

## 3. Other routes
DePlot followed by typed numerical reasoning, without an independent visual correspondence check, has ESTIMATED R=0.56, range 0.35–0.74. Its mistakes should concentrate on the exact curve-identity reversals the card proposes, making it a useful single-recipe baseline rather than the whole saturation attack.

A search route samples alternative panel crops and series-to-legend assignments, rejects assignments inconsistent with visible markers or text, and selects using legal development accuracy. ESTIMATED R=0.68, range 0.47–0.83. Parsing a public source table is also lawful when the report intentionally supplies one; the hidden renderer table must remain inaccessible, and visible equivalent evidence must still earn credit.

## 4. What would lower lawful saturation
Split by independently authored visual correspondence grammar, rather than recoloring familiar plots. Include multi-panel intervention relations whose visible legend conventions require joint interpretation, and score the scientific decision after controlled treatment-label swaps. The fixed VLM must still have enough resolution and context to solve them; visual illegibility is not research headroom. ESTIMATED revised combined R=0.47–0.61, costing ESTIMATED 8–14 author-days and ESTIMATED 40 H100-h for parser and decision validation. A counterfactual rendering pilot should first establish that the reference actually follows the changed correspondence.

## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 6 GPU-h. New ESTIMATED 40 H100-GPU-h assumes an ESTIMATED 3B document retriever/parser and an ESTIMATED 7B VLM answerer, ESTIMATED 4 arms, ESTIMATED 3 independent renderer families with one generation seed per family, and ESTIMATED 2.5 H100-h per complete arm/family pass: 4×3×2.5=30. Image indexing, disjoint crop warmup and repeated scoring add ESTIMATED 10, yielding ESTIMATED 30+10=40. No parser pretraining is included. If deployment requires newly training the visual parser, this envelope is insufficient and must be repriced before experimentation; the narrow pilot relies on existing model weights.

## 6. Duplicate check
T19: WEAK after reading its visual-temporal evaluator packet; evidence composition overlaps, but it learns a selection evaluator rather than a research figure-extraction tool. T11: MODERATE from its source, because visual counterfactual correspondence is central to both; this card changes the research retrieval/extraction pipeline instead of the VLM learning objective. The interventions therefore differ even when some diagnostic examples could be shared.

## 7. Verdict
CUT. ESTIMATED best-of-4 exceeds the binding threshold by 0.21, and ESTIMATED single-run reward exceeds its line by 0.02. Mature retrieval, chart transcription, explicit legend matching and selective visual checking can be composed lawfully; hidden color permutations alone do not defeat that combination.

## 8. Measurement status
Rollouts UNMEASURED (planned: full tool-pipeline searches across unseen figure grammars); grader noise UNMEASURED (planned: repeated extraction and answer passes on fixed rendered inputs); score ladder UNMEASURED (planned: captions, plot transcription, visual matching, independent checking and attainable causal correspondence control).

## Screen record
id: C054
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.72
attack_single_range: 0.53-0.86
bo4_est: 0.81
pass4_est: 0.93
ub95_est: 0.94
gpuh_old: 6
gpuh_new_est: 40
duplicate_of: T19 WEAK; T11 MODERATE
kill_reason: explicit visual correspondence stack likely closes ordinary plot errors
souping_flag: no
