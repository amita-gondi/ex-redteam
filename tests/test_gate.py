from redteam.gate import strict_gate
from redteam.killlines import KillLines

L = KillLines()


def mk_screen(v="CONDITIONAL", **s):
    sc = {"single": 0.45, "bo4": 0.57, "pass4": 0.30, "ub95": 0.68}
    sc.update(s)
    return {"verdict": v, "scores": sc, "souping": "no"}


def mk_anchored(basis, ev_v, anc_v, souping="no"):
    return {"evidence_only_verdict": ev_v,
            "evidence_only_scores": {"single": 0.45, "bo4": 0.57, "pass4": 0.30, "ub95": 0.68},
            "anchored_verdict": anc_v,
            "anchored_scores": {"single": 0.30, "bo4": 0.45, "pass4": 0.10, "ub95": 0.55},
            "attack_basis": basis, "written_strict_verdict": None, "souping": souping}


def test_literature_only_uses_preanchoring_not_anchored():
    r = strict_gate(mk_screen("CONDITIONAL"), mk_anchored("LITERATURE-ONLY", "CONDITIONAL", "PASS-SCREEN"), L)
    assert r["strict_verdict"] == "CONDITIONAL"       # the gate
    assert r["anchored_verdict"] == "PASS-SCREEN"      # upper bound, not the gate
    assert "LITERATURE-ONLY" in r["strict_source"]
    assert r["advance"] is True
    assert r["flip_strict_vs_anchored"] == "PASS-SCREEN->CONDITIONAL"


def test_assumed_also_uses_preanchoring():
    r = strict_gate(mk_screen("CUT"), mk_anchored("ASSUMED", "CUT", "PASS-SCREEN"), L)
    assert r["strict_verdict"] == "CUT"
    assert r["anchored_verdict"] == "PASS-SCREEN"
    assert r["advance"] is False


def test_demonstrated_agent_may_lower_strict_to_anchored():
    r = strict_gate(mk_screen("CUT"), mk_anchored("DEMONSTRATED-AGENT", "CUT", "CONDITIONAL"), L)
    assert r["strict_verdict"] == "CONDITIONAL"       # anchored is allowed to lower it here
    assert "DEMONSTRATED-AGENT" in r["strict_source"]


def test_souping_forces_cut():
    r = strict_gate(mk_screen("CONDITIONAL"), mk_anchored("LITERATURE-ONLY", "CONDITIONAL", "PASS-SCREEN", souping="yes"), L)
    assert r["strict_verdict"] == "CUT"
    assert any("souping" in n for n in r["notes"])


def test_unknown_basis_is_conservative():
    r = strict_gate(mk_screen("CONDITIONAL"), mk_anchored(None, "CONDITIONAL", "PASS-SCREEN"), L)
    assert r["strict_verdict"] == "CONDITIONAL"       # harsher of the two
    assert any("attack_basis" in n for n in r["notes"])


def test_reported_strict_disagreement_noted_but_computed_used():
    anc = mk_anchored("LITERATURE-ONLY", "CONDITIONAL", "PASS-SCREEN")
    anc["written_strict_verdict"] = "PASS-SCREEN"
    r = strict_gate(mk_screen("CONDITIONAL"), anc, L)
    assert r["strict_verdict"] == "CONDITIONAL"
    assert any("record wrote strict_verdict" in n for n in r["notes"])
