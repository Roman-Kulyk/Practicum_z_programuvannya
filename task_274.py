# 274. Дано цілі числа a і b (a > b). Визначити результати цілочисельного ділення a на b і залишку 
# від ділення a на b, не використовуючи стандартні операції цілочисельного ділення і залишку від ділення. 
# Результати необхідно вивести в одному рядку, спочатку результат цілочисельного ділення, а потім залишок 
# від ділення, розділені одним пропуском.
'''
Вхідні дані:

16
5

Вихідні дані:

3 1

'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
num_list = []
while a > b:
    a = a - b
    num_list.append(a)
print(len(num_list), a)
