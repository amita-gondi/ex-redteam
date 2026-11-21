# Screen vs independent red team: disagreements

Written last, after all 50 red-team verdicts were frozen (R1–R6 done; last session exited 12:16 PM PT Nov 21 2026). Every number is **ESTIMATED**. Nothing is measured.

Mapping used: PASS-SCREEN ≈ HOLDS, CONDITIONAL ≈ FIX, CUT ≈ CUT. For the D cards, "promising" ≈ HOLDS and "conditional" ≈ FIX. No D-card saturation screen exists, so the D cards are compared with their original design verdicts in `/workspace/hidden_task_cards_v4/00_index.md`. Those cards give only symbolic F_D(U) attack forecasts, so there are no numeric deltas for them.

## Wave 1: D cards vs original card verdicts
- Promising (5): all 5 were downgraded to **FIX** (D07, D17, D21, D26, D32). None HOLDS.
- Conditional (19): **5 FIX** (D06, D08, D12, D18, D28; consistent) and **14 CUT** (D03, D04, D05, D09, D10, D11, D14, D15, D20, D22, D25, D27, D29, D30). Each CUT is a disagreement.
- Ranking: the cards' top 5 (D26, D07, D21, D32, D17) are still among the red team's top 7. The red team ranks D28 (the cards' #7) at #4, ahead of D21 and D17.
- Total: 19 of 24 verdicts are one step harsher than the original. None is more lenient.

| ID | Original card verdict | Red-team verdict | Red-team strongest attack ESTIMATED | Red-team bo4 / pass@4 ESTIMATED |
|---|---|---|---|---|
| D03 | conditional | CUT | ESTIMATED 0.76 (ESTIMATED 0.52–0.95) | ESTIMATED 0.84 / ESTIMATED 0.92 |
| D04 | conditional | CUT | ESTIMATED 0.74 (ESTIMATED 0.49–0.94) | ESTIMATED 0.82 / ESTIMATED 0.89 |
| D05 | conditional | CUT | ESTIMATED 0.79 (ESTIMATED 0.55–0.97) | ESTIMATED 0.87 / ESTIMATED 0.95 |
| D06 | conditional | FIX | ESTIMATED 0.66 (ESTIMATED 0.41–0.89) | ESTIMATED 0.74 / ESTIMATED 0.79 |
| D07 | promising | FIX | ESTIMATED 0.62 (ESTIMATED 0.39–0.84) | ESTIMATED 0.69 / ESTIMATED 0.68 |
| D08 | conditional | FIX | ESTIMATED 0.64 (ESTIMATED 0.39–0.88) | ESTIMATED 0.72 / ESTIMATED 0.75 |
| D09 | conditional | CUT | ESTIMATED 0.77 (ESTIMATED 0.51–0.96) | ESTIMATED 0.85 / ESTIMATED 0.92 |
| D10 | conditional | CUT | ESTIMATED 0.82 (ESTIMATED 0.61–0.98) | ESTIMATED 0.90 / ESTIMATED 0.94 |
| D11 | conditional | CUT | ESTIMATED 0.79 (ESTIMATED 0.56–0.96) | ESTIMATED 0.88 / ESTIMATED 0.92 |
| D12 | conditional | FIX | ESTIMATED 0.66 (ESTIMATED 0.41–0.88) | ESTIMATED 0.75 / ESTIMATED 0.77 |
| D14 | conditional | CUT | ESTIMATED 0.77 (ESTIMATED 0.53–0.95) | ESTIMATED 0.86 / ESTIMATED 0.90 |
| D15 | conditional | CUT | ESTIMATED 0.80 (ESTIMATED 0.55–0.97) | ESTIMATED 0.89 / ESTIMATED 0.93 |
| D17 | promising | FIX | ESTIMATED 0.65 (ESTIMATED 0.42–0.88) | ESTIMATED 0.72 / ESTIMATED 0.77 |
| D18 | conditional | FIX | ESTIMATED 0.65 (ESTIMATED 0.39–0.87) | ESTIMATED 0.74 / ESTIMATED 0.75 |
| D20 | conditional | CUT | ESTIMATED 0.78 (0.52–0.96) | ESTIMATED 0.85 / ESTIMATED 0.94 |
| D21 | promising | FIX | ESTIMATED 0.64 (ESTIMATED 0.42–0.86) | ESTIMATED 0.73 / ESTIMATED 0.72 |
| D22 | conditional | CUT | ESTIMATED 0.76 (0.49–0.94) | ESTIMATED 0.83 / ESTIMATED 0.92 |
| D25 | conditional | CUT | ESTIMATED 0.80 (0.53–0.96) | ESTIMATED 0.87 / ESTIMATED 0.95 |
| D26 | promising | FIX | ESTIMATED 0.61 (ESTIMATED 0.37–0.84) | ESTIMATED 0.70 / ESTIMATED 0.66 |
| D27 | conditional | CUT | ESTIMATED 0.79 (0.52–0.96) | ESTIMATED 0.86 / ESTIMATED 0.94 |
| D28 | conditional | FIX | ESTIMATED 0.63 (0.38–0.87) | ESTIMATED 0.70 / ESTIMATED 0.77 |
| D29 | conditional | CUT | ESTIMATED 0.84 (0.57–0.98) | ESTIMATED 0.91 / ESTIMATED 0.97 |
| D30 | conditional | CUT | ESTIMATED 0.77 (0.46–0.96) | ESTIMATED 0.84 / ESTIMATED 0.91 |
| D32 | promising | FIX | ESTIMATED 0.61 (0.37–0.85) | ESTIMATED 0.68 / ESTIMATED 0.71 |

## Wave 2: creative survivors vs creative saturation screen (`/workspace/creative_v4_saturation_screen/screen.tsv`)
Verdict cross-tab (screen → red team):
- PASS-SCREEN (5) → FIX 3 (C045, C081, C099), CUT 2 (**C086, C116**). No PASS-SCREEN card HOLDS.
- CONDITIONAL (21) → FIX 11 (C010, C024, C042, C053, C064, C084, C096, C103, C106, C112, C127), CUT 10 (C012, C020, C037, C044, C056, C080, C087, C095, C119, C122).
- Agreement (CONDITIONAL↔FIX): 11 of 26. Disagreement: 15 of 26, all in the harsher direction. The sharpest cases are C086 and C116, PASS-SCREEN cards the red team CUT. Their attack deltas are the largest at +0.38 and +0.40.

Attack-estimate deltas: red-team strongest lawful combined-recipe attack minus the screen's strongest single attack is **+0.17 to +0.40, mean +0.26 (ESTIMATED)**. The direction is uniform across all 26. The screen put all 26 below the single-run line (0.40–0.51) and its best-of-4 estimates at 0.50–0.59. The red team puts all 26 over all four lines.

Why they diverge (my reading of the files; not measured):
1. The red team scores a full stack of lawful published recipes plus engineering tuned under a 10T/12h budget. It often uses a direct bypass, such as search, probing, exact fallback or distillation, that removes the claimed learned residual. The screen scored a narrower strongest single attack.
2. The red team treats the card's unspecified anchors (b, c, ceiling) as leaving the whole reward range open. It refuses to credit margins that depend on calibration the card does not yet have.
3. Decisive-check cost means different things in the two outputs. The screen re-estimated a full decisive check at ESTIMATED 20–1200 GPU-h. The red team's figure is the cheapest kill check, which is CPU-only (0 GPU-h) for 17 of 26 and ESTIMATED 2–44 GPU-h for the rest. These figures measure different experiments and should not be compared directly.

Neither side is evidence. The gap of about 0.26 is itself the main finding. It shows the attack estimates are not calibrated, and the cheapest CPU kill checks should run before any GPU pilot.

| ID | Title | Screen verdict | Red-team verdict | Screen attack ESTIMATED | Red-team attack ESTIMATED | Delta | Screen bo4 / pass@4 / ub95 ESTIMATED | Red-team bo4 / pass@4 / ub95 ESTIMATED | Screen decisive GPU-h (new) ESTIMATED | Red-team cheapest decisive GPU-h ESTIMATED |
|---|---|---|---|---|---|---|---|---|---|---|
| C010 | Train through delayed simulator corrections | CONDITIONAL | FIX | 0.46 | 0.67 | +0.21 | 0.56 / 0.34 / 0.72 | 0.74 / 0.84 / 0.93 | 120 | 0.0 |
| C012 | Recover learnability after curriculum-induced gradient starvation | CONDITIONAL | CUT | 0.49 | 0.76 | +0.27 | 0.59 / 0.43 / 0.74 | 0.84 / 0.93 / 0.98 | 252 | 21.0 |
| C020 | Train a memory admission predictor for inference state | CONDITIONAL | CUT | 0.48 | 0.77 | +0.29 | 0.59 / 0.44 / 0.74 | 0.85 / 0.94 / 0.99 | 68 | 0.0 |
| C024 | Retain scientific uncertainty in compressed experiment records | CONDITIONAL | FIX | 0.42 | 0.71 | +0.29 | 0.53 / 0.29 / 0.7 | 0.8 / 0.89 / 0.96 | 120 | 0.0 |
| C037 | Co-schedule draft training and target inference | CONDITIONAL | CUT | 0.51 | 0.78 | +0.27 | 0.59 / 0.46 / 0.74 | 0.86 / 0.95 / 0.99 | 60 | 0.0 |
| C042 | Pretrain conditional computation with delayed expert utility | CONDITIONAL | FIX | 0.49 | 0.66 | +0.17 | 0.58 / 0.41 / 0.73 | 0.74 / 0.83 / 0.94 | 432 | 0.0 |
| C044 | Choose pretraining architectures using downstream editability | CONDITIONAL | CUT | 0.48 | 0.75 | +0.27 | 0.57 / 0.37 / 0.72 | 0.83 / 0.92 / 0.98 | 480 | 19.0 |
| C045 | Pretraining with stateful external memory under update churn | PASS-SCREEN | FIX | 0.42 | 0.68 | +0.26 | 0.51 / 0.23 / 0.68 | 0.77 / 0.86 / 0.95 | 400 | 0.0 |
| C053 | Search for absent evidence without inventing a negative result | CONDITIONAL | FIX | 0.50 | 0.73 | +0.23 | 0.58 / 0.4 / 0.72 | 0.81 / 0.9 / 0.97 | 48 | 0.0 |
| C056 | Search that learns executable query rewrites for codebases | CONDITIONAL | CUT | 0.48 | 0.76 | +0.28 | 0.57 / 0.35 / 0.71 | 0.84 / 0.91 / 0.98 | 192 | 0.0 |
| C064 | Router regularization invariant to token packing | CONDITIONAL | FIX | 0.47 | 0.68 | +0.21 | 0.56 / 0.32 / 0.7 | 0.77 / 0.85 / 0.95 | 768 | 0.0 |
| C080 | Recover address-generation speed without changing integer semantics | CONDITIONAL | CUT | 0.48 | 0.81 | +0.33 | 0.58 / 0.32 / 0.73 | 0.89 / 0.96 / 0.99 | 20 | 0.0 |
| C081 | Masked-input regularization after repetitions stop being exchangeable | PASS-SCREEN | FIX | 0.43 | 0.63 | +0.20 | 0.52 / 0.16 / 0.68 | 0.73 / 0.8 / 0.93 | 408 | 4.8 |
| C084 | Approximate speculation with a real downstream regret contract | CONDITIONAL | FIX | 0.49 | 0.71 | +0.22 | 0.59 / 0.36 / 0.74 | 0.8 / 0.88 / 0.96 | 48 | 2.1 |
| C086 | Research world models graded only by executed improvements | PASS-SCREEN | CUT | 0.40 | 0.78 | +0.38 | 0.5 / 0.12 / 0.67 | 0.86 / 0.94 / 0.99 | 1200 | 0.0 |
| C087 | Prior-support diagnostics that unlock genuinely new RL behavior | CONDITIONAL | CUT | 0.47 | 0.79 | +0.32 | 0.57 / 0.29 / 0.72 | 0.87 / 0.94 / 0.99 | 352 | 0.0 |
| C095 | Find an optimizer coordinate system beyond standard recipe sweeps | CONDITIONAL | CUT | 0.49 | 0.80 | +0.31 | 0.59 / 0.34 / 0.74 | 0.88 / 0.95 / 0.99 | 624 | 0.0 |
| C096 | Discover an image representation that retains violated constraints | CONDITIONAL | FIX | 0.47 | 0.67 | +0.20 | 0.57 / 0.28 / 0.72 | 0.78 / 0.86 / 0.96 | 336 | 0.0 |
| C099 | Recheck a curriculum proxy when the learner changes | PASS-SCREEN | FIX | 0.42 | 0.66 | +0.24 | 0.52 / 0.16 / 0.68 | 0.75 / 0.86 / 0.96 | 480 | 16.0 |
| C103 | First build a privacy attack, then train a deletion method | CONDITIONAL | FIX | 0.46 | 0.78 | +0.32 | 0.56 / 0.38 / 0.72 | 0.89 / 0.95 / 0.99 | 176 | 27.0 |
| C106 | Improve a world model by limiting its planner's evidence access | CONDITIONAL | FIX | 0.44 | 0.65 | +0.21 | 0.54 / 0.31 / 0.71 | 0.76 / 0.83 / 0.97 | 144 | 14.0 |
| C112 | Recover scientific images while learning a better acquisition policy | CONDITIONAL | FIX | 0.45 | 0.69 | +0.24 | 0.55 / 0.33 / 0.72 | 0.8 / 0.89 / 0.98 | 160 | 19.0 |
| C116 | A tool-building curriculum for unfamiliar accelerator DSLs | PASS-SCREEN | CUT | 0.41 | 0.81 | +0.40 | 0.51 / 0.24 / 0.69 | 0.91 / 0.98 / 0.995 | 144 | 0.0 |
| C119 | Train the agent to detect its own research dead ends | CONDITIONAL | CUT | 0.48 | 0.76 | +0.28 | 0.58 / 0.44 / 0.74 | 0.86 / 0.94 / 0.99 | 304 | 0.0 |
| C122 | Self-training a research critic without rewarding persuasive prose | CONDITIONAL | CUT | 0.50 | 0.74 | +0.24 | 0.59 / 0.46 / 0.74 | 0.85 / 0.93 / 0.99 | 256 | 0.0 |
| C127 | A curriculum flywheel that learns from cross-project interference | CONDITIONAL | FIX | 0.45 | 0.67 | +0.22 | 0.56 / 0.34 / 0.73 | 0.78 / 0.87 / 0.97 | 400 | 44.0 |

Delta (red team minus screen, ESTIMATED): min +0.17, max +0.40, mean +0.26, n=26
