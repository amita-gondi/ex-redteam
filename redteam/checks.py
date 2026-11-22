"""Report checks (read-only on reports): wording/boilerplate and URL liveness.

Wording/boilerplate (generalised from the audit_wording.py / wording_check.py used for every historical batch):
  - prompt copy: share of the report's long prose sentences (>= 15 words) that appear verbatim in the
    rendered prompt (a report that parrots the instructions). Must be < max_prompt_copy_frac.
  - cross-report repeat: share of long sentences that also occur in another report of the SAME stage for a
    DIFFERENT task (templated prose). Must be < max_repeat_frac.
  - pairwise Jaccard of word 8-gram shingles against each of those reports. Must be <= max_pair_jaccard.
  The record block, headings, link targets and URLs are excluded from prose.
URL liveness (generalised from url_check.sh): GET each unique cited URL (follow redirects). 2xx/3xx = ok,
401/403/405/429/999 = blocked (bot wall; not evidence the page is missing), 404/410/5xx/DNS/timeouts = dead.
"""
from __future__ import annotations

import concurrent.futures as cf
import itertools
import re
import urllib.error
import urllib.request
from pathlib import Path

RECORD_SPLIT = re.compile(r"\n\s*(?:#{1,6}\s*|\*\*)\s*(?:screen|audit|verdict|probe|anchored)\s+record\b", re.I)
URL_RE = re.compile(r"https?://[^\s)>\]\"'`|]+")


def prose(text: str) -> str:
    t = RECORD_SPLIT.split(text, maxsplit=1)[0]
    t = "\n".join(line for line in t.splitlines() if not line.lstrip().startswith("#"))
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = URL_RE.sub(" ", t)
    return re.sub(r"[*_`]", "", t)


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9%.\- ]", " ", s.lower())).strip()


def sentences(text: str, min_words: int = 15) -> list[str]:
    out = []
    for line in text.split("\n"):
        for cell in line.split("|"):
            for s in re.split(r"(?<=[.!?;:])\s+", cell):
                n = _norm(s)
                if len(n.split()) >= min_words:
                    out.append(n)
    return out


def shingles(text: str, k: int = 8) -> set:
    w = _norm(text).split()
    return {" ".join(w[i:i + k]) for i in range(len(w) - k + 1)}


def jaccard(a: set, b: set) -> float:
    u = a | b
    return len(a & b) / len(u) if u else 0.0


def wording_check(report_text: str, prompt_text: str, peer_reports: dict, cfg: dict) -> dict:
    """peer_reports: {label: text} of same-stage reports for other tasks."""
    mw = int(cfg.get("min_sentence_words", 15))
    k = int(cfg.get("shingle", 8))
    p = prose(report_text)
    ss = sentences(p, mw)
    prompt_s = set(sentences(prompt_text, mw))
    copied = [s for s in ss if s in prompt_s]
    peer_s = {lab: set(sentences(prose(t), mw)) for lab, t in peer_reports.items()}
    all_peer = set(itertools.chain.from_iterable(peer_s.values()))
    repeated = [s for s in ss if s in all_peer]
    sh = shingles(p, k)
    pairs = sorted(((round(jaccard(sh, shingles(prose(t), k)), 4), lab) for lab, t in peer_reports.items()), reverse=True)
    n = len(ss)
    res = {
        "long_sentences": n,
        "prompt_copy_frac": round(len(copied) / n, 4) if n else 0.0,
        "repeat_frac": round(len(repeated) / n, 4) if n else 0.0,
        "max_pair_jaccard": pairs[0][0] if pairs else 0.0,
        "max_pair_with": pairs[0][1] if pairs else None,
        "peers_compared": len(peer_reports),
        "examples": [s[:160] for s in (copied + repeated)[:3]],
    }
    fails = []
    if res["prompt_copy_frac"] >= float(cfg.get("max_prompt_copy_frac", 0.10)):
        fails.append("prompt_copy_frac")
    if res["repeat_frac"] >= float(cfg.get("max_repeat_frac", 0.10)):
        fails.append("repeat_frac")
    if res["max_pair_jaccard"] > float(cfg.get("max_pair_jaccard", 0.10)):
        fails.append("max_pair_jaccard")
    if n == 0:
        fails.append("no_long_sentences")
    res["status"] = "FAIL" if fails else "PASS"
    res["failed"] = fails
    return res


def extract_urls(text: str) -> list[str]:
    return sorted({u.rstrip(".,;:)]}*") for u in URL_RE.findall(text)})


def _fetch(url: str, timeout: float) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) redteam-url-check"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return str(r.status)
    except urllib.error.HTTPError as e:
        return str(e.code)
    except (urllib.error.URLError, OSError, ValueError) as e:
        return "ERR:" + type(getattr(e, "reason", e)).__name__


def classify(code: str) -> str:
    if code.isdigit():
        c = int(code)
        if 200 <= c < 400:
            return "ok"
        if c in (401, 403, 405, 406, 429, 451, 999):
            return "blocked"
        return "dead"
    return "dead" if code.startswith("ERR") else "unknown"


def url_check(text: str, cfg: dict, fetch=None, offline: bool = False) -> dict:
    urls = extract_urls(text)
    if offline or not cfg.get("enabled", True):
        return {"status": "SKIPPED", "reason": "offline" if offline else "disabled", "urls": len(urls)}
    fetch = fetch or (lambda u: _fetch(u, float(cfg.get("timeout_seconds", 20))))
    results = {}
    if urls:
        with cf.ThreadPoolExecutor(max_workers=int(cfg.get("workers", 8))) as ex:
            for u, code in zip(urls, ex.map(fetch, urls), strict=False):
                results[u] = code
    counts: dict = {}
    for code in results.values():
        counts[classify(code)] = counts.get(classify(code), 0) + 1
    dead = sorted(u for u, c in results.items() if classify(c) == "dead")
    return {"status": "FAIL" if dead else "PASS", "urls": len(urls), "counts": counts, "dead": dead,
            "blocked": sorted(u for u, c in results.items() if classify(c) == "blocked"),
            "codes": dict(sorted(results.items()))}


def peer_reports(runs_dir: Path, stage: str, report_name: str, exclude_task: str, limit: int = 200) -> dict:
    """Same-stage reports of OTHER tasks under runs/ (latest per task). Read by the pipeline only, never by an agent."""
    out: dict = {}
    if not runs_dir.is_dir():
        return out
    for tdir in sorted(p for p in runs_dir.iterdir() if p.is_dir() and p.name != exclude_task):
        hits = sorted(tdir.glob(f"*/*/{stage}/{report_name}"))
        if hits:
            try:
                out[tdir.name] = hits[-1].read_text(encoding="utf-8", errors="replace")
            except OSError:
                pass
        if len(out) >= limit:
            break
    return out
