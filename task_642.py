# 642. Напишіть функцію, яка приймає послідовність слів, розділених за допомогою 
# дефісу і друкує слова в послідовності, розділеній за допомогою дефісу, 
# після сортування за алфавітом.
'''
Вхідні дані:
one-two-three-four-five-six-seven

Вихідні дані:
five-four-one-seven-six-three-two
'''
def list_function():
    lst = input("Enter the list members: ").split('-')
    lst.sort()
    lst = '-'.join(lst)

    print(lst)

list_function()