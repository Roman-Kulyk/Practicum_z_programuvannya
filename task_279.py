# 279. Напишіть програму для отримання рядка Фібоначчі від 0 до n, де n - ціле число. 
# Послідовність Фібоначчі - це серія чисел 0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
# Кожне наступне число знайдено шляхом додавання двох номерів перед ним.

'''
Вхідні дані:

50

Вихідні дані:

1 1 2 3 5 8 13 21 34

'''
n = int(input("Enter a number: "))
fibonacci = [0,1]
for i in range(2, n + 1):
    next_num = fibonacci[i -1] + fibonacci[i - 2]
    fibonacci.append(next_num)
print(f"First {n} terms of the Fibonacci sequence:{fibonacci}")