import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
mojibake_chars = set()
for c in s:
    if ord(c) > 127 and not (0x0400 <= ord(c) <= 0x04FF) and c not in '—–…«»„“”' and c not in ' \xa0':
        mojibake_chars.add(c)
print('mojibake chars:', mojibake_chars)
for m in re.finditer(r'[\x80-\xff]{3,}', s):
    print('MOJI:', repr(m.group(0)[:60]))
print('Done')
