#!/usr/bin/env python3
"""Import existing desk verdicts (read-only copies) into runs/<task_id>/<date>/<run_kind>/.
Sources are never modified. Re-running overwrites runs/ and tasks/<id>/ copies."""
import os, re, csv, hashlib, shutil, json
W = '/workspace'
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABEL = 'ESTIMATED desk verdict, UNMEASURED'
EXCLUDED_TASKS = {'03A': 'v2 03A (expert consolidation; includes task-arithmetic/TIES merging attacks): souping/merging material excluded'}
OUTCOME = {'PASS-SCREEN':'ADVANCE','CONDITIONAL':'FIX','CUT':'CUT','HOLDS':'ADVANCE','FIX':'FIX',
           'needs fixes':'FIX','cut':'CUT','likely-pass':'ADVANCE','at-risk':'FIX'}
log = []

def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def num(x):
    if x is None: return None
    m = re.search(r'-?\d+(?:\.\d+)?', str(x)); return float(m.group(0)) if m else None
def q(v):
    if v is None: return 'null'
    if isinstance(v, float): return repr(v)
    s = str(v).replace('\\','\\\\').replace('"','\\"'); return f'"{s}"'
def dump(d, ind=0):
    out = []
    for k, v in d.items():
        if isinstance(v, dict):
            out.append(' '*ind + f'{k}:'); out += dump(v, ind+2)
        elif isinstance(v, list):
            out.append(' '*ind + f'{k}:')
            for x in v:
                if isinstance(x, dict):
                    first = True
                    for kk, vv in x.items():
                        out.append(' '*ind + ('  - ' if first else '    ') + f'{kk}: {q(vv)}'); first = False
                else: out.append(' '*ind + f'  - {q(x)}')
        else: out.append(' '*ind + f'{k}: {q(v)}')
    return out

def emit(task, date, kind, method, sources, stage_verdict, status='COMPLETE', est=None, evidence=None,
         anchored=None, binding=None, extra=None, files=(), addendum='pending', note=None):
    if task in EXCLUDED_TASKS: return
    d = os.path.join(R, 'runs', task, date, kind); os.makedirs(d, exist_ok=True)
    av = (anchored or {}).get('verdict')
    outcome = OUTCOME.get(av or stage_verdict, 'UNMAPPED')
    rec = {'task_id': task, 'run_kind': kind, 'date': date, 'method_version': method, 'status': status,
           'label': LABEL, 'measurement_status': 'UNMEASURED', 'visibility': 'AIUC-internal (private repo only)',
           'stage_verdict': stage_verdict, 'outcome': outcome, 'binding_line': binding or 'na'}
    if est: rec['estimates'] = est
    rec['evidence'] = evidence or {'attack_basis': 'na', 'verdict_rests_on_assumption': 'na'}
    if anchored: rec['anchored'] = anchored
    rec['anchored_addendum'] = addendum
    if extra: rec.update(extra)
    rec['source'] = [{'path': p, 'sha256': sha(p)} for p in sources]
    if note: rec['note'] = note
    open(os.path.join(d, 'run.yaml'), 'w').write('\n'.join(dump(rec)) + '\n')
    for src, name in files: shutil.copyfile(src, os.path.join(d, name))
    if addendum == 'pending':
        open(os.path.join(d, 'ANCHORED_ADDENDUM_PENDING.md'), 'w').write(
            f'# Anchored addendum: pending\n\nThe anchored re-score for {task} ({kind}, {date}) under '
            'method/evidence_grounding_rule.md will be added here when it finishes. Until then, this run\'s '
            f'verdict ({stage_verdict}) is an {LABEL} that predates or lacks the anchored fields.\n')
    log.append((task, date, kind, stage_verdict, outcome, status, addendum))

def rec_block(path, header):
    s = open(path).read(); i = s.find(header)
    if i < 0: return {}
    d = {}
    for line in s[i+len(header):].split('\n'):
        if line.startswith('## '): break
        m = re.match(r'^([a-z0-9_]+):\s*(.*)$', line.strip())
        if m: d[m.group(1)] = m.group(2).strip()
    return d

