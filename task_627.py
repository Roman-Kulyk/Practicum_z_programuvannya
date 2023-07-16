# 627. Напишіть функцію, яка приймає ціле число і друкує інформацію про парність чи непарність числа.
'''
Вхідні дані:
2
9

Вихідні дані:
True
False
'''
def even_or_odd(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)

even_or_odd(2)
even_or_odd(9)