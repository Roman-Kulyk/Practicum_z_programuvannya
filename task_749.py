# 749. Напишіть програму для розрахунку кількості днів між двома датами, використовуючи модуль datetime.
'''
Вхідні дані:
2018
8
1
2019
3
4

Вихідні дані:
215
'''
from datetime import date as date_n


def number_of_days(date_1, date_2):
    print(date_1)
    print(date_2)
    result = (date_2-date_1).days
    print(result)

number_of_days(date_n(2018,8,1),date_n(2019,3,4))

#date_1 = date_n(2018,8,1)
#date_2 = date_n(2019,3,4)