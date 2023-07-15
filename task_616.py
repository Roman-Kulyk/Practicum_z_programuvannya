# 616. Напишіть функцію, яка отримує 3 аргументи: перші 2 - числа, 
# третій - операція (+, -, *, /), яка повинна бути проведена над ними. 
# У випадку невідомої операції, функція повертає рядок Unknown operation. 
# Результатом має бути дійсне число з двома знаками після десяткової крапки.
'''
Вхідні дані:
3
8
+

Вихідні дані:
11.00
'''
def calculator(var_1, var_2, oper):
    result = 0
    if oper == "+":
        result = var_1 + var_2
        
    elif oper == "-":
        result = var_1 - var_2
        
    elif oper == "*":
        result = var_1 * var_2
        
    elif oper == "/":
        result = var_1 / var_2
        
    else:
        result = "Unknown operation!"
        
    return result



print(calculator(3,8,'+'))
print(calculator(4,5,'*'))
print(calculator(4,9,'-'))
print(calculator(3,3,'/'))
print(calculator(2,2,'//'))