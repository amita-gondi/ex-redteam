# Weakness-task (Claude W-series) saturation screen — summary (first batch)

Desk review, CPU only, Nov 21 2026. Go-ahead: Amita 10:33 AM PT. No GPU, no rollouts, no doc writes, nothing to GDM, source folder read-only.
All scores and GPU-h figures below are ESTIMATED. Rollouts, grader noise, score ladders and competent-recipe anchors are all UNMEASURED.
Kill bar (attacker ~10T params, 12 h): single run >0.70, best-of-4 >0.60, pass@4 (R>=0.60) >0.50, projected upper-95% >=0.75.

## Batch 1 (screened 10:35–10:48 AM PT): W01–W06 — 6 screened, 0 PASS-SCREEN, 0 CONDITIONAL, 6 CUT

| id | title | verdict | binding line | strongest lawful attack (ESTIMATED single / range; bo4; pass@4; ub95) | decisive-check H100-h (task stated → ESTIMATED) | nearest duplicates (none STRONG) |
|---|---|---|---|---|---|---|
| W01 | Vocabulary migration without destroying compositional support | CUT | bo4>0.60 (0.66) | Keep active-token/BPE-ancestor closure + FOCUS init + MATT model-aware transfer + balanced continuation with scheduled teacher withdrawal; 0.57 / 0.37–0.76; 0.66; 0.72; 0.82 | 1728 → 606 | C107, T02, T08, T07 — all MODERATE |
| W02 | Joint retrieval learning through encoder–index drift | CUT | single>0.70 (0.77) | Compile evidence into a typed, versioned relation store (DuckDB CTEs, Soufflé-style provenance) answering most queries exactly; fallback = Atlas-style query-only tuning + hybrid lexical/dense (Faiss) + rerank. Bypasses the learned encoder–index problem; 0.77 / 0.51–0.91; 0.85; 0.99; 0.96 | 2496 → 936 | T05, T20, T08, C051, C049 — MODERATE |
| W03 | Dense-to-MoE growth with compositional expert specialization | CUT | pass4>0.50 (0.59) | Sparse Upcycling + granular/virtual-group upcycling (arXiv 2410.07524) + DeepSeekMoE shared+fine experts + standard balancing/z-loss, OLMoE recipe; 0.54 / 0.31–0.73; 0.63; 0.59; 0.80 | 9216 → 5760 | T04, C042, C064, W04 — MODERATE |
| W04 | Dense model growth with retained and newly learned capability | CUT | bo4>0.60 (0.73) | Net2Net + composable Transformer expansions + LiGO learned growth operator, with a stacking (copied-depth) fallback, then balanced continuation; 0.64 / 0.40–0.80; 0.73; 0.78; 0.86 | 2448 → 1512 | 01A, T08, C044, W03 — MODERATE |
| W05 | Discrete-diffusion language refinement with global consistency | CUT | bo4>0.60 (0.80) | Compile the disclosed table/ledger semantics into program skeletons with copied identifiers; jointly supervised diffusion repair only for uncertain parses; 0.72 / 0.40–0.94; 0.80; 0.89; 0.96 | 2592 → 816 | T06, C007 — MODERATE |
| W06 | Neural audio coding that retains quiet events | CUT | ub95>=0.75 (0.82) | Hybrid codec: matching-pursuit parametric front end for structured beds/transients + EnCodec/DAC residual (RVQ vs FSQ), trained on present/absent pairs with a differential loss, arithmetic-coded; 0.43 / 0.15–0.76; 0.57; 0.40; 0.82 | 2000 → 772 | 06A, C004 — MODERATE |

## Main kill patterns
1. **Symbolic-compiler bypass (W02, W05):** the task discloses finite semantics (Horn rules or table/ledger ops), so a lawful compiler plus a trained fallback answers most items without doing the intended learning. This gives the highest attack scores (ESTIMATED 0.72–0.77 single). It's a design flaw, not recipe competence.
2. **Published-recipe stack (W01, W03, W04):** the FIX-task pattern again. Known transfer/growth papers plus continuation and sweep reach ESTIMATED 0.54–0.64 single, and repeated attempts cross bo4 or pass@4.
3. **Source-predictability tail (W06):** the central attack is moderate (ESTIMATED 0.43; bo4 0.57, only 0.03 under its line), but compressible authored sources leave a material upper tail (ESTIMATED ub95 0.82). W06 is the closest to surviving. A fix would have to select stochastic/natural sources where parametric fitting fails, and that is unproven.
4. In every case the "competent-recipe" normalization anchor is designed, not measured. None of the revisions closes the critic's core saturation objection.

## GPU-h re-estimates
The task-stated figures are whole screening/pilot programmes (2000–9216 H100-h). The re-estimated *decisive* checks are smaller: a frozen strongest-attack stack vs reference vs baseline, 3 blocks × 3 seeds plus evaluation. Ranges: W01 606, W02 936, W03 5760 (MoE training dominates), W04 1512, W05 816, W06 772 H100-h, all ESTIMATED. They exclude package/data authoring.

## Duplicates
No STRONG duplicate was found against v3, FIX, D01–D32, catalog T01–T23 or creative v4. The closest collisions, all MODERATE, are W01↔C107 (vocabulary + optimizer-moment migration), W03↔W04 (siblings: sparse vs dense growth), W04↔C044, W05↔C007, W06↔C004/06A, and W02↔C049/C051/T05.

## Checks
- Repeated wording (6 cards, 218 sentences of 15+ words): 0 repeated (max per-card 0.0%), max pairwise 8-gram Jaccard 0.0003. No rewrites needed. Tool: tools/audit_wording.py, output logs/wording_audit.json.
- URLs: all 28 unique cited URLs return HTTP 200 (logs/url_check.tsv).
- Calibration: single-run points are 0.43/0.54/0.57/0.64/0.72/0.77 and binding lines vary (bo4 ×3, single, pass@4, ub95), so the scores aren't clustered from a template. The uniform CUT reflects each task's design, not one shared number.
- Source integrity: the Codex sessions wrote only into this folder (patch audit of the session JSONL). The source folder was read-only to us.

## Pending
W07–W14 have no rev_ entry yet. At 10:49 AM PT: W07 crit running, W08 and W09 gen running, W10–W14 not started. The watcher (logs/watcher.sh) auto-screens each one as its rev_ appears and updates screen.tsv/screened.txt. This summary needs a second-batch section when they finish.
