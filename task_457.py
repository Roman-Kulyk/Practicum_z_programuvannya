# 457. Напишіть програму для знаходження медіани з трьох введених цілих чисел. 
# Числа вводяться в одному рядку через пропуск.
'''
Вхідні дані:
25 50 11
1 9 7

Вихідні дані:
25
7
'''
lst = []
lst = [int(item) for item in input("Enter the list memebers: ").split()]
if lst[0] > lst[1] > lst[2]:
    print(lst[1])
elif lst[0] > lst[2] > lst[1]:
    print(lst[2])
elif lst[1] > lst[0] > lst[2]:
    print(lst[0])
elif lst[1] > lst[2]>lst[0]:
    print(lst[2])
elif lst[2] > lst[0]>lst[1]:
    print(lst[0])
elif lst[2] > lst[1]>lst[0]:
    print(lst[1])