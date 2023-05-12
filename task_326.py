# 326. Дано рядок. Замініть у цьому рядку всі цифри 4 на слово Four.
'''
Вхідні дані:

4 Christmases
Fantastic 4
The Nutcracker and the 4 Realms

Вихідні дані:

Four Christmases
Fantastic Four
The Nutcracker and the Four Realms

'''
message = input("Enter a string:")
print(message.replace("4", "Four"))