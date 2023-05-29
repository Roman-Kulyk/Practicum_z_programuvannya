# 411. Виведіть всі елементи списку з парними індексами. Вводиться список чисел. 
# Всі числа списку знаходяться на одному рядку.
'''
Вхідні дані:
1 2 3 4 5

Вихідні дані:
1 3 5
'''
lst = []
lst = [int(item) for item in input("Enter the list items : ").split()]
print(lst)
for i in lst:
    if lst.index(i)%2==0:
        print(i, end=" ")
print()


