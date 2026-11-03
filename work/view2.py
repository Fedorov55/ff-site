import json
recs=json.load(open('C:/Users/Eblan/Downloads/records_classified.json',encoding='utf-8'))
debits=[r for r in recs if r['is_debit']]
for r in debits:
    if 'Тавиат' in r['corr_name'] or 'Асборн' in r['corr_name'] or 'Заслон' in r['corr_name'] or 'Баланс' in r['corr_name'] or 'Ростелеком' in r['corr_name'] or 'ПЖКХ' in r['corr_name'] or 'Управляющая' in r['corr_name']:
        print(r['date'], '|', r['corr_name'], '|', r['content'], '|', r['amount'])
