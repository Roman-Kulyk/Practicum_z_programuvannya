# 414. Знайдіть кількість додатних елементів у введеному списку. 
# Вводиться список чисел. Всі числа списку знаходяться на одному рядку.
'''
Вхідні дані:
2 -4 5 6 -3

Вихідні дані:
3
'''
lst = []
lst = [int(item) for item in input("Enter the list items : ").split()]
print(lst)
positive = 0
for i in lst:
    if i > 0:
        positive+=1
    else:
        pass
print(positive)

