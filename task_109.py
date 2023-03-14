# 109. Дано радіус кола і сторона квадрата (дійсні числа). У якої фігури площа більше?

r = float(input('Enter a radius: '))
a = float(input('Enter a value: '))

s_1 = 3.14 * r ** 2 
s_2 = a * a

if s_1 > s_2:
    print('Circle is greater.')
else:
    print('Square is greater.')