from redteam.records import norm_verdict, num, num_range, parse_record
from redteam.stages import SCREEN_KEYS

CANON = """# T: screen
## Screen record
id: T01
verdict: CONDITIONAL
binding_line: bo4>0.60
attack_single_est: 0.45
attack_single_range: 0.30-0.60
bo4_est: 0.57
pass4_est: 0.30
ub95_est: 0.68
gpuh_new_est: 24
duplicate_of: none
kill_reason: none
souping_flag: no
"""

DRIFT = """# T: screen
### the Screen Record
```
- **Id**: `T01`
- **Verdict** = CONDITIONAL | binding bo4
* bo4_est : 0.57
*  pass4 est — 0.30
| ub95_est | 0.68 |
souping_flag: no
```
Some trailing prose.
"""

NO_HEADING = """# T
blah blah
id: T01
verdict: CUT
bo4_est: 0.80
souping_flag: yes
more prose here that should not become keys at all really.
"""


def test_canonical():
    rec, how = parse_record(CANON, ["screen"], SCREEN_KEYS)
    assert how == "heading"
    assert rec["verdict"] == "CONDITIONAL"
    assert rec["bo4_est"] == "0.57"
    assert rec["souping_flag"] == "no"


def test_drift_headinglevel_bold_backtick_table_endash():
    rec, how = parse_record(DRIFT, ["screen"], SCREEN_KEYS)
    assert how == "heading"
    assert rec["id"] == "T01"
    assert norm_verdict(rec["verdict"]) == "CONDITIONAL"
    assert rec["bo4_est"] == "0.57"
    assert rec["pass4_est"] == "0.30"    # "pass4 est" normalises to pass4_est
    assert rec["ub95_est"] == "0.68"     # from a table row
    assert rec["souping_flag"] == "no"


def test_fallback_tail_without_heading():
    rec, how = parse_record(NO_HEADING, ["screen"], SCREEN_KEYS)
    assert how == "fallback-tail"
    assert rec["verdict"] == "CUT"
    assert rec["souping_flag"] == "yes"


def test_last_block_wins_when_template_quoted_first():
    text = ("## Screen record\nid: T01\nverdict: PASS-SCREEN|CONDITIONAL|CUT\n\n"
            "lots of analysis\n\n## Screen record\nid: T01\nverdict: CUT\nsouping_flag: no\n")
    rec, how = parse_record(text, ["screen"], SCREEN_KEYS)
    assert rec["verdict"] == "CUT"


def test_norm_verdict_rejects_unfilled_template():
    assert norm_verdict("PASS-SCREEN|CONDITIONAL|CUT") is None
    assert norm_verdict("**Pass-screen**") == "PASS-SCREEN"
    assert norm_verdict("FIX") == "FIX"
    assert norm_verdict("holds.") == "HOLDS"


def test_num_and_range():
    assert num("ESTIMATED 0.67 (0.47-0.87)") == 0.67
    assert num("0.xx") is None
    assert num_range("ESTIMATED 0.67 (0.47-0.87)") == (0.47, 0.87)
    assert num_range("0.30-0.60") == (0.30, 0.60)
