# 578. Напишіть програму для пошуку загальних елементів з двох введених рядків слів.
"""
Вхідні дані:
Red Green Orange White
Black Green White Pink

Вихідні дані:
White Green
"""
input_sequence_1 = input("Enter your sequence: ").split()
input_sequence_2 = input("Enter your sequence: ").split()

set_sequence_1 = set(input_sequence_1)
set_sequence_2 = set(input_sequence_2)

z = set_sequence_1.intersection(set_sequence_2) 

print(' '.join(z))