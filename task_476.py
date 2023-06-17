# 476. Напишіть програму, яка приймає 2 цілих числа, a і b і генерує двовимірний 
# масив. Значення елемента в i-му рядку і j-му стовпці масиву має бути i * j 
# (i = 0,1...,a-1; j = 0,1..., b-1).
'''
Вхідні дані:
3 5

Вихідні дані:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
matrix = []
for i in range(a):
    row = []
    for j in range(b):
        row.append(i * j)
    matrix.append(row)
print("Two dimensional matrix: ")
for row in matrix:
    print(row)