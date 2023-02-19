#Напишіть програму для запису і розв’язування виразу(a + b) * (a + b), де a і b
#- натуральні цілі числа.

a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
result = (a + b) * (a + b)
print(f'({a} + {b}) * ({a} + {b}) = {result}')
