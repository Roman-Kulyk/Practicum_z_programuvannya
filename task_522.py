# 522. Напишіть програму для підрахунку кількості символів (символьної частоти)
# у введеному рядку.
'''
Вхідні дані:
google

Вихідні дані:
g 2
o 2
l 1
e 1
'''
text = input("Enter your string: ")
dictionary = {}

for i in text:
    if i in dictionary:
        dictionary[i] +=1
    else:
        dictionary[i] = 1

for key, value in dictionary.items():
    print(key,value)