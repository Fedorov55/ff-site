import os
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files=['img/case-tobacco.webp','img/case-tobacco-400w.webp','img/case-tobacco-800w.webp','img/case-tatar-septic.webp','img/case-tatar-septic-400w.webp','img/case-tatar-septic-800w.webp','img/case-server-turnkey.webp','img/case-server-turnkey-400w.webp','img/case-server-turnkey-800w.webp']
for f in files:
    print(f, '->', 'OK' if os.path.exists(os.path.join(root,f)) else 'MISSING')
