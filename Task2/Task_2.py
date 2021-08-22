import requests
from collections import Counter


result = []
with open('nginx_log.txt', 'w') as f:
    file_nginx = f.write(requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text)
with open('nginx_log.txt') as f:
    for line in f:
        f_line = str(f.readline().split(' ')[:1])
        result.append(f_line)
    print(len(result)) #уже тут строк в 2 раза меньше чем должно быть
my_dict = Counter(result)
print(my_dict) #проверка работы счетчика
result = (max(my_dict.items(), key=lambda item: item[1])) #избыточно
print(result)
print(f'IP: {str(result[0])}, number of requests: {str(result[1])}')

# Файл создается правильно и содержит 51к+ строк. при чтении строк получается в 2 раза меньше