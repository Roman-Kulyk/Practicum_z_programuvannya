# 405. Створіть список на основі введеної послідовності цілих чисел і надрукуйте 
# другу половину списку як у вихідних даних.
'''
Вхідні дані:
7 2 1 0 4 2 5
7 2 1 0 4 2

Вихідні дані:
0 4 2 5
0 4 2
'''
lst = []
lst = [int(item) for item in input("Enter the list items : ").split()]
print(lst)

half_list = len(lst)//2
print(half_list)
for i in lst[half_list:]:
    print(i, end = " ")
print()
