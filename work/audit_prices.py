import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
print('=== H1 count ===')
hs=re.findall(r'<h1[^>]*>(.*?)</h1>', s, re.S)
print(len(hs))
for h in hs: print(' ', re.sub(r'<[^>]+>','',h).strip()[:60])
print()
print('=== Sections ===')
secs=re.findall(r'<section[^>]*>(.*?)</section>', s, re.S)
print('Total sections:', len(secs))
for i,sec in enumerate(secs):
    h=re.search(r'<h[123][^>]*>(.*?)</h[123]>', sec, re.S)
    t=re.sub(r'<[^>]+>','',h.group(1)).strip() if h else 'NO HEADING'
    print(f'  {i+1:2d}. {t[:60]}')
print()
# mojibake
moji=[c for c in s if ord(c)>127 and not (0x0400<=ord(c)<=0x04FF) and c not in '—–…«»„“”' and c not in ' \xa0·→₽©×']
print('mojibake chars:', set(moji))
# duplicate sections
from collections import Counter
sec_texts = [re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',sec)).strip() for sec in secs]
dup = [t for t,c in Counter(sec_texts).items() if c>1]
print('duplicate sections:', len(dup))
for d in dup: print('  DUP:', d[:80])
print('Done')
