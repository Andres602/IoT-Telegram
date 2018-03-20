#!/usr/bin/python
# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from ConfigParser import SafeConfigParser
from database import database

config = SafeConfigParser()
config.read('/home/orangepi/IoT-Telegram/server/config.ini')
db=None
token=None

#class database():
#    def __init__(self, host, port):
#        self.host = host
#        self.port = port
#
#    def getLight(self, id, ligth):
#        return "light:{:02d}".format(ligth)#return self.r.hget('user:' + str(id), "light:{:02d}".format(ligth))

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global db, token
        self._set_headers()
        print self.headers.getheader('token')
        if self.headers.getheader('token') == token:
            if self.path == '/light':
                self.wfile.write("{}".format(db.getLight(5951788)))
            else:
                self.send_response(400)
                self.wfile.write("<html><body><h1>noFound</h1></body></html>")
        else:
            self.send_response(400)
            self.wfile.write("<html><body><h1>noToken</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    print(S)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
    global db, token
    token=config.get('esp8266', 'token')
    db=database(config.get('database','host'), config.get('database','port'))
    db.connect()
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

