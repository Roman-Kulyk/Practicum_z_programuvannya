# 350.Напишіть програму, яка отримує рядок і обчислює кількість 
# цифр і букв у ньому.
'''
Вхідні дані:
Andromeda, M 31, NGC 224

Вихідні дані:
Letters 13
Digits 5
'''
string = input("Enter a string: ")
digits = 0
letters = 0
for char in string:
    if char.isdigit():
      digits += 1
    elif char.isalpha():
        letters += 1
print(f'Letters: {letters}')
print(f'Numbers: {digits}')
    