import requests
from collections import Counter


result = []
with open('nginx_log.txt', 'w') as f:
     file_nginx = f.write(requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text)

with open('nginx_log.txt') as f:
    for line in f:
        f_line = str(line.split(' ')[:1])
        result.append(f_line)
my_dict = Counter(result)
result = (max(my_dict.items(), key=lambda item: item[1])) #избыточно
print(f'IP: {str(result[0])}, number of requests: {str(result[1])}')