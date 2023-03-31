#152. Прямокутник на площині, зі сторонами, паралельними координатним осям, заданий координатами лівої верхньої і 
#правої нижньої своїх вершин. Також дані координати точки. Усі координати - цілі числа. Визначити, чи належить 
#вказана точка заданому прямокутнику.

x1 = int(input("Enter a number: "))
y1 = int(input("Enter a number: "))
x2 = int(input("Enter a number: "))
y2 = int(input("Enter a number: "))
x5 = int(input("Enter a number: "))
y5 = int(input("Enter a number: "))

x4 = x1; x3 = x2; y4 = y1; y3 =y2

if x1 < x5 < x2 and y1 > y5 > y2:
    print("Yes")
else:
    print("No")