import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = ['blog/it-outsourcing-cost-kazan-2026.html', 'blog/cost-of-downtime.html', 'blog/3-year-tco-comparison.html']

for rel in files:
    path = os.path.join(root, rel)
    s = open(path, encoding='utf-8').read()
    original = s
    # Fix the broken escape: &gt;> -> &gt;"
    s = s.replace('&gt;>\n<meta', '&gt;">\n<meta')
    s = s.replace('&gt;><meta', '&gt;"><meta')
    # Also handle case where newline not present
    s = s.replace('&gt;>', '&gt;">')
    open(path, 'w', encoding='utf-8').write(s)
    print(f'Updated {rel}: changed={s != original}')
print('Done')
