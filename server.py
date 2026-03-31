#!/usr/bin/env python3
import http.server
import json
import subprocess
import os
import random
from pathlib import Path
from urllib.parse import urlparse

WISDOM_QUOTES = [
    "That, that is, is. That, that is not, is not. That, that is, is not that, that is not. That, that is not, is not that, that is.",
    "The door is the key.",
    "It is possible to make anything if you really believe.",
    "The bird is on the wing.",
    "Don't think too much, just do.",
    "The greatest pleasure is to do a good deed by stealth.",
    "The only way to do great work is to love what you do.",
    "Perfection is not just about control. It is also about letting go.",
]

def cowsay(text):
    """Generate cowsay ASCII art with the given text."""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines) if lines else 0
    width = max_len + 2
    
    result = []
    result.append(' ' + '_' * (width + 2))
    
    for i, line in enumerate(lines):
        is_first = (i == 0)
        is_last = (i == len(lines) - 1)
        
        left = '/' if is_first else '|'
        right = '\\' if is_first else '|'
        
        padded = line.ljust(max_len)
        result.append(f'{left} {padded} {right}')
    
    result.append(' ' + '-' * (width + 2))
    result.append('        \\   ^__^')
    result.append('         \\  (oo)\\_______')
    result.append('            (__)\       )\\/\\')
    result.append('                ||----w |')
    result.append('                ||     ||')
    
    return '\n'.join(result)

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        if path == '/api/fortune':
            try:
                quote = random.choice(WISDOM_QUOTES)
                fortune_text = cowsay(quote)
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
