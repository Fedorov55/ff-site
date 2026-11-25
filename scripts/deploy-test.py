#!/usr/bin/env python3
"""Deploy site to test host (92.255.199.90) via SFTP (atomic).

Usage:
    python scripts/deploy-test.py

Uploads only site files to a staging dir, then swaps it with
/var/www/test-site on the server. Minimizes the window where the site is
in an inconsistent (partially-updated) state.

After deploy, verify at http://92.255.199.90:8080
"""
import os, paramiko

LOCAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REMOTE_ROOT = '/var/www/test-site'
STAGING = '/var/www/test-site-staging'
BACKUP = '/var/www/test-site-prev'
EXCLUDE_DIRS = {'.git', 'node_modules', '.agents', 'dist', 'docs', 'scripts', 'server', 'files'}
EXCLUDE_FILES = {'.gitignore', 'AGENTS.md', 'README.md', 'package.json', 'package-lock.json',
                 'opencode.jsonc', 'skills-lock.json', '.clinerules', '.htmlhintrc',
                 'eslint.config.mjs', 'build.js', '.nojekyll'}
ALLOWED_EXT = {'.html', '.css', '.js', '.json', '.txt', '.xml', '.webp', '.ico', '.svg',
               '.woff2', '.png', '.jpg', '.jpeg', '.gif'}
ALLOWED_NAMES = {'_headers', '_redirects', 'robots.txt', 'sitemap.xml', 'favicon.ico',
                 'manifest.json', 'sw.js', 'data.json', 'search-index.json',
                 'security.txt', 'llms.txt', 'llms-full.txt', 'rss.xml'}

HOST = '92.255.199.90'
PORT = 2222
USER = 'ftpuser'
PASS = '!1assert!!'
SUDO_PASS = '!1assert!!'

def is_site_file(name):
    if name in ALLOWED_NAMES:
        return True
    ext = os.path.splitext(name)[1].lower()
    return ext in ALLOWED_EXT

def ensure_dir(sftp, path):
    try:
        sftp.stat(path)
    except FileNotFoundError:
        try:
            sftp.mkdir(path)
        except Exception:
            pass

# Prepare staging dir via sudo (odmin)
ssh_admin = paramiko.SSHClient()
ssh_admin.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_admin.connect(HOST, port=PORT, username='odmin', password=SUDO_PASS, timeout=15)
stdin, stdout, stderr = ssh_admin.exec_command(
    'echo "%s" | sudo -S bash -c "rm -rf %s; mkdir -p %s; chown -R ftpuser:www-data %s"' % (SUDO_PASS, STAGING, STAGING, STAGING))
stdout.read()
ssh_admin.close()

# Upload via SFTP as ftpuser
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, port=PORT, username=USER, password=PASS, timeout=30)
sftp = ssh.open_sftp()

uploaded = 0
skipped = 0
for r_, _, fs in os.walk(LOCAL):
    rel = os.path.relpath(r_, LOCAL).replace('\\', '/')
    if rel == '.':
        rel = ''
    parts = rel.split('/') if rel else []
    if any(p in EXCLUDE_DIRS for p in parts):
        continue
    remote_dir = STAGING if not rel else STAGING + '/' + rel
    ensure_dir(sftp, remote_dir)
    for f in fs:
        if f in EXCLUDE_FILES or f.startswith('.'):
            skipped += 1
            continue
        if not is_site_file(f):
            skipped += 1
            continue
        local_path = os.path.join(r_, f)
        remote_path = remote_dir + '/' + f
        try:
            sftp.put(local_path, remote_path)
            uploaded += 1
        except Exception as e:
            print('UPLOAD ERR', remote_path, e)

sftp.close()
ssh.close()

# Swap: move current to backup, then staging to live
ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect(HOST, port=PORT, username='odmin', password=SUDO_PASS, timeout=15)
# step 1: remove old backup, move current to backup (ignore if current doesn't exist)
ssh2.exec_command('echo "%s" | sudo -S rm -rf %s' % (SUDO_PASS, BACKUP))[1].read()
ssh2.exec_command('echo "%s" | sudo -S mv %s %s 2>/dev/null || true' % (SUDO_PASS, REMOTE_ROOT, BACKUP))[1].read()
# step 2: move staging to live
stdin, stdout, stderr = ssh2.exec_command('echo "%s" | sudo -S mv %s %s' % (SUDO_PASS, STAGING, REMOTE_ROOT))
print('move staging->live:', stdout.read().decode('utf-8','ignore').strip(), stderr.read().decode('utf-8','ignore').strip())
ssh2.close()

print(f'uploaded: {uploaded} skipped: {skipped}')
print('verify: http://92.255.199.90:8080/')