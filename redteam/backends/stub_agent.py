"""Deterministic stub desk agent (stdlib only). Run as a subprocess in the stage workdir:
    python3 stub_agent.py <stage> <task_id> [resume <sid>]   (prompt or resume message on stdin)
It lists what it can see, writes a canned report with a valid record block into out/, then DONE.txt.
Config (JSON in $REDTEAM_STUB_CONFIG): {"behaviour": {"<stage>": "ok|stall_once|fail_once|no_record|drift"},
"sleep": seconds, "scores": {...}}. OUTPUT IS NOT A DESK JUDGEMENT: it exists to exercise the pipeline.
"""
import json
import os
import sys
import time
import uuid

STAGE, TASK = sys.argv[1], sys.argv[2]
RESUME = len(sys.argv) > 4 and sys.argv[3] == "resume"
SID = sys.argv[4] if RESUME else str(uuid.uuid4())
CFG = json.loads(os.environ.get("REDTEAM_STUB_CONFIG") or "{}")
BEHAVIOUR = (CFG.get("behaviour") or {}).get(STAGE, "ok")
prompt = sys.stdin.read()


def ev(obj):
    sys.stdout.write(json.dumps(obj) + "\n")
    sys.stdout.flush()


ev({"type": "thread.started", "thread_id": SID})
seen = sorted(os.path.join(d, f)[2:] for d, _, fs in os.walk(".") for f in fs)
ev({"type": "item.completed", "item": {"type": "command_execution", "command": "find . -type f",
                                        "aggregated_output": "\n".join(seen)}})
os.makedirs("out", exist_ok=True)
with open("out/.stub_seen.json", "w") as f:
    json.dump({"stage": STAGE, "files": seen, "cwd_entries": sorted(os.listdir("."))}, f)

state = "out/.stub_attempts"
n = int(open(state).read()) if os.path.exists(state) else 0
open(state, "w").write(str(n + 1))
if BEHAVIOUR == "fail_once" and n == 0:
    sys.stderr.write("stub: simulated transient failure\n")
    sys.exit(1)
if BEHAVIOUR == "stall_once" and n == 0:
    open("out/partial.md", "w").write("partial\n")
    time.sleep(3600)
time.sleep(float(CFG.get("sleep", 0)))

title = TASK
try:
    for line in open("task/card.md", encoding="utf-8"):
        if line.startswith("# "):
            title = line[2:].strip()
            break
except OSError:
    pass

S = {"single": 0.45, "bo4": 0.57, "pass4": 0.30, "ub95": 0.68,
     "a_single": 0.40, "a_bo4": 0.52, "a_pass4": 0.20, "a_ub95": 0.62, "basis": "LITERATURE-ONLY"}
S.update(CFG.get("scores") or {})
note = ("This report was written by the STUB backend to exercise the pipeline for task %s (%s). "
        "It is not a desk judgement, cites no sources and must never be used as evidence." % (TASK, title))


def screen():
    v = "CONDITIONAL"
    return ("# %s: %s: saturation screen\n\n%s\n\n## 7. Verdict\n%s\n\n## Screen record\n"
            "id: %s\nverdict: %s\nbinding_line: bo4>0.60\nattack_single_est: %.2f\nattack_single_range: 0.30-0.60\n"
            "bo4_est: %.2f\npass4_est: %.2f\nub95_est: %.2f\ngpuh_new_est: 0\nduplicate_of: none\nkill_reason: none\n"
            "souping_flag: no\n") % (TASK, title, note, v, TASK, v, S["single"], S["bo4"], S["pass4"], S["ub95"])


