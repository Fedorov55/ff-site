path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/contacts.html'
s = open(path, encoding='utf-8').read()
original = s
# Add about.html link to the "Смотрите также" block if not present
if 'about.html' not in s.split('Смотрите также')[-1].split('</section>')[0]:
    s = s.replace(
        '<a href="contacts.html" class="btn btn--ghost btn--sm">Контакты</a>',
        '<a href="contacts.html" class="btn btn--ghost btn--sm">Контакты</a>\n<a href="about.html" class="btn btn--ghost btn--sm">О компании</a>',
        1
    )
    open(path, 'w', encoding='utf-8').write(s)
    print('Updated contacts.html')
else:
    print('Already has about link')
print('Done')
