import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/about.html'
s = open(path, encoding='utf-8').read()
matches = list(re.finditer(r'<h1[^>]*>(.*?)</h1>', s, re.S))
# keep first, change rest to h2
for m in reversed(matches[1:]):
    tag = m.group(0)
    new_tag = tag.replace('<h1', '<h2', 1).replace('</h1>', '</h2>', 1)
    s = s[:m.start()] + new_tag + s[m.end():]
open(path, 'w', encoding='utf-8').write(s)
print(f'Changed {len(matches)-1} H1 to H2')
print('Done')
# verify
s2 = open(path, encoding='utf-8').read()
hs = re.findall(r'<h1[^>]*>', s2)
print('H1 count now:', len(hs))
