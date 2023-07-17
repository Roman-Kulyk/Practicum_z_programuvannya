# 640. Напишіть функцію для визначення суми трьох цілих чисел. Якщо будь-які два 
# значення однакові, необхідно вивести нуль.
'''
Вхідні дані:
1 2 3
1 2 2

Вихідні дані:
6
0
'''
def remove_duplicates(*nums):
    remove_duplicates = []
    for i in nums:
        remove_duplicates.append(i)
            
    if remove_duplicates[0] == remove_duplicates[1]\
    or remove_duplicates[0] == remove_duplicates[2]\
    or remove_duplicates[1] == remove_duplicates[2]:
        print(0)
    else:
        print(sum(remove_duplicates))
                      

remove_duplicates(1, 2, 3)
remove_duplicates(1, 2, 2)