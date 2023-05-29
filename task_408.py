# 408. Збережіть назви мов світу, які вводяться в одному рядку через пропуск, у 
# списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному 
# порядку. Відсортуйте список в порядку протилежному алфавітному і виведіть його 
# елементи в рядку через пропуск.
'''
Вхідні дані:
Ukrainian French Bulgarian Norwegian Latvian

Вихідні дані:
Ukrainian Norwegian Latvian French Bulgarian
'''
txt = input("Enter your string: ")

x = txt.split()#it splits strings into a list
x.sort(reverse=True)#it sorts list in reverse order
for i in x:#for every item in list
    print(i,end=' ')#prints items in the same lint through a space
print()

