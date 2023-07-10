# 562. Напишіть програму, яка приймає послідовність чисел і визначає, 
# чи всі числа відрізняються один від одного чи ні. 
# Використовувати цикли не можна.
'''
Вхідні дані:
1 4 5 0 2 4
1 6 9 10

Вихідні дані:
duplicate list
is unique sequence
'''
lst = [int(item) for item in input("Enter the list members: ").split()]
if len(lst) == len(set(lst)):
    print("is unique sequence")
else:
    print("duplicate list")