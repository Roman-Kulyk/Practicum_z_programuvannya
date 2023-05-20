# 358. Користувач вводить рядок одноцифрових чисел без пропусків. 
# Напишіть програму для обчислення суми цих чисел.
'''
Вхідні дані:
1239
88
01

Вихідні дані:
15
16
1
'''
sequence = input("Enter a string: ")
result = 0

for char in sequence:
    if char.isdigit():
        result += int(char)
print(result)