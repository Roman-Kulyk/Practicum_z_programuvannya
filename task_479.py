# 479. Робот може рухатися, починаючи від початкової точки (0, 0), вгору, вниз, 
# вліво та вправо за допомогою кроків, наприклад:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Назви вказують напрямок, а цифри позначають кількість кроків. 
# Введення порожнього рядка завершує рух робота. 
# Напишіть програму для обчислення відстані від поточної позиції робота 
# до початкової точки.
'''
Вхідні дані:
UP 5
DOWN 3
LEFT 3
RIGHT 2

Вихідні дані:
2
'''
horizontal = 0
vertical = 0
distance = 0

while True:
    lst = input("Enter the list members: ").split()
    if lst == []:
        break
    else:
        if lst[0] == 'UP':
            vertical += int(lst[1])
        elif lst[0] == 'DOWN':
            vertical -= int(lst[1])
        elif lst[0] == 'RIGHT':
            horizontal += int(lst[1])
        elif lst[0] == 'LEFT':
            horizontal -= int(lst[1])
            
distance = (horizontal ** 2 + vertical ** 2) **0.5
print(distance)


