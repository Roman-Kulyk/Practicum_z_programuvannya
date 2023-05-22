# 366. Знайти у рядку зазначений підрядок і замінити його на новий. 
# Рядок, підрядок для заміни та новий рядок вводить користувач. 
# Розгляньте випадок заміни усіх підрядків. 
# Також необхідно врахувати випадок відсутності підрядка, 
# який необхідно замінити (вивести is impossible).
'''
Вхідні дані:
12 45 32 567 32 109
32
0
12 45 32 567 32 109
33
-1

Вихідні дані:
12 45 0 567 0 109
is impossible
'''
txt = input("Enter a string: ")
substr_1 = input("Enter a substring to find: ")
substr_2 = input("Enter a substring to input: ")
if substr_1 in txt:
    x = txt.replace(substr_1, substr_2)
    print(x) 
else:
    print("is impossible")