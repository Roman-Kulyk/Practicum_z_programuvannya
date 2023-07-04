# 538. Дано два списки чисел. Порахуйте, скільки унікальних цифр міститься в 
# обох з них.
'''
Вхідні дані:
1 6 3 5 6
10 12 6 5 1 4

Вихідні дані:
3
'''
list_1 = {1,6,3,5,6}
list_2 = {10,12,6,5,1,4}
set_1 = set(list_1)
set_2 = set(list_2)

set_3 = set_2.difference(set_1)
set_4 = set_1.difference(set_2)
print(set_3, set_4)
print(len(set_3)+len(set_4))

set_5 = set_1.union(set_2)
print(set_5)
print(len(set_5))