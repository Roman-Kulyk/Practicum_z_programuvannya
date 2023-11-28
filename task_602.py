# 602. Напишіть програму, яка для двох послідовностей, що складаються з натуральних чисел, 
# що не перевершують n, буде визначати, які числа зустрічаються в кожній з послідовностей, 
# а які з чисел від 1 до n - в жодній з них. Спочатку на вхід програмі подається 
# число n (1 ≤ n ≤ 255). У другому рядку вхідних даних знаходяться елементи першої послідовності, 
# у третьому рядку - елементи другої послідовності. Виведіть у першому рядку в порядку зростання 
# без повторень числа, які зустрічаються в кожній з послідовностей, а у другому рядку - в порядку 
# зростання числа від 1 до 255, які не зустрічаються в жодній з них.
"""
Вхідні дані:
7
3 2 4 5 2
2 7 4 3 4 2

Вихідні дані:
2 3 4
1 6
"""
num = int(input("Enter your number n(1 ≤ n ≤ 255) : "))
lst_1 = [int(item) for item in input("Enter your list members: ").split()]
lst_2 = [int(item) for item in input("Enter your list members: ").split()]

set_1 = set(lst_1)
set_2 = set(lst_2)

newlist = [x for x in range(1,num)]
new_set = set(newlist)

inter_set = set_1.intersection(set_2) 
for _ in inter_set:
    print(_, end= ' ')
print()

union_set = set_1.union(set_2) 

differ_set = new_set.difference(union_set) 
for _ in differ_set:
    print(_, end= ' ')
print()
