# 460. Вводиться список цілих чисел. Всі числа списку знаходяться на одному рядку. 
# У списку всі елементи різні. Поміняйте місцями мінімальний і максимальний елементи 
# цього списку.
'''
Вхідні дані:
5 6 8 1 4 9 12

Вихідні дані:
5 6 8 12 4 9 1
'''
lst = [int(item) for item in input("Enter the list members: ").split()] #it initialize the list

max_index = lst.index(max(lst)) #it founds index of max element

min_index = lst.index(min(lst)) #it founds index of min element

lst[min_index],lst[max_index] = lst[max_index], lst[min_index] #it reassingn mix with min value

for item in lst:
    print(item, end = " ")
print()