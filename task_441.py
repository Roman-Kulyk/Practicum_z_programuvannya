# 441. Дано список цілих чисел. Визначте елемент у списку з найбільшим значенням. 
# Надрукувати значення найбільшого елемента, а потім номер індексу. 
# Якщо найбільший елемент не є унікальним, надрукуйте індекс першого входження 
# найбільшого елемента.
'''
Вхідні дані:

2 5 10 0 4 7 11 5 8

Вихідні дані:
11 6
'''
lst = []
lst = [int(item) for item in input("Enter the list members: ").split()]
maximum_value = max(lst)

x = lst.index(maximum_value) 
print(maximum_value, x)