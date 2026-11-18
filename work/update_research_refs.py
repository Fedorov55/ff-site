import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# Step 1: global replace research.html -> research-msb.html
for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    s = s.replace('research.html', 'research-msb.html')
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)

# Step 2: revert nav dropdowns and mobile menu to research.html (hub)
for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    # desktop dropdown
    s = s.replace('research-msb.html" class="dropdown__link">Исследования</a>', 'research.html" class="dropdown__link">Исследования</a>')
    # mobile
    s = s.replace('research-msb.html" class="mobile-nav__link">Исследования</a>', 'research.html" class="mobile-nav__link">Исследования</a>')
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)

# Step 3: fix relative paths for root-level pages (research-msb.html in root, but if in subdir needs ../)
# Already handled by original links? The global replace kept relative prefixes. Good.

print('Done')
# verify
s = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
print('index.html research dropdown:', 'research.html' in s and 'research-msb.html' in s)
print('research-msb refs in index:', s.count('research-msb.html'))
