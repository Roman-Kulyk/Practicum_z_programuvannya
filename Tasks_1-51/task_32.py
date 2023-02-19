#32.Вводяться три додатних числа - довжини сторін трикутника. Обчисліть площу
#трикутника за формулою Герона.
#S=√p(p-a)(p-b)(p-c), (де р=(а+ b +с)/2 - півпериметр).
a=int(input('Enter a number: '))
b=int(input('Enter a number: '))
c=int(input('Enter a number: '))
p=(a+b+c)/2
S=pow((p*(p-a)*(p-b)*(p-c)),0.5)
print(S)
