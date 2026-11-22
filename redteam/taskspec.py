"""Load and validate a task directory (task.yaml + referenced files).

`validate_task` never stops at the first problem: it collects every schema error and every semantic
problem (missing files, unfilled placeholders, leaks of hidden data into shared inputs, overrides without
a reason) so `redteam validate` can list them all at once.
"""
from __future__ import annotations

import copy
import fnmatch
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .config import CANONICAL_PAIRINGS
from .killlines import KillLines

PLACEHOLDER = re.compile(r"\b(TODO|TBD|FIXME)\b|<fill[^>]*>|<your[^>]*>", re.I)
SOUPING = re.compile(r"\b(model soup|souping|weight averag\w*|task arithmetic|TIES[- ]merg\w*|DARE[- ]merg\w*|model merg\w*)\b", re.I)
DEFAULT_SECRET_GLOBS = ["**/*secret*", "**/*seed*", "**/*.key", "**/*.pem", "**/.env", "**/.env.*", "**/hidden/**", "**/heldout/**"]


@dataclass
class TaskSpec:
    task_dir: Path
    data: dict
    kill_lines: KillLines
    pairings: list
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)

    @property
    def id(self) -> str:
        return str(self.data.get("id"))

    @property
    def version(self) -> str:
        return str(self.data.get("version"))

    def path(self, rel: str) -> Path:
        p = Path(rel).expanduser()
        return p if p.is_absolute() else (self.task_dir / p)

    # ------------------------------------------------------------------ input sets (blindness)
    def shared_inputs(self) -> list[tuple[Path, str]]:
        """(source, destination-relative-to-workdir/task) for every file any desk stage may see."""
        d = self.data
        out = [(self.path(d["card"]["file"]), "card.md"),
               (self.path(d["grader"]["interface_file"]), "grader_interface.md")]
        sota = (d.get("evidence") or {}).get("sota_file")
        if sota:
            out.append((self.path(sota), "sota_sources.md"))
        for x in (d.get("inputs") or {}).get("extra", []) or []:
            out.append((self.path(x), "extra/" + Path(x).as_posix()))
        return out

    def peer_cards(self) -> list[tuple[Path, str]]:
        out = []
        for i, x in enumerate((self.data.get("duplicate_check") or {}).get("peer_cards", []) or []):
            p = self.path(x).resolve()
            out.append((p, f"peers/{i:02d}_{p.parent.name}_{p.name}"))
        return out

    def grader_source(self) -> Path | None:
        sp = (self.data.get("grader") or {}).get("source_path")
        return self.path(sp).resolve() if sp else None

    def hidden_paths(self) -> list[Path]:
        return [self.path(h["path"]).resolve() for h in self.data.get("hidden_data", []) or []]

    def canaries(self) -> list[str]:
        return [h["canary_string"] for h in self.data.get("hidden_data", []) or [] if h.get("canary_string")]

    def secret_globs(self) -> list[str]:
        g = (self.data.get("grader") or {}).get("secret_globs")
        return list(g) if g else list(DEFAULT_SECRET_GLOBS)

    def whitebox_files(self) -> list[tuple[Path, str]]:
        """Files of the grader source exposed READ-ONLY to the white-box probe: everything under source_path
        except secret_globs and hidden_data paths, unless explicitly listed in whitebox_include."""
        src = self.grader_source()
        if not src or not src.exists():
            return []
        include = set((self.data.get("grader") or {}).get("whitebox_include", []) or [])
        hidden = self.hidden_paths()
        files = [src] if src.is_file() else sorted(p for p in src.rglob("*") if p.is_file())
        base = src.parent if src.is_file() else src
        out = []
        for f in files:
            r = f.relative_to(base).as_posix()
            if any(_inside(f.resolve(), h) for h in hidden):
                continue   # hidden/held-out data is never exposed, even if listed
            if r not in include and any(_glob(r, g) for g in self.secret_globs()):
                continue
            if "__pycache__" in f.parts:
                continue
            out.append((f, "grader_src/" + r))
        return out

    def withheld_whitebox(self) -> list[str]:
        src = self.grader_source()
        if not src or not src.exists() or src.is_file():
            return []
        shown = {d for _, d in self.whitebox_files()}
        return sorted("grader_src/" + p.relative_to(src).as_posix() for p in src.rglob("*")
                      if p.is_file() and "__pycache__" not in p.parts
                      and "grader_src/" + p.relative_to(src).as_posix() not in shown)

    def public_yaml(self) -> str:
        """task.yaml as shown to desk agents: hidden data, canaries and grader source location removed."""
        d = copy.deepcopy(self.data)
        d.pop("hidden_data", None)
        g = d.get("grader") or {}
        for k in ("source_path", "whitebox_include", "secret_globs"):
            g.pop(k, None)
        hdr = ("# Public copy of task.yaml for desk agents. hidden_data, canary strings and the grader source\n"
               "# location are removed. Do not try to find them.\n")
        return hdr + yaml.safe_dump(d, sort_keys=False, allow_unicode=True)

    def wallclock_hours(self) -> float:
        return float(self.data["card"].get("wallclock_hours", 12))


