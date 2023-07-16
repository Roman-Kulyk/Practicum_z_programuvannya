# 635. Напишіть функцію, яка приймає послідовність чисел як у вхідних даних і 
# створює список лише з першого та останнього елементів.
'''
Вхідні дані:
5 16 72 29 11 217 112

Вихідні дані:
[5, 112]
'''
def list_function(*nums):
    list_function = []
    list_to_print = []
    for i in nums:
        list_function.append(i)
    
    list_to_print.append(list_function[0])
    list_to_print.append(list_function[-1])
    print(list_to_print)


list_function(5, 16, 72, 29, 11, 217, 112)