# ---- v2 design red team (Nov 20) ----
v2 = f'{W}/task_design_v2_redteam'; v2m = f'v2-design-redteam (PROMPT sha {sha(v2+"/PROMPT.md")[:12]})'
for m in re.finditer(r'\| \[(\w+)\]\((/workspace/task_design_v2_redteam/[^)#]+)#task-\w+\) — (.*?) \| \*\*(.*?)\*\* \| (.*?) \|', open(v2+'/00_summary.md').read()):
    tid, src, title, verdict, reason = m.groups()
    if tid in EXCLUDED_TASKS: continue
    s = open(src).read(); a = s.find(f'## Task {tid}'); b = s.find('\n## Task ', a+5)
    sec = s[a: b if b > 0 else len(s)]
    d = os.path.join(R, 'runs', tid, '2026-11-20', 'design_redteam'); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'redteam_section.md'), 'w').write(f'<!-- excerpt: section "## Task {tid}" of {src} -->\n' + sec)
    emit(tid, '2026-11-20', 'design_redteam', v2m, [src, v2+'/00_summary.md'], verdict,
         extra={'title': title, 'kill_reason': reason}, note='Date from status.txt (Nov 20). Pre-12:04-rule: no attack_basis.')
# v2 rerank: program-level
rr = f'{W}/task_design_v2_rerank'; d = os.path.join(R, 'runs', '_program', '2026-11-20', 'v2_rerank'); os.makedirs(d, exist_ok=True)
for f in ['00_rerank.md', '01_trimmed_budget.md', 'trimmed_budget.csv']:
    lines = open(f'{rr}/{f}').read().split('\n')
    kept = [l for l in lines if '03A' not in l]
    open(os.path.join(d, f), 'w').write('\n'.join(kept))
    log.append(('_program', '2026-11-20', 'v2_rerank:'+f, f'{len(lines)-len(kept)} 03A lines dropped', '', 'COMPLETE', 'na'))

# ---- v3 catalog self-review (Nov 20, 11:21 PM PT) and independent red team (Nov 21, 12:19 AM PT) ----
v3 = f'{W}/task_catalog_v3_full'
for i in range(1, 24):
    tid = f'T{i:02d}'; p = f'{v3}/redteam/{tid}.md'; s = open(p).read()
    m = re.search(r'## Adversarial verdict\s+\*\*([a-z-]+);', s)
    emit(tid, '2026-11-20', 'self_review', 'v3-catalog-self-review (same-session; not independent)', [p], m.group(1),
         files=[(p, 'self_review.md')], extra={'release_hold': True},
         note='Codex log starts 2026-11-21T07:21Z = Nov 20, 11:21 PM PT. Same-session review, not independent (F8 open).')
summ = open(f'{v3}/independent_redteam/00_summary.md').read()
for m in re.finditer(r'^\| (\d+) \| \[(T\d+)\]\((redteam/T\d+_independent\.md)\) \| (\w+) \| ([\d.]+) \| ([\d.]+) \| (.*?) \|$', summ, re.M):
    rank, tid, rel, verdict, r_ind, r_desk, reason = m.groups(); p = f'{v3}/independent_redteam/{rel}'
    emit(tid, '2026-11-21', 'redteam', 'v3-independent-redteam (METHOD.md)', [p, f'{v3}/independent_redteam/00_summary.md'], verdict,
         est={'lawful_composite_R': float(r_ind), 'desk_R_source': float(r_desk)}, files=[(p, 'redteam.md')],
         extra={'priority_rank': int(rank), 'kill_reason': reason}, note='Codex log 2026-11-21T08:19Z = Nov 21, 12:19 AM PT.')

# ---- v4 independent red team (Nov 21, complete 12:19 PM PT) ----
v4 = f'{W}/v4_independent_redteam'
for r in csv.DictReader(open(f'{v4}/verdicts.tsv'), delimiter='\t'):
    tid = r['id']; p = f'{v4}/redteam/{tid}_independent.md'
    emit(tid, '2026-11-21', 'redteam', 'v4-independent-redteam', [p, f'{v4}/verdicts.tsv'], r['verdict'],
         est={'single': num(r['single-run max ESTIMATED']), 'bo4': num(r['best-of-4 ESTIMATED']),
              'pass4': num(r['pass@4 ESTIMATED']), 'ub95': num(r['upper-95 projected ESTIMATED']),
              'strongest_attack': r['strongest attack ESTIMATED']},
         binding=r['kill line breached'] or 'none', files=[(p, 'redteam.md')],
         extra={'source_group': r['source group'], 'required_fixes': r['required fixes'], 'kill_reason': r['main kill reason'],
                'duplicate_of': r['duplicate of'], 'souping_flag': r['souping flag']},
         note='Pre-12:04-rule method: no attack_basis fields.')

