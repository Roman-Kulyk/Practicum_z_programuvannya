# 582. Дано два списки чисел, які можуть містити до 100000 чисел кожен. 
# Порахуйте, скільки чисел міститься одночасно як в першому списку, так і в другому списках. 
# Вводяться два списки цілих чисел. Всі числа кожного списку знаходяться на окремому рядку.
"""
Вхідні дані:
3 5 8
5 2 3

Вихідні дані:
2
"""
lst_1 = [int(item) for item in input("Enter the list members: ").split()]
lst_2 = [int(item) for item in input("Enter the list members: ").split()]

set_1 = set(lst_1)
set_2 = set(lst_2)

z = set_1.intersection(set_2) 
print(len(z))
