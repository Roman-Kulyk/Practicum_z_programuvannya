# 387. Напишіть програму, яка зчитує рядок, кодує її запропонованим алгоритмом і виводить 
# закодовану послідовність. Кодування повинно враховувати регістр символів. Правила 
# кодування: групи однакових символів початкового рядка замінюються на цей символ і 
# кількість його повторень в цій позиції рядка. Наприклад: рядок aaaabbbсaa кодується в 
# a4b3с1a2.
"""
Вхідні дані:
aaaabbbcaa
abc
Hello

Вихідні дані:
a4b3c1a2
a1b1c1
H1e1l2o1
"""
def str_coding(text):
    coded_str = ""
    counter = 1

    for i in range(len(text)-1):
        if text[i] == text[i + 1]:
            counter += 1
        else:
            coded_str += text[i] + str(counter)
            counter = 1

    coded_str += text[-1] + str(counter)
    return coded_str

text = input("Enter your string: ")
coded_str = str_coding(text)
print(coded_str)