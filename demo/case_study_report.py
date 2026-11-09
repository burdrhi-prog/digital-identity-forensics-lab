"""Reproducible, fictional 2024 case study. Standard library only."""
import csv
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

DATA=Path(__file__).resolve().parents[1]/'examples'/'case-study-2024'

def rows(name):
    with (DATA/name).open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))

def evaluate():
    events=rows('events.csv')
    evidence={r['artifact_id'] for r in rows('evidence_index.csv')}
    ids=set()
    for e in events:
        if e['event_id'] in ids:
            raise ValueError('Duplicate event ID')
        ids.add(e['event_id'])
        artifact=e['source_ref'].split(':',1)[0]
        if artifact not in evidence:
            raise ValueError('Unindexed source: '+artifact)
        raw=datetime.fromisoformat(e['raw_timestamp'].replace('Z','+00:00'))
        normalized=datetime.fromisoformat(e['utc_timestamp'].replace('Z','+00:00'))
        if raw.tzinfo is None or normalized.tzinfo is None:
            raise ValueError('Missing timezone')
        if raw.astimezone(timezone.utc)!=normalized.astimezone(timezone.utc):
            raise ValueError('UTC normalization mismatch: '+e['event_id'])
    pairs=[]
    for left,right in combinations(sorted(events,key=lambda x:x['utc_timestamp']),2):
        if left['account_alias']!=right['account_alias']:
            continue
        a=datetime.fromisoformat(left['utc_timestamp'].replace('Z','+00:00'))
        b=datetime.fromisoformat(right['utc_timestamp'].replace('Z','+00:00'))
        delta=abs((b-a).total_seconds())/60
        if delta<=15:
            pairs.append((left['event_id'],right['event_id'],int(delta)))
    return events,pairs

def report():
    events,pairs=evaluate()
    lines=['# Fictional 2024 cross-provider investigation report','',
        '**Synthetic demonstration only.** No real records, identifiers or allegations.','',
        f'**Evidence:** {len(rows("evidence_index.csv"))} fictional artifacts; {len(events)} events; {len(pairs)} candidate pairs.','',
        '## Chronological events','','| UTC | Event | Provider | Source pointer |','|---|---|---|---|']
    for e in sorted(events,key=lambda x:x['utc_timestamp']):
        lines.append(f'| {e["utc_timestamp"]} | {e["event_id"]} | {e["provider"]} | {e["source_ref"]} |')
    lines+=['','## Candidate correlations','','| Events | Gap (minutes) | Classification |','|---|---:|---|']
    for left,right,delta in pairs:
        lines.append(f'| {left} / {right} | {delta} | Review only |')
    lines+=['','## Evidence interpretation','',
        '**Observed:** Same-account events occur within the selected window.',
        '**Unresolved:** Authorization, physical-device count, and operator identity.',
        '**Constraint:** Time proximity does not prove causation or compromise.',
        '','## Provenance and corrections','',
        'See evidence_index.csv, identifier_crosswalk.csv and correction_log.csv for fictional source pointers and the preserved timestamp correction.','']
    return '\n'.join(lines)

if __name__=='__main__':
    print(report())
