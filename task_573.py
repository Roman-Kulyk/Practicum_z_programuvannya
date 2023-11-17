# 573.Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, 
# так і другому списках, і надрукуйте їх у порядку зростання.
""" 
Вхідні дані:
2 5 8 11 10 9
11 3 7 6 8 5

Вихідні дані:
5 8 11
"""
lst_1 = [int(item) for item in input("Enter the list members: ").split()]
lst_2 = [int(item) for item in input("Enter the list members: ").split()]

set_1 = set(lst_1)
set_2 = set(lst_2)

z = set_1.intersection(set_2) 
for i in sorted(z):
    print(i, end= ' ')
print()