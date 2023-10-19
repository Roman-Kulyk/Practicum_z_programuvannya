# 401. Дано рядок, що містить одне або більше цілих чисел від 0 до 1000000000, розділених 
# знаками + або -. Розрахуйте значення цього виразу.
"""
Вхідні дані:
12-5+3
26-14+2-1
7-0+3

Вихідні дані:
10
13
10
"""
def calculate_expression(expression):
    result = 0
    current_number = 0
    sign = 1

    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == '+':
            result += sign * current_number
            current_number = 0
            sign = 1

        elif char == '-':
            result += sign * current_number
            current_number = 0
            sign = -1

    result += sign * current_number
    return result

expression = input("Enter your expression: ")
result  = calculate_expression(expression)
print(result)
