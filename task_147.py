#147. Вводяться координати (x, y) точки A і радіус кола (r). Визначити, чи належить дана точка колу, 
#якщо його центр знаходиться в початку координат.

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
r = int(input("Enter a number: "))

if x <= r and y <= r:
    print("The point belongs to the circle")
else:
    print("The point is outside the circle")




    