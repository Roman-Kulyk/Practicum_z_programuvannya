#133. Залежно від розміру суми, розмір податку з неї розраховується за такою схемою: якщо сума не перевищує деяку 
#величину a, то податок не вираховується; якщо сума більша за a, але не перевищує b, то податок становить 10%; 
#якщо сума більша за b, але не перевищує c, то податок становить 25%; якщо сума більша c, то податок становить 50%. 
#Визначити, який податок (дійсне число) буде вираховано із суми розміром s. 
#Дані (цілі числа) вводяться в такому порядку: a, b, c, s.

a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number: '))
s = int(input('Enter a number: '))

if s < a:
    print('There is no any taxes!')
elif a < s < b:
    tax = s * 0.1
elif b < s < c:
    tax = s * 0.25
else:
    tax = s * 0.5
print(tax)