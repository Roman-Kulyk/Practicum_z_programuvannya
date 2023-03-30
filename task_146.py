#146. Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає, 
#яка із точок знаходиться далі від початку координат.
x1 = int(input('Enter a number: '))
y1 = int(input('Enter a number: '))
x2 = int(input('Enter a number: '))
y2 = int(input('Enter a number: '))

if x2 == x1 and y2 == y1:
    print('The distance is the same')
elif x1 >= x2 and y1 >= y2:
    print('A')
elif x2 >= x1 and y2 >= y1:
    print('B')

