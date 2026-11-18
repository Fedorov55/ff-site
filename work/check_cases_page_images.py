import os, re
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
s=open(os.path.join(root,'cases.html'),encoding='utf-8').read()
# find img src
srcs=re.findall(r'<img[^>]*src="([^"]+)"', s)
missing=[]
for src in srcs:
    p=src.split('?')[0]
    full=os.path.join(root,p)
    if not os.path.exists(full):
        missing.append(p)
print('Total img src:', len(srcs))
print('Missing:', len(missing))
for m in missing:
    print(' ', m)
# also check srcset
srcsets=re.findall(r'srcset="([^"]+)"', s)
for ss in srcsets:
    for part in ss.split(','):
        url=part.strip().split()[0]
        p=url.split('?')[0]
        full=os.path.join(root,p)
        if not os.path.exists(full):
            print('MISSING srcset:', p)
print('Done')
