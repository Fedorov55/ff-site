from fpdf import FPDF
import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/files'
font_path = 'C:/Windows/Fonts/arial.ttf'

pdf = FPDF()
pdf.add_page()
pdf.add_font('Arial', '', font_path, uni=True)
pdf.set_font('Arial', '', 12)

pdf.set_text_color(180, 140, 40)
pdf.set_font('Arial', '', 22)
pdf.cell(0, 12, '7 признаков, что ваши бэкапы не работают', new_x='LMARGIN', new_y='NEXT', align='C')
pdf.ln(2)
pdf.set_text_color(80, 80, 80)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 8, 'Чек-лист для проверки за 10 минут', new_x='LMARGIN', new_y='NEXT', align='C')
pdf.ln(6)
pdf.set_draw_color(212, 175, 55)
pdf.line(20, pdf.get_y(), 190, pdf.get_y())
pdf.ln(8)

sections = [
    ('7 признаков проблемного бэкапа', [
        'Бэкап никогда не проверяли. Копирование идёт, файлы лежат, но никто не пробовал развернуть.',
        'Бэкап на том же диске, что оригинал. При сбое диска потеряете и оригинал, и копию.',
        'Нет проверки целостности. Архив может быть повреждён при копировании.',
        'Версия бэкапа не совпадает с версией 1С. База не откроется на несовместимой версии.',
        'Бэкап делается «по настроению». Ручной бэкап = бэкапа нет.',
        'Нет глубины хранения. Если бэкап перезаписывается каждый день — одна копия.',
        'Бэкап не хранится вне офиса. Пожар/кража — и бэкап уничтожен вместе с оригиналом.',
    ]),
    ('Что делать дальше', [
        'Проверьте каждый пункт чек-листа на вашей инфраструктуре.',
        'Если нашли 2+ проблемы — бэкапы под угрозой.',
        'Свяжитесь с F&F для бесплатного аудита бэкапов.',
    ]),
]
for sec_title, items in sections:
    pdf.set_text_color(20, 20, 20)
    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 8, sec_title, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)
    pdf.set_font('Arial', '', 11)
    for item in items:
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(0, 6, f'- {item}', new_x='LMARGIN', new_y='NEXT')
        pdf.ln(1)
    pdf.ln(4)

pdf.ln(6)
pdf.set_draw_color(212, 175, 55)
pdf.line(20, pdf.get_y(), 190, pdf.get_y())
pdf.ln(4)
pdf.set_text_color(100, 100, 100)
pdf.set_font('Arial', '', 9)
pdf.multi_cell(0, 5, 'F&F — IT-аутсорсинг для бизнеса в Казани\nТелефон: +7 (901) 265-52-52 | Email: FathFed@yandex.ru\nhttps://fedorov55.github.io/ff-site/', align='C')

out = os.path.join(root, 'backup-checklist.pdf')
pdf.output(out)
print(f'Created backup-checklist.pdf ({os.path.getsize(out)} bytes)')
print('Done')
