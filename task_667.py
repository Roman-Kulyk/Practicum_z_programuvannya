# 667. Напишіть функцію для сортування рядка слів, розділених пропусками, 
# за довжиною слів в порядку зменшення.
'''
Вхідні дані:
Ruby Python Go JavaScript Java

Вихідні дані:
JavaScript Python Java Ruby Go
'''
def Sorting():
    lst = input('Enter your list members: ').split()
    lst.sort(key=len, reverse=True)
    for i in lst:
        print(i,end = ' ')
    print()   

Sorting()