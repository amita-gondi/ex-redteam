"""Tolerant parser for the machine-readable record block at the end of a desk report.

Desk agents mostly write `key: value` lines under a fixed heading, but the format drifts:
heading level/case ("## Screen record", "### screen Record", "**Audit record**"), code fences,
bullets, bold or backticked keys, `=` instead of `:`, table rows `| key | value |`, en dashes,
"ESTIMATED 0.67 (0.47–0.87)" values, CRLF line ends. This parser accepts all of those.
If the heading is missing entirely it falls back to scanning the tail of the file for known keys.
"""
from __future__ import annotations

import re
from collections.abc import Iterable

_HEADING = r"(?:#{1,6}\s*|\*\*\s*|__\s*)?(?:the\s+)?(NAMES)\s+record\b"
_KEY_LINE = re.compile(
    r"""^\s*(?:[-*+]\s+|\d+[.)]\s+)?      # optional bullet or number
        (?:\*\*|__|`)?\s*                 # optional bold/backtick open
        ([A-Za-z][A-Za-z0-9 _@\-]{0,60}?)  # key
        \s*(?:\*\*|__|`)?\s*              # optional close
        (?:[:=]|\s[\u2012\u2013\u2014\u2212]\s)\s*(?:\*\*|__|`)?\s*   # separator (colon/equals or spaced en/em dash)
        (.*?)\s*$""", re.X)
_TABLE_LINE = re.compile(r"^\s*\|\s*`?([A-Za-z][A-Za-z0-9 _@\-]{0,60}?)`?\s*\|\s*(.*?)\s*\|\s*$")
_NUM = re.compile(r"-?\d+(?:\.\d+)?")
DASHES = dict.fromkeys(map(ord, "\u2010\u2011\u2012\u2013\u2014\u2212"), "-")


def norm_key(k: str) -> str:
    k = k.strip().strip("*_`").strip().lower()
    k = re.sub(r"[\s\-@]+", "_", k)
    return re.sub(r"_+", "_", k).strip("_")


def clean_value(v: str) -> str:
    v = v.translate(DASHES).strip()
    v = re.sub(r"^(\*\*|__|`)+|(\*\*|__|`)+$", "", v).strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1].strip()
    return v


def find_block(text: str, names: Iterable[str]) -> str | None:
    """Return the text after the LAST matching record heading (agents sometimes quote the template earlier)."""
    pat = re.compile(_HEADING.replace("NAMES", "|".join(re.escape(n) for n in names)), re.I)
    last = None
    for m in pat.finditer(text):
        line_start = text.rfind("\n", 0, m.start()) + 1
        prefix = text[line_start:m.start()]
        if prefix.strip() == "":
            last = m
    if last is None:
        return None
    nl = text.find("\n", last.end())
    return "" if nl == -1 else text[nl + 1:]


def _parse_lines(lines: Iterable[str], known: set | None, stop_at_heading: bool) -> dict:
    out: dict = {}
    seen_any = False
    for raw in lines:
        line = raw.rstrip("\r")
        s = line.strip()
        if not s or s.startswith("```") or s.startswith("~~~") or re.fullmatch(r"\|?[\s:\-|]+\|?", s):
            continue
        if stop_at_heading and seen_any and re.match(r"^#{1,3}\s+[A-Z0-9]", s):
            break   # next real section (capitalised heading); "# comment" lines inside the block are lowercase
        if s.startswith("#") and not re.match(r"^#{1,6}\s*[A-Za-z][\w ]*[:=]", s):
            continue
        m = _TABLE_LINE.match(line) or _KEY_LINE.match(s.lstrip("#").strip() if s.startswith("#") else line)
        if not m:
            continue
        key = norm_key(m.group(1))
        if key in ("key", "field") or not key:
            continue
        if known is not None and key not in known:
            continue
        val = clean_value(m.group(2))
        if key not in out:          # first occurrence wins inside the block
            out[key] = val
            seen_any = True
    return out


