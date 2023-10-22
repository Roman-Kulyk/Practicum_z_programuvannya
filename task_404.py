# 404.Напишіть програму, яка визначає, чи є у введеному рядку десяткові цифри, і виводить 
# найбільше число, яке можна скласти з цих цифр. Провідних нулів у числі бути не повинно 
# (за винятком числа 0, запис якого містить рівно одну цифру). Гарантовано, що у рядку є 
# принаймні одна цифра. Вхідний рядок містить довільні символи. Програма повинна вивести 
# найбільше число, яке можна скласти з присутніх в рядку десяткових цифр.
"""
Вхідні дані:
Release Date: July 27, 2008
Last Updated: February 22, 2018

Вихідні дані:
872200
822210
"""
text = input("Enter your text: ")
num_list = []#it initialize empty list

for i in text:#it checks if a char in string is digit
    if i.isdigit():
        num_list.append(int(i))#if so adds digit to the num_list

num_list.sort(reverse=True)#it sorts digits in descending order
digit_string = ''#it initializes an empty string

for i in num_list:#it takes every char in num_list
    digit_string += str(i)#and adds it to the string
print(digit_string)#it prints string