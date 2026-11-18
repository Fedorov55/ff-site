import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/cases.html',encoding='utf-8').read()
cards=re.findall(r'class="case-card', s)
print('case-card count:', len(cards))
links=re.findall(r'href="(cases/[^"]+)"', s)
print('case links:', len(links))
for l in sorted(set(links)):
    print(' ', l)
# also check for case- links
case_links=re.findall(r'href="(cases/case-[^"]+)"', s)
print('case-* links:', len(case_links))
for l in sorted(set(case_links)):
    print(' ', l)
