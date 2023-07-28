# Напишіть простий калькулятор, який зчитує три рядки, які вводить користувач: 
# перше число, друге число і операцію, після чого застосовує операцію до введених 
# числах («перше число» «операція» «друге число») і виводить результат на екран. 
# Підтримувані операції: +, -, /, *, mod, pow, div, де mod - це взяття залишку від 
# ділення, pow - піднесення до степеня, div - цілочисельне ділення. У випадку ділення 
# на 0, необхідно використати обробник винятку, який має вивести повідомлення 
# Division by zero!.

def calculator(num_1,num_2,operator):
    result = 0
    if operator == '+':
        result = num_1 + num_2
        return result

    elif operator == '-':
        result = num_1 - num_2
        return result
    
    elif operator == '*':
        result = num_1 * num_2
        return result
    
    elif operator == '/':
        result = num_1/num_2
        return result
    
    elif operator == '//':
        result = num_1//num_2
        return result  
    elif  operator == 'mod':
        result = num_1 % num_2
        return result
    
    elif operator == 'pow':
        result == num_1 ** num_2
        return result
    
    

print(calculator(4,5,'+'))
print(calculator(4,5,'-'))
print(calculator(4,5,'*'))
print(calculator(4,5,'/'))
print(calculator(4,5,'//'))
print(calculator(4,5,'mod'))
print(calculator(4,5,'pow'))