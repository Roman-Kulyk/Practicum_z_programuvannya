# 669. Напишіть функцію, яка створює комбінацію двох послідовностей таким чином як у вихідних даних.
'''
Вхідні дані:
1 2 3 4 5
a b c d e

Вихідні дані:
1 a 2 b 3 c 4 d 5 e
'''
def sorted_func():
    lst_1 = [int(item) for item in input("Enter the list members: ").split()]
    lst_2 = input("Enter the list members: ").split()

    combined_lst = []
    for i in range(len(lst_1)):
        combined_lst.append(lst_1[i])
        combined_lst.append(lst_2[i])
        i +=1


    for i in combined_lst:
        print(i, end = ' ')
    print()
sorted_func()