# W07 — Diffusion training for valid rare conditional modes — saturation screen

## 1. What the grader actually rewards

W07 rewards macro conditional 1−TV between generated images and an authored scene law after certified decoding into semantic alternatives and finite nuisance probes; failed or uncertified draws remain invalid mass. All numerical contract values, forecasts and resource allowances below are ESTIMATED; named kill thresholds identify the user's requirements, not measurements. The proposed formula is `R=clip((U-P_cov-P_reg-0.05*E_claim-0.42)/0.58)`, with local penalties rather than a multiplicative validity gate: ESTIMATED penalized utility V≤0.42 earns R≈0, while ESTIMATED V≈1 earns R≈1. An unchanged starter has a special zero branch, but its native utility, the competent-recipe floor, and the attainable neural ceiling are all UNMEASURED; the floor is designed, not calibrated. The intended reference reward is ESTIMATED 0.60, not an observed anchor, and a modestly imperfect learned renderer can exceed it because the finite channel does not establish complete image-distribution fidelity.

## 2. Strongest lawful combined attack

Fit the latent scene distribution directly, then generate its images inside the permitted tensor interface. The released bank contains ESTIMATED roughly one million images, visible conditioning descriptors, a small semantic alphabet and low-dimensional nuisance variation. Training rarity is therefore mainly an exposure problem; it does not establish that the conditional law is hard to identify.

