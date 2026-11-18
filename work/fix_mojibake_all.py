import re

path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(path, encoding='utf-8').read()
original = s

# Fix mojibake: UTF-8 bytes misread as CP1251
def fix_moji(text):
    try:
        return text.encode('cp1251').decode('utf-8')
    except:
        return text

# Find sequences of mojibake chars (Cyrillic mojibake)
moji_chars = '╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀■□▪▫▬▲►◄↕‼¶§▬ '
# Pattern: 2+ consecutive mojibake chars
pat = re.compile(r'[\u00c0-\u00ff\u2500-\u259f]{2,}')
def repl(m):
    return fix_moji(m.group(0))
s = pat.sub(repl, s)

open(path, 'w', encoding='utf-8').write(s)
print('Fixed mojibake')
# verify
s2 = open(path, encoding='utf-8').read()
moji = [c for c in s2 if ord(c)>127 and not (0x0400<=ord(c)<=0x04FF) and c not in '—–…«»„“”' and c not in ' \xa0·→₽©']
print('remaining mojibake chars:', set(moji))
print('Done')
