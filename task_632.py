# 632. Напишіть функцію для створення і друку списку, в якому значення - квадрати 
# цілих чисел від 1 до n включно.
'''
Вхідні дані:
5

Вихідні дані:
[1, 4, 9, 16, 25]
'''
def list_square(n):
    list_square = []
    for i in range(1, n + 1):
        i = i * i
        list_square.append(i)
    print(list_square)

list_square(5)
