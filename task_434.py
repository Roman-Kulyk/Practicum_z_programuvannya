# 434. Напишіть програму для отримання частини рядка URL, що позначає назву ресурсу.
'''
Вхідні дані:
https://www.namesite.com/folder/index.html

Вихідні дані:
index.html
'''
txt = input("Enter your string: ")
lst = list(txt.split("/"))
print(lst[-1])