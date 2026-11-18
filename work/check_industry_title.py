import os, re
root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = sorted([f for f in os.listdir(root) if f.startswith('industry-') and f.endswith('.html')])
for f in files:
    s = open(os.path.join(root, f), encoding='utf-8').read()
    m = re.search(r'<title>(.*?)</title>', s)
    title = m.group(1) if m else 'NONE'
    print(f'{f:35s} | {title}')
print('Total:', len(files))
