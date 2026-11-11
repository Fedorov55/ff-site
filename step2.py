import re
s = open('support.html', encoding='utf-8').read()
orig = s
# Remove "Вы находитесь в разделе" block
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:860px;margin:0 auto;padding:16px;border:1px solid var\(--border\);border-radius:12px;background:var\(--card\);text-align:center;">\s*<p style="margin:0;font-size:13px;color:var\(--text-2\);">Вы находитесь в разделе:.*?</section>\s*', '', s, flags=re.S)
if s != orig:
    open('support.html', 'w', encoding='utf-8').write(s)
    print('done')
else:
    print('not found')