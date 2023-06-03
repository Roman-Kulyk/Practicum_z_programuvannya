# 437. Напишіть програму для перетворення списку декількох цілих чисел у єдине ціле 
# число. Значення списку вводяться через пропуск в одному рядку.
'''
Вхідні дані:
1 7 9 4

Вихідні дані:
1794
'''
lst = []
lst = [(item) for item in input("Enter the list memebers: ").split()]
print(lst)
result = "".join(lst)
print(int(result))