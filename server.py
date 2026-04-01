#!/usr/bin/env python3
import http.server
import json
import os
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse

FORTUNE_ARGS = ['fortune', '-s', 'linux']
MAX_QUOTE_CHARS = 140
MAX_RENDER_WIDTH = 28
FALLBACK_FORTUNE = """ ________________________________
< Keep it small, sharp, and real. >
 --------------------------------
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
"""


def compact_quote(text):
    normalized = re.sub(r'\s+', ' ', text).strip()
    if len(normalized) <= MAX_QUOTE_CHARS:
        return normalized

    truncated = normalized[: MAX_QUOTE_CHARS - 1]
    if ' ' in truncated:
        truncated = truncated.rsplit(' ', 1)[0]
    return truncated.rstrip(' ,;:-') + '...'


def generate_fortune():
    for _ in range(3):
        try:
            fortune_proc = subprocess.run(
                FORTUNE_ARGS,
                capture_output=True,
                text=True,
                timeout=1.0,
                check=True,
            )
            quote = compact_quote(fortune_proc.stdout)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            continue

        if not quote:
            continue

        try:
            cowsay_proc = subprocess.run(
                ['cowsay', '-W', str(MAX_RENDER_WIDTH)],
                input=quote,
                capture_output=True,
                text=True,
                timeout=1.0,
                check=True,
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            continue

        rendered = cowsay_proc.stdout.strip('\n')
        if rendered:
            return rendered

    return FALLBACK_FORTUNE.strip('\n')


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == '/api/fortune':
            try:
                fortune_text = generate_fortune()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'fortune': fortune_text}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            super().do_GET()

if __name__ == '__main__':
    os.chdir(Path(__file__).parent)
    server = http.server.HTTPServer(('0.0.0.0', 5000), CustomHTTPRequestHandler)
    print('Server running on port 5000')
    server.serve_forever()
