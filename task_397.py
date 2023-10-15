# 397. Шифр Цезаря полягає в заміні кожного символу вхідного рядка на символ, що 
# знаходиться на кілька позицій ліворуч або праворуч його в алфавіті. Напишіть програму, 
# яка шифрує текст шифром Цезаря. Використовуваний алфавіт - пропуск і малі літери 
# англійського алфавіту. На першому рядку вказується зміщення шифрування: ціле число. 
# Додатне число відповідає зміщенню вправо. На другому рядку вказується непорожній рядок-
# фраза для шифрування. Результатом роботи програми має бути записана зашифрована 
# послідовність.
"""
Вхідні дані:

Вхідні дані:
3
i am caesar
26
abc
1
Python

Вихідні дані:
lcdpcfdhvdu
abc
qzuipo
"""


def decrypt_text(text,k):
    decrypt_text = ""

    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset + k) % 26 + ascii_offset)
            decrypt_text += decrypted_char
        else:
            decrypt_text += char
    return decrypt_text

encrypted_text = input('Enter your text: ')
k = int(input("Enter your number: "))

decrypted_text = decrypt_text(encrypted_text,k)
print(decrypted_text)
