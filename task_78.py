#78.Отримати реверсний (в зворотному порядку) запис введеного користувачем
#трицифрового числа.

num = int(input('Enter a number: '))
last = num%100%10
middle  = num%100//10
first = num//100

print('{}{}{}'.format(last,middle,first))
