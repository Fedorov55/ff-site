import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/style.css',encoding='utf-8').read()
for m in re.finditer(r'\.[a-zA-Z0-9_-]+\{[^}]*font-size:14px[^}]*color:var\(--text-2\)[^}]*\}', s):
    print(m.group(0)[:150])
print('---done---')
# also search for u-text-2 with margin
for m in re.finditer(r'\.[a-zA-Z0-9_-]+\{[^}]*margin:0 0 8px[^}]*\}', s):
    print('margin class:', m.group(0)[:120])
