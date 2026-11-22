"""Stage definitions. Desk stages run an agent; local stages are pure computation."""
from __future__ import annotations

from dataclasses import dataclass, field

from .records import norm_enum, norm_verdict, norm_yesno, num, num_range

SCREEN_KEYS = ["id", "verdict", "binding_line", "attack_single_est", "attack_single_range", "bo4_est", "pass4_est",
               "ub95_est", "gpuh_new_est", "duplicate_of", "kill_reason", "souping_flag"]
AUDIT_KEYS = ["id", "old_verdict", "evidence_grade", "new_single", "new_single_range", "new_bo4", "new_pass4", "new_ub95",
              "new_verdict", "binding_line", "attack_basis", "demonstrated_ref", "gap_to_attack", "subfield_sota_ref",
              "anchored_single", "anchored_bo4", "anchored_pass4", "anchored_ub95", "anchored_verdict",
              "anchored_binding_line", "anchored_flip", "strict_verdict", "strict_binding_line",
              "verdict_rests_on_assumption", "redesign_status", "redesign_oneline", "redesign_attack_basis", "souping_flag"]
REDTEAM_KEYS = ["id", "verdict", "strongest_attack", "combined_recipe_attack", "best_of_4", "pass_at_4", "single_run_max",
                "upper95_projected", "kill_line_breached", "attack_basis", "demonstrated_ref", "gap_to_attack",
                "subfield_sota_ref", "decisive_gpu_h", "required_fixes", "main_kill_reason", "duplicate_of", "souping_flag"]
PROBE_KEYS = ["id", "mode", "findings_total", "findings_high", "findings_medium", "findings_low", "blocks_panel",
              "hidden_data_reachable", "top_finding", "findings", "defences_held", "counts_toward_saturation", "souping_flag"]
BASES = ["DEMONSTRATED-AGENT", "LITERATURE-ONLY", "ASSUMED"]


@dataclass
class DeskStage:
    name: str
    prompt: str
    report: str
    record_names: list
    known_keys: list
    requires: list = field(default_factory=list)
    blind: bool = False          # must never see prior verdicts
    probe_mode: str | None = None


DESK = {
    "screen": DeskStage("screen", "screen.md", "screen_card.md", ["screen"], SCREEN_KEYS),
    "anchored_rescore": DeskStage("anchored_rescore", "anchored_rescore.md", "audit_card.md", ["audit", "anchored"],
                                  AUDIT_KEYS, requires=["screen"]),
    "redteam": DeskStage("redteam", "redteam.md", "redteam.md", ["verdict"], REDTEAM_KEYS, blind=True),
    "probe_blackbox": DeskStage("probe_blackbox", "probe_blackbox.md", "probe_blackbox.md", ["probe"], PROBE_KEYS,
                                blind=True, probe_mode="blackbox"),
    "probe_whitebox": DeskStage("probe_whitebox", "probe_whitebox.md", "probe_whitebox.md", ["probe"], PROBE_KEYS,
                                blind=True, probe_mode="whitebox"),
}
LOCAL = ["validate", "strict_gate", "aggregate", "index"]
ORDER = ["validate", "screen", "anchored_rescore", "strict_gate", "redteam", "probe_blackbox", "probe_whitebox",
         "aggregate", "index"]
GATED = ["canary", "panel"]
ALL = ORDER + GATED
OUTCOME = {"PASS-SCREEN": "ADVANCE", "HOLDS": "ADVANCE", "CONDITIONAL": "FIX", "FIX": "FIX", "CUT": "CUT"}
SEVERITY_RANK = {"CUT": 2, "FIX": 1, "ADVANCE": 0}


def interpret(stage: str, rec: dict) -> dict:
    """Normalise a parsed record into typed fields. Missing/unfilled values become None."""
    if stage == "screen":
        return {"verdict": norm_verdict(rec.get("verdict")),
                "scores": {"single": num(rec.get("attack_single_est")), "bo4": num(rec.get("bo4_est")),
                           "pass4": num(rec.get("pass4_est")), "ub95": num(rec.get("ub95_est"))},
                "single_range": num_range(rec.get("attack_single_range")),
                "binding_line": rec.get("binding_line"), "souping": norm_yesno(rec.get("souping_flag"))}
    if stage == "anchored_rescore":
        return {"old_verdict": norm_verdict(rec.get("old_verdict")),
                "evidence_only_verdict": norm_verdict(rec.get("new_verdict")),
                "evidence_only_scores": {"single": num(rec.get("new_single")), "bo4": num(rec.get("new_bo4")),
                                         "pass4": num(rec.get("new_pass4")), "ub95": num(rec.get("new_ub95"))},
                "anchored_verdict": norm_verdict(rec.get("anchored_verdict")),
                "anchored_scores": {"single": num(rec.get("anchored_single")), "bo4": num(rec.get("anchored_bo4")),
                                    "pass4": num(rec.get("anchored_pass4")), "ub95": num(rec.get("anchored_ub95"))},
                "attack_basis": norm_enum(rec.get("attack_basis"), BASES),
                "written_strict_verdict": norm_verdict(rec.get("strict_verdict")),
                "rests_on_assumption": norm_yesno(rec.get("verdict_rests_on_assumption")),
                "redesign_status": rec.get("redesign_status"), "souping": norm_yesno(rec.get("souping_flag"))}
    if stage == "redteam":
        return {"verdict": norm_verdict(rec.get("verdict")),
                "scores": {"single": num(rec.get("single_run_max")), "bo4": num(rec.get("best_of_4")),
                           "pass4": num(rec.get("pass_at_4")), "ub95": num(rec.get("upper95_projected"))},
                "combined_recipe": num(rec.get("combined_recipe_attack")),
                "attack_basis": norm_enum(rec.get("attack_basis"), BASES),
                "kill_line_breached": rec.get("kill_line_breached"), "required_fixes": rec.get("required_fixes"),
                "souping": norm_yesno(rec.get("souping_flag"))}
    if stage.startswith("probe_"):
        def i(k):
            v = num(rec.get(k))
            return int(v) if v is not None else None
        return {"mode": (rec.get("mode") or "").strip().lower() or None, "findings_total": i("findings_total"),
                "high": i("findings_high"), "medium": i("findings_medium"), "low": i("findings_low"),
                "blocks_panel": norm_yesno(rec.get("blocks_panel")),
                "hidden_data_reachable": norm_yesno(rec.get("hidden_data_reachable")),
                "top_finding": rec.get("top_finding"), "findings": rec.get("findings"),
                "souping": norm_yesno(rec.get("souping_flag"))}
    return {}


def primary_verdict(stage: str, info: dict) -> str | None:
    if stage in ("screen", "redteam"):
        return info.get("verdict")
    if stage == "anchored_rescore":
        return info.get("anchored_verdict")
    if stage.startswith("probe_"):
        return "FINDINGS" if info.get("findings_total") is not None else None
    return None
