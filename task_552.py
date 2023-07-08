# 552. Дано словник, у якому ключами є назви 10 карпатських вершин, 
# а значеннями - їх висота у метрах. Елементи у словнику невпорядковані. 
# Напишіть програму для виведення висоти трьох найвищих гір. Примітка. 
# При використанні метода sorted, можна застосувати як ключ лямбда-функцію 
# на зразок key=lambda x: x[1].
'''
Вхідні дані:
Немає

Вихідні дані:
Hoverla: 2061 m
Brebenescul: 2032 m
Pip Ivan Chernogirsky (Chorna gora): 2028 m
'''
dictionary = {
              'Breskul':1911.0,
              'Hoverla':2061.0,
              'Pip Ivan':2028.5,
              'Brebeneskul':2035.8,
              'Hutyn Tomnatyk':2016.4,
              'Rebra':2001.0, 
              'Menchul':1998.0,
              'Turkul':1933.0, 
              'Petros':2022.5,
              'Smotrych':1898.0
              }
sorted_dictionary = sorted(dictionary.items(),reverse=True, key = lambda x:x[1])
converted_dict = dict(sorted_dictionary)

x = list(converted_dict.items())#it creates list from converted dictionary

c = dict(x[0:3])#it takes first three elements from the list and creates dictionarya again
for key,value in c.items():#it prints dictionary
    print(f"{key}:{value}")#wihch contains only three elements from the first dict