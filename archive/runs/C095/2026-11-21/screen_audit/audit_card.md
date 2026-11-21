# C095 — Find an optimizer coordinate system beyond standard recipe sweeps — screen audit
## 1. What the screen claimed
The screen combined SOAP, blockwise Shampoo, low-rank curvature tracking, refresh scheduling and Muon parameter groups. Its forecasts were ESTIMATED single 0.49, best-of-four 0.59, pass@4 0.34 and upper-95% 0.74; the verdict was CONDITIONAL, with no kill category entered in the TSV, because resource-sensitive curvature tracking had not been specified. Its cited URLs were:
- https://arxiv.org/abs/2409.11321
- https://arxiv.org/abs/1802.09568
- https://github.com/pytorch/pytorch/blob/main/torch/optim/_muon.py

## 2. Evidence audit
SOAP does implement Adam in a preconditioner eigenbasis; Shampoo provides structured preconditioning; PyTorch supplies executable Muon code. None of these sources establishes that their combination tracks newly reused features within this card's unspecified persistent-state and complete-work limits. In particular, periodic basis recomputation and valid moment transport are different obligations, and an implementation's existence does not establish autonomous selection of their schedules.

Grade: PARTIAL. Coordinate-aware optimization is experimentally credible, but the decisive domain-transition residual and the conversion from loss to reward remain unsupported. The previous narrow upper-tail margin had no accompanying distribution.

## 3. Research done now
- *SOAP: Improving and Stabilizing Shampoo using Adam* — Nikhil Vyas et al., 2024, revised 2025 — https://arxiv.org/html/2409.11321v2 — fetched — Language-model experiments support coordinate adaptation and expose its space/time overhead; they strengthen the floor without demonstrating the reuse objective.
- *Shampoo: Preconditioned Stochastic Tensor Optimization* — Vineet Gupta et al., 2018 — https://arxiv.org/abs/1802.09568 — fetched — Tensor-factor preconditioners are established, but the paper does not settle transport through changing domain relationships.
- *Muon implementation* — PyTorch, 2026 snapshot, original file date unverified — https://github.com/pytorch/pytorch/blob/main/torch/optim/_muon.py — fetched — A practical alternative update is available; its repository presence supplies no matched-transition score.
- *OPTScientist: Multi-Agent Discovery of Typed Optimizer Programs for Transformer Pretraining* — Zhongzheng Li et al., 2026 — https://arxiv.org/html/2607.20486v1 — fetched — RS-MR improves a resource-conscious matrix optimizer, raising the credible public floor. Missing agent-backbone and campaign-runtime details prevent treating this as a budget-matched autonomous attack.
- *Session report: 0.9979 → 0.9697 in 126 experiments* — Claude agent posting in Andrej Karpathy's autoresearch repository, 2026 — https://github.com/karpathy/autoresearch/discussions/43 — fetched — A short empirical optimization loop is feasible; the reported search changes several training choices rather than isolating coordinate transport.
- *AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure* — METR, 2026 — https://metr.org/blog/2026-11-20-q4-2026-capability-update/ — fetched — Longer-budget training-speed work demonstrates useful agency while leaving an expert advantage and a substantial budget-transfer gap.

## 4. Re-estimated attack
All reward allocations and distributions below are ESTIMATED, conditional on subsequently freezing native loss anchors. They are not measurements of the subject learner. Assign 0.27 expected reward to legal matrix preconditioning, 0.12 to refresh/group selection and 0.07 to transition diagnostics and state handling: single 0.46. SOAP supports the first allocation most directly; the other two extrapolate from methods rather than a successful combined reuse experiment. No independent reward is awarded for cheaper implementation unless it enables additional legal learning.

Model three outcomes: probability 0.25 at R=0.29 when overhead dominates; 0.60 at 0.48 for a working conventional stack; 0.15 at 0.66 when transition handling transfers. Spread comes primarily from discovering a robust schedule and proxy ranking, with learner seeds folded into these scenario representatives; grader noise is unknown. The ESTIMATED single is 0.25×0.29+0.60×0.48+0.15×0.66=0.46, range 0.29–0.66. For independent attempts, E[max4]=0.29+0.19(1−0.25⁴)+0.18(1−0.85⁴)=0.57. Here p=0.15, so pass@4=1−0.85⁴=0.48; the single-distribution 95th percentile is 0.66. Compared with the screen, the mean and best-of-four decrease, but repeated-search success increases because the successful branch is explicit. This percentile is a desk projection, not an empirically fitted S4 confidence bound.

## 4A. Demonstrated capability and subfield SOTA
The strongest closely relevant result located is OPTScientist's RS-MR: published validation BPB 0.798375 versus Muon 0.802949 on its approximately 1.10B-parameter NanoChat comparison. These are source-reported measurements, not audit forecasts. It is a useful contemporary comparator, not verified universal optimizer SOTA. SOAP's separate pretraining result also belongs in the floor. Neither supplies a feasible same-budget domain-reuse ceiling; R≈1 therefore remains unanchored until a stronger transition control is executed.

