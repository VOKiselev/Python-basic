# Task_2 
import requests
import re


# with open('nginx_log.txt', 'w') as f:
#     file_nginx = f.write(requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text)

RE_IP = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
RE_TIME = re.compile(r'^\d{2}/\w+/\d{4}(:\d{2}){3}$')
RE_TIME_1 = re.compile(r'^\+\d{4}$')
RE_GET = re.compile(r'^\w{4}$')
RE_RES = re.compile(r'^/\w{9}/\w{7}\d$')
RE_NUM = re.compile(r'^\d{1,4}$')

with open('nginx_log.txt') as f:
    for line in f:
        f_line = (re.sub('[^a-zA-Z0-9/.:+ ]', '', line).split())[0:8]
        a = (item for item in f_line if RE_IP.match(item) or RE_TIME.match(item) or RE_TIME_1.match(item)\
            or RE_GET.match(item) or RE_RES.match(item) or RE_NUM.match(item))
        print(tuple(a))