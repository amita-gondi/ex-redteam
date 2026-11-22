"""Strict promotion gate and the aggregate verdict.

STRICT rule (Amita, Nov 21 2026, 3:02 PM PT; method/evidence_grounding_rule.md section 5):
  - attack_basis LITERATURE-ONLY or ASSUMED -> the evidence-only / pre-anchoring scores and verdict are the gate
    (treat that attack as executable by a 12-hour frontier agent);
  - only DEMONSTRATED-AGENT evidence may lower an attack score below that: then strict = anchored;
  - unknown basis -> the harsher of the two (conservative);
  - the anchored verdict is kept as an UPPER BOUND on survival, never the gate.
"""
from __future__ import annotations

from .killlines import KillLines, binding_line, breaches, margins, numeric_verdict
from .stages import OUTCOME, SEVERITY_RANK

HARSH = {"CUT": 2, "CONDITIONAL": 1, "PASS-SCREEN": 0}


def harsher(a: str | None, b: str | None) -> str | None:
    if a is None:
        return b
    if b is None:
        return a
    return a if HARSH.get(a, 0) >= HARSH.get(b, 0) else b


def flip(a: str | None, b: str | None) -> str:
    if not a or not b:
        return "na"
    return "none" if a == b else f"{a}->{b}"


def strict_gate(screen: dict, anchored: dict, lines: KillLines) -> dict:
    """screen/anchored: interpreted records (stages.interpret). Returns the strict_gate result."""
    basis = anchored.get("attack_basis")
    pre_v = anchored.get("evidence_only_verdict") or screen.get("verdict")
    pre_s = anchored.get("evidence_only_scores") or {}
    if not any(v is not None for v in pre_s.values()):
        pre_s = screen.get("scores") or {}
        pre_src = "screen (no evidence-only scores in the re-score)"
    else:
        pre_src = "evidence-only (re-score section 4)"
    anc_v = anchored.get("anchored_verdict")
    anc_s = anchored.get("anchored_scores") or {}
    notes = []
    if basis == "DEMONSTRATED-AGENT":
        sv, ss, src = anc_v, anc_s, "anchored (DEMONSTRATED-AGENT evidence may lower the attack)"
    elif basis in ("LITERATURE-ONLY", "ASSUMED"):
        sv, ss, src = pre_v, pre_s, f"{pre_src}; attack_basis {basis} is treated as executable by a 12-hour frontier agent"
    else:
        sv = harsher(pre_v, anc_v)
        ss = pre_s if sv == pre_v else anc_s
        src = "unknown attack_basis: harsher of pre-anchoring and anchored (conservative)"
        notes.append("attack_basis missing or unrecognised")
    written = anchored.get("written_strict_verdict")
    if written and sv and written != sv:
        notes.append(f"record wrote strict_verdict={written}; the gate uses the computed {sv}")
    if screen.get("souping") == "yes" or anchored.get("souping") == "yes":
        sv = "CUT"
        notes.append("souping_flag yes: CUT (souping/merging excluded entirely)")
    num_v = numeric_verdict(ss, lines) if ss else None
    if num_v and sv and num_v != sv:
        notes.append(f"the strict scores alone imply {num_v}; the recorded verdict {sv} is kept "
                     "(recorded verdicts may be structural: duplicate, souping, a named design condition)")
    if anc_v and sv and HARSH.get(anc_v, 0) > HARSH.get(sv, 0):
        notes.append(f"anchored ({anc_v}) is harsher than strict ({sv}); an upper bound on survival should not be")
    return {
        "rule": "strict",
        "attack_basis": basis,
        "strict_verdict": sv,
        "strict_source": src,
        "strict_scores": ss,
        "strict_breaches": breaches(ss, lines) if ss else [],
        "strict_margins": margins(ss, lines) if ss else {},
        "strict_binding_line": binding_line(ss, lines) if ss else "na",
        "anchored_verdict": anc_v,
        "anchored_scores": anc_s,
        "anchored_is": "upper bound on survival (not the gate)",
        "screen_verdict": screen.get("verdict"),
        "flip_strict_vs_anchored": flip(anc_v, sv),
        "flip_strict_vs_screen": flip(screen.get("verdict"), sv),
        "flip_anchored_vs_screen": flip(screen.get("verdict"), anc_v),
        "outcome": OUTCOME.get(sv or "", "UNKNOWN"),
        "advance": sv in ("PASS-SCREEN", "CONDITIONAL"),
        "notes": notes,
        "label": "ESTIMATED desk verdict, UNMEASURED",
    }


def aggregate(strict: dict | None, redteam: dict | None, probes: dict, skipped: list) -> dict:
    """Combine stage results. Saturation verdict = the worse of the strict gate and the red team.
    Probe findings are reported separately, tagged by mode, and NEVER counted toward saturation metrics;
    a high-severity finding (or blocks_panel: yes) only sets environment_fix_required."""
    parts = []
    if strict and strict.get("strict_verdict"):
        parts.append(("strict_gate", OUTCOME.get(strict["strict_verdict"], "UNKNOWN")))
    if redteam and redteam.get("verdict"):
        parts.append(("redteam", OUTCOME.get(redteam["verdict"], "UNKNOWN")))
    sat = None
    if parts:
        sat = max((p[1] for p in parts), key=lambda o: SEVERITY_RANK.get(o, 3))
    env_fix = False
    by_mode = {}
    for name, info in sorted(probes.items()):
        if not info:
            continue
        mode = info.get("mode") or name.replace("probe_", "")
        by_mode.setdefault(mode, []).append({
            "stage": name, "high": info.get("high"), "medium": info.get("medium"), "low": info.get("low"),
            "blocks_panel": info.get("blocks_panel"), "hidden_data_reachable": info.get("hidden_data_reachable"),
            "top_finding": info.get("top_finding"), "findings": info.get("findings")})
        if (info.get("high") or 0) > 0 or info.get("blocks_panel") == "yes" or info.get("hidden_data_reachable") == "yes":
            env_fix = True
    complete = sat is not None and "UNKNOWN" not in [p[1] for p in parts]
    overall = sat if complete else "INCOMPLETE"
    if complete and sat == "ADVANCE" and env_fix:
        overall = "FIX"
    return {
        "saturation_outcome": sat,
        "saturation_parts": dict(parts),
        "strict_verdict": (strict or {}).get("strict_verdict"),
        "anchored_verdict_upper_bound": (strict or {}).get("anchored_verdict"),
        "redteam_verdict": (redteam or {}).get("verdict"),
        "probe_findings_by_mode": by_mode,
        "probe_findings_count_toward_saturation": False,
        "environment_fix_required": env_fix,
        "outcome": overall,
        "skipped_stages": skipped,
        "meaning": ("ADVANCE = the next step may look at the task (never 'cleared'); FIX = redesign/fix before any GO; "
                    "CUT = drop or redesign. Desk only: rollouts UNMEASURED; a 4x4 panel can kill but not clear."),
        "label": "ESTIMATED desk verdict, UNMEASURED",
    }
