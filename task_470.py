# 470. Дано послідовність цілих чисел, яка вводиться в рядку через пропуск. 
# Визначте два найменших елемента послідовності. Вони можуть бути як рівні між собою 
# (обидва бути мінімальними), так і відрізнятися.
'''
Вхідні дані:
14 3 40 56 42 43 89 69 64 72 5 44 11 25

Вихідні дані:
5 3
'''
lst = [int(item) for item in input("Enter the list members: ").split()]
lst.sort()
print(lst[1], lst[0])