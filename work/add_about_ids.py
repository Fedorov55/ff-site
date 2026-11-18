import re

path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/about.html'
s = open(path, encoding='utf-8').read()
original = s

# Add id to sections based on their heading text
section_ids = {
    'О F&F': 'about',
    'Четыре человека, которые отвечают за ваш офис': 'team',
    'Как устроена работа с F&F': 'methodology',
    'Trust Center': 'trust',
    'Вы слышите про сервер. Мы его поднимаем.': 'partners',
}

# We'll add id to <section class="section reveal"> that contains a specific h2
for heading, sid in section_ids.items():
    # find section containing this heading
    pat = re.compile(r'(<section class="section reveal")(?![^>]*id=)([^>]*>)(?:(?!</section>).)*?' + re.escape(heading), re.S)
    def repl(m):
        return m.group(1) + f' id="{sid}"' + m.group(2)
    s = pat.sub(repl, s, count=1)

# Add table of contents after page-intro
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
marker = '<section class="section reveal" id="about">'
if marker not in s:
    marker = '<main id="main" class="site-main">'
    if marker in s:
        s = s.replace(marker, marker + '\n' + toc, 1)
else:
    # insert before first section with id=about
    s = s.replace(marker, toc + marker, 1)

open(path, 'w', encoding='utf-8').write(s)
print('Done')
# verify
s2 = open(path, encoding='utf-8').read()
print('H1 count:', len(re.findall(r'<h1[^>]*>', s2)))
print('id=about:', 'id="about"' in s2)
print('id=team:', 'id="team"' in s2)
print('id=methodology:', 'id="methodology"' in s2)
print('id=trust:', 'id="trust"' in s2)
print('id=partners:', 'id="partners"' in s2)
