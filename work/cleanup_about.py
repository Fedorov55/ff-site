import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/about.html'
s = open(path, encoding='utf-8').read()
original = s

# Remove duplicate "Смотрите также" sections (keep first)
see_also_pat = re.compile(r'<section class="section reveal u-pt-0" aria-label="Смотрите также">.*?</section>', re.S)
matches = see_also_pat.findall(s)
print('Смотрите также sections found:', len(matches))
if len(matches) > 1:
    # keep first, remove rest
    first = matches[0]
    # replace all with first, then remove extras
    # We'll remove all and add one at the end before </main>
    s = see_also_pat.sub('', s)
    # add one before </main>
    s = s.replace('</main>', first + '\n</main>', 1)

# Remove duplicate "Нужна смета или консультация?" sections (keep first)
smeta_pat = re.compile(r'<section class="section reveal u-pt-0">\s*<div class="container u-center">\s*<h2[^>]*>Нужна смета или консультация\?</h2>.*?</section>', re.S)
smatches = smeta_pat.findall(s)
print('Нужна смета sections found:', len(smatches))
if len(smatches) > 1:
    s = smeta_pat.sub('', s)
    # add one before </main> (after see_also)
    smeta_block = smatches[0]
    s = s.replace('</main>', smeta_block + '\n</main>', 1)

open(path, 'w', encoding='utf-8').write(s)
print('Done')
# verify
s2 = open(path, encoding='utf-8').read()
print('Смотрите также remaining:', len(see_also_pat.findall(s2)))
print('Нужна смета remaining:', len(smeta_pat.findall(s2)))
print('H1 count:', len(re.findall(r'<h1[^>]*>', s2)))