# ---- creative v4 screen (Nov 21, complete 11:20 AM PT) ----
cs = f'{W}/creative_v4_saturation_screen'
for r in csv.DictReader(open(f'{cs}/screen.tsv'), delimiter='\t'):
    tid = r['id']; p = f'{cs}/cards/{tid}.md'
    emit(tid, '2026-11-21', 'screen', 'creative-v4-saturation-screen', [p, f'{cs}/screen.tsv'], r['verdict'],
         est={'single': num(r['strongest_attack_single_ESTIMATED']), 'single_range': r['attack_range_ESTIMATED'],
              'bo4': num(r['best_of_4_ESTIMATED']), 'pass4': num(r['pass_at_4_ESTIMATED']), 'ub95': num(r['upper95_ESTIMATED'])},
         binding=r['binding_line'], files=[(p, 'screen_card.md')],
         extra={'title': r['title'], 'author_verdict': r['author_verdict'], 'kill_reason': r['kill_reason'],
                'duplicate_of': r['duplicate_of'], 'souping_flag': r['souping_flag']},
         addendum='pending',
         note='Anchored re-score of this screen is the creative_screen_audit run (same date), IN-PROGRESS at import.')

# ---- creative v4 screen audit (Nov 21, RUNNING at import) ----
ca = f'{W}/creative_v4_screen_audit'
ids = [l.strip() for l in open(f'{ca}/ref/all_ids.txt') if l.strip()]
AUDIT_STATUS = 'COMPLETE' if os.path.exists(f'{ca}/00_summary.md') and os.path.exists(f'{ca}/VALIDATION.md') else 'IN-PROGRESS'
for tid in ids:
    p = f'{ca}/cards/{tid}.md'
    if not os.path.exists(p):
        emit(tid, '2026-11-21', 'screen_audit', 'creative-v4-screen-audit + AMEND 12:04', [f'{ca}/ref/all_ids.txt'], 'not started',
             status='IN-PROGRESS', note='No audit card yet at import (snapshot 1:54 PM PT).'); continue
    a = rec_block(p, '## Audit record'); done = 'anchored_verdict' in a and 'souping_flag' in a
    emit(tid, '2026-11-21', 'screen_audit', 'creative-v4-screen-audit + AMEND 12:04 (evidence_grounding_rule.md)', [p],
         a.get('new_verdict', 'incomplete'), status=AUDIT_STATUS,
         est={'single': num(a.get('new_single')), 'single_range': a.get('new_single_range'), 'bo4': num(a.get('new_bo4')),
              'pass4': num(a.get('new_pass4')), 'ub95': num(a.get('new_ub95'))},
         evidence={'attack_basis': a.get('attack_basis', 'na'), 'demonstrated_ref': a.get('demonstrated_ref'),
                   'gap_to_attack': a.get('gap_to_attack'), 'subfield_sota_ref': a.get('subfield_sota_ref'),
                   'verdict_rests_on_assumption': a.get('verdict_rests_on_assumption', 'na'), 'evidence_grade': a.get('evidence_grade')},
         anchored={'single': num(a.get('anchored_single')), 'bo4': num(a.get('anchored_bo4')), 'pass4': num(a.get('anchored_pass4')),
                   'ub95': num(a.get('anchored_ub95')), 'verdict': a.get('anchored_verdict'),
                   'binding_line': a.get('anchored_binding_line'), 'flip': a.get('anchored_flip')} if done else None,
         binding=a.get('binding_line'), files=[(p, 'audit_card.md')],
         extra={'old_verdict': a.get('old_verdict'), 'flip_vs_old': a.get('flip'), 'redesign_status': a.get('redesign_status'),
                'redesign_oneline': a.get('redesign_oneline'), 'souping_flag': a.get('souping_flag'), 'card_complete': done},
         addendum='present' if done else 'pending',
         note='Snapshot of a RUNNING audit (STATUS.md: RUNNING); aggregation/validation not done. Card may still change.')

