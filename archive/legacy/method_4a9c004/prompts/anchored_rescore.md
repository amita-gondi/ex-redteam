You are doing a CPU-only, desk-only ANCHORED RE-SCORE of an earlier saturation screen of one RL-environment research task. Task: {{TASK_ID}}. Date: {{DATE}}. Repo root: {{REPO}}. Method version: {{METHOD_VERSION}}.

WHY THIS STAGE EXISTS (Amita's binding rule, Nov 21, 2026, 12:04 PM PT)
Screen attack estimates measured the attacker against our own idea of what could be done, not against what SOTA agents have actually been shown to do. Anchor every attack to DEMONSTRATED results. Don't defend the earlier screen, and don't overturn it for the sake of it. Flips in either direction are fine.

{{COMMON}}

STAGE-SPECIFIC INPUTS (read-only)
- The earlier screen: {{PRIOR_SCREEN}}
- method/evidence_grounding_rule.md (binding) and method/refs/frontier_reference_snapshot_2026-11-21.md, a starting list. You must fetch any source you cite yourself, and tie it to THIS task's capability.

WHAT TO DO
1. **Demonstrated results:** cite at least 2 demonstrated agent or model results on this capability, or the closest comparable ones. Fetch each. For each, record:
   - model and scaffold;
   - time and compute;
   - what was achieved;
   - the gap to what this task's attack needs.
2. **Recipe vs demonstration:** separate KNOWN-RECIPE (a human recipe exists) from AGENT-DEMONSTRATED (an agent found, integrated and validated it unaided within a comparable budget).
   - attack_basis is DEMONSTRATED-AGENT only for the latter, LITERATURE-ONLY when only a human recipe exists, and ASSUMED when neither exists.
   - Only DEMONSTRATED-AGENT justifies a high attack score. Where only a recipe exists, score what an agent must still discover, integrate and validate in 12 h, and say that the verdict rests on assumption.
   - Don't reflexively lower everything. Where agents have demonstrated the capability, score high.
3. **Subfield SOTA:** find the subfield's best known human or system result, with its source and year, and anchor the task's north star (R≈1 or the reference R) to it.
4. **Anchored estimate:** give the ANCHORED estimate and verdict. This is an **upper bound** on survival, not the promotion decision.
5. **Strict (the gate):** if attack_basis is LITERATURE-ONLY or ASSUMED, the STRICT verdict and scores are the section-4 (evidence-only / pre-anchoring) ones — treat that attack as executable by a 12-hour frontier agent. Only DEMONSTRATED-AGENT evidence may lower an attack score below that estimate; in that case STRICT equals ANCHORED. A task that survives only in the anchored reading is not promoted.

WRITE {{OUT_DIR}}/audit_card.md with these sections (about 700–1300 words, hand-written):
# {{TASK_ID}}: <task title>: anchored re-score
## 1. What the screen claimed
The old attack, numbers, verdict, kill reason and cited URLs.
## 2. Evidence audit
For each load-bearing attack component: is there current, comparable-setup evidence? Name the gap precisely. Grade the evidence WELL-SUPPORTED, PARTIAL or ASSUMED.
## 3. Research done now
At least 3 newly consulted sources, each as: "- <title> — <author/org>, <year> — <URL> — fetched|search-only — <what it shows for THIS task; raises/lowers the attack>". Include evidence against the attack.
## 4. Re-estimated attack
Component derivation, the spread, then ESTIMATED single (point + range), best-of-4, pass@4 and ub95, with the arithmetic.
## 4A. Demonstrated capability and subfield SOTA
- Subfield SOTA, and how the north star is anchored to it.
- At least 2 demonstrated agent results, each with model + scaffold, time and compute, what was achieved, and the gap. Describe each benchmark only through its relevance to this task.
- The KNOWN-RECIPE vs AGENT-DEMONSTRATED analysis, attack_basis, and what an agent would have to do in 12 h that no agent has been shown to do.
- ANCHORED estimate: single (point + range), bo4, pass@4 and ub95, ESTIMATED, plus whether the verdict rests on assumption.
## 5. Verdict under the kill lines
The section-4 (evidence-only) verdict, the ANCHORED verdict (upper bound on survival), and the STRICT verdict (the promotion gate), each with its binding line and margin. Also the flip of the anchored verdict against the screen's verdict, and the flip of the strict verdict against both, with the reason.
## 6. Redesign
Judge this using the STRICT verdict (the promotion gate). Still report the anchored verdict as the upper bound. For a strict CUT, redesign unless the task is a duplicate or has a souping dependency. Classify the kill cause:
- (a) a mature-stack attack;
- (b) a grader optimizable by search;
- (c) leaked semantics;
- (d) other.

Then propose a concrete redesign that stays real frontier R&D. It must not work by hiding needed information, adding noise or crippling feasibility. Give its ESTIMATED re-attack and the attack basis. Mark the result REDESIGNABLE or TRULY-DEAD.
## 7. Measurement status
Rollouts, grader noise and score ladder: all UNMEASURED, with the planned measurement for each.
## Audit record
(one per line; numbers ESTIMATED; "na" where not applicable)
id: {{TASK_ID}}
old_verdict: PASS-SCREEN|CONDITIONAL|CUT|na
evidence_grade: WELL-SUPPORTED|PARTIAL|ASSUMED
new_single: 0.xx
new_single_range: 0.xx-0.xx
new_bo4: 0.xx
new_pass4: 0.xx
new_ub95: 0.xx
new_verdict: PASS-SCREEN|CONDITIONAL|CUT
binding_line: single>0.70|bo4>0.60|pass4>0.50|ub95>=0.75|none|duplicate|souping
attack_basis: DEMONSTRATED-AGENT|LITERATURE-ONLY|ASSUMED
demonstrated_ref: <short: benchmark/system, model, year; ';'-separated>
gap_to_attack: <one short phrase>
subfield_sota_ref: <short: result, source, year>
anchored_single: 0.xx
anchored_bo4: 0.xx
anchored_pass4: 0.xx
anchored_ub95: 0.xx
anchored_verdict: PASS-SCREEN|CONDITIONAL|CUT
anchored_binding_line: single>0.70|bo4>0.60|pass4>0.50|ub95>=0.75|none|duplicate|souping
anchored_flip: none|CUT->CONDITIONAL|CUT->PASS-SCREEN|CONDITIONAL->PASS-SCREEN|CONDITIONAL->CUT|PASS-SCREEN->CONDITIONAL|PASS-SCREEN->CUT
strict_verdict: PASS-SCREEN|CONDITIONAL|CUT
strict_binding_line: single>0.70|bo4>0.60|pass4>0.50|ub95>=0.75|none|duplicate|souping
# strict_verdict equals new_verdict when attack_basis is LITERATURE-ONLY or ASSUMED;
# it equals anchored_verdict only when attack_basis is DEMONSTRATED-AGENT.
verdict_rests_on_assumption: yes|no
redesign_status: REDESIGNABLE|TRULY-DEAD|DUPLICATE-STAYS-CUT|NOT-NEEDED
redesign_oneline: <one sentence or na>
redesign_attack_basis: DEMONSTRATED-AGENT|LITERATURE-ONLY|ASSUMED|na
souping_flag: no|yes
