#169. Напишіть програму, у яку вводяться трицифрове ціле число і цифра. 
#Необхідно визначити, чи входить у число введена цифра.

num = int(input("Enter a number:"))
fig = int(input("Enter a figure: "))

f = num // 100
s = num % 100 // 10
t = num % 100 % 10

if f == fig or s == fig or t == fig:
    print(True)
else:
    print(False)