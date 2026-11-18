import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

# Add missing utility classes to style.css
css_path = os.path.join(root, 'style.css')
css = open(css_path, encoding='utf-8').read()
additions = ''
if '.u-mx-4' not in css:
    additions += '\n.u-mx-4{margin:0 4px;}'
if '.u-hidden' not in css:
    additions += '\n.u-hidden{display:none;}'
if additions:
    open(css_path, 'a', encoding='utf-8').write(additions)
    print('Added utility classes:', additions.strip())

# Patterns to replace: exact inline style -> utility class
patterns = [
    ('color:var(--gold);', 'u-gold'),
    ('margin:0 4px;', 'u-mx-4'),
    ('text-align:center;', 'u-text-center'),
    ('color:var(--text);', 'u-text'),
    ('display:none;', 'u-hidden'),
]

total_replaced = 0
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if not f.endswith('.html'):
            continue
        path = os.path.join(r, f)
        s = open(path, encoding='utf-8').read()
        original = s
        for style_val, cls in patterns:
            # Replace style="EXACT" with class="cls" (if no existing class) or append to class
            # Case 1: element has no class attribute
            s = re.sub(
                rf'(<[a-zA-Z][^>]*?)\s+style="{re.escape(style_val)}"([^>]*>)',
                lambda m: f'{m.group(1)} class="{cls}"{m.group(2)}' if 'class=' not in m.group(0) else m.group(0),
                s
            )
            # Case 2: element has class attribute before style
            s = re.sub(
                rf'(<[a-zA-Z][^>]*?class="[^"]*?)(")([^>]*?)\s+style="{re.escape(style_val)}"([^>]*>)',
                lambda m: f'{m.group(1)} {cls}"{m.group(3)}{m.group(4)}',
                s
            )
            # Case 3: style before class
            s = re.sub(
                rf'(<[a-zA-Z][^>]*?)\s+style="{re.escape(style_val)}"([^>]*?class="[^"]*?)(")([^>]*>)',
                lambda m: f'{m.group(1)}{m.group(2)} {cls}"{m.group(4)}',
                s
            )
        if s != original:
            open(path, 'w', encoding='utf-8').write(s)
            total_replaced += 1

print(f'Updated {total_replaced} files')
print('Done')
