# 666. Напишіть функцію для сортування рядка слів, розділених пропусками, 
#за довжиною слів в порядку зростання.
'''
Вхідні дані:
Ruby Python Go JavaScript Java

Вихідні дані:
Go Java Ruby Python JavaScript
'''
def Sorting():
    lst = input('Enter your list members: ').split()
    lst.sort(key=len)
    for i in lst:
        print(i,end = ' ')
    print()   

Sorting()