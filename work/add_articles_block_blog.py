path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/blog.html'
s = open(path, encoding='utf-8').read()
original = s

block = '''
<section class="section reveal u-pt-0">
<div class="container">
<div class="u-max-760">
<h3 class="u-title-16">Статьи и исследования</h3>
<p style="color:var(--text-2);font-size:14px;margin:0 0 12px;">Гайды, исследования и калькуляторы по IT для бизнеса.</p>
<a href="articles.html" class="btn btn--ghost btn--sm">Все статьи и исследования →</a>
</div>
</div>
</section>
'''

if '</main>' in s:
    s = s.replace('</main>', block + '</main>', 1)
    open(path, 'w', encoding='utf-8').write(s)
    print('Updated blog.html')
else:
    print('No </main> found')
print('Done')
