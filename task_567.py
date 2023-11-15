# 567.Дано дві послідовності цілих чисел. 
# Надрукуйте числа, які присутні в обох послідовностях.
"""
Вхідні дані:
1 5 8 0 2 9
8 3 6 7 1

Вихідні дані:
8 1
"""
lst_1 = [int(item) for item in input("Enter the list members: ").split()]
lst_2 = [int(item) for item in input("Enter the list members: ").split()]

set_1 = set(lst_1)
set_2 = set(lst_2)

z = set_1.intersection(set_2) 
for i in z:
    print(i, end= ' ')
print()