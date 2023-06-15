# 477. Для введеної послідовності цілих чисел, вивести їх у списку так, 
# щоб парні елементи розташовувалися на початку списку, а непарні - в кінці.
'''
Вхідні дані:
2 5 7 8 9 10 12 32 5

Вихідні дані:
32 12 10 8 2 5 7 9 5
'''
lst = [int(item) for item in input("Enter the list members: ").split()]
lst_even = []
lst_odd = []
for item in lst:
    if item % 2 == 0:
        lst_even.append(item)
    else:
        lst_odd.append(item)

lst_even.reverse()
lst_even.extend(lst_odd)
for i in lst_even:
    print(i,end = ' ')
print()