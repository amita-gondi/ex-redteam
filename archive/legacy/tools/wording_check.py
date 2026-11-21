#!/usr/bin/env python3
"""Repeated-wording check for desk reports (redteam.md, screen_card.md, audit_card.md) (a CHECKER, not a generator).
# Generic copy of the v4 red-team checker. Point it at runs/ (or a subset) to compare reports across tasks.
Per file: share of its long sentences (>=15 words) that also occur verbatim (normalized) in any other file of the set. Must be <10%.
Pairwise: Jaccard similarity of word 8-gram shingle sets. Must be <=0.10.
The '## Verdict record' block (structured key: value fields) is excluded.
Usage: wording_check.py [--json OUT] [--ref DIR] FILES_OR_DIRS...
"""
import re, sys, json, os, itertools, glob
def load(p):
    t=open(p,encoding='utf-8').read()
    t=re.split(r'\n## (Verdict|Screen|Audit) record', t)[0]
    return t
def norm(s): return re.sub(r'\s+',' ',re.sub(r'[^a-z0-9%.\- ]',' ',s.lower())).strip()
def sentences(t):
    t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t)  # drop link targets
    parts=[]
    for line in t.split('\n'):
        for cell in line.split('|'):
            parts += re.split(r'(?<=[.!?;:])\s+', cell)
    out=[]
    for s in parts:
        n=norm(s)
        if len(n.split())>=15: out.append(n)
    return out
def shingles(t,k=8):
    w=norm(re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t)).split()
    return set(' '.join(w[i:i+k]) for i in range(len(w)-k+1))
args=sys.argv[1:]; jout=None; ref=None
if '--json' in args: i=args.index('--json'); jout=args[i+1]; del args[i:i+2]
if '--ref' in args: i=args.index('--ref'); ref=args[i+1]; del args[i:i+2]
files=[]
for a in args:
    files += sorted(glob.glob(os.path.join(a,'**','*.md'),recursive=True)) if os.path.isdir(a) else [a]
files=[f for f in files if os.path.basename(f) in ('redteam.md','screen_card.md','audit_card.md')]
texts={os.path.relpath(f):load(f) for f in files}
sents={k:sentences(v) for k,v in texts.items()}
sh={k:shingles(v) for k,v in texts.items()}
owners={}
for k,ss in sents.items():
    for s in set(ss): owners.setdefault(s,set()).add(k)
res={'files':{}, 'pairs_over_0.10':[], 'max_pair':None}
for k,ss in sents.items():
    rep=[s for s in ss if len(owners[s])>1]
    frac=len(rep)/len(ss) if ss else 0.0
    res['files'][k]={'long_sentences':len(ss),'repeated':len(rep),'repeated_frac':round(frac,4),'examples':rep[:5]}
mx=(0,None)
for a,b in itertools.combinations(sorted(sh),2):
    u=len(sh[a]|sh[b]); j=len(sh[a]&sh[b])/u if u else 0
    if j>mx[0]: mx=(j,(a,b))
    if j>0.10: res['pairs_over_0.10'].append([a,b,round(j,4)])
res['max_pair']=[round(mx[0],4),mx[1]]
if ref:
    rf=sorted(glob.glob(os.path.join(ref,'**','*.md'),recursive=True))
    rs=set(); rsh={}
    for f in rf:
        t=load(f); rs|=set(sentences(t)); rsh[f]=shingles(t)
    res['vs_reference']={k:{'sent_frac_in_ref':round(sum(1 for s in sents[k] if s in rs)/max(1,len(sents[k])),4),
        'max_jaccard_ref':round(max([len(sh[k]&v)/max(1,len(sh[k]|v)) for v in rsh.values()] or [0]),4)} for k in sents}
bad=[k for k,v in res['files'].items() if v['repeated_frac']>=0.10]
res['files_failing']=bad
print(f"files={len(files)} failing_files(>=10%)={len(bad)} pairs>0.10={len(res['pairs_over_0.10'])} max_pair={res['max_pair']}")
for k in sorted(res['files']): 
    v=res['files'][k]; print(f"  {k}: {v['repeated']}/{v['long_sentences']} = {v['repeated_frac']:.1%}" + (f"  ref_sent={res['vs_reference'][k]['sent_frac_in_ref']:.1%} ref_maxJ={res['vs_reference'][k]['max_jaccard_ref']}" if ref else ''))
for a,b,j in res['pairs_over_0.10']: print('  PAIR',a,b,j)
for k in bad:
    for e in res['files'][k]['examples']: print('   REPEATED in',k,':',e[:160])
if jout: json.dump(res,open(jout,'w'),indent=1)
