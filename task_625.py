# 625. Напишіть функцію для перетворення літер введеного рядка у великі, 
# якщо він містить принаймні n великих літер в перших m символах. 
# Спочатку вводиться сам рядок, а в з нового рядка - числа n і m.
'''
Вхідні дані:
Python
1 3
Ruby
2 2

Вихідні дані:
PYTHON
Ruby
'''
def upper_letters(text, n, m):
    upper_letters_list = []
    for i in text[0:m]:
        if i.isupper():
            upper_letters_list.append(i)

    if len(upper_letters_list) >= n:
        print(text.upper())
    else:
        print(text)


upper_letters('PYthon',1,3)
upper_letters('Ruby',2,2)