# 299.Дано натуральне число n (n ≤ 1000). Скласти програму для перевірки чи 
# ділиться ціле число на кожну з його цифр без залишку. 
# Надрукувати такі числа в інтервалі від 10 до n в порядку зростання, 
# через пропуск.
'''
Вхідні дані:

100
40
20

Вихідні дані:

11 12 15 22 24 33 36 44 48 55 66 77 88 99
11 12 15 22 24 33 36
11 12 15

'''
n = int(input("Enter a number: "))
for num in range(10, n+1):
    if all(num % int(dig) == 0):
       for dig in str(num):
        print(num, end ='')