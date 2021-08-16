# Task_2/3
import requests
import re
from datetime import datetime


def currency_rates(curr):
    resp = list(filter(None, ((re.sub('[<>="]', ' ', requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text)).split(' '))))
    for item in range(len(resp)):# почему не работает просто: for item in resp
        if resp[item] == 'Date':
            date_serv = (datetime.strptime(resp[item+1], '%d.%m.%Y')).date()
        if curr.upper() not in resp:
            print('None')
            break
        if resp[item] == curr.upper():
            nom = resp[item:].index('Nominal')
            val = (resp[item:].index('Value'))
            print(f'Corrent rate for {resp[item:][nom+1]} {curr.upper()}: {resp[item:][val+1]} rub., date: {date_serv}')


currency_rates('Eur')