import re, os
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
f='industry-clinics.html'
s=open(os.path.join(root,f),encoding='utf-8').read()
pat = re.compile(r'<section class="section">\s*<div class="container">(?:(?!</section>).)*?Частые вопросы(?:(?!</section>).)*?</section>', re.S)
print('matches:', len(pat.findall(s)))
s2 = pat.sub('', s)
# remove FAQPage schema
schema_pat = re.compile(r'<script type="application/ld\+json">\{"@context": "https:// schema.org", "@type": "FAQPage".*?</script>', re.S)
# fix pattern
schema_pat = re.compile(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>', re.S)
print('schema matches:', len(schema_pat.findall(s2)))
s2 = schema_pat.sub('', s2)
print('len before', len(s), 'after', len(s2))
open(os.path.join(root,'work','test_out2.html'),'w',encoding='utf-8').write(s2)
print('written')
