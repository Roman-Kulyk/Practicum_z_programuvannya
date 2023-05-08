# 315. Скласти програму, яка визначає, який з двох введених рядків довший 
# і друкує його. Якщо рядки рівні, вивести повідомлення equally.
'''
Вхідні дані:

Linus
Guido

Вихідні дані:

equally

'''
row_1 = input("Enter a string: ")
row_2 = input("Enter another string: ")
if len(row_1) > len(row_2):
    print(row_1)
elif len(row_2) > len(row_1):
    print(row_2)
else:
    print("equally")