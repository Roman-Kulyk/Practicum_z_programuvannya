# 314. Напишіть програму, яка отримує три рядки: прізвище, ім’я і по батькові особи, 
# а потім виводить на екран ініціали та прізвище.
'''
Вхідні дані:

Hansson
David
Heinemeier

Вихідні дані:

D.H.Hansson


'''

name = input("Enter your name: ")
surname = input("Enter your surname: ")
lastname = input("Enter your lastname: ")
print(name[0]+'.'+surname[0]+'.',lastname)