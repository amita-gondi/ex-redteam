# W06 — Neural audio coding that retains quiet events — saturation screen

## 1. What the grader actually rewards

W06 pays for dominant-waveform fidelity F and counterfactual response fidelity T: the decoded event-present minus decoded event-absent waveform must approximate the entire added event, including silence outside its support. The proposed formula is R=clip((U−P−0.10E−0.50)/0.50), with U=(F+T)/2; these coefficients, the ESTIMATED 0.50 floor, and the slice-deficit constants are designed and UNMEASURED. With no deductions, R=max(0,F+T−1), so matching the bed while discarding the event earns approximately zero, and perfect waveform reconstruction plus perfect response approaches one. The unchanged codec's required zero, the competent-recipe plateau and all reference/ceiling values remain UNMEASURED; the floor has an algebraic interpretation but no demonstrated baseline calibration. This is an additive reward with localized deficits, not a hard all-strata gate: baseline-relative coverage blocks certification separately, and a good average can still earn substantial reward with weak quiet-natural slices.

## 2. Strongest lawful combined attack

Use a single hybrid codec: a source predictor/parametric front end for structured beds and transients, followed by a trained residual channel. [Matching pursuit](https://www.di.ens.fr/~mallat/papiers/MallatPursuit93.pdf) supplies an established dictionary-fitting method; fit legal training atoms and continuous onset, phase and decay parameters rather than guessing a hidden source ID. [EnCodec](https://arxiv.org/abs/2210.13438) supplies an encoder/decoder, residual quantization and entropy-coding starting point; [DAC](https://arxiv.org/abs/2306.06546) supplies improved quantization and reconstruction training, with code and checkpoint routes in its [official repository](https://github.com/descriptinc/descript-audio-codec). All sources were verified by web search during S2. They establish available ingredients, not success on this response metric.

Train directly on authorized present/absent training pairs using full-waveform reconstruction and normalized differential error. Balance energy/overlap strata, reduce reliance on adversarial perceptual quality, and encourage coarse bed codes to remain invariant under quiet perturbations while allocating finer bits to innovation. Test scalar versus vector residual quantization; [finite scalar quantization](https://arxiv.org/abs/2309.15505), also verified this session, offers a simple alternative discretization, although its paper does not prove input-response stability. Arithmetic-code the actual symbols; transmit every parameter, gain, allocation decision and decoder mode inside the counted frame. Selection may choose one overall hybrid artifact, never different static artifacts by hidden instance. Historical audit claims can be checked exactly and need not consume scientific headroom.

A plausible within-episode allocation is ESTIMATED eight four-GPU probes of half an hour, costing 16 H100-h, then ESTIMATED six hours on four GPUs for the chosen residual model, costing 24 H100-h, leaving ESTIMATED 8 H100-h for dictionary fitting, protected validation, cold replay and failed work. Total ESTIMATED 48 H100-h fits the stated reservation only with a competitive lawful warm start and profiled short probes. Encoder fitting must meet the actual per-clip deadline; unrestricted iterative inversion at deployment is not assumed.

My central decomposition is deliberately less optimistic than generic perceptual-codec recall. On synthesis, assume ESTIMATED F=0.95 and T by increasing quietness of 0.95/0.85/0.60; on natural sources, ESTIMATED F=0.85 and T=0.55/0.25/0.05, with overlap averaged within those assumptions. This yields ESTIMATED macro F=0.90, T≈0.542, and a quiet-natural deficit deduction of ESTIMATED 0.017 reward, hence R≈0.43. **ESTIMATED single-run R=0.43, range 0.15–0.76; oracle best-of-four mean=0.57; pass@4 at R≥0.60=0.40; projected upper-95% bound=0.82.** These summarize a subjective, source-dependent desk distribution, not measured frequencies or a fitted statistical interval; correlated source difficulty is retained.

The residual is substantial: unseen stochastic details resist sparse fitting, and tiny input changes can change a loud quantizer code anywhere in the clip. Published subjective audio quality does not resolve that error. Conversely, the source specification does not rule out highly compressible natural recordings and synthesis; ESTIMATED F=0.97/T=0.85 would yield ESTIMATED R=0.82 without deductions. I assign material upper-tail risk to that regime. Current §10 gives scenarios spanning ESTIMATED 0.20–0.88 rather than a central forecast; I reject treating its ESTIMATED F=0.95/T=0.60 example as representative of the hardest natural slices, while retaining its warning that source coding can succeed. The old identical-midpoint attack is fixed: unchanged outputs now have T=0.

## 3. Other routes

- **Best single recipe:** full-budget DAC or EnCodec adaptation with paired response loss and ordinary balanced sampling, without a source decomposition. ESTIMATED R=0.22, range 0.00–0.49. Extra reconstruction quality can leave T near zero when code assignments change discontinuously.
- **Autotuning:** jointly sweep companding strength, coarse/fine bit split, paired-loss weight and quantizer choice using short probes and the charged protected service. ESTIMATED R=0.38, range 0.10–0.65. This is feasible selection over a compact menu, with uncertain short-to-long transfer; it is included in the combined attack rather than credited as extra free compute.
- **Normalizer/response shortcut:** infer an event prior from the bed and use branch-dependent corrections around a common biased reconstruction. ESTIMATED R=0.30, range 0.00–0.78. Common bias cancels in T and is cheap in F for a quiet event, but the encoder still needs an observable event-dependent distinction. Emitting an identical conditional mean on both inputs earns zero. No paired IDs, protected stems or uncharged communication are assumed.

## 4. What would lower lawful saturation

Freeze a source-complexity contract, beyond naming recordings “natural”: independently held-out sessions and mechanisms; independent sign/onset/detail interventions; and measured bed-only predictive event-energy fraction at most ESTIMATED 0.10 in each stratum. Keep the existing reward unchanged and test strong training-dictionary and continuous source-fitting controls on a separate validation population. This would reduce the projected hybrid attack by ESTIMATED 0.05–0.12 reward and, if it actually removes the predictable-source tail, lower its ESTIMATED upper projection toward 0.68–0.73. Cost is ESTIMATED 80–140 author-hours for acquisition, provenance and source design, plus ESTIMATED 96–192 H100-h for fitting/prior/codec controls.

That change is useful only with a same-rate positive control demonstrating response fidelity on the quiet-natural strata. More random detail can destroy feasibility for everyone. Budget ESTIMATED 144–288 additional H100-h for paired reference/direct-stack checks and ESTIMATED 30–50 author-hours for diagnostics. Neither lowering bitrate nor raising the floor addresses the lawful shortcut; neither is recommended here.

## 5. Decisive-check GPU-h re-estimate

§7 distinguishes an ESTIMATED “16GPU-h” bounded preflight from ESTIMATED “2,000” GPU-h for “Cheap anchors.” The latter is the relevant stated complete-screen value; the former cannot establish saturation after adaptation.

I estimate **772 H100-h** for a focused decisive screen, conditional on assembled lawful starts. Allocate three arms—direct paired-loss residual codec, source/residual hybrid, and reference—each with ESTIMATED four independent training/search seeds at the full ESTIMATED four-H100×twelve-hour reservation: ESTIMATED 3×4×48=576 H100-h. Plan ESTIMATED 30M–80M learned scalars per codec, with total dictionaries and weights inside the task's static envelope; these are planning sizes, not inventoried models. Evaluate each of the resulting artifacts on ESTIMATED three independent source/session blocks: ESTIMATED 12×3×4=144 H100-h, using the task's complete grade allowance. This includes its ESTIMATED 2,496 cold clip jobs and preparation/aggregation overhead per grade; seeds are not multiplied again inside a non-retraining grade. Add ESTIMATED three frozen controls—unchanged codec, conditional prior and conventional/source codec—×three blocks×four H100-h=36, and the ESTIMATED 16-H100-h lifecycle/physical preflight. Arithmetic: ESTIMATED 576+144+36+16=772 H100-h.

The preflight must validate the proposed cold-job deadline before any training tranche; failure stops this plan instead of extending the deployed timeout. The same trained artifacts across blocks are paired evaluations, not extra independent researcher attempts. This can detect strong single-run or repeated-search breaches, but ambiguous intervals require a separately planned expansion. The task's ESTIMATED 512-H100-h preparation ceiling is additional when starts/data/runtime do not exist. No resources were booked or used.

## 6. Duplicate check

I inspected these source contracts and the supplied index:

- **v3 06A — MODERATE:** rare-sensitive residual protection and conditional allocation are close interventions, but it compresses persistent attention state for task success rather than transmitting observed waveforms.
- **FIX T11 — WEAK:** matched counterfactual grounding shares the requirement that an intervention matter; it trains visual answering behavior rather than a communication representation.
- **Catalog T23 — WEAK:** instrumented video controllability grades generated trajectories under sampling cost, with no observed-audio reconstruction channel.
- **Catalog V-P2-V6 — NONE:** its source is speech-subset selection with an ASR grader, sharing only audio data.
- **D30 — WEAK:** recovery of temporal evidence from corrupted video latents is evaluator training, not compression/decompression of an input signal.
- **Creative C004 — MODERATE:** quiet precursor preservation is the same application motivation, but the intervention is collection policy and the target is downstream detector performance.
- **Sibling W07, candidate brief — WEAK:** rare conditional generation scores distributional mode mass rather than fidelity of a supplied observation's response.

These overlaps warrant transplant controls, not a STRONG duplicate verdict.

## 7. Verdict

**CUT**, binding on the projected upper-95% line: ESTIMATED 0.82 exceeds 0.75 by ESTIMATED 0.07. This is a desk-screen rejection under the requested projection rule, not an observed S4 or rollout failure. The central attack is appreciably weaker than W04's because the full-waveform differential target creates a real quantization obstacle; its ESTIMATED best-of-four remains only 0.03 below that kill line. The unresolved critique objection is the feasibility-versus-source-predictability fork: the revision improves the estimand and schema but supplies no evidence selecting a useful middle regime. No true merging dependence was found.

## 8. Measurement status

Rollouts UNMEASURED (planned: full-budget direct and hybrid codecs with independent training/search seeds). Grader noise UNMEASURED (planned: replay frozen frames/artifacts across cold workers and hosts, then separately cluster sources and sessions). Score ladder UNMEASURED (planned: identical-output, unstable-quantizer, response-trained and stronger legal artifacts, retaining F/T/deficits). Competent-recipe anchor UNMEASURED (planned: faithful rate-matched DAC/EnCodec plus source-coding controls before any baseline normalization claim). The numeric record entries below are ESTIMATED planning values rather than observed-run statistics.

## Screen record

id: W06
verdict: CUT
binding_line: ub95>=0.75
attack_single_est: 0.43
attack_single_range: 0.15-0.76
bo4_est: 0.57
pass4_est: 0.40
ub95_est: 0.82
gpuh_task_stated: 2000
gpuh_new_est: 772
duplicate_of: v3:06A MODERATE; FIX:T11 WEAK; catalog:T23 WEAK; catalog:V-P2-V6 NONE; D30 WEAK; C004 MODERATE; W07 WEAK
kill_reason: ESTIMATED predictable-source upper tail exceeds projection cutoff
souping_flag: no
