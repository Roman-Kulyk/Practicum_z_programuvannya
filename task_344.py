# 344. Напишіть програму для друку таблиці індексів і значень символів у 
# введеному користувачем рядку.
'''
Вхідні дані:
Ruby
Вихідні дані:
0 R
1 u
2 b
3 y
'''
txt = input("Enter a string: ")
for index,char in enumerate(txt):#it returns an enumerate object.
    print(index, char)