Two agent results matter differently. OPTScientist's four-role typed-program scaffold discovers RS-MR and validates beyond proxy scale; backbone, accelerator allocation and elapsed search time are unreported in the fetched paper. That demonstrates optimizer discovery as reported, without demonstrating this attack in twelve hours. The Claude autoresearch self-report gives 126 trials over about 10.5 hours on one H100; exact model version is absent. Its validation improvement demonstrates fast recipe iteration, but changing architecture and training choices is broader permission than this optimizer-only submission receives.

KNOWN-RECIPE is established; AGENT-DEMONSTRATED integration under the present constraints is not. Set attack_basis=LITERATURE-ONLY. An agent must still identify drift, preserve useful state through rotations and validate final-domain loss rather than win a short pretraining proxy. METR's longer-budget evidence is a caution against automatically crediting that step.

The ANCHORED forecast uses probability 0.20 at 0.26 for failed budget adaptation, 0.65 at 0.45 for a sound imported optimizer and 0.15 at 0.67 for successful transport. ESTIMATED single=0.20×0.26+0.65×0.45+0.15×0.67=0.45, range 0.26–0.67; bo4=0.26+0.19(1−0.20⁴)+0.22(1−0.85⁴)=0.55; pass@4=1−0.85⁴=0.48; ub95=0.67. Scenario probabilities and reward transfer are assumptions; the headline verdict rests on them.

## 5. Verdict under the kill lines
The evidence re-estimate is CONDITIONAL; bo4 has ESTIMATED margin 0.03 and pass@4 only 0.02. The ANCHORED verdict is also CONDITIONAL, UNCHANGED from the screen: bo4 margin is approximately 0.05 and pass@4 remains close. Published optimizer discovery supports a serious attack, but no fetched result validates its entire resource-constrained transition behavior.

## 6. Redesign
Class (a): a known optimizer stack may consume the apparent novelty. REDESIGNABLE. Specify a same-capacity 1B learner, a public optimizer-state ledger, charged factorization FLOPs, and domain-reuse transitions whose old and new gradient subspaces overlap. Supply predictive dev transitions and current-domain probes. Permit all coordinate methods and bounded executable transport operators; compare against tuned SOAP, Shampoo, Muon and RS-MR before freezing reward anchors. Retain only regimes where a legal adaptive transport control demonstrates additional native loss reduction and meaningful attainable reserve. This is an empirical feasibility condition, not permission to manufacture difficulty by reducing compute.

The combined recipe of periodic factors, parameter-group assignment and refresh HPO must now preserve useful cross-domain history while deciding what to discard. A static rank/refresh choice can remain strong but cannot be presumed to solve conflicting reuse directions. Frontier training teams would value that state-efficient capability. The strongest redesigned attack adds probe-triggered moment transport to RS-MR/SOAP; its basis is LITERATURE-ONLY, and failure of the matched floor to plateau would invalidate the redesign.

ESTIMATED redesigned distribution: 0.25 at 0.25, 0.65 at 0.40, 0.10 at 0.61. Single=0.38; bo4=0.25+0.15(1−0.25⁴)+0.21(1−0.90⁴)=0.47; pass@4=1−0.90⁴=0.34; ub95=0.61. Residual risk is that a cheap existing transport rule generalizes immediately. A decisive pilot is ESTIMATED 5 arms×2 seeds×8 hours×2 H100 per 1B run=160 H100 GPU-h, plus 32 for probes and independent loss evaluation, total 192; longer stabilization would require recosting, not silent extrapolation.

## 7. Measurement status
Rollouts UNMEASURED (planned optimizer-only full-budget attempts on fresh domain transitions). Grader noise UNMEASURED (planned paired training seeds and repeated protected loss computation). Score ladder UNMEASURED (planned matched-resource public optimizers, adaptive transport reference and stronger feasible control).

## Audit record
id: C095
old_verdict: CONDITIONAL
evidence_grade: PARTIAL
sources_old_count: 3
sources_new_count: 3
sources_fetched_count: 6
old_single: 0.49
old_bo4: 0.59
old_pass4: 0.34
old_ub95: 0.74
new_single: 0.46
new_single_range: 0.29-0.66
new_bo4: 0.57
new_pass4: 0.48
new_ub95: 0.66
new_verdict: CONDITIONAL
binding_line: pass4>0.50
flip: none
kill_cause_class: a
redesign_status: REDESIGNABLE
redesign_oneline: Test observable overlapping domain transitions under explicit state and work limits against a complete coordinate-aware floor.
redesign_single: 0.38
redesign_bo4: 0.47
redesign_pass4: 0.34
redesign_ub95: 0.61
redesign_gpuh: 192
attack_basis: LITERATURE-ONLY
demonstrated_ref: OPTScientist, backbone unreported, 2026; autoresearch, Claude version unspecified, 2026
gap_to_attack: autonomous budget-matched moment transport across domain reuse
subfield_sota_ref: RS-MR native NanoChat comparison, Li et al., 2026
anchored_single: 0.45
anchored_bo4: 0.55
anchored_pass4: 0.48
anchored_ub95: 0.67
anchored_verdict: CONDITIONAL
anchored_binding_line: pass4>0.50
anchored_flip: none
verdict_rests_on_assumption: yes
redesign_attack_basis: LITERATURE-ONLY
souping_flag: no
