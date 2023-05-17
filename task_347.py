# 347.Напишіть програму для розрахунку довжини рядка без використання функції len().
'''
Вхідні дані:
pythonguide.pp.ua
Вихідні дані:
17
'''
a = input("Enter a string: ")

count = 0

while True:
    try:
        if a[count]:
            count += 1
    except IndexError as e:
        break

print(count)