#coding=utf-8
import http.client
from urllib import request, parse
import urllib
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import Send_Post

class UE(BaseHTTPRequestHandler):
    url = "localhost:8981"
    id = ' id = Lemonade '
    password =' password = 1023 '
    data = ''
    IDue = ''

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(length).decode('utf-8'))
        # You now have a dictionary of the post data
        data = {"Method:": self.command,
                "Path:": self.path,
                "Post Data": post_data}
        print(data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def GenerateKap1(self,Kahm,IDue,IDap1,SEQ):
        return

def start_server():
    data = {'result': 'this is a test'}
    host = ('localhost', 8983)
    ue1 = UE
    UEserver = HTTPServer(host, ue1)
    print("Starting server, listen at: %s:%s" % host)
    UEserver.serve_forever()

if __name__ == '__main__':
    ue = UE
    ue.data = {
        ue.id:ue.password,
    }
    start_server()
    print("AP1 start server success...")
    print(ue.data)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    print("----------Send head test:-----------")
    Send_Post.send_post(ue.url, path="/index", data=ue.data, header=headers)




