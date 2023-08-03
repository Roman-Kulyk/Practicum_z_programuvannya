# 662. Напишіть функцію, яка отримує послідовність балів (цілі числа) і повертає 
#буквенну інтерпретацію числових балів на основі наступної шкали оцінок:
# 90-100 - A
# 80-89 - B
# 70-79 - C
# 60-69 - D
# Нижче 60 - F
'''
Вхідні дані:
60 80 64 45 35 87 90 95 91 64 78

Вихідні дані:
{'A': [90, 95, 91], 'B': [80, 87], 'C': [78], 'D': [60, 64, 64], 'F': [45, 35]}
'''
def fun_value():
    lst = [int(item) for item in input("Enter the list members: ").split()]
    dict = {}
    a_list = []
    b_list = []
    c_list = []
    d_list = []
    f_list = []
    for i in lst:
        if 100 > i >= 90:
            a_list.append(i)
        elif 89 > i >= 80:
            b_list.append(i)
        elif 79 > i >= 70:
            c_list.append(i)
        elif 69 > i >= 60:
            d_list.append(i)
        elif 60 > i:
            f_list.append(i)

    dict['A'] = a_list
    dict['B'] = b_list
    dict['C'] = c_list
    dict['D'] = d_list
    dict['F'] = f_list

    print(dict)

fun_value()