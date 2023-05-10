# 319.Напишіть програму, яка зчитує значення a і b і виводить вірш, 
# в якому замість a і b використовуються ці значення.
'''
Вхідні дані:

A
B

Вихідні дані:

A and B sat in the tree.
A had fallen, B was stolen.
What's remaining in the tree?

'''
char_1 = input("Enter a string: ")
char_2 = input("Enter a string: ")
print(f"{char_1} and {char_2} sat in the tree.\n{char_1} had fallen, {char_2} was stolen.\nWhat's remaining in the tree?")