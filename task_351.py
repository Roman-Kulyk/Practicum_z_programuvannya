# 351. Дано послідовність символів, що має вигляд p1*p2*...*pn, де pn - цифра. 
# Обчисліть значення виразу.
'''
Вхідні дані:
2*5*7

Вихідні дані:
70
'''
sequence = input("Enter a string: ")
result = 1

for char in sequence:
    if char.isdigit():
        result *= int(char)
print(result)