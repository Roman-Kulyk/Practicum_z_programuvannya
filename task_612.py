# 612. Напишіть функцію для визначення більшого з двох цілих чисел без використання 
# вбудованої функції max(). Якщо числа рівні, то вивести повідомлення equal.
'''
Вхідні дані:
12 56
11 4
3 3

Вихідні дані:
56
11
equal
'''
def maximum(var_1, var_2):
    if var_1 > var_2:
        print(var_1)
    elif var_2 > var_1:
        print(var_2)
    else:
        print('equal')


maximum(12, 56)
maximum(11, 4)
maximum(3, 3)