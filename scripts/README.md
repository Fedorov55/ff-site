# F&F Site Scripts

## generate-sitemap.py
Generates `sitemap.xml` from all HTML files in the project.

```bash
python scripts/generate-sitemap.py
```

Excludes: 404.html, pasahalki.html, room.html, vcard.html.
Priority: index=1.0, support/servers/services/cases=0.9, for-*/infrastructure/security/audit/vpn=0.8, etc.

## check-site.py
Basic CI checks for the site.

```bash
python scripts/check-site.py
```

Checks:
1. Broken internal links
2. Empty sections
3. Placeholders/TODOs (excluding verification meta tags)
4. JS syntax (node --check)
5. CSS/JS version consistency
6. One H1 per page
7. JSON-LD validity
8. _headers exists

Exit code 1 if any errors found.