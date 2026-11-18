import os, re, json

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

for f in files:
    s = open(f, encoding='utf-8').read()
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    faq_count = 0
    for sch in schemas:
        try:
            data = json.loads(sch)
            items = data.get('@graph', [data]) if isinstance(data, dict) else [data]
            for item in items:
                if isinstance(item, dict) and item.get('@type') == 'FAQPage':
                    faq_count += 1
        except:
            pass
    if faq_count > 1:
        print(f'{os.path.relpath(f, root)}: FAQPage x{faq_count}')
        # show first question of each
        for sch in schemas:
            try:
                data = json.loads(sch)
                items = data.get('@graph', [data]) if isinstance(data, dict) else [data]
                for item in items:
                    if isinstance(item, dict) and item.get('@type') == 'FAQPage':
                        q = item.get('mainEntity', [{}])[0].get('name', '?')[:60]
                        print(f'   -> {q}')
            except:
                pass
# also check LocalBusiness and Product
print('\n--- LocalBusiness / Product ---')
for f in files:
    s = open(f, encoding='utf-8').read()
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for sch in schemas:
        try:
            data = json.loads(sch)
            items = data.get('@graph', [data]) if isinstance(data, dict) else [data]
            for item in items:
                if isinstance(item, dict) and item.get('@type') in ('LocalBusiness', 'Product'):
                    print(f'{os.path.relpath(f, root)}: {item.get("@type")} - {item.get("name","?")}')
        except:
            pass
