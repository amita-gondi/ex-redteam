# C056 — Search that learns executable query rewrites for codebases — saturation screen
## 1. What the grader actually rewards
The learned inspector supplies findings to a fixed downstream researcher, whose executed edits must improve real training or inference. Finding a symbol, naming a dispatch branch, or producing plausible explanatory text contributes no utility without a useful resulting change. R≈0 denotes the competent inspection floor, including the unchanged text-search policy, while R≈1 denotes the stronger attainable downstream ML result; all numeric forecasts here are ESTIMATED because this end-to-end ladder is UNMEASURED.

Learned selective inspection would nominally place the author reference at ESTIMATED R=0.60; downstream repair benefits supporting that placement are UNMEASURED.

## 2. Strongest lawful combined attack
Use static symbol and call-graph retrieval to propose candidate paths, then run small discriminating inputs under runtime hooks to identify the implementation actually selected. [RepoCoder](https://arxiv.org/abs/2303.12570) verifies iterative retrieval as an established repository method, while [SWE-agent](https://arxiv.org/abs/2405.15793) establishes the utility of an interface combining repository navigation with program execution. Neither paper establishes generated-kernel research competence; the relevant extrapolation is the combination of retrieval and executable feedback.

Collect inspection trajectories where a probe changes a repair hypothesis and the fixed agent subsequently achieves a validated improvement. Train the inspector on those actions and on misleading static matches, with an auxiliary objective predicting whether a proposed trace will distinguish competing dispatch explanations. Runtime evidence records input shape, dtype, compiled identity and observed launch path, rather than trusting generated filenames. Development search compares full tracing with selective tracing to price observation overhead.

ESTIMATED single-run R=0.48, range 0.28–0.65; ESTIMATED best-of-4=0.57; ESTIMATED pass@4 at R≥0.60=0.35; ESTIMATED upper-95% projection=0.71. They are desk scenarios above an independently frozen control, not measured tails. The residual is transfer of experiment choice: an unseen generator may require changing an input or cache condition before the causally relevant path appears, and collecting every trace can exhaust the repair budget. The inspector also has to communicate evidence that the fixed downstream agent can exploit. Those dependencies are more substantial than ordinary source-location recall, but the present interface does not quantify them.

## 3. Other routes
A tracing-capable coding agent with no inspector training has ESTIMATED R=0.42, range 0.22–0.61. It can recover common dispatch logic through hooks and minimal examples, and therefore belongs in the full combined floor rather than a text-only baseline.

A probe-search route enumerates legal shapes, dtypes, graph-cache states and specialization switches, clusters the resulting paths, and fine-tunes only on successful discriminators. ESTIMATED R=0.46, range 0.26–0.64. Blanket instrumentation is a lawful shortcut when its complete overhead fits the budget; the design must measure that control before claiming selective probing is necessary.

## 4. What would lower lawful saturation
Freeze an inspection API with charged trace volume and matched downstream repair budgets. Hold out independently different dispatch dependencies, not renamed generated functions, and require cases where a static answer and a default runtime trace support different repair hypotheses. Include an exhaustive-trace control and an ablation that shuffles inspector findings before the fixed agent acts. ESTIMATED attack after that specification is 0.41–0.53. ESTIMATED preparation: 12–20 person-days plus ESTIMATED 192 H100-h for training and repair checks. If unrestricted tracing already wins, increasing obfuscation would be a poor repair; the task should be cut.

## 5. Decisive-check GPU-h re-estimate
The card's ESTIMATED 14 GPU-h omits learned-policy data and end-to-end repairs. New ESTIMATED total is 192 H100-GPU-h. For an ESTIMATED 4B inspector, ESTIMATED 4 methods×3 seeds×6 H100-h per adaptation gives ESTIMATED 72; producing authorized executable trajectories with an ESTIMATED 8B teacher adds ESTIMATED 24. Executed downstream repairs on ESTIMATED 1B training or ESTIMATED 8B inference subjects use ESTIMATED 4×3×6=72, and fresh grading/trace-overhead controls add ESTIMATED 24. Arithmetic: ESTIMATED 72+24+72+24=192. This reduced pilot cannot establish large-scale kernel generalization, but it can falsify any gain over ordinary tracing.

## 6. Duplicate check
T20: MODERATE from its inspected packet; both improve a research-agent tool pipeline, but T20 freezes model behavior and submits harness workers rather than a trained inspection policy. T04: WEAK after reading its protocol-transfer source; trained tool use overlaps, yet unseen execution mechanisms and downstream ML repair replace equivalent interface schemas as the scientific target. No STRONG same-intervention match was established.

## 7. Verdict
CONDITIONAL. ESTIMATED best-of-4 is only 0.03 below the cutoff and the ESTIMATED projected bound is 0.04 below its line. Require the charged tracing interface, independent dispatch-mechanism holdouts and causal finding-shuffle ablation, together with demonstrated reserve over exhaustive tracing. Those are exact design requirements for retention, not a recommendation to launch work now.

## 8. Measurement status
Rollouts UNMEASURED (planned: inspector learning searches on fresh generated-code mechanisms); grader noise UNMEASURED (planned: fixed inspector findings through repeated downstream repair campaigns); score ladder UNMEASURED (planned: text retrieval, static analysis, blanket tracing, learned selective probes and attainable end-to-end repair).

## Screen record
id: C056
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.48
attack_single_range: 0.28-0.65
bo4_est: 0.57
pass4_est: 0.35
ub95_est: 0.71
gpuh_old: 14
gpuh_new_est: 192
duplicate_of: T20 MODERATE; T04 WEAK
kill_reason: trace-budget and held-out mechanism requirements unresolved near tail line
souping_flag: no
