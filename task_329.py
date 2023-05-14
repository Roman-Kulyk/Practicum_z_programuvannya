# 329.Напишіть програму, щоб у введеному користувачем рядку виконати 
# обмін місцями першого та останнього символів.
'''
Вхідні дані:

Hong Kong
Antarctica

Вихідні дані:

gong KonH
antarcticA

'''
word = input("Enter a word: ")
new_word = word[-1] + word[1:-1]+ word[0]
print(new_word)