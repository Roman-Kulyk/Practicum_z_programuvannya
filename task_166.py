#166. Дано два натуральних числа n і m. Якщо одне з них ділиться на інше без остачі, виведіть 1, 
#інакше виведіть будь-яке інше ціле число.

n = int(input("Enter a number: "))
m = int(input("Enter a number: "))

if n % m == 0 or m % n == 0:
    print(1)
else:
    print(2)