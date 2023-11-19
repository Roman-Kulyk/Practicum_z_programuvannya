# 583.  Дано два списки чисел, які можуть містити до 10000 чисел кожен. Виведіть всі числа, 
# які входять як в перший, так і в другий список в порядку зростання. Вводяться два списки 
# цілих чисел. Всі числа кожного списку знаходяться на окремому рядку.
"""
Вхідні дані:
4 6 8 9
1 9 3 6

Вихідні дані:
6 9
"""
lst_1 = [int(item) for item in input("Enter the list members: ").split()]
lst_2 = [int(item) for item in input("Enter the list members: ").split()]

set_1 = set(lst_1)
set_2 = set(lst_2)

z = set_1.intersection(set_2) 
list_z = list(z)

for i in sorted(list_z):
    print(i, end = ' ')
print()
