# C084: Approximate speculation with a real downstream regret contract — independent adversarial review

**Verdict: FIX.** Measuring executed program utility is a sound replacement for assuming local logit regret implies safety. However, optimized exact speculation and conservative adaptive fallback are strong lawful alternatives, and the quality-cost exchange rate is absent. Retain only a version whose semantic risk allocation has native benefit beyond that complete frontier on fresh executable tasks.

Source file: `/workspace/task_ideation_v4_creative/cards/C084.md`.

The review uses CPU reasoning and web reading only. Serving measurements, rollout scores, grader noise, observed runs and pass@k observed are **UNMEASURED**; they require paired same-work generation, execution and timing of frozen decoders. Reward estimates assume a monotone useful-utility/time contract, not a formula known to exist. The card supplies no target/draft model pins, generated-program schema or benchmark implementation.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Exact speculative escape | Use strict verifier acceptance with a tuned draft and block length; preserve target semantics while gaining parallel verification speed. Spend no approximation budget at all. | ESTIMATED 0.60–0.86 | Exact decoding is explicitly legitimate; the card does not establish the optimized exact frontier. | Compare optimized exact speculation, plain target and approximate variants with identical cache, batch and hardware treatment. | ESTIMATED 0.60–0.86 | If exact speculation dominates utility/time, approximate regret allocation has no remaining purpose. |
| Conservative syntax gates | Turn approximation off around control flow, literals, identifiers, tool names and arguments; adapt block length to acceptance elsewhere using legal prefix features. | ESTIMATED 0.57–0.83 | No; it matches the proposed branch-aware role and needs no private semantic labels. | Include parser-conditioned and uncertainty-conditioned fallback in the complete recipe; use semantics-changing twins with matched syntax. | ESTIMATED 0.57–0.83 | A large share of harmless tokens may provide adequate speed without solving difficult sensitivity prediction. |
| Utility-per-second denominator collapse | Emit tiny programs that return a common answer, terminate generation early or abstain on costly tool choices; maximize a ratio with nearly empty work. | ESTIMATED 0.65–0.97 | Actual execution helps only if noncompletion and quality costs are fully defined. | Fixed offered tasks and deadline; disclose utility and quality floors, charge unfinished work and test no-output/constant-program controls. | ESTIMATED 0.10–0.43 | A lawful short solution deserves speed credit, so length itself cannot be used as an invalidity rule. |
| Filesystem/mount/proc/IPC/frozen-asset access | Inspect private program tests through tool subprocess handles; modify target logits, draft weights, reference outputs or the serving timer through shared mounts and caches. | ESTIMATED 0.89–1.00 | Execution is required, but model/evaluator isolation is unstated. | Separate decoder workers from test truth and timing authority; immutable target/draft assets, private IPC and descriptor tests in proposed `test_speculation_boundary`. | ESTIMATED 0.00 | A tool sandbox can become a confused deputy for the private evaluator. |
| Interface or encoded-state smuggling | Place hidden solutions in draft adapters, acceptance tables or compressed decoder configuration; decode a program lookup instead of using metered model calls. | ESTIMATED 0.84–1.00 | There is no permitted-state or offline-training lineage contract. | Freeze allowed assets; authenticate any legal adaptation; bound code/config payloads and provenance of final token streams. | ESTIMATED 0.00 | Legitimate grammar-constrained decoding and small syntax tables remain lawful methods. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Print fake tool success or timing JSON, skip executing approximate outputs, or pass public canonical programs by hash and mark other tests unavailable. | ESTIMATED 0.86–1.00 | The card explicitly rejects certification from a separate exact trace, but result authority is undefined. | Parent executes every actual generated artifact on independent tests; require equivalent positive programs and keep failed tools in denominator. | ESTIMATED 0.00 | Execution tests can still miss a semantic branch unless their truth bank is independently complete. |
| Timing/check-decoupling/branch laundering | Time draft acceptance only, run correction after stopping the clock, use exact text for correctness and approximate text for speed, or reuse an uncharged target cache. | ESTIMATED 0.78–1.00 | Same-output execution is intended without an operational capture protocol. | Receipt prompt, generated bytes, target calls, cache lineage and downstream execution; synchronize all device work before timing ends. | ESTIMATED 0.00 | Host/JIT asymmetry can create apparent gains despite honest token receipts. |
| Dev-hidden leakage/cue inference | Infer branch danger from protected-only prompt styles, recognizable public programs or tool ordering; memorize which task families tolerate approximate tokens. | ESTIMATED 0.56–0.88 | Fresh programs and matched sensitivity are promised, with no construction independence. | Split program semantics/provenance, cross surface form and risk labels, and test style-only and syntax-only sensitivity predictors. | ESTIMATED 0.21–0.53 | True semantic prefix signals are allowed; if they universally solve allocation, that is a difficulty failure. |
| Adaptive aggregate oracle | Sweep regret budgets and token-class gates, use scalar utility/time responses to infer hidden task costs and coordinate queries across decoder branches. | ESTIMATED 0.59–0.84 | No query precision, refresh or shared-budget policy exists. | Global scored-query ledger and fresh dev blocks; include the fully adaptive legal selector when measuring the baseline. | ESTIMATED 0.34–0.66 | Useful tradeoff tuning can remain strong after all illicit quota bypasses are blocked. |
| Slice abandonment/denominator optimization | Prefer easy program synthesis, avoid high-impact tool choices and let failed executions disappear from speed averages. | ESTIMATED 0.62–0.92 | No fixed program/tool stratum weights or tail quality requirement is stated. | Fixed task/seed counts, macro quality and latency reporting, numeric minimum utility and deliberate branch-sensitive specialist controls. | ESTIMATED 0.22–0.55 | Average utility can conceal severe rare branch errors even with fixed denominators. |
| Strongest lawful combined recipe | Select between strict speculation and ASD; jointly tune block size and acceptance from runtime statistics, use syntax/uncertainty fallback, and optimize the disclosed utility/time tradeoff through legal dev feedback. | ESTIMATED 0.71 (ESTIMATED 0.46–0.91) | It uses exactly the permitted inference trajectory choices. | Establish the complete same-hardware quality-latency frontier before crediting semantic regret prediction. | ESTIMATED 0.71 (ESTIMATED 0.46–0.91) | Known adaptive selection may achieve the reference without any novel causal predictor. |

