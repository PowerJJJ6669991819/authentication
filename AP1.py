#coding=utf-8
import http.client
import urllib
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import request, parse
import json
import re
import GetData
import Send_Post

class AP1(BaseHTTPRequestHandler):
    IDap1 = ''

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(length).decode('utf-8'))
        # You now have a dictionary of the post data
        #data = GetData.GetIdAndPwd(post_data)
        InitData = parse.urlencode(post_data).encode('utf-8')
        result = AHMResponse("localhost:8982",path="/index",data=InitData,header={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"})
        if result == b'1':
            result1 = 'OK'
        else:
            result1 = 'Wrong'
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result1).encode())

def AHMResponse(url, path, data, header):
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, data, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    data1 = r1.read()
    print(data1)
    conn.close()
    return data1

def start_server():
    data = {'result': 'this is a test'}
    host = ('localhost', 8981)
    ap1 = AP1
    AP1server = HTTPServer(host, ap1)
    print("Starting server, listen at: %s:%s" % host)
    AP1server.serve_forever()

if __name__ == '__main__':
    start_server()
    #data = {' id = Lemonade ': ' password = 1023 '}
    #datas = parse.urlencode(data).encode('utf-8')
    #headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    #Send_Post.send_post("localhost:8983", path="/index", data=datas, header=headers)
    print("AP1 start server success...")