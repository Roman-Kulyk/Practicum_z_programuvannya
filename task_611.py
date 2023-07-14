# 611. Напишіть функцію для отримання рядка з перших n символів іншого рядка. 
# Якщо довжина рядка менше n, поверніть початковий рядок.
'''
Вхідні дані:
5
Java
2
Java

Вихідні дані:
Java
Ja
'''
def row_func(text, char):
    if len(text) >= char:
        print(text[:char])
    else:
        print(text)
    
row_func('Java',5)
row_func('Java',2)