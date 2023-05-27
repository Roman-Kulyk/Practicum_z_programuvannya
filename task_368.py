# 368. Користувач вводить рядок і певний символ. Напишіть програму, 
# яка друкує місця розташування (індекси) першої та останньої появи введеного 
# символа. Якщо символ зустрічається лише один раз, то виведіть його індекс. 
# Якщо символ не зустрічається, надрукуйте missing. У цьому завданні не можна 
# використовувати цикли.
'''
Вхідні дані:
9965 GNU
6
9965 GNU
9
9965 GNU
N
9965 GNU
A

Вихідні дані:
2
0 1
6
missing
'''
txt = input("Enter a string: ")
char = input("Enter a chararcter to find: ")
amount = txt.count(char)


if amount ==2:
    x_1 = txt.index(char)
    x_2 = txt.rindex(char)
    print(x_1,x_2)
elif amount == 1:
    x_1 = txt.index(char)
    print(x_1)  
elif amount == 0:
    print("is missing")
else:
    pass
