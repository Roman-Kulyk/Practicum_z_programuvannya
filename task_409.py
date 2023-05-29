# 409. Збережіть назви мов світу, які вводяться в одному рядку через пропуск, 
# у списку. Виведіть елементи списку в зворотному порядку в рядку через пропуск.
'''
Вхідні дані:
Ukrainian French Bulgarian Norwegian Latvian

Вихідні дані:
Latvian Norwegian Bulgarian French Ukrainian
'''
txt = input("Enter your string: ")

x = txt.split()#it splits strings into a list
x.sort(reverse=True)#it sorts list in reverse order
for i in x:#for every item in list
    print(i,end=' ')#prints items in the same lint through a space
print()