import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = [os.path.join(root, f) for f in os.listdir(root) if f.startswith('industry-') and f.endswith('.html')]

faq_section_pat = re.compile(r'<section class="section">\s*<div class="container">(?:(?!</section>).)*?Частые вопросы(?:(?!</section>).)*?</section>', re.S)
faq_schema_pat = re.compile(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>', re.S)

for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    s2 = faq_section_pat.sub('', s)
    s2 = faq_schema_pat.sub('', s2)
    # add compact FAQ link before </main> if not present
    if 'faq.html' not in s2:
        link = '\n<section class="section reveal u-pt-0"><div class="container u-center"><p class="u-text-2-sm">Частые вопросы по IT для вашей отрасли — в <a href="faq.html" class="u-gold">общем FAQ</a>.</p></div></section>\n'
        s2 = s2.replace('</main>', link + '</main>', 1)
    if s2 != original:
        open(f, 'w', encoding='utf-8').write(s2)
        print('Updated', os.path.basename(f))
    else:
        print('No change', os.path.basename(f))
print('Done')
