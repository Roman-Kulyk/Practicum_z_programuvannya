#98. Дано прямокутник з розмірами a x b мм. Скільки квадратів зі стороною c мм можна відрізати від нього? 
#Вхідні дані такі, що сторони прямокутника і квадрата є цілими числами. 
#Програма повинна вивести одне число: кількість квадратів, які можна відрізати від даного прямокутника.

a = int(input('Enter length: '))               #4
b = int(input('Enter width:'))                 #5 
c = int(input('Enter square\'s side: '))       #2
n = a // c * b // c
print(n)

