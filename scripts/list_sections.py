s=open('C:/opencode/f&f/site/глобальный_аудитище.md',encoding='utf-8').read()
import re
sections=[m.group(0) for m in re.finditer(r'^## .+$', s, re.M)]
with open('C:/opencode/f&f/site/scripts/sections_list.txt','w',encoding='utf-8') as f:
    for sec in sections:
        f.write(sec+'\n')
print('Total sections:', len(sections))
