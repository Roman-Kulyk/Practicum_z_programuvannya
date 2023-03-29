#140. Визначити, чи є число а дільником числа b або, навпаки, число b дільником числа a

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

if a % b == 0:
    print(True)
elif b % a == 0:
    print(True)
else:
    print(False)
