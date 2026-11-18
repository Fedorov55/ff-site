import os, re
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files=['blog/backup-3-2-1.html','blog/sisadmin-cost-2026.html','152fz-prep.html','vpn.html','blog/server-1c-saturday.html']
for fn in files:
    s=open(os.path.join(root,fn),encoding='utf-8').read()
    c=re.search(r'<link rel="canonical" href="([^"]*)">',s)
    print(fn, '->', c.group(1) if c else 'NONE')
