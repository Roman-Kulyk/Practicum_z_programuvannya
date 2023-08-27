# 739. Напишіть програму для обчислення найменшого спільного кратного (LCM) двох натуральних чисел. 
# Використайте модуль fractions.
'''
Вхідні дані:
15 17

Вихідні дані:
255
'''
import math#previously method gcd was in fractions module
def lcm(a,b):
    return abs(a*b) // math.gcd(a,b)

print(lcm(17,15))
print(lcm(23,14))