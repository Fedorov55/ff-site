import re, json, os
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
s=open(os.path.join(root,'cases.html'),encoding='utf-8').read()
for i,m in enumerate(re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)):
    d=json.loads(m.group(1))
    items=d.get('@graph',[d]) if isinstance(d,dict) else [d]
    for it in items:
        if isinstance(it,dict):
            print(i, it.get('@type'), json.dumps(it, ensure_ascii=False)[:250])
            print()
