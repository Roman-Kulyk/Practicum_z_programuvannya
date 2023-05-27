# 376. Дано рядок і символ, який зустрічається у рядку принаймні два рази. 
# Напишіть програму, яка надрукує новий рядок (на основі введеного користувачем), 
# у якому послідовність символів, що містяться між першою і останньою появою введеного
# символа, буде записана у зворотному порядку.
'''
Вхідні дані:
Complex is better than complicated.
a

Вихідні дані:
Complex is better thacilpmoc nated.
'''
txt = input("Enter a string: ")
char = input("Enter a character to find: ")

x_1 = txt.find(char)

x_2 = txt.rfind(char)
print(txt[: x_1] + txt[x_2 : x_1 : -1] +txt[x_2 :])