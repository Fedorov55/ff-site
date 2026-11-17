import os, re, json, subprocess
root='.'
html_files=[]
for r,ds,fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r: continue
    for f in fs:
        if f.endswith('.html'): html_files.append(os.path.join(r,f))
errors=[]
for f in html_files:
    rel=os.path.relpath(f,root).replace(chr(92),'/')
    s=open(f,encoding='utf-8',errors='replace').read()
    for m in ['<title','meta name="description"','rel="canonical"','og:title','twitter:card','lang="ru"','viewport','bg-orb--1','<body','</body>','<footer']:
        if m not in s: errors.append(rel+': missing '+m)
    h1_count=len(re.findall(r'<h1\b', s))
    if h1_count!=1: errors.append(rel+': h1 count '+str(h1_count))
    for img in re.finditer(r'<img\b[^>]*>',s):
        t=img.group(0)
        if 'alt=' not in t: errors.append(rel+': img no alt')
        if 'width=' not in t or 'height=' not in t: errors.append(rel+': img no dims')
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
        try: json.loads(m.group(1))
        except: errors.append(rel+': bad schema')
mm=0
for f in html_files:
    s=open(f,encoding='utf-8',errors='replace').read()
    for m in re.finditer(r'<(h[1-6])\b[^>]*>(.*?)</(h[1-6])>',s,re.S):
        if m.group(1)!=m.group(3): mm+=1
if mm: errors.append('heading mismatches: '+str(mm))
for jsf in ['script.js','search.js','calculator.js','sw.js','search-worker.js']:
    r=subprocess.run(['node','--check',jsf],capture_output=True,text=True,cwd=root)
    if r.returncode!=0: errors.append(jsf+': syntax error')
print('=== FINAL AUDIT ===')
print('Pages: '+str(len(html_files)))
print('Errors: '+str(len(errors)))
if errors:
    for e in errors[:30]: print(e)
else:
    print('ALL CHECKS PASSED')