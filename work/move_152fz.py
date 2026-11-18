import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
src = '152fz-prep.html'
dst = 'services/152fz.html'
src_path = os.path.join(root, src)
dst_path = os.path.join(root, dst)

if not os.path.exists(src_path):
    print('Source not found:', src)
else:
    s = open(src_path, encoding='utf-8').read()
    # Adjust relative links: root-level -> ../
    # Links to root pages need ../
    s = re.sub(r'href="(?!https?://|mailto:|tel:|#|\.\./)([^"]+\.html)', r'href="../\1', s)
    s = re.sub(r'href="(?!https?://|mailto:|tel:|#|\.\./)([^"]+\.css)', r'href="../\1', s)
    s = re.sub(r'href="(?!https?://|mailto:|tel:|#|\.\./)([^"]+\.js)', r'href="../\1', s)
    s = re.sub(r'href="(?!https?://|mailto:|tel:|#|\.\./)([^"]+\.webp)', r'href="../\1', s)
    s = re.sub(r'href="(?!https?://|mailto:|tel:|#|\.\./)([^"]+\.ico)', r'href="../\1', s)
    s = re.sub(r'href="(?!https?://|mailto:|tel:|#|\.\./)([^"]+\.png)', r'href="../\1', s)
    s = re.sub(r'src="(?!https?://|mailto:|tel:|#|\.\./)([^"]+)"', r'src="../\1"', s)
    # canonical/og
    s = re.sub(r'href="https://fedorov55.github.io/ff-site/152fz-prep.html"', 'href="https://fedorov55.github.io/ff-site/services/152fz.html"', s)
    s = re.sub(r'content="https://fedorov55.github.io/ff-site/152fz-prep.html"', 'content="https://fedorov55.github.io/ff-site/services/152fz.html"', s)
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    open(dst_path, 'w', encoding='utf-8').write(s)
    print(f'Created {dst}')
    # Delete source
    os.remove(src_path)
    print(f'Deleted {src}')
    # Add redirect
    redirects_path = os.path.join(root, '_redirects')
    rds = open(redirects_path, encoding='utf-8').read()
    line = '/152fz-prep.html /services/152fz.html 301\n'
    if line not in rds:
        rds += line
        open(redirects_path, 'w', encoding='utf-8').write(rds)
        print('Added redirect')
print('Done')
