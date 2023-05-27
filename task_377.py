# 377. Користувачем вводиться рядок і буква, що зустрічається у рядку принаймні 
# три рази. Напишіть програму, яка замінить кожне входження букви у нижньому регістрі 
# на цю ж букву у верхньому регістрі, за винятком першого і останнього.
'''
Вхідні дані:
There should be one-- and preferably only one --obvious way to do it.
n

Вихідні дані:
There should be one-- aNd preferably oNly one --obvious way to do it.
'''
txt = input("Enter a string: ")
char = input("Enter a character to find: ")

x_1 = txt.find(char)

x_2 = txt.rfind(char)

print(txt[: x_1] + txt[x_1 : x_2].replace(char,char.swapcase()) +txt[x_2 :])