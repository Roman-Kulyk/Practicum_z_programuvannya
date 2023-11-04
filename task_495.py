# 495. Вводиться рядок, який може мати пропуски на початку, між словами і у кінці. 
# Пропусків може бути більше одного. Необхідно привести рядок до нормального вигляду, 
# тобто видалити усі пропуски, а між словами залишити тільки один пропуск.
"""
Вхідні дані:
      The   Zen     of     Python

Вихідні дані:
The Zen of Python
"""
test_list = input("Enter your list: ").split()
print(test_list)
str = ''
for ele in test_list:
        str += ' ' + ele
str_final = str[1:]
print(str_final)