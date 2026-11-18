import re

path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/support.html'
s = open(path, encoding='utf-8').read()
original = s

# Pattern: a div containing a testimonial quote
pat = re.compile(r'<div style="padding:20px;border:1px solid var\(--border\);border-radius:12px;background:var\(--card\);">\s*<p style="color:var\(--text-2\);font-size:14px;font-style:italic;margin:0 0 12px;">.*?</p>\s*<div style="font-size:13px;color:var\(--muted\);">.*?</div>\s*</div>', re.S)
matches = pat.findall(s)
print('Found testimonial blocks:', len(matches))

# Keep first, replace rest with compact link
compact = '<div style="padding:20px;border:1px solid var(--border);border-radius:12px;background:var(--card);text-align:center;"><p style="color:var(--text-2);font-size:14px;margin:0 0 8px;">Кейс: экономия до 660 000 ₽/год, 0 простоев.</p><a href="cases.html" class="u-gold">Все кейсы →</a></div>'

count = [0]
def repl(m):
    count[0] += 1
    if count[0] == 1:
        return m.group(0)
    return compact

s2 = pat.sub(repl, s)
# protect script blocks (none affected, but safe)
if s2 != original:
    open(path, 'w', encoding='utf-8').write(s2)
    print(f'Replaced {count[0]-1} testimonial blocks on support.html')
else:
    print('No changes')
print('Done')
