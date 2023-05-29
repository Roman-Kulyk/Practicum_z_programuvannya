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
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input('Enter an element: '))
    lst.append(ele) 
print(lst)

half_list = len(lst)//2
print(half_list)
print(lst[half_list:])
