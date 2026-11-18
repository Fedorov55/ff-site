path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(path, encoding='utf-8').read()
original = s

# Replace mojibake headings with proper Russian
replacements = {
    '╨С╨╡╤Б╨┐╨╗╨░╤В╨╜╤Л╨╣ IT-╨░╤Г╨┤╨╕╤В\n╨Я╤А╨╛╨▓╨╡╤А╨║╨░ ╨╕╨╜╤Д╤А': 'Бесплатный IT-аудит\nПроверка инфраструктуры',
    '╨з╤В╨╛ ╨▓╤Е╨╛╨┤╨╕╤В ╨▓ ╨▒╨╡╤Б╨┐╨╗╨░╤В╨╜╤Л╨╣ ╨░╤Г╨┤╨╕╤В': 'Что входит в бесплатный аудит',
    '╨Ф╨╛╤Б╤В╤Г╨┐╤Л': 'Доступы',
    '╨С╤Н╨║╨░╨┐╤Л': 'Бэкапы',
    '╨Ю╨▒╨╜╨╛╨▓╨╗╨╡╨╜╨╕╤П': 'Обновления',
    '╨н╨ж╨Я ╨╕ ╨Ъ╤А╨╕╨┐╤В╨╛╨Я╤А╨╛': 'ЭЦП и КриптоПро',
}
for old, new in replacements.items():
    if old in s:
        s = s.replace(old, new)
        print(f'Replaced: {old[:40]} -> {new}')
    else:
        print(f'NOT FOUND: {old[:40]}')

# Also fix the "Частые вопросы" heading if mojibake
s = s.replace('╨з╨░╤Б╤В╤Л╨╡ ╨▓╨╛╨┐╤А╨╛╤Б╤Л', 'Частые вопросы')

open(path, 'w', encoding='utf-8').write(s)
print('Done')
