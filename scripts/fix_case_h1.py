import os, re
root='C:/opencode/f&f/site'
cases_dir=os.path.join(root,'cases')
old_h1_text='Сервер под ключ для офиса на 25 человек'
for f in os.listdir(cases_dir):
    if not f.endswith('.html'):
        continue
    p=os.path.join(cases_dir,f)
    s=open(p,encoding='utf-8').read()
    if old_h1_text not in s:
        continue
    # get title
    m=re.search(r'<title>(.*?)</title>',s,re.S)
    title=m.group(1).strip() if m else ''
    # strip " | F&F" or " | F&F — Казань | F&F"
    h1_text=title.replace(' | F&F','').replace(' | F&F — Казань','').strip()
    old_h1=f'<h1 class="article-title">{old_h1_text}</h1>'
    new_h1=f'<h1 class="article-title">{h1_text}</h1>'
    assert old_h1 in s, f'pattern not found in {f}'
    s=s.replace(old_h1,new_h1)
    open(p,'w',encoding='utf-8').write(s)
    print(f'fixed {f}: {h1_text}')
