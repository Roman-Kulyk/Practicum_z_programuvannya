# 641. Напишіть функцію для перевірки наявності одного списку у іншому списку. 
#Cписки містять принаймні по одному елементу.
'''
Вхідні дані:
2 6 8 4 9 1
4 9
2 6 8 4 9 1
9 4

Вихідні дані:
True
False
'''
def if_list_in_list():
    lst_1 = input("Enter your list members: ")
    lst_2 = input("Enter your list 2 members: ")
    if lst_2 in lst_1:
        print(True)
    else:
        print(False)


if_list_in_list()