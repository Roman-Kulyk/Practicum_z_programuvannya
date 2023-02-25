#66.Вводиться число n, необхідно «відрізати« від нього k останніх цифр.
#Наприклад, при n = 123456 і k = 3 відповідь повинна бути 123.

n = int(input('Enter a number: '))
k = int(input('Enter a number: '))

n_truncated = n // pow(10,k)
print(n_truncated)
