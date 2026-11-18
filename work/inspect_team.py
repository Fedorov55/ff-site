import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/team.html',encoding='utf-8').read()
for m in re.finditer(r'<div class="team-card".*?</div>\s*</div>', s, re.S):
    print(m.group(0)[:500])
    print('---')
print('done')
