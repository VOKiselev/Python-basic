import requests


result =[]
with open('nginx_log.txt', 'w') as f:
    file_nginx = f.write(requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text)

with open('nginx_log.txt') as f:
    for line in f:
        f_line = line.split(' ')[0:7]
        f_result = (f_line[0], f_line[5][1:4], f_line[6])
        result.append(f_result)
print(result)