# 730. Напишіть програму, яка форматує текст, показаний у вихідних даних, із шириною n. 
# Використайте модуль textwrap.
'''
Вхідні дані:
35

Вихідні дані:
Python is a widely used high-level,
general-purpose, interpreted,
dynamic programming language. Its
design philosophy emphasizes code
readability, and its syntax allows
programmers to express concepts in
fewer lines of code than possible
in languages such as C++ or Java.
'''
import textwrap

text = "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its \
design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in\
fewer lines of code than possible in languages such as C++ or Java."

text_wrapped = textwrap.fill(text,width=35)
print(text_wrapped)