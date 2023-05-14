# 328. Користувач вводить рядок, у якому чергуються цифри та інші символи. 
# На початку і у кінці рядка цифри відсутні. 
# Напишіть програму, яка друкує усі символи введеного рядка у тому ж порядку, 
# але без цифр.
'''
Вхідні дані:

H1e2l3l4o5w6o7r8l9d
i1m3p4o9r0t4 6t7h8i9s

Вихідні дані:

Helloworld
import this

'''
input_str = input("Enter a row: ")
result = []#it initialize empty list
for char in input_str:#it create cycle fof checking every char in input
    if not char.isdigit():#it checks if every char is a digit
        result.append(char)#if not adds it to list
print("".join(result))#it joins and print list with result