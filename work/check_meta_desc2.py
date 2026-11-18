import re
for f in ['blog/it-outsourcing-cost-kazan-2026.html','blog/cost-of-downtime.html','blog/3-year-tco-comparison.html']:
    s=open(f,encoding='utf-8').read()
    m=re.search(r'description" content="([^"]*)"', s)
    print(f, '->', repr(m.group(1)[:120]) if m else 'NONE')
    print()
