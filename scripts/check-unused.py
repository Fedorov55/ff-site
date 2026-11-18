import os, re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            html_files.append(os.path.join(r, f))

all_html = ''
for f in html_files:
    all_html += open(f, encoding='utf-8', errors='replace').read()

# collect all file references in HTML
referenced = set()
for m in re.finditer(r'(?:src|href)="([^"]+)"', all_html):
    href = m.group(1).split('?')[0].split('#')[0]
    if href.startswith(('http', 'mailto', 'tel', 'javascript', 'data:', '#')) or href == '':
        continue
    referenced.add(href)

# check directories
for subdir in ['img', 'fonts', 'files', 'pdf', 'js', 'data']:
    dirpath = os.path.join(root, subdir)
    if not os.path.exists(dirpath):
        continue
    for r, ds, fs in os.walk(dirpath):
        for f in fs:
            rel = os.path.relpath(os.path.join(r, f), root).replace('\\', '/')
            if rel not in referenced:
                print(f'UNUSED: {rel}')

print('Done')
