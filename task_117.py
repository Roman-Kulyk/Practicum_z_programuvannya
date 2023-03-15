#117. Дано три цілих числа. Визначте, скільки серед них збігаються. Програма повинна вивести одне з чисел: 
#3 (якщо усі однакові), 2 (якщо два однакові) або 0 (якщо усі числа різні).

num_1 = int(input('Enter first number: '))
num_2 = int(input('Eneter second number: '))
num_3 = int(input('Enter third number: '))

if num_1 == num_2 == num_3:
    print(3)
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print(2)
else:
    print(1)