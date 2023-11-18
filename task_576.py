# 576. Дано список цілих чисел, який може містити до 100000 чисел. 
# Визначте, скільки в ньому зустрічається різних чисел.
"""
Вхідні дані:
2 5 7 7 9 0 3 4
3 3 4 4 5 1

Вихідні дані:

7
4
"""
lst_1 = [int(item) for item in input("Enter the list members: ").split()]
set_numbers = set(lst_1)
print(len(set_numbers))