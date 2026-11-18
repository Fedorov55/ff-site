s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/backup-checklist.html',encoding='utf-8').read()
import re
m=re.search(r'files/[^\"]+', s)
print('found:', m.group(0) if m else 'NONE')
print('backup-checklist.pdf in s:', 'backup-checklist.pdf' in s)
