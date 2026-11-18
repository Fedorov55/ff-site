import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
# collect all img src from cases.html
s = open(os.path.join(root, 'cases.html'), encoding='utf-8').read()
srcs = re.findall(r'src="([^"]+)"', s)
srcset = re.findall(r'srcset="([^"]+)"', s)
missing = []
for src in srcs:
    p = src.split('?')[0]
    full = os.path.join(root, p)
    if not os.path.exists(full):
        missing.append(p)
for ss in srcset:
    for part in ss.split(','):
        url = part.strip().split()[0]
        p = url.split('?')[0]
        full = os.path.join(root, p)
        if not os.path.exists(full):
            missing.append(p)
print('Missing images:', len(set(missing)))
for m in sorted(set(missing)):
    print(' ', m)