def _glob(rel: str, pat: str) -> bool:
    if fnmatch.fnmatch(rel, pat):
        return True
    if pat.startswith("**/") and fnmatch.fnmatch(rel, pat[3:]):
        return True
    return False


def _inside(p: Path, parent: Path) -> bool:
    try:
        p.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def _walk_strings(obj, path="$"):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _walk_strings(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _walk_strings(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        yield path, obj


def _fmt_schema_error(e) -> str:
    loc = "$" + "".join(f"[{p}]" if isinstance(p, int) else f".{p}" for p in e.absolute_path)
    msg = e.message
    if e.validator == "not" and isinstance(e.instance, str):
        msg = f"{e.instance!r} looks like an unfilled placeholder or an unsafe path"
    elif e.validator == "required":
        msg = msg.replace("is a required property", "is required but missing")
    elif e.validator == "additionalProperties":
        msg = f"unknown field(s): {msg}"
    return f"{loc}: {msg}"


def load_schema(schema_path: Path) -> dict:
    return json.loads(Path(schema_path).read_text(encoding="utf-8"))


def validate_task(task_dir: str | Path, cfg: dict, schema_path: Path) -> TaskSpec:
    from jsonschema import Draft202012Validator

    task_dir = Path(task_dir).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    ty = task_dir / "task.yaml"
    data: dict = {}
    if not task_dir.is_dir():
        errors.append(f"{task_dir}: task directory not found")
    elif not ty.is_file():
        errors.append(f"{ty}: task.yaml not found (copy tasks/_template/ and fill it in)")
    else:
        try:
            data = yaml.safe_load(ty.read_text(encoding="utf-8")) or {}
            if not isinstance(data, dict):
                errors.append("task.yaml: top level must be a mapping")
                data = {}
        except yaml.YAMLError as e:
            errors.append(f"task.yaml: YAML parse error: {e}")
    schema = load_schema(schema_path)
    if data:
        v = Draft202012Validator(schema)
        for e in sorted(v.iter_errors(data), key=lambda e: [str(x) for x in e.absolute_path]):
            errors.append(_fmt_schema_error(e))

    # kill lines (defaults from config; override needs a reason)
    try:
        kl = KillLines.from_dicts(cfg.get("kill_lines"), data.get("kill_thresholds") if data else None)
    except ValueError as e:
        errors.append(f"$.kill_thresholds: {e}")
        kl = KillLines.from_dicts(cfg.get("kill_lines"))
    if data.get("pairings"):
        pairings = data["pairings"].get("set") or []
        warnings.append(f"$.pairings: non-canonical pairing set ({data['pairings'].get('reason', 'no reason')})")
    else:
        pairings = copy.deepcopy(cfg.get("pairings") or CANONICAL_PAIRINGS)
    spec = TaskSpec(task_dir=task_dir, data=data, kill_lines=kl, pairings=pairings, errors=errors, warnings=warnings)
    if not data:
        return spec

    # placeholders anywhere in task.yaml
    for p, s in _walk_strings(data):
        if PLACEHOLDER.search(s):
            errors.append(f"{p}: unfilled placeholder ({PLACEHOLDER.search(s).group(0)!r})")
    if data.get("id") and data["id"] != task_dir.name:
        warnings.append(f"$.id: {data['id']!r} differs from the directory name {task_dir.name!r}")
    if str(data.get("id", "")).startswith("_"):
        errors.append("$.id: must not start with '_' (reserved for templates)")

    # referenced files
    def need_file(label, rel):
        if not isinstance(rel, str) or not rel:
            return None
        f = spec.path(rel)
        if not f.is_file():
            errors.append(f"{label}: file not found: {rel}")
            return None
        if not _inside(f, task_dir):
            errors.append(f"{label}: must be inside the task directory: {rel}")
        return f

    shared_files = []
    card = data.get("card") or {}
    grader = data.get("grader") or {}
    ev = data.get("evidence") or {}
    for label, rel in (("$.card.file", card.get("file")), ("$.grader.interface_file", grader.get("interface_file")),
                       ("$.evidence.sota_file", ev.get("sota_file"))):
        f = need_file(label, rel)
        if f:
            shared_files.append(f)
    for i, x in enumerate((data.get("inputs") or {}).get("extra", []) or []):
        f = need_file(f"$.inputs.extra[{i}]", x)
        if f:
            shared_files.append(f)
    for i, x in enumerate((data.get("duplicate_check") or {}).get("peer_cards", []) or []):
        f = spec.path(x)
        if not f.is_file():
            errors.append(f"$.duplicate_check.peer_cards[{i}]: file not found: {x}")
        elif "runs" in f.resolve().parts:
            errors.append(f"$.duplicate_check.peer_cards[{i}]: peers must be card files, never run records: {x}")
        else:
            shared_files.append(f)
    for f in shared_files:
        try:
            txt = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for ln, line in enumerate(txt.splitlines(), 1):
            if PLACEHOLDER.search(line):
                errors.append(f"{f.relative_to(task_dir) if _inside(f, task_dir) else f}:{ln}: unfilled placeholder: {line.strip()[:100]}")
                break
        for ln, line in enumerate(txt.splitlines(), 1):
            if SOUPING.search(line):
                warnings.append(f"{f.name}:{ln}: mentions souping/merging ({SOUPING.search(line).group(0)!r}); "
                                "souping/merging is excluded entirely: it must not be part of the task, an attack or a fix")
                break

    # evidence lists
    for k in ("agent_demonstrated", "subfield_sota"):
        if isinstance(ev.get(k), list) and not ev.get(k) and not str(ev.get("not_found_reason", "")).strip():
            errors.append(f"$.evidence.{k}: empty; add entries or explain in $.evidence.not_found_reason")
    for i, e in enumerate(ev.get("agent_demonstrated", []) or []):
        if isinstance(e, dict) and e.get("status") in ("fetched", "search-only") and not e.get("url"):
            errors.append(f"$.evidence.agent_demonstrated[{i}].url: required when status is {e.get('status')}")
    for i, e in enumerate(ev.get("subfield_sota", []) or []):
        if isinstance(e, dict) and e.get("status") in ("fetched", "search-only") and not e.get("url"):
            errors.append(f"$.evidence.subfield_sota[{i}].url: required when status is {e.get('status')}")

    # reward
    rw = data.get("reward") or {}
    if rw.get("grader_noise") == "UNMEASURED" and not str(rw.get("grader_noise_plan", "")).strip():
        warnings.append("$.reward.grader_noise: UNMEASURED without $.reward.grader_noise_plan (planned measurement)")
    sc = rw.get("scale") or {}
    if isinstance(sc.get("min"), (int, float)) and isinstance(sc.get("max"), (int, float)) and sc["min"] >= sc["max"]:
        errors.append("$.reward.scale: min must be < max")
    cr = data.get("cost_rates") or {}
    if cr and "basis" not in cr:
        errors.append("$.cost_rates.basis: required (ESTIMATED unless measured)")

    # grader source (white-box probe only)
    wb = (cfg.get("probe_modes") or {}).get("whitebox") or {}
    src = spec.grader_source()
    if wb.get("enabled", True) and int(wb.get("count", 1)) > 0:
        if not src:
            errors.append("$.grader.source_path: required for the white-box probe (or disable probe_modes.whitebox in config)")
        elif not src.exists():
            errors.append(f"$.grader.source_path: not found: {grader.get('source_path')}")
    if src and src.exists():
        for f in shared_files:
            if _inside(f, src):
                errors.append(f"{f.name}: a shared input lies inside grader.source_path; the grader source is white-box only")

    # hidden data never reachable through shared inputs
    seen_canary = set()
    for i, h in enumerate(data.get("hidden_data", []) or []):
        if not isinstance(h, dict) or not h.get("path"):
            continue
        hp = spec.path(h["path"]).resolve()
        if not hp.exists():
            warnings.append(f"$.hidden_data[{i}].path: not present on this machine ({h['path']}); it is hidden anyway")
        for f in shared_files:
            if _inside(f, hp) or _inside(hp, f):
                errors.append(f"$.hidden_data[{i}]: overlaps shared input {f.name}; hidden data must never be a desk input")
        if hp == task_dir or _inside(task_dir, hp):
            errors.append(f"$.hidden_data[{i}]: must not contain the task directory")
        c = h.get("canary_string")
        if c:
            if c in seen_canary:
                errors.append(f"$.hidden_data[{i}].canary_string: duplicate canary string")
            seen_canary.add(c)
    canaries = spec.canaries()
    if canaries:
        exposed = list(shared_files) + [f for f, _ in spec.whitebox_files()]
        for f in exposed:
            try:
                t = f.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if any(c in t for c in canaries):
                errors.append(f"{f}: contains a hidden-data canary string; that file would leak hidden data to desk agents")
        if any(c in spec.public_yaml() for c in canaries):
            errors.append("task.yaml: a canary string appears outside hidden_data")
    return spec
