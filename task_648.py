# 648. Дано чотири дійсних числа: x1, y1, x2, y2. Напишіть функцію 
# distance(x1, y1, x2, y2), яка обчислює відстань між точкою (x1, y1) і (x2, y2). 
# Введіть чотири дійсних числа і виведіть результат роботи цієї функції.
'''
Вхідні дані:
0
0
1
1

Вихідні дані:
1.41421
'''
def find_distance(x1,y1,x2,y2):
    distance = ((x2 - x1) ** 2 + (y2 -y1) ** 2)**0.5
    print(f'{distance:.5f}')

find_distance(0,0,1,1)