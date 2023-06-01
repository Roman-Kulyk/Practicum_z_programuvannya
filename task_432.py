# 432. Напишіть програму, щоб перевірити, чи певне ціле число n перевищує всі 
# елементи цілочисельного списку. Значення списку вводяться через пропуск в одному 
# рядку, число n вводиться у новому рядку.
'''
Вхідні дані:
4 67 109 25 44 12
99

Вихідні дані:
False
'''
lst = []
lst = [int(item) for item in input("Entet the list members: ").split()]
n = int(input("Enter the number: "))
if n > sum(lst):
    print(True)
else:
    print(False)