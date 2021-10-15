from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class Queue: 
 
  def __init__(self): 
      self.queue = list() 
 
  def add_element(self,val): 
      if val not in self.queue: 
          self.queue.insert(0,val) 
          return True 
      return False 
 
  def remove_element(self): 
     if len(self.queue)<1: 
         return None
     return self.queue.pop(0)

  def size(self): 
      return len(self.queue)
  def display(self):
      next_item = ''
      while len(self.queue)>0:
          next_item += str(self.queue.pop()) + '\n'
      return next_item
      


global que
que = Queue()
que.add_element("January") 
que.add_element("February") 
que.add_element("March")
print(que.display())



class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    # определяем метод `do_GET` 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(que.display())
        

    # определяем метод `do_POST` 
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
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