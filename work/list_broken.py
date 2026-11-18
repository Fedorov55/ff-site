import os, re
root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
html_files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            html_files.append(os.path.join(r, f))
existing = set(os.path.relpath(f, root).replace('\\', '/') for f in html_files)
broken = []
for f in html_files:
    rel = os.path.relpath(f, root).replace('\\', '/')
    s = open(f, encoding='utf-8', errors='replace').read()
    d = os.path.dirname(rel)
    for m in re.finditer(r'href="([^"]+)"', s):
        href = m.group(1)
        if href.startswith(('http', 'mailto', 'tel', 'javascript', 'data:', '#')) or href == '':
            continue
        pp = href.split('?')[0].split('#')[0]
        target = pp.lstrip('/') if pp.startswith('/') else os.path.normpath(os.path.join(d, pp)).replace('\\', '/')
        if target == '.' or target in existing or os.path.exists(os.path.join(root, target)):
            continue
        broken.append((rel, href))
print('BROKEN:', len(broken))
for b in broken:
    print(b[0], '->', b[1])
