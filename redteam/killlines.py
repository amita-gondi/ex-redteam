"""Kill-line math (method/kill_thresholds.md). Pure functions, stdlib only.

Kill lines (defaults; a task may override them with a reason):
  single run > 0.70, best-of-4 > 0.60, pass@4 at R >= tau > 0.50, upper-95% >= 0.75.
Note the asymmetry: ub95 kills AT the line (>=); the other three only ABOVE it (>).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

DEFAULT_LINES = {"single_max": 0.70, "best_of_4": 0.60, "pass_at_4": 0.50, "upper95": 0.75, "tau": 0.60}
# Key used in records -> (config key, kills at equality?)
LINE_KEYS = {"single": ("single_max", False), "bo4": ("best_of_4", False),
             "pass4": ("pass_at_4", False), "ub95": ("upper95", True)}
LINE_LABEL = {"single": "single>{:.2f}", "bo4": "bo4>{:.2f}", "pass4": "pass4>{:.2f}", "ub95": "ub95>={:.2f}"}
CONDITIONAL_MARGIN = 0.05   # screen prompt: PASS-SCREEN needs a margin of more than ~0.05 on all four lines


@dataclass
class KillLines:
    single_max: float = 0.70
    best_of_4: float = 0.60
    pass_at_4: float = 0.50
    upper95: float = 0.75
    tau: float = 0.60
    override_reason: str | None = None
    overridden: list = field(default_factory=list)

    @classmethod
    def from_dicts(cls, defaults: dict | None, override: dict | None = None) -> KillLines:
        base = dict(DEFAULT_LINES)
        base.update({k: float(v) for k, v in (defaults or {}).items() if k in DEFAULT_LINES})
        changed = []
        reason = None
        if override:
            reason = (override.get("override_reason") or "").strip() or None
            for k in DEFAULT_LINES:
                if k in override and override[k] is not None and float(override[k]) != base[k]:
                    changed.append(k)
                    base[k] = float(override[k])
            if changed and not reason:
                raise ValueError(f"kill_thresholds override of {changed} needs a non-empty override_reason")
        return cls(**base, override_reason=reason, overridden=changed)

    def threshold(self, key: str) -> float:
        return getattr(self, LINE_KEYS[key][0])

    def label(self, key: str) -> str:
        return LINE_LABEL[key].format(self.threshold(key))

    def as_text(self) -> str:
        return (f"single run > {self.single_max:.2f}; best-of-4 > {self.best_of_4:.2f}; "
                f"pass@4 at R >= {self.tau:.2f} > {self.pass_at_4:.2f}; upper-95% >= {self.upper95:.2f}")

    def to_dict(self) -> dict:
        d = {k: getattr(self, k) for k in DEFAULT_LINES}
        if self.overridden:
            d["overridden"] = list(self.overridden)
            d["override_reason"] = self.override_reason
        return d


def breaches(scores: dict, lines: KillLines) -> list[str]:
    """Lines crossed by an ESTIMATED score set {single, bo4, pass4, ub95}. Missing scores are ignored."""
    out = []
    for k, (_, at_eq) in LINE_KEYS.items():
        v = scores.get(k)
        if v is None:
            continue
        t = lines.threshold(k)
        if (v >= t) if at_eq else (v > t):
            out.append(k)
    return out


def margins(scores: dict, lines: KillLines) -> dict:
    """Signed clearance threshold - score per line (positive = below the line)."""
    return {k: round(lines.threshold(k) - scores[k], 4) for k in LINE_KEYS if scores.get(k) is not None}


def numeric_verdict(scores: dict, lines: KillLines, margin: float = CONDITIONAL_MARGIN) -> str | None:
    """The screen verdict the four numbers alone imply. Recorded verdicts may differ for structural reasons
    (duplicate, souping, a named design condition); callers report mismatches, they don't overwrite."""
    if not all(scores.get(k) is not None for k in LINE_KEYS):
        return None
    if breaches(scores, lines):
        return "CUT"
    m = margins(scores, lines)
    # ub95 kills at equality, so a 0.00 margin on ub95 is already a breach (handled above).
    if min(m.values()) <= margin:
        return "CONDITIONAL"
    return "PASS-SCREEN"


def binding_line(scores: dict, lines: KillLines) -> str:
    m = margins(scores, lines)
    if not m:
        return "na"
    b = breaches(scores, lines)
    if b:
        return "+".join(lines.label(k) for k in b)
    k = min(m, key=m.get)
    return lines.label(k)


def pass_at_k(p: float, k: int = 4) -> float:
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must be in [0, 1]")
    return 1.0 - (1.0 - p) ** k


# ---------------------------------------------------------------- exact intervals (no scipy)
def _betacf(a: float, b: float, x: float) -> float:
    # Continued fraction for the incomplete beta (Numerical Recipes, Lentz's method).
    tiny, eps = 1e-300, 3e-16
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 500):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        de = d * c
        h *= de
        if abs(de - 1.0) < eps:
            break
    return h


def betainc(a: float, b: float, x: float) -> float:
    """Regularized incomplete beta I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbt = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x)
    bt = math.exp(lbt)
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1.0 - x) / b


def _bisect(f, lo: float, hi: float, target: float, it: int = 200) -> float:
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        if f(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def beta_ppf(q: float, a: float, b: float) -> float:
    return _bisect(lambda x: betainc(a, b, x), 0.0, 1.0, q)


def clopper_pearson(x: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Exact two-sided (1 - alpha) interval for a binomial proportion (method/rollout_spec.md, section 5)."""
    if n <= 0 or not 0 <= x <= n:
        raise ValueError("need 0 <= x <= n, n > 0")
    lo = 0.0 if x == 0 else beta_ppf(alpha / 2, x, n - x + 1)
    hi = 1.0 if x == n else beta_ppf(1 - alpha / 2, x + 1, n - x)
    return lo, hi


def pass_at_k_upper(x: int, n: int, k: int = 4, alpha: float = 0.05) -> float:
    """Upper bound on pass@k implied by the Clopper-Pearson upper bound on the per-run pass rate."""
    return pass_at_k(clopper_pearson(x, n, alpha)[1], k)


def t_cdf(t: float, df: float) -> float:
    x = df / (df + t * t)
    p = 0.5 * betainc(df / 2.0, 0.5, x)
    return 1.0 - p if t > 0 else p


def t_ppf(q: float, df: float) -> float:
    return _bisect(lambda t: t_cdf(t, df), -1e3, 1e3, q)


def mean_upper95(values: list[float]) -> float:
    """Two-sided 95% t-interval upper end on a mean: mean + t_{0.975, n-1} * SD / sqrt(n). At n = 4, t = 3.18."""
    n = len(values)
    if n < 2:
        raise ValueError("need at least 2 values")
    mu = sum(values) / n
    sd = math.sqrt(sum((v - mu) ** 2 for v in values) / (n - 1))
    return mu + t_ppf(0.975, n - 1) * sd / math.sqrt(n)
