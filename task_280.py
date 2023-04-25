# 280.За введеним користувачем цілим числом n визначте n-е число Фібоначчі.
'''
Вхідні дані:

9
3
5

Вихідні дані:

34
2
5

'''
n = int(input("Enter a number: "))
fibonacci = [0,1]
for i in range(2, n + 1):
    next_num = fibonacci[i -1] + fibonacci[i - 2]
    fibonacci.append(next_num)
print(fibonacci)
print(fibonacci[-1])