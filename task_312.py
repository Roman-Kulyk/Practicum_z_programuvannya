# 312. Дано рядок. Визначити порядковий номер першої вказаної букви. 
# Якщо такої літери немає, вивести нуль.
'''
Вхідні дані:

euro
r

Вихідні дані:

3
'''
message = input("Enter a string: ")
symbol = input("Enter a symbol to find: ")
print(message.find(symbol))

