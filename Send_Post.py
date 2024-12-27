#coding=utf-8
import http.client
import urllib
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib import request, parse
def send_post(url, path, data, header):
    datas = parse.urlencode(data).encode('utf-8')
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    data1 = r1.read()
    print(data1)  #
    conn.close()