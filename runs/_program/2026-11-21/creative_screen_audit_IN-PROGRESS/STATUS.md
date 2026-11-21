# STATUS: creative v4 screen audit (evidence audit + re-estimate + redesign; CPU/desk only)

**State: RUNNING.**  Go-ahead: Amita, 11:49 AM PT Nov 21 2026, relayed via Extrapolate RL Envs.
Scope: 120 cards (21 CONDITIONAL + 99 CUT incl. C002/C008 overridden to CUT). Out of scope: C086, C045, C116, C099, C081.

## Checkpoints (PT)
- 11:50 AM. Folder created; 120 ids in ref/all_ids.txt, 12 batches of 10 (ref/batch_00..11). Source SHA-256 snapshot: ref/source_sha256_before.txt (320 files from creative_v4_saturation_screen + task_ideation_v4_creative, logs excluded).
- 11:51 AM. Prompts in prompts/ (TEMPLATE.md, B00..B11, F for frontier_reference.md). Watcher tools/watcher.sh started (pid in logs/watcher.pid): max 4 concurrent own sessions, stall = session JSONL idle >=15 min -> kill own pid, resume same session, cap 4 resumes. Launched F, B00, B01, B02.

## If you resume
Watcher state: logs/watch_status.txt, logs/watcher.log. A card is complete when it has "## Audit record" and "souping_flag:". If the watcher died, restart: `cd /workspace/creative_v4_screen_audit && nohup bash tools/watcher.sh > logs/watcher.out 2>&1 &` (it resumes, does not relaunch, any job with a log).
Do NOT touch pids 274171 / 278578 or red-team / Claude sessions.
- 11:55 AM. F done: frontier_reference.md written (20 sources, all marked fetched; liveness check pending).
- 12:01 PM. 13 cards done across B00–B02 (~1–1.3 min/card/session). B03 launched. Spot-check of C014: card-specific evidence audit, 5 fetched sources incl. RE-Bench/RExBench, scenario-mixture derivation of bo4/pass@4/ub95 (no fixed offset). ETA all 120 ≈ 12:45–1:15 PM PT, then aggregation/validation ≈ 20 min.
- 12:06 PM. BINDING amendment from Amita (12:04 PM PT, via RL Envs): anchor every attack to DEMONSTRATED agent results; attack_basis field (DEMONSTRATED-AGENT | LITERATURE-ONLY | ASSUMED); subfield SOTA anchor; anchored verdict + flip headline; new audit.tsv columns; update frontier_reference.md. Plan: stop watcher, kill own B00–B03 sessions, resume each with amendment instructions (amend done cards in place), regenerate B04–B11 prompts, add job F2 (frontier_reference update), restart watcher with completion = 'anchored_verdict:' present. State before: 2026-11-21 12:04:31 PST active=4 F:1/1(r0) B00:4/10(r0) B01:5/10(r0) B02:4/10(r0) B03:0/10(r0)
- 12:06 PM. Amendment applied: prompts/AMEND.md appended to all batch prompts (B04–B11 regenerated); B00–B03 killed (own pids) and resumed in the same sessions with the amendment (amend done cards in place); watcher patched (completion requires anchored_verdict:; job F2 = resume of F session to update frontier_reference.md, queued before B04) and restarted, pid 404458.
- 12:17 PM. Found the original watcher (pid 382596, started 11:51; logs/watcher.pid had recorded wrapper pid 382593) still running alongside the new one; both were this audit's (PWD=creative_v4_screen_audit). Killed 382596; exactly one watcher remains: 404458. No duplicate launches occurred (watcher.log clean). 15 cards complete in amended format (B00 4, B01 4, B02 4, B03 3); pace ≈2.6 min/card/session.
- ETA (PT): all 120 cards + F2 ≈ 1:30–1:45 PM; aggregation (audit.tsv incl. attack_basis, demonstrated_ref, gap_to_attack, subfield_sota_ref, anchored verdict), URL liveness, boilerplate + distribution checks, 00_summary.md, VALIDATION.md ≈ 2:00–2:10 PM.

## Remaining after cards finish
1. Extend tools/aggregate.py cols with attack_basis, demonstrated_ref, gap_to_attack, subfield_sota_ref, anchored_single/bo4/pass4/ub95, anchored_verdict, anchored_flip, verdict_rests_on_assumption, redesign_attack_basis; run it.
2. python3 tools/audit_wording.py > logs/wording.json (target: repeated 15+ word sentences ≈0, no pair >0.10 Jaccard8; check 4A paragraphs especially).
3. bash tools/url_check.sh (all URLs incl. frontier_reference.md).
4. Distribution check: bo4−single gap spread, exact-value clustering, 0.54–0.57 band occupancy, old vs new.
5. Source integrity: re-hash vs ref/source_sha256_before.txt.
6. Write 00_summary.md (grade counts, flips old→new and old→anchored by direction, REDESIGNABLE ranked, TRULY-DEAD grouped, under-research verdict) and VALIDATION.md.
