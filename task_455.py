# 455. Дано дві цілочисельні послідовності, елементи яких розділені пропуском і 
# комою. Напишіть програму, яка повертає послідовність, що містить лише елементи, 
# які є загальними між введеними послідовностями (без дублікатів). Переконайтеся, що 
# ваша програма працює на двох послідовностях різних розмірів.
'''h
Вхідні дані:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13

Вихідні дані:
1 2 3 5 8 13
'''
lst_1 = []
lst_2 = []
lst_1 = [int(item) for item in input("Enter the list members: ").split(', ')]
lst_2 = [int(item) for item in input("Enter the list members: ").split(', ')]

common_lst = []
for item in lst_1: 
    if item in lst_2:
        common_lst.append(item)
         
common_set = set(common_lst)
for item in common_set:
    print(item, end = " ")
print()
