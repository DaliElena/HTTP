from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import queue

global que
que = queue.Queue(5)
que.put('A') 
que.put('B') 
que.put('C')

def display(self):
      next_item = ''
      for i in self.queue:
          next_item += str(i) + '\n'
      return next_item


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    # определяем метод `do_GET` 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        out_data = bytes(display(que), encoding = 'utf-8')
        self.wfile.write(out_data)
        

    # определяем метод `do_POST` 
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data=body.decode('UTF-8')
        if data!='':
            if que.full():
                que.get()
                que.put(data)        
            else:
                que.put(data)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()