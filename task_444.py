# 444.  Напишіть програму, яка приймає послідовність слів, розділених комами і без 
# пропусків в якості введення, і друкує послідовність слів, розділених комами, після 
# сортування за алфавітом.
'''
Вхідні дані:
one,moment,please

Вихідні дані:
moment,one,please
'''
lst = []
lst = [(item) for item in input("Enter the list members: ").split(',')]
lst.sort()
for item in lst:
    print(item, end = ',')
print()