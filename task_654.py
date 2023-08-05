# 654. Напишіть функцію для визначення, чи рік високосний чи ні.
'''
Вхідні дані:
2023
2020

Вихідні дані:
False
True
'''
def leap_year(year):
    if year % 400 == 0:
        print(True)
    elif year % 100 == 0 and year % 400 != 0:
        print(False)
    elif year % 4 == 0:
        print(True)
    else:
        print(False)

leap_year(2023)
leap_year(2020)
leap_year(2000)
leap_year(2026)
leap_year(2028)