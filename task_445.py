# 445. Для введеної послідовності унікальних цілих чисел, поміняйте місцями 
# мінімальний та максимальний елементи цієї послідовності. 
# Надрукуйте отриманий список.
'''
Вхідні дані:
1 9 12 5 3 8

Вихідні дані:
12 9 1 5 3 8
'''
lst = []
lst = [int(item) for item in input("Enter the list members: ").split()]

min_index = lst.index(min(lst))#it founds index of minimum list's member
max_index = lst.index(max(lst))#it founds index of maximum list's member

lst[min_index],lst[max_index] = lst[max_index],lst[min_index]#it changes their order

for item in lst:# it prints every list members 
    print(item, end = " ")#in the same row with space as separator
print()