# 449. Для списку цілих чисел знайдіть і надрукуйте елементи, які з’являються у 
# списку лише один раз. Елементи повинні бути роздруковані у тому порядку, в якому 
# вони перебувають у вхідному списку.
'''
Вхідні дані:
5 3 1 6 5 8 0 12
1 45 23 45 90 1 0

Вихідні дані:
3 1 6 8 0 12
23 90 0
'''
lst = []
lst = [int(item) for item in input("Enter the list members: ").split()]

lst_origin = []
for item in lst:
    if lst.count(item) == 1:
        lst_origin.append(item)
for item in lst_origin:
    print(item, end = " ")
print()