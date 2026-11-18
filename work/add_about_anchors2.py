path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/about.html'
s = open(path, encoding='utf-8').read()
original = s

replacements = [
    ('<h2>Четыре человека, которые отвечают за ваш офис</h2>', '<h2 id="team">Четыре человека, которые отвечают за ваш офис</h2>'),
    ('<h2 class="page-intro__title">Как устроена работа с F&F</h2>', '<h2 class="page-intro__title" id="methodology">Как устроена работа с F&F</h2>'),
    ('<h2 class="page-intro__title">Trust Center</h2>', '<h2 class="page-intro__title" id="trust">Trust Center</h2>'),
]

for old, new in replacements:
    if old in s:
        s = s.replace(old, new, 1)
        print(f'Added id: {new[:60]}')
    else:
        print(f'NOT FOUND: {old[:60]}')

# Add id to H1 "О F&F"
s = s.replace('<h1 class="section__title reveal">О F&F</h1>', '<h1 class="section__title reveal" id="about">О F&F</h1>', 1)

# Add TOC after first </section> (page-intro)
toc = '''
<section class="section reveal u-pt-0">
<div class="container">
<div class="u-max-760">
<h3 class="u-title-16">О компании</h3>
<div class="u-flex" style="flex-wrap:wrap;gap:8px;">
<a href="#about" class="btn btn--ghost btn--sm">О F&F</a>
<a href="#team" class="btn btn--ghost btn--sm">Команда</a>
<a href="#methodology" class="btn btn--ghost btn--sm">Как мы работаем</a>
<a href="#trust" class="btn btn--ghost btn--sm">Доверие и SLA</a>
<a href="#partners" class="btn btn--ghost btn--sm">Партнёрам</a>
</div>
</div>
</div>
</section>
'''
first_sec_end = s.find('</section>')
if first_sec_end != -1 and 'О компании' not in s[:first_sec_end+200]:
    s = s[:first_sec_end+len('</section>')] + '\n' + toc + s[first_sec_end+len('</section>'):]

open(path, 'w', encoding='utf-8').write(s)
print('Done')
# verify
s2 = open(path, encoding='utf-8').read()
print('H1 count:', len(__import__('re').findall(r'<h1[^>]*>', s2)))
print('id=about:', 'id="about"' in s2)
print('id=team:', 'id="team"' in s2)
print('id=methodology:', 'id="methodology"' in s2)
print('id=trust:', 'id="trust"' in s2)
print('id=partners:', 'id="partners"' in s2)
