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

fixed_total = 0
for f in html_files:
    rel = os.path.relpath(f, root).replace('\\', '/')
    d = os.path.dirname(rel)
    if d == '.':
        continue  # root-level files: links are already correct
    s = open(f, encoding='utf-8').read()
    original = s

    def replacer(m):
        global fixed_total
        href = m.group(1)
        # only simple relative links without path separators or protocols
        if href.startswith(('http', 'mailto', 'tel', 'javascript', 'data:', '#', '/')):
            return m.group(0)
        pp = href.split('?')[0].split('#')[0]
        # target relative to current dir
        target = os.path.normpath(os.path.join(d, pp)).replace('\\', '/')
        if target in existing or os.path.exists(os.path.join(root, target)):
            return m.group(0)
        # try one level up
        up_target = os.path.normpath(os.path.join(d, '..', pp)).replace('\\', '/')
        if up_target in existing or os.path.exists(os.path.join(root, up_target)):
            fixed_total += 1
            # preserve query/hash
            suffix = href[len(pp):]
            return 'href="../' + pp + suffix + '"'
        return m.group(0)

    s = re.sub(r'href="([^"]+)"', replacer, s)
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)

print('Fixed links:', fixed_total)
