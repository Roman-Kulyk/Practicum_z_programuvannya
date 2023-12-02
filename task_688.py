# 688. Напишіть функцію для створення всіх можливих перестановок елементів з послідовності 
# різних цілих чисел.
"""
Вхідні дані:
1 2 3

Вихідні дані:
[[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
"""
from itertools import permutations
def generate_permutations(sequence):
    return list(permutations(sequence))

input_sequence = [1,2,3]
permutations_list = generate_permutations(input_sequence)

print("All possible permutations: ")
print(permutations_list)

