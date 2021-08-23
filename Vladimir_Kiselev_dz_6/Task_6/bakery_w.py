print('___Bakery DB___ (write)')
data = input('enter your data(sep comma):')+', '
with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.writelines(data)
