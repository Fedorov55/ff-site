import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from collections import defaultdict, OrderedDict

recs=json.load(open('C:/Users/Eblan/Downloads/records_classified.json',encoding='utf-8'))

# ---------- classification ----------
def classify_expense(r):
    cn = r['corr_name'] or ''
    content = r['content'] or ''
    cl = content.lower()
    cnl = cn.lower()
    account = r['account'] or ''
    if cn == 'АО "ТБанк"':
        if 'эквайринг' in cl:
            return ('Банковские комиссии и эквайринг', 'Эквайринг', 'Комиссия за операции по терминалам эквайринга')
        if 'пополнение по операции сбп' in cl:
            return ('Банковские комиссии и эквайринг', 'Комиссия за СБП', 'Плата за пополнение по операции СБП')
        if 'внешний банковский перевод' in cl:
            return ('Банковские комиссии и эквайринг', 'Комиссия за переводы', 'Комиссия за внешний банковский перевод')
        if 'обслуживание счета' in cl or 'обслуживание счёта' in cl:
            return ('Банковские комиссии и эквайринг', 'Обслуживание счёта', 'Плата за обслуживание расчётного счёта')
        return ('Банковские комиссии и эквайринг', 'Прочие банковские комиссии', content)
    if 'кодылев' in cnl:
        if account == '40817810100054219227':
            return ('Собственные средства', 'Вывод на личную карту', 'Перевод собственных средств на личную карту владельца')
        return ('Собственные средства', 'Перевод между счетами ИП', 'Перевод собственных средств между счетами ИП')
    suppliers = ['абдулгалимов','файзуллин','имангалиев','пардон','шанс']
    if any(s in cnl for s in suppliers):
        return ('Закупка товаров (себестоимость)', 'Товары для перепродажи', 'Оплата по счёту поставщика')
    if 'ростелеком' in cnl:
        return ('Связь и интернет', 'Телефония/интернет', 'Оплата услуг связи')
    if 'баланс' in cnl:
        return ('Бухгалтерские и консалтинговые услуги', 'Бухгалтерия', 'Оплата бухгалтерских услуг')
    if 'тавиат' in cnl:
        return ('Прочие операционные расходы', 'Услуги/прочее', 'Оплата по счёту')
    if 'асборн' in cnl:
        return ('Прочие операционные расходы', 'Хозтовары/материалы', 'Оплата по счёту')
    if 'заслон' in cnl:
        return ('Охрана', 'Охрана объекта', 'Оплата услуг ЧОП')
    if 'управля' in cnl or 'пжкх' in cnl:
        return ('Коммунальные расходы', 'Вывоз ТКО', 'Оплата услуг по обращению с ТКО')
    return ('Прочие расходы', 'Не классифицировано', content)

def classify_income(r):
    cl = (r['content'] or '').lower()
    if 'зачисление средств по терминалам' in cl:
        return 'Выручка от продаж (эквайринг)'
    if 'пополнение по операции сбп' in cl:
        return 'Выручка от продаж (СБП)'
    if 'перевод собственных средств' in cl:
        return 'Ввод собственных средств'
    return 'Прочие поступления'

for r in recs:
    if r['is_debit']:
        cat, sub, com = classify_expense(r)
        r['category'] = cat
        r['subcategory'] = sub
        r['comment'] = com
    else:
        r['category'] = classify_income(r)
        r['subcategory'] = ''
        r['comment'] = ''

# ---------- workbook ----------
wb = Workbook()

thin = Side(style='thin', color='BFBFBF')
border = Border(left=thin, right=thin, top=thin, bottom=thin)
header_fill = PatternFill('solid', fgColor='1F3864')
header_font = Font(bold=True, color='FFFFFF', size=11)
title_font = Font(bold=True, size=14, color='1F3864')
total_fill = PatternFill('solid', fgColor='D9E2F3')
subtotal_fill = PatternFill('solid', fgColor='FFF2CC')

def style_header(ws, row, ncols):
    for c in range(1, ncols+1):
        cell = ws.cell(row=row, column=c)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell.border = border

def set_widths(ws, widths):
    for i,w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

# ---------- Sheet: Расходы ----------
ws = wb.active
ws.title = 'Расходы'
headers = ['№','Дата','Номер документа','Вид','Контрагент','ИНН/КПП','Счёт контрагента',
           'Содержание операции','Сумма, руб.','Тип','Категория расхода','Подкатегория','Комментарий']
ws.append(headers)
style_header(ws, 1, len(headers))
ws.row_dimensions[1].height = 30

