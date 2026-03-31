#!/usr/bin/env python3
import http.server
import json
import subprocess
import os
from pathlib import Path
from urllib.parse import urlparse

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        if path == '/api/fortune':
            try:
                result = subprocess.run(
                    'nix-shell -p fortune cowsay --run "fortune wisdom | cowsay"',
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                fortune_text = result.stdout
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
