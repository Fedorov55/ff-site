s = open('index.html', encoding='utf-8').read()
old = 'Алерт приходит нам, а не директору. Инженер берёт заявку за 15 минут. В понедельник офис работает как обычно.'
new = 'Алерт приходит нам, а не директору. В понедельник офис работает как обычно.'
if old in s:
    s = s.replace(old, new, 1)
    open('index.html', 'w', encoding='utf-8').write(s)
    print('done')
else:
    print('not found')