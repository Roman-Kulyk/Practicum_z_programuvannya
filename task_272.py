# 272. Дано два натуральних числа a і b. Розробити програму для визначення найбільшого спільного 
# дільника (НСД) заданих чисел. Використайте алгоритм Евкліда .
'''
Вхідні дані:

8
2

Вихідні дані:

2

'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: ")) 

while b:
    a, b = b, a % b
print(a)