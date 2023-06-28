# 519. Напишіть програму, яка приймає рядок символів, і обчислює кількість 
# букв і цифр.
'''
Вхідні дані:
Project Gutenberg offers over 59,000 free eBooks

Вихідні дані:
LETTERS 36
DIGITS 5
'''

text = input("Enter a text: ")

letters = 0
digits = 0

for i in text:
    if i.isalpha():
        letters +=1
    elif i.isdigit():
        digits +=1

print('LETTERS', letters)
print('DIGITS', digits)