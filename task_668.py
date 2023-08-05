# 668.Напишіть функцію, яка створює комбінацію із двох послідовностей цілих чисел, 
# впорядковану за зростанням.
'''
Вхідні дані:
1 4 0 12 4 5
24 1 2 10 8

Вихідні дані:
0 1 1 2 4 4 5 8 10 12 24
'''
def sorted_func():
    lst_1 = [int(item) for item in input("Enter the list members: ").split()]
    lst_2 = [int(item) for item in input("Enter the list members: ").split()]
    combined_lst = lst_1 + lst_2
    srt_lst = (sorted(combined_lst))
    for i in srt_lst:
        print(i, end = ' ')
    print()
sorted_func()