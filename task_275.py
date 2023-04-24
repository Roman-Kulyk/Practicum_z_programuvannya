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
a_list = list(a) #turn a string into a list
if (int(max(a_list)) - (int(min(a_list)))) % 2 == 0: #takes a max and min member of the list
    print(True)
else:
    print(False)