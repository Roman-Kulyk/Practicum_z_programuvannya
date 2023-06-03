# 439. Напишіть простий інтерпретатор математичного виразу. На вхід подається рядок 
# з виразом, що складається з двох чисел (0 ≤ a, b ≤ 1000), об’єднаних бінарним 
# оператором: a operator b, де замість operator можуть використовуватися такі слова: 
# plus, minus, multiply, divide для, відповідно, додавання, віднімання, множення і 
# цілочисельного ділення. Результат обчислення - рядок, що містить ціле число.
'''
Вхідні дані:
20 plus 7
15 minus 9
144 multiply 2
49 divide 7

Вихідні дані:
27
6
288
7
'''
txt = input("Enter your expression: ")
x = txt.split()
#print(x) 
if x[1] == 'plus':
    print(int(x[0]) + int(x[-1]))
elif x[1] == 'minus':
    print(int(x[0]) - int(x[-1]))
elif x[1] == 'multiply':
    print(int(x[0]) * int(x[-1]))
elif x[1] == 'divide':
    print(int(x[0]) / int(x[-1]))


