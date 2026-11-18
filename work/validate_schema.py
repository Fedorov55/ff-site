import os, json, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

errors = 0
pages_no_schema = []
for f in files:
    s = open(f, encoding='utf-8').read()
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    if not schemas:
        pages_no_schema.append(os.path.relpath(f, root))
        continue
    for sch in schemas:
        try:
            data = json.loads(sch)
            # basic validation
            if '@type' not in data and not (isinstance(data, list) and data and '@type' in data[0]):
                print('Missing @type:', os.path.relpath(f, root))
                errors += 1
        except Exception as e:
            print('Invalid JSON-LD:', os.path.relpath(f, root), str(e)[:80])
            errors += 1

print('Pages without schema:', len(pages_no_schema))
if pages_no_schema:
    print(pages_no_schema[:10])
print('Schema errors:', errors)
print('Total pages:', len(files))
