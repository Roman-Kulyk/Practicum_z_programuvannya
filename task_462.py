# 462.  Напишіть програму, яка обчислює частку студентів, які отримали оцінку A. 
# Використовується п’ятибальна система оцінювання з оцінками A, B, C, D, F. 
# Вводиться рядок, в якому через пропуск записані оцінки студентів. 
# Оцінок завжди не менш однієї. 
# Виводиться дробове число з рівно двома знаками після коми.
'''
Вхідні дані:
A B A A B C A D F
A A A A A
A F
B B C B F F B C F

Вихідні дані:
0.44
1.00
0.50
0.00
'''
lst = input("Enter the list members: ").split()
lenght = len(lst)
percentage = lst.count('A') / lenght
print(f'{percentage:.2f}')