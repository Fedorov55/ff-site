import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

# blog.html: update links
p = os.path.join(root, 'blog.html')
s = open(p, encoding='utf-8').read()
s = s.replace('articles/backup-3-2-1.html', 'blog/backup-3-2-1.html')
s = s.replace('articles/152fz-prep.html', '152fz-prep.html')
s = s.replace('blog/152fz-prep.html', '152fz-prep.html')
s = s.replace('blog/vpn-udalenny-dostup.html', 'vpn.html')
s = s.replace('blog/sisadmin-cost.html', 'blog/sisadmin-cost-2026.html')
open(p, 'w', encoding='utf-8').write(s)
print('updated blog.html')

# map.html
p = os.path.join(root, 'map.html')
s = open(p, encoding='utf-8').read()
s = s.replace('blog/vpn-udalenny-dostup.html', 'vpn.html')
open(p, 'w', encoding='utf-8').write(s)
print('updated map.html')

# services.html
p = os.path.join(root, 'services.html')
s = open(p, encoding='utf-8').read()
s = s.replace('blog/sisadmin-cost.html', 'blog/sisadmin-cost-2026.html')
open(p, 'w', encoding='utf-8').write(s)
print('updated services.html')

# articles/tco-calc.html
p = os.path.join(root, 'articles', 'tco-calc.html')
if os.path.exists(p):
    s = open(p, encoding='utf-8').read()
    s = s.replace('blog/sisadmin-cost.html', 'blog/sisadmin-cost-2026.html')
    open(p, 'w', encoding='utf-8').write(s)
    print('updated articles/tco-calc.html')
print('Done')
