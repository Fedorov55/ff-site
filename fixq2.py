p = '_hotite6.py'
s = open(p, encoding='utf-8').read()
lines = s.split(chr(10))
if lines and lines[-1].strip() == '"':
    lines = lines[:-1]
open(p, 'w', encoding='utf-8').write(chr(10).join(lines))
print('fixed')