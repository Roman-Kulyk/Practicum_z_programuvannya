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
from operator import itemgetter
#initializing dictionary

dictionary = {'Burj Khalifa': 828, 'Shanghai Tower': 632, 'Abraj Al Bait': 601}

#printing original dictionary
print("The original dictionary is: " + str(dictionary))

#sorting dictionary by keys and values
res = dict(sorted(dictionary.items(), key = itemgetter(0, 1)))

#printing result
print("Sorted dictionary: " + str(res))