"""
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from httplib import HTTPResponse
from os import curdir,sep

#Create a index.html aside the code
#Run: python server.py
#After run, try http://localhost:8080/

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path  = '/index.html'
        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimeType = 'text/html'
                sendReply = True
            if sendReply == True:
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimeType)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return
        except IOError:
            self.send_error(404,'File not found!')


def run():
    print('http server is starting...')
    #by default http server port is 80
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    try:
        print('http server is running...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()

if __name__ == '__main__':
    run()


"""
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import threading
import argparse
import re
import cgi
 
class LocalData(object):
  records = {}
 
class HTTPRequestHandler(BaseHTTPRequestHandler):
  def do_POST(self):
    if None != re.search('/api/v1/addrecord/*', self.path):
      ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
      if ctype == 'application/json':
        length = int(self.headers.getheader('content-length'))
        data = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        #recordID = self.path.split('/')[-1]
        #LocalData.records[recordID] = data
        #print("record %s is added successfully" % recordID)
        print("OK")
      else:
        data = {}
      self.send_response(200)
      self.end_headers()
    else:
      self.send_response(403)
      self.send_header('Content-Type', 'application/json')
      self.end_headers()
    return
 
  def do_GET(self):
    if None != re.search('/api/v1/getrecord/*', self.path):
      recordID = self.path.split('/')[-1]
      if LocalData.records.has_key(recordID):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(LocalData.records[recordID])
      else:
        self.send_response(400, 'Bad Request: record does not exist')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
    else:
      self.send_response(403)
      self.send_header('Content-Type', 'application/json')
      self.end_headers()
    return
 
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
  allow_reuse_address = True
 
  def shutdown(self):
    self.socket.close()
    HTTPServer.shutdown(self)
 
class SimpleHttpServer():
  def __init__(self, ip, port):
    self.server = ThreadedHTTPServer((ip,port), HTTPRequestHandler)
 
  def start(self):
    self.server_thread = threading.Thread(target=self.server.serve_forever)
    self.server_thread.daemon = True
    self.server_thread.start()
 
  def waitForThread(self):
    self.server_thread.join()
 
  def addRecord(self, recordID, jsonEncodedRecord):
    LocalData.records[recordID] = jsonEncodedRecord
 
  def stop(self):
    self.server.shutdown()
    self.waitForThread()
 
if __name__=='__main__':
  parser = argparse.ArgumentParser(description='HTTP Server')
  parser.add_argument('port', type=int, default=8081, help='Listening port for HTTP Server')
  parser.add_argument('ip', default="1277.0.0.1", help='HTTP Server IP')
  args = parser.parse_args() 
  try:
    server = SimpleHttpServer(args.ip, args.port)
    print('HTTP Server Running...........')
    server.start()
    server.waitForThread()
  except KeyboardInterrupt, e:
    print "Stop - interrupted by keyboard."
    server.stop()

