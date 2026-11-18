import re
for f in ['blog/it-outsourcing-cost-kazan-2026.html','blog/cost-of-downtime.html','blog/3-year-tco-comparison.html']:
    s=open(f,encoding='utf-8').read()
    m=re.search(r'description" content="([^"]*)"', s)
    desc=m.group(1)
    print(f)
    print('  has <:', '<' in desc, 'has >:', '>' in desc)
    print('  desc:', desc)
    print()
