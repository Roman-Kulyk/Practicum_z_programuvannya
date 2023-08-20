# Використайте модуль sqlite3, щоб створити базу даних SQLite під назвою imdb.db і таблицю ratings, що містить 
# наступні поля: id (INTEGER PRIMARY KEY), title (VARCHAR(20)), year (INT), rating (FLOAT). Зчитайте дані з файла 
# imdb.csv і додайте їх у таблицю ratings. Зчитайте і виведіть на екран усі значення таблиці ratings у 
# алфавітному порядку за полем title. Зчитайте і виведіть на екран усі записи таблиці ratings з ретингом більшим 
# за 8.70.

import sqlite3

with open('ex_#883_10_imdb.csv', 'rt' ) as freading:
    lines = freading.readline()
    print(type(lines))


conn = sqlite3.connect('imdb.db') 
curs = conn.cursor() 
curs.execute('''CREATE TABLE ratings (id INT PRIMARY KEY, title VARCHAR(20), year INT, rating FLOAT)''') 
curs.execute('INSERT INTO  ratings VALUES(lines[0]: lines[1]: lines[2]: lines[3]')
conn.commit() 
curs.close() 
conn.close() 


