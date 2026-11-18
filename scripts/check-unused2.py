import os, re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Collect all text from HTML + CSS + JS
all_text = ''
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith(('.html', '.css', '.js')):
            all_text += open(os.path.join(r, f), encoding='utf-8', errors='replace').read()

for subdir in ['img', 'fonts', 'files', 'pdf', 'js', 'data']:
    dirpath = os.path.join(root, subdir)
    if not os.path.exists(dirpath):
        continue
    for r, ds, fs in os.walk(dirpath):
        for f in fs:
            rel = os.path.relpath(os.path.join(r, f), root).replace('\\', '/')
            if rel not in all_text:
                print(f'UNUSED: {rel}')

print('Done')
