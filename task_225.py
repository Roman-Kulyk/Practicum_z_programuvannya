# 225.Напишіть програму для створення таблиці множення (від 1 до 10) для введеного цілого числа n.

num = int(input("Enter a number: "))
for i in range(1,11):
    mul = i * num
    print(f'{i} * {num} = {mul}'.format(i,num,mul))