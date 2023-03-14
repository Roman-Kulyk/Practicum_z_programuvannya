#113. Напишіть програму, яка запитує два цілих числа. Якщо добуток чисел перевищує їх суму, надрукувати добуток 
#чисел, у протилежному випадку - вивести їх суму. Якщо добуток дорівнює сумі, вивести різницю чисел.

num_1 = int(input('Enter a first number: '))
num_2 = int(input('Enter a second number: '))

if (num_1 * num_2) > (num_1 + num_2):
    print(num_1 * num_2)
elif (num_1 * num_2) == (num_1 + num_2):
    print(num_1 - num_2)
else:
    print(num_1 + num_2)