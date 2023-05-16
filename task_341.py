# 341. Виведіть поспіль, без пропусків, усі символи, що лежать в таблиці ASCII 
# між двома заданими символами. Програма отримує на вхід два символу, кожен в 
# окремому рядку і повинна вивести рядок, що починається першим із заданих символів 
# і закінчується другим.
'''
Вхідні дані:
A
F
0
9
Вихідні дані:
ABCDEF
0123456789
'''
n = input("Enter a first symbol: ")
m = input("Enter a last symbol: ")
n_num = ord(n)#Given a string representing one Unicode character,... 
m_num = ord(m)#returns an integer representing the Unicode code point of that character.

for i in range(n_num, m_num +1):
    print(chr(i),end='')
print()