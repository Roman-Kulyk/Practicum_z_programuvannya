# 673. Напишіть функцію для перевірки, чи є даний рядок анаграмою іншого рядка. 
# Букви початкового рядка використовуються одноразово і враховується регістр літер. 
# Примітка. Анаграма - переставлення літер у слові, завдяки чому утворюється нове 
# значення слова.
'''
Вхідні дані:
eleven plus two
twelve plus one
I am Lord Voldemort
tom marVoLo rIddle
Forty five
over fifty

Вихідні дані:
True
True
False
'''
def if_anagram():
    text_1 = input("Enter text_1: ")
    text_2 = input("Enter text_2: ")
    set_1 = set(text_1)
    set_2 = set(text_2)
    if set_1 == set_2:
        print(True)
    else:
        print(False)

if_anagram()