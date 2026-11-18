import re
path='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/about.html'
s=open(path,encoding='utf-8').read()
original=s

pat=re.compile(r'<section class="section reveal u-pt-0" aria-label="Смотрите также">.*?</section>', re.S)
matches=pat.findall(s)
print('Смотрите также sections:', len(matches))
if len(matches)>1:
    # keep first, remove rest
    first=matches[0]
    s=pat.sub('', s)
    # add one before </main>
    s=s.replace('</main>', first+'\n</main>', 1)

open(path,'w',encoding='utf-8').write(s)
print('Done')
s2=open(path,encoding='utf-8').read()
print('Смотрите также remaining:', len(pat.findall(s2)))
print('H1 count:', len(re.findall(r'<h1[^>]*>', s2)))
