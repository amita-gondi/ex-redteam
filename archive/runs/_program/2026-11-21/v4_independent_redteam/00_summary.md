# v4 independent red team: summary

Amita approved this at 10:33 AM PT on Nov 21 2026. It is a CPU-only desk review in the T01–T23 independent red-team format. Each task file has 11 attacks: 3 specific to the task, 7 standard exploit categories, and a row for the strongest lawful combined recipe. Each file also has a web-checked recipe section, a saturation check against the 10T/12h kill lines and a HOLDS/FIX/CUT verdict. All scores are **ESTIMATED** and all measurements are **UNMEASURED**. No rollouts or GPU work were run, no docs were written, nothing was sent anywhere, and no sources were modified.

| Group | Tasks | HOLDS | FIX | CUT |
|---|---|---|---|---|
| D cards (5 promising + 19 conditional) | 24 | 0 | 10 | 14 |
| Creative v4 screen survivors (5 PASS-SCREEN + 21 CONDITIONAL) | 26 | 0 | 14 | 12 |
| Claude W tasks passing their screen | 0 | – | – | – |
| **Total** | **50** | **0** | **24** | **26** |

- Wave 1 details: [redteam/00_wave1_summary.md](redteam/00_wave1_summary.md). Wave 2 details: [redteam/00_wave2_summary.md](redteam/00_wave2_summary.md). Machine table: [verdicts.tsv](verdicts.tsv). Disagreements: [screen_disagreement.md](screen_disagreement.md).
- Headline: **no task HOLDS**. The red team puts every one of the 50 tasks over all four kill lines as currently specified. FIX means a bounded redesign might restore a credible residual mechanism.
- Strongest lawful combined-recipe attack, ESTIMATED: FIX 0.61–0.78, CUT 0.74–0.84. Every task sits at or above the 0.57–0.62 level that kept the 10 catalog FIX tasks on HOLD.
- Top survivors overall, by ESTIMATED attack: D32 0.61, D26 0.61, D07 0.62, C081 0.63, D28 0.63, D21 0.64, D08 0.64, C106 0.65, D17 0.65, D18 0.65.
- Versus the creative screen: every one of 26 is harsher. Attack deltas run +0.17 to +0.40, mean +0.26 (ESTIMATED). The screen passed C086 and C116, and the red team CUT both. Both sets of estimates are uncalibrated. The cheapest CPU kill checks (0 GPU-h for 25 of 50 tasks) should run before any GPU pilot.
- W tasks: W01–W07 were all screened CUT as of 11:25 AM PT, so none entered this red team. The W ids covered are **none**. A separate hourly routine handles W08–W14 if any pass.
