#165. Напишіть програму простого калькулятора, яка зчитує введені користувачем три рядки: 
#перше число, друге число і арифметичну дію, після чого застосовує введену дію до введених числах і 
#виводить результат. 
#Калькулятор повинен підтримувати такі арифметичні дії як: +, -, /, *, mod (залишок від ділення), 
#pow (піднесення до степеня), div (цілочисельне ділення). Якщо виконується ділення і друге число дорівнює 0, 
#необхідно виводити рядок Division by 0!. Введені числа є дійсними.

a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
op = input("Enter an operator '+', '-', '*', '/', 'mod', 'pow', 'div': ")


if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Division by 0!")
    else:
        print(a / b)
elif op == "mod":
    if b == 0:
        print("Division by 0!")
    else:
        print(a % b)
elif op == "div":
    if b == 0:
        print("Division by 0!")
    else:
        print(a // b)
elif op == "pow":
    print(a ** b)
