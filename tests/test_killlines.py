import math

from redteam.killlines import (
    KillLines,
    binding_line,
    breaches,
    clopper_pearson,
    mean_upper95,
    numeric_verdict,
    pass_at_k,
    pass_at_k_upper,
    t_ppf,
)

L = KillLines()


def test_clopper_pearson_known_bounds():
    # method/kill_thresholds.md: a panel can kill but not clear.
    assert clopper_pearson(0, 4)[1] == pytest_approx(0.6024, 1e-3)
    assert clopper_pearson(0, 16)[1] == pytest_approx(0.2059, 1e-3)
    assert pass_at_k_upper(0, 4) == pytest_approx(0.975, 1e-3)
    assert pass_at_k_upper(0, 16) == pytest_approx(0.6024, 1e-3)
    assert pass_at_k_upper(0, 24) == pytest_approx(0.459, 1e-2)


def test_clopper_pearson_two_sided():
    lo, hi = clopper_pearson(3, 10)
    assert lo == pytest_approx(0.0667, 1e-2)
    assert hi == pytest_approx(0.6525, 1e-2)
    assert clopper_pearson(0, 4) == (0.0, clopper_pearson(0, 4)[1])
    assert clopper_pearson(4, 4)[1] == 1.0


def test_t_quantile_n4():
    assert t_ppf(0.975, 3) == pytest_approx(3.1824, 1e-3)


def test_mean_upper95():
    assert mean_upper95([0.5, 0.5, 0.5, 0.5]) == pytest_approx(0.5, 1e-9)
    hi = mean_upper95([0.4, 0.5, 0.6, 0.7])
    mu = 0.55
    sd = math.sqrt(sum((v - mu) ** 2 for v in [0.4, 0.5, 0.6, 0.7]) / 3)
    assert hi == pytest_approx(mu + 3.1824 * sd / 2, 1e-3)


def test_pass_at_k():
    assert pass_at_k(0.0) == 0.0
    assert pass_at_k(1.0) == 1.0
    assert pass_at_k(0.1) == pytest_approx(1 - 0.9 ** 4)


def test_breaches_asymmetry_ub95_vs_others():
    # ub95 kills AT the line (>=); the other three only ABOVE (>).
    assert breaches({"single": 0.70, "bo4": 0.60, "pass4": 0.50, "ub95": 0.74}, L) == []
    assert breaches({"ub95": 0.75}, L) == ["ub95"]
    assert breaches({"single": 0.701}, L) == ["single"]
    assert breaches({"bo4": 0.61}, L) == ["bo4"]


def test_numeric_verdict():
    assert numeric_verdict({"single": 0.80, "bo4": 0.50, "pass4": 0.40, "ub95": 0.70}, L) == "CUT"
    assert numeric_verdict({"single": 0.45, "bo4": 0.57, "pass4": 0.30, "ub95": 0.68}, L) == "CONDITIONAL"
    assert numeric_verdict({"single": 0.30, "bo4": 0.40, "pass4": 0.20, "ub95": 0.55}, L) == "PASS-SCREEN"
    assert numeric_verdict({"single": 0.45}, L) is None  # incomplete


def test_binding_line():
    assert binding_line({"single": 0.80, "bo4": 0.50, "pass4": 0.40, "ub95": 0.70}, L).startswith("single")
    assert binding_line({"single": 0.45, "bo4": 0.59, "pass4": 0.30, "ub95": 0.55}, L) == "bo4>0.60"


def test_override_needs_reason():
    import pytest
    with pytest.raises(ValueError):
        KillLines.from_dicts(None, {"single_max": 0.8})
    kl = KillLines.from_dicts(None, {"single_max": 0.8, "override_reason": "harder task"})
    assert kl.single_max == 0.8 and kl.overridden == ["single_max"]


def pytest_approx(v, rel=1e-6):
    import pytest
    return pytest.approx(v, rel=rel)
