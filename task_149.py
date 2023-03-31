#149. Дано трицифрове число. Визначити, чи рівний квадрат суми цифр числа сумі кубів його цифр.

num = int(input("Enter a number: "))
f = num % 100 % 10
s = num % 100 //10
t = num //100

if (f + s + t) ** 2 == (f ** 3 + s ** 3 + t ** 3):
    print(True)
else:
    print(False)