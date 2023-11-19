# 584. Напишіть програму, яка приймає на вхід список цілих чисел, розділених пропуском, 
# і виводить на екран значення, які повторюються в ньому більш ніж один раз. При виведенні 
# числа не повинні повторюватися, порядок виведення може бути довільним.
"""
Вхідні дані:
4 6 10 14 6 9 10 11

Вихідні дані:
6 10
"""
lst = [int(item) for item in input("Enter your list members: ").split()]
string = []
for i in lst:
    if i not in string and lst.count(i) > 1:
        string.append(i)
        #print(i)
    else:
        continue

for i in string:
    print(i, end=" ")
print()