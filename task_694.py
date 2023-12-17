# 694. Напишіть рекурсивну функцію для обчислення суми списку цілих чисел.
"""
Вхідні дані:
1 4 7 90 45 23 16

Вихідні дані:
186
"""
def rec_sum(list_num):
    if not list_num:
        return 0
    else:
        return list_num[0]+ rec_sum(list_num[1:])
    

my_list = [int(item) for item in input("Enter the list members: ").split()]
result = rec_sum(my_list)
print(result)