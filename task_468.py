# 468. Напишіть програму для видалення кожного третього елемента із цілочисельного 
# списку і друку результуючого списку, доки список не стане порожнім. Початковий 
# список цілих чисел вводиться в одному рядку через пропуск.
'''
Вхідні дані:
2 5 8 9 4 78 7 1

Вихідні дані:
[2, 5, 9, 4, 78, 7, 1]
[2, 5, 4, 78, 7, 1]
[2, 5, 78, 7, 1]
[2, 5, 7, 1]
[2, 5, 1]
[2, 5]
[5]
[]
'''
numbers = input().split()
i = 0
while i < len(numbers):
    if (i + 1)% 3 == 0:
        numbers.pop(i)
    else: 
        i += 1
    print(numbers)