#148. Дано натуральное число. Визначити, чи закінчується число парною цифрою.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("It is even number.")
else:
    print("The number is odd.")