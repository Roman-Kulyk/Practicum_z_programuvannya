# 431. Напишіть програму для друкування всіх парних чисел із введеного списку чисел 
# у тому ж порядку і припиніть друк, якщо у списку буде число n або нуль. Значення 
# списку вводяться через пропуск в одному рядку, число n вводиться у новому рядку.
'''
Вхідні дані:
1 8 9 0 4 2 5 6
2

Вихідні дані:
8
'''
lst = []
lst = [int(item) for item in input("Enter the list members: ").split()]
n = int(input("Enter a number: "))
for num in lst:
    if num == 0 or num == n:
        break
    elif num % 2 == 0:
        print(num)


