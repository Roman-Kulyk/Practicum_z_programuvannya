#190. Напишіть програму, яка отримує на вхід три цілих числа, по одному числу в рядку, 
#і виводить у три рядки спочатку максимальне, потім мінімальне, після чого число, що залишилося. 
#Вводитися можуть повторювані числа. Використайте лише конструкції розгалуження, 
#без обміну значеннями між двома змінними.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a == b == c:
    print(a)
    print(b)
    print(c)

elif a >= b >= c:
    print(a)
    print(c)
    print(b)

elif a >= c >= b:
    print(a)
    print(b)
    print(c)
elif b >= a >= c:
    print(b)
    print(c)
    print(a)

elif b >= c >= a:
    print(b)
    print(a)
    print(c)

elif c >= a >= b:
    print(c)
    print(b)
    print(a)

elif c >= b >= a:
    print(c)
    print(a)
    print(b)