# 110. Дано маси і об’єми двох тіл, виготовлених з різних матеріалів (дійсні числа). 
#Матеріал якого з тіл має більшу густину? 
#Введення величин відбувається у такому порядку:m1, v1, m2, v2.

m1 = float(input('Enter a m1:'))
v1 = float(input('Enter a v1:'))
m2 = float(input('Enter a m2:'))
v2 = float(input('Enter a v2:'))
p1 = m1 / v1
p2 = m2 / v2

if p1 > p2:
    print('p1 is greater.')
else:
    print('p2 is greater.')