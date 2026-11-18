import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
targets = {
    'blog/152fz.html': ('152fz-prep.html', '../152fz-prep.html'),
    'blog/fines-2026.html': ('152fz-prep.html', '../152fz-prep.html'),
    'blog/sisadmin-kazan.html': ('sisadmin-cost.html', '../blog/sisadmin-cost-2026.html'),
    'blog/sisadmin-vs-abonent.html': ('sisadmin-cost.html', '../blog/sisadmin-cost-2026.html'),
    'blog/tco-calc.html': ('sisadmin-cost.html', '../blog/sisadmin-cost-2026.html'),
}

for rel, (old, new) in targets.items():
    path = os.path.join(root, rel)
    s = open(path, encoding='utf-8').read()
    s2 = s.replace(f'href="{old}"', f'href="{new}"')
    if s2 != s:
        open(path, 'w', encoding='utf-8').write(s2)
        print('Updated', rel)
    else:
        print('No change', rel)
print('Done')
