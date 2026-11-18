import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = [os.path.join(root, f) for f in os.listdir(root) if f.startswith('industry-') and f.endswith('.html')]

# regex for visible FAQ section
faq_section_re = re.compile(r'<section class="section">\s*<div class="container">\s*<div class="section__head fade-up">\s*<span class="section__label">FAQ</span>\s*<h2 class="section__title">Частые вопросы</h2>\s*</div>\s*<div class="faq">.*?</div>\s*</div>\s*</section>', re.S)
# regex for FAQPage json-ld
faq_schema_re = re.compile(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>', re.S)

for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    # remove visible FAQ section
    s2 = faq_section_re.sub('', s)
    # remove FAQPage schema
    s2 = faq_schema_re.sub('', s2)
    # insert compact link before </main> if not already
    if 'faq.html' not in s2.split('</main>')[0].split('Смотрите также')[-1] if '</main>' in s2 else True:
        link = '\n<section class="section reveal u-pt-0"><div class="container u-center"><p class="u-text-2-sm">Частые вопросы по IT для вашей отрасли — в <a href="faq.html" class="u-gold">общем FAQ</a>.</p></div></section>\n'
        s2 = s2.replace('</main>', link + '</main>', 1)
    if s2 != original:
        open(f, 'w', encoding='utf-8').write(s2)
        print('Updated', os.path.basename(f))
    else:
        print('No change', os.path.basename(f))
print('Done')
