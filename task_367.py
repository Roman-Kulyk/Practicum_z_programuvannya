# 367. Напишіть програму, яка дає користувачеві можливість вводити рядок і 
# відображає символ, який найчастіше з’являється у рядку та кількість його входжень. 
# Якщо у рядку є кілька таких символів, необхідно врахувати лише перший з них.
'''
Вхідні дані:
Black Dog Appears and Disappears
I Go to Bristol

Вихідні дані:
a 5
пропуск 3
'''
string = input("Enter a string: ")
char_frequency = {}
for char in string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
most_common_char = max(char_frequency, key = char_frequency.get)
print("The most frequent char is '{}'-{}".format(most_common_char,char_frequency[most_common_char]))