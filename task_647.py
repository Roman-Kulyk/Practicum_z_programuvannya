# 647. Надрукуйте найменше з трьох введених чисел без використання вбудованої 
# функції min(). Для цього напишіть першу функцію, яка повертає найменше число з 
# двох заданих. У другій функції реалізуйте використання першої функції для визначення 
# найменшого значення серед трьох чисел.
'''
Вхідні дані:
5 8 11
12 12 24
1 1 1

Вихідні дані:
5
12
1

def minimum_func(var_1, var_2, var_3):
    if var_1 <= var_2 and var_1 <= var_3:
        print(var_1)
    elif var_2 <= var_1 and var_2 <= var_3:
        print(var_2)
    elif  var_3 <= var_2 and var_3 <= var_1:
        print(var_3)

minimum_func(5, 8, 11)
minimum_func(12, 12, 24)
minimum_func(1, 1, 1)
'''
def min_two_numbers(a,b):
    if a < b:
        return a
    else:
        return b

def min_of_three_numbers(a,b,c):
    min_ab = min_two_numbers(a,b)
    if c < min_ab:
        return c
    else:
        return min_ab
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

min_number = min_of_three_numbers(a, b, c)
print(min_number)






