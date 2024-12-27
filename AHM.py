#coding=utf-8
import http.client
import urllib
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re
import GetData
import Send_Post

class AHM(BaseHTTPRequestHandler):
    Kahm = ''
    users = {'Lemonade': '1023', 'LMD': '1008'} # 存储合法的用户信息的字典

    def add_user(self, id, password):
        # 将一个用户设备添加到合法的用户信息字典中
        self.users[id] = password

    def verify(self,data):
        ue = {'Lemonade': '1023'}
        keys_iterator = iter(ue)  # 使用迭代器进行分离，然后比较ue是否在ahm.users中
        first_key = next(keys_iterator)
        first_value = ue[first_key]
        if (first_key in self.users):
            a = self.users.get(first_key)
            if (a == first_value):
                return 1
            else:
                return 0
        else:
            return 0

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(length).decode('utf-8'))
        # You now have a dictionary of the post data
        data = GetData.GetIdAndPwd(post_data)
        print(data)
        result = self.verify(data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

    def GenerateTIDue(self):
        return

def start_server():
    data = {'result': 'this is a test'}
    host = ('localhost', 8982)
    ahm = AHM
    AHMserver = HTTPServer(host, ahm)
    print("Starting server, listen at: %s:%s" % host)
    AHMserver.serve_forever()


if __name__ == '__main__':
    ahm = AHM
    start_server()
    Send_Post.send_post("localhost:8983",path="/index", data={'Lemonade': '1023', 'LMD': '1230'},header={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"})
    print("AHM start server success...")

