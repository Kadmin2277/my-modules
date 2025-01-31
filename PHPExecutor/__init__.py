import http.server
import socketserver
import subprocess
import os


class PHPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith(".php"):
            # Определяем путь к файлу.
            file_path = self.path[1:]
            if os.path.isfile(file_path):
                result = subprocess.run(['php', file_path], capture_output=True, text=True)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(result.stdout.encode('utf-8'))
            else:
                self.send_error(404, "File not found.")
        else:
            self.send_error(404, "Only PHP files are supported.")


def run(server_class=http.server.HTTPServer, handler_class=PHPRequestHandler, PORT=8000):
    with server_class(("", PORT), handler_class) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
