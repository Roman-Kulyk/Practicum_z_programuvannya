# 729. Дано додатне дійсне число n. Виведіть його дробову і цілу частину. Використайте модуль math.
'''
Вхідні дані:
7.9
5.8

Вихідні дані:
(0.9000000000000004, 7.0)
(0.7999999999999998, 5.0)
'''
import math

print(math.modf(5.8))#it returns the integer and fractional parts of float as a tuple, in that order
print(math.modf(7.9))#it returns the integer and fractional parts of float as a tuple, in that order