# ---- weakness (W) screen (Nov 21; W12-W14 not yet screened) ----
ws = f'{W}/weakness_tasks_saturation_screen'
for r in csv.DictReader(open(f'{ws}/screen.tsv'), delimiter='\t'):
    tid = r['id']; p = f'{ws}/cards/{tid}.md'; add = f'{ws}/anchored_addendum/{tid}.md'
    files = [(p, 'screen_card.md')]
    if os.path.exists(add): files.append((add, 'anchored_addendum_SNAPSHOT_IN_PROGRESS.md'))
    emit(tid, '2026-11-21', 'screen', 'weakness-saturation-screen', [p, f'{ws}/screen.tsv'], r['verdict'],
         est={'single': num(r['attack_single_est']), 'single_range': r['attack_single_range'], 'bo4': num(r['bo4_est']),
              'pass4': num(r['pass4_est']), 'ub95': num(r['ub95_est'])},
         binding=r['binding_line'], files=files,
         extra={'kill_reason': r['kill_reason'], 'duplicate_of': r['duplicate_of'], 'souping_flag': r['souping_flag']},
         addendum='pending', note=('Anchored addendum running at import (snapshot copied).' if os.path.exists(add) else None))

# ---- task cards: FIX packets (T*) and hidden D cards ----
for tid in ['T02','T06','T08','T09','T10','T11','T13','T16','T17','T18']:
    d = os.path.join(R, 'tasks', tid); os.makedirs(d, exist_ok=True)
    shutil.copyfile(f'{W}/fix_packets_v4/{tid}/packet.md', os.path.join(d, 'card.md'))
    open(os.path.join(d, 'PROVENANCE.md'), 'w').write(f'card.md = copy of /workspace/fix_packets_v4/{tid}/packet.md (sha256 {sha(W+"/fix_packets_v4/"+tid+"/packet.md")}). Pre-migration: its pairing table still lists the old roster (Carbon/6.1 Sol/Astra); canonical set is in config/runner.yaml.\n')
for f in sorted(os.listdir(f'{W}/hidden_task_cards_v4/cards')):
    tid = f[:-3]; d = os.path.join(R, 'tasks', tid); os.makedirs(d, exist_ok=True)
    shutil.copyfile(f'{W}/hidden_task_cards_v4/cards/{f}', os.path.join(d, 'card.md'))
    open(os.path.join(d, 'PROVENANCE.md'), 'w').write(f'card.md = copy of /workspace/hidden_task_cards_v4/cards/{f} (sha256 {sha(W+"/hidden_task_cards_v4/cards/"+f)}), Nov 21 2026.\n')

# ---- program-level summaries ----
prog = [('2026-11-20','v2_design_redteam',[f'{v2}/00_summary.md']),
        ('2026-11-21','v3_independent_redteam',[f'{v3}/independent_redteam/00_summary.md', f'{v3}/independent_redteam/METHOD.md', f'{v3}/independent_redteam/VALIDATION.md']),
        ('2026-11-21','v4_independent_redteam',[f'{v4}/00_summary.md', f'{v4}/STATUS.md', f'{v4}/VALIDATION.md', f'{v4}/screen_disagreement.md', f'{v4}/verdicts.tsv']),
        ('2026-11-21','creative_screen',[f'{cs}/00_summary.md', f'{cs}/VALIDATION.md', f'{cs}/screen.tsv']),
        ('2026-11-21','creative_screen_audit_IN-PROGRESS',[f'{ca}/STATUS.md', f'{ca}/audit.tsv']),
        ('2026-11-21','weakness_screen_IN-PROGRESS',[f'{ws}/00_summary.md', f'{ws}/STATUS.md', f'{ws}/screen.tsv']),
        ('2026-11-21','hidden_task_cards_v4',[f'{W}/hidden_task_cards_v4/00_index.md', f'{W}/hidden_task_cards_v4/VALIDATION.md'])]
for date, kind, fs in prog:
    d = os.path.join(R, 'runs', '_program', date, kind); os.makedirs(d, exist_ok=True)
    for f in fs: shutil.copyfile(f, os.path.join(d, os.path.basename(f)))
    open(os.path.join(d, 'SOURCES.txt'), 'w').write('\n'.join(f'{f}  sha256={sha(f)}' for f in fs) + '\n')

with open(os.path.join(R, 'runs', 'INDEX.tsv'), 'w') as f:
    f.write('task_id\tdate\trun_kind\tstage_verdict\toutcome\tstatus\tanchored_addendum\n')
    for row in sorted(log): f.write('\t'.join(map(str, row)) + '\n')
print(len(log), 'records')
