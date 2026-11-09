#!/usr/bin/env python3
"""Generate a shareable PDF from the fictional 2024 case-study CSVs.

Requires: pip install reportlab
Run: python demo/publish_report.py --output fictional_case_report.pdf
"""
import argparse
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
try:
    from demo.case_study_report import evaluate, rows
except ModuleNotFoundError:
    from case_study_report import evaluate, rows

def generate_pdf(output):
    events, pairs = evaluate()
    artifacts = rows('evidence_index.csv')
    corrections = rows('correction_log.csv')
    navy=colors.HexColor('#12253D')
    teal=colors.HexColor('#137D86')
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='ForensicTitle',parent=styles['Title'],fontSize=19,leading=24,textColor=navy,spaceAfter=12))
    styles.add(ParagraphStyle(name='ForensicSection',parent=styles['Heading2'],fontSize=12,textColor=teal,spaceBefore=15,spaceAfter=8))
    styles.add(ParagraphStyle(name='ForensicBody',parent=styles['BodyText'],fontSize=9,leading=14,spaceAfter=8))
    styles.add(ParagraphStyle(name='ForensicCell',parent=styles['BodyText'],fontSize=8,leading=11))
    def p(value,kind='ForensicBody'):
        return Paragraph(escape(str(value)),styles[kind])
    def tbl(data,widths):
        table=Table([[p(cell,'ForensicCell') for cell in row] for row in data],colWidths=widths,repeatRows=1,hAlign='LEFT')
        table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DDE9EE')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F1F6F8')]),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
        return table
    story=[p('Digital Identity Forensics | Case Study','ForensicTitle'),
        p('FICTIONAL 2024 INVESTIGATION  •  Synthetic records only'),
        p('Executive summary','ForensicSection'),
        p(f'{len(artifacts)} fictional source artifacts and {len(events)} source-linked events produced {len(pairs)} same-account candidate pairs within 15 minutes. Temporal correlation does not establish unauthorized access, causation, device count, or operator identity.'),
        p('Chronological event timeline','ForensicSection'),
        tbl([['UTC','Event','Provider','Source reference']]+[[e['utc_timestamp'],e['event_id'],e['provider'],e['source_ref']] for e in sorted(events,key=lambda x:x['utc_timestamp'])],[145,65,115,125]),
        p('Correlation review','ForensicSection'),
        tbl([['Event pair','Gap','Classification']]+[[f'{a} / {b}',f'{minutes} min','Review required; no attribution'] for a,b,minutes in pairs],[145,65,240]),
        p('Corrections and evidence provenance','ForensicSection'),
        p(f'{len(corrections)} documented fictional correction(s). Original timestamp and normalized UTC timestamp are retained. Source references point back to the fictional evidence index.'),
        p('Observations, interpretation, and constraints','ForensicSection'),
        p('Observed: same-account events occurred within the configured window. Unresolved: authorization, provider semantics, source clock accuracy, physical device identity, and operator identity.'),
        p('Limitations: This report is a synthetic teaching artifact, not a real incident finding. Logical client identifiers do not prove multiple physical devices or people.'),
        p('Reproducibility','ForensicSection'),
        p('Generated directly from the fictional CSV source tables in examples/case-study-2024. Re-run using python demo/publish_report.py --output fictional_case_report.pdf.') ]
    output=Path(output)
    output.parent.mkdir(parents=True,exist_ok=True)
    SimpleDocTemplate(str(output),pagesize=(612,792),leftMargin=48,rightMargin=48,topMargin=45,bottomMargin=45).build(story)
    return output

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='fictional_case_report.pdf')
    args=parser.parse_args()
    print(generate_pdf(args.output))
