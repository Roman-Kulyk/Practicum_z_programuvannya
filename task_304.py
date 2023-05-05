# 304. Напишіть програму, яка приймає від користувача рядок, 
# і відображає цей рядок у верхньому і нижньому регістрах.
'''
Вхідні дані:

My favourite language is Python

Вихідні дані:

MY FAVOURITE LANGUAGE IS PYTHON
my favourite language is python

'''
message = input("Enter a message: ")
print(message.upper())
print(message.lower())