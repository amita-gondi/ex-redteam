# C057 — Search across a corpus whose experiments have different resource contracts — saturation screen
## 1. What the grader actually rewards
The submitted artifact is an evidence corpus used by a fixed research agent; the chosen recipe is executed under the actual deployment envelope and judged on resulting ML utility. Unaffordable recipes lose their consumed work and cannot claim extrapolated quality. R≈0 represents the calibrated competent corpus/selection floor, including unchanged summaries; R≈1 reaches the stronger legal execution control, with every score and cost estimate below labeled collectively ESTIMATED because both anchors remain UNMEASURED.

A resource-conditioned evidence reference has nominal ESTIMATED R=0.60 placement, although no executed transfer result establishes that target.

## 2. Strongest lawful combined attack
Convert reports into typed records for model size, training tokens, precision, peak and persistent memory, setup compute, inference work and prerequisite assets. Preserve source provenance and missing-field uncertainty. A resource estimator rejects clearly impossible candidates; uncertain cases receive cheap feasibility probes before the fixed agent sees a recommendation. Present a deployment-specific Pareto frontier rather than a single normalized headline speedup, and provide a conservative executable variant for each retained method.

Use [BOHB](https://proceedings.mlr.press/v80/falkner18a.html) for staged recipe trials, combined with an explicit cost model informed by [multi-fidelity cost-aware Bayesian optimization](https://arxiv.org/abs/2211.02732). These sources verify established search ingredients, not the correctness of extrapolating between unrelated published experiments. The corpus includes the assumptions behind each adaptation and records actual low-budget measurements when the task legally supplies them. The agent then chooses among feasible candidates with resource uncertainty already exposed.

ESTIMATED single-run R=0.82, range 0.66–0.93; ESTIMATED oracle best-of-4=0.89; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED upper-95% projected score=0.98. Those are provisional stress forecasts for stronger curation than a frozen calibration recipe, not measured probabilities. The remaining loss is transfer error from a small probe to a full workload, especially undocumented preparation or nonlinear memory behavior. The current design does not explain why direct execution and conservative capacity estimates would fail often enough to preserve substantial native reserve.

## 3. Other routes
Structured extraction followed by conservative feasibility filtering is the strongest single recipe: ESTIMATED R=0.73, range 0.55–0.88. It directly corrects the inherited system's stated mistake and does not need to infer every resource dependency to avoid the most expensive failures.

A lawful search route ignores most narrative ranking and trials a short list of feasible methods with early stopping and matched resource metering. ESTIMATED R=0.78, range 0.59–0.91. When reports expose a finite candidate set, brute-force memory estimation and a small pilot for each may dominate elaborate corpus learning. Missing resource fields should be represented as uncertainty, not used as secret quiz answers.

## 4. What would lower lawful saturation
Require coupled resource changes that alter algorithm behavior after adaptation: for example, a feasible memory reduction changes the batch/noise regime and reverses the apparent training-quality order. Provide legal evidence and development transfers with the same phenomenon, then grade executed adaptation rather than completeness of extracted fields. ESTIMATED resulting attack R=0.52–0.68, still unsafe near the repeated-search cutoff. ESTIMATED authoring effort is 10–16 person-days, with ESTIMATED 240 H100-h for actual transfer pilots. Purely hiding more contract fields risks making the task an unidentifiable reporting exercise rather than ML research.

## 5. Decisive-check GPU-h re-estimate
Old figure: ESTIMATED 8 GPU-h. New ESTIMATED 240 H100-GPU-h uses ESTIMATED 1B learners, ESTIMATED 4 corpus/selection arms, ESTIMATED 3 private workload blocks with one paired recipe-training seed per block, and ESTIMATED 16 H100-h for the selected recipe and its charged feasibility probes: 4×3×16=192. Corpus ingestion and fixed-agent inference with an ESTIMATED 8B model add ESTIMATED 24; independent quality and memory verification add ESTIMATED 24. Thus ESTIMATED 192+24+24=240. This is reduced-scale execution, not billions-of-tokens pretraining. The original budget could catch an obvious memory mismatch but cannot compare learning quality under multiple genuine resource contracts.

## 6. Duplicate check
T14: WEAK, based on its reporting-policy packet; provenance and cost-sensitive assertions overlap but its trained reporting model is a different intervention. T03: MODERATE, since its inspected controller already performs cost-aware multi-fidelity experiment allocation, while this card submits curated evidence to a fixed agent. T20: MODERATE because evidence preparation and downstream recipe selection overlap, without this explicit resource-contract corpus artifact.

## 7. Verdict
CUT. ESTIMATED single-run reward exceeds its line by 0.12, and ESTIMATED best-of-4 exceeds its line by 0.29. The particularly high forecast follows from reward alignment: resource-aware extraction and cheap feasibility checks are almost exactly the missing capability described by the card, and no additional hard dependency is instantiated.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent evidence-curation attempts with full downstream recipe execution); grader noise UNMEASURED (planned: repeated selected-recipe runs and fixed-corpus agent replays); score ladder UNMEASURED (planned: headline summaries, typed contracts, conservative feasibility, pilot-validated curation and attainable transfer control).

## Screen record
id: C057
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.82
attack_single_range: 0.66-0.93
bo4_est: 0.89
pass4_est: 0.99
ub95_est: 0.98
gpuh_old: 8
gpuh_new_est: 240
duplicate_of: T14 WEAK; T03 MODERATE; T20 MODERATE
kill_reason: contract extraction and feasibility pilots directly solve the stated failure
souping_flag: no