First infer object masks, visible attachment/containment choices and nuisance coordinates from legal images, sharing shape estimates across conditions. [Differentiable vector rasterization](https://people.csail.mit.edu/tzumao/diffvg/) and its [diffvg implementation](https://github.com/BachiLi/diffvg/) establish a standard fitting route from raster supervision; they do not demonstrate W07 reconstruction accuracy. Next fit semantic probabilities by conditional likelihood and nuisance densities using a [mixture density network](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bishop-ncrg-94-004.pdf), with held-out training compositions selecting complexity. Balance condition exposure while preserving each condition's internal alternative probabilities. Do not flatten the semantic distribution or treat inferred labels as private truth.

Compile the fitted sampler and image synthesis into admitted arithmetic, matrix and convolution operations, or distill their outputs into an ESTIMATED 16–32M-parameter conditional image decoder. Use the supplied Gaussian input as randomness and count every evaluation; neither diffvg custom operators nor cross-image state enter deployment. In parallel, continue the inherited ESTIMATED 64M denoiser using the [improved-DDPM implementation](https://github.com/openai/improved-diffusion) with compatible [Min-SNR weighting](https://arxiv.org/abs/2303.09556). Select one complete artifact using the lawful protected calls, and transcribe reporting receipts automatically. A plausible allocation is ESTIMATED 8 H100-h geometry fitting + 4 density fitting + 24 renderer fitting + 24 diffusion fallback + 12 evaluation + 8 export/audit = 80 H100-h, within the task's ESTIMATED 96-H100-h cap and 12-hour schedule through overlapping independent branches.

My ESTIMATED single-run R is **0.80**, scenario range **0.40–0.94**; ESTIMATED oracle best-of-four mean is **0.88**, ESTIMATED pass@4 at R≥0.60 is **0.90**, and ESTIMATED upper-95% planning bound is **0.97**. These are subjective desk forecasts, not measured frequencies or a fitted scaling interval. The pass estimate allows substantial shared instance difficulty; independent attempts with ESTIMATED success probability 0.50 would instead give ESTIMATED pass@4≈0.94.

The central score requires ESTIMATED corrected V≈0.884. For example, ESTIMATED U≈0.89 with small local penalties suffices, leaving room for decoding failures, conditional-law error and empirical histogram loss. Residual difficulty is unseen contour reconstruction, strict global certification and composition transfer; complete fitting failure can still yield ESTIMATED R=0. The revision's §10 gives ESTIMATED central R=0.84 and range 0.75–0.93. I retain its attack mechanism but lower the point and substantially widen the downside: the geometry equations, working inverse and graph realization are missing. Nothing establishes its narrow successful-renderer band as likely.

## 3. Other routes

- **Single standard recipe:** Native conditional [EDM](https://arxiv.org/abs/2206.00364), with faithful preconditioning/loss, balanced conditions and an integrator respecting the evaluation cap: ESTIMATED R=0.57, range 0.25–0.79. This is a separate compatible stack, not an indiscriminate extra loss on the inherited variance head. Pixel-level certification may remain its main bottleneck.
- **Search route:** [Hyperband-style allocation](https://jmlr.org/papers/v18/16-558.html) over conditioning width, noise weighting, learning rate and guidance schedule: ESTIMATED R=0.68, range 0.35–0.88. Train ESTIMATED eight short branches, promote two, and reserve the limited protected calls for finalists; public loss alone is unsuitable. [Classifier-free guidance](https://arxiv.org/abs/2207.12598) supplies a known fidelity/diversity tradeoff, with both branches charged.
- **Lawful-looking shortcut:** Learn a dense bank of nuisance prototypes and their probabilities, optimized against the disclosed probe distribution rather than exact hidden keys: ESTIMATED R=0.73, range 0.37–0.91. Fresh conditions prevent literal training-image lookup, but a fitted conditional bank can match finite feature expectations while omitting continuous detail. Honest ledger automation removes reporting loss; it cannot itself create image fidelity. The revision fixes optional-record dilution, so that obsolete exploit receives no assumed benefit.

## 4. What would lower lawful saturation

The fixed probe channel needs an independently qualified resolution contract, fresh multiscale spatial features and observed-pixel relation checks. ESTIMATED reduction to the finite-bank shortcut is 0.08–0.18 R, but only ESTIMATED 0.02–0.06 against a genuinely fitted continuous renderer. Cost: ESTIMATED 3–5 researcher-weeks, 64–128 H100-h for qualification, and greater CPU decoding work.

A substantive redesign would replace the compact coefficient/polygon construction with independently authored mechanisms whose conditional support cannot be captured by the same small sufficient statistic, while retaining observable training evidence. ESTIMATED attack reduction is 0.15–0.30 R; cost is ESTIMATED 6–10 researcher-weeks and 768–2,304 H100-h for new histories and controls. This could also damage learnability, so it requires fresh review rather than conditional acceptance here. More images, secret seeds, a higher normalization floor or excluding a correct renderer provide no defensible reduction. The central attack leaves only ESTIMATED 0.11 native utility to mathematical perfection, already too little for the requested broad reserve.

## 5. Decisive-check GPU-h re-estimate

The task names no dedicated cheapest experiment. Its §7, line 249, states: “S2/S6 tail pilot | 2,688 | Three fresh blocks×eight attempts×112”; this is an ESTIMATED full tail pilot, excluding asset preparation.

For an earlier single-run kill check, use one frozen semantic instance containing both scene families, three independent seeds for each of two arms: the density/renderer stack and an executable ESTIMATED 64M diffusion reference. The renderer uses ESTIMATED 16–32M parameters; every arm receives the same ESTIMATED 96-H100-h maximum, including its searches and proxy calls. ESTIMATED arithmetic: training/search `2×3×8 H100×12h=576 H100-h`; six full grades `6×16 H100×1h=96`; three starter grades plus three repeated frozen-artifact grades `6×16×1h=96`; execution subtotal **768 H100-h**. Each grade includes claim replay and decoder controls.

Because the source supplies specifications rather than built assets, add ESTIMATED 768 H100-h for one instance's warm start/history construction and ESTIMATED 48 H100-h for truth-bank qualification: **ESTIMATED 1,584 H100-h total**. Decoder implementation and CPU qualification precede this hypothetical check. Stop on a valid attack above the single-run line; failure to cross is HOLD, not evidence about population best-of-four or stronger-tier scaling. No experiment is launched.

## 6. Duplicate check

The following comparisons were checked in original source files, beyond W07's dedupe assertions:

- **v3 01A — WEAK:** Its corpus/stage mixture intervention targets downstream acquisition and retention, rather than emitted image-law fidelity.
- **FIX T11 — WEAK:** Counterfactual visual training improves a question-answering actor; W07 submits an image generator.
- **D18 — WEAK:** It constructs reachable training support for a fixed learner and grades subsequent goal success, rather than sampling the target distribution directly.
- **Catalog T22 — MODERATE:** Both grade conditional generated distributions through finite representations, but T22 fixes the training objective and varies teacher-information acquisition.
- **Catalog T23 and T12 — MODERATE:** Instrumented generation and inverse graphics expose similar synthesis shortcuts; their graders target specified trajectories and individual-image reconstruction respectively.
- **Catalog C-17.1 / suite 17.1 — MODERATE:** Conditional-law fitting and distributional agreement closely resemble W07's closure risk, but next-user-action prediction lacks the image-rendering intervention.
- **Creative C096 — WEAK:** Its image bottleneck must preserve falsifying marks for downstream reasoning, a different artifact and grader target; C006's set-valued recipe prediction is NONE.
- **Sibling W05 — WEAK:** Discrete refinement targets whole-program execution, rather than continuous nuisance frequencies.

No STRONG duplicate is established.

## 7. Verdict

**CUT.** Binding line: single>0.70, exceeded by ESTIMATED 0.10 at the central attack. ESTIMATED best-of-four also exceeds its line by 0.28 and pass@4 by 0.40. The upper-95% entry is only a planning forecast, not an empirical S4 result. The revision repairs finite-distribution wording and reporting dilution, but leaves the critique's decisive compact-law renderer, unqualified inverse and absent native anchors unresolved. No souping/merging dependency is present.

## 8. Measurement status

Rollouts **UNMEASURED** (planned: independent researcher attempts after the scripted kill check). Grader noise **UNMEASURED** (planned: repeated frozen artifacts across committed draw banks and hosts). Score ladder **UNMEASURED** (planned: starter, balanced diffusion, finite-bank sampler, fitted renderer and reference, retaining raw U and invalid mass). Competent-recipe anchor **UNMEASURED** (planned: full-budget compatible diffusion and density/rendering controls on independent compositions, without changing the floor after inspection).

All numerical Screen record fields below are ESTIMATED.

## Screen record
id: W07
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.80
attack_single_range: 0.40-0.94
bo4_est: 0.88
pass4_est: 0.90
ub95_est: 0.97
gpuh_task_stated: 2688
gpuh_new_est: 1584
duplicate_of: v3:01A WEAK; FIX:T11 WEAK; D18 WEAK; catalog:T22 MODERATE; catalog:T23 MODERATE; catalog:T12 MODERATE; catalog:C-17.1 MODERATE; C096 WEAK; C006 NONE; W05 WEAK
kill_reason: compact conditional-law fitting plus legal tensor renderer exceeds single-run line
souping_flag: no
