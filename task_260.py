# 260. Дано цілі числа a і b. Обчислити ab, не використовуючи операцію піднесення до степеня.
'''
Вхідні дані:

4
2

Вихідні дані:

16
'''


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

for i in range(1,b+1):
    a *= a
print(a)