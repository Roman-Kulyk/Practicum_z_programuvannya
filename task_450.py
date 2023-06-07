# 450. У введеному списку цілих чисел, знайдіть і надрукуйте сусідні елементи, 
# які мають однаковий знак. Якщо такої пари немає, не повинно нічого виводитися.
'''
Вхідні дані:
1 -2 -3 5 6 -3 7 8

Вихідні дані:
-2 -3
5 6
7 8
'''
lst = []
lst = [int(item) for item in input("Enter the list members: ").split()]

for item in range(len(lst)-1):
    if lst[item] * lst[item+1] > 0: #it checks if item have the same sign
        print(lst[item], lst[item+1]) #it print current and next numbers
    
