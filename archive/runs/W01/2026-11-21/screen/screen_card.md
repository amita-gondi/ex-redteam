# W01 — Vocabulary migration without destroying compositional support — saturation screen
## 1. What the grader actually rewards
The outcome is macro executable-completion accuracy across new atomic, new morphological, new dependency, old atomic, old compositional and mixed API cases, after independently reconstructing the submitted migration and continuation recipe. Under the ESTIMATED design constants, reward is clipped `(U − P_slice − P_claim − 0.30)/0.70`: effective accuracy at or below ESTIMATED 0.30 earns zero, the reference target of ESTIMATED 0.72 earns ESTIMATED R=0.60, and perfect unpenalized accuracy earns R=1. Neither the no-op zero, the competent-recipe floor nor that reference accuracy has been measured; the proposed stronger control is also a desired outcome, not an attainable ceiling demonstrated by execution. Slice floors affect certification and impose small continuous penalties, rather than multiplying reward by a preservation gate. Every numerical forecast and derived quantity below, including the numerical Screen record, is ESTIMATED; source section identifiers and the user's kill thresholds are requirements, not measurements.

## 2. Strongest lawful combined attack
Start by counting the old training corpus's active tokens and complete BPE ancestor closure. Keep the corresponding ranks and both untied embedding rows, recycle genuinely dormant rows, and admit new pieces only after checking segmentation on permitted old contexts. A vocabulary cap does not establish vocabulary pressure: these compact authored libraries might leave ample spare capacity. This is the attack's structural advantage, before any sophisticated initialization.