debits = [r for r in recs if r['is_debit']]
row = 2
for i, r in enumerate(debits, start=1):
    ws.append([
        i,
        r['date'],
        r['doc_number'],
        r['vid'],
        r['corr_name'],
        r['inn'],
        r['account'],
        r['content'],
        r['amount'],
        'Дебет',
        r['category'],
        r['subcategory'],
        r['comment'],
    ])
    # formats
    ws.cell(row=row, column=1).alignment = Alignment(horizontal='center')
    ws.cell(row=row, column=2).alignment = Alignment(horizontal='center')
    ws.cell(row=row, column=9).number_format = '#,##0.00'
    ws.cell(row=row, column=9).alignment = Alignment(horizontal='right')
    for c in range(1, len(headers)+1):
        ws.cell(row=row, column=c).border = border
        if c in (5,8,11,12,13):
            ws.cell(row=row, column=c).alignment = Alignment(wrap_text=True, vertical='top')
    row += 1

# total row
total_row = row
ws.cell(row=total_row, column=1, value='ИТОГО').font = Font(bold=True)
ws.cell(row=total_row, column=8, value='Всего расходов:').font = Font(bold=True)
ws.cell(row=total_row, column=9, value=f'=SUM(I2:I{total_row-1})').font = Font(bold=True)
ws.cell(row=total_row, column=9).number_format = '#,##0.00'
for c in range(1, len(headers)+1):
    ws.cell(row=total_row, column=c).fill = total_fill
    ws.cell(row=total_row, column=c).border = border

ws.freeze_panes = 'C2'
ws.auto_filter.ref = f'A1:M{total_row-1}'
set_widths(ws, [5,12,14,5,34,22,22,46,13,7,34,26,40])

# ---------- Sheet: Доходы ----------
ws2 = wb.create_sheet('Доходы')
h2 = ['№','Дата','Номер документа','Вид','Контрагент','ИНН/КПП','Счёт контрагента',
      'Содержание операции','Сумма, руб.','Тип','Источник дохода']
ws2.append(h2)
style_header(ws2, 1, len(h2))
ws2.row_dimensions[1].height = 30
credits = [r for r in recs if not r['is_debit']]
row = 2
for i, r in enumerate(credits, start=1):
    ws2.append([
        i, r['date'], r['doc_number'], r['vid'], r['corr_name'], r['inn'], r['account'],
        r['content'], r['amount'], 'Кредит', r['category'],
    ])
    ws2.cell(row=row, column=9).number_format = '#,##0.00'
    for c in range(1, len(h2)+1):
        ws2.cell(row=row, column=c).border = border
    row += 1
tr = row
ws2.cell(row=tr, column=1, value='ИТОГО').font = Font(bold=True)
ws2.cell(row=tr, column=8, value='Всего доходов:').font = Font(bold=True)
ws2.cell(row=tr, column=9, value=f'=SUM(I2:I{tr-1})').font = Font(bold=True)
ws2.cell(row=tr, column=9).number_format = '#,##0.00'
for c in range(1, len(h2)+1):
    ws2.cell(row=tr, column=c).fill = total_fill
    ws2.cell(row=tr, column=c).border = border
ws2.freeze_panes = 'C2'
ws2.auto_filter.ref = f'A1:K{tr-1}'
set_widths(ws2, [5,12,14,5,34,22,22,46,13,7,30])

# ---------- Sheet: Сводка по категориям ----------
ws3 = wb.create_sheet('Сводка по категориям')
h3 = ['Категория расхода','Кол-во операций','Сумма, руб.','Доля в расходах, %','Средний чек, руб.']
ws3.append(h3)
style_header(ws3, 1, len(h3))
agg = defaultdict(lambda: [0, 0.0])
for r in debits:
    agg[r['category']][0] += 1
    agg[r['category']][1] += r['amount']
total_exp = sum(v[1] for v in agg.values())
row = 2
for cat in sorted(agg, key=lambda c: -agg[c][1]):
    cnt, sm = agg[cat]
    ws3.append([cat, cnt, sm, sm/total_exp if total_exp else 0, sm/cnt if cnt else 0])
    ws3.cell(row=row, column=3).number_format = '#,##0.00'
    ws3.cell(row=row, column=4).number_format = '0.0%'
    ws3.cell(row=row, column=5).number_format = '#,##0.00'
    for c in range(1, len(h3)+1):
        ws3.cell(row=row, column=c).border = border
    row += 1
# total
ws3.cell(row=row, column=1, value='ИТОГО').font = Font(bold=True)
ws3.cell(row=row, column=2, value=f'=SUM(B2:B{row-1})').font = Font(bold=True)
ws3.cell(row=row, column=3, value=f'=SUM(C2:C{row-1})').font = Font(bold=True)
ws3.cell(row=row, column=3).number_format = '#,##0.00'
ws3.cell(row=row, column=4, value=1).number_format = '0.0%'
ws3.cell(row=row, column=5, value=f'=C{row}/B{row}').number_format = '#,##0.00'
for c in range(1, len(h3)+1):
    ws3.cell(row=row, column=c).fill = total_fill
    ws3.cell(row=row, column=c).border = border
set_widths(ws3, [40,18,16,20,18])

