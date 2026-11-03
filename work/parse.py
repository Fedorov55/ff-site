import pdfplumber, re, json

PDF='C:/Users/Eblan/Downloads/Выписка_ИП КОДЫЛЕВ АЛЕКСЕЙ ВЛАДИМИРОВИЧ_40802810500002951090_01.10.2026-31.10.2026.pdf'
date_re=re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
footer_starts=('Обороты за день','Остаток на начало','Остаток на конец','Остаток на начало периода')

def col(x):
    if x < 130: return 'date'
    if x < 235: return 'req'
    if x < 420: return 'corr'
    if x < 600: return 'content'
    if x > 760: return 'ignore'
    return 'amount'

ops=[]
with pdfplumber.open(PDF) as pdf:
    for pi, pg in enumerate(pdf.pages):
        words=pg.extract_words()
        lines={}
        for w in words:
            lines.setdefault(round(w['top']), []).append(w)
        tops=sorted(lines)
        current=None
        for t in tops:
            ws=sorted(lines[t], key=lambda w:w['x0'])
            if not ws: continue
            first=ws[0]['text']
            is_start = bool(date_re.match(first)) and any(w['text']=='Вид:' for w in ws)
            line_text=' '.join(w['text'] for w in ws)
            is_footer = line_text.startswith(footer_starts) or line_text.startswith('Дата проведения')
            if is_start:
                if current: ops.append(current)
                current={'page':pi+1, 'start_top':t, 'tops':[t], 'lines':{t:ws}}
            else:
                if current is not None:
                    if is_footer:
                        ops.append(current)
                        current=None
                    else:
                        current['tops'].append(t)
                        current['lines'][t]=ws
        if current:
            ops.append(current)

records=[]
for op in ops:
    cols={'date':[],'req':[],'corr':[],'content':[],'amount':[],'ignore':[]}
    for t in op['tops']:
        for w in sorted(op['lines'][t], key=lambda w:w['x0']):
            cols[col(w['x0'])].append(w['text'])
    date=' '.join(cols['date']).strip()
    req_text=' '.join(cols['req'])
    m=re.search(r'Вид:\s*(\d+)', req_text)
    vid=m.group(1) if m else ''
    docnum_m=re.search(r'Номер:\s*(\S+)', req_text)
    docnum=docnum_m.group(1) if docnum_m else ''
    corr_text=' '.join(cols['corr'])
    name_part=corr_text.split('ИНН/КПП:')[0].strip() if 'ИНН/КПП:' in corr_text else corr_text.strip()
    inn_m=re.search(r'ИНН/КПП:\s*([\d/]+)', corr_text)
    inn=inn_m.group(1) if inn_m else ''
    acct_m=re.search(r'Счёт:\s*(\d+)', corr_text)
    acct=acct_m.group(1) if acct_m else ''
    bik_m=re.search(r'БИК:\s*(\d+)', corr_text)
    bik=bik_m.group(1) if bik_m else ''
    bank_m=re.search(r'Банк:\s*(.*?)(?=К/С:|$)', corr_text)
    bank=bank_m.group(1).strip() if bank_m else ''
    ks_m=re.search(r'К/С:\s*(\d+)', corr_text)
    ks=ks_m.group(1) if ks_m else ''
    content=' '.join(cols['content']).strip()
    amt_str=' '.join(cols['amount']).strip()
    records.append({
        'page':op['page'],
        'date':date,
        'vid':vid,
        'doc_number':docnum,
        'corr_name':name_part,
        'inn':inn,
        'account':acct,
        'bik':bik,
        'bank':bank,
        'ks':ks,
        'content':content,
        'amount_str':amt_str,
    })

json.dump(records, open('C:/Users/Eblan/Downloads/records.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('records', len(records))
for r in records[:8]:
    print(r['date'], r['vid'], '|', r['corr_name'], '|', r['content'], '|', r['amount_str'], '|', r['inn'])
