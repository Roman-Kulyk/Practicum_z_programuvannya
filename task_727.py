# 727. Напишіть функцію, яка друкує випадкове ціле число від n до m включно.
'''
Вхідні дані:
1
1000

Вихідні дані:
338
'''
import random



def print_random():
    a = int(input())
    b = int(input())
    print(random.randint(a,b))

print_random()