from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class ApplicationHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        version = os.getenv("APP_VERSION", "unknown")

        response = f"""
Blue-Green Deployment Platform

Application Version: {version}
"""

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode())

    def log_message(self, format, *args):
        return


server = HTTPServer(("0.0.0.0", 8080), ApplicationHandler)

print("Application listening on port 8080")

server.serve_forever()
