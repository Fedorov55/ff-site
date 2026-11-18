import re, json, os
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
s=open(os.path.join(root,'cases.html'),encoding='utf-8').read()
ms=re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
# find Organization blocks
for i,m in enumerate(ms):
    d=json.loads(m)
    items=d.get('@graph',[d]) if isinstance(d,dict) else [d]
    for it in items:
        if isinstance(it,dict) and it.get('@type')=='Organization':
            print('Block', i)
            print(json.dumps(it, ensure_ascii=False, indent=2))
            print()
