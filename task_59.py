#59.Вводиться додатне ціле трицифрове число. Знайти суму цифр числа.

num = int(input('Enter a number: '))
total = num//100 + num%100//10 + num%10
print(total)
