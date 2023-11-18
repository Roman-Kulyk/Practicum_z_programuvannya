# 580. Дано дві послідовності цілих чисел. Необхідно надрукувати обидві послідовності 
# з числами, які відсутні в іншій послідовності.
"""
Вхідні дані:
1 3 4 5 8 9 12
3 4 7 8 12

Вихідні дані:
1 5 9
7
"""
input_sequence_1 = input("Enter your sequence: ").split()
input_sequence_2 = input("Enter your sequence: ").split()

set_sequence_1 = set(input_sequence_1)
set_sequence_2 = set(input_sequence_2)

z_1 = set_sequence_1.difference(set_sequence_2)
z_2 = set_sequence_2.difference(set_sequence_1) 

print(' '.join(sorted(z_1)))
print(' '.join(sorted(z_2)))