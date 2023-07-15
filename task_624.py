# 624. Напишіть функцію для вставки рядка всередину іншого рядка.
'''
Вхідні дані:
[] Python
<<>> HTML
qwerty 123

Вихідні дані:
[Python]
<<HTML>>
qwe123rty
'''
def insertion(text_1, text_2):
    middle = len(text_1) // 2
    print(text_1[:middle]+text_2+text_1[middle:])


insertion('[]','Python')
insertion('<<>>','HTML')
insertion('qwerty', '123')
