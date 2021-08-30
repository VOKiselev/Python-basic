# Task_6
import sys
from sys import argv

script, *is_slice = argv


def sales(*args):
    sales_line = line.strip().split(',')[s_start - 1:s_end]
    for i, value in enumerate(sales_line):
        print(f'{i + s_start}) {float(value):0.2f}')

s_start = 1
s_end = -1
print('Sales: ')
with open('bakery.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if len(is_slice) == 2:
            s_start = int(is_slice[0])
            s_end = int(is_slice[1])
            sales(s_start, s_end)
        elif len(is_slice) == 1:
            s_start = int(is_slice[0])
            sales(s_start, s_end)
        elif len(is_slice) <= 0:
            sales(s_start)
        else:
            print('incorrect args')
            sys.exit(1)
input('')

