# 292. Назвемо число паліндромом, якщо воно не змінюється при перестановці його 
# цифр у зворотному порядку. Напишіть програму, яка за введеним користувачем числом 
# n (1 ≤ n ≤ 100000) виводить числа-паліндроми, які не перевищують n.
'''
Вхідні дані:

50

Вихідні дані:

1
2
3
4
5
6
7
8
9
11
22
33
44
'''
n = int(input("Enter a number: "))
for i in range(0,n):
    b_i = str(i)#it changes variale type to str
    rb_i = b_i[::-1]#it returns a string in backward order
    if str(i) == rb_i:#it checks values of variables
        print(i)#it prints it if they are equal
    else:
        continue
