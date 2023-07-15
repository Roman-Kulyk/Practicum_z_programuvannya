# 619. Напишіть функцію для перевірки того, 
# чи введена літера є голосною чи приголосною.
'''
Вхідні дані:
c
e

Вихідні дані:
False
True
'''
def is_vowel(char):
    vowels =('a','e','o','i','u')
    if char in vowels:
        print(True)
    else:
        print(False)


is_vowel('c')
is_vowel('e')