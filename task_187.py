#187.Визначити максимальну і мінімальну цифри із введеного трицифрового числа і вивести цифри в одному рядку 
#через пропуск. Якщо цифри однакові, то вивести лише одну цифру.


num = int(input("Enter a number: "))
a = num//100
b = num % 100 // 10
c = num % 100 % 10

if a == b == c:
    print(a)
elif a >= b >= c:
    print(str(a)+ ' ' + str(c))
elif a >= c >= b:
    print(str(a)+ ' ' + str(b))
elif b >= a >= c:
    print(str(b)+ ' ' + str(c))
elif b >= c >= a:
    print(str(b)+ ' ' + str(a))
elif c >= a >= b:
    print(str(c)+ ' ' + str(b))
elif c >= b >= a:
    print(str(c)+ ' ' + str(a))