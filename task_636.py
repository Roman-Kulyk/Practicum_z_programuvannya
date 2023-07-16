# 636. Напишіть програму, і створіть в ній дві функції. Перша з них - приймає 
# послідовність цілих чисел і повертає список. Друга - повертає новий список, 
# що містить всі елементи першого списку без дублікатів.
'''
Вхідні дані:
5 16 5 29 11 217 11

Вихідні дані:
[5, 11, 16, 217, 29]
'''
def remove_duplicates(*nums):
    remove_duplicates = []
    for i in nums:
        if i not in remove_duplicates:
            remove_duplicates.append(i)
    print(remove_duplicates)

remove_duplicates(5, 16, 5, 29, 11, 217, 11)