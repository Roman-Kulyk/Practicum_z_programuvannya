# 413. Виведіть всі парні елементи списку. Вводиться список чисел. 
# Всі числа списку знаходяться на одному рядку.
'''
Вхідні дані:
1 2 2 3 3 3 4 4 4 4

Вихідні дані:
2 2 4 4 4 4
'''
list = [1,2,2,3,3,3,4,4,4,4]
for i in list:
    if i % 2 == 0:
        print(i,end=' ')
print()