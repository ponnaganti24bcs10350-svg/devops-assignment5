from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>Hello World - Python</title>
          <style>
            body {
              font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
              display: flex;
              justify-content: center;
              align-items: center;
              height: 100vh;
              margin: 0;
              background: #0f172a;
              color: #f8fafc;
            }
            .card {
              background: #1e293b;
              padding: 2.5rem 3.5rem;
              border-radius: 12px;
              box-shadow: 0 10px 25px rgba(0,0,0,0.3);
              text-align: center;
              border: 1px solid #334155;
            }
            h1 { color: #4ade80; margin-bottom: 0.5rem; }
            p { color: #94a3b8; font-size: 1.1rem; }
          </style>
        </head>
        <body>
          <div class="card">
            <h1>Hello World!</h1>
            <p>Running on Python inside Docker</p>
          </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5000), HelloHandler)
    print("Python HTTP Server running on port 5000...")
    server.serve_forever()
