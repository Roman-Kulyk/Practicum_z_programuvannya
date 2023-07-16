# 633. Напишіть функцію, яка може генерувати та друкувати кортеж зі значеннями 
# квадратів чисел від 1 до n включно.
'''
Вхідні дані:
6

Вихідні дані:
(1, 4, 9, 16, 25, 36)
'''
def tuple_square(n):
    list_square = []
    for i in range(1, n + 1):
        i = i * i
        list_square.append(i)
    tuple_square = tuple(list_square)
    print(tuple_square)

tuple_square(6)