# ---------- Sheet: Подкатегории ----------
ws4 = wb.create_sheet('Подкатегории')
h4 = ['Категория','Подкатегория','Кол-во','Сумма, руб.','Доля, %']
ws4.append(h4)
style_header(ws4, 1, len(h4))
agg2 = defaultdict(lambda: [0,0.0])
for r in debits:
    agg2[(r['category'], r['subcategory'])][0]+=1
    agg2[(r['category'], r['subcategory'])][1]+=r['amount']
row = 2
for (cat,sub) in sorted(agg2, key=lambda k: -agg2[k][1]):
    cnt,sm = agg2[(cat,sub)]
    ws4.append([cat,sub,cnt,sm,sm/total_exp if total_exp else 0])
    ws4.cell(row=row, column=4).number_format='#,##0.00'
    ws4.cell(row=row, column=5).number_format='0.0%'
    for c in range(1,len(h4)+1):
        ws4.cell(row=row,column=c).border=border
    row+=1
set_widths(ws4, [34,30,10,16,12])

# ---------- Sheet: По месяцам ----------
ws5 = wb.create_sheet('По месяцам')
h5 = ['Месяц','Расходы, руб.','Доходы, руб.','Нетто, руб.']
ws5.append(h5)
style_header(ws5, 1, len(h5))
by_month = defaultdict(lambda: [0.0,0.0])
for r in recs:
    m = r['date'][3:]  # MM.YYYY
    if r['is_debit']:
        by_month[m][0]+=r['amount']
    else:
        by_month[m][1]+=r['amount']
row=2
for m in sorted(by_month):
    exp,inc = by_month[m]
    ws5.append([m, exp, inc, inc-exp])
    ws5.cell(row=row,column=2).number_format='#,##0.00'
    ws5.cell(row=row,column=3).number_format='#,##0.00'
    ws5.cell(row=row,column=4).number_format='#,##0.00'
    for c in range(1,len(h5)+1):
        ws5.cell(row=row,column=c).border=border
    row+=1
# total
ws5.cell(row=row,column=1,value='ИТОГО').font=Font(bold=True)
ws5.cell(row=row,column=2,value=f'=SUM(B2:B{row-1})').font=Font(bold=True)
ws5.cell(row=row,column=3,value=f'=SUM(C2:C{row-1})').font=Font(bold=True)
ws5.cell(row=row,column=4,value=f'=SUM(D2:D{row-1})').font=Font(bold=True)
for c in range(1,len(h5)+1):
    ws5.cell(row=row,column=c).fill=total_fill
    ws5.cell(row=row,column=c).border=border
    if c>1: ws5.cell(row=row,column=c).number_format='#,##0.00'
set_widths(ws5, [12,16,16,16])

# ---------- Sheet: Все операции ----------
ws6 = wb.create_sheet('Все операции')
h6 = ['№','Дата','Номер документа','Вид','Контрагент','ИНН/КПП','Счёт',
      'Содержание','Сумма, руб.','Тип','Категория']
ws6.append(h6)
style_header(ws6,1,len(h6))
row=2
for i,r in enumerate(recs, start=1):
    ws6.append([i,r['date'],r['doc_number'],r['vid'],r['corr_name'],r['inn'],r['account'],
                r['content'],r['amount'],'Дебет' if r['is_debit'] else 'Кредит',r['category']])
    ws6.cell(row=row,column=9).number_format='#,##0.00'
    for c in range(1,len(h6)+1):
        ws6.cell(row=row,column=c).border=border
    row+=1
ws6.freeze_panes='C2'
ws6.auto_filter.ref=f'A1:K{row-1}'
set_widths(ws6,[5,12,14,5,34,22,22,46,13,7,34])

# ---------- Sheet: Метаданные ----------
ws7 = wb.create_sheet('Инфо')
info = [
    ['Файл выписки', 'Выписка_ИП КОДЫЛЕВ АЛЕКСЕЙ ВЛАДИМИРОВИЧ_40802810500002951090_01.10.2026-31.10.2026.pdf'],
    ['Владелец счёта', 'ИП Кодылев Алексей Владимирович (ИНН 165700297396)'],
    ['Период', '01.10.2026 — 31.10.2026'],
    ['Входящий остаток', 2450.91],
    ['Исходящий остаток', 67705.35],
    ['Обороты по дебету', 655356.06],
    ['Обороты по кредиту', 720610.50],
    ['Количество операций', 248],
    ['Расходов (дебет)', len(debits)],
    ['Доходов (кредит)', len(credits)],
    ['Сумма расходов', sum(r['amount'] for r in debits)],
    ['Сумма доходов', sum(r['amount'] for r in credits)],
]
ws7.append(['Показатель','Значение'])
style_header(ws7,1,2)
row=2
for k,v in info:
    ws7.append([k,v])
    if isinstance(v,(int,float)):
        ws7.cell(row=row,column=2).number_format='#,##0.00'
    for c in range(1,3):
        ws7.cell(row=row,column=c).border=border
    row+=1
set_widths(ws7,[30,70])

out = 'C:/Users/Eblan/Downloads/Расходы_ИП_Кодылев_октябрь_2026.xlsx'
wb.save(out)
print('saved', out)