def parse_record(text: str, names: Iterable[str], known_keys: Iterable[str] | None = None,
                 tail_lines: int = 120) -> tuple[dict, str]:
    """Parse a record block. Returns (fields, how) with how in {"heading", "fallback-tail", "none"}."""
    text = (text or "").replace("\r\n", "\n")
    known = set(known_keys) if known_keys else None
    block = find_block(text, names)
    if block is not None:
        rec = _parse_lines(block.splitlines(), known, stop_at_heading=True)
        if rec:
            return rec, "heading"
    if known:
        rec = _parse_lines(text.splitlines()[-tail_lines:], known, stop_at_heading=False)
        if len(rec) >= 3:
            return rec, "fallback-tail"
    return {}, "none"


# ---------------------------------------------------------------- value normalisation
VERDICT_ALIASES = {
    "PASS-SCREEN": "PASS-SCREEN", "PASS_SCREEN": "PASS-SCREEN", "PASS SCREEN": "PASS-SCREEN", "PASSSCREEN": "PASS-SCREEN",
    "PASS": "PASS-SCREEN", "CONDITIONAL": "CONDITIONAL", "COND": "CONDITIONAL", "CUT": "CUT", "KILL": "CUT",
    "HOLDS": "HOLDS", "HOLD": "HOLDS", "FIX": "FIX", "NEEDS FIX": "FIX", "NEEDS FIXES": "FIX",
}


def norm_verdict(v: str | None) -> str | None:
    """'CONDITIONAL | binding bo4' -> CONDITIONAL; '**Pass-screen**' -> PASS-SCREEN. Template text
    with several alternatives ('PASS-SCREEN|CONDITIONAL|CUT') is rejected (returns None)."""
    if not v:
        return None
    s = clean_value(v).upper()
    if s.count("|") >= 2 and all(p.strip() in VERDICT_ALIASES for p in s.split("|")):
        return None   # unfilled template
    s = re.split(r"[|(;,]| - | \u2014 ", s)[0].strip().rstrip(".")
    s = re.sub(r"\s+", " ", s)
    if s in VERDICT_ALIASES:
        return VERDICT_ALIASES[s]
    first = s.split(" ")[0]
    return VERDICT_ALIASES.get(first)


def num(v) -> float | None:
    """First number in a value: 'ESTIMATED 0.67 (0.47-0.87)' -> 0.67; '0.xx' -> None."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    cv = clean_value(str(v)).replace("ESTIMATED", "")
    if re.search(r"\d*\.?x+|\bN\b|<", cv):   # unfilled template (0.xx, 0.x, N, <...>)
        return None
    m = _NUM.search(cv)
    return float(m.group()) if m else None


def num_range(v) -> tuple[float, float] | None:
    if v is None:
        return None
    nums = re.findall(r"\d+(?:\.\d+)?", clean_value(str(v)).replace("ESTIMATED", ""))
    if len(nums) >= 3:      # 'ESTIMATED 0.67 (0.47-0.87)': point then range
        return float(nums[1]), float(nums[2])
    if len(nums) == 2:
        return float(nums[0]), float(nums[1])
    return None


def norm_enum(v: str | None, allowed: Iterable[str]) -> str | None:
    if not v:
        return None
    s = clean_value(v).upper().replace("_", "-")
    s = re.split(r"[|(;,]", s)[0].strip()
    s = re.sub(r"\s+", "-", s)
    for a in allowed:
        if s == a.upper():
            return a
    for a in allowed:
        if s.startswith(a.upper()):
            return a
    return None


def norm_yesno(v: str | None) -> str | None:
    if not v:
        return None
    s = clean_value(v).lower().split()[0].strip(".,;")
    if s in ("yes", "y", "true"):
        return "yes"
    if s in ("no", "n", "false", "none"):
        return "no"
    return None
