#!/usr/bin/env python3
"""Set-level metrics for the forecast-judgment eval.

Usage: python3 evals/judgment/summarize.py [.claude/hillclimb/forecast-judgment/baseline]

Per-case grades live in results.jsonl; this adds what no single case can show:
  yes_rate        share of ok rows answering yes
  anchoring       flip-<date> answer equals replay-<date> answer, same rep
                  (the two cases share evidence; only the prior differs)
  rep_agreement   same case, same answer across reps
  replay_changes  answer changes between consecutive replay dates, per rep
Writes summary.json beside results.jsonl.
"""
import json, sys
from collections import defaultdict
from pathlib import Path

vdir = Path(sys.argv[1] if len(sys.argv) > 1 else '.claude/hillclimb/forecast-judgment/baseline')
rows = [json.loads(l) for l in (vdir / 'results.jsonl').read_text().splitlines() if l.strip()]
ok = [r for r in rows if r.get('status') == 'ok']
ans = {(r['prompt_id'], r['rep']): ('yes' if r['grade']['yes'] else 'no') for r in ok if r['grade'].get('valid')}

def mean(xs):
    return round(sum(xs) / len(xs), 3) if xs else None

out = {'rows': len(rows), 'ok_rows': len(ok),
       'means': {m: mean([r['grade'][m] for r in ok]) for m in ('valid', 'first_pass', 'judgment', 'yes')},
       'cost_usd_total': round(sum(r.get('cli_cost_usd') or 0 for r in rows), 2)}

pairs = [(cid, rep, a, ans.get(('replay-' + cid[5:], rep))) for (cid, rep), a in ans.items() if cid.startswith('flip-')]
pairs = [p for p in pairs if p[3] is not None]
out['anchoring'] = {'agree': sum(p[2] == p[3] for p in pairs), 'pairs': len(pairs),
                    'disagree': sorted(f'{c} rep{k}: flip={a} replay={b}' for c, k, a, b in pairs if a != b)}

by_case = defaultdict(dict)
for (cid, rep), a in ans.items():
    by_case[cid][rep] = a
multi = {c: v for c, v in by_case.items() if len(v) > 1}
out['rep_agreement'] = {'agree': sum(len(set(v.values())) == 1 for v in multi.values()), 'cases': len(multi),
                        'split': sorted(c for c, v in multi.items() if len(set(v.values())) > 1)}

changes = {}
for rep in sorted({k for _, k in ans}):
    seq = [(c, ans[(c, rep)]) for c in sorted(by_case) if c.startswith('replay-') and (c, rep) in ans]
    changes[f'rep{rep}'] = {'replays': len(seq), 'changes': [f'{a[0]}={a[1]} -> {b[0]}={b[1]}' for a, b in zip(seq, seq[1:]) if a[1] != b[1]]}
out['replay_changes'] = changes

(vdir / 'summary.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(out, ensure_ascii=False, indent=2))
