# 744. За правилами числа округлюються до найближчого цілого числа, а якщо дробова частина числа дорівнює 0.5, 
# то число округляється вгору. Дано невід’ємне число x, яке необхідно округлити за цими правилами. Зверніть увагу, 
# що функція round() не підходить для цього завдання! Використайте функції ceil() і floor() з математичного модуля math.
'''
Вхідні дані:
3.4
10.6

Вихідні дані:
3
11
'''
import math
number = float(input('Enter your number: '))
print(math.ceil(number))
print(math.floor(number))