import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

# Fix blog links
for f in ['blog/152fz.html', 'blog/fines-2026.html']:
    path = os.path.join(root, f)
    s = open(path, encoding='utf-8').read()
    s = s.replace('../../services/152fz.html', '../services/152fz.html')
    open(path, 'w', encoding='utf-8').write(s)
    print('Fixed', f)

# Fix rss.xml in services/152fz.html
path = os.path.join(root, 'services/152fz.html')
s = open(path, encoding='utf-8').read()
s = s.replace('href="rss.xml"', 'href="../rss.xml"')
open(path, 'w', encoding='utf-8').write(s)
print('Fixed services/152fz.html rss.xml')

print('Done')
