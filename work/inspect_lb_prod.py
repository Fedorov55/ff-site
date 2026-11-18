import re, json, os
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
for f in ['cases.html','services.html']:
    s=open(os.path.join(root,f),encoding='utf-8').read()
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        d=json.loads(m.group(1))
        items=d.get('@graph',[d]) if isinstance(d,dict) else [d]
        for it in items:
            if isinstance(it,dict) and it.get('@type') in ('LocalBusiness','Product'):
                print(f, '->', json.dumps(it, ensure_ascii=False)[:200])
                print()