Initialize added rows with [FOCUS](https://aclanthology.org/2023.emnlp-main.829/), using auxiliary representations built exclusively from the admitted corpus, then apply [MATT](https://arxiv.org/abs/2510.21954) attention/value alignment and output-head calibration. The verified [MATT implementation](https://github.com/Goader/matt) explicitly combines overlap preservation, FOCUS initialization and aligned spans; these are compatible components, not unrelated paper names. Compare a separate [OMP transplantation](https://arxiv.org/abs/2506.06607) branch only if a permitted donor can be constructed economically. This is vocabulary-embedding initialization, with no checkpoint combination. [WECHSEL](https://aclanthology.org/2022.naacl-main.293/) is a legitimate comparator only where its aligned semantic-space assumptions can actually be supplied; there is no free multilingual donor in this task.

Continue with balanced old/new exposure, a short embedding-focused phase, cautious backbone updates, common-byte teacher support and scheduled withdrawal. Tune transfer strength, retained pieces and continuation settings on training probes, spending the scarce primary dev queries on complete contenders. The ESTIMATED research allocation is 8 H100-h for corpus/transfer probes, 12 H100-h for smaller-model screening, 48 H100-h for primary continuations, 12 H100-h for official evaluation and 16 H100-h for calibration, failed work and final selection: ESTIMATED 96 H100-h total within the task reservation. Use one serialized final recipe and a receipt-derived truthful ledger. No inference compiler or additional labeled training is needed.

My ESTIMATED single-run R is 0.57, range 0.37–0.76; ESTIMATED oracle best-of-four is 0.66, pass@4 at R≥0.60 is 0.72, and projected upper-95% score bound is 0.82. These are subjective saturation forecasts, not fitted confidence intervals. One explicit central scenario has ESTIMATED stratum accuracies `(0.82,0.69,0.51,0.85,0.74,0.59)`, averaging ESTIMATED U=0.70 and yielding approximately ESTIMATED R=0.57 when penalties are inactive. An ESTIMATED per-attempt threshold probability of 0.27 gives ESTIMATED pass@4 of 0.72 under conditional independence; shared project difficulty makes that approximation uncertain.

The remaining gap is learned long dependency execution and mixed-library composition, which initialization cannot supply by preserving surface units. Limited exposure, actual donor costs and three-seed reconstruction prevent assuming the best research checkpoint transfers unchanged. I therefore put the center below §10's ESTIMATED R≈0.643, rather than adopting its optimistic retained/compositional vector. Nevertheless, the complete known stack closely matches the proposed reference's substantive work, and search can beat the designed floor. The author's revised warning is appropriate; its central value is not evidence for my tail probabilities.

## 3. Other routes
- **One established recipe:** retained-overlap MATT followed by ordinary continuation, without contextual merge scoring or broad search: ESTIMATED R=0.43, range 0.22–0.64. The aligned transfer helps initialization; unseen call graphs remain a learned capability deficit.
- **Budgeted enumeration:** successive elimination over vocabulary admission, alignment strength, embedding learning rate and support withdrawal, using cheap training probes before primary evaluations: ESTIMATED R=0.53, range 0.30–0.73. Smaller-model rank transfer is uncertain, but there is no measured lower bound on full-trial duration that prevents useful search.
- **Lawful objective shortcut:** prioritize acquisition and mixed cases while automating required claims and accepting localized old-support penalties: ESTIMATED R=0.46, range 0.28–0.58. Under §5's estimated anchors, even complete old-stratum abandonment can retain roughly ESTIMATED R=0.46. This does not itself cross a kill line, but demonstrates that the retention floors do not gate the reward to zero. Legal dev selection could improve it; quota bypass or hidden-label access is excluded.

## 4. What would lower lawful saturation
Replace compact lexical worlds with independently authored projects whose measured active vocabulary and competing semantic boundaries impose a deployment-relevant tradeoff at the existing row limit. Preserve dormant-row reuse and unchanged-token baselines as legal choices. Conditional on a real conflict, ESTIMATED attack reduction is 0.08–0.16 R; establishing learnability and lexical pressure would cost ESTIMATED 3–5 author-weeks plus 192 H100-h of matched continuations. Adding arbitrary rare strings or merely lowering the row cap would not establish that effect.

Separately, publish an acquisition/retention utility that charges old-support loss relative to the stronger inherited or continued baseline before averaging gains. Calibrate a smooth tradeoff on independent content, retaining localized credit. ESTIMATED effect on the balanced stack is only 0.00–0.04 R, although the abandonment route could lose ESTIMATED 0.12–0.22 R; ESTIMATED cost is 2 author-days and 96 H100-h for specialist controls. Neither change warrants a pass without raw reference-minus-recipe reserve; moving the floor after a strong recipe wins supplies no scientific improvement.

## 5. Decisive-check GPU-h re-estimate
The relevant stated §7 screening row is “Three complete recipe families×three paired pilots,” with “9(B+H) = 1728” GPU-h, an ESTIMATED task budget rather than an executed check. It is broader than the cheapest informative comparison.

My new ESTIMATED minimum is **606 H100-h**. Freeze one combined attack using an ESTIMATED 96 H100-h search allowance; then compare that recipe, the author reference and unchanged-token continuation on separate authored project blocks. ESTIMATED training arithmetic is 3 arms × 3 blocks × 3 continuation seeds × 4 H100 × 4 hours = 432 H100-h on Pythia-1.4b. Add ESTIMATED 9 arm/block evaluations × 6 H100-h = 54 H100-h for fixed hidden decoding, baseline retention and independent truth controls, plus ESTIMATED 24 H100-h for conversion, admitted claim checks and cold replay: ESTIMATED 96+432+54+24=606 H100-h. Equal per-arm training reservations avoid buying a weak baseline.

This assumes the package, warm starts and independent semantic banks already exist; their authoring is additional. The experiment can reveal a clear score/native-reserve breach and stop work, but cannot certify best-of-four tails or the unavailable stronger researcher. Borderline project variation requires a preregistered expansion; repeated continuation seeds do not replace new projects. All proposed GPU work remains unexecuted.

## 6. Duplicate check
- **v3 01A — WEAK:** its actual source changes corpus allocation across stages with an immutable tokenizer; W01 changes segmentation and embedding correspondence.
- **FIX T02 / catalog T02 — MODERATE:** both optimize continued learning with retention, but their source interfaces keep tokenization fixed and grade held-text loss rather than executable lexical transfer.
- **FIX T08 / catalog T08; catalog T07 — MODERATE:** their actual contracts cover parameter interference or supervision withdrawal, so W01's consolidation alone adds little; vocabulary treatment remains a distinct intervention.
- **D07 — WEAK:** the source trains an online shortcut-prevention controller using learning telemetry, rather than migrating an alphabet.
- **Creative C107 — MODERATE:** its source jointly migrates vocabulary and optimizer moments, grading byte loss within migration time; W01 lacks that moment-state treatment and uses executable support accuracy. This is the closest collision, but does not meet the same-intervention/same-target definition of STRONG.
- **Creative C041 / C048 — WEAK:** opened sources respectively hold tokenization fixed for exposure allocation and change a lossless storage codec.
- **Sibling W03 / planned W04 — WEAK:** their candidate briefs concern sparse expert growth or dense capacity growth, not lexical rows. No STRONG duplicate is established.

## 7. Verdict
**CUT.** The binding forecast is ESTIMATED best-of-four 0.66, exceeding the 0.60 line by ESTIMATED 0.06; ESTIMATED pass@4 and projected upper bound also cross their kill thresholds. This is a desk decision, not an observed saturation result. The critique's key objection survives the revision: active-support capacity and faithful transfer/consolidation may remove the purported dependent research problem. Revised accounting, historical-claim scopes and explicit admission that recipes may win improve the specification without lowering lawful saturation.

## 8. Measurement status
Rollouts UNMEASURED (planned: frozen complete stack and reference on independent API projects). Grader noise UNMEASURED (planned: repeated same-artifact grades and separately clustered continuation/project variation). Score ladder UNMEASURED (planned: unchanged alphabet, retained expansion, model-aware transfer, complete stack and reference, reporting native strata before normalization). Competent-recipe anchor UNMEASURED (planned: active-closure audit and matched-byte/work full-stack continuation before accepting the proposed floor).

## Screen record
id: W01
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.57
attack_single_range: 0.37-0.76
bo4_est: 0.66
pass4_est: 0.72
ub95_est: 0.82
gpuh_task_stated: 1728
gpuh_new_est: 606
duplicate_of: C107 MODERATE; T02 MODERATE; T08 MODERATE; T07 MODERATE
kill_reason: retained vocabulary plus model-aware transfer and continuation exceeds repeated-search bar
souping_flag: no
