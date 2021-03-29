'''
run this script to host web server for our applications
'''

import http.server
import threading
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

def http_server(ip="127.0.0.1", PORT=8000):
    with socketserver.TCPServer((ip, PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


def start_http_server(IP="127.0.0.1", PORT=8000):
    http_server_thread= threading.Thread(target=start_http_server, args=[IP,PORT])
    http_server_thread.start()
    
    


