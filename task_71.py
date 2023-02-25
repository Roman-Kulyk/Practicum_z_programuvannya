#71.Напишіть програму для обчислення координат середини відрізка.
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

x = x2 - (x2 - x1)/2
y = y2 - (y2 - y1)/2

print(f"The midpoint's x value is: {x}".format(x))
print(f"The midpoint's y value is: {y}".format(y))


x = x1 + (x2 - x1)/2
y = y1 + (y2 - y1)/2

print(f"The midpoint's x value is: {x}".format(x))
print(f"The midpoint's y value is: {y}".format(y))
