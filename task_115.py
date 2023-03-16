#115. Напишіть програму, яка зчитує два цілих числа a і b (від 1 до 1000) та виводить найбільше значення з них.

num_1 = int(input('Enter first number from 1 till 1000: '))
num_2 = int(input('Enter second number from 1 till 1000: '))

if num_1 > num_2:
    print(num_1)
else:
    print(num_2)