# C071 — Recover preference information lost to truncation — saturation screen
## 1. What the grader actually rewards
Useful preprocessing must improve trained preferences on late decisive evidence without sacrificing ordinary cases, while charging the actual retained context tokens. Removing collapsed pairs is a validity repair, not proof of recovered supervision. R≈0 is the competent pair-preserving preprocessing floor, including de-duplication, and R≈1 is the attainable private preference-learning control; all score and resource numbers in this review are ESTIMATED because the raw coverage/quality ladder is UNMEASURED.

Dependency-preserving preference recovery has nominal ESTIMATED reference R=0.60, pending evidence that it beats spending the token budget on intact pairs.

## 2. Strongest lawful combined attack
Inspect chosen and rejected token sequences after the real tokenizer, EOS insertion and context limit. Preserve the distinguishing span plus its shared prompt dependencies, rather than choosing a suffix window solely by raw string difference. Cluster pairs by effective token cost, retain full context for the most valuable long comparisons, and use sliding or prefix-plus-tail windows only where the transformed example still supports its original preference label.

[TRL's DPO configuration](https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_config.py) exposes truncation policies, and its [memory guidance](https://huggingface.co/docs/trl/main/reducing_memory_usage) explicitly discusses adjusting default sequence limits. Start from a correct [DPO objective](https://arxiv.org/abs/2305.18290), combine length bucketing, gradient checkpointing and token-budget-aware example selection, and search the allocation between full long examples and ordinary short ones. None of these ingredients requires recovering already deleted text: the source card provides the original preference pool for preprocessing, so the attack can revisit raw examples lawfully.

ESTIMATED single-run R=0.80, range 0.61–0.92; ESTIMATED best-of-4=0.88; ESTIMATED pass@4 at R≥0.60=0.98; ESTIMATED upper-95% projection=0.97. These are forecasts for a stronger transferred data policy than frozen controls, not measured gains. The residual is examples whose decisive suffix depends on a long, dispersed prefix that cannot fit cheaply. The attacker can allocate more of its fixed token budget to intact representatives, so difficult long cases are not automatically lost. The design has not shown a meaningful attainable advantage over that full-context allocation baseline.

## 3. Other routes
Increasing the context cap for affected pairs, with bucketing and ordinary preference training, is the strongest single standard recipe: ESTIMATED R=0.71, range 0.49–0.87. It is lawful unless actual model context or memory makes it infeasible, which the present card leaves unspecified.

A search route varies intact-long sampling, contrast-window width, dependency-prefix retention and ordinary-case replay under identical token debits. ESTIMATED R=0.77, range 0.56–0.90. Training on a smaller number of complete pairs may beat retaining many mutilated pairs. Raw pair count is not the optimization target, and the grader correctly needs to meter tokens instead.

## 4. What would lower lawful saturation
Specify a model context limit and token budget that make naive cap increases insufficient, while supplying an executable reference that selects semantically sufficient evidence without accessing private preference keys. Hold out long-range dependency mechanisms rather than just longer strings, and verify retained labels after preprocessing. ESTIMATED revised attack R=0.49–0.65. ESTIMATED cost: 8–13 person-days of evidence/dependency authoring and ESTIMATED 216 H100-h for a preference-learning pilot. If no affordable sufficient representation exists for either method, the apparent difficulty is an information bottleneck rather than research reserve.

## 5. Decisive-check GPU-h re-estimate
Old value: ESTIMATED 8 GPU-h. New ESTIMATED 216 H100-GPU-h assumes an ESTIMATED 3B policy and fixed ESTIMATED 3B reference, ESTIMATED 4 preprocessing arms×3 seeds×14 H100-h for long-context preference training=168. Reference preparation and post-tokenization conformance add ESTIMATED 24; exact long-decision and ordinary-case evaluation add ESTIMATED 24. Total ESTIMATED 168+24+24=216. No model is pretrained from scratch. The old budget could confirm collapsed token pairs and try one short adaptation, but does not compare token-efficient recovery of late evidence over multiple training seeds.

## 6. Duplicate check
01A: WEAK after reading its corpus-reconstruction source; both alter learning data, but stage-dependent source ranking differs from preserving the semantics of a single preference pair. T06: MODERATE from its continuation packet because support retention and length/exposure effects overlap, while C071 submits preprocessing rather than a broad support-preserving update controller. T14: WEAK because supported evidence matters to both, but its reporting-policy target is different.

## 7. Verdict
CUT. ESTIMATED single-run reward exceeds its binding line by 0.10 and ESTIMATED best-of-4 exceeds its threshold by 0.28. Full-context allocation, contrast-preserving windows and mature token-budgeted training together are stronger than a suffix-only recovery baseline; the stated extension does not establish a hard residual after them.

## 8. Measurement status
Rollouts UNMEASURED (planned: independent preprocessing searches on fresh suffix-dependency families); grader noise UNMEASURED (planned: repeated preference training and exact long-case evaluation for fixed pools); score ladder UNMEASURED (planned: dropped pairs, suffix windows, complete long pairs, dependency-aware token allocation and attainable retained-preference control).

## Screen record
id: C071
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.80
attack_single_range: 0.61-0.92
bo4_est: 0.88
pass4_est: 0.98
ub95_est: 0.97
gpuh_old: 8
gpuh_new_est: 216
duplicate_of: 01A WEAK; T06 MODERATE; T14 WEAK
kill_reason: intact context allocation and contrast-aware preprocessing cover most gain
souping_flag: no
