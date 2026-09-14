"""Development server — serves the built site using stdlib only."""

import http.server
import os


def serve(directory: str = 'site', port: int = 8080):
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    with http.server.HTTPServer(('', port), handler) as httpd:
        print(f'Serving {directory}/ on http://localhost:{port}')
        httpd.serve_forever()


if __name__ == '__main__':
    serve()
