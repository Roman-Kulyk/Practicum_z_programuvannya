# 475. Напишіть програму, яка приймає на вхід список чисел в одному рядку і 
# виводить на екран в один рядок значення, які повторюються в ньому більш ніж один раз. 
# Виведені числа не повинні повторюватися, порядок їх виведення маж бути за зростанням.
'''
Вхідні дані:
5 8 1 3 5 2 1 3 0
2 2 4 4 4 1

Вихідні дані:
1 3 5
2 4
'''
lst = [int(item) for item in input("Enter the list members: ").split()]
lst_to_print = []
for i in lst:
    if lst.count(i) > 1:
        if i not in lst_to_print:
            lst_to_print.append(i)
lst_to_print.sort()
for i in lst_to_print:
    print(i,end = ' ')
print()