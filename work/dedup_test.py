import re, os
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
f='industry-clinics.html'
s=open(os.path.join(root,f),encoding='utf-8').read()
faq_section_re = re.compile(r'<section class="section">\s*<div class="container">\s*<div class="section__head fade-up">\s*<span class="section__label">FAQ</span>\s*<h2 class="section__title">Частые вопросы</h2>\s*</div>\s*<div class="faq">.*?</div>\s*</div>\s*</section>', re.S)
faq_schema_re = re.compile(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>', re.S)
s2 = faq_section_re.sub('', s)
s2 = faq_schema_re.sub('', s2)
print('section removed:', s != s2 and 'section' in (s if False else ''))
print('faq_section matches:', len(faq_section_re.findall(s)))
print('faq_schema matches:', len(faq_schema_re.findall(s)))
# show diff size
print('len before', len(s), 'after', len(s2))
open(os.path.join(root,'work','test_out.html'),'w',encoding='utf-8').write(s2)
print('written test_out.html')
