from itertools import zip_longest
from re import sub
import sys
import json
import os
# ЗАДАНИЕ ВЫПОЛНЯЛОСЬ ПО УСЛОВИЯМ ПРАКТИЧЕСКОГО ЗАДАНИЯ УРОКА 6 (ПОЭТОМУ ЕСТЬ РАСХОЖДЕНИЯ С МЕТОДИЧКОЙ)


user_dir =(input('Select folder for user file: '))
user_file ='/'+(input('Choose a file name for storing users: '))
os.chdir(user_dir)
user_dir+= user_file
print('file created')
with open(user_dir, 'w', encoding='utf-8') as f_users:
    f_users.write('Иванов,Иван,Иванович\nПетров,Петр,Петрович\nФилиппов,Филипп,Филиппович\nСергеев,Сергей,Сергеевич')

hobby_dir =(input('Select folder for hobby file: '))
user_hobby ='/'+(input('Choose a file name for storing hobby: '))
os.chdir(hobby_dir)
hobby_dir+=user_hobby
print('file created')
with open(hobby_dir, 'w', encoding='utf-8') as f_hobby:
    f_hobby.write('Плаванье,Садоводство\nМоделирование\nЧтение,Горные лыжи')

users = []
hobby = []
with open(user_dir,encoding='utf-8') as f:
    for line in f:
         users.append(str(sub(',', ' ', line.strip()).split(' ')))
with open(hobby_dir,encoding='utf-8') as f:
    for line in f:
        hobby.append(list(sub(',', ' ', line.strip()).split(' ')))
my_dict = dict(zip_longest(users, hobby))
for key in my_dict:
    if key == None:
        my_dict.popitem()
        sys.exit(1)

result_dir =(input('Select folder for result file: '))
result_file = '/' + (input('Choose a file name for storing result: '))
os.chdir(result_dir)
result_dir+=result_file
print('JSON file created')
with open(result_dir, 'w') as f: #не смотря на кодировку в самом json закодированно (почему-то)
    json.dump(my_dict, f)
with open(result_dir) as f:
    print(json.load(f))
