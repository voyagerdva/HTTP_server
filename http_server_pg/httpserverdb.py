# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from mycontroller import MyController
from http import cookies

portHost = 9900
hostName = 'localhost'
myHeader = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# 26-11-2019 #

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        cookie = cookies.SimpleCookie()
        myController = MyController()
        resp = myController.getRedirect(self.path)

        if resp == 404:
            self.send_response(404, 'PAGE not FOUND')
            cookie['client_name'] = 'Insom'
            cookie['client_age'] = '50'
            cookie['Expi'] = '2019'
            self.send_header('Content-type', 'text/html')
            self.send_header('Set-Cookie', cookie.output(header='', sep=''))
            self.end_headers()
            self.wfile.write(bytes(str(self.headers), 'utf-8'))
            self.wfile.write(bytes(str(resp) + '    404', 'utf-8'))
        else:
            cookie['client_name'] = 'Insom'
            cookie['client_age'] = '50'
            cookie['Expi'] = '2019'
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'text/html')
            self.send_header('Set-Cookie', cookie.output(header='', sep=''))
            self.end_headers()

            if 'favicon_ico' in str(resp):
                self.wfile.write(bytes(resp, 'utf-8'))
            else:
                self.wfile.write(bytes(resp, 'utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header('application/json', 'text/json')
        self.end_headers()
        content_lenght = int(self.headers['Content-Length'])
        body = self.rfile.read(content_lenght)
        myController = MyController()
        resp = myController.postRedirect(self.path, body)
        print(resp, type(resp))
        self.wfile.write(bytes(resp, 'utf-8'))


myServer = HTTPServer((hostName, portHost), MyServer)
print(time.asctime(), 'Server Starts - %s:%s' % (hostName, portHost))
print('=====', (hostName, portHost))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), 'Server Stops - %s:%s' % (hostName, portHost))