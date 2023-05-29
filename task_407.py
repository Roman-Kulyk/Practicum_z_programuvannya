# 407. Збережіть назви мов світу, які вводяться в одному рядку через пропуск, у 
# списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному 
# порядку. Відсортуйте список в алфавітному порядку і виведіть його елементи в 
# рядку через пропуск.
'''
Вхідні дані:
Ukrainian French Bulgarian Norwegian Latvian

Вихідні дані:
Bulgarian French Latvian Norwegian Ukrainian
'''
txt = input("Enter your string: ")

x = txt.split()
print(x)
x.sort()
print(x) 
for i in x:
    print(i,end=' ')
print()

