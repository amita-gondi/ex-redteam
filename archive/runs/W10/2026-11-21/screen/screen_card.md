# W10 — World models that survive their planner’s exploitation — saturation screen

## 1. What the grader actually rewards

The submitted dynamics/acquisition recipe is rebuilt on fresh worlds and consumed by an immutable CEM planner; independently replayed physical return, rather than prediction error or imagined success, determines utility. Under the ESTIMATED design constants, episode utility combines ESTIMATED 0.60 safe sustained-goal credit with ESTIMATED 0.40 time-averaged progress, and `R=clip01((U−0.10E_claim−0.05D_c−0.05D_q−0.30)/0.70)`. Thus R≈0 means utility below the designed floor, while R≈1 requires nearly immediate, sustained, safe attainment across the bank; the physical endpoint is not an established attainable ceiling. Empty/starter zeros are prescribed, idle native utility is expected near zero, and the competent floor, stratum baselines, reference and stronger controls are all UNMEASURED; their ESTIMATED proposed utilities are respectively 0.30, 0.30, 0.72 and 0.94. Goal/safety certification floors do not globally gate reward, and a minimal truthful ledger can eliminate claim deductions without contributing modeling insight.

## 2. Strongest lawful combined attack

Use structured identification with an uncertainty-aware residual model. [SINDYc](https://arxiv.org/abs/1605.06682) verifies the controlled-dynamics regression precedent; [SINDY-MPC](https://arxiv.org/abs/1711.05501) explicitly connects learned sparse laws to predictive control. [Ensemble-SINDy](https://arxiv.org/abs/2111.10992) supplies probabilistic identification and active-learning components. These establish applicable methods, not a solution to the unbuilt W10 worlds.

Fit observable actuator/valve memory and linear couplings first, then products, saturation splines and conditional residuals. The supplied equations expose low-order structure, and memory is observed. Use trusted ridge/spline fitting rather than importing coefficients; validate on blocked trajectories, then train bootstrap Gaussian residual heads with multistep consistency. [PETS](https://arxiv.org/abs/1805.12114) supports probabilistic ensemble propagation, and [MBRL-Lib](https://github.com/facebookresearch/mbrl-lib) supplies the inherited implementation precedent. Compare minimum uncertainty with calibrated uncertainty while preserving the fixed risk wrapper. None of this changes the planner.

Rank offered reachable probes by disagreement, feature leverage and training-goal relevance; mix joint pulses with boundary probes so marginally familiar actions do not leave joint support empty. [MAX](https://proceedings.mlr.press/v97/shyam19a.html) verifies forward-model disagreement exploration, although its unrestricted exploration machinery must be adapted to W10's offered-sequence interface. Fit every coefficient from authorized observations and export deferred hidden measurements plus receipt facts.

The attack has an ESTIMATED 24 H100-h solver allowance. Budget ESTIMATED 6 H100-h for structured/residual fits, ESTIMATED 7 H100-h for acquisition and public closed-loop checks, ESTIMATED 9 H100-h for the capped protected comparisons, and ESTIMATED 2 H100-h for reconstruction checks. Use inexpensive structured models and an ESTIMATED 0.25–1 million-parameter residual ensemble; no maximum-size network is needed. Public diagnostic selection precedes the two complete protected comparison cycles; the service cannot reliably compare an unlimited recipe list.

My clean native scenario assigns ESTIMATED U=0.88 to ordinary-support cells, ESTIMATED U=0.78 to boundary cells and ESTIMATED U=0.65 to delayed-coupling cells. Equal weighting yields ESTIMATED U=0.77 and ESTIMATED R≈0.67, with negligible slice deductions in that scenario. Forecasts: **ESTIMATED single-run R=0.67, range 0.38–0.86; ESTIMATED oracle best-of-four mean=0.78; ESTIMATED pass@4 at R≥0.60=0.88; ESTIMATED upper-95% scenario bound=0.94.** The last value is subjective upper-tail planning uncertainty, not a fitted confidence or scaling bound; repeated-search forecasts allow shared hard-world failures rather than assuming independent episode successes.

Residual losses come from reachable-probe restrictions, correlated errors around contact thresholds, noisy multistep fitting and finite-horizon CEM failure. Accordingly, I discount §10's ESTIMATED central R≈0.786 and reject treating its conditional ESTIMATED 0.714–0.914 range as a lower-bounded forecast. Nevertheless, broad excitation and direct fitting plausibly bypass the intended insight sequence. Like the required T02/T08/T18 FIX dossiers, this task needs the combined lawful method measured before security provisions can support any difficulty claim.

## 3. Other routes

- **Single standard recipe:** a faithful PETS ensemble, normalized delta targets and competent early stopping, retaining the common planner. ESTIMATED R=0.43, range 0.14–0.70; this can improve smooth regions but retain shared boundary extrapolation errors.
- **Search/sweep:** enumerate structured versus spline-residual models, regularization, probe mixtures and minimum/calibrated uncertainty on public worlds, then compare the finalists through complete protected cycles. ESTIMATED R=0.61, range 0.30–0.83. Cheap fitting enables substantial search, but the final protected budget permits only limited macro comparisons; noisy partial-cell winners may generalize poorly.
- **Lawful shortcut:** combine minimal reporting, minimum uncertainty and specialization toward easier cells. Under an ESTIMATED scenario solving ten strata at U=0.94 and leaving two at zero with finite execution, the formula gives ESTIMATED R≈0.679 after the quality deduction. Operational forecast: ESTIMATED R=0.59, range 0.28–0.80. Certification can fail while reward remains high; no private labels, unauthorized weights or fabricated receipts are required. Constant uncertainty removes action-dependent risk discrimination only when replacing a variable penalty; a constant penalty alone cancels.

## 4. What would lower lawful saturation

Replace the current low-order family templates prospectively with independently authored, observable switching-contact and flow-coupling compositions whose useful probes compete under the existing acquisition cap. Require an independently demonstrated same-data learned control to solve them, and retain structured regression as a challenger. ESTIMATED attack reduction: 0.12–0.22 R; ESTIMATED cost: 80–160 authoring hours plus 120–240 H100-h for paired feasibility/recipe pilots. This is a new distribution requiring new anchors, not evidence that the current candidate survives.

Rebalance native return toward balanced completion across declared mechanisms, using localized group aggregation rather than tiny linear deficits or a global zero. ESTIMATED specialization-score reduction: 0.08–0.15 R; ESTIMATED combined-attack reduction: 0.02–0.07 R; ESTIMATED cost: 24–48 authoring hours and 48–96 H100-h for score-ladder and control replays. Merely increasing the normalization floor conceals success without creating native reserve. Neither proposed change independently warrants PASS-SCREEN.

## 5. Decisive-check GPU-h re-estimate

W10 states no standalone cheapest decisive-check figure. The nearest envelope is §7, line 266: “300–700 GPU-h above, including actual histories and ≥2 recipe families×3 paired pilot seeds”; its separate complete-grade estimate is ESTIMATED 24 GPU-h (§7, line 250). Those are preparation/grade envelopes, not a priced minimal saturation experiment.

New **ESTIMATED decisive check: 192 H100-h**, conditional on implemented worlds and a verified interpreter. Freeze four combined-attack configurations plus PETS and the reference. Each artifact uses the proposed complete bank: ESTIMATED 24 world structures, ESTIMATED three learner seeds per world, ESTIMATED eight episodes per fit. With structured coefficients plus ESTIMATED 0.25–1 million residual parameters, reserve ESTIMATED 0.20 H100-h per fit including acquisition and ESTIMATED 0.0125 H100-h per control episode.

Arithmetic, entirely ESTIMATED: six grades × (72 fits × 0.20 + 576 episodes × 0.0125 + 0.80 warmup/reconstruction) = 134.4 H100-h; add 24 H100-h public selection/protected-dev work, 22.4 H100-h independent fresh-bank replay of the strongest artifact, and 11.2 H100-h profiling/fault reserve, totaling 192 H100-h. Minimal ledgers avoid optional snapshot replay. Seeds are already included. This can reveal a crossing and native-reserve collapse; it cannot certify repeated-search population bounds. Actual frontier-attempt tails and a scaling projection remain separate UNMEASURED studies. No experiment was launched.

## 6. Duplicate check

The following judgments use opened source contracts, not W10's own table:

- **v3:01B / 07B — MODERATE:** their source sections concern changing experience value and optimizer-resistant evidence judgments; neither learns physical transitions recursively consumed by fixed CEM.
- **FIX:T13 / catalog:T13 — WEAK:** both source packets learn perception/action grounding from passive video and a fixed bridge, whereas W10 receives numeric Markov observations and changes forward dynamics.
- **catalog:C-17.5 / C-17.6 — MODERATE:** the opened source suites learn longitudinal policies or select fixed policies under identified clinical simulators, sharing cheap-identification risk but differing in intervention and outcome authority.
- **D32 — WEAK:** its source fixes the complete robot learner and changes information purchases; W10 also changes the dynamics-learning method. D24 and D31 are weaker fixed-policy selection neighbors.
- **C106 — MODERATE:** its source trains the world model and planner evidence interface for independent-simulator completion; W10 freezes the interface, leaving a narrower model/acquisition intervention. **C086 — WEAK:** its world model predicts research gains, not physical transitions.
- **W13 — WEAK:** the candidate brief predicts signed neural-intervention effects and rankings, without recursive control; its revised task file was unavailable. No STRONG duplicate is established.

## 7. Verdict

**CUT.** Binding line: ESTIMATED oracle best-of-four mean 0.78 exceeds 0.60 by ESTIMATED 0.18; ESTIMATED pass@4 also exceeds its line by ESTIMATED 0.38. The ESTIMATED single-run point sits only ESTIMATED 0.03 below its kill line. The upper-tail scenario reinforces concern but is not claimed as an identifiable measured projection. The revision candidly repaired the critic's low forecasts and interface omissions; it left the decisive scientific objection unresolved: disclosed low-order dynamics, dense labels and trusted fitting may erase the research chain before sustained outer experimentation. No souping/merging dependency exists.

## 8. Measurement status

Rollouts **UNMEASURED** (planned: strongest lawful full-budget attempts on independent world blocks, preserving every artifact/failure). Grader noise **UNMEASURED** (planned: fixed-artifact repeat grades, fresh acquisition/fit seeds and cross-host boundary stability). Score ladder **UNMEASURED** (planned: idle, PETS, structured-only, full-stack, reference and stronger-control native/slice returns). Competent-recipe anchor **UNMEASURED** (planned: independent competent structured and neural composites on calibration banks before freezing the floor). All numeric forecasts and resource arithmetic above are **ESTIMATED**; no observed runs or invented empirical bounds are reported.

## Screen record
id: W10
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.67
attack_single_range: 0.38-0.86
bo4_est: 0.78
pass4_est: 0.88
ub95_est: 0.94
gpuh_task_stated: not stated
gpuh_new_est: 192
duplicate_of: v3:01B MODERATE; v3:07B MODERATE; catalog:C-17.5 MODERATE; catalog:C-17.6 MODERATE; C106 MODERATE
kill_reason: ESTIMATED combined identification and acquisition stack crosses best-of-four line
souping_flag: no
