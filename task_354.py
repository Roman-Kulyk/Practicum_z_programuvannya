# 354. Напишіть програму для перевірки чи є введена літера голосною або приголосною.
'''
Вхідні дані:
F
e

Вихідні дані:
F is a consonant
e is a vowel
'''
vowel = ['a','e','i','o','u']
char = input("Enter a letter: ")
if char in vowel:
    print(char + " is a vowel.")
else:
    print(char + " is consonant.")