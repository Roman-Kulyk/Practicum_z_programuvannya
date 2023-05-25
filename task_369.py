# 369. Користувач вводить рядок і певний символ. Напишіть програму, 
# яка друкує індекс розташування другої появи введеного символа у рядку. 
# Якщо рядок містить введений символ лише один раз, то надрукуйте -1, 
# а якщо рядок не містить шуканого символа, то надрукуйте -2.
'''
Вхідні дані:
The morning's sun rose clear and resplendent, touching the foamy waves into a network of ruby-tinted light.
s

Вихідні дані:
14
'''
s = input("Enter a string: ")
c = input("Enter a char to find: ")
first_index = s.find(c)
if first_index == -1:
    print("-2")
else:
    second_index = s.find(c,first_index + 1)
if second_index == -1:
    print("-1")
else:
    print(second_index)