def audit():
    rec = ("## Audit record\n" if BEHAVIOUR != "drift" else "### audit Record\n```\n")
    kv = [("id", TASK), ("old_verdict", "CONDITIONAL"), ("evidence_grade", "PARTIAL"),
          ("new_single", "%.2f" % S["single"]), ("new_single_range", "0.30-0.60"), ("new_bo4", "%.2f" % S["bo4"]),
          ("new_pass4", "%.2f" % S["pass4"]), ("new_ub95", "%.2f" % S["ub95"]), ("new_verdict", "CONDITIONAL"),
          ("binding_line", "bo4>0.60"), ("attack_basis", S["basis"]), ("demonstrated_ref", "none (stub)"),
          ("gap_to_attack", "stub"), ("subfield_sota_ref", "none (stub)"),
          ("anchored_single", "%.2f" % S["a_single"]), ("anchored_bo4", "%.2f" % S["a_bo4"]),
          ("anchored_pass4", "%.2f" % S["a_pass4"]), ("anchored_ub95", "%.2f" % S["a_ub95"]),
          ("anchored_verdict", S.get("a_verdict", "PASS-SCREEN")), ("anchored_binding_line", "none"),
          ("anchored_flip", "CONDITIONAL->PASS-SCREEN"), ("strict_verdict", S.get("strict_written", "CONDITIONAL")),
          ("strict_binding_line", "bo4>0.60"), ("verdict_rests_on_assumption", "yes"),
          ("redesign_status", "NOT-NEEDED"), ("redesign_oneline", "na"), ("redesign_attack_basis", "na"), ("souping_flag", "no")]
    if BEHAVIOUR == "drift":
        body = "".join("- **%s**: `%s`\n" % (k.replace("_", " ").title() if i % 3 == 0 else k, v) for i, (k, v) in enumerate(kv))
        body = body.replace("0.30-0.60", "0.30\u20130.60") + "```\n"
    else:
        body = "".join("%s: %s\n" % (k, v) for k, v in kv)
    return "# %s: %s: anchored re-score\n\n%s\n\n%s%s" % (TASK, title, note, rec, body)


def redteam():
    return ("# %s: %s: independent adversarial review\n\n**Verdict: FIX.** %s\n\n## Verdict record\n"
            "id: %s\nverdict: FIX\nstrongest_attack: ESTIMATED 0.50 (0.35-0.65)\ncombined_recipe_attack: ESTIMATED 0.50 (0.35-0.65)\n"
            "best_of_4: ESTIMATED 0.58\npass_at_4: ESTIMATED 0.35\nsingle_run_max: ESTIMATED 0.62\nupper95_projected: ESTIMATED 0.70\n"
            "kill_line_breached: none\nattack_basis: LITERATURE-ONLY\ndemonstrated_ref: none (stub)\ngap_to_attack: stub\n"
            "subfield_sota_ref: none (stub)\ndecisive_gpu_h: ESTIMATED 0\nrequired_fixes: stub fix one; stub fix two\n"
            "main_kill_reason: n/a\nduplicate_of: none\nsouping_flag: no\n") % (TASK, title, note, TASK)


def probe(mode):
    high = 0
    med = 1 if mode == "whitebox" else 0
    return ("# %s: %s: desk exploit probe (%s)\n\n%s\n\n## Probe record\n"
            "id: %s\nmode: %s\nfindings_total: %d\nfindings_high: %d\nfindings_medium: %d\nfindings_low: 0\n"
            "blocks_panel: no\nhidden_data_reachable: no\ntop_finding: %s\nfindings: %s\ndefences_held: stub\n"
            "counts_toward_saturation: no\nsouping_flag: no\n") % (
        TASK, title, mode, note, TASK, mode, high + med, high, med,
        "F1 medium grader-logic: stub finding" if med else "none", "F1 [medium] grader-logic: stub finding" if med else "none")


REPORTS = {"screen": ("screen_card.md", screen), "anchored_rescore": ("audit_card.md", audit),
           "redteam": ("redteam.md", redteam), "probe_blackbox": ("probe_blackbox.md", lambda: probe("blackbox")),
           "probe_whitebox": ("probe_whitebox.md", lambda: probe("whitebox"))}
name, fn = REPORTS[STAGE]
text = fn()
if BEHAVIOUR == "no_record":
    text = text.split("## ")[0]
with open(os.path.join("out", name), "w", encoding="utf-8") as f:
    f.write(text)
with open("out/last_message.md", "w") as f:
    f.write("stub %s done\n" % STAGE)
with open("out/DONE.txt", "w") as f:
    f.write("%s %s %s stub\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), TASK, STAGE))
ev({"type": "turn.completed"})
