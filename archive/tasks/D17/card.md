# D17 — Train reward aggregation for the learner it will actually teach

**Generator:** downstream-evaluator-usefulness recovery. **Stage × artifact:** eval/grading × reward. **Modality:** evaluator signals and policy learning.

## Problem

An inherited evaluator ensemble makes accurate static judgments yet supplies gradients that teach a policy to exploit shared errors. Submit a trainable aggregation/correction rule and train it through actual downstream learner outcomes, as required by [Suite 9.14](/workspace/task_suites_claude.md:12921). Individual evaluators and the downstream learner algorithm are separately pinned to isolate the aggregation treatment.

## Why known recipes plateau

Calibration, majority voting, disagreement filtering, robust aggregation and execution-checked reward are the complete baseline. The possible residual is optimizer-induced distribution change: aggregation changes exploration, which changes which correlated errors the learner encounters. Static accuracy need not predict this trajectory, but that mismatch remains unmeasured.

## Deterministic grader

Root rebuilds the aggregation component, trains independent learners using its rewards and measures exact private terminal competence. U is macro-averaged safe useful success across learner/optimizer/domain strata, with reward-model accuracy diagnostic only. All train/query costs count, and failed continuations retain their weight. F_D17 measures teaching usefulness, not ensemble consensus.

## Hidden-score design

Independently authored common-error mechanisms and learner optimizers form a declared shift, with protected dev optimizer/producer proxies. Match honest-artifact semantics and query costs. Independent attack algorithms must retain healthy feedback and complete their scheduled searches; candidate timeouts cannot create apparent robustness.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D17(U_checked_aggregation).** If executable checks cover the exploited dimensions, ordinary calibrated aggregation plus rejection of invalid outputs may attain reference learning. An outcome-only search over aggregation rules is also a legal no-diagnosis baseline. A constant low reward that suppresses learning cannot gain through reduced observed exploits alone.

## Saturation note vs 10T / 12h

The researcher can replace aggregation with a complete checked reward pipeline and optimize it against development learners. Reserve requires a measured chain from correlated-error diagnosis to altered exploration to improved independent learning. Index hard gates apply to the entire search process, including selection cost and ceiling-relative saturation.

## Cheapest decisive check

**ESTIMATED: 24 GPU-h** including matched downstream learner continuations and private-outcome evaluation. Cross static-equal-quality reward rules with optimizer choice; stop if static calibration or ordinary checked reward predicts and achieves all downstream gains.

## GDM Round 2 compliance and shape

Like pretraining_latest, actual learned capability is graded. R1 rejects stochastic LLM-invented repair tests; R2 requires all independently implemented honest positives to pass and prevents cleanup-only or attacker-starvation windfalls. The outer scorer is executable exact truth throughout.

## DISTINCTNESS NOTE

**Wrong parent: v3 07B. Nearest other: [T18](/workspace/task_catalog_v3_full/packets/T18.md).** Static evaluator decisions do not measure teaching effects. T18 changes learner objectives against a fixed reward service; D17 changes the reward aggregation while independently controlling the learner.

## Verdict

**promising** — A substantive downstream estimand with plausible learning feedback, pending complete checked-reward baselines and independent optimizer transport.
