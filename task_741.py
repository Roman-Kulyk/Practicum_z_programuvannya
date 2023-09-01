# 741. Напишіть програму для сортування словника пар «будівля-висота» за значеннями і ключами (в порядку зростання і спадання). 
# Використайте модуль operator.
'''
Вхідні дані:
Немає

Вихідні дані:
[('Burj Khalifa', 828), ('Shanghai Tower', 632), ('Abraj Al Bait', 601)]
[('Abraj Al Bait', 601), ('Shanghai Tower', 632), ('Burj Khalifa', 828)]
[('Abraj Al Bait', 601), ('Burj Khalifa', 828), ('Shanghai Tower', 632)]
[('Shanghai Tower', 632), ('Burj Khalifa', 828), ('Abraj Al Bait', 601)]
'''

import operator
dictionary = {'Burj Khalifa': 828, 'Shanghai Tower': 632, 'Abraj Al Bait': 601}
print(operator.itemgetter(dictionary))
print(operator.itemgetter(dictionary))