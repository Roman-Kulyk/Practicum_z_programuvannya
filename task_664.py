# 664. Напишіть функцію для сортування рядка в алфавітному порядку 
# без врахування регістру літер.
'''
Вхідні дані:
JavaScript
Python

Вихідні дані:
aaciJprStv
hnoPty
'''
def sortString():
    return "".join(sorted(str, key = lambda x:x.lower()))
     
str = input('Enter your text: ')
print(sortString())

sortString()