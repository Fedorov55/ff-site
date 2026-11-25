#!/usr/bin/env python3
"""Deploy site to test host (92.255.199.90) via SFTP.

Usage:
    python scripts/deploy-test.py

Uploads the entire site (excluding node_modules, .git, .agents, dist, hidden files)
to /var/www/test-site on the test server via SFTP (port 2222, user ftpuser).

After deploy, verify at http://92.255.199.90:8080
"""
import os, paramiko

LOCAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REMOTE_ROOT = '/var/www/test-site'
EXCLUDE_DIRS = {'.git', 'node_modules', '.agents', 'dist'}
EXCLUDE_FILES = {'.gitignore'}
HOST = '92.255.199.90'
PORT = 2222
USER = 'ftpuser'
PASS = '!1assert!!'

def ensure_dir(sftp, path):
    try:
        sftp.stat(path)
    except FileNotFoundError:
        try:
            sftp.mkdir(path)
        except Exception:
            pass

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
    remote_dir = REMOTE_ROOT if not rel else REMOTE_ROOT + '/' + rel
    ensure_dir(sftp, remote_dir)
    for f in fs:
        if f in EXCLUDE_FILES or f.startswith('.'):
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
print(f'uploaded: {uploaded} skipped: {skipped}')
print('verify: http://92.255.199.90:8080/')
"