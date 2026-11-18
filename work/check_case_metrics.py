import os, re
root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = sorted([f for f in os.listdir(os.path.join(root, 'cases')) if f.startswith('case-') and f.endswith('.html')])
for f in files:
    s = open(os.path.join(root, 'cases', f), encoding='utf-8').read()
    m = re.search(r'<div class="case-card__result">(.*?)</div>', s, re.S)
    r = re.sub(r'<[^>]+>', ' ', m.group(1)).strip() if m else 'NONE'
    print(f'{f:35s} -> {r[:80]}')
print('Total:', len(files))
