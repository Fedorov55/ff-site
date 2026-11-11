import re
s = open('support.html', encoding='utf-8').read()

# Remove orphan CTA section (section 9: double-cta without heading)
s = re.sub(r'<section class="section reveal" style="padding-top:24px;">\s*<div class="container">\s*<div style="max-width:760px;margin:0 auto;text-align:center;">\s*<div class="double-cta">\s*<a href="services.html#estimate" class="btn btn--primary">Рассчитать стоимость</a>.*?</section>\s*', '', s, flags=re.S)

# Remove "Мы не пряchem цены..." section
s = re.sub(r'<section[^>]*>.*?Мы не пряchem цены и не держим вас заложником.*?</section>\s*', '', s, flags=re.S)

open('support.html', 'w', encoding='utf-8').write(s)
print('done')