# 323. Напишіть програму, щоб перевірити, з яких символів складається рядок, 
# введений користувачем: лише з цифр, лише з букв, або з букв і цифр.
'''
Вхідні дані:

abc
Street122
23

Вихідні дані:

Your message includes letters only.
Your message includes numbers and letters.
Your message includes numbers only.
'''
txt = input("Enter a text: ")

if txt.isalpha():
    print("Your message includes letters only.")
elif txt.isdigit():
    print("Your message includes numbers only.")
elif txt.isalnum():
    print("Your message includes numbers and letters.")
else:
    pass