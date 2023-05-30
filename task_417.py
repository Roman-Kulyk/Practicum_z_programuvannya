# 417. Вводиться список чисел. Всі числа списку знаходяться в одному рядку. 
# Обчисліть, скільки у списку різних елементів, не змінюючи самого списку.
'''
Вхідні дані:
5 7 7 9 12

Вихідні дані:
4
'''
lst = []
lst = [int (item) for item in input("Enter the list items: ").split()]
elements = []
for i in lst:
    if i not in elements:
        elements.append(i)
    else:
        pass
print(len(elements))
    
