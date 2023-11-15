#568. Дано дві послідовності цілих чисел. Надрукуйте нову послідовність, 
# яка об’єднує числа, що присутні в обох послідовностях, без дублікатів.
"""
Вхідні дані:
1 5 8 0 2 9
8 3 6 7 1

Вихідні дані:
0 1 2 3 5 6 7 8 9
"""
lst_1 = [int(item) for item in input("Enter the list members: ").split()]
lst_2 = [int(item) for item in input("Enter the list members: ").split()]

set_1 = set(lst_1)
set_2 = set(lst_2)

z = set_1.union(set_2) 
for i in z:
    print(i, end= ' ')
print()