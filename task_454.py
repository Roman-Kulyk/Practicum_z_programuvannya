# 454.Напишіть програму для друку елементів певного цілочисельного списку після 
# видалення з нього парних чисел. Значення списку вводяться через пропуск в одному 
# рядку.
'''
Вхідні дані:
3 44 6 8 9 12 7

Вихідні дані:
[3, 9, 7]
'''
lst = []
lst = [int(item) for item in input("Enter the list members: ").split()]

odd_number = []
for item in lst:
    if item % 2 != 0:
        odd_number.append(item)
print(odd_number)