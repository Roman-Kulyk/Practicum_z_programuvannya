# 504. Анаграма - переставлення літер у слові, завдяки чому утворюється нове значення 
# слова. Напишіть програму, яка перевіряє, чи є два введених слова анаграмами. Програма 
# повинна вивести True в разі, якщо введені слова є анаграмами, і False в інших випадках. 
# Слово може складатися тільки з англійських символів. Регістр букв не повинен впливати на 
# відповідь.
"""
Вхідні дані:
restful
fluster
forty-five
over-fifty
anagram
naganra

Вихідні дані:
True
True
False
"""
word_1 = input("Enter your first word: ")
word_2 = input("Enter your second word: ")
#print(type(word_1), type(word_2))

word_1_sorted = sorted(word_1)
word_2_sorted = sorted(word_2)
#print(word_1_sorted)
#print(word_2_sorted)

if word_1_sorted == word_2_sorted:
    print(True)
else:
    print(False)