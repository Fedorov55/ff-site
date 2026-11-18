s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
moji=[c for c in s if ord(c)>127 and not (0x0400<=ord(c)<=0x04FF) and c not in '—–…«»„“”' and c not in ' \xa0·→₽©×']
print('mojibake:', set(moji))
import re
hs=re.findall(r'<h1[^>]*>(.*?)</h1>', s, re.S)
print('H1 count:', len(hs))
print('Done')
