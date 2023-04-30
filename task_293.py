# 293. Назвемо число паліндромом, якщо воно не змінюється при перестановці його 
# цифр у зворотному порядку. Напишіть програму, яка за введеною користувачем 
# кількістю n (1 ≤ n ≤ 100000) виводить кількість таких чисел-паліндромів, 
# які не перевищують n.
'''
Вхідні дані:

1
50
10

Вихідні дані:

1
13
9
'''
n = int(input("Enter a number: "))
pal_list = []#it initialize empty list
for i in range(1,n+1):
    b_i = str(i)#it changes variale type to str
    rb_i = b_i[::-1]#it returns a string in backward order
    if str(i) == rb_i:#it checks values of variables
        pal_list.append(i)#it adds member to the list
    else:
        continue
print(len(pal_list))