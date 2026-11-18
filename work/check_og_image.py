import re
for f in ['cases/server-turnkey.html','cases/tatar-septic.html','cases/tobacco.html']:
    s=open(f,encoding='utf-8').read()
    m=re.search(r'<meta property="og:image" content="(.*?)">', s)
    print(f, '->', m.group(1) if m else 'NONE')
