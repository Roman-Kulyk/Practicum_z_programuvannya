# 442. Дано послідовність цілих чисел. Визначте, у відсортованому за зростанням 
# списку, кількість елементів, що не повторюються один за одним.
'''
Вхідні дані:
1 9 10 3 7 5 2 2 3 0 4 5 6

Вихідні дані:
10
'''
lst = []
lst = [int(item) for item in input('Enter the list members: ').split()]
lst.sort()
cur = 0
prev = 0
qi_ty = 0
for i in lst:
    cur = i
    if cur != prev:
        qi_ty += 1
        prev = cur
if lst[0] == 0:
    print(qi_ty + 1)
else:
    print(qi_ty)