# 275. Дано натуральне число n. Визначити, чи є різниця його максимальної та мінімальної цифр парним числом.

'''
Вхідні дані:

2134389
1234

Вихідні дані:

True
False
'''
a = input("Enter a number: ")
#print(type(a))
a_list = list(a)
#print(a_list)
#print(type(a_list))
if (int(max(a_list)) - (int(min(a_list)))) % 2 == 0:
    print(True)
else:
    print(False)