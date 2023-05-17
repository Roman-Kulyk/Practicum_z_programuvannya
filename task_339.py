# 339. Дано вираз, який має один з наступних виглядів: 'A+B', 'A-B' або 'A*B', 
# де A і B - цілі числа від 0 до 1000000000. Визначте значення цього виразу.
'''
Вхідні дані:
3*3
50-49
33+16
Вихідні дані:
9
1
49
'''
expression = input("Enter an expression: ")
a,op,b = expression.split()
a,b = int(a),int(b)
if op =='+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
print(result)