# 628. Напишіть функцію для друку парних чисел із заданої послідовності цілих чисел.
'''
Вхідні дані:
32 4 7 9 11 13 15 8

Вихідні дані:
32 4 8
'''
def if_even(*nums):
    nums_list = []
    for num in nums:
        if num % 2 == 0:
            nums_list.append(num)
    
    for i in nums_list:
        print(i, end = " ")
    print()

if_even(32, 4, 7, 9, 11, 13, 15, 8)