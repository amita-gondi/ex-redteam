# VALIDATION: creative v4 saturation screen

Checks run at 11:20–11:30 AM PT on Nov 21 2026. The tools are in `tools/` and the raw outputs in `logs/`.

## Integrity and limits
- **Sources unchanged.** All 136 source files in /workspace/task_ideation_v4_creative/ (the cards plus the top-level .md files) match their SHA-256 snapshot taken before launch: OK. See ref/source_sha256_before.txt.
- **Limits held.** CPU only: no GPU job, rollout, purchase, doc write, outbound message or GDM contact by this job. The Codex sessions only read local files, ran web searches and wrote card files.
- **Our sessions only.** Five sessions, B0–B4, were run (session ids in STATUS.md), with at most 4 at once. There were zero stalls, zero resumes and zero kills. The three task_design_weakness_claude Codex sessions on the box were left alone.
- **Coverage.** 125/125 card files exist. Each has all 8 sections plus the Screen record and contains UNMEASURED. Cards run 713–883 words, 98,363 in total.
- **Hand-written.** An audit of the session tool calls found that every card was created by a single, card-specific apply_patch "Add File" call: 25 per session × 5. No script wrote card prose; the suspicious-write pattern matched zero times. `tools/aggregate.py` and `tools/finalize.py` only parse the Screen records into screen.tsv.
- **Souping and merging.** No card depends on them and no attack route uses them. A grep found only disclaimers (C035, C093). Every card has `souping_flag: no`.

## Verdict consistency with the bar
Each card's own ESTIMATED numbers were checked against the four kill lines. Over any line means CUT. Within 0.05 of any line means CONDITIONAL.
- 123 of 125 cards were consistent.
- C002 and C008 were marked CONDITIONAL even though their own numbers are over a line (C002: best-of-4 0.63, pass@4 0.54, upper 95% 0.79; C008: upper 95% 0.76). Both are CUT under the bar, the author verdict is kept in screen.tsv, and a reconciliation note was appended to each card.
- All 5 PASS-SCREEN cards clear every line by more than 0.05: best-of-4 0.50–0.52, upper 95% 0.67–0.69, pass@4 0.12–0.24.
- One borderline: C122 (CONDITIONAL) has a single-run range whose upper end reaches 0.71, though its point estimate is 0.50.

## Repeated-wording check
Sentences of 15 words or more were whitespace- and punctuation-normalized and compared exactly across files. Pairwise overlap is the Jaccard similarity of word 8-gram shingles. Headings, the Screen record and the lead's reconciliation notes were excluded.

| Metric | Result | Target |
|---|---|---|
| Long sentences | 2,688 | |
| Long sentences repeated in another file | 0 | |
| Maximum per-file repeated fraction | 0.0% | < 10% |
| Maximum pair Jaccard | 0.0235 (C081–C099) | ≤ 0.10 |
| Pairs above 0.10 | 0 | 0 |

- No batch failed, so no rewrite resume was needed and the before and after numbers are identical. An interim check at 110 files gave the same result (max pair 0.0235).
- Looser check: 256 10-word shingles appear in 3 or more files. All of them are number-reporting fragments such as "ESTIMATED pass@4 at R≥0.60 = 0.99, ESTIMATED projected upper-95% …" or the "no-op ESTIMATED R=0.00 / intended reference ESTIMATED R=0.60" anchors that the source cards share. None is reasoning boilerplate.

## Calibration check (flags)
- **The verdict split is not templated around 0.55–0.60.** Only 1 of 125 single-run attack estimates falls in 0.55–0.60. Mean 0.692, SD 0.141, range 0.40–0.95.
  Histogram by 0.05 bin: 0.40:7, 0.45:16, 0.50:5, 0.55:1, 0.60:11, 0.65:12, 0.70:17, 0.75:23, 0.80:20, 0.85:9, 0.90:3, 0.95:1.
- **FLAG: bimodal, with an empty band at the decision boundary.** Every survivor has a single-run estimate of 0.40–0.53, and every CUT is at 0.58 or above. No card sits between 0.54 and 0.57. This suggests reviewers settled the verdict first and then placed numbers clearly on one side. The rank order inside the survivor set is therefore weakly informative.
- **FLAG: best-of-4 is close to a fixed offset.** Best-of-4 minus single run has mean 0.083, SD 0.016 and range 0.03–0.11, so best-of-4 was not reasoned independently. In practice the best-of-4 line becomes "single run of about 0.52 or more means CUT". That explains why it binds on 58 of 97 CUTs.
- **FLAG: the survivors' upper 95% bounds sit just under the line.** CONDITIONAL bounds are 0.70–0.74, with 9 of 21 at 0.74, and PASS-SCREEN bounds are 0.67–0.69. Upper 95% minus single run has mean 0.207 and SD 0.051, which is more varied but still formulaic.
- **Direction of the re-estimates.** Against the authors' own "ESTIMATED attack R≈" values (mean 0.507, range 0.36–0.71), the screen raised 118 cards, lowered 6 and left 1 unchanged, for a mean change of ESTIMATED +0.185. This matches the FIX-task lesson that the authors' estimates understated the combined-recipe attack.
- **GPU-h is no longer placeholder-like.** The old values took 13 distinct numbers (median 12); the new ones take 58 (median 180, IQR 64–320). Every card shows its arithmetic.

## Citation check
- 253 unique URLs are cited across the cards.
- A seeded random sample of 25 was fetched with curl GET, following redirects. All 25 returned 200 (logs/url_check.tsv).
- Content spot-check: the titles of the 16 arXiv pages in the sample all match the method the card names (ANCE, GPTQ, Punica, Shampoo, DSPy, PPO, PLR, APS, SGLang, DreamCoder, CQL, AlphaCodium, Llumnix, MemGPT, MIR, ST-MoE).
- Three load-bearing 2025–26 citations on PASS-SCREEN cards were also checked: arXiv 2610.23344 "Language Models Learn to Improve Language Models" (C086), 2606.06888 "Data-Constrained Language Model Pretraining…" (C081) and 2502.10517 KernelBench (C116). All exist with matching titles.
- The remaining 228 URLs were not individually checked.

## Known gaps
- Everything is a desk forecast: zero rollouts, zero grader measurements, and score ladders UNMEASURED.
- The duplicate check rests on the reviewers reading the source files the index points to. It is a semantic judgment, not a proof. MODERATE overlaps (156 mentions) were not adjudicated further.
- The kill-reason categories in screen.tsv are my editorial grouping.
- No second, independent reviewer pass was run. The calibration flags above argue for one on the 26 survivors before any of them is promoted.
