#43.Напишіть програму для друку повідомлення: «Значення змінної назва змінної
#дорівнює значення змінної, а її тип тип змінної.» Значення змінної вводять з
#клавіатури і у повідомленні виводиться у лапках.

a = input('Enter value of a: ')
b = int(input('Enter value of b: '))
c = float(input('Enter value of c: '))

print(f'Value of a is {a}, and its type {type(a)}.')
print(f'Value of b is {b}, and its type {type(b)}.')
print(f'Value of c is {c}, and its type {type(c)}.')
