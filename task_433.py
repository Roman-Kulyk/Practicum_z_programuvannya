# 433. Цілі числа (додатні і від’ємні) вводяться через пропуск в одному рядку. 
# Напишіть програму для друку списку лише із введених додатних чисел.
'''
Вхідні дані:
0 9 -4 6 8 -15 4

Вихідні дані:
[9, 6, 8, 4]
'''
lst = []
lst = [int(item) for item in input("Enter the list members: ").split()]
positive = []
for item in lst:
    if item > 0:
        positive.append(item)
print(positive)