## Published recipe shortcut — web checked

- [Approximate Speculative Decoding](https://arxiv.org/abs/2608.03447): the primary page describes an approximate verifier with a regret budget and a zero-budget strict-verification limit.
- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192): the checked primary abstract establishes exact speculative generation without retraining as a strong alternative family.
- [Speculative Decoding with Big Little Decoder](https://arxiv.org/abs/2302.07863): primary material supplies an established adaptive small/large-decoder route rather than a fixed approximation-only baseline.

I opened the primary abstract pages and read their returned descriptions; no decoder implementation, checkpoint compatibility or paper performance result was reproduced. None of their speed figures is transferred here. Parser-aware semantic fallback is my proposed adversarial engineering addition, not an attributed theorem from these sources. The strongest complete recipe remains **ESTIMATED 0.71 (ESTIMATED 0.46–0.91)** after security repairs.

Strict verification is especially important because the source comparison can otherwise be artificially weak. Plain target decoding does not exhaust exact methods. Conversely, exact distributional verification does not guarantee a program is correct; task utility still needs execution. Both distinctions must survive into the grader and its reference controls.

## Saturation against the hypothetical 10T researcher / 12h

The target researcher can recover the intended inference algorithm from the paper, profile draft/target costs and run a budgeted search over regret thresholds and block lengths. It can infer obvious sensitivity classes from syntax, use exact fallback near decisions and approximate only contexts with demonstrable slack. That complete route need not solve all semantic risk prediction to obtain most profitable speed.

Conditional forecasts: **ESTIMATED single-run maximum 0.85**, compared with the user's >0.70 cutoff; **ESTIMATED oracle best-of-4 mean 0.80**, compared with >0.60; **ESTIMATED pass@4 0.88**, compared with >0.50 at R≥0.60; **ESTIMATED projected upper-95% 0.96**, compared with ≥0.75. All are likely breaches for the present underdefined reward. These are not fitted bounds or observed events. The lower recipe scenario allows for a harder distribution where semantically sensitive errors are hard to recognize and conservative fallback loses much of the speed opportunity.

S1 requires demonstrated attainable utility/time reserve beyond a mid-range reference under the identical serving contract. That evidence is absent. S7 additionally needs an achievable physical frontier incorporating target-call cost, verification batching, mandatory tool execution and irreducible task uncertainty. A logit-regret bound cannot stand in for that ceiling. Both statuses are OPEN; no numerical ceiling-relative test can be performed from the card.

The projected upper bound must eventually come from separate researcher-budget and concurrency sweeps, with subject serving hardware fixed. Current-model passivity is irrelevant: assume the hypothetical solver can maintain a Pareto frontier, retest conclusions and spend its entire budget. All tail and noise fields are UNMEASURED; the measurement plan uses independent program families, fresh-container repeat timing, full-budget restarts and a distinction between oracle and lawful dev selection. Boundary-overlapping intervals remain HOLD.

## Revised estimate versus the source card

The designer's **ESTIMATED 0.50** assumes branch-aware regret conservation cannot always predict later semantic damage. That limitation is real but insufficient: the adversary may decline approximation in broad uncertain regions and win through strict speculation plus cheap safe regions. My **ESTIMATED 0.71 (ESTIMATED 0.46–0.91)** gives those alternatives proper weight. I am not claiming that syntax predicts all downstream effects or that exact decoding is always faster.

This is more threatening than the moderate complete-recipe examples in the calibration packets because exactness is a permitted escape and the quality-cost exchange rate is unspecified. A very generous latency weight makes ordinary speculation strong; a strict quality weight can make the exact route optimal. A credible residual needs a calibrated region between those cases, demonstrated without removing either lawful method.

## Boilerplate and missing build content

General framing occupies **ESTIMATED 25–35%** of the card; the remaining **ESTIMATED 65–75%** concerns approximation, branch sensitivity and actual execution. It is not mostly boilerplate. Missing build content nevertheless includes models and precision, speculation implementation, permitted draft changes, KV-cache semantics, workload concurrency, generation limits, executable tool environment and the exact outcome-to-reward formula.

The phrase “same quality budget” needs an explicit utility functional, not only a local predictor. Are wrong tool calls reversible? Does malformed code lose only its item? Is execution time charged alongside serving? How are retry, abstention and deadline failures aggregated? These are specification gaps to resolve, not questions requiring this reviewer to invent favorable answers. An independent bank must include semantically equivalent programs with different syntax and near-identical syntax with different consequences, while preserving public evidence sufficiency.

## Duplicate check

No duplicate is established among the checked materials. The inspected v3 05A heading and opening problem concern exact serving capacity, whereas C084 explicitly optimizes an approximate acceptance trajectory against downstream outcomes. The T21 source packet was not opened, so its relation remains unverified and no URL or duplicate id is asserted from the card's nearest-task claim. Structural exemplars were not used as evidence of distinctness.

## Verdict, required fixes and cheapest decisive check

**FIX** through a bounded serving/utility contract:

1. Define exact utility, quality floors, deadlines, final output capture and all charged work; exclude empty-task and ratio windfalls through executed controls.
2. Build optimized strict speculation and complete adaptive approximate/exact selection before the reference. Keep every legal fallback available.
3. Construct independent executable branch families with matched surface cues and observable semantic context; prove that local-regret mismatch is a real task phenomenon rather than a private-label artifact.
4. Show a native quality-latency region where the proposed semantic policy beats the whole known frontier, with attainable further reserve and stable repeat grades.

Cheapest useful evaluation needs no training: use a proposed already-supplied target/draft pair and replay matched private executable tasks under strict, published approximate and conservative adaptive decoding. Allow **ESTIMATED 0.55 H100-hours per method**, plus **ESTIMATED 0.45 H100-hours** for shared warmup and repeat timing, totaling **ESTIMATED 2.1 H100-hours**. This assumes a modest model pair that fits the card's eventual hardware; it excludes model acquisition and is a falsification pilot, not certification. Nothing was launched.

Required R2 checks include model/cache immutability, trace-to-executed-program binding, verdict spoofing, worker deletion, independent equivalent positive programs, encoded solution tables and timing/cache swaps. Delivery still needs portable isolated startup, trusted linkage, no secrets/egress, global feedback limits, fixed failed-seed accounting and a private fully reconciled archive. Successful sandbox tests would leave the lawful recipe estimate unchanged.

## Verdict record
id: C084
source_group: creative_v4
verdict: FIX
strongest_attack: ESTIMATED 0.71 (0.46–0.91)
combined_recipe_attack: ESTIMATED 0.71 (0.46–0.91)
best_of_4: ESTIMATED 0.80
pass_at_4: ESTIMATED 0.88
single_run_max: ESTIMATED 0.85
upper95_projected: ESTIMATED 0.96
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 2.1
required_fixes: exact speculation frontier; fixed executable utility and cost; semantic twin families; same-stream timing and execution
main_kill_reason: exact and conservative adaptive speculation threaten the whole gain
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
