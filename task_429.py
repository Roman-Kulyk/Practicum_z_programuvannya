# 429. Напишіть програму для підрахунку кількості днів, в яких температура була не 
# нижче, ніж середня температура за весь період. У першому рядку вводиться список 
# показників температури на кожен день. У рядку виведення одне число - кількість днів, 
# які відповідають умові.
'''
Вхідні дані:
-3 -1 0 2 6 8 12 15

Вихідні дані:
4
'''
lst = []
lst = [int(item) for item in input("Enter the list members: ").split()]
average = sum(lst)/len(lst)

total_day_greater = 0
for item in lst:
    if item > average:
        total_day_greater+=1
print(total_day_greater)