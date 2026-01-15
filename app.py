#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import subprocess

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Security vulnerability - subprocess with shell=True
        subprocess.run("stat /tmp/whistory.1000.2966", shell=True)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"message": "Hello from Python HTTP Server", "version": "1.0", "status": "success"}
        self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), MyHandler)
    print("Server running on port 8080")
    server.serve_forever()
