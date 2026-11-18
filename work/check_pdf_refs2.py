import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

all_text = ''
for f in files:
    all_text += open(f, encoding='utf-8', errors='replace').read()

# check files/ dir
files_dir = os.path.join(root, 'files')
if os.path.exists(files_dir):
    for f in os.listdir(files_dir):
        rel = 'files/' + f
        if rel not in all_text:
            print(f'UNUSED: {rel}')
        else:
            print(f'USED: {rel}')
print('Done')
