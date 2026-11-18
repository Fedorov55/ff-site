import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = ['vpn.html', 'cases.html', 'blog/it-outsourcing-cost-kazan-2026.html', 'blog/cost-of-downtime.html', 'blog/3-year-tco-comparison.html']

for rel in files:
    path = os.path.join(root, rel)
    s = open(path, encoding='utf-8').read()
    original = s
    # Fix unescaped > in meta descriptions: replace ">\"" at end of content with "&gt;\""? Actually the error is spec-char-escape: > must be escaped as &gt;
    # Simplest: replace ">>" or ">\"" patterns in meta content? Let's just replace 'F&F.">' with 'F&F.&gt;'? 
    # The errors show '... F&F.">' — a > before closing quote. Replace ">\"" with "&gt;\"" globally? Risky.
    # Instead, target specific patterns
    s = s.replace('Исследование F&F.">', 'Исследование F&F.&gt;')
    s = s.replace('Расчёт F&F.">', 'Расчёт F&F.&gt;')
    # vpn.html: check line 230
    # cases.html: img srcset has unescaped < ? Actually error says [ < ] on line 202. Let's inspect.
    if s != original:
        open(path, 'w', encoding='utf-8').write(s)
        print(f'Updated {rel}')
    else:
        print(f'No changes {rel}')
